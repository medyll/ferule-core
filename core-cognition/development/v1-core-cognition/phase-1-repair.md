# PHASE 1 — Core-Cognition Definition & Intent Routing

> Define core-cognition as the attentive perception layer: receives raw input, classifies via machinery, routes with resolved context:domain.

---

### 1.1 — Define agent identity and role

**File:** `core-cognition/USER-NOTES.md`
**Problem:** Role defined conceptually but not formalized as an agent with concrete capabilities.
**Risk:** Medium — other agents don't know what core-cognition can do or when to invoke it.

- [x] Formalize: core-cognition = attentive cognition (not passive "ear") — observes, detects, classifies, routes
- [x] Document: does not execute missions, only understands and delegates
- [x] Document: hard constraint — never submit to Place de Grève without `context:domain` resolved

**Effort:** 15 min

---

### 1.2 — Define intent classification pipeline

**File:** `core-cognition/BLUEPRINT.md`
**Problem:** Pipeline described conceptually but no concrete classification steps defined.
**Risk:** Medium — routing decisions are ad-hoc, no standard flow.

- [x] Define 4-step pipeline: Receive → Interpret intent → Resolve domain → Route
- [x] Define ambiguity protocol: request confirmation before routing when domain is unclear
- [x] Document machinery dependency: read `classifier.mjs` before any routing decision

**Effort:** 20 min

---

### 1.3 — Define sensory input registry

**File:** `core-cognition/BLUEPRINT.md`
**Problem:** No registry of what sensory inputs core-cognition can process.
**Risk:** Medium — unclear which formats/channels feed into cognition.

- [x] Define sensory layer: structural-mapping (metrics), matrix-topology (conceptual space), formal-ideation (raw thoughts)
- [x] Define common sensor report format: `{sensor, language, observation, confidence, timestamp}`
- [x] Document: core-cognition reads common format regardless of source sensor

**Effort:** 20 min

---

### 1.4 — Create SKILL.md

**File:** `core-cognition/skill/core-cognition/SKILL.md`
**Problem:** Skill file exists but needs updated description reflecting attentive cognition role.
**Risk:** Low — skill is placeholder.

- [x] Update SKILL.md with attentive cognition description, sensory input registry, and routing pipeline

**Effort:** 15 min

---

### 1.5 — Create empty reports

**File:** `core-cognition/development/v1-core-cognition/reports/`
**Problem:** Reports directory exists but empty.
**Risk:** Low — validator warns.

- [x] Create `bug-reports.md` (empty template)
- [x] Create `deployment-report.md` (empty template)

**Effort:** 5 min
