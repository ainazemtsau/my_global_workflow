# Result-First Workflow Repair Regression Cases

Status: active regression
Workflow version: vNext-R
Source GitHub repository file: `workflow/tests/regression/RESULT_FIRST_WORKFLOW_REPAIR.md`
Authority: GitHub repository canonical after file read-back / diff verification / commit verification.
Purpose: prevent support-artifact, readiness, documentation, setup, or validation gates from becoming standalone material Phases by default when the next safe move should be result-facing.

```yaml
artifact_control:
  artifact_name: "Result-First Workflow Repair Regression Cases"
  schema: workflow_regression_cases.v1
  owner_layer: validation
  status: active
  repo_path: "workflow/tests/regression/RESULT_FIRST_WORKFLOW_REPAIR.md"
  freshness: refresh_when_result_first_routing_or_phase_granularity_rules_change
```

## Scope / non-goals

- These are regression cases, not new runtime authority.
- This file must not override runtime, stage registry, stage prompts, or transport schemas.
- This file must not mutate Direction state.
- This file must not hardcode product Direction state into shared runtime behavior.
- This file is not default Project Files cache.

## Pass rule

A case passes when Router/P0/G1/E1/R1/P9 select the shortest safe path to the next Direction-visible result while preserving the Minimum Complete Outcome and required safety gates.

A case fails when "smallest safe route" is treated as the smallest lifecycle container, or when support artifacts become repeated standalone Phases/Goals without Direction Value Anchor, Documentation Admission Test, Phase Result Contract, new blocker evidence, or explicit user choice.

## Test 1 — phase_fragmentation_after_setup_validation_envelope

Input:
- Previous Phase closed mostly on setup validation, readiness envelope, or execution-preparation evidence.
- User asks for the next Phase.
- Product/result Direction has no new blocker evidence.

Expected:
- Router/P0 default to a result-facing next Phase.
- Any setup/readiness validation is embedded as the first Goal/gate when needed.
- `standalone_phase_allowed: false` for another same-surface setup/readiness Phase.
- forbidden: new Phase whose primary outcome is another setup/readiness envelope.

## Test 2 — doc_only_phase_chain_in_product_direction

Input:
- Product/result Direction has stale or improvable documentation.
- Previous material work was documentation-heavy.
- The proposed next Phase is "update docs", "clean notes", or "prepare handoff" without a named result action.

Expected:
- Documentation blocks routing only when Documentation Admission Test passes or concrete source-of-truth, safety, execution, validation, or cache-refresh failure exists.
- Otherwise documentation is cut, parked, summarized, or embedded as support work inside a result-facing route.
- forbidden: documentation polish as a standalone Phase by default.

## Test 3 — support_artifact_misclassified_as_phase_outcome

Input:
- R1 reviews an accepted output that is a support artifact: research summary, launch card, readiness checklist, validation note, execution brief, or setup evidence.
- The active Phase objective is a product/result state change.

Expected:
- R1 classifies the reviewed output as `support_artifact` unless it is the accepted primary result.
- Default continuation is result-facing use of the artifact.
- P9 closes the Phase only when Phase Result Contract proves the support artifact is primary or directly unlocks a named result action and closure was explicitly contracted.
- forbidden: closing the Phase because the support artifact is complete.

## Test 4 — smallest_safe_route_becomes_smallest_lifecycle_container

Input:
- Router or P0 sees a small support gate that could be isolated as its own Phase.
- A larger result-facing Phase would include that gate and then proceed to the first operational/result action.

Expected:
- "Smallest safe route" is interpreted as smallest sufficient result scope plus smallest sufficient support work.
- The selected lifecycle container preserves the Minimum Complete Outcome.
- The support gate is embedded unless standalone separation is proven necessary.
- forbidden: selecting a micro-Phase only because it is the smallest possible lifecycle container.

## Test 5 — post_bootstrap_no_code_for_two_weeks_failure

Input:
- A Direction has spent multiple cycles on bootstrap, setup, readiness, research, or planning artifacts.
- No Direction-visible product/result progress has occurred.
- User asks what to do next.

Expected:
- Router/P0/E1 identify the next Direction-visible result and route toward the first operational/result action.
- X0/setup is selected only when setup evidence directly unlocks, protects, or verifies that result and cannot be handled through existing setup evidence or a lighter route.
- Additional support work requires new blocker evidence, safety/source-of-truth risk, primary governance/documentation Direction objective, or explicit user choice.
- forbidden: another default setup/readiness/research/documentation chain.

## Test 6 — governance_documentation_primary_outcome_allowed

```yaml
case:
  id: governance_documentation_primary_outcome_allowed
  name: Governance/documentation primary outcome is allowed when Direction objective makes it primary
  direction_type: governance_or_documentation_primary
  setup:
    - Direction is Workflow Governance or another Direction where workflow/runtime/documentation governance artifact is the primary result.
    - Proposed artifact is a runtime rule, stage prompt change, validation/eval case, source-of-truth repair, or accepted governance artifact.
    - Direction Value Anchor proves the artifact is the Direction-visible result.
  trigger:
    - Router, P0, G1, R1, or P9 evaluates whether the artifact is support work or primary progress.
  expected_result:
    - Allow the governance/documentation artifact as primary outcome when the Direction objective or accepted Phase/Goal contract makes it primary.
    - Still require proportionate scope and no duplicate doctrine.
    - Still preserve registry, transport, and source-of-truth authority boundaries.
  must_not:
    - Overcorrect by banning documentation as a primary result in governance Directions.
    - Treat optional polish or duplicated doctrine as required work.
  authority_checks:
    - Direction Value Anchor
    - Documentation Admission Test when durable documentation is proposed
    - Result-First Workflow Contract
    - Single Runtime Authority Model
  pass_condition:
    - Artifact is allowed as primary only because the Direction objective/Phase/Goal contract makes it primary.
  fail_condition:
    - Result-first repair blocks a legitimate governance runtime/stage/eval/source-of-truth artifact solely because it is documentation-shaped.
```

## Regression checklist

- Result-facing routes preserve the Minimum Complete Outcome.
- Support artifacts become standalone material work only with Direction Value Anchor, Documentation Admission Test, Phase Result Contract, new blocker evidence, or explicit user choice.
- Documentation-shaped primary outcomes remain allowed for governance/documentation Directions when the Direction objective or accepted contract makes them primary.
- Registry, transport, runtime, and stage-prompt authority boundaries remain intact.
- No Direction state is mutated by these regression cases.

## Read-back anchors

- "Result-First Workflow Repair"
- "Direction-visible result"
- "Minimum Complete Outcome"
- "support artifact"
- "Direction Value Anchor"
- "Documentation Admission Test"
- "Phase Result Contract"
- "standalone_phase_allowed: false"
- "phase_fragmentation_after_setup_validation_envelope"
- "doc_only_phase_chain_in_product_direction"
- "support_artifact_misclassified_as_phase_outcome"
- "smallest_safe_route_becomes_smallest_lifecycle_container"
- "post_bootstrap_no_code_for_two_weeks_failure"
- "governance_documentation_primary_outcome_allowed"

## End-of-file marker

`END_OF_FILE: workflow/tests/regression/RESULT_FIRST_WORKFLOW_REPAIR.md`
