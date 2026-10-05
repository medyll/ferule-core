# Core Ferule Engine — Component Documentation

> **Version:** v1-core-ferule-engine  
> **Date:** 2026-04-17  

---

## Architecture (V1 Minimal)

```
core-ferule-engine/
├── run_engine.py              # File bus poller + router
├── requirements.txt           # Python dependencies
├── config/
│   └── rules_config.yaml      # Engine configuration
├── core/
│   └── rules/                 # YAML rules (condition → route)
└── skill/
    └── ferule-core/           # Entry point skill
```

**Removed (Overthinking):**
- `core/models/` — Inline dans engine.py
- `core/workflows/` — Pas de workflows V1
- `interfaces/` — Pas d'interfaces V1
- Cron hooks, Redis events, Event hooks

---

## 1. Python Engine

### Role

**File bus poller** — lit missions, évalue rules, écrit résultats.

### Flow

```
1. Poll `mission-queue/missions/` (5s)
2. Lit mission JSON/YAML
3. Évalue rules (Jinja2 conditions)
4. Écrit `ferule-core/results/routed-<id>.json`
```

### Configuration

```yaml
file_bus:
  input_dir: "mission-queue/missions"
  output_dir: "ferule-core/results"
  poll_interval_seconds: 5
```

### API (Optional)

| Endpoint | Purpose |
|----------|---------|
| `/health` | Status |
| `/process` | Direct processing |

---

## 2. Core Rules

### Structure

```yaml
name: rule_name
condition: "data.priority > 1"
actions:
  - type: route
    target: "core-standard"
    payload: "{{data}}"
```

### Default Rules

| File | Purpose |
|------|---------|
| `filter_rule.yaml` | Filtre low-priority |
| `route_to_domain.yaml` | Route par domain |

---

## 3. Entry Point Skill

### Routing

| Intent | Target |
|--------|--------|
| Norme | `core-standard/` |
| Incidents | `incidents/` |

---

## Quick Start

```bash
cd core-ferule-engine
pip install -r requirements.txt
python run_engine.py
```

---

*See OVERTHINKING.md for lessons learned.*
