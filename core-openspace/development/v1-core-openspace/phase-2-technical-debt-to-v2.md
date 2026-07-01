# TECHNICAL DEBT — core-openspace V1 → V2

> **Author:** Mydde — 2026-04-12
> Items identified at scaffold time. Do not block V1. Address in V2.

---

### TD-01 — Event Persistence / Queue

**Discovered:** 2026-04-12 — V1 scaffold — Mydde
**File:** `core-openspace/openspace.mjs`
**Issue:** `openspace.mjs` dispatches events synchronously with no persistence. If a target app is unavailable at dispatch time, the event is lost.
**Impact:** Transient unavailability causes silent event loss — no retry, no queue.
**Risk:** Medium

- [ ] Design event queue with persistence (JSONL or SQLite)
- [ ] Add retry policy for undelivered events
- [ ] Document delivery guarantees in `protocol.json`

**Effort:** 45 min

---

### TD-02 — Protocol Version Negotiation

**Discovered:** 2026-04-12 — V1 scaffold — Mydde
**File:** `core-openspace/protocol.json`
**Issue:** `protocol.json` has a `_meta.version` field but no mechanism for participants to declare which protocol version they support.
**Impact:** Breaking protocol changes cannot be detected at registration time.
**Risk:** Medium

- [ ] Add `protocol_version` field to each participant declaration
- [ ] Add version compatibility check in dispatcher startup
- [ ] Define semver policy for protocol.json changes

**Effort:** 20 min

---

### TD-03 — Handler Acknowledgement

**Discovered:** 2026-04-12 — V1 scaffold — Mydde
**File:** `core-openspace/openspace.mjs`
**Issue:** V1 dispatcher routes events but does not receive or track handler acknowledgements. No way to confirm delivery.
**Impact:** Silent failures — event dispatched, handler never executed, no trace.
**Risk:** Medium

- [ ] Define ACK contract in protocol.json
- [ ] Implement handler response callback in dispatcher
- [ ] Log ACK/NACK per event dispatch

**Effort:** 30 min

---

### TD-04 — `bmad/` Directory Not Covered by core-standard

**Discovered:** 2026-04-12 — V1 scaffold — Mydde
**File:** `core-openspace/bmad/`
**Issue:** `bmad/` directory is present but not defined in the core-standard structure spec. Unknown element per check-structure.mjs.
**Impact:** Validator will flag it as unknown — normative candidate not yet formalized.
**Risk:** Low

- [ ] Submit to core-standard pull cycle: formalize `bmad/` as optional app-root element
- [ ] Add to `KNOWN_DIRS` in `check-structure.mjs`

**Effort:** 15 min

---

### TD-05 — openspace.mjs Not Covered by core-standard

**Discovered:** 2026-04-12 — V1 scaffold — Mydde
**File:** `core-openspace/openspace.mjs`
**Issue:** `openspace.mjs` is a script at app root — not covered by the standard structure. Will be flagged as unknown element.
**Impact:** Normative candidate: applications with a primary dispatch script need a convention.
**Risk:** Low

- [ ] Submit to core-standard pull cycle: define convention for app-root executable scripts
- [ ] Add to `KNOWN_FILES` in `check-structure.mjs`

**Effort:** 15 min

---

## Technical Debt Summary

| ID | Item | Effort | Status |
|----|------|--------|--------|
| TD-01 | Event persistence / queue | 45 min | 📋 Open |
| TD-02 | Protocol version negotiation | 20 min | 📋 Open |
| TD-03 | Handler acknowledgement | 30 min | 📋 Open |
| TD-04 | `bmad/` not covered by core-standard | 15 min | 📋 Open |
| TD-05 | `openspace.mjs` not covered by core-standard | 15 min | 📋 Open |
