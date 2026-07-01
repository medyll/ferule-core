# USER-NOTES — core-openspace V1

> **Author:** Mydde
> **Date:** 2026-04-12

---

## Preferences

- `openspace.mjs` must stay dependency-free — pure Node.js ESM only.
- `protocol.json` is edited directly by hand or by an agent following an explicit instruction. No auto-generation.

---

## Decisions

- V1 scope is intentionally minimal: dispatcher + participant registration + ocm deprecation.
- Event queue and ACK are V2 — do not scope-creep into V1.
- `openspace.mjs` lives at `core-openspace/` root, not inside `development/`. It is the runtime artifact.

---

## Instructions

- Phase order is fixed: 1.1 → 1.2 → 1.3 → 1.4 → 1.5. Do not skip verification steps.
- Before implementing 1.3, participant capabilities in `protocol.json` must be verified (step 1.2).
- Do not modify `openclaw-master/ocm-INSTRUCTIONS.md` until step 1.5 — deprecation is the last step, not the first.
