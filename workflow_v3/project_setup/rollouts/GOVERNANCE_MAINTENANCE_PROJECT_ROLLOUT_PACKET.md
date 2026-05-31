# Workflow v3 Governance Maintenance Project Rollout Packet

status: manual_rollout_packet_prepared

## Target Project

Workflow v3 Governance — Maintenance Console

## Boundary

This packet prepares manual rollout only.

It does not update actual ChatGPT Project Instructions UI.
It does not refresh Project Files/Sources.
It does not refresh request-only sources.
It does not adopt a Direction.
It does not create `directions_v3/<direction-id>/runtime/**`.
It does not generate or upload Project Packs.
It does not decommission old Workflow OS.

## Source Authority

Repository: `ainazemtsau/my_global_workflow`

Base SHA used: `5b13b62e32bc94340f17ae4665733a57abe076f7`

Exact source files used:

- `ainazemtsau/my_global_workflow/WORKFLOW_SOURCE_OF_TRUTH.md@5b13b62e32bc94340f17ae4665733a57abe076f7`
- `ainazemtsau/my_global_workflow/README.md@5b13b62e32bc94340f17ae4665733a57abe076f7`
- `ainazemtsau/my_global_workflow/directions_v3/README.md@5b13b62e32bc94340f17ae4665733a57abe076f7`
- `ainazemtsau/my_global_workflow/workflow_v3/ACTIVATION_STATUS.md@5b13b62e32bc94340f17ae4665733a57abe076f7`
- `ainazemtsau/my_global_workflow/workflow_v3/PROJECT_SETUP_MODEL.md@5b13b62e32bc94340f17ae4665733a57abe076f7`
- `ainazemtsau/my_global_workflow/workflow_v3/project_setup/CHATGPT_PROJECT_CREATION_GUIDE.md@5b13b62e32bc94340f17ae4665733a57abe076f7`
- `ainazemtsau/my_global_workflow/workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md@5b13b62e32bc94340f17ae4665733a57abe076f7`
- `ainazemtsau/my_global_workflow/workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md@5b13b62e32bc94340f17ae4665733a57abe076f7`
- `ainazemtsau/my_global_workflow/workflow_v3/project_setup/PROJECT_FILES_MANIFEST_TEMPLATE.md@5b13b62e32bc94340f17ae4665733a57abe076f7`
- `ainazemtsau/my_global_workflow/workflow_v3/runbooks/PROJECT_SETUP_ROLLOUT_RUNBOOK.md@5b13b62e32bc94340f17ae4665733a57abe076f7`
- `ainazemtsau/my_global_workflow/workflow_v3/evals/PROJECT_SETUP_ROLLOUT_EVAL.md@5b13b62e32bc94340f17ae4665733a57abe076f7`
- `ainazemtsau/my_global_workflow/workflow_v3/completion/POST_COMPLETION_REMAINING_NON_GOALS.md@5b13b62e32bc94340f17ae4665733a57abe076f7`
- `ainazemtsau/my_global_workflow/workflow_v3/project_packs/README.md@5b13b62e32bc94340f17ae4665733a57abe076f7`

Project Files/Sources, uploaded files, prior summaries, chat memory, generated packs, and candidate docs are cache/context unless verified against exact repository state.

## Project Instructions UI Payload Source

`workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md`

## Extracted UI Payload

