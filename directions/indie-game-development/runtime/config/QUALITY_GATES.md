# Quality Gates

## Gates

- source gate
- scope gate
- evidence gate
- acceptance gate
- Codex validation gate
- Project setup refresh gate
- rollback/coexistence gate

No validation means no done claim.

## Gate Boundaries

The source gate requires exact repo/path/ref when exact state matters. Project Files/Sources are cache/context only.

The scope gate keeps this package to one clean_start Direction adoption under `directions/indie-game-development/runtime/**`.

The evidence gate requires validation output before any done claim.

The acceptance gate requires explicit acceptance/update path. Adapters, document existence, Project Files/Sources, and Runtime Console do not create accepted state.

The Codex validation gate requires branch name, commit SHA when committed, changed files, allowed paths only, forbidden paths unchanged, validation results, EOF markers for Markdown, residual risks, and project refresh requirements.

The Project setup refresh gate requires reporting Project Instructions UI, Project Files/Sources, request-only sources, and do-not-upload requirements separately.

The rollback/coexistence gate requires the old Workflow OS to remain untouched and available.

Old Direction files are legacy_evidence only. No old Ledger, Obligations, Receipts, Dashboard, Migration receipt, project_setup, project_files, archive, or run history is accepted_v3_state.

END_OF_FILE: directions/indie-game-development/runtime/config/QUALITY_GATES.md
