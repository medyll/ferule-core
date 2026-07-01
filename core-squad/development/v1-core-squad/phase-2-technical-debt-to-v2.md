# TECHNICAL DEBT

> **Authors:** core-analyse scan (2026-04-14)

> Items identified during V1 core-analyse that do not block current work but must be addressed in V2.

---

### TD-01 — Missing USER-NOTES.md at app root

**Discovered:** 2026-04-14 — core-analyse structure validation — Qwen Code
**File:** `core-squad/USER-NOTES.md`
**Issue:** USER-NOTES.md does not exist at app root as required by §10.
**Impact:** Validator expects USER-NOTES.md at app root — non-compliant with standard.
**Risk:** Low

- [ ] Create USER-NOTES.md at core-squad/ app root (can be empty if no user instructions yet)

**Effort:** 5 min

---

### TD-02 — Missing SCRATCHPAD.md at app root

**Discovered:** 2026-04-14 — core-analyse structure validation — Qwen Code
**File:** `core-squad/SCRATCHPAD.md`
**Issue:** SCRATCHPAD.md does not exist at app root as required by §14.
**Impact:** Validator flags missing SCRATCHPAD.md — non-compliant with standard.
**Risk:** Low

- [ ] Create SCRATCHPAD.md at core-squad/ app root (can be empty if no raw captures yet)

**Effort:** 5 min

## Technical Debt Summary

| ID | Item | Effort | Status |
|----|------|--------|--------|
| TD-01 | Missing USER-NOTES.md at app root | 5 min | 📋 Open |
| TD-02 | Missing SCRATCHPAD.md at app root | 5 min | 📋 Open |
