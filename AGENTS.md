# Repository Agent Instructions

Status: active

This repository is the canonical AI workflow source for the Workflow OS.

Rules:
- Treat this repository as active/canonical only while `WORKFLOW_SOURCE_OF_TRUTH.md` says `active`.
- Use `workflow/**` as the active workflow authority.
- Do not use old stage, phase, goal, or vNext-R files as active authority.
- Do not treat old Direction `project_files/00-08` as accepted state.
- Do not invent Direction proof state.
- Do not touch other Direction folders unless the task explicitly names them.
- Use small diffs.
- Do not delete files or notes without explicit approval.
- For repository maintenance, preserve the workflow rule: Receipt -> Verify -> Commit -> Ledger update.
- For Codex, repository maintenance is the default unless an explicit product execution task exists.
- Do not run product/project execution by default.
- Report separated project refresh requirements when changed files affect ChatGPT Projects: Project Instructions UI updates, Project Instructions UI payload character counts when instruction sources change, Project Files/Sources refreshes, request-only source refreshes, and files that must not be uploaded as Project Files/Sources.
- If old workflow runtime, stage, or transport evidence is needed, use the legacy branch/tag and the Legacy Import Receipt process.
