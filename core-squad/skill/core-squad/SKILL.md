---
name: core-squad
description: |-
  Primary orchestrator and mission control system. Manages OCM protocol (OCM-SIMULATE / OCM-PROCEED), sub-agent spawning, autonomous mission execution, and health monitoring.
argument-hint: "OCM-SIMULATE, OCM-PROCEED, CRITICAL_FAILURE"
user-invocable: true
---

# Core-Squad — Primary Orchestrator

## Purpose

OpenClaw Master — the orchestrator that reads user instructions from `ocm-INSTRUCTIONS.md`, manages the mission queue, spawns sub-agents, and reports status.

## Commands

| Command | Action |
|---------|--------|
| `OCM-SIMULATE` | Preview execution plan in `ocm-STATUS-REPORT.md`, wait for confirmation |
| `OCM-PROCEED` | Execute the simulated plan |
| `CRITICAL_FAILURE` | System pause requiring human intervention |

## Sub-Agent Model

- **No auto-inheritance** — Master must explicitly whitelist tools
- **Context injection** — Master provides `context_fragment` and `root_lock`
- **Read-only environment** — Cannot modify inherited env vars
- **Telemetry redirection** — All logs go to `ocm-audit-trail.log`

## Escalation Levels

1. **Level 1 (Direct)** — Master fixes simple issues directly
2. **Level 2 (Delegation)** — Spawns `ocm-sub-[specialist]` for complex debugging
3. **Level 3 (Escalation)** — System pause + `[CRITICAL_FAILURE]` marker for human intervention

## Key Files

| File | Purpose |
|------|---------|
| `index.mjs` | Main orchestrator entry point |
| `ocm-INSTRUCTIONS.md` | User command protocol |
| `ocm-MISSION-QUEUE.md` | Auto-managed mission queue |
| `ocm-STATUS-REPORT.md` | Agent reports and status |
| `scripts/maintenance-scanner.mjs` | Generic health scanner |
| `HEARTBEAT.md` | V5 health check protocol |

## Current Status

✅ V1 operational — Phase 1 formalization in progress.
