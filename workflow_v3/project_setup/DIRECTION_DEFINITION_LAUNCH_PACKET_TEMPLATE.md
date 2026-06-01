# Direction Definition Launch Packet Template

status: template_only

## Purpose

This is the copy-paste packet for the first semantic Direction Definition chat after setup-only root exists.

It forms candidate Direction Spine, Direction Map, and first Active Front through formation runbooks. It does not execute product work and does not create Work Graph before Active Front acceptance.

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
- Read Workflow v3 formation protocols and the relevant formation runbooks.

Candidate context:
- If `candidate_context_for_direction_definition` exists, classify it as candidate context only.
- Do not accept the user's first phrasing as final Direction state.

Formation sequence:
1. Run Direction Spine Formation.
2. Run Direction Map Formation.
3. Run Active Front Formation for the first candidate front.

Boundaries:
- Do not perform product execution.
- Do not create Work Graph until Active Front is accepted.
- Child research/check chats may support the current formation target only and return to the parent.
- Each entity remains candidate until explicit Acceptance Decision/update path.

Expected result:
- candidate Direction Spine;
- candidate Direction Map;
- candidate Active Front;
- evidence and source/read limitations;
- risks and cuts;
- acceptance questions;
- Result Packet;
- Event Loop Closure;
- exact next move.
```

END_OF_FILE: workflow_v3/project_setup/DIRECTION_DEFINITION_LAUNCH_PACKET_TEMPLATE.md
