# Project Setup Rollout Runbook

status: active_repository_completion_framework

## Trigger condition

Use when a future package explicitly authorizes Project setup rollout, Project Instructions UI update preparation, Project Files/Sources manifest refresh, request-only source refresh planning, or generated pack preparation.

Trigger signals include `project_setup_update_needed`, `stale_context_detected`, `project_instruction_source_changed`, or `blocked_lifecycle_transition`.

## Input sources

- `workflow_v3/PROJECT_SETUP_MODEL.md`
- `workflow_v3/project_setup/CHATGPT_PROJECT_CREATION_GUIDE.md`
- Project Instructions source file with UI payload markers
- `workflow_v3/project_setup/PROJECT_FILES_MANIFEST_TEMPLATE.md`
- `workflow_v3/project_packs/README.md`
- exact future package authorization

## Source authority classification

Repository setup sources are authority for preparing rollout. Actual ChatGPT Project UI and Project Files/Sources are external surfaces and are not updated by repository commit alone.

## Required templates

- `workflow_v3/project_setup/PROJECT_FILES_MANIFEST_TEMPLATE.md`
- `workflow_v3/templates/RESULT_PACKET_TEMPLATE.md`
- `workflow_v3/templates/EVIDENCE_RECORD_TEMPLATE.md`
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`

## Operating path

1. Separate repository commit from actual Project Instructions UI update.
2. Separate Project Files/Sources refresh from repository commit.
3. Separate request-only source refresh from default Project Files/Sources.
4. List do-not-upload sources.
5. Locate `BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD` and `END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD` markers when instruction sources change.
6. Measure trimmed UI payload character count.
7. Fail validation if payload is above 8,000 characters.
8. Warn if payload is above 7,200 characters.
9. Target under 6,500 characters.
10. Do not list Project Instruction sources as Project Files/Sources uploads.
11. Report refresh categories separately.
12. End with Event Loop Closure and exact Next Move.

## Expected output

Rollout result packet with repository commit status, UI payload counts, Project Files/Sources manifest impact, request-only source impact, do-not-upload list, and exact Next Move.

## Closure signal

`project_setup_update_needed`, `project_instruction_source_changed`, `stale_context_detected`, or `blocked_lifecycle_transition`.

## Return destination

Return to the governance/setup parent chat for human rollout decision or verification.

## Acceptance/update requirement

Repository setup changes do not update actual ChatGPT Projects. Actual UI update or refresh requires a later explicit rollout action and evidence.

## Failure/stop condition

Stop if Project UI update is implied by commit, payload count fails, Project Files/Sources are treated as authority, request-only sources are uploaded by default, or do-not-upload sources are omitted.

END_OF_FILE: workflow_v3/runbooks/PROJECT_SETUP_ROLLOUT_RUNBOOK.md
