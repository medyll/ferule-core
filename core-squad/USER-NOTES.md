# Technical Specification: OpenClaw Master & Mission Orchestration (Unified)
# This document is a blueprint for the core-squad application

## 1. Executive Summary
This document defines the operational framework for the **core-squad** agent. It operates as a high-authority local orchestrator focused on infrastructure health and the management of the internal **core-squad-mission** (OCM-Mission) workflow. It utilizes a granular inheritance model for ephemeral Sub-Agents and a strict scope protection via the `ocm-` prefix.

## 2. Workspace & Naming Convention (Scope Protection)
All system-generated documents must use the `ocm-` prefix to distinguish platform-specific files from user project files.

| Purpose | Filename | Location |
| :--- | :--- | :--- |
| **User Commands** | `ocm-INSTRUCTIONS.md` | Root `/` |
| **Mission Monitoring** | `ocm-MISSION-QUEUE.md` | Root `/` |
| **Agent Reports** | `ocm-STATUS-REPORT.md` | Root `/` |
| **Sub-Agent Config** | `ocm-sub-[task_id].md` | `.openclaw/runtime/` |
| **System Audit Logs** | `ocm-audit-trail.log` | `.openclaw/runtime/` |
| **Backups** | `[name].ocm-bak` | Same as source |

## 3. Sub-Agent Inheritance & Delegation Model
Sub-Agents are specialized extensions spawned by the Master. They operate under strict "Parent-Child" laws:

* **Skill Inheritance**: No auto-inheritance. The Master must explicitly white-list `tools: []` for each child.
* **Context Inheritance**: Master injects a `context_fragment` and a mandatory `root_lock` (e.g., path restricted to a specific sub-folder).
* **Shadow Environment**: Sub-Agents inherit environment variables but are strictly forbidden from modifying them.
* **Reporting Pipe**: All telemetry must be redirected to `ocm-audit-trail.log`.

## 4. Mission Workflow Management (OCM-Mission)
The agent acts as the primary controller for the mission queue application.

* **Autonomous Discovery**: Upon startup, the Master must map the application logic (entry points, database schema, and loop mechanisms) using its file-read skills.
* **Mission Debugging**: For any failed task, the Master extracts parameters, spawns a `ocm-sub-debugger` in a sandbox, and attempts reproduction before patching.

## 5. User Interaction Protocol

### 5.1 Command & Shadow Mode
* **Interaction**: User orders are written in `ocm-INSTRUCTIONS.md`.
* **Simulation**: Use keyword `OCM-SIMULATE`. The Master outputs the plan in `ocm-STATUS-REPORT.md` and waits for `OCM-PROCEED` in the instructions file before action.

### 5.2 Reporting
The Master must summarize all technical actions into simplified French for the User within the `ocm-STATUS-REPORT.md` file.

## 6. Ticket ID Format

Format: `FAM-PROJ-NNNNN` — family (4 letters), project slug (6 chars max, kebab-case), 5-digit number.

| Family | Usage | Example |
|--------|-------|---------|
| `CORE-` | Core applications (`core-ferule/`) | `CORE-squad-00001` |
| `BMAD-` | BMAD dev projects (`D:\boulot\dev\`) | `BMAD-cv-mgr-00001` |
| `TECH-` | Technical debt (any app) | `TECH-cstds-00001` |
| `ISSUE-` | Bug reports (any app) | `ISSUE-cstds-00001` |

Project slug rules: 6 chars max, tirets autorisés, kebab-case. Exemples : `squad`, `cs-bas`, `id-idb`, `cv-mgr`.

---

## 6. Core Identity: core-squad
```markdown
# Agent: core-squad
- Role: Primary Orchestrator, Lead Developer & Human Liaison.
- Authority: Full local permissions within the project root.
- Capabilities: Sub-Agent Breeding, Mission Control, Self-Healing.
```

## 7. Unified Operational Skills (ocm-master-toolkit)
```markdown
---
name: ocm-master-toolkit
permissions:
  - filesystem:read-write (prefixed files only)
  - shell:bash-direct
  - agent_lifecycle:manage
  - mission_control:read-write
---

# Functions
- `spawn_ocm_specialist`: Configures and launches a specialized Sub-Agent.
- `inspect_mission_queue`: Monitors the OCM-Mission status.
- `rollback_snapshot`: Reverts changes if a Sub-Agent reports a failure.
- `patch_application_logic`: Fixes code within the OCM-Mission workflow.
- `translate_to_human`: Simplifies logs for the User.
```

## 8. Escalation & Self-Healing Workflow
1. **Level 1 (Direct)**: Master fixes simple issues or service restarts directly.
2. **Level 2 (Delegation)**: Master spawns `ocm-sub-[specialist]` for complex debugging.
3. **Level 3 (Escalation)**: If a Sub-Agent fails 3 times, or reports a "Critical Logic Conflict", the Master triggers a System Pause and marks `ocm-INSTRUCTIONS.md` with a `[CRITICAL_FAILURE]` tag for human intervention.