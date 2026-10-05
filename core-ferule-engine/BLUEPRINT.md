# core-ferule-engine — BLUEPRINT

> **Date:** 2026-04-17
> **Origin:** Rationalized from `SCRATCHPAD.md`
> **Author:** OpenClaw Session
> **Version:** v1-core-ferule-engine

---

## Overview

**Execution engine** — route les missions vers les ferules compétentes.

**Principle:** File-based, passive, simple.

**Separation of Concerns:**
- `core-standard` → **What** (norms)
- `core-ferule-engine` → **How** (execution)

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
├── skill/
│   └── ferule-core/           # Entry point skill
└── BLUEPRINT.md               # This document
```

---

## What's NOT in V1 (Overthinking Removed)

| Element | Why Removed |
|---------|-------------|
| Cron hooks | Hors scope V1 |
| Redis events | File bus suffit |
| Event hooks | data_field suffit |
| Hook actions | Route suffit |
| `/metrics`, `/skills` | API minimale |
| Pydantic models | Validation simple |
| `core/models/` | Inline dans engine.py |
| `core/workflows/` | Pas de workflows V1 |
| `interfaces/` | Pas d'interfaces V1 |
core-ferule-engine/
├── run_engine.py              # Python execution engine
├── requirements.txt           # Python dependencies
├── core/
│   ├── rules/                 # Business rules (normative enforcement)
│   ├── models/                # Data models (shared structures)
│   └── workflows/             # Workflow definitions (action chains)
├── interfaces/                # External system interfaces
├── nexus-protocol/            # Inter-ferule communication protocol
├── scripts/                   # Utility scripts
├── skill/
│   └── ferule-core/           # Entry point skill
│       └── SKILL.md
└── BLUEPRINT.md               # This document
```

---

## Components

### 1. Entry Point Skill

**Location:** `skill/ferule-core/SKILL.md`

**Purpose:** Single entry point for all Ferule-Core interactions.

**Routing Table:**

| Intent | Target |
|--------|--------|
| Norm, structure, taxonomy | `core-standard/` |
| Incident report | `incidents/` |

**Status:** ⏳ To be created (auto-generated on bootstrap)

---

### 2. Python Engine

**Location:** `run_engine.py`

**Purpose:** Execute normative rules, validate conformance, trigger workflows.

**Dependencies:** `requirements.txt`

**Status:** 🟡 Exists — requires documentation

**Open Questions:**
- What is the exact execution model?
- How is it triggered (CLI, API, heartbeat)?
- Which rules does it execute?

---

### 3. Core Rules

**Location:** `core/rules/`

**Purpose:** Normative rules enforced by the engine.

**Expected Content:**
- Rule definitions (YAML, JSON, or Python classes)
- Validation logic
- Enforcement actions

**Status:** 🟡 Exists — requires documentation

---

### 4. Data Models

**Location:** `core/models/`

**Purpose:** Shared data structures across the Ferule ecosystem.

**Expected Content:**
- Mission schema
- Ferule state schema
- Validation result schema

**Status:** 🟡 Exists — requires documentation

---

### 5. Workflows

**Location:** `core/workflows/`

**Purpose:** Defined action chains (multi-step operations).

**Expected Content:**
- Workflow definitions
- Trigger conditions
- Step sequences

**Status:** 🟡 Exists — requires documentation

---

### 6. Interfaces

**Location:** `core/interfaces/`

**Purpose:** External system connections.

**Expected Content:**
- API definitions
- Webhook handlers
- Import/export adapters

**Status:** 🟡 Exists — requires documentation

---

### 7. Nexus Protocol

**Location:** `nexus-protocol/`

**Purpose:** Inter-ferule communication standard.

**Expected Content:**
- Message format
- Routing protocol
- Acknowledgment flow

**Status:** 🟡 Exists — requires documentation

---

## Development Phases

### Phase 1: Foundation (Current)

- [x] SCRATCHPAD.md created
- [x] BLUEPRINT.md rationalized
- [ ] `skill/ferule-core/SKILL.md` created (bootstrap)
- [ ] `development/v1-core-ferule-engine/` scaffolded

### Phase 2: Documentation

- [ ] Document `run_engine.py` (role, triggers, execution model)
- [ ] Document `core/rules/` (rule format, examples)
- [ ] Document `core/models/` (schema definitions)
- [ ] Document `core/workflows/` (workflow definitions)
- [ ] Document `interfaces/` (external connections)
- [ ] Document `nexus-protocol/` (communication standard)

### Phase 3: Implementation

- [ ] Implement entry point skill routing
- [ ] Implement Python engine execution
- [ ] Implement rule validation
- [ ] Implement workflow triggers
- [ ] Integration testing

---

## Technical Debt (Pre-V2)

| ID | Description | Priority |
|----|-------------|----------|
| TD-01 | `run_engine.py` undocumented | High |
| TD-02 | `core/rules/` structure undefined | High |
| TD-03 | `core/models/` schema undefined | High |
| TD-04 | `core/workflows/` undefined | Medium |
| TD-05 | `interfaces/` undefined | Medium |
| TD-06 | `nexus-protocol/` undefined | Medium |
| TD-07 | Entry point skill not created | High |

---

## Key Files

| File | Role | Status |
|------|------|--------|
| `BLUEPRINT.md` | Structured specification | ✅ Created |
| `SCRATCHPAD.md` | Historical reference (preserved) | ✅ Preserved |
| `USER-NOTES.md` | LLM preferences (to be derived) | ⏳ Pending |
| `skill/ferule-core/SKILL.md` | Entry point skill | ⏳ Pending bootstrap |
| `run_engine.py` | Python engine | 🟡 Exists |
| `requirements.txt` | Python dependencies | 🟡 Exists |

---

## Relationships

| Ferule | Relationship |
|--------|--------------|
| `core-standard/` | Enforces norms defined by standard |
| `incidents/` | Logs critical failures |

---

## Bootstrap Command

```bash
node core-standard/scripts/check-structure.mjs --bootstrap
```

**Expected Output:**
```
core-ferule-engine/
├── USER-NOTES.md
├── skill/ferule-core/SKILL.md
└── development/
    └── v1-core-ferule-engine/
        ├── llms.txt
        ├── README.md
        ├── USER-NOTES.md
        └── reports/
```

---

*This BLUEPRINT is the authoritative specification for core-ferule-engine. All development must align with this document.*
