# USER-NOTES — Core Standards

> Last updated: 2026-04-11 — User

## Preferences

- Standards must be machine-readable first, human-readable second.
- Unknown elements must be formalized via the pull cycle, not ignored.

## Decisions

- `core-standard` governs all applications under `workspace/core-ferule`.
- Structural validation is automated via `check-structure.mjs`.

## Instructions

- Every new application must be scaffolded according to `core-ferule/README.md`.
- Run `[core-validate]` after any structural change to an application.
- If validation fails, fix the error immediately or formalize unknown elements via `[core-formalize]`.
