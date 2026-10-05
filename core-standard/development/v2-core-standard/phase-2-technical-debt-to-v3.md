# TECHNICAL DEBT — V3 Planning

> Items identified during V2 normative consolidation for V3.

---

### TD-01 — App-level technical debt file convention

**Discovered:** 2026-04-12 — V2 transition — Qwen Code
**Issue:** V2 phase-1-repair.md is fully completed but no technical debt file exists yet for V3.
**Impact:** No backlog for next version.
**Risk:** Low

- [x] Create `phase-2-technical-debt-to-v3.md`

**Effort:** 5 min

---

### TD-02 — Normative candidate: protocol.json inter-app communication

**Discovered:** 2026-04-12 — core-normalize scan — Qwen Code
**File:** `core-openspace/protocol.json`
**Issue:** Element `protocol.json` defines a reusable inter-app communication pattern — 6 participants, 6 event types, capability-based routing. Any multi-app system could benefit from this convention.
**Impact:** Without standardization, each app maintains its own ad-hoc cross-app communication.
**Risk:** Medium

- [x] Formalize as convention: `protocol.json` — optional app-root file for inter-app protocol declaration
- [x] Document structure in `structure.md` (§17)
- [x] Add to `KNOWN_FILES` in `check-structure.mjs`

**Effort:** 15 min

---

### TD-03 — Normative candidate: domain-registry.json

**Discovered:** 2026-04-12 — core-normalize scan — Qwen Code
**File:** `mission-queue/domain-registry.json`
**Issue:** Element `domain-registry.json` defines domain routing alongside `domain-registry.json` — same pattern, complementary purpose.
**Impact:** Both files follow the same convention; should be documented together.
**Risk:** Low

- [x] Formalize alongside `domain-registry.json` — both are known domain routing files
- [x] Add to `KNOWN_FILES` in `check-structure.mjs` (already present)

**Effort:** 5 min

---

### TD-04 — Close remaining unknown elements (transient)

**Discovered:** 2026-04-12 — core-normalize scan — Qwen Code

| Unknown | Decision |
|---------|----------|
| `core-openspace/bmad` | ❌ Ignored — BMAD-specific |
| `core-squad/.openclaw` | ❌ Ignored — runtime directory |
| `core-squad/bmad` | ❌ Ignored — BMAD-specific |
| `core-squad/index.mjs` | ❌ Ignored — Node.js convention |
| `core-squad/package.json` | ❌ Ignored — Node.js convention |

**Effort:** 10 min

---

## Technical Debt Summary

| ID | Item | Effort | Status |
|----|------|--------|--------|
| TD-01 | App-level technical debt file convention | 5 min | ✅ Done |
| TD-02 | Normative candidate: protocol.json | 15 min | ✅ Done |
| TD-03 | Normative candidate: domain-registry.json | 5 min | ✅ Done |
| TD-04 | Close transient unknowns | 10 min | ✅ Done |
