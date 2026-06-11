# Indie Game Development

Direction ID: `indie-game-development`

Source of truth: GitHub repository markdown.

## Layout

Live workflow lives in `workflow/`.

Root is navigation only, not a dump of workflow files.

Accepted state is read from `workflow/LEDGER.md` and committed receipts.

Next valid run is read from `workflow/DASHBOARD.md` and `workflow/OBLIGATIONS.md`.

Project setup is under `workflow/project_setup/`.

Archive is `legacy_evidence` only. Do not load archive content by default, and do not treat archived material as accepted live state.
