# v1-core-ferule-engine

> **Version:** v1-core-ferule-engine
> **Date:** 2026-04-17
> **Status:** ✅ Documentation complete

---

## Overview

**Execution engine** — route les missions vers les ferules compétentes.

**Separation of Concerns:**
- `core-standard` → **What** (norms)
- `core-ferule-engine` → **How** (execution)

## Key Files

| File | Role |
|------|------|
| `llms.txt` | LLM context |
| `README.md` | This file |
| `USER-NOTES.md` | LLM preferences |
| `COMPONENTS.md` | Component documentation |

## Status

| Component | Status |
|-----------|--------|
| `run_engine.py` | ✅ Documented |
| `core/rules/` | ✅ Documented |
| `core/models/` | ✅ Documented |
| `core/workflows/` | ✅ Documented (empty) |
| `interfaces/` | ✅ Documented |
| `nexus-protocol/` | ✅ Documented |
| `skill/ferule-core/` | ✅ Created |

## Quick Start

```bash
cd core-ferule-engine
pip install -r requirements.txt
python run_engine.py
curl http://localhost:8000/health
```

---

*See COMPONENTS.md for details, BLUEPRINT.md for spec.*
