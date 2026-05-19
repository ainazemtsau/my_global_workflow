# Project Питание v0

This folder is the repo-backed package for a standalone ChatGPT Project named `Питание`.

It is a manual-install package, not evidence that the Project has already been created in ChatGPT, not a live diet, and not clinical nutrition advice.

## Install Order

1. Create a ChatGPT Project named `Питание`.
2. Paste `CHATGPT_PROJECT_INSTRUCTIONS.md` into the Project instructions field.
3. Upload the six files in `project_files/` as the Project's durable source files.
4. Keep `PROJECT_FILES_MANIFEST.md` as the package manifest.
5. Use `protocols/DRY_RUN_ACCEPTANCE.md` to validate a fresh Project chat before relying on it.
6. Use `protocols/CODEX_SAVE_OPERATOR.md` only when an approved state-update packet needs to be saved back to the repository.

## Runtime Shape

Project `Питание` is a low-friction nutrition operating loop. It supports:

- start or resume from durable state;
- cycle/default menu planning from baseline and preferences;
- meal, photo, or voice-style event intake with missing-answer defaults;
- practical correction after off-menu eating or overeating;
- day/week review;
- compact `nutrition_state_update_packet.v1` output for approved saving.

## Boundaries

- No live user diet/menu is included in this package.
- No heavy calorie or macro ledger is required by default.
- No food database, API automation, external tracker, or app import is required.
- No training, cardio, recovery, supplements, fasting, labs, or clinical protocol is included.
- Codex Save Operator saves approved packets only; it does not interpret nutrition content or give nutrition advice.

## File Set

The exact package file set is listed in `PROJECT_FILES_MANIFEST.md`.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/README.md`
