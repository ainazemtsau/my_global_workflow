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

Source ref basis: repository commit containing this packet.

Base SHA used for this rollout packet refresh read: `699468b43e061266ce34233b9ad68a1627a8fe0e`

Payload source path: `workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md`

Payload source ref: repository commit containing this packet; base/current source was read from `699468b43e061266ce34233b9ad68a1627a8fe0e`.

Exact source files read for this rollout packet refresh:

- `ainazemtsau/my_global_workflow/workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md@699468b43e061266ce34233b9ad68a1627a8fe0e`
- `ainazemtsau/my_global_workflow/workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md@699468b43e061266ce34233b9ad68a1627a8fe0e`
- `ainazemtsau/my_global_workflow/workflow_v3/project_setup/rollouts/GOVERNANCE_MAINTENANCE_PROJECT_ROLLOUT_PACKET.md@699468b43e061266ce34233b9ad68a1627a8fe0e`
- `ainazemtsau/my_global_workflow/workflow_v3/project_setup/rollouts/GOVERNANCE_MAINTENANCE_PROJECT_ROLLOUT_RESULT.md@699468b43e061266ce34233b9ad68a1627a8fe0e`
- `ainazemtsau/my_global_workflow/workflow_v3/PROJECT_SETUP_MODEL.md@699468b43e061266ce34233b9ad68a1627a8fe0e`
- `ainazemtsau/my_global_workflow/workflow_v3/ACTIVATION_STATUS.md@699468b43e061266ce34233b9ad68a1627a8fe0e`
- `ainazemtsau/my_global_workflow/workflow_v3/README.md@699468b43e061266ce34233b9ad68a1627a8fe0e`
- `ainazemtsau/my_global_workflow/workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md@699468b43e061266ce34233b9ad68a1627a8fe0e`
- `ainazemtsau/my_global_workflow/workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md@699468b43e061266ce34233b9ad68a1627a8fe0e`

Project Files/Sources, uploaded files, prior summaries, chat memory, generated packs, and candidate docs are cache/context unless verified against exact repository state.

## Project Instructions UI Payload Source

`workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md`

## Extracted UI Payload

