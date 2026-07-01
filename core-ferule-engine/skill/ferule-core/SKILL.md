---
name: ferule-core
description: |-
  Point d'entrée métier pour Ferule-Core. Écoute, interprète, route vers la ferule compétente.
  - Vers core-squad: missions, orchestration, Place de Grève
  - Vers core-standard: normes, taxonomie, validation
  - Vers watchdog: health checks, alerts
  - Vers incidents: rapports d'incidents critiques
argument-hint: "mission, norm, health, incident"
user-invocable: true
---

# Ferule-Core Skill

## Rôle

**core-ferule-engine** est le **moteur métier** de la Férule. Cette skill est le point d'entrée unique pour toutes les interactions avec le système Ferule-Core.

## Routing

| Intent | Cible | Fichier |
|--------|-------|---------|
| Mission, Place de Grève | `core-squad/` | `ocm-INSTRUCTIONS.md` |
| Norme, structure, taxonomie | `core-standard/` | `SKILL.md` |
| Health, alerts | `watchdog/` | `scripts/watchdog.mjs` |
| Incident report | `incidents/` | `killing-joe.md` |
| Cognition, routing | `core-cognition/` | `BLUEPRINT.md` |

## Commands

Aucune commande directe — **délègue exclusivement** vers la ferule compétente.

## Key Files

| File | Role |
|------|------|
| `run_engine.py` | Python execution engine |
| `core/rules/` | Business rules |
| `core/models/` | Data models |
| `core/workflows/` | Workflow definitions |
| `interfaces/` | External interfaces |
| `nexus-protocol/` | Inter-ferule protocol |

## Current Status

| Component | Status |
|-----------|--------|
| BLUEPRINT.md | ✅ Rationalized |
| USER-NOTES.md | ✅ Created |
| SKILL.md | ✅ This file |
| development/v1-core-ferule-engine/ | ⏳ Pending scaffold |
| run_engine.py | 🟡 Exists (undocumented) |
| core/ | 🟡 Exists (undocumented) |

## Relationships

| Ferule | Relationship |
|--------|--------------|
| `core-squad/` | Routes missions to orchestrator |
| `core-standard/` | Enforces norms defined by standard |
| `watchdog/` | Receives health alerts |
| `incidents/` | Logs critical failures |
| `core-cognition/` | Listening and routing layer |

---

*For LLMs: Read BLUEPRINT.md for full specification, USER-NOTES.md for preferences.*
