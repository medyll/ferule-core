---
name: watchdog
description: |-
  [status] (Report current watchdog status and recent alerts.)
  [install] (Install watchdog as a Windows Task Scheduler task — runs every 5 min.)
  [uninstall] (Remove watchdog from Task Scheduler.)
argument-hint: "status, install, uninstall"
user-invocable: true
---

# Watchdog — Independent Health Monitor

Monitors critical application-core subsystems every 5 minutes and alerts on failure. Zero external dependencies — pure Node.js.

## Checks

| # | Check | Failure Condition | Severity |
|---|-------|-------------------|----------|
| 1 | `dashboard-watcher.mjs` running | Process not found | Critical |
| 2 | Scan log recent | Last entry > 1 hour old | Warning |
| 3 | `context-registry.json` readable | File missing or invalid JSON | Critical |
| 4 | `place-de-greve.md` accessible | File missing or unreadable | Critical |
| 5 | Lock file not stale | Lock held > 60s | Warning |

## Alert Protocol

- All results → `logs/alerts.jsonl` (1000-line rotation)
- Critical failures → written to `core-squad/ocm-INSTRUCTIONS.md` under `## Watchdog Alerts`

## Key Files

| File | Purpose |
|------|---------|
| `scripts/watchdog.mjs` | Main watchdog script |
| `scripts/install-watchdog.ps1` | Task Scheduler installation |
| `scripts/uninstall-watchdog.ps1` | Task Scheduler removal |
| `logs/alerts.jsonl` | Alert log (append-only, rotated) |

## Current Status

🔄 V1 scaffolded — watchdog script created, Task Scheduler pending installation.
