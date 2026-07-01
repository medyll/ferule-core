# Application Core — Role, Structure & Core-Standards

> **Date:** 2026-04-12
> **Type:** Audit report — informational only, no modifications
> **Author:** Qwen Code

## Sources

- Structure: [`structure.md`](./structure.md)
- Behaviour: [`behaviour.md`](./behaviour.md)
- Governance: [`governance.md`](./governance.md)
- Core-Standards Skill: [`core-standard/skill/core-standard/SKILL.md`](./core-standard/skill/core-standard/SKILL.md)

## Overview

`core-ferule/` is the **governance and application layer** of the OpenClaw Desktop environment. It hosts every application that runs within the OpenClaw ecosystem, along with the standards, tooling, and coordination protocols that govern how those applications are built, maintained, and evolved. It is not the OpenClaw runtime itself — it is the **rules of the game** and the **applications that play it**.

The directory serves three roles simultaneously:

1. **Standard authority** — defines formatting, naming, lifecycle, and agent behaviour for all applications
2. **Application host** — contains 8 applications covering orchestration, mission management, maintenance, formal-ideation, and external integrations
3. **Self-improving system** — unknown elements detected in applications are evaluated for normative value and either integrated into the standard or logged as technical debt

## Structure

| File | Content |
|------|---------|
| [`README.md`](./README.md) | Application standards index — entry point |
| [`structure.md`](./structure.md) | Part A — Directory layout, file formats, naming, templates |
| [`behaviour.md`](./behaviour.md) | Part B — Agent startup, maintenance, crisis protocol |
| [`governance.md`](./governance.md) | Part C — Norm governance, pull cycle, versioning |
| [core-standard/](#1-core-standard--the-normalization-hub) | Normalization hub — commands, validator, templates |
| [core-squad/](#2-core-squad--orchestrator--mission-control) | OpenClaw master orchestrator and mission control |
| [place-de-greve/](#3-place-de-greve--autonomous-mission-queue) | Autonomous mission queue and BMAD orchestrator |
| [registry-mind/](#4-registry-mind--android-cognitive-sensor) | Android 16 cognitive capture sensor |
| [token-strategie/](#5-token-strategie--cost-aware-llm-routing) | Cost-aware LLM routing strategy |
| [structural-mapping/](#6-structural-mapping--organizational-power-mapper) | Organizational power structure mapper |
| [openclaw-maintenance/](#7-openclaw-maintenance--systems-maintainer) | Senior systems maintainer and code auditor |
| [formal-ideation/](#8-formal-ideation--raw-ideas--experimental) | Raw ideas and experimental concepts |

## Hierarchy of Features

### 1. Core-Standards — The Normalization Hub

| Sub-element | Role |
|-------------|------|
| **SKILL.md** | Exposes 6 commands: `core-bootstrap`, `core-rationalize`, `core-validate`, `core-normalize`, `core-formalize`, `core-status` |
| **check-structure.mjs** | Zero-dependency structure validator — scans all applications for compliance |
| **Templates/** | 6 templates: README, phase, bug report, technical debt, deployment report, prompts |
| **Pull cycle** | Practices emerge from real applications → evaluated via `core-normalize` → integrated into standard or logged as technical debt |

### 2. Core-Squad — Orchestrator & Mission Control

| Sub-element | Role |
|-------------|------|
| **index.mjs** | Main entry point — reads `ocm-INSTRUCTIONS.md`, executes commands, updates status report |
| **OCM Protocol** | File-based command interface: `OCM-SIMULATE` (preview) → `OCM-PROCEED` (execute) |
| **Maintenance Scanner** | Generic health scanner for queue, YAML, JSON, and generic text targets |
| **HEARTBEAT.md** | 6 automated health checks: queue integrity, scanner, watcher, recent activity, backups, stale missions |
| **Sub-Agent Model** | Strict parent-child laws — no auto-inheritance, explicit tool whitelisting, audit trail logging |
| **Escalation Levels** | Level 1 (direct fix), Level 2 (delegate to sub-agent), Level 3 (pause + human intervention) |

### 3. Place de Grève — Autonomous Mission Queue

| Sub-element | Role |
|-------------|------|
| **Watcher** | File-change detector with 4 targets, 22+ paths, auto-start via Task Scheduler |
| **Scanner** | Auto-prioritize and auto-take missions from the queue |
| **Dashboard Sync** | Syncs mission queue to `production-dashboard.md` |
| **Context Registry** | 6 domains (maturation, development, core-squad, authoring, capture, manual) with routing rules |
| **Backup** | Auto-backup before every write operation |
| **Idempotence Guard** | Prevents empty-queue destruction — aborts if 0 missions detected |
| **Versions** | V3 (deployed), V4 (stabilization + midnight investigation), V5 (core-standard compliance), V6 (timestamps + atomic lock) |

### 4. Registry-Mind — Android Cognitive Sensor

| Sub-element | Role |
|-------------|------|
| **Platform** | Android 16, Kotlin 2.1 / Coroutines |
| **Capture** | Snap Key trigger → screen buffer + OCR → JSON packet |
| **Relay** | Tailscale or local sync to OpenClaw Desktop |
| **Offline Mode** | Room/SQLite local cache, automatic sync when reconnected |
| **Performance Targets** | Wake-up <100ms, OCR <350ms, Memory <60MB, Idle drain 0% |

### 5. Token-Strategie — Cost-Aware LLM Routing

| Sub-element | Role |
|-------------|------|
| **Tier 1** | modelstudio/qwen3.5-plus (default, cost-efficient) |
| **Tier 2** | Coding tasks — qwen3-coder-next or codestral |
| **Tier 3** | Heavy reasoning — claude-opus-4.6 (last resort) |
| **Tier 4** | Multimodal — qwen3.5-omni |
| **Tier 5** | Local/offline — Ollama models |
| **Budget** | DashScope $10-20/month target |

### 6. Structural-Mapping — Organizational Power Mapper

| Sub-element | Role |
|-------------|------|
| **Nomenclature** | `ind-[group]-[name5]` — normalized indicators on 0-3 scale |
| **Indicator Groups** | pvr (internal power), ray (external reach), sem (knowledge) |
| **Outputs** | Synthesis table, arborescence (.md), Mermaid diagram |
| **Reference Case** | Franc-Tireur editorial staff (first instance) |

### 7. Openclaw-Maintenance — Systems Maintainer

| Sub-element | Role |
|-------------|------|
| **Health** | Node.js v22+, pnpm workspace, git status before file ops |
| **Security** | Credential leak detection, no destructive commands without confirmation |
| **Coverage** | Minimum 70% (Vitest/V8) |
| **Automation** | Nightly scans, hotspot optimization, memory consolidation |

### 8. Ideation — Raw Ideas & Experimental

| Sub-element | Role |
|-------------|------|
| **Purpose** | Capture and structure raw ideas without risk to Maturation system |
| **Constraint** | DO NOT touch Maturation (`D:\boulot\dev\maturation\`) |
| **Status** | Germination — scaffold created, scope to be defined |

## Core-Standards — Role in the Ecosystem

Core-standards is the **governing norm** for all applications under `core-ferule/`. It is not an application itself — it is the **standard authority** that all applications must conform to.

### What It Defines

| Domain | Content |
|--------|---------|
| **Directory layout** | Mandatory structure for every application |
| **File templates** | README, phase, bug report, technical debt, deployment report |
| **Naming conventions** | kebab-case, version-safe, standardized IDs |
| **Markdown rules** | English only, formal tone, max `###` headers, fenced code |
| **Agent behaviour** | Startup sequence, SCRATCHPAD detection, scaffold trigger |
| **Maintenance standards** | Dashboard interface, scanner compliance, post-restart validation |
| **Crisis protocol** | Midnight-hell investigation lifecycle |
| **Norm governance** | Pull cycle, unknown element evaluation, versioning |

### The Pull Cycle

```
Application encounters unknown element
    ↓
[core-validate] detects and reports it
    ↓
[core-normalize] evaluates against 4 criteria:
    • Structure — does it define a reusable pattern?
    • Reusability — can other applications benefit?
    • Intent — was it deliberate, not accidental?
    • Completeness — is it sufficiently developed?
    ↓
≥ 2 criteria met → integrated into standard automatically
< 2 criteria met → logged as TECH-xxxx-NNNNN in core-standard debt file
```

### The Commands

| Command | Trigger | Action |
|---------|---------|--------|
| `[core-bootstrap]` | BLUEPRINT.md exists, no development/ | Scaffold v1 automatically |
| `[core-rationalize]` | Human explicitly asks | SCRATCHPAD.md → BLUEPRINT.md |
| `[core-validate]` | On demand or auto-chain | Run structure validator |
| `[core-normalize]` | Auto after validate | Evaluate and integrate unknowns |
| `[core-formalize]` | On demand | Create TECH entries for review |
| `[core-status]` | On demand | Report conformity state |

### SCRATCHPAD / BLUEPRINT Cycle

```
SCRATCHPAD.md                          BLUEPRINT.md                        SCAFFOLD
─────────────────                      ─────────────────                   ────────────
Freeform capture, no structure          Normalized, core-standard format   development/v1-<app>/
User writes freely, any language        English, structured, clear          USER-NOTES.md derived
Agent NEVER auto-normalizes             Derived from SCRATCHPAD by          Skill, llms.txt, README
Agent may tidy if asked                 [core-rationalize] (human-triggered) Phase files created on demand
```

## Current System State

| Component | Status | Notes |
|-----------|--------|-------|
| **Core-Standards** | V1 operational | Phase 1 complete, phase 2 (technical debt) planned |
| **Core-Squad** | V1 operational | Initialization implemented, event loop pending |
| **Place de Grève** | V3 deployed, V6 in development | 26+ versions of the norm, midnight investigation complete |
| **Registry-Mind** | V1 scaffolded | BLUEPRINT defined, Kotlin spec complete |
| **Token-Strategie** | V1 scaffolded | Implementation pending |
| **Structural-Mapping** | Pre-scaffold | BLUEPRINT defined, nomenclature validated |
| **Openclaw-Maintenance** | V1 scaffolded | Blueprint defined, implementation pending |
| **Ideation** | V1 scaffolded | Germination — scope to be defined |

## Validator

```bash
node core-standard/scripts/check-structure.mjs
```


# testimony
    the previous version of the atlas which was made by <previous visitor> had differences, here are they, or here are they not
    <!-- i should have put a short resume (10 lines) of the precedent atlas.md, but it was inexistent, so i wrote this. There should be a core-standard norm -->