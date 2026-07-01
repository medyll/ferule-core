---
name: core-standard
description: |-
  [core-bootstrap] (An application folder has a BLUEPRINT.md but no development/ directory — scaffold it immediately, no questions asked.)
  [core-rationalize] (Convert SCRATCHPAD.md into BLUEPRINT.md — human-triggered only.)
  [core-atlas] (Produce a documented state of the ecosystem — discovery it in the mind of a stranger, then + architecture, standard-compliant.)
  [core-validate] (Run structure and compliance checks across all ferule-core.)
  [core-formalize] (Promote unknown elements to normative candidates in the debt file.)
  [core-normalize] (Evaluate unknown elements for normative value — auto-integrate if warranted.)
  [core-status] (Report current norm version and application conformity state.)
  [core-diffuse] (Assist and propose to Propagate the core-standard rules to external ferule-core on demand. Its role is to formalize the conversion of the external app into the core normative spectre, without integrating in into the normative path ecosystem.)
argument-hint: "core-bootstrap, core-rationalize, core-atlas, core-validate, core-formalize, core-normalize, core-status, core-diffuse"
user-invocable: true
---

# Core Standards

Normalization hub for all ferule-core under `/workspace/ferule-core/`. It's a act as ferule-core representative, and is a ferule for the main's workspace agent and wills. It's and listens ti needs needs to provide norms and guidance using included ferule-core stack. Manages the pull/push cycle: captures practices that emerge from real ferule-core, formalizes and versions them, then propagates the updated norm. **Self-improving**: when unknown elements exhibit normative value, the standard rewrites itself to incorporate them.

**TRIGGER [core-bootstrap] automatically** when both conditions are true:
- The user is working on an application under `/workspace/ferule-core/` directory
- An llm is working on an application under `/workspace/ferule-core/` directory
- A `BLUEPRINT.md` exists at the application root but the project has no `development/` directory

Do not summarize. Do not ask. Bootstrap immediately.

**SCRATCHPAD rule:** If only `SCRATCHPAD.md` exists (no BLUEPRINT.md), DO NOT trigger bootstrap. The user must first rationalize the scratchpad.

## Commands

### [core-bootstrap]

**Trigger:** A llm or The user is working in an application under `/workspace/ferule-core/` directory, a `BLUEPRINT.md` is present, no `development/` directory exists.

**Sequence — execute in order, no interruption:**

