# Deployment Report — v1-core-workflow

**Date:** 2026-04-13
**Version:** V1
**Status:** Deployed

---

## Overview

Migration of `bmad-method` from `skills/bmad-method/` to `core-ferule/core-workflow/`.

## Changes

| Action | Details |
|--------|---------|
| Copied | references/, templates/, scripts/, artifacts/, source/ |
| Created | config/ (engine.yaml, roles.yaml, workspace.yaml) |
| Created | skill/core-workflow/SKILL.md (adapted for OpenClaw) |
| Created | README.md, SCRATCHPAD.md, USER-NOTES.md |
| Created | development/v1-core-workflow/ with phase-1-migration.md |

## Validation

- Core-standard validator: ✅ structure conforme
- Unknowns formalized: 8 entries in core-standard debt file

## Rollback

Original bmad-method remains in `skills/bmad-method/` — untouched.
