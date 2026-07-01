# Core-Squad — V1 Formalization

> Tasks to formalize the live core-squad orchestrator under core-standard.

---

### 1.1 — Create SKILL.md

**File:** `core-squad/skill/core-squad/SKILL.md`
**Problem:** No skill file exists for the most critical app in the ecosystem.
**Risk:** High — agents cannot invoke or understand core-squad capabilities.

- [ ] Create SKILL.md with OCM protocol description, sub-agent model, escalation levels
- [ ] Document commands: OCM-SIMULATE, OCM-PROCEED, CRITICAL FAILURE

**Effort:** 15 min

---

### 1.2 — Create llms.txt

**File:** `core-squad/development/v1-core-squad/llms.txt`
**Problem:** No machine-readable index.
**Risk:** Low — agents must explore manually.

- [x] Create llms.txt with document map

**Effort:** 5 min

---

### 1.3 — Link existing code to v1 structure

**File:** `core-squad/development/v1-core-squad/`
**Problem:** Live code (`index.mjs`, `package.json`, `scripts/`, `ocm-*.md`) exists at root but not linked to v1 folder.
**Risk:** Medium — v1 folder appears empty of actual functionality.

- [ ] Add cross-references in README.md to root-level code files
- [ ] Document that `index.mjs`, `ocm-*.md` are the actual implementation

**Effort:** 10 min

---

### 1.4 — Document OCM protocol as standard

**File:** `core-squad/development/v1-core-squad/phase-1-repair.md`
**Problem:** OCM protocol (OCM-SIMULATE / OCM-PROCEED) is app-specific and not documented as a reusable pattern.
**Risk:** Low — but could be normative for other orchestrators.

- [ ] Document OCM protocol structure: instructions → simulate → proceed → status
- [ ] Note: this is app-specific, not a general convention (do not formalize)

**Effort:** 20 min

---

### 1.5 — Create DEPENDENCIES.md

**File:** `core-squad/DEPENDENCIES.md`
**Problem:** core-squad depends on place-de-greve (mission queue), machinery (classification), and all sensory apps.
**Risk:** Medium — changes to dependencies may break orchestration.

- [ ] Create DEPENDENCIES.md with: place-de-greve (required), machinery (required), core-standard (required), structural-mapping (optional), matrix-topology (optional), embeddings (optional)

**Effort:** 10 min
