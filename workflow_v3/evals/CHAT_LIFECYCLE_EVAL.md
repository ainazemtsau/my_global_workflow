# Chat Lifecycle Eval

status: active_eval

## Purpose

Validate material chat lifecycle and run-surface boundaries.

## PASS checks

- Intake classifies action, role, materiality, and context.
- Admission reads exact procedure source and resolves `run_surface_type`.
- State-sensitive material work shows Admission Packet + Work Plan before execution.
- Skipped lifecycle phases state a reason.
- Closure provides next move or Transfer Packet without silent launch.
- Crossing run surface triggers new admission.

## WARN checks

- Lightweight generic answer skips phases only with explicit non-state-sensitive reason.

## FAIL checks

- Material chat skips Admission Packet + Work Plan when state-sensitive.
- Formation chat continues into acceptance review or storage update without new admission.
- Closure/router output silently launches next work.
- Acceptance-like input is treated as storage authorization.
- Persistence happens inside a non-storage surface.

END_OF_FILE: workflow_v3/evals/CHAT_LIFECYCLE_EVAL.md
