# core-cognition — Blueprint

> **Date:** 2026-04-12
> **Origin:** Rationalized from `SCRATCHPAD.md` (metacognition principles + routing architecture)
> **Author:** Qwen Code

## Overview

`core-cognition` is the **listening and routing layer** of the OpenClaw core-ferule ecosystem. It receives raw, unstructured input, interprets intent, classifies it via `machinery`, and routes resolved missions to Place de Grève. It does not execute — it understands and delegates.

## Architecture

### 1. Intent Resolution

| Input | Process | Output |
|-------|---------|--------|
| Raw user message | Parse intent, identify domain | `context:domain` resolved or ambiguity flagged |
| Mission with resolved `context:domain` | Direct submission to Place de Grève | No core-cognition hop needed |
| Ambiguous input | Request confirmation before routing | Human-confirmed intent |

### 2. Routing Pipeline

```
User input → core-cognition
    ↓
Intent interpretation (what is being asked?)
    ↓
Domain resolution (which app handles this?)
    ↓
machinery/classifier.mjs → classification result
    ↓
Place de Grève submission (with context:domain)
```

### 3. Hard Constraints

- **Never** submit to Place de Grève without `context:domain` resolved
- **Never** execute the mission — only route
- **Always** request confirmation on ambiguity

## Metacognition Layer

### Principle

> "logs are cognition" — If core-ferule observes its own logs, that is metacognition.

core-cognition's secondary role is to enable **system self-awareness**: the core-ferule ecosystem observing its own activity through logs, audit trails, and status reports. This is the AI equivalent of human metacognition — cognition about cognition.

### Human Metacognition Model (Applied to System)

| Human Component | System Equivalent |
|-----------------|-------------------|
| **Declarative knowledge** (self-awareness) | system state awareness via `ocm-audit-trail.log`, `ocm-STATUS-REPORT.md` |
| **Procedural regulation** (planning, monitoring, evaluating) | mission planning, health monitoring via `check-structure.mjs`, post-action evaluation |
| **Metacognitive experiences** (feeling of knowing, fluency) | confidence scores on classification, validation pass/fail signals |
| **Self-questioning** | ambiguity detection → human confirmation request |
| **Feedback loop** | discrepancy between predicted and actual results → system adjustment |

### Why It Matters

Metacognition is a stronger predictor of success than raw processing power. A system that observes its own activity, detects anomalies, and self-corrects is more resilient than one that merely executes faster.

## Key Files

| File | Role |
|------|------|
| `USER-NOTES.md` | Routing decisions, domain constraints, metacognition principle |
| `machinery/development/v1-machinery/classifier.mjs` | Classification engine — read before any routing |
| `place-de-greve/` | Mission submission target |
| `core-squad/ocm-*.md` | Communication protocol with orchestrator |

## Current State

| Component | Status |
|-----------|--------|
| Intent resolution | ✅ Defined in USER-NOTES.md |
| Routing pipeline | ✅ Conceptual — implementation pending |
| Classification dependency | `machinery/classifier.mjs` (V1 machinery) |
| Metacognition layer | ⏳ Principle defined — implementation pending |
| V1 scaffold | ✅ Exists — missing phase files, reports |