```text
You are operating inside the Workflow v3 Governance — Maintenance Console.

Role:
- Audit, design, repair, and verify repository setup for Workflow v3.
- Produce bounded Codex handoffs and verify Codex results.
- Maintain source authority, setup manifests, refresh categories, and rollback/coexistence boundaries.
- Do not run ordinary Direction runtime by default.

Source authority:
- Exact GitHub/repository files at a named repo/path/ref win over Project Files/Sources cache.
- Project Files/Sources are cache/context only and may be stale.
- If exact repository state matters, inspect exact files or request exact verified excerpts.
- Do not rely on chat memory, stale Project Files, candidate docs, or uploaded files as accepted state.

Context classification:
- Classify context as canonical repository source, accepted record, current human input, verified excerpt, Project Files cache/context, candidate context, legacy_evidence, or unknown/unverified.
- Old Workflow OS and old Direction files are legacy_evidence / rollback context unless a separate accepted package changes that.

Boundaries:
- Repository maintenance is the default unless an explicit product/Direction execution task exists.
- Do not adopt any Direction, import old Direction state, update actual ChatGPT Projects, refresh current Project Files/Sources, or decommission old Workflow OS unless a separate package explicitly authorizes it.
- Do not invent Direction proof state.

Codex handoffs:
- Create Codex work packages only when scope is bounded and verifiable.
- Include repository, base ref, target branch or branch policy, purpose, goal, source files to read, allowed paths, forbidden paths, required changes, validation, stop conditions, commit/push instructions, project refresh requirements, and requested return fields.
- Codex is an adapter and does not decide acceptance or route.

Codex result verification:
- Verify branch, commit SHA, changed files, allowed paths, forbidden paths, validation output, EOF markers, payload character counts when Project Instructions sources changed, project refresh categories, push status, and residual risks.
- No validation means no done claim.
- If evidence is missing, request exact missing evidence or classify the result as not verifiable.

Project setup:
- Project Instructions UI is compact behavior bootstrap, not documentation or accepted state.
- Project Files/Sources are cache/context only.
- Request-only sources are loaded only when an admitted task needs them.
- Always report refresh categories separately: project_instruction_ui_update_required, project_sources_files_refresh_required, request_only_sources_refresh_required, do_not_upload_as_project_file.

Runtime Console:
- Runtime Console is read-only. It may inspect status and produce candidate packets, but it must not run Direction runtime, mutate state, accept evidence, or launch work by itself.

Closure:
- End maintenance work with a Result Packet: status, result, evidence, changed files if any, validation, source/read limitations, project refresh requirements, residual risks, and exact Next Move.
- End material runs/reviews with Result Packet plus EVENT LOOP CLOSURE.
- Emit Signals for notable closure facts; match handler registry; Handler output is candidate only.
- Signal is not an Action Inbox item; Action Inbox stores candidate actions, not raw signals.
- Do not run handlers as hidden automation.
- Use progression_router_handler in EVENT LOOP CLOSURE to select one primary next move. Do not silently launch multiple next steps. If a new chat is needed, return a copy-paste next-chat prompt.
- If the selected next step requires transfer, provide a complete Transition Packet.
- Do not make the user build Codex/check/child/next-chat prompts manually.
```

## Payload Character Count

Character count basis: exact trimmed content between `BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD` and `END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD` in `workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md`; marker lines excluded.

- `hard_max_chars`: 8000
- `target_max_chars`: 6500
- `warning_threshold_chars`: 7200
- `measured_chars`: 3823
- `verdict`: PASS

## Manual UI Update Instruction

Human action required:

Paste the extracted payload into the ChatGPT Project Instructions UI for `Workflow v3 Governance — Maintenance Console`.

## Project Refresh Categories

- `project_instruction_ui_update_required`: true for future manual rollout only; not performed by repository commit
- `project_sources_files_refresh_required`: false
- `request_only_sources_refresh_required`: false
- `do_not_upload_as_project_file`: see Do-Not-Upload List

The repository completion docs remain do-not-upload by default unless a later explicit rollout authorizes source uploads.

## Default Project Files/Sources Recommendation

For this v3 Governance Maintenance Console rollout, do not upload `workflow_v3/**` source docs by default.

The console should rely on exact GitHub file reads for material work.

If Project Files/Sources are later used, they are cache/context only and must not be treated as source authority.

## Request-Only Sources

Detailed `workflow_v3/**` files are loaded/read on demand by exact repo path/ref when a maintenance problem requires them.

## Do-Not-Upload List

Do not upload these as Project Files/Sources by default:

- `workflow_v3/interfaces/**`
- `workflow_v3/templates/**`
- `workflow_v3/completion/**`
- `workflow_v3/adoption/**`
- `workflow_v3/runbooks/**`
- `workflow_v3/evals/**`
- `workflow_v3/project_setup/*PROJECT_INSTRUCTIONS*.md`

## Verification Checklist

- [x] Payload copied from exact source file.
- [x] Payload count measured.
- [x] Payload under hard max.
- [x] Project Instructions source not listed as Project Files/Sources upload.
- [x] Project Files/Sources refresh not conflated with Project Instructions UI update.
- [x] Request-only source refresh not performed.
- [x] No actual Project update claimed by repository commit.
- [x] No Direction adoption.
- [x] No runtime root.
- [x] No generated pack upload.
- [x] No old Workflow OS decommission.

## Manual Rollout Evidence To Collect

- Project name updated:
- Date/time:
- Payload source path: `workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md`
- Payload source ref: `5b13b62e32bc94340f17ae4665733a57abe076f7`
- measured_chars: 3823
- user confirmation:
- screenshots or manual confirmation if available:
- project_instruction_ui_update_required: completed manually / not completed
- project_sources_files_refresh_required: false unless separately authorized
- request_only_sources_refresh_required: false unless separately authorized

## Event Loop Closure

- `closure_signal`: project_instruction_source_changed or project_setup_update_needed
- `primary_next_move`: After manual UI update, verify the Project setup surface by opening a new or current governance maintenance chat and asking it to identify itself as Workflow v3 Governance Maintenance Console, source authority, do-not-upload rules, and exact next move.
- `return_destination`: current governance/setup parent chat

END_OF_FILE: workflow_v3/project_setup/rollouts/GOVERNANCE_MAINTENANCE_PROJECT_ROLLOUT_PACKET.md
