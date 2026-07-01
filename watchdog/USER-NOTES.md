# USER-NOTES — watchdog

> Last updated: 2026-04-13 — Qwen Code

## Preferences

- All technical artifacts in English
- Formal tone, core-standard compliant

## Decisions

- Watchdog runs every 5 minutes via Windows Task Scheduler
- Alerts are written to `logs/alerts.jsonl` (1000-line rotation)
- Critical alerts also written to `core-squad/ocm-INSTRUCTIONS.md`
- Zero external dependencies — pure Node.js only

## Instructions

- Install Task Scheduler task via provided PowerShell script
- Uninstall via provided PowerShell script
- Do not modify check intervals without user approval
- Follow core-standard V2 (DEPENDENCIES.md, protocol if needed)
