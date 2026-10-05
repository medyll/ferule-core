# core-ferule-engine — USER-NOTES

> **Derived from:** BLUEPRINT.md (2026-04-17)
> **Purpose:** LLM preferences and instructions for core-ferule-engine

---

## App Purpose

`core-ferule-engine` is the **execution engine** of Ferule-Core:
- Receives incoming requests
- Interprets intent
- Routes to appropriate ferule (core-squad, core-standard)
- Executes normative rules via Python engine

## Key Files

| File | Role |
|------|------|
| `run_engine.py` | Python execution engine |
| `requirements.txt` | Python dependencies |
| `core/rules/` | Business rules |
| `core/models/` | Data models |
| `core/workflows/` | Workflow definitions |
| `interfaces/` | External interfaces |
| `nexus-protocol/` | Inter-ferule protocol |
| `skill/ferule-core/SKILL.md` | Entry point skill |

## Routing Table

| Intent | Target |
|--------|--------|
| Mission, Place de Grève | core-squad/ |
| Norm, structure, taxonomy | core-standard/ |
| Incident report | incidents/ |

## Current Status

- **Version:** v1-core-ferule-engine (foundation phase)
- **BLUEPRINT.md:** ✅ Rationalized
- **SKILL.md:** ⏳ Pending creation
- **development/:** ⏳ Pending scaffold

## Technical Debt (Pre-V2)

| ID | Description | Priority |
|----|-------------|----------|
| TD-01 | run_engine.py undocumented | High |
| TD-02 | core/rules/ structure undefined | High |
| TD-03 | core/models/ schema undefined | High |
| TD-04 | core/workflows/ undefined | Medium |
| TD-05 | interfaces/ undefined | Medium |
| TD-06 | nexus-protocol/ undefined | Medium |
| TD-07 | Entry point skill not created | High |

## Development Phases

### Phase 1: Foundation (Current)
- BLUEPRINT.md rationalized
- SKILL.md to be created
- development/v1-core-ferule-engine/ to be scaffolded

### Phase 2: Documentation
- Document run_engine.py, core/rules/, core/models/, core/workflows/, interfaces/, nexus-protocol/

### Phase 3: Implementation
- Implement skill routing, Python engine, rule validation, workflow triggers

---

*For LLMs: Read BLUEPRINT.md for full specification, SCRATCHPAD.md for historical context.*
