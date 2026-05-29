---
artifact_control:
  namespace: workflow_v3
  artifact_type: readme
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Clean Workflow Runtime v3

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Purpose

Workflow Runtime v3 exists as a clean candidate surface for long-running solo+AI projects.

Target users:

- One human owner.
- AI assistants used for planning, continuation, research, writing, and review.
- Codex or similar agents used for bounded repository work.
- Research and review agents used for challenge, verification, and synthesis.

The goal is to keep control state small, make continuation reliable from any chat, and prevent planning artifacts from turning into unreviewed runtime authority.

## Core Architecture

- Direction Control: root result, success conditions, global spine, active front, queues, and continuation pointer.
- Active Front: the small part of the project currently being advanced.
- Local Work Maps: detailed maps only for active composite nodes.
- Memory System: scoped control, node, shared, decision, event, and artifact memory.
- Event / Review / Patch System: explicit events, review jobs, patch proposals, and parent integration.
- Parallel Chat Runtime: parent-issued child packets with bounded scope and explicit result reports.
- Execution Boundary: route selection, readiness, execution, evidence, and validation remain distinct.
- Legacy Boundary: current and old data are preserved in place and may be reused later only through explicit import/review.

## What Is Different From The Current Runtime

- Global planning stays coarse instead of trying to model every possible future task.
- Detailed task graphs exist only where work is active and integration is possible.
- Child chats are bounded by parent contracts rather than implicit context.
- Reviews can propose patches, but parent control accepts or rejects them.
- Memory promotion is explicit, so local outputs do not silently become shared truth.
- The runtime is candidate-only and does not mutate existing `directions/**`.

## Continuation Model

Any chat can continue work if it receives:

- Current Direction Control reference.
- Active Front summary.
- Selected node contract.
- Allowed memory references.
- Recent decisions and events.
- Current task.
- Forbidden actions.
- Expected output.

The continuation packet is the restart surface. It keeps the assistant focused on the active front and prevents unbounded rediscovery.

## Preservation Model

- Legacy/current workflow data preserved in place.
- Old data may be imported later only by explicit import/review.
- Existing artifacts are evidence, not v3 authority.
- No current Direction state is created, closed, accepted, or modified by this scaffold.
- No existing workflow namespace is moved, deleted, renamed, or rewritten.

## Current Status

- Status: candidate-only.
- Authority: not active authority.
- Scope: parallel runtime design.
- Review target: branch-only scaffold.
- Product execution: none.

END_OF_FILE: workflow-v3/README.md
