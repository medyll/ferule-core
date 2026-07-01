# Applications — Structure Standard

> Part A of the Applications norm. Defines what every project must contain.
> Governed by `core-standard`. See [README.md](./README.md) for index.

---

## 1. Directory Structure

```
application-core/
└── <application-name>/
    ├── SCRATCHPAD.md                                        ← Freeform capture (REQUIRED at app root, §14)
    ├── USER-NOTES.md                                         ← User instructions (REQUIRED at app root)
    ├── skill/
    │   └── <application-name>/
    │       └── SKILL.md                                     ← Application skill (REQUIRED, §13)
    ├── contexts/                                            ← (optional) Domain-specific content
    ├── sources/                                             ← (optional) Reference material (saved web pages, transcripts, raw documents)
    ├── assets/                                              ← (optional) Binary media (images, video, audio)
    ├── DEPENDENCIES.md                                      ← (optional) Cross-application dependency map
    └── development/
        └── <version>-<project-id>/
            ├── llms.txt                                     ← Machine-readable index (REQUIRED)
            ├── README.md                                    ← Index & overview
            ├── USER-NOTES.md                                ← Mirror of app-root USER-NOTES.md
            ├── phase-1-<slug>.md                            ← Phase documents (sequential)
            ├── phase-2-<slug>.md
            ├── phase-N-<slug>.md
            ├── phase-N-<slug>-openspace.md                  ← Discussion file per phase
            ├── phase-<N>-technical-debt-to-v<X>.md          ← Technical debt (REQUIRED for next version planning)
            ├── archives/
            │   └── openspace/                               ← Archived discussion files
            └── reports/
                ├── bug-reports.md                           ← All bugs for this project
                └── deployment-report.md                     ← Final deployment summary
```

### Rules

