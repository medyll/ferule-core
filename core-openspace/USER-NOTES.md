# USER-NOTES — core-openspace

> **Author:** Mydde
> **Date:** 2026-04-12

---

## Preferences

- Protocol declaration lives in `protocol.json` at the app root — this is the single source of truth.
- No app registers its own cross-app handlers in its own files. Registration happens here.

---

## Decisions

- `core-openspace` replaces the `ocm-INSTRUCTIONS.md` pattern.
  All inter-app communication that previously required manual message files is now declared via protocol.
- Event types are fixed at declaration time. New types require a protocol update here.

---

## Instructions

- To add a new participant app: add an entry to `protocol.json` under `participants`.
- To declare a new event type: add to `protocol.json` under `event_types`.
- To register a handler: add to `protocol.json` under `routing`.
- v1 development work lives in `development/v1-core-openspace/`.
