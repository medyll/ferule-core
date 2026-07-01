# PROMPT TEMPLATES — Agent Startup Heuristics

> Standardized prompt templates for consistent agent behavior across all applications.
> See `applications/README.md` Section 13.2 — Agent Startup Heuristic.

---

## Project Initialization Template

Use when an agent is starting work on a new project.

```
You are working on a project under applications/<app-name>/development/<version>-<project-id>/.

Follow this mandatory sequence before taking any action:

1. Read `llms.txt` — identify project type, structure, and available documents
2. Read `README.md` — gather overview, status, and file map
3. Read `USER-NOTES.md` — apply user instructions and preferences
4. Read phase files listed in README — understand current work and status
5. Cross-reference your task against gathered documentation

Do NOT skip any step. If any file is missing, report it and proceed with best judgment.
```

---

## Phase Transition Template

Use when moving from one phase to the next or from one version to the next.

```
You are transitioning from <current-state> to <next-state>.

Before proceeding:
1. Confirm all checkboxes in the current phase file are either ✅ or have a reason for being left open
2. Check the technical debt file (`phase-N-technical-debt-to-v<X>.md`) for open items
3. If transitioning versions:
   a. Scaffold the new version folder per Section 12 of the standard
   b. Transfer all open debt items to `phase-1-repair.md` of the new version
   c. Add back-references in the old version's TD file
4. Update the README.md status line to reflect the new state
5. Log the transition in today's `memory/YYYY-MM-DD.md`
```

---

## Conformance Check Template

Use when validating a project against the standard.

```
You are performing a conformance check on <project-path>.

Checklist:
- [ ] `llms.txt` exists and contains doc map
- [ ] `README.md` exists and follows Section 2 structure
- [ ] `USER-NOTES.md` exists and is in English
- [ ] Phase files follow `phase-N-<slug>.md` naming
- [ ] `reports/` directory exists
- [ ] `reports/bug-reports.md` exists (even if empty)
- [ ] `phase-N-technical-debt-to-v<X>.md` exists
- [ ] BUG-NNN IDs are sequential (if any bugs exist)
- [ ] TD-NN IDs are sequential (if any debt items exist)
- [ ] No headers deeper than `###`
- [ ] All code blocks are fenced with language tags

Report violations with file paths and specific line references.
```
