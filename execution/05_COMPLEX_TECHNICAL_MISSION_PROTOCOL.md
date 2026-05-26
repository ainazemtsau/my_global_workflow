---
artifact_control:
  namespace: workflow
  artifact_type: complex_technical_mission_protocol
  status: gate_2_initial
  owner: workflow_os
---

# Complex Technical Mission Protocol

## Purpose

Complex Technical Mission protocol governs huge or high-risk technical obligations.

Examples include simulation systems, architecture-heavy features, multi-module systems, migrations, performance-sensitive systems, unclear validation systems, and large repairs.

A gas simulation may be an example of this class, but the protocol is stack-agnostic.

## Direct Implementation Denial

Direct implementation is denied for mission-scale obligations.

The first execution move must frame, discover, or plan. It must not mutate broad product surfaces before the mission protocol admits slices.

## Required Flow

Complex Technical Mission flow:

```text
Mission Frame
-> Technical Discovery
-> Architecture Options
-> Validation Harness
-> Spike
-> Architecture Decision
-> Slice Plan
-> Slice Execution
-> Integration Validation
-> Technical Memory Update
```

## Slice Rule

Each slice must be its own execution Obligation.

Each slice must have a launch card, execution receipt, validation receipt, and commit recommendation.

Integration validation must prove that accepted slices work together before business-facing projection claims broader completion.

END_OF_FILE: execution/05_COMPLEX_TECHNICAL_MISSION_PROTOCOL.md
