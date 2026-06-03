# Current Next Move

direction_id: indie-game-development
primary_next_move: launch_direction_definition
next_entrypoint: launch_direction_definition
run_surface_type: formation_chat
procedure_ref: workflow_v3/runbooks/DIRECTION_DEFINITION_RUNBOOK.md
launch_packet_template_ref: workflow_v3/project_setup/DIRECTION_DEFINITION_LAUNCH_PACKET_TEMPLATE.md

## Preconditions for next move

Before launching Direction Definition, future chat must verify exact repository sources:

- directions_v3/indie-game-development/runtime/state/CURRENT_STATUS.md
- directions_v3/indie-game-development/runtime/state/CURRENT_NEXT_MOVE.md
- directions_v3/indie-game-development/runtime/config/DIRECTION_PROJECT_BINDING.md

CURRENT_STATUS.md must show:

```text
setup_status: setup_only_root_created
semantic_definition_status: pending_definition
````

CURRENT_NEXT_MOVE.md must show:

```text
primary_next_move: launch_direction_definition
```

## Boundary

Do not perform product work from setup-only state.

Do not create Work Graph or Work Contract before admitted Direction Definition and required entity acceptance.

Direction Definition forms candidate Direction Spine, Direction Map, and Active Front. Those outputs remain candidate until explicit Acceptance Decision / storage update path.

END_OF_FILE: directions_v3/indie-game-development/runtime/state/CURRENT_NEXT_MOVE.md
