# PHASE 1 — Initial State, Scaffold Audit, Participant Onboarding

> Establish core-openspace as a functional protocol bus. Audit scaffold conformance, register participants, implement the dispatcher, and retire ocm-INSTRUCTIONS.md.

---

### 1.1 — Scaffold Audit vs. core-standard

**File:** `core-ferule/core-openspace/`
**Problem:** Newly scaffolded app — conformance to core-standard must be verified before any implementation work.
**Risk:** Structural gaps will cause validator failures and slow future phases.

- [ ] Run `check-structure.mjs` against `core-openspace/`
- [ ] Verify presence: `README.md`, `USER-NOTES.md`, `SCRATCHPAD.md`, `skill/core-openspace/SKILL.md`
- [ ] Verify presence: `development/v1-core-openspace/llms.txt`, `reports/`
- [ ] Verify `protocol.json` is present and valid JSON
- [ ] Document any gaps found

**Effort:** 10 min

---

### 1.2 — Participant Registration

**File:** `core-ferule/core-openspace/protocol.json`
**Problem:** Initial scaffold lists participants but capabilities have not been verified against each app's actual behavior.
**Risk:** Declared capabilities that don't match real app behavior create silent routing failures.

- [ ] Read `core-squad` README — confirm capabilities match `protocol.json` entry
- [ ] Read `place-de-greve` README — confirm `mission.assigned` / `mission.completed` events are accurate
- [ ] Read `core-standards` README — confirm `norm.updated` / `query` capabilities
- [ ] Update `protocol.json` participants section if any capability is wrong
- [ ] Add `openclaw-maintenance` capabilities after verification

**Effort:** 10 min

---

### 1.3 — Implement `openspace.mjs` Dispatcher

**File:** `core-ferule/core-openspace/openspace.mjs`
**Problem:** No implementation exists. `protocol.json` declares routing but nothing executes it.
**Risk:** Protocol remains theoretical without a dispatcher — apps cannot use it.

- [ ] Create `openspace.mjs` at `core-openspace/` root
- [ ] Load `protocol.json` on startup
- [ ] Implement `dispatch(event)` — accepts `{ type, from, payload }`, returns list of matched handlers
- [ ] Routing logic: match `event.type` against participant `capabilities` where `handle:<type>` is declared
- [ ] Log unrouted events (no silent drops — per protocol.json routing rule)
- [ ] Zero external dependencies — pure Node.js ESM

**Effort:** 30 min

---

### 1.4 — Validate Routing for All Declared Event Types

**File:** `core-ferule/core-openspace/openspace.mjs`
**Problem:** Dispatcher implementation must be verified against all 6 event types.
**Risk:** A routing gap discovered in production is harder to diagnose.

- [ ] Write test fixtures in `development/v1-core-openspace/reports/` — one per event type
- [ ] Verify `intervention.request` routes to: place-de-greve, core-squad, openclaw-maintenance
- [ ] Verify `status.update` routes to: all participants with `handle:status.update`
- [ ] Verify `broadcast` routes to: all `handle:broadcast` handlers
- [ ] Verify `query` routes to: core-cognition, formal-ideation, core-standards
- [ ] Verify `mission.assigned` and `mission.completed` route from place-de-greve
- [ ] Verify unrouted event logs correctly

**Effort:** 20 min

---

### 1.5 — Deprecate `ocm-INSTRUCTIONS.md`

**File:** `openclaw-master/ocm-INSTRUCTIONS.md`
**Problem:** Manual file-based messaging is replaced by core-openspace. The old mechanism must be formally retired to prevent parallel usage.
**Risk:** Two messaging mechanisms coexisting will create confusion and drift.

- [ ] Add deprecation notice to `openclaw-master/ocm-INSTRUCTIONS.md` header
- [ ] Document migration: what `ocm-INSTRUCTIONS.md` provided → equivalent in `protocol.json`
- [ ] Update any README or USER-NOTES that references `ocm-INSTRUCTIONS.md` pattern

**Effort:** 15 min

---

## Summary

| Step | Task | Effort | Status |
|------|------|--------|--------|
| **1.1** | Scaffold audit | 10 min | 📋 Open |
| **1.2** | Participant registration | 10 min | 📋 Open |
| **1.3** | Implement `openspace.mjs` | 30 min | 📋 Open |
| **1.4** | Validate routing | 20 min | 📋 Open |
| **1.5** | Deprecate `ocm-INSTRUCTIONS.md` | 15 min | 📋 Open |
