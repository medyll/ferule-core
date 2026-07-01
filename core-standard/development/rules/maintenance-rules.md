# Maintenance Rules — Infrastructure Debug & Panic Room

> **Version:** 1.0
> **Date:** 2026-04-10
> **Author:** Claude
> **Source:** Derived from midnight-hell 09-04-2026 (place-de-greve) and core-standard v1 consolidation.

---

## 1. Source of Truth

| Rule | Detail |
|------|--------|
| **Raw sources first** | Always read raw logs, JSONL, and system files to assess state — never rely on status files, dashboards, or agent-generated summaries |
| **Process ≠ functional** | A running process is not proof the system is functional. Verify the data path end-to-end |
| **Status files are outputs** | `status-dashboard.md` and equivalent files are read-only for diagnostic purposes — they are never sources of truth |

---

## 2. Safety Net Replacement

| Rule | Detail |
|------|--------|
| **No net removed without replacement** | Any fix that removes an existing mechanism (cron, watchdog, fallback) MUST include a validated replacement |
| **Failure-mode validation** | The replacement mechanism MUST be tested under failure conditions before the original is removed |
| **Document the fallback** | Every repair step that removes something MUST include `**Fallback validated:**` with evidence |

---

## 3. Restart Protocol

| Rule | Detail |
|------|--------|
| **Post-restart validation** | Every restart MUST be followed by a data-path verification — not just process presence |
| **Verification sequence** | After restart: (1) confirm process alive, (2) confirm data flowing, (3) confirm expected output appearing |
| **No assumption of health** | Never declare a system healthy after a restart without completing the verification sequence |

---

## 4. Deadlock Prevention

| Rule | Detail |
|------|--------|
| **Hard limits are hard** | Concurrency limits (`maxInProgress`, slot counts) MUST be enforced strictly — race conditions must be anticipated |
| **Stale state timeout** | Any resource held in a transitional state for longer than a defined threshold MUST be force-released |
| **Slot audit before repair** | Before any repair session, audit all in-progress or locked resources and release stale ones |

---

## 5. Log Hygiene

| Rule | Detail |
|------|--------|
| **Silent logs are valuable** | A log with no entries during normal operation is more useful than a noisy one |
| **Dead processes must be decommissioned** | Any process producing recurring errors for a decommissioned component MUST be stopped |
| **Noise masks failure** | Log pollution delays crisis detection — clean logs are a maintenance obligation, not optional |

---

## 6. Repair Scope

| Rule | Detail |
|------|--------|
| **Read before touching** | Never modify a file during diagnosis — read only until the root cause is confirmed |
| **One fix at a time** | Apply one fix, validate, then proceed — never batch fixes under uncertainty |
| **Audit trail required** | Every repair action MUST be logged with timestamp, actor, and outcome |

---

## 7. Crisis Detection

| Rule | Detail |
|------|--------|
| **Silence is a signal** | A system that produces no output for longer than its expected cycle is in failure — silence must trigger investigation |
| **Watchdog obligation** | Any periodic mechanism (heartbeat, cron, watcher) MUST have an independent watchdog that detects and reports its absence |
| **First signal matters** | The tipping point of a failure cascade is always earlier than it appears — identify the first anomaly, not the most visible one |

---

## 8. Distributed Responsibility

| Rule | Detail |
|------|--------|
| **No singular blame** | System failures are always distributed across actors (human, agent, architecture) |
| **Architecture is an actor** | Design decisions that enabled the failure MUST be included in the responsibility map |
| **Shared lessons** | Every post-mortem conclusion applies to all actors — lessons are systemic, not individual |

---

## 10. Monorepo Package Extraction

| Rule | Detail |
|------|--------|
| **No standalone extraction without decision** | A package from the idae monorepo (or any workspace monorepo) MUST NOT be extracted into a standalone repo without a decision explicitly traced in Place de Grève |
| **Collision risk** | Extracting a package creates a duplicate `project:` entry in BMAD scan — the scan has no tiebreaker, resolution is undefined |
| **Decision ticket required** | The Place de Grève ticket MUST include: reason for extraction, target path, and whether the monorepo copy is to be archived or kept in sync |
| **Naming disambiguation** | If a standalone variant must coexist with a monorepo package, its `bmad/status.yaml` MUST use a distinct `project:` value (e.g. `idae-machine-statemachine` vs `idae-machine`) |

---

## 9. Panic Room Protocol

When a system enters unknown failure state, follow this sequence before any intervention:

```
1. FREEZE    — Stop all active repair attempts. Do not make changes.
2. SNAPSHOT  — Record current system state from raw sources only.
3. SCOPE     — Define the incident window (start timestamp → now).
4. ISOLATE   — Identify affected components. Mark unaffected components as safe.
5. ANALYZE   — Follow midnight-hell protocol (Section 16 of applications/README.md).
6. ONE FIX   — Apply the single highest-confidence fix. Validate before proceeding.
7. DOCUMENT  — Log every action with timestamp and outcome.
```

> **Never skip step 1.** Applying fixes to an unanalyzed system extends the failure.

