---
artifact_control:
  namespace: proof_workflow
  artifact_type: execution_obligations
  status: gate_2_initial
  owner: proof_carrying_workflow_os
---

# Execution Obligations

## Obligation Types

Execution obligation types:

- `project_setup`
- `target_binding`
- `technical_discovery`
- `execution_planning`
- `code_mutation`
- `validation`
- `repair`
- `complex_technical_mission`
- `human_guided_action`
- `technical_memory_update`

These are obligation types, not semantic primitives.

## Execution Admission Checklist

An execution Operator invocation may begin only when:

- an open execution Obligation exists
- the target project/repository/worktree is bound
- setup status is known through setup or setup_gap Receipt
- technical context is available, or discovery is required first
- an acceptance predicate exists
- a validation plan exists
- allowed and forbidden surfaces are defined
- proof policy is defined
- required human gate is satisfied or represented as blocking
- selected Operator exists and is eligible
- launch artifact is ready

No execution-ready receipt -> no CodexRun.

Direct CodexRun is denied if any readiness item is missing.

## Missing Readiness

Missing readiness must produce one of:

- Context Request Card
- Human Action Card
- Project Setup Receipt with `setup_gap`
- Technical Discovery Receipt
- residual execution Obligation

## Complex Work Routing

Complex or mission-scale work must route to the Complex Technical Mission Protocol before implementation.

Direct implementation is denied when the work spans architecture-heavy features, multi-module systems, migrations, performance-sensitive systems, simulation systems, or unclear validation systems.

END_OF_FILE: proof_workflow/execution/02_EXECUTION_OBLIGATIONS.md
