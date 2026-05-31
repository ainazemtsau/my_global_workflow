# Direction Bootstrap Runbook

status: active_repository_completion_framework

## Trigger condition

Use when a future Workflow v3 Direction needs adoption, runtime root planning, or confirmation that no accepted v3 runtime exists.

Trigger signals include `direction_runtime_missing`, `direction_adoption_needed`, `direction_spine_missing`, `direction_map_missing`, `active_front_missing`, or `blocked_lifecycle_transition`.

## Input sources

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow_v3/ACTIVATION_STATUS.md`
- `workflow_v3/STORAGE_LAYOUT.md`
- `workflow_v3/LEGACY_EVIDENCE_POLICY.md`
- `workflow_v3/adoption/**`
- exact Direction-specific sources named by the future package

## Source authority classification

Exact repository files at named ref/path are authority. Old `directions/**` files are `legacy_evidence` only. Project Files/Sources, prior chat, and generated packs are cache/context.

## Required templates

- `workflow_v3/adoption/CLEAN_START_DIRECTION_ADOPTION_PACKAGE_TEMPLATE.md`
- `workflow_v3/adoption/DIRECTION_BOOTSTRAP_DECISION_TEMPLATE.md`
- `workflow_v3/adoption/DIRECTION_RUNTIME_ROOT_MANIFEST_TEMPLATE.md`
- `workflow_v3/adoption/ADOPTION_RESULT_PACKET_TEMPLATE.md`
- `workflow_v3/templates/DIRECTION_SPINE_TEMPLATE.md`
- `workflow_v3/templates/DIRECTION_MAP_TEMPLATE.md`
- `workflow_v3/templates/ACTIVE_FRONT_TEMPLATE.md`

## Operating path

1. Confirm `direction_id`.
2. Confirm `adoption_mode`; default is `clean_start`.
3. State `clean_start_reason`.
4. Classify whether legacy evidence is allowed and list `legacy_evidence_paths`.
5. Require explicit accepted initial Direction Spine, Direction Map, and Active Front.
6. Report Project setup and refresh requirements separately.
7. Record rollback/coexistence notes.
8. Require `acceptance_decision_ref` before any runtime root can be created.
9. Emit lifecycle signals and run `direction_adoption_guard_handler`.
10. End with Event Loop Closure and Progression Router result.

## Expected output

Adoption decision packet, runtime root creation plan or blocked result, Project setup impact classification, validation evidence, and exact Next Move.

## Closure signal

`direction_adoption_needed`, `direction_runtime_missing`, `direction_spine_accepted`, `direction_map_accepted`, `active_front_accepted`, or `blocked_lifecycle_transition`.

## Return destination

Return to the requesting parent/governance chat for acceptance review and Event Loop Closure.

## Acceptance/update requirement

No runtime root or accepted v3 Direction state exists until an explicit adoption package and Acceptance Decision authorize it.

## Failure/stop condition

Stop if Direction identity, adoption mode, accepted initial state, acceptance decision, source authority, legacy boundary, or Project setup authorization is unclear.

END_OF_FILE: workflow_v3/runbooks/DIRECTION_BOOTSTRAP_RUNBOOK.md
