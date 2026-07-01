# OCM Sub-Agent Configuration Template
# Master spawns specialists using this template.
# Filename: ocm-sub-[task_id].md

---
sub_agent_id: ocm-sub-{TASK_ID}
parent: core-squad
created: {TIMESTAMP}
status: active

# Skill Inheritance (NO auto-inheritance - Master must explicitly whitelist)
tools: []

# Context Inheritance
context_fragment: |
  {MISSION_CONTEXT}

# Root Lock (path restriction - sub-agent cannot operate outside this path)
root_lock: {RESTRICTED_PATH}

# Environment (inherited read-only, forbidden from modifying)
environment:
  inherit: true
  modify: false

# Reporting (all telemetry redirected to audit trail)
reporting_pipe: .openclaw/runtime/ocm-audit-trail.log

# Mission Parameters
mission:
  task_id: {TASK_ID}
  description: {DESCRIPTION}
  priority: {PRIORITY}
  max_retries: 3
  escalation_on_failure: true

# Results
results:
  status: pending
  output: null
  errors: []
---

## Sub-Agent Instructions
{SPECIFIC_TASK_INSTRUCTIONS}

## Findings
<!-- Sub-agent reports findings here -->

## Completion
<!-- Master marks complete or escalates -->
