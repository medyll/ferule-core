# Core Workflow V1 — BMAD Method Migration

**Date:** 2026-04-12
**Status:** Phase 1 ✅ Complete

## Sources

- Origin: `skills/bmad-method/` (migrated to core-ferule)
- User Notes: `core-workflow/USER-NOTES.md`
- Config: `config/engine.yaml`, `config/roles.yaml`, `config/workspace.yaml`

## Overview

V1 migrates `bmad-method` from `skills/` to `core-ferule/core-workflow/`, adapting it for OpenClaw with centralized configuration and renamed commands (`workflow` instead of `bmad`).

## Structure

| File | Content |
|------|---------|
| [phase-1-migration.md](phase-1-migration.md) | Migration from bmad-method |
| [phase-1-technical-debt-to-v2.md](phase-1-technical-debt-to-v2.md) | Technical debt |

## Summary Table

| Step | Task | Effort | Depends on | Status |
|------|------|--------|------------|--------|
| **1.1** | Create directory structure (core-standard compliant) | 10 min | — | ✅ |
| **1.2** | Copy `references/` from bmad-method | 5 min | — | ✅ |
| **1.3** | Copy `templates/` from bmad-method | 5 min | — | ✅ |
| **1.4** | Copy `scripts/engine.mjs` + node_modules | 5 min | — | ✅ |
| **1.5** | Copy `artifacts/` and `source/` | 5 min | — | ✅ |
| **1.6** | Create centralized config (engine.yaml, roles.yaml, workspace.yaml) | 15 min | — | ✅ |
| **1.7** | Create SKILL.md with workflow commands | 10 min | 1.6 | ✅ |
| **1.8** | Create root files (README, SCRATCHPAD, USER-NOTES) | 10 min | — | ✅ |

## Decisions

| Decision | Reason |
|----------|--------|
| Commands renamed `workflow` instead of `bmad` | Assert OpenClaw identity, avoid confusion |
| Config in `config/` instead of per-project `./bmad/` | Centralized orchestration |
| Roles copied as-is | Generic, no changes needed |
| engine.mjs unchanged | CLI functional |

## Current System State

| Component | Status |
|-----------|--------|
| Migration | ✅ Complete |
| CLI (engine.mjs) | ✅ Functional |
| Config | ✅ Created |
| Skill integration | ✅ Created |
| Conformance to core-standard V2 | ✅ Verified |
