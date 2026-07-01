"""
core/engine.py — Core Ferule Engine
Rule engine: load YAML rules, evaluate Jinja2 conditions, dispatch actions.
"""

import json
import logging
import os
import time
from pathlib import Path
from typing import Any, Dict, List

import yaml
from jinja2 import Environment, BaseLoader, TemplateError
from jinja2.sandbox import SandboxedEnvironment

# ── Paths ────────────────────────────────────────────────────────────────────

ENGINE_DIR = Path(__file__).parent                    # core/
FERULE_DIR = ENGINE_DIR.parent                        # core-ferule-engine/
WORKSPACE   = FERULE_DIR.parent.parent.parent         # workspace/

CONFIG_PATH = FERULE_DIR / "config" / "rules_config.yaml"
RULES_DIR   = ENGINE_DIR / "rules"

# ── Config ───────────────────────────────────────────────────────────────────

def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

CONFIG = load_config()

# ── Logging ───────────────────────────────────────────────────────────────────

log_path = Path(os.path.expandvars(CONFIG["logging"]["file"]))
log_path.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=getattr(logging, CONFIG["logging"]["level"], logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    handlers=[
        logging.FileHandler(log_path, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("core-ferule-engine")

# ── Jinja2 sandbox ────────────────────────────────────────────────────────────

_jinja_env = SandboxedEnvironment(loader=BaseLoader())


def evaluate_condition(condition: str, data: dict) -> bool:
    """Evaluate a Jinja2 condition string against data. No eval()."""
    try:
        template = _jinja_env.from_string("{% if " + condition + " %}1{% else %}0{% endif %}")
        result = template.render(data=_DotDict(data))
        return result.strip() == "1"
    except TemplateError as exc:
        logger.warning("Condition eval error (%s): %s", condition, exc)
        return False


def render_template(text: str, data: dict) -> str:
    try:
        return _jinja_env.from_string(text).render(data=_DotDict(data))
    except TemplateError as exc:
        logger.warning("Template render error: %s", exc)
        return text


class _DotDict:
    """Wraps a dict for attribute-style access in Jinja2 conditions."""
    def __init__(self, d: dict):
        self._d = d

    def __getattr__(self, key: str):
        val = self._d.get(key)
        if isinstance(val, dict):
            return _DotDict(val)
        return val

    def __contains__(self, key: str):
        return key in self._d

    def __repr__(self):
        return repr(self._d)


# ── Rule Engine ───────────────────────────────────────────────────────────────

class RuleEngine:
    """
    Pure YAML rule engine.
    
    Loads rules from YAML files, evaluates Jinja2 conditions,
    and executes actions (log, route).
    
    No hooks, no cron, no events, no API, no file bus.
    """
    
    def __init__(self):
        self.rules: List[Dict] = []
        self._load_rules()

    def _load_rules(self):
        """Load all YAML rules from RULES_DIR."""
        self.rules = []
        if not RULES_DIR.exists():
            logger.warning("Rules directory not found: %s", RULES_DIR)
            return
        for root, _, files in os.walk(RULES_DIR):
            for fname in files:
                if fname.endswith(".yaml") or fname.endswith(".yml"):
                    path = Path(root) / fname
                    try:
                        with open(path, encoding="utf-8") as f:
                            rule = yaml.safe_load(f)
                        if rule and "condition" in rule:
                            self.rules.append(rule)
                            logger.debug("Rule loaded: %s", rule.get("name", fname))
                    except Exception as exc:
                        logger.error("Failed to load rule %s: %s", path, exc)
        logger.info("Rules loaded: %d", len(self.rules))

    def process(self, request: dict) -> dict:
        """
        Apply all matching rules to a request.
        
        Returns summary of actions taken.
        """
        actions_taken = []
        for rule in self.rules:
            condition = rule.get("condition", "")
            try:
                matched = evaluate_condition(condition, request)
            except Exception as exc:
                logger.error("Rule '%s' condition error: %s", rule.get("name"), exc)
                continue

            if matched:
                logger.info("Rule '%s' matched request %s", rule.get("name"), request.get("id", "?"))
                for action in rule.get("actions", []):
                    result = self._dispatch_action(action, request)
                    actions_taken.append(result)

        return {"request_id": request.get("id"), "actions": actions_taken}

    def _dispatch_action(self, action: dict, request: dict) -> dict:
        """Dispatch a single action."""
        atype = action.get("type")
        
        if atype == "log":
            message = render_template(action.get("message", ""), request)
            level = action.get("level", "info").upper()
            getattr(logger, level.lower(), logger.info)(message)
            return {"type": "log", "message": message}

        elif atype == "route":
            return self._route(action, request)

        else:
            logger.warning("Unknown action type: %s", atype)
            return {"type": "unknown", "raw": action}

    def _route(self, action: dict, request: dict) -> dict:
        """Route a request to a target."""
        target = action.get("target", "")
        payload = render_template(str(action.get("payload", "")), request)
        metadata = action.get("metadata", {})

        output_dir = WORKSPACE / CONFIG.get("output_dir", "output")
        output_dir.mkdir(parents=True, exist_ok=True)
        out_file = output_dir / f"routed-{request.get('id', 'unknown')}-{int(time.time())}.json"
        route_doc = {
            "request_id": request.get("id"),
            "target": target,
            "request": {
                "id": request.get("id"),
                "demand": request.get("demand"),
            },
            "response": {
                "domain": metadata.get("domain"),
                "group": metadata.get("group"),
                "title": metadata.get("title"),
                "priority": request.get("priority"),
                "metadata": metadata.get("extra"),
            },
            "routed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        out_file.write_text(json.dumps(route_doc, indent=2, ensure_ascii=False), encoding="utf-8")
        logger.info("Routed request %s → %s → %s", request.get("id"), target, out_file.name)
        return {"type": "route", "target": target, "out_file": str(out_file)}
