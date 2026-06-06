# Repository Agent Instructions

Status: active

This repository is the canonical AI workflow source for Workflow governance and Workflow v3 maintenance.

Rules:
- Treat this repository as active/canonical only while `WORKFLOW_SOURCE_OF_TRUTH.md` says `active`.
- For tasks explicitly targeting Workflow v3, use exact files under `workflow_v3/**` as the current Workflow v3 governance/setup/procedure authority.
- For tasks explicitly targeting the old Workflow OS or rollback surface, use `workflow/**` only within that explicitly scoped legacy/rollback task.
- Do not use `workflow/**` as default authority for `workflow_v3/**` tasks.
- Exact repository files at named path/ref win over ChatGPT Project Files/Sources, pasted snippets, chat memory, candidate docs, or legacy evidence.
- Do not use old stage, phase, goal, vNext-R files, old Direction `project_files/00-08`, or old Workflow OS files as active Workflow v3 authority unless an explicit accepted bridge/import/adoption package authorizes it.
- Do not invent Direction proof state.
- Do not touch other Direction folders unless the task explicitly names them.
- Use small diffs.
- Do not delete files or notes without explicit approval.
- For repository maintenance, preserve the workflow rule: Receipt -> Verify -> Commit -> Ledger update when the scoped workflow source requires that path.
- For Codex, repository maintenance is the default unless an explicit product execution task exists.
- Do not run product/project execution by default.
- Obey the task's allowed paths, forbidden paths, validation, stop conditions, commit/push instructions, and requested return fields.
- Report separated project refresh requirements when changed files affect ChatGPT Projects: Project Instructions UI updates, Project Instructions UI payload character counts when instruction sources change, Project Files/Sources refreshes, request-only source refreshes, and files that must not be uploaded as Project Files/Sources.
- If old workflow runtime, stage, or transport evidence is needed, use the legacy branch/tag and the Legacy Import Receipt process.
