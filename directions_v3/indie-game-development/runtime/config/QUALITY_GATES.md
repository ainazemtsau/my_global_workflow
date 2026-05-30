# Quality Gates

status: active
direction_id: indie-game-development
adoption_mode: clean_start
legacy_import: none

## Required Gates

Source gate:

- exact repository files win over cache/context;
- missing exact state must be reported;
- old Direction files remain legacy_evidence only.

Scope gate:

- allowed and forbidden paths must be explicit for repository work;
- product execution must not start until the Direction Spine is accepted.

Evidence gate:

- no validation means no done claim;
- result evidence must name commands, changed files, and limitations.

Acceptance gate:

- accepted state changes require explicit acceptance/update paths;
- adapters do not accept their own output.

Project setup refresh gate:

- Project Instructions UI update: none unless separately authorized;
- Project Files/Sources refresh: none unless separately authorized;
- request-only sources refresh: none unless separately authorized.

END_OF_FILE: directions_v3/indie-game-development/runtime/config/QUALITY_GATES.md
