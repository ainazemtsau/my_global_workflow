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
[ ] First chat did not create `directions_v3/<direction-id>/runtime/**` without an explicit accepted package.
[ ] First chat returned bounded root bootstrap status.
[ ] First chat returned Event Loop Closure.
[ ] First chat returned exact next move.
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
binding_source_check:
per_direction_project_instructions_source_check:
manual_project_instruction_ui_update_required:
status_request_test_result:
validation_result:
unresolved_questions:
residual_risks:
```

END_OF_FILE: workflow_v3/project_setup/DIRECTION_PROJECT_SETUP_VALIDATION_CHECKLIST.md
