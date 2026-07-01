# HEARTBEAT INSTRUCTIONS (V5 — Standard Compliant)

**Frequency:** Configured in `openclaw.json` → `agents_defaults.heartbeat.every`

---

## 1. Place de Grève Health Check (Automated)

> **Mandatory** — runs every heartbeat. Replaces manual process checks.
> Script: `workspace/scripts/health-check-place-de-greve.mjs`

### What it validates:
1. **Mission Queue Integrity** — `place-de-greve.md` has valid table (header + mission rows)
2. **Scanner Functionality** — scanner runs without errors, finds missions
3. **Watcher Process** — `dashboard-watcher.mjs` process is alive
4. **Recent Activity** — scan log has entries < 15 min old
5. **Backup Health** — at least 1 backup exists, none corrupted
6. **No Stale Missions** — no mission stuck `in-progress` > 2h

### Run:
```
node workspace/scripts/health-check-place-de-greve.mjs
```

**Output:** JSON to stdout + appended to `logs/health-check.jsonl`
```json
{
  "timestamp": "2026-04-11T09:00:00Z",
  "overall": "healthy",
  "checks": {
    "queue_integrity": "pass",
    "scanner": "pass",
    "watcher_process": "pass",
    "recent_activity": "pass",
    "backups": "pass",
    "stale_missions": "pass"
  }
}
```

**If ANY check fails:**
- Log the failure to `logs/health-check.jsonl`
- Update `ocm-STATUS-REPORT.md` with details
- If `watcher_process` fails → attempt restart via `start /B node workspace/scripts/dashboard-watcher.mjs`
- If `queue_integrity` fails → restore from latest backup

---

## 2. Post-Restart Validation Protocol

> **Mandatory** after every `openclaw gateway --force` or watcher restart.
> Ensures "Process Alive" ≠ "System Functional".

### After restart, run the full health check:
```
node workspace/scripts/health-check-place-de-greve.mjs
```
- **Success:** `overall: "healthy"`
- **Failure:** Trigger escalation — log details, attempt recovery, notify user.

### Log Verification
Check for silent failures.
- Run: `tail -10 workspace/logs/place-de-greve-scan.jsonl`
- **Check:** Is there a scan entry < 15 min old?
- **If no:** Heartbeat is broken. Restart OpenClaw Gateway.

---

## 3. Routine Maintenance

### Scan & Sync
1. **Periodic Scan:** `node workspace/scripts/scan-place-de-greve.mjs`
   - Keeps the queue alive (auto-prioritize + auto-take).
   - The watcher handles reactive triggers; this is the periodic safety net.
2. **Dashboard Sync:** `node workspace/scripts/sync/dashboard-project-sync.mjs`
   - Always sync dashboard on heartbeat.

### Inbox Protocol
1. **Read:** `CLAUDE-INBOX.md` (if exists).
2. **Respond:** If a message is addressed to Synapses, append to `SYNAPSES-INBOX.md`.

### Reporting
1. **Update:** `ocm-STATUS-REPORT.md` with findings from the Health Check.
   - Include the Health Check JSON output.
   - Summarize in simplified French for the User.
