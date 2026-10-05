# PHASE 1 — Setup & File Bus Integration

> Establish the Python engine, base YAML rules, and file-based communication with mission-queue.

---

### 1.1 — Python Engine Bootstrap

**File:** `core/engine.py`
**Problem:** Engine does not exist yet — no rule loading, no polling loop.
**Risk:** Nothing runs without this. All other phases depend on it.

- [x] Create `core/engine.py` with `RuleEngine` class
- [x] Implement YAML rule loader (`os.walk` from `core/rules/`)
- [x] Implement Jinja2 condition evaluator (no `eval()`)
- [x] Implement action dispatcher (`route`, `log`, `hook`)
- [x] Add `asyncio` polling loop (5s interval)

**Effort:** 90 min

---

### 1.2 — Base YAML Rules

**File:** `core/rules/default/filter_rule.yaml`, `core/rules/default/route_to_llm.yaml`
**Problem:** No rules defined — engine loads nothing on first start.
**Risk:** Silent no-op on all incoming missions.

- [x] Validate `filter_rule.yaml` against engine loader
- [x] Validate `route_to_llm.yaml` against engine loader
- [ ] Add at least one rule per domain prefix (DEV-, AUTH-, CAP-)

**Effort:** 30 min

---

### 1.3 — File Bus with mission-queue

**File:** `config/rules_config.yaml`, `core/engine.py`
**Problem:** No polling of `mission-queue/missions/` implemented.
**Risk:** Engine never receives missions — fully deaf.

- [x] Configure `file_bus.input_dir` in `rules_config.yaml`
- [x] Implement file scanner in engine (consume on read)
- [x] Write processed result to `ferule-core/results/`
- [x] Add structured logging on each mission consumed

**Effort:** 45 min

---

### 1.4 — Skill Discovery

**File:** `skill/core-ferule-engine/SKILL.md`
**Problem:** Skill file exists but engine doesn't load it at startup.
**Risk:** Internal agents cannot discover capabilities.

- [x] Implement `os.walk` skill loader in `RuleEngine.__init__`
- [x] Expose loaded skills via internal registry (dict)

**Effort:** 20 min

---

### 1.5 — Requirements & Quick Start

**File:** `requirements.txt`, `scripts/start.ps1`
**Problem:** No dependency file, no quick-start script.
**Risk:** Onboarding and testing blocked.

- [x] Create `requirements.txt` (fastapi, uvicorn, jinja2, pyyaml, httpx)
- [x] Create `scripts/start.ps1` for local testing

**Effort:** 15 min
