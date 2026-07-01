# core-openspace V1 — Inter-Application Protocol Bus

**Date:** 2026-04-12
**Status:** Phase 1 📋 Planned | Phase 2 📋 Planned
**Author:** Mydde

---

## Sources

- Protocol declaration: `core-ferule/core-openspace/protocol.json`
- User notes: `core-ferule/core-openspace/USER-NOTES.md`
- Replaced mechanism: `openclaw-master/ocm-INSTRUCTIONS.md`

---

## Overview

V1 establishes `core-openspace` as the authoritative inter-application protocol bus for `core-ferule`.
It replaces manual file-based messaging (`ocm-INSTRUCTIONS.md`) with a declared protocol in `protocol.json`.
All cross-app event routing is centralized here — no app maintains its own messaging files.

---

## Scope

| Item | Included in V1 |
|------|----------------|
| `protocol.json` as source of truth | ✅ |
| Participant registration: `core-squad`, `place-de-greve`, `core-standards` | ✅ |
| Event types: intervention.request, status.update, broadcast, query, mission.* | ✅ |
| `openspace.mjs` — minimal dispatcher | ✅ |
| Replace `ocm-INSTRUCTIONS.md` usage | ✅ |
| Full event persistence / queue | ❌ V2 |
| Web UI / dashboard | ❌ V2 |

---

## Structure

| File | Content |
|------|---------|
| [phase-1-repair.md](phase-1-repair.md) | Initial state audit, scaffold gaps, participant onboarding |
| [phase-2-technical-debt-to-v2.md](phase-2-technical-debt-to-v2.md) | Debt identified at scaffold time |
| [reports/bug-reports.md](reports/bug-reports.md) | Bug log |
| [reports/deployment-report.md](reports/deployment-report.md) | Deployment summary |

---

## Summary Table

| Step | Task | Effort | Depends on | Status |
|------|------|--------|------------|--------|
| **1.1** | Audit scaffold against core-standard | 10 min | — | 📋 |
| **1.2** | Register core-squad, place-de-greve, core-standards as participants | 10 min | 1.1 | 📋 |
| **1.3** | Implement `openspace.mjs` dispatcher | 30 min | 1.2 | 📋 |
| **1.4** | Validate routing for all declared event types | 20 min | 1.3 | 📋 |
| **1.5** | Deprecate `ocm-INSTRUCTIONS.md` — document migration | 15 min | 1.4 | 📋 |