| Rule | Detail |
|------|--------|
| **Root** | `application-core/<app-name>/` — one folder per application domain |
| **Development** | `development/<project-id>/` — one folder per project/version |
| **Project ID** | `<version>-<project-id>` — kebab-case. Version uses no dots: `v3`, `v2`, `v1` |
| **Phases** | Numbered sequentially: `phase-1-<slug>.md`, `phase-2-<slug>.md` |
| **Reports** | All post-execution artifacts go in `reports/`. Investigation sub-folders allowed: `reports/<topic>/` |
| **README** | Every project MUST have a `README.md` at its root |
| **USER-NOTES.md** | Every application MUST have a `USER-NOTES.md` at app root — even if empty |
| **SCRATCHPAD.md** | Every application MUST have a `SCRATCHPAD.md` at app root — even if empty. This is the freeform capture file for raw ideas and thinking before rationalization |
| **sources/** | Optional app-root directory for reference material — saved web pages, transcripts, raw documents that inform the application's domain |
| **Unknown elements** | Any element not covered by this standard is a normative candidate — process through `core-standard` |

---

## 2. README.md Structure

> Template: [core-standard/development/v1-core-standard/templates/readme-template.md](core-standard/development/v1-core-standard/templates/readme-template.md)

### Rules

| Rule | Detail |
|------|--------|
| **Date format** | `YYYY-MM-DD` only |
| **Status line** | Single line with emoji: ✅ done, 📋 planned, 🔄 in progress, ⏸️ paused |
| **Sources** | Always list source files with workspace-relative paths in backticks |
| **Structure table** | Links to all phase files + reports, one-line descriptions |
| **Summary table** | One row per task step, with effort estimate and dependency |
| **System state** | Final section with component status — only if system is live |
| **No trailing content** | Keep README scannable. Details belong in phase files |

---

## 3. Phase File Structure

> Template: [core-standard/development/v1-core-standard/templates/phase-template.md](core-standard/development/v1-core-standard/templates/phase-template.md)

### Rules

| Rule | Detail |
|------|--------|
| **Header** | `# PHASE N — <TITLE>` — uppercase, numbered |
| **Blockquote context** | Single `>` line under the header |
| **Step header** | `### N.N — <Title>` — three `#`, numbered step |
| **Metadata fields** | `**File:**`, `**Problem:**`, `**Risk:**` — bold labels, inline values |
| **Effort** | `**Effort:** X min` — always at end of step |
| **Checkboxes** | **Agents MUST update checkboxes on every task.** `- [ ]` pending, `- [x]` done, `- [~]` in progress |
| **Separator** | `---` between each step |
| **Code blocks** | Fenced with language tag |
| **Paths** | Always in backticks |

---

## 4. Bug Report Structure

> Template: [core-standard/development/v1-core-standard/templates/bug-report-template.md](core-standard/development/v1-core-standard/templates/bug-report-template.md)

Location: `reports/bug-reports.md`

### Rules

| Rule | Detail |
|------|--------|
| **Bug ID** | `ISSUE-xxxx-NNNNN` — family `ISSUE`, project slug (6 chars max), 5-digit number |
| **Severity** | One of: 🔴 Critical, 🟡 Medium, 🟢 Low |
| **Metadata block** | Date, Severity, File, Function, Discovered by — all required |
| **Sections** | Symptom → Root Cause → Impact → Test Case → Fix Required → Status |
| **Test Case** | Triple backtick block with Input/Expected/Actual |
| **Deployed** | Always include timestamp (~HH:MM) and who fixed it |
| **Summary table** | End of file: ID, Severity, Status, Fixed By |

---

## 5. Technical Debt Structure

> Template: [core-standard/development/v1-core-standard/templates/technical-debt-template.md](core-standard/development/v1-core-standard/templates/technical-debt-template.md)

### Rules

| Rule | Detail |
|------|--------|
| **Debt ID** | `TECH-xxxx-NNNNN` — family `TECH`, project slug (6 chars max), 5-digit number |
| **Metadata** | Discovered, File, Issue, Impact, Risk — all required |
| **Risk level** | Single word: Low, Medium, High |
| **Status** | Inferred from checkbox: `- [x]` = done, `- [ ]` = open |
| **Summary table** | End of file: ID, Item, Effort, Status |

---

## 6. Deployment Report Structure

> Template: [core-standard/development/v1-core-standard/templates/deployment-report-template.md](core-standard/development/v1-core-standard/templates/deployment-report-template.md)

Location: `reports/deployment-report.md`

### Rules

| Rule | Detail |
|------|--------|
| **Title** | `<PROJECT> — DEPLOYMENT SUCCESS` — uppercase |
| **Status line** | Emoji + ALL CAPS: 🟢 FULLY OPERATIONAL, 🟡 DEGRADED, 🔴 FAILED |
| **Tables** | Bug status + System state — always include both |
| **Test Results** | Monospace block — raw output, not interpreted |
| **Lessons Learned** | Numbered list — each item is one clear sentence |

---

## 7. General Markdown Rules

| Rule | Detail |
|------|--------|
| **Language** | English only |
| **Author attribution** | Every written entry MUST identify the author |
| **Tone** | Formal. No humor, no casual language |
| **Headers** | `#` title, `##` sections, `###` sub-items. No deeper than `###` |
| **Emojis** | Status only: ✅ 📋 🔄 ⏸️ 🔴 🟡 🟢 ⏳ |
| **Code blocks** | Always fenced with language tag |
| **Paths** | Backticks |
| **Separators** | `---` between major sections |
| **Tables** | Use for summaries, not detailed step content |
| **No paragraphs > 2 sentences** | Keep it scannable |

---

## 8. Naming Conventions

| Item | Convention | Example |
|------|-----------|---------|
| **Application folder** | kebab-case | `place-de-greve` |
| **Project folder** | `<version>-<project-id>` | `v3-place-de-greve` |
| **Phase files** | `phase-N-<slug>.md` | `phase-1-repair.md` |
| **Bug IDs** | `ISSUE-xxxx-NNNNN` | `ISSUE-cstds-00003` |
| **Debt IDs** | `TECH-xxxx-NNNNN` | `TECH-cstds-00007` |
| **Mission IDs** | `<PREFIX>-NNN` | `PWA-005` |
| **Dates** | `YYYY-MM-DD` | `2026-04-09` |
| **Reports folder** | `reports/` | Always lowercase |

---

## 9. Discussion & OpenSpace Convention

### Rules

| Rule | Detail |
|------|--------|
| **File naming** | `phase-<N>-<title>-openspace.md` |
| **Location** | Alongside the phase file |
| **Hard limit** | If file exceeds 300 lines → archive |
| **Archive path** | `archives/openspace/<original-filename>-<YYYY-MM-DD>.md` |
| **Link in current file** | Add archive link at the top of the new empty file |
| **Tone** | Formal. See §7. |
| **Author attribution** | Required on every entry |

---

## 10. USER-NOTES.md — User Instructions

> Template structure: `# USER-NOTES — <Project Name>` / `## Preferences` / `## Decisions` / `## Instructions`

### Rules

| Rule | Detail |
|------|--------|
| **Language** | English only |
| **Agent enforcement** | Non-conformant file → MUST correct immediately, preserving intent |
| **Pre-scaffold normalization** | If `BLUEPRINT.md` exists → normalize from BLUEPRINT. If only `SCRATCHPAD.md` exists → user must first rationalize it to BLUEPRINT (human-triggered) |
| **Scaffold detection** | `USER-NOTES.md` at app root + no `development/` → unconditional scaffold |
| **Location** | App root, alongside `README.md` |
| **Not a log** | Instructions only — discussion goes in openspace |

---

## 11. Technical Debt File — Mandatory for Version Planning

### Rules

| Rule | Detail |
|------|--------|
| **Naming** | `phase-<N>-technical-debt-to-v<X>.md` |
| **Required** | MUST exist in every project that has phase files — fresh v1 bootstraps exempt |
| **Summary table** | End of file: ID, Item, Effort, Status |
| **Archive on version transition** | Add `→ Addressed in v<X>` reference to each transferred item |

---

## 12. Version Transition — Scaffolding the Next Version

### Rules

| Rule | Detail |
|------|--------|
| **Naming** | `v<N+1>-<project-id>` |
| **Debt transfer** | All open TD items → `phase-1-repair.md` of new version |
| **Back-link** | Each transferred item → reference new version |
| **Preserve history** | Never delete old version folder |
| **User confirmation** | Present new structure after scaffolding |

---

## 13. Skill Convention

### Structure

```
<application-name>/
└── skill/
    └── <application-name>/
        └── SKILL.md
```

### SKILL.md Format

```markdown
---
name: <application-name>
description: |-
  [command] (Short description.)
argument-hint: "command1, command2"
user-invocable: true|false
---
```

### Rules

| Rule | Detail |
|------|--------|
| **Required** | Every application MUST have `skill/<app-name>/SKILL.md` |
| **Location** | `<application-name>/skill/<application-name>/SKILL.md` |
| **Front matter** | `name`, `description`, `argument-hint`, `user-invocable` — all required |
| **Startup heuristic** | Any skill operating on an application MUST execute the §15.2 startup sequence before any write action |
| **Response tag** | Every user-facing response from a skill MUST begin with a structured identity tag: `[<app-name>:skill v<N> | core-standard v<X> | type: <command>]` |

### 13.1 Response Tag

When a skill produces a user-facing response (any command output, status report, atlas, validate, normalize, etc.), the response MUST begin with a structured identity tag:

```markdown
[<app-name>:skill v<N> | core-standard v<X> | type: <command>]
```

| Segment | Example | Purpose |
|---------|---------|---------|
| `<app-name>:skill` | `core-cognition:skill` | Identifies which skill is responding |
| `v<N>` | `v1.0` | Application version |
| `core-standard v<X>` | `core-standard v1` | Active norm version |
| `type: <command>` | `type: atlas` | Command or action type |

**Examples:**

| Skill responding | Tag |
|-----------------|-----|
| `core-cognition` | `[core-cognition:skill v1.0 | core-standard v1 | type: atlas]` |
| `place-de-greve` | `[place-de-greve:skill v3.0 | core-standard v1 | type: scan]` |
| `formal-ideation` | `[formal-ideation:skill v1.0 | core-standard v1 | type: brainstorm]` |

**Rules:**
- Tag is the **first line** of any user-facing response
- No greeting, no preamble before the tag
- Tag uses the app's kebab-cased name + `:skill` suffix
- Version `v<N>` matches the app's current development version (from `development/v<N>-...`)

---

## 13.2 DEPENDENCIES.md — Cross-Application Dependencies

Optional app-root file for tracking dependencies between applications.

```markdown
# <App Name> — Dependencies

| App | Type | Notes |
|-----|------|-------|

```

### Rules

| Rule | Detail |
|------|--------|
| **Location** | App root: `<app-name>/DEPENDENCIES.md` |
| **Types** | `required` (blocks operation), `optional` (enhanced features), `data` (consumes output) |
| **Validator** | Known element — not flagged as unknown |

---

## 13.3 assets/ — Binary Media

Optional app-root directory for binary media files.

### Rules

| Rule | Detail |
|------|--------|
| **Location** | App root: `<app-name>/assets/` |
| **Supported formats** | `.png`, `.jpg`, `.gif`, `.mp4`, `.webm`, `.svg`, `.mp3`, `.wav` |
| **References** | Use relative paths in markdown: `![image](./assets/file.png)` |
| **Validator** | Known directory — not flagged as unknown |

---

## 17. protocol.json — Inter-App Communication

Optional app-root file declaring inter-application protocol: participants, event types, and routing rules.

### Rules

| Rule | Detail |
|------|--------|
| **Location** | App root: `<app-name>/protocol.json` |
| **Structure** | JSON with `participants[]`, `event_types[]`, and `routing` sections |
| **Participants** | Each declares `name`, `domain`, and `capabilities[]` (emit/handle prefixes) |
| **Event types** | Each declares `type`, `description`, and `payload_required[]` |
| **Routing** | Handlers declared via `handle:<event_type>` capability — unrouted events are logged, no silent drops |
| **Validator** | Known element — not flagged as unknown |

---

## 16. context-registry.json — Domain Routing

Optional app-root file for applications that route across multiple contexts/domains.

### Rules

| Rule | Detail |
|------|--------|
| **Location** | App root: `<app-name>/context-registry.json` |
| **Structure** | JSON array of domain objects with `prefix`, `label`, `description`, `basePath`, `statusFile`, `statusFormat`, `watchPattern`, `resolveStrategy` |
| **Validator** | Known element — not flagged as unknown |

---

## 8.1 Root File Casing Rule

| Rule | Detail |
|------|--------|
| **Allowed uppercase at root** | `README.md`, `USER-NOTES.md`, `BLUEPRINT.md`, `SCRATCHPAD.md`, `DEPENDENCIES.md` |
| **Allowed mixed-case at root** | `llms.txt` (lowercase `llms`), `context-registry.json`, `domain-registry.json` |
| **All other files** | Must be lowercase and live in a sub-folder (`templates/`, `reports/`, `archives/`, `assets/`, `sources/`) |

---

## 3.1 Safety Net Replacement Rule

Any repair step that removes an existing mechanism MUST include:

- `**Fallback validated:**` — evidence that the replacement works under failure conditions
- This field is mandatory for any step with a `removes` or `replaces` action

---

## 3.2 Post-Restart Health Check Template

Any restart procedure MUST include a data-path verification step:

1. **Process Check** — verify PID is running
2. **Health Check** — run scanner, confirm `health: "healthy"`
3. **Log Verification** — check last 10 lines for `ERROR` or `FATAL`

"Process alive" is NOT proof of "system functional."

---

## 14. SCRATCHPAD.md — Pre-scaffold Capture

### Purpose

`SCRATCHPAD.md` is a **freeform, unstructured capture file** at the application root. It holds raw notes, brain dumps, half-formed ideas, and evolving thinking — before any rationalization occurs.

### Rules

| Rule | Detail |
|------|--------|
| **Location** | App root only: `<app-name>/SCRATCHPAD.md` |
| **Language** | No enforcement — user writes freely, in any language |
| **Structure** | None. Tables, code, prose, bullet lists, whatever works. |
| **Agent behavior** | Agent MAY tidy or reorganize the file **if asked**, but MUST NOT auto-normalize it. The transition from SCRATCHPAD to BLUEPRINT is **exclusively human-triggered**. |
| **Lifecycle** | Created by user at any time. Preserved after scaffold. Never deleted automatically. |
| **Validator** | Known element — not flagged as unknown by `check-structure.mjs` |

---

## 15. Blueprint — Pre-Scaffold Planning Document

### Purpose

`BLUEPRINT.md` is the **normalized, structured output** derived from `SCRATCHPAD.md`. It is the rationalized document that is ready for scaffold transition. The user triggers the rationalization: *"prends mon scratchpad et fais-en un blueprint"*.

### Rules

| Rule | Detail |
|------|--------|
| **Location** | App root only: `<app-name>/BLUEPRINT.md` |
| **Origin** | Derived from `SCRATCHPAD.md` via agent rationalization (human-triggered) |
| **Language** | English — must conform to core-standard formatting |
| **Lifecycle** | Created when user decides the SCRATCHPAD is ready. Preserved after bootstrap. Never deleted automatically. |
| **Relationship** | `SCRATCHPAD.md` → (human triggers rationalization) → `BLUEPRINT.md` → (core-bootstrap) → `USER-NOTES.md` |
| **Agent behavior** | Read-only after bootstrap — MUST NOT be rewritten |
| **Validator** | Known element — not flagged as unknown by `check-structure.mjs` |

---

## 16. Centralized Workspace Config — `config/` Directory

### Purpose

Some applications under `application-core/` serve as orchestrators or engines for the broader workspace. For these applications, configuration is not local to individual projects — it is centralized in a `config/` directory at the application root, governing behavior across all known applications.

### Rules

| Rule | Detail |
|------|--------|
| **Location** | Application root only: `<app-name>/config/` |
| **Purpose** | Centralized workspace configuration — engine settings, role definitions, known applications, cross-app hooks |
| **Format** | YAML files (`.yaml`) — one per domain (e.g., `engine.yaml`, `roles.yaml`, `workspace.yaml`) |
| **Content** | Deterministic settings: routing, thresholds, identity pools, application paths, hook targets |
| **Consumption** | Read by the application's skill (SKILL.md) and/or CLI scripts at runtime |
| **Validator** | Known element — `config/` directory and `.yaml` files inside are not flagged as unknown |
| **Not for every app** | Only applications that orchestrate other applications need a `config/` directory. Regular development projects use their own `status.yaml` and `config.yaml` in `./bmad/` or equivalent. |

### Standard Config Files

| File | Domain |
|------|--------|
| `config/engine.yaml` | Engine behavior: ACP availability, chain protocol, test enforcement, logging |
| `config/roles.yaml` | Role definitions, harness mapping, agent identity pools |
| `config/workspace.yaml` | Known applications, paths, cross-workflow hooks |

### Usage Guidance

- Use `config/` when an application needs to **orchestrate** or **coordinate** other applications
- Do NOT use for per-project configuration — those belong in the project's own context folder (e.g., `./bmad/config.yaml`)
- Config files are **machine-readable first** — SKILL.md and scripts consume them directly
- Changes to `config/` should be documented in `USER-NOTES.md` with decision rationale
