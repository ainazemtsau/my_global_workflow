# Console Source Index

console_role: read_only_status_navigation

## Default Current Sources

- state/DIRECTION_SPINE.md
- state/ACTIVE_FRONT.md
- state/CURRENT_STATUS.md
- state/CURRENT_NEXT_MOVE.md
- operations/action_inbox/ACTION_INBOX.md
- indexes/FRONTS_INDEX.md
- indexes/RECORDS_INDEX.md
- config/QUALITY_GATES.md
- config/LEGACY_EVIDENCE_BOUNDARY.md

## Request-Only Sources

- exact front node files
- exact future Work Contracts
- exact future Runs
- exact future Evidence
- old Direction files as legacy_evidence

## Forbidden

- treating Project Files/Sources as truth
- treating old files as accepted_v3_state
- executing work from Console
- accepting evidence from Console

## Boundary

Runtime Console is read-only. This clean_start package is for one Direction only.

No actual ChatGPT Project UI update is performed. No Project Files/Sources refresh is performed. Project Files/Sources are cache/context only.

END_OF_FILE: directions/indie-game-development/runtime/console/CONSOLE_SOURCE_INDEX.md
