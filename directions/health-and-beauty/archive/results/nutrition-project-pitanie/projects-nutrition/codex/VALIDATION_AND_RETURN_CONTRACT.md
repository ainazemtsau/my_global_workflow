# Nutrition Codex Validation and Return Contract

Status: active
Scope: Codex local operation inside `directions/health-and-beauty/projects/nutrition/**`

## Required validation after mutation

Run:

```text
git diff --stat
git diff --name-only
git status --short
```

Check changed paths.

Allowed normal changed path prefix:

```text
directions/health-and-beauty/projects/nutrition/
```

Forbidden path prefixes:

```text
workflow/
directions/health-and-beauty/project_files/
directions/health-and-beauty/phases/
directions/health-and-beauty/project_setup/
directions/workflow-governance/
directions/solo-max-productive/
directions/indie-game-development/
```

If forbidden paths changed unintentionally, revert them or report STUCK.

## Read-back anchors

For every changed file, read back enough content to prove the intended change exists.

Minimum anchors by file type:

### `CHATGPT_PROJECT_INSTRUCTIONS.md`

Read back:

- relevant mode routing section;
- changed authority/save/refresh behavior;
- changed user-facing behavior constraints.

### `project_files/*.md`

Read back:

- changed section heading;
- changed rules;
- changed expected output;
- changed acceptance criteria if applicable.

### `state/USER_PROFILE_AND_CONSTRAINTS.yml`

Read back:

- changed profile/preference fields;
- `known_unknowns`/`useful_later_questions` if affected.

### `state/GLOBAL_NUTRITION_PLAN.md`

Read back:

- plan status;
- changed strategy rules;
- approval/source notes.

### `research/*.md`

Read back:

- status;
- core changed sections.

### `weeks/current/*.md`

Read back:

- changed week/menu/tracking/review/next-week sections.

### `recipes/*.yml` and `recipes/*.md`

Read back:

- changed taxonomy/index metadata;
- confirmation that index remains metadata-only if affected.

### `recipes/catalog/*.json`, `recipes/bundles/*.json`, and `weeks/current/*.json`

Read back:

- JSON validation result;
- changed recipe or bundle identifiers;
- no credentials or bearer tokens were written.

### `AGENTS.md` or `codex/*.md`

Read back:

- changed Codex operating rules;
- scope and forbidden-path guard.

## EOF marker policy

If a changed file has an `END_OF_FILE:` marker:

- marker must appear exactly once;
- marker must be last non-whitespace content;
- do not append content after marker.

If the marker is broken, repair before commit or report STUCK.

## Commit and push

After validation passes:

```text
git add <changed files>
git commit -m "<appropriate message>"
git push origin codex/direction-health-and-beauty
```

Do not claim main integration unless actually merged or verified.

## Return format

Return exactly this structure:

```text
Status: DONE or STUCK

Request classification:
Worktree:
Branch:
Rebase result:

Changed files:
Diff summary:

Read-back anchors:
- file:
  anchors:

Forbidden-path check:
- workflow/**:
- directions/health-and-beauty/project_files/**:
- directions/health-and-beauty/phases/**:
- directions/health-and-beauty/project_setup/**:
- sibling Directions:
- result:

Legacy-file check:
- project_setup/pitanie reintroduced:
- superseded nutrition files reintroduced:
- result:

Commit SHA:
Push result:
Main integration status:

ChatGPT Project refresh required:
- yes/no

Refresh in Project `Питание`:
- Project Instructions:
- Project Files:
- State/research/week files:

Do not upload:
- AGENTS.md
- codex/*.md

Suggested quick test in Project `Питание`:
- prompt:
- expected behavior:

Blockers/warnings:
```

## Project Files refresh classification

If any changed file is one of:

```text
CHATGPT_PROJECT_INSTRUCTIONS.md
project_files/*.md
state/*.md
state/*.yml
research/*.md
weeks/ACTIVE_WEEK_POINTER.md
weeks/current/*.md
recipes/RECIPE_TAXONOMY.yml
recipes/RECIPE_CATALOG_INDEX.md
```

then:

```text
ChatGPT Project refresh required: yes
```

If only these changed:

```text
AGENTS.md
codex/*.md
```

then:

```text
ChatGPT Project refresh required: no
```

unless the user explicitly wants ChatGPT Project to see those docs.
