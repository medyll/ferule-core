# TECHNICAL DEBT

> **Authors:** core-analyse scan (2026-04-14)

> Items identified during V1 core-analyse that do not block current work but must be addressed in V2.

---

### TD-01 — Missing USER-NOTES.md at app root

**Discovered:** 2026-04-14 — core-analyse structure validation — Qwen Code
**File:** `core-cognition/USER-NOTES.md`
**Issue:** USER-NOTES.md exists at development/v1-core-cognition/ but not at app root as required by §10.
**Impact:** Validator expects USER-NOTES.md at app root — non-compliant with standard.
**Risk:** Low

- [ ] Copy or mirror USER-NOTES.md to core-cognition/ app root

**Effort:** 5 min

---

### TD-02 — Embeddings directory not yet normative

**Discovered:** 2026-04-14 — core-analyse normalization scan — Qwen Code
**File:** `core-cognition/embeddings/`
**Issue:** Embedding database exists but was not covered by standard at time of creation.
**Impact:** Now integrated as §17 — no further action needed, but historical TD entry for tracking.
**Risk:** Low

- [x] Integrated into standard as §17 (structure.md)
- [x] Added to KNOWN_DIRS in check-structure.mjs

**Effort:** 30 min (already resolved)

## Technical Debt Summary

| ID | Item | Effort | Status |
|----|------|--------|--------|
| TD-01 | Missing USER-NOTES.md at app root | 5 min | 📋 Open |
| TD-02 | Embeddings directory normative integration | 30 min | ✅ Done (V2 §17) |
