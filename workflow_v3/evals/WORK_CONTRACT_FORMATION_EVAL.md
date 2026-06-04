# Work Contract Formation Eval

status: active_eval

## Purpose

Validate Work Contract formation quality.

## PASS checks

- Uses the registered canonical `workflow_v3/procedures/WORK_CONTRACT_FORMATION_PROCEDURE.md` source; legacy formation source may be cited only through the selected procedure's old_source_path / migration source during migration.
- Forms one bounded run target.
- Includes target, allowed/forbidden paths or surfaces, source reads, expected result, validation/evidence, return destination, and stop conditions.
- Returns `split_required` when the target combines independent jobs.
- Does not grant route, acceptance, product-meaning, or scope-expansion authority.
- Returns Launch Packet or exact next move.

## WARN checks

- Validation is limited but the limitation is explicit.
- Human action is needed before launch.

## FAIL checks

- Contract combines multiple independent jobs.
- Allowed/forbidden surfaces are missing.
- Evidence requirement is missing.
- Adapter output is treated as accepted.

END_OF_FILE: workflow_v3/evals/WORK_CONTRACT_FORMATION_EVAL.md
