# Watchdog V1

> **Date:** 2026-04-13
> **Status:** Phase 1 ✅ — All tasks complete, Task Scheduler pending installation

## Overview

Independent health monitor that runs every 5 minutes via Windows Task Scheduler. Checks 5 critical subsystems and alerts on failure.

## Structure

| File | Content |
|------|---------|
| [phase-1-repair.md](phase-1-repair.md) | 3 steps — all ✅ done |

## Summary Table

| Step | Task | Effort | Depends on | Status |
|------|------|--------|------------|--------|
| **1.1** | Create watchdog.mjs (5 checks, alerts, notifications) | 45 min | — | ✅ |
| **1.2** | Create install/uninstall PowerShell scripts | 15 min | — | ✅ |
| **1.3** | Create application scaffold (skill, BLUEPRINT, dependencies) | 15 min | — | ✅ |

## Next Steps

- [ ] Run `scripts/install-watchdog.ps1` to register Task Scheduler task
- [ ] Verify first run via Task Scheduler → `logs/alerts.jsonl`
- [ ] Monitor alerts for 24h to validate check thresholds
