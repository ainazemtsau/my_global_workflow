# Direction Console

direction_id: indie-game-development
console_status: setup_only_placeholder
setup_mode: setup_only_root_bootstrap
setup_status: setup_only_root_created
semantic_definition_status: pending_definition
legacy_policy: read_only_legacy_evidence, no import

## Canonical runtime paths

current_status_path: directions_v3/indie-game-development/runtime/state/CURRENT_STATUS.md
current_next_move_path: directions_v3/indie-game-development/runtime/state/CURRENT_NEXT_MOVE.md
project_binding_source_path: directions_v3/indie-game-development/runtime/config/DIRECTION_PROJECT_BINDING.md
project_setup_source_path: directions_v3/indie-game-development/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
project_files_manifest_path: directions_v3/indie-game-development/project_setup/PROJECT_FILES_MANIFEST.md

## Current continuation

primary_next_move: launch_direction_definition

## Boundary

This console is a setup-only navigation surface.

It does not define or accept:
- root outcome;
- Direction Spine;
- Direction Map;
- Active Front;
- Work Graph;
- Work Contract;
- roadmap;
- backlog;
- product strategy;
- product work;
- legacy import.

## Lifecycle signals

lifecycle_signals:
- direction_runtime_missing: resolved by setup-only placeholder package after acceptance/merge
- direction_adoption_needed: pending Direction Definition
- blocked_lifecycle_transition: product work blocked until Direction Definition and later accepted work admission
