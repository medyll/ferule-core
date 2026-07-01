# core-workflow — BLUEPRINT

**Version:** 1.0
**Date:** 2026-04-12
**Origin:** Migrated from `skills/bmad-method/` to `core-ferule/core-workflow/`
**Author:** Qwen Code

---

## Overview

`core-workflow` is the **BMAD workflow engine** for the ferule-core ecosystem. It was migrated from `skills/bmad-method/` and adapted for OpenClaw. It provides CLI commands for project initialization, role assignment, status tracking, and workflow continuation across all BMAD projects.

## Architecture

```
config/             ← Centralized configuration
├── engine.yaml     ← Engine settings
├── roles.yaml      ← Role definitions (7 roles + identities)
└── workspace.yaml  ← Known apps, cross-workflow hooks

scripts/            ← CLI engine
└── engine.mjs      ← Core workflow CLI

references/         ← Role docs, commands, templates
├── roles/          ← 7 role definitions
├── commands.md
└── status-yaml-validation.md

templates/          ← Project templates
artifacts/          ← Generated artifacts
source/             ← Shared source code
skill/              ← OpenClaw skill integration
```

## Commands

Commands are prefixed with `workflow` (not `bmad`) to assert OpenClaw identity:

| Command | Purpose |
|---------|---------|
| `workflow init` | Initialize a new BMAD project |
| `workflow continue` | Resume work with a specific role |
| `workflow status` | Check project status |
| `workflow analyze` | Analyze project state |

## Configuration

| File | Role |
|------|------|
| `config/engine.yaml` | Engine settings |
| `config/roles.yaml` | Role definitions (Developer, PM, Architect, etc.) |
| `config/workspace.yaml` | Known apps, cross-workflow hooks |

## Dependencies

| App | Type | Notes |
|-----|------|-------|
| `place-de-greve` | consumer | Spawns BMAD agents via CLAW.md |
| `core-ferule-engine` | consumer | Routes tasks to workflow roles |
| `core-standard` | required | Conforms to V2 norm |

## Current State

| Component | Status |
|-----------|--------|
| Migration from bmad-method | ✅ Complete |
| CLI (engine.mjs) | ✅ Functional |
| Config (engine.yaml, roles.yaml, workspace.yaml) | ✅ Created |
| Role definitions | ✅ 7 roles copied |
| Skill integration | ✅ Created |
| V1 scaffold | ✅ Complete |
| Integration with core-ferule-engine | ⏳ Pending |
