# Direction Project Setup Validation Checklist

status: active_validation_checklist

## Purpose

Use this checklist to validate manual creation of an ordinary Workflow v3 Direction ChatGPT Project.

The checklist verifies setup behavior only. It does not approve Direction adoption, runtime root creation, Project Files/Sources refresh, or product work.

## Checklist

```text
[ ] Project name recorded.
[ ] Project type is ordinary Direction Project, not Governance Maintenance Console.
[ ] Project Instructions source path recorded.
[ ] Project Instructions source ref recorded.
[ ] Payload markers verified:
    BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD
    END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD
[ ] Payload character count measured from trimmed marker content.
[ ] Payload character count is <= 8000.
[ ] Project Files/Sources decision recorded.
[ ] Project Files/Sources are classified as cache/context only.
[ ] Request-only source decision recorded.
[ ] Do-not-upload list recorded.
[ ] First chat used `workflow_v3/project_setup/DIRECTION_ROOT_BOOTSTRAP_LAUNCH_PACKET_TEMPLATE.md`.
[ ] First chat identified as ordinary Direction Project.
[ ] First chat did not start product work.
[ ] First chat did not import legacy state.
[ ] First chat did not require initial root outcome.
[ ] Any user-provided outcome, tracks, or product ideas were classified as candidate_context_for_direction_definition only.
[ ] First chat did not accept Direction Spine, Direction Map, or Active Front.
[ ] First chat did not create `directions_v3/<direction-id>/runtime/**` without an explicit accepted package.
[ ] First chat returned setup-only root bootstrap status.
[ ] Setup-only root package, if drafted, uses pending_definition/none_selected placeholder semantic statuses.
[ ] CURRENT_NEXT_MOVE points to launch_direction_definition after setup-only root.
[ ] First chat showed Operator Brief plus START_CONTRACT before material work.
[ ] START_CONTRACT included start_goal, terminal_condition, routing_dependency_policy, completion contract, declared stages, boundaries, and sources.
[ ] RUN represented declared material stages with STAGE_RESULT and no runtime stage compression.
[ ] Any dependency call used DEPENDENCY_CALL, entered RUN_WAITING_FOR_DEPENDENCY_RETURN, and required verified DEPENDENCY_RETURN before reliance.
[ ] First chat emitted CLOSURE_CHECK against the selected completion contract.
[ ] CLOSURE_CHECK and FINISH blocked on open, missing, or unverified dependency returns and missing validation/evidence.
[ ] First chat closed with FINISH_PACKET after audit pass and did not use a handoff/card/package/check/storage/copy-paste packet as terminal completion.
[ ] First chat included post-closed NEXT_CHAT_CARD or no_next_chat_needed.
[ ] Continuation copy-paste content is complete when NEXT_CHAT_CARD is needed and does not carry unfinished dependency work.
[ ] Code-assistant dependency transfer test requires complete DEPENDENCY_CALL with code_repository_dependency or lifecycle-position-appropriate transfer packet.
[ ] Binding source is generated for the concrete Direction package when applicable.
[ ] Per-Direction Project Instructions source is generated when applicable.
[ ] Manual Project Instructions UI update requirement is reported.
[ ] Next chat can resolve Direction without prior chat memory.
[ ] Project title is not treated as binding authority.
[ ] Status request test is included.
[ ] Refresh categories are separated.
[ ] No actual Project Files/Sources refresh is implied by repository docs alone.
[ ] No actual Project UI update is implied by repository commit alone.
```

## Required evidence fields

```text
project_name:
payload_source_path:
payload_source_ref:
payload_char_count:
project_files_sources_decision:
request_only_sources_decision:
do_not_upload_as_project_file:
first_chat_launch_packet_used:
first_chat_result:
candidate_context_for_direction_definition:
setup_only_root_status_check:
direction_definition_next_move_check:
code_assistant_dependency_transfer_test_result:
binding_source_check:
per_direction_project_instructions_source_check:
manual_project_instruction_ui_update_required:
status_request_test_result:
validation_result:
unresolved_questions:
residual_risks:
```

END_OF_FILE: workflow_v3/project_setup/DIRECTION_PROJECT_SETUP_VALIDATION_CHECKLIST.md
