# Project Питание v0 Manifest

```yaml
manifest:
  schema: nutrition_project_manifest.v1
  package_name: "Питание"
  package_version: v0
  package_root: directions/health-and-beauty/projects/nutrition
  file_count: 11
  package_files:
    - directions/health-and-beauty/projects/nutrition/README.md
    - directions/health-and-beauty/projects/nutrition/CHATGPT_PROJECT_INSTRUCTIONS.md
    - directions/health-and-beauty/projects/nutrition/PROJECT_FILES_MANIFEST.md
    - directions/health-and-beauty/projects/nutrition/project_files/00_NUTRITION_START_HERE.md
    - directions/health-and-beauty/projects/nutrition/project_files/01_NUTRITION_BASE.md
    - directions/health-and-beauty/projects/nutrition/project_files/02_MENU_PREFERENCES.md
    - directions/health-and-beauty/projects/nutrition/project_files/03_ACTIVE_CYCLE.md
    - directions/health-and-beauty/projects/nutrition/project_files/04_TRACKING_AND_EXCEPTIONS.md
    - directions/health-and-beauty/projects/nutrition/project_files/05_REVIEW_AND_SYNC.md
    - directions/health-and-beauty/projects/nutrition/protocols/CODEX_SAVE_OPERATOR.md
    - directions/health-and-beauty/projects/nutrition/protocols/DRY_RUN_ACCEPTANCE.md
```

## Upload Set For The ChatGPT Project

Upload the six files under `project_files/` as the Project source files. Keep the README, manifest, and protocol files in the repository as operator/setup references.

## Validation Expectations

- The file set above is exact.
- Project Instructions are pasted separately and are not a Project source upload.
- The Project can operate from the six uploaded Project files without external process machinery.
- Dry-run acceptance uses only synthetic inputs.
- Codex Save Operator applies approved state packets only and gives no nutrition advice.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/PROJECT_FILES_MANIFEST.md`