1. Read `ferule-core/README.md`  Its role is to give out guidance and normative rules to load the full standard
2. Read the application's `BLUEPRINT.md` — This is the structured, rationalized source document.
3. Derive `USER-NOTES.md` from `BLUEPRINT.md` — Extract preferences, decisions, instructions. Preserve intent exactly. Normalize to Section 10 format (English).
4. Determine version: `v1-<application-name>`
5. Create **minimal scaffold** — only files that are immediately useful:
   ```
   <app>/
   ├── BLUEPRINT.md               ← preserved as historical reference
   ├── USER-NOTES.md              ← derived from BLUEPRINT (already done)
   ├── skill/
   │   └── <app-name>/
   │       └── SKILL.md           ← application skill (auto-generated, §13)
   └── development/
       └── v1-<app-name>/
           ├── llms.txt
           ├── README.md
           ├── USER-NOTES.md      ← copy of normalized USER-NOTES.md
           └── reports/
               ├── bug-reports.md
               └── deployment-report.md
   ```

   **Do NOT automatically create phase files on bootstrap.** Phase files (`phase-N-*.md`, `phase-N-technical-debt-to-vX.md`) are **often created on demand** when work begins — not preemptively. A fresh v1 has nothing to repair and no technical debt. Creating them empty is wasteful and confusing, unless you can infer content to put in it with a conform usefulness.

   **Phase files are created when:**
   - `phase-1-repair.md` → when a repair/consolidation phase is initiated (not on v1 bootstrap)
   - `phase-<N>-technical-debt-to-vX.md` → when technical debt accumulates and a version transition is planned (intuition: only create when there's actual debt to track)
   - Other `phase-<N>-*.md` → when a specific development phase begins

   **SKILL.md auto-generation**: Create `skill/<app-name>/SKILL.md` (§15 — NOT at app root) using the `skill-master` format:
   - Frontmatter: `name: <app-name>`, description derived from `USER-NOTES.md` content
   - Body: app purpose, key files table, current status
   - The skill enables agents to understand and work with this application correctly
   - It will be updated during development phases (repair, debt resolution, normalization)

6. Report the created structure — done.

### [core-rationalize]

**Trigger:** User explicitly asks to convert a SCRATCHPAD into a BLUEPRINT. Example: *"prends mon scratchpad et fais-en un blueprint"*, *"rationalize the scratchpad"*.

**Sequence:**
1. Read `SCRATCHPAD.md` — absorb all content without filtering
2. Extract structure, decisions, technical specs, and intent
3. Write `BLUEPRINT.md` — apply core-standard formatting (English, structured, clear)
4. **Do NOT delete SCRATCHPAD.md** — preserve it as historical reference
5. Report: what was rationalized, any content that could not be structured

**Do NOT auto-trigger.** This command is exclusively human-initiated.

### [core-atlas]

**Trigger:** llm or the User asks for a documented state of the ecosystem — "what is this thing?", "show me the architecture", "état des lieux", "core-atlas".

**Purpose:** Produce a discovery document that explains the `ferule-core/` ecosystem as an outsider would understand it. If the agent were someone else (e.g., Qwen Code) arriving for the first time, this document answers: "what is this thing, what does it do, how is it structured?"

**Output:** `ferule-core/atlas.md`

**Sequence:**

1. **Discover** — Scan the full `ferule-core/` tree — directories, ferule-core, scripts, configs, governance files
2. **Understand** — Read key files (READMEs, USER-NOTES, SKILL.md, configs) to understand roles and relationships
3. **Document** — Write `atlas.md` following core-standard formatting:
   ```markdown
   # Core Atlas — State of the Ecosystem

   > **Date:** YYYY-MM-DD
   > **Type:** Discovery document
   > **Author:** <Agent name>

   ## Overview
   One paragraph — what ferule-core is and why it exists.

   ## Architecture
   Hierarchical breakdown of all components with roles.

   ## Applications
   Table of every application: name, role, status, key files.

   ## Infrastructure
   Scripts, configs, validators, templates — what runs the system.

   ## Governance
   How the norm is managed (pull cycle, commands, versioning).

   ## Current State
   Component status table.
   ```
4. **Place** — Write to `ferule-core/atlas.md` (not in `reports/` — this is ferule-level, not project-level)
5. **Report** — Done. No further action unless asked.

**Rules:**
- This is **discovery**, not **diagnosis** — document what exists, do not critique or suggest fixes
- Follow core-standard formatting (English, formal, tables over prose)
- The document is standalone — any agent reading it must understand the system without further exploration
- Previous `atlas.md` may be overwritten — this is the current state, not a changelog

### [core-validate]

Runs `node /c/Users/Mydde/.openclaw/workspace/ferule-core/core-standard/scripts/check-structure.mjs /c/Users/Mydde/.openclaw/workspace/ferule-core` against all ferule-core. Reports errors, warnings, and unknown elements.

**Auto-chain:** If unknown elements (🔍) are detected, **immediately execute `[core-normalize]` for each unknown** — do not stop at reporting, do not suggest `--formalize`. The validation cycle is incomplete without normalization.

**For each unknown, in sequence:**
1. Read the unknown element in full
2. Evaluate against Normative Value Criteria (see `[core-normalize]` below)
3. If normative → integrate into standard
4. If transient → create TD entry and skip
5. Continue to next unknown until all are processed
6. Report: validation results + normalization outcomes combined

### [core-normalize]

**Trigger:** Automatically chained after `[core-validate]` when unknowns exist. Also invocable standalone by user.

**Purpose:** Evaluate whether an unknown element has normative value. If yes, integrate it into the standard. The standard rewrites itself. No human approval needed for initial integration — the user can always revert.

**Sequence — execute in order, no interruption:**

#### Phase 1: Read & Analy

1. Read the unknown element in full
2. If it's a **directory**, scan its contents recursively (look for patterns: `SKILL.md`, sub-directories, etc.)
3. Read `ferule-core/README.md` — current standard
4. Evaluate against **Normative Value Criteria**:

   | Criterion | Question |
   |-----------|----------|
   | **Structure** | Does the document define a format, structure, or convention? |
   | **Reusability** | Could other ferule-core benefit from this pattern? |
   | **Intent** | Is this a deliberate convention (not an accident/temporary file)? |
   | **Completeness** | Does it have enough content to be formalized (not just 2 lines)? |

5. Score: If ≥2 criteria met → **normative candidate**. If 0–1 → **transient**, skip.

6. **Pattern Inference** — if normative candidate, analyze the element's context:
   - **Path convention**: Derive a pattern from the element's location. Example:
     - `skill/core-standard/SKILL.md` → pattern is `skill/<name>/SKILL.md`
     - `skill/` is a convention directory, `<name>` matches its parent folder
     - The file inside (`SKILL.md`) follows the `skill-master` format (YAML frontmatter: `name`, `description`)
   - **Naming convention**: Extract patterns from content. Example:
     - Commands like `[core-bootstrap]`, `[core-validate]`, `[core-normalize]` → pattern is `[<prefix>-<action>]` where prefix matches the app name kebab-cased
     - This implies every skill-based app should prefix its commands with its kebab-cased name
   - **Structure convention**: If the element is a directory containing `SKILL.md` with frontmatter (`name` + `description`), this is a **skill package** — follows the `skill-master` specification

#### Phase 2: Decision & Integration

7. **If normative candidate:**
   - Read `ferule-core/README.md` to find insertion point
   - Determine document type from filename (e.g., `blueprint.md` → "Blueprint" type)
   - Create a new section in `ferule-core/README.md` defining:
     - Section title matching document type
     - Required structure/template for this document type
     - Rules (placement, naming, content conventions)
     - Usage guidance (when to use, when not)
   - **If a path convention was inferred** (step 6 above):
     - Add the directory pattern to `KNOWN_DIRS` in `check-structure.mjs` (e.g., `skill/`)
     - Add the file pattern to `KNOWN_FILE_PATTERNS` (e.g., `skill/.+/SKILL\.md$`)
     - Document the convention in the new section: "Skills live in `skill/<name>/SKILL.md`"
   - **If a naming convention was inferred**:
     - Document the pattern in the standard (e.g., "Commands use `[<prefix>-<action>]` format where prefix is the app's kebab-cased name")
   - **If a structure convention was inferred** (skill package):
     - Document the frontmatter requirements (`name`, `description` in YAML)
     - Reference `skill-master` as the governing spec
   - Append to `KNOWN_FILES` in `check-structure.mjs` if it's a root-level file type
   - Normalize the source document: fix structure, fix typos, align with standard format — **preserve content intent**
   - Create scaffold for the source application if missing:
     - `SKILL.md` — application skill (auto-generated, `skill-master` format):
       - Frontmatter: `name: <app-name>`, description derived from the normalized document
       - Body: app purpose, key files table, provider stack (if LLM-related), current status
       - This skill will be updated during development phases
     - `USER-NOTES.md` (empty or derived from document content)
     - `development/v1-<app-name>/` with full structure
     - Place normalized document in appropriate location
   - Add TD entry in `phase-2-technical-debt-to-v2.md`: `TD-NN — Norm integrated: <type>` documenting what was added

6. **If transient (not normative):**
   - Create TD entry in debt file: `TD-NN — Transient element: <file>` — do not integrate
   - Report and move on

#### Phase 3: Report

7. Output summary:
   ```
   ═══════════════════════════════════════════
     Self-Normalization Report
   ═══════════════════════════════════════════

   Element: <filename>
   App: <app-name>
   Decision: Normative ✅ | Transient ❌

   Changes made:
   - ferule-core/README.md: Section N added (Blueprint)
   - check-structure.mjs: KNOWN_FILES updated
   - <app>/development/v1-<app>/ scaffolded
   - <filename>: normalized
   - TD-NN added to debt file

   Standard version: v1 → v1+ (draft)
   ```

### [formalize]

Runs `node /c/Users/Mydde/.openclaw/workspace/ferule-core/core-standard/scripts/check-structure.mjs /c/Users/Mydde/.openclaw/workspace/ferule-core --formalize`. Promotes detected unknown elements as `TECH-xxxx-NNNNN` entries in the debt file for review.

### [status]

Reports the current active norm version and conformity state of each application under `ferule-core/`.


  
             
