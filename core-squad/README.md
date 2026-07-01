# OpenClaw Master

Primary Orchestrator & Mission Control System for the OpenClaw platform.

## Overview

OpenClaw Master (`core-squad`) acts as a high-authority local orchestrator focused on:

- **Infrastructure health monitoring**
- **Mission queue management** (OCM-Mission workflow)
- **Sub-Agent spawning and delegation**
- **Autonomous mission execution** (Place de Grève protocol)
- **User interaction via file-based command interface**

## Quick Start

### Prerequisites

- Node.js >= 18.0.0

### Installation

```bash
# Navigate to the project directory
cd core-squad

# Initialize the system (first run)
node index.mjs
```

### Usage

#### 1. User Commands

Write your commands in `ocm-INSTRUCTIONS.md`:

```markdown
## Active Instructions
- Deploy the new feature to production
- OCM-SIMULATE: Run a test deployment first
```

#### 2. Simulation Mode

Use `OCM-SIMULATE` to preview actions without execution:

```markdown
- OCM-SIMULATE: Check system health and report issues
```

The Master will write the execution plan to `ocm-STATUS-REPORT.md` and wait for `OCM-PROCEED`.

#### 3. Execute Planned Operations

After simulation, add `OCM-PROCEED` to execute:

```markdown
- OCM-PROCEED
```

#### 4. Mission Scanning

Run the Place de Grève mission scanner:

```bash
npm run scan
```

This autonomously discovers, prioritizes, and marks missions for execution.

## Architecture

### Core Files

| File | Purpose |
|------|---------|
| `ocm-INSTRUCTIONS.md` | User command interface |
| `ocm-MISSION-QUEUE.md` | Mission queue status |
| `ocm-STATUS-REPORT.md` | Agent reports (human-readable) |
| `HEARTBEAT.md` | Autonomous protocol for periodic checks |
| `index.mjs` | Main orchestrator entry point |

### Runtime Directory (`.openclaw/runtime/`)

| File | Purpose |
|------|---------|
| `ocm-audit-trail.log` | All telemetry and system events |
| `ocm-sub-template.md` | Sub-Agent configuration template |
| `ocm-sub-[task_id].md` | Individual Sub-Agent configurations |

### Scripts

| Script | Purpose |
|--------|---------|
| `scripts/scan-place-de-greve.mjs` | Autonomous mission scanner |

## Sub-Agent Model

Sub-Agents operate under strict Parent-Child laws:

- **No auto-inheritance**: Master explicitly whitelists tools
- **Context injection**: Master provides `context_fragment` and `root_lock`
- **Read-only environment**: Cannot modify inherited environment variables
- **Telemetry redirection**: All logs go to `ocm-audit-trail.log`

### Escalation Levels

1. **Level 1 (Direct)**: Master fixes simple issues
2. **Level 2 (Delegation)**: Spawns `ocm-sub-[specialist]`
3. **Level 3 (Escalation)**: System pause + `[CRITICAL_FAILURE]` marker for human intervention

## Naming Convention

All system-generated files use the `ocm-` prefix to distinguish from user project files.

## License

MIT
