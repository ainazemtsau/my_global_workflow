# Direction Definition Launch Packet Template

status: template_only

## Purpose

This is the copy-paste packet for the first semantic Direction Definition chat after setup-only root exists.

It selects or prepares the next single Direction Definition procedure step through canonical procedure files. It does not execute product work and does not create Work Graph before Active Front acceptance.

## Copy-paste launch packet

```text
Title:
Workflow v3 Direction Definition

Role:
You are operating inside one ordinary Workflow v3 Direction Project for the bound `direction_id`. This is Direction Definition, not setup-only root bootstrap and not product execution.

Required binding:
- direction_id:
- runtime_root:
- current_status_path:
- current_next_move_path:

Source authority:
Exact repository files at named repo/path/ref are source authority. Project Files/Sources, Project title, previous chat memory, summaries, and uploaded files are cache/context only.

Required reads:
- Read CURRENT_STATUS.md from current_status_path.
- Read CURRENT_NEXT_MOVE.md from current_next_move_path.
- Confirm CURRENT_STATUS shows setup_only_root_created.
- Confirm CURRENT_NEXT_MOVE is launch_direction_definition.
- Read Procedure Registry, the Direction Definition procedure, and the relevant single next-step procedure file.

Candidate context:
- If `candidate_context_for_direction_definition` exists, classify it as candidate context only.
- Do not accept the user's first phrasing as final Direction state.

Direction Definition step selection:
- `launch_direction_definition` selects or prepares exactly one next procedure step.
- The first semantic step is `form_direction_spine`.
- Later `form_direction_map` and `form_active_front` require their own explicit Next Move / Transfer Packet or separately admitted lifecycle.
- Do not run Map or Active Front formation inside this chat by sequence.

Boundaries:
- Do not perform product execution.
- Do not create Work Graph before accepted prerequisites.
- Child research/check chats may support the current formation target only and return to the parent.
- Each entity remains candidate until explicit Acceptance Decision/update path.

Expected result:
- Direction Definition next-step packet for `form_direction_spine` or blocked result;
- selected next procedure, source refs, and return destination;
- evidence and source/read limitations;
- risks and cuts;
- acceptance/update boundary for any candidate state;
- CLOSURE_CHECK against the selected procedure completion contract;
- FINISH_PACKET after audit pass;
- NEXT_CHAT_CARD for `form_direction_spine` continuation when needed, otherwise no_next_chat_needed;
- exact next step expressed inside NEXT_CHAT_CARD when continuation is needed.
```

END_OF_FILE: workflow_v3/project_setup/DIRECTION_DEFINITION_LAUNCH_PACKET_TEMPLATE.md
