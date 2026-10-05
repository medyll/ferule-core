# PHASE 1 — Standard Consolidation

> Audit existing applications, resolve inconsistencies, create enforcement tools, and propagate the unified standard.

---

### 1.1 — Audit Existing Application Structures

**File:** `ferule-core/mission-queue/`, `ferule-core/openclaw-master/`
**Problem:** No systematic audit of conformance to the standard has been performed.
**Risk:** Inconsistencies accumulate, making future migration harder.

- [x] Analyze `mission-queue` V3/V4 structure — document deviations
- [x] Analyze `openclaw-master` V1 structure — document deviations
- [x] Cross-reference with `ferule-core/README.md` standard
- [x] Produce inconsistency report (completed during analysis phase)

**Effort:** 15 min

---

### 1.2 — Resolve Inconsistencies — Define Unified Spec

**File:** `ferule-core/README.md`
**Problem:** Several inconsistencies exist across applications that the standard must accommodate or prohibit.
**Risk:** Ambiguous conventions lead to drift.

**Identified inconsistencies:**

| # | Issue | Found in | Resolution |
|---|-------|----------|------------|
| 1 | Phase file numbering not sequential (`phase-5-technical-debt.md` after phase-4) | v3-mission-queue | **Prohibit** — phase numbers must be sequential. TD file uses next available number |
| 2 | TD file missing version suffix (`phase-5-technical-debt.md` vs `phase-5-technical-debt-to-v4.md`) | v3-mission-queue | **Require** `to-v<N>` suffix for clarity |
| 3 | Non-standard subdirectory (`midnight-hell/`) | v4-mission-queue | **Allow** for ad-hoc working dirs but document as non-standard — should migrate to `archives/` or `reports/` |
| 4 | Extra descriptor in phase file name (`phase-1-repair-monitoring-log.md`) | v4-mission-queue | **Allow** — descriptor adds clarity, doesn't break parsing |
| 5 | Missing `llms.txt` doc map structure | v1-openclaw-master | **Require** — add placeholder doc map |
| 6 | Bug reports use minimal placeholder format | v1-openclaw-master, v4-mission-queue | **Allow** for empty state — full template required when bugs exist |
| 7 | `reports/` directory missing in some projects | general | **Require** — must exist even if empty |

**Actions:**
- [x] Document all inconsistencies with resolutions
- [x] Update `ferule-core/README.md` to clarify edge cases (non-standard dirs, empty reports)
- [x] Add conformance checklist for new project scaffolding

**Effort:** 15 min

---

### 1.3 — Create `.markdownlint.json` for Workspace-Wide Linting

**File:** `ferule-core/.markdownlint.json`
**Problem:** No automated enforcement of Section 7 markdown rules.
**Risk:** Headers deeper than `###`, unfenced code blocks, and other violations go undetected.

- [ ] Create `.markdownlint.json` at `ferule-core/` root
- [ ] Enforce: no headers deeper than `###` (MD025, MD001)
- [ ] Enforce: fenced code blocks required (MD040, MD046)
- [ ] Enforce: consistent date format (custom rule if possible)
- [ ] Add to workspace root so all projects inherit rules

**Effort:** 10 min

---

### 1.4 — Create `check-structure.mjs` Validator Script

**File:** `ferule-core/scripts/check-structure.mjs`
**Problem:** No automated verification that `BUG-NNN` and `TD-NN` IDs are sequential and not duplicated.
**Risk:** ID collisions and gaps make auditing unreliable.

- [ ] Create script that scans all project folders under `ferule-core/`
- [ ] Verify: `llms.txt`, `README.md`, `USER-NOTES.md` exist in each project
- [ ] Verify: `reports/` directory exists in each project
- [ ] Extract and validate `BUG-NNN` sequences (must be sequential, no gaps, no duplicates)
- [ ] Extract and validate `TD-NN` sequences (same rules)
- [ ] Output: pass/fail per project with specific violations
- [ ] Zero external dependencies — pure Node.js

**Effort:** 30 min

---

### 1.5 — Create `PROMPT-TEMPLATES.md` for Agent Startup

**File:** `ferule-core/core-standards/development/v1-core-standards/PROMPT-TEMPLATES.md`
**Problem:** Agents don't consistently follow Section 13.2 Startup Heuristic.
**Risk:** Inconsistent project reading leads to missed instructions or wrong assumptions.

- [ ] Create "Project Initialization" template
- [ ] Create "Phase Transition" template
- [ ] Include mandatory sequence: `llms.txt` → `README.md` → `USER-NOTES.md` → phase files
- [ ] Reference in standard as recommended practice

**Effort:** 15 min

---

### 1.6 — Propagate Standard to Existing Applications

**File:** `ferule-core/mission-queue/`, `ferule-core/openclaw-master/`
**Problem:** Existing applications don't fully conform to V1 standard.
**Risk:** Drift continues, standard becomes theoretical rather than enforced.

- [x] Update `openclaw-master/v1-openclaw-master/llms.txt` to use full doc map structure
- [x] Create missing `reports/` directories where absent
- [x] Add technical debt file to `openclaw-master/v1-openclaw-master/`
- [x] Add technical debt file to `mission-queue/v4-mission-queue/`
- [x] Fix header depth violations in `mission-queue/v3-mission-queue/phase-1-repair.md`
- [x] Update READMEs to reference new TD files

**Effort:** 30 min

---

## Summary

| Step | Task | Effort | Status |
|------|------|--------|--------|
| **1.1** | Audit existing application structures | 15 min | ✅ Done |
| **1.2** | Resolve inconsistencies — define unified spec | 15 min | ✅ Done |
| **1.3** | Create `.markdownlint.json` for linting | 10 min | ✅ Done |
| **1.4** | Create `check-structure.mjs` validator | 30 min | ✅ Done |
| **1.5** | Create `PROMPT-TEMPLATES.md` | 15 min | ✅ Done |
| **1.6** | Propagate standard to existing applications | 30 min | ✅ Done |
