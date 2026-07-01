# watchdog — BLUEPRINT

> **Date:** 2026-04-13
> **Origin:** Rationalized from `SCRATCHPAD.md` — gap analysis revealed no alert system exists
> **Author:** Qwen Code

## Overview

`watchdog` is an **independent health monitor** for the core-ferule ecosystem. It runs on a fixed schedule (every 5 minutes via Windows Task Scheduler), checks that critical subsystems are alive, and alerts when they are not.

Unlike the heartbeat (which runs inside the agent session), the watchdog is a **standalone process** — it works even if the gateway is dead, the agent is stuck, or the watcher has silently crashed.

## Design Principles

1. **Zero dependencies** — pure Node.js, no npm packages
2. **Fail-loud** — any check failure produces an alert log entry and a notification
3. **Independent** — does not rely on any core-ferule process to function
4. **Minimal** — checks only what matters, logs everything

## Checks

| # | Check | Method | Failure Condition |
|---|-------|--------|-------------------|
| 1 | `dashboard-watcher.mjs` running | `tasklist /FI "IMAGENAME eq node.exe"` + scan for watcher path | No matching process found |
| 2 | Scan log recent | Read `logs/place-de-greve-scan.jsonl`, check last entry timestamp | Last entry > 1 hour old |
| 3 | `context-registry.json` readable | `JSON.parse(fs.readFileSync(...))` | File missing or invalid JSON |
| 4 | `place-de-greve.md` accessible | `fs.statSync(...)` | File missing or unreadable |
| 5 | Lock file stale | Read `place-de-greve.lock`, compare `acquiredAt` + 60s vs now | Lock held > 60s without update |

## Alert Protocol

```json
{
  "timestamp": "ISO8601",
  "check": "<check-name>",
  "status": "fail",
  "expected": "<what should have been>",
  "actual": "<what was found>",
  "severity": "critical|warning"
}
```

- **Critical:** Watcher dead, registry unreadable, queue inaccessible
- **Warning:** Scan log stale, lock file stale

Alerts are written to: `core-ferule/watchdog/logs/alerts.jsonl` (append, 1000-line rotation).

## Notification Channel

When a critical alert fires, the watchdog writes to `core-squad/ocm-INSTRUCTIONS.md` under a `## Watchdog Alerts` section. This ensures the next agent session sees it immediately.

## Dependencies

| App | Type | Notes |
|-----|------|-------|
| `place-de-greve` | required | Monitors its watcher, logs, registry, and lock file |
| `core-squad` | required | Receives alert notifications via `ocm-INSTRUCTIONS.md` |
| `core-standard` | required | This app conforms core-standard V2 |

## Current State

| Component | Status |
|-----------|--------|
| SCRATCHPAD | ✅ Created |
| BLUEPRINT | ✅ This file |
| V1 scaffold | ❌ Pending |
| Skill | ❌ Pending |
| Watchdog script | ❌ Pending |
| Task Scheduler | ❌ Pending |
