---
name: nexus-protocol
description: |-
  [status] (Report protocol state and registered participants.)
  [declare] (Add or update a participant, event type, or routing rule in protocol.json.)
  [route] (Simulate routing an event through the declared protocol.)
argument-hint: "status, declare, route"
user-invocable: true
---

# Nexus-Protocol — Inter-App Communication Bus

Inter-application communication layer for the core-ferule ecosystem. Declares participants, event types, and capability-based routing via `protocol.json`.

## Purpose

`nexus-protocol` is the single source of truth for cross-app communication. Any app can emit events, query other apps, or request interventions — routing is handled by declared capabilities, not ad-hoc logic.

## Commands

| Command | Action |
|---------|--------|
| `[status]` | Report registered participants, event types, and routing state |
| `[declare]` | Add or update a participant, event type, or routing rule |
| `[route]` | Simulate routing an event through the declared protocol |

## Key File

| File | Purpose |
|------|---------|
| `protocol.json` | Inter-app protocol declaration — participants, event types, routing rules |
| `bmad/CLAW.md` | BMAD migration context (legacy) |

## Current Status

🔄 V1 scaffold — protocol.json defined, phase 1 not started.
