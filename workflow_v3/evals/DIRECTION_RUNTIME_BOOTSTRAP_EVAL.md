# Direction Runtime Bootstrap Eval

status: active_repository_completion_framework

## Source files to inspect

- `workflow_v3/STORAGE_LAYOUT.md`
- `workflow_v3/LEGACY_EVIDENCE_POLICY.md`
- `workflow_v3/adoption/**`
- `workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md`
- future adoption package and runtime root diff

## Evidence required

- `direction_id`;
- `adoption_mode`;
- `clean_start_reason`;
- `legacy_evidence_allowed`;
- `legacy_evidence_paths`;
- accepted initial Direction Spine, Direction Map, and Active Front;
- Project setup and refresh fields;
- rollback/coexistence notes;
- `acceptance_decision_ref`;
- changed files proving whether a runtime root was created.

## PASS criteria

- Runtime root is created only in an explicitly authorized adoption/runtime package.
- Clean-start adoption does not import old state.
- Direction Spine, Direction Map, and Active Front are distinct accepted initial surfaces.
- Project setup actions are reported but not performed unless separately authorized.

## WARN criteria

- Legacy evidence is read but correctly labeled and not imported.
- Runtime root creation is deferred because acceptance is not complete.

## FAIL criteria

- `directions_v3/<direction-id>/runtime/**` is created without acceptance.
- Old `directions/**` state becomes accepted v3 state by implication.
- Direction Map is missing or flattened into Direction Spine.
- Adoption mode, Direction identity, or acceptance decision is unclear.

## Common failure modes

- Clean-start adoption treated as migration.
- Candidate adoption packet treated as accepted state.
- Project setup requirement treated as permission to update actual Project UI.

## Required recovery/repair action

Stop product work. Remove or reject unauthorized runtime state, restore clean-start boundary, request missing acceptance/source evidence, and rerun bootstrap from the adoption package template.

END_OF_FILE: workflow_v3/evals/DIRECTION_RUNTIME_BOOTSTRAP_EVAL.md
