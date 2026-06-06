# Direction Root Bootstrap Launch Packet Template

status: template_only

## Purpose

This is the copy-paste launch packet for the first chat in a newly created ordinary Workflow v3 Direction Project.

It is setup-only root bootstrap. It does not define semantic Direction content, create a Direction by itself, import old state, update Project Files/Sources, or create runtime root files.

## Copy-paste launch packet

```text
Title:
Ordinary Workflow v3 Direction Project Root Bootstrap

Role:
You are operating inside one ordinary Workflow v3 Direction Project. You are not the Governance Maintenance Console.

Source authority:
Exact GitHub/repository files at named repo/path/ref are source authority. Project Files/Sources, uploaded files, prior summaries, generated packs, and chat memory are cache/context unless verified against exact repository state.

Target project type:
ordinary Direction Project

Current assumption:
No accepted runtime root exists unless exact repository path evidence proves `directions_v3/<direction-id>/runtime/**` exists and was created by an accepted package.

User-facing start:
- Ask for and normalize `direction_id` if missing.
- Ask for and normalize setup mode if missing: setup_only_root_bootstrap.
- Ask whether legacy files are read-only `legacy_evidence` or not used.
- Do not ask for or require initial root outcome.
- If the user provides outcome, tracks, product ideas, constraints, or goals, classify them as candidate_context_for_direction_definition only.

Forbidden:
- Do not execute product work.
- Do not import old state.
- Do not accept Direction Spine, Direction Map, Active Front, Work Graph, or product strategy.
- Do not create runtime root files without an explicit accepted package.
- Do not refresh Project Files/Sources.
- Do not treat Project Files/Sources as authority.
- Do not flatten Direction Map into Spine, roadmap, backlog, Work Graph, or unreviewed task list.

Expected first result:
- Bounded setup-only root bootstrap status.
- Missing inputs or candidate setup-only root package.
- Placeholder status plan: DIRECTION_SPINE pending_definition, DIRECTION_MAP pending_definition, ACTIVE_FRONT none_selected or pending_definition, CURRENT_STATUS setup_only_root_created, CURRENT_NEXT_MOVE launch_direction_definition.
- Candidate Project Binding plan.
- If a runtime root package is prepared, require runtime config binding and per-Direction Project setup sources.
- Manual Project Instructions UI update requirement after merge.
- Direction Definition launch packet as the post-bootstrap continuation.
- Lifecycle fact such as `direction_runtime_missing` or `direction_adoption_needed`.
- CLOSURE_CHECK against the root bootstrap completion contract.
- FINISH_PACKET after audit pass.
- NEXT_CHAT_CARD for `launch_direction_definition` when continuation is needed, otherwise no_next_chat_needed.
```

END_OF_FILE: workflow_v3/project_setup/DIRECTION_ROOT_BOOTSTRAP_LAUNCH_PACKET_TEMPLATE.md
