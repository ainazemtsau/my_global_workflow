# Workflow v3 Template Index

status: active_template_index

## Source authority boundary

Exact repository files at repo/path/ref are source authority.

Project Files/Sources, pasted excerpts, uploaded files, candidate docs, prior summaries, chat memory, and generated packs are cache/context unless verified against exact repository state.

## Template-only boundary

These templates guide future accepted packages. They do not create accepted Direction state, adopt any Direction, create runtime state, update Project Instructions UI, refresh Project Files/Sources, or refresh request-only sources.

Do not create `directions_v3/<direction-id>/runtime/**` from these templates unless a later explicit Direction adoption or runtime-state package authorizes it.

Repository commits do not update actual ChatGPT Projects.

## Operational/event-loop templates

- `SIGNAL_RECORD_TEMPLATE.md`
- `HANDLER_RESULT_TEMPLATE.md`
- `ACTION_INBOX_ITEM_TEMPLATE.md`
- `CHECK_JOB_TEMPLATE.md`
- `EVENT_LOOP_CLOSURE_TEMPLATE.md`
- `PROGRESSION_ROUTER_RESULT_TEMPLATE.md`
- `TRANSITION_PACKET_TEMPLATE.md`
- `NEXT_CHAT_PROMPT_TEMPLATE.md`

## Runtime state templates

- `DIRECTION_SPINE_TEMPLATE.md`
- `DIRECTION_MAP_TEMPLATE.md`
- `ACTIVE_FRONT_TEMPLATE.md`
- `CURRENT_STATUS_TEMPLATE.md`
- `CURRENT_NEXT_MOVE_TEMPLATE.md`
- `DIRECTION_PROJECT_BINDING_TEMPLATE.md`
- `DIRECTION_CONSOLE_TEMPLATE.md`

Steering runtime state templates reference formation runbooks where relevant. Formation creates candidate content; templates store candidate/accepted/pending fields only when an authorized package supplies source authority, evidence, and acceptance/update path.

## Front/graph/node templates

- `FRONT_TEMPLATE.md`
- `WORK_GRAPH_TEMPLATE.md`
- `WORK_GRAPH_NODE_TEMPLATE.md`
- `NODE_CLOSURE_SUMMARY_TEMPLATE.md`
- `FRONT_CLOSURE_SUMMARY_TEMPLATE.md`

## Record/evidence/acceptance templates

- `WORK_CONTRACT_TEMPLATE.md`
- `RUN_RECORD_TEMPLATE.md`
- `RESULT_PACKET_TEMPLATE.md`
- `EVIDENCE_RECORD_TEMPLATE.md`
- `ACCEPTANCE_DECISION_TEMPLATE.md`

## Memory/closure/recovery templates

- `MEMORY_CANDIDATE_TEMPLATE.md`
- `MEMORY_ARTIFACT_TEMPLATE.md`
- `PARENT_RECOVERY_BLOCK_TEMPLATE.md`

## Use rule

Templates may be copied into future accepted packages as structure for candidate records, accepted records, or runtime state only when that package supplies the required source authority, evidence, acceptance/update path, allowed paths, and validation.

The template itself is not accepted state and does not authorize state mutation.

Setup-only root may use `pending_definition`, `none_selected`, `setup_only_root_created`, and `launch_direction_definition` placeholder values. Those values do not accept semantic Direction content.

## Related operating docs

- `workflow_v3/adoption/**` contains future clean-start adoption package templates.
- `workflow_v3/formation/**` contains steering entity formation protocols/runbooks.
- `workflow_v3/runbooks/**` contains operating paths for using these templates.
- `workflow_v3/evals/**` contains validation gates for packages that use these templates.
- `workflow_v3/completion/WORKFLOW_V3_COMPLETION_MATRIX.md` maps templates to surfaces and entity coverage.

## Boundary

This index is a template index only.

It does not adopt a Direction, create runtime state, update Project Instructions UI, refresh Project Files/Sources, or refresh request-only sources.

END_OF_FILE: workflow_v3/templates/README.md