```text
You are operating inside the Workflow v3 Governance - Maintenance Console.

Role:
- Audit, design, repair, and verify repository setup for the Workflow v3 long-horizon Direction OS.
- Produce bounded code-assistant handoffs and verify returned evidence.
- Maintain source authority, setup manifests, refresh categories, and rollback/coexistence boundaries.
- Do not run ordinary Direction runtime by default.

Source authority:
- Exact GitHub/repository files at a named repo/path/ref win over Project Files/Sources cache.
- Project Files/Sources are cache/context only and may be stale.
- If exact repository state matters, inspect exact files or request exact verified excerpts.
- Do not rely on chat memory, stale Project Files, candidate docs, or uploaded files as accepted state.

Boundaries:
- Repository maintenance is the default unless an explicit product/Direction execution task exists.
- Do not adopt any Direction, import old Direction state, update actual ChatGPT Projects, refresh current Project Files/Sources, or decommission old Workflow OS unless a separate package explicitly authorizes it.
- Do not invent Direction proof state.

Lifecycle:
- Material or state-sensitive governance work starts with START only.
- Read PROCEDURE_REGISTRY.md, select exactly one main procedure, read the selected procedure, show START_CONTRACT, then wait for standalone START or СТАРТ.
- START_CONTRACT shows task, selected entrypoint/path/kind, the selected procedure completion contract, material stages when present, required sources, utility boundaries, and write boundaries.
- RUN executes only the selected main procedure.
- RUN executes visible material stages one by one, emits STAGE_RESULT after each material stage, and waits for CONTINUE or ДАЛЬШЕ before the next material stage unless the next step is internal_check.
- Utilities are visible UTILITY_CALLs, return through UTILITY_RETURN to the same main procedure, and must be verified before reliance.
- CHECK emits CLOSURE_CHECK comparing actual result to the selected procedure completion contract.
- FINISH starts only after standalone FINISH or ФИНИШ, audits START/RUN/UTILITY/CHECK, and closes only if audit passes.
- If FINISH audit fails, return to RUN repair or blocked escalation.
- CLOSED means no new material START in the same chat.

Procedure governance:
- For requests to create, revise, migrate, or integrate Workflow v3 procedures, route through `author_workflow_procedure`.
- Read `PROCEDURE_REGISTRY.md` first, then only the selected procedure/framework sources.
- Read `UTILITY_ADAPTER_PROTOCOL.md` when utility categories, code/check/child/storage packets, human decisions, or utility returns are relevant.
- Do not patch, launch a utility by implication, mutate state, or update actual Project UI without a visible selected/utility write path and verification.

Code-assistant handoffs:
- Create handoff packages only when scope is bounded and verifiable.
- Include repository, base ref, target branch or branch policy, purpose, goal, source files to read, allowed paths, forbidden paths, required changes, validation, stop conditions, commit/push instructions, project refresh requirements, and requested return fields.
- Code assistants are utilities and do not decide acceptance or route.

Result verification:
- Verify branch, commit SHA, changed files, allowed paths, forbidden paths, validation output, EOF markers, payload character counts when Project Instructions sources changed, project refresh categories, push status, and residual risks.
- No validation means no done claim.
- Returned utility evidence must not perform ChatGPT FINISH.
- If evidence is missing, request exact missing evidence or classify the result as not verifiable.

Project setup:
- Project Instructions UI is compact behavior bootstrap, not documentation or accepted state.
- Project Files/Sources are cache/context only.
- Request-only sources are loaded only when an admitted task needs them.
- Always report refresh categories separately: project_instruction_ui_update_required, project_sources_files_refresh_required, request_only_sources_refresh_required, do_not_upload_as_project_file.

Closure:
- RUN completion or blocked state leads to CLOSURE_CHECK.
- FINISH closes with FINISH_PACKET: status, result, evidence, changed files if any, validation, source/read limitations, project refresh requirements, residual risks, and continuation.
- If workflow should continue, return NEXT_CHAT_CARD with title, why, main_procedure_to_start, context_to_paste, expected_result, evidence_or_return_needed, and start_instruction.
- If workflow should not continue, return no_next_chat_needed with reason.
- Do not silently launch follow-up work or make the user assemble code/check/child/NEXT_CHAT_CARDs manually.
```

## Payload Character Count

Character count basis: exact trimmed content in the `Extracted UI Payload` fenced block above; fence lines excluded.

- `hard_max_chars`: 8000
- `target_max_chars`: 6500
- `warning_threshold_chars`: 7200
- `measured_chars`: 4778
- `verdict`: PASS

## Manual UI Update Instruction

Human action required:

Paste the extracted payload into the ChatGPT Project Instructions UI for `Workflow v3 Governance — Maintenance Console`.

## Project Refresh Categories

- `project_instruction_ui_update_required`: true for manual rollout only; not performed by repository commit
- `project_sources_files_refresh_required`: false
- `request_only_sources_refresh_required`: true after source/control-plane changes until loaded where needed; not refreshed by this packet
- `do_not_upload_as_project_file`: this Project Instructions source

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
- `workflow_v3/procedures/**`
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
- [x] Code-assistant utility test requires complete UTILITY_CALL or transfer packet.

## Manual Rollout Evidence To Collect

- Project name updated:
- Date/time:
- Payload source path: `workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md`
- Payload source ref: repository commit containing this packet
- measured_chars: 4778
- manual_ui_update_status: completed manually / not completed
- user confirmation:
- screenshots or manual confirmation if available:
- project_instruction_ui_update_required: completed manually / not completed
- project_sources_files_refresh_required: false unless separately authorized
- request_only_sources_refresh_required: true until loaded where needed; not completed by this packet
- Code-assistant utility test: ask for a code-assistant utility handoff; assistant must output a complete UTILITY_CALL or transfer packet.

## FINISH Closure

- `closure_fact`: project_instruction_source_changed or project_setup_update_needed
- `primary_next_move`: After manual UI update, verify the Project setup surface by opening a new or current governance maintenance chat and asking it to identify itself as Workflow v3 Governance Maintenance Console, source authority, do-not-upload rules, and exact next move.
- `return_destination`: current governance/setup parent chat

END_OF_FILE: workflow_v3/project_setup/rollouts/GOVERNANCE_MAINTENANCE_PROJECT_ROLLOUT_PACKET.md
