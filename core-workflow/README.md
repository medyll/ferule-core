# core-workflow

**Version:** V1 Operational
**Origin:** Migrated from `skills/bmad-method/`
**Role:** BMAD Workflow Engine — project initialization, role management, status tracking

---

## Overview

`core-workflow` is the operational engine for BMAD methodology within the ferule-core ecosystem. It was migrated from `skills/bmad-method/` and adapted with OpenClaw-native configuration and command naming.

## Commands

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
| `config/roles.yaml` | 7 role definitions + identities |
| `config/workspace.yaml` | Known apps, cross-workflow hooks |

## Structure

| Directory | Content |
|-----------|---------|
| `scripts/engine.mjs` | CLI engine |
| `references/roles/` | 7 role definition files |
| `templates/` | Project templates |
| `artifacts/` | Generated artifacts |
| `skill/core-workflow/SKILL.md` | OpenClaw skill integration |

---

## Codification

Commands renamed from `bmad` to `workflow` to assert OpenClaw identity and avoid confusion with the original skill.
