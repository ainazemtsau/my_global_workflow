# Work, Run, and Acceptance Interface

status: active_interface_layer

## Purpose

This file defines bounded material work in Workflow v3: Work Contract, Run, Evidence, Result Packet, and Acceptance Decision.

## Owner/surface

Owner/surface: material work execution and acceptance boundary.

## Persistence target

Persistence target: `workflow_v3/interfaces/03_WORK_RUN_ACCEPTANCE_INTERFACE.md` for shared rules; future adopted Direction records belong under `directions_v3/<direction-id>/runtime/records/**` after explicit adoption.

## Work Contract input contract

A Work Contract must state:

- bounded target;
- source authority and required source reads;
- in-scope surfaces;
- out-of-scope and forbidden surfaces;
- expected result;
- evidence and validation required;
- allowed producer or adapter;
- return destination;
- stop conditions;
- persistence expectations;
- acceptance review path.

## Run

Run is execution of a Work Contract through a human action, ChatGPT, Codex, research agent, GitHub access, future provider, or other adapter.

The Run must stay inside the Work Contract. Scope expansion requires a repair Next Move, human decision request, or future package split.

## Evidence output contract

Evidence must be verifiable and bounded to the Work Contract.

Evidence may include changed files, diffs, command outputs, test or validation results, exact source reads, screenshots, human confirmation, or limitations explaining why evidence is incomplete.

Human confirmation is evidence, not automatic accepted state.

No validation means no done claim.

## Result Packet output

A Result Packet must state:

- status;
- result;
- source/read limitations;
- evidence and validation;
- changed files or surfaces;
- what was not done;
- assumptions;
- unresolved decisions;
- risks;
- candidate-state notice;
- return destination;
- exact Next Move;
- whether Event Loop Closure is included or needed.

## Acceptance Decision boundary

Acceptance is the explicit decision to accept, reject, or return a result for repair.

No adapter accepts its own result.

Accepted State changes only through the explicit acceptance/update path after evidence is reviewed.

## Rejected, repair, and accepted paths

Rejected results remain candidate history or are discarded according to the applicable records policy.

Repair keeps the same bounded target unless the reviewer explicitly changes scope.

Accepted results may be persisted to accepted state only through the correct state mutation path and storage target.

## Inputs

Inputs are Work Contracts, source authority, Launch Packets, adapter capabilities, human decisions, and existing accepted records when available.

## Outputs

Outputs are Runs, Evidence, Result Packets, repair candidates, rejected outcomes, accepted outcomes, and Acceptance Decisions.

## State mutation rights

Runs, Evidence, and Result Packets do not mutate accepted state.

Acceptance Decisions may authorize accepted-state mutation only when they are explicit, evidenced, and routed to an allowed storage target.

## Allowed producers

Allowed producers are ChatGPT, Codex, human actions, Claude Code/future code assistants, Deep Research/research agents, GitHub access, Check Jobs, and future providers operating from bounded contracts.

## Allowed consumers

Allowed consumers are parent review chats, Acceptance Decisions, Event Loop Closure, Progression Router, Runtime Console summaries, Memory promotion review, and future Direction records.

## Validation/evidence requirement

The result must include evidence tied to the Work Contract and state validation limitations. Repository work must report branch, commit if committed, changed files, allowed paths, forbidden paths unchanged, checks run, and residual risks.

## Forbidden behaviors

- Starting material work from vague memory when accepted state is absent.
- Expanding scope without an explicit decision.
- Claiming done without validation.
- Treating Evidence as accepted state.
- Letting Codex, ChatGPT, or another adapter accept its own result.
- Treating human action as complete without confirmation.
- Persisting accepted state without an Acceptance Decision.

## Failure/recovery path

Use blocked result when source, permission, scope, or validation is missing.

Use same-package repair when validation failed and repair remains in scope.

Use human decision request when acceptance, scope, or judgment is required.

Use future package split when the needed work is real but outside the Work Contract.

## Dependencies

- `workflow_v3/RUNTIME_MODEL.md`
- `workflow_v3/QUALITY_AND_RECOVERY.md`
- `workflow_v3/project_setup/GENERIC_AI_PROVIDER_SETUP.md`
- `workflow_v3/templates/TRANSITION_PACKET_TEMPLATE.md`

END_OF_FILE: workflow_v3/interfaces/03_WORK_RUN_ACCEPTANCE_INTERFACE.md
