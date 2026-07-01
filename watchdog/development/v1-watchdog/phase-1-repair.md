# PHASE 1 — Watchdog Implementation

> Create and deploy the independent health monitor for core-ferule.

---

### 1.1 — Create watchdog script

**File:** `scripts/watchdog.mjs`
**Problem:** No system alerts when critical subsystems fail.
**Risk:** High — silent failures go undetected (as demonstrated with the dead BMAD link).

- [x] Create `watchdog.mjs` with 5 checks: watcher process, scan log, domain-registry, queue accessibility, lock file staleness
- [x] Zero dependencies — pure Node.js (`fs`, `path`, `child_process`)
- [x] Alert logging to `logs/alerts.jsonl` with 1000-line rotation
- [x] Critical alerts written to `core-squad/ocm-INSTRUCTIONS.md`

**Effort:** 45 min

---

### 1.2 — Create installation scripts

**File:** `scripts/install-watchdog.ps1`, `scripts/uninstall-watchdog.ps1`
**Problem:** No automated deployment of watchdog.
**Risk:** Medium — manual setup is error-prone.

- [x] Create `install-watchdog.ps1` — registers Windows Task Scheduler task (5-min interval, hidden, highest privileges)
- [x] Create `uninstall-watchdog.ps1` — removes the task cleanly

**Effort:** 15 min

---

### 1.3 — Create application scaffold

**File:** `development/v1-watchdog/`
**Problem:** Watchdog app needs core-standard compliance.
**Risk:** Low — structural debt.

- [x] Create `development/v1-watchdog/` with README.md, llms.txt
- [x] Create `skill/watchdog/SKILL.md`
- [x] Create `DEPENDENCIES.md` (place-de-greve required, core-squad required, core-standard required)
- [x] Create `BLUEPRINT.md` and `USER-NOTES.md`

**Effort:** 15 min
