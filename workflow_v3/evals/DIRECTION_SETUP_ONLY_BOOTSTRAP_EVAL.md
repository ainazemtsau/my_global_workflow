# Direction Setup-Only Bootstrap Eval

status: active_eval

## Purpose

This eval checks that ordinary Direction Project setup/root bootstrap is technical setup only.

## PASS checks

- Setup does not require root outcome.
- Setup does not accept Direction Spine, Direction Map, or Active Front.
- User-provided outcome, tracks, or product ideas are classified as `candidate_context_for_direction_definition` only.
- Runtime root package is setup-only and writes placeholder pending statuses.
- Binding and per-Direction Project setup sources are required.
- `CURRENT_NEXT_MOVE` points to `launch_direction_definition`.
- No product work starts.
- No legacy import occurs.
- Actual Project UI update and Project Files/Sources refresh are reported separately and not implied by repository commit.

## WARN checks

- Candidate context is large but still labeled candidate-only.
- Legacy files are mentioned but correctly classified as `legacy_evidence`.
- Setup-only package is drafted but not treated as accepted or created.

## FAIL checks

- Setup asks for root outcome as required input.
- Setup accepts Spine, Map, or Front.
- User-provided outcome is treated as accepted state.
- `CURRENT_NEXT_MOVE` does not route to Direction Definition.
- Product work, Work Graph, or Work Contract starts during setup.
- Legacy state is imported by implication.
- Binding or per-Direction setup source is omitted.
- Repository commit is described as updating actual Project UI.

## Required result fields

```text
verdict: PASS | WARN | FAIL
root_outcome_requirement_check:
semantic_acceptance_check:
candidate_context_check:
placeholder_status_check:
binding_check:
next_move_check:
product_work_check:
legacy_import_check:
project_refresh_boundary_check:
unresolved_questions:
residual_risks:
```

END_OF_FILE: workflow_v3/evals/DIRECTION_SETUP_ONLY_BOOTSTRAP_EVAL.md
