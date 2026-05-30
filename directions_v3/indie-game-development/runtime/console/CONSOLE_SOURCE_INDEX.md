# Runtime Console Source Index

status: active
direction_id: indie-game-development
adoption_mode: clean_start
legacy_import: none
runtime_console: read-only

## Console Boundary

Runtime Console: read-only

The console may summarize verified status, show uncertainty, list candidate actions, and draft candidate Launch Packets or Next Moves.

It must not execute work, mutate accepted state, accept evidence, promote Memory, import legacy state, or update Project setup surfaces.

## Default Sources

| Source | Purpose |
| --- | --- |
| state/DIRECTION_SPINE.md | Current Direction Spine status and pending decisions. |
| state/ACTIVE_FRONT.md | Current Active Front. |
| state/CURRENT_STATUS.md | Current runtime status. |
| state/CURRENT_NEXT_MOVE.md | Exact next move. |
| indexes/FRONTS_INDEX.md | Front lookup. |
| indexes/RECORDS_INDEX.md | Record lookup. |
| operations/action_inbox/ACTION_INBOX.md | Candidate actions. |
| memory/MEMORY_INDEX.md | Promoted memory lookup. |
| config/PROJECT_SETUP_NOTES.md | Project setup refresh boundary. |
| config/LEGACY_EVIDENCE_BOUNDARY.md | Legacy evidence boundary. |

## Current Console Summary

accepted_product_root_result: pending_current_human_decision
accepted_success_conditions: pending_current_human_decision
next move: define current Direction Spine from current human decision

END_OF_FILE: directions_v3/indie-game-development/runtime/console/CONSOLE_SOURCE_INDEX.md
