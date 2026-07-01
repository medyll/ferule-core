# Overthinking — Lessons Learned

> **Date:** 2026-04-17  
> **Context:** core-ferule-engine V1 bootstrap  

---

## What Was Overthought

### 1. Cron Hooks

**Added:** `interfaces/hooks/cron_health_hook.yaml`, `cron_health_check.yaml`

**Why unnecessary:** La ferule n'a pas besoin de santé autonome. Le watchdog suffit.

**Lesson:** Pas de services background — la ferule est **passive**, déclenchée par missions.

---

### 2. Redis Event Listener

**Added:** `interfaces/events/listener.py` (5.6KB)

**Why unnecessary:** File bus polling suffit pour V1. Redis ajoute de la complexité sans valeur.

**Lesson:** Start simple — file-based first, events later if needed.

---

### 3. Complex Hook Triggers

**Added:** 3 trigger types (data_field, event, cron)

**Why unnecessary:** **data_field** suffit pour V1. Les events et cron sont de l'anticipation prématurée.

**Lesson:** One trigger type at a time.

---

### 4. Multiple Action Types

**Added:** `log`, `route`, `hook`

**Why unnecessary:** **route** est l'action principale. `log` est du debug. `hook` est redundant.

**Lesson:** Route first, log second, hooks never (for V1).

---

### 5. REST API Complexity

**Added:** 4 endpoints (`/health`, `/skills`, `/metrics`, `/process`), Pydantic models, error handlers

**Why unnecessary:** File bus polling est le primary trigger. L'API est un nice-to-have, pas un must-have.

**Lesson:** File-first, API-second.

---

## What core-ferule-engine Should Be (V1)

### Simple Architecture

```
core-ferule-engine/
├── run_engine.py          # File bus poller + router
├── requirements.txt       # fastapi, pyyaml, jinja2
├── config/
│   └── rules_config.yaml  # input_dir, output_dir
├── core/
│   └── rules/             # YAML rules (condition → route)
└── skill/
    └── ferule-core/       # Entry point (routing only)
```

### Simple Flow

```
1. Place de Grève écrit mission → place-de-greve/missions/
2. Engine poll (5s) → lit mission
3. Engine évalue rules → trouve target
4. Engine écrit → ferule-core/results/routed-<id>.json
5. Core-squad lit结果 → exécute
```

### What's NOT Needed (V1)

- ❌ Cron hooks
- ❌ Redis events
- ❌ Event hooks
- ❌ Hook actions
- ❌ `/metrics`, `/skills` endpoints
- ❌ Pydantic validation models
- ❌ Error handlers
- ❌ Watchdog listener (watchdog se débrouille seul)

---

## Principle

**File-based, passive, simple.**

La ferule engine:
- ✅ Polls un dossier
- ✅ Lit des YAML rules
- ✅ Route vers une cible
- ✅ Écrit un fichier résultat

C'est tout.

---

*Documenté pour ne pas re-refaire les mêmes erreurs.*
