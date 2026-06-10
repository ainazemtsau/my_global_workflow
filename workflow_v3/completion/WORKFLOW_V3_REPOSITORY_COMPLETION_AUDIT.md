# Workflow v3 Repository Completion Audit

status: active_repository_completion_framework

## Audit scope

This audit is a repository framework coverage audit. It covers the repository-side Workflow v3 completion framework:

- completion matrix;
- clean-start adoption package model;
- canonical procedure files, including active procedures and pending-authoring stubs, whose implementation status remains authoritative in each procedure file header;
- evals and validation gates;
- Project setup and pack source readiness alignment;
- index reconciliation.

It explicitly does not cover actual Direction adoption, runtime root creation, legacy import, ChatGPT Project UI update, Project Files/Sources refresh, request-only source refresh, generated pack upload, product execution, or old Workflow OS decommission.

Explicitly authorized decommission/cleanup packages may delete named concrete Direction folders. They must not modify unrelated Direction folders, and they must validate that stale references to the deleted Direction ID do not remain in active v3/current setup docs.

## Status taxonomy

This audit may support the following repository/runtime distinction:

- `repository_framework_coverage_complete` - repository-side framework surfaces have the required coverage and validation hooks.
- `runtime_not_created` - no `directions_v3/<direction-id>/runtime/**` root is created by this audit.
- `directions_not_adopted` - no Direction is adopted by this audit.
- `migration_not_performed` - no legacy Direction state is migrated, bridged, imported, or accepted by this audit.
- `project_ui_not_updated` - no actual ChatGPT Project Instructions UI is updated by this audit.
- `project_files_not_refreshed` - no Project Files/Sources or request-only sources are refreshed by this audit.

## Required source authority

Material decisions must use exact repository files at a named repo/path/ref.

Project Files/Sources, pasted excerpts, prior chat summaries, generated packs, and candidate docs are cache/context. Candidate docs under `workflow/candidates/**` are design evidence only and not accepted Workflow v3 authority.

## Audit checklist

| Check | Required evidence | Status |
| --- | --- | --- |
| Base ref verified | `origin/main` SHA is at or after the accepted Workflow v3 templates package merge commit. | required per package result |
| Required reads completed | Root/source, accepted v3 docs, interfaces, templates, project setup sources, and project pack source model read from repository files. | required per package result |
| Allowed paths only | Changes limited to the package's explicit allowed paths. Standard completion packages use `workflow_v3/**`, `README.md`, and `directions_v3/README.md`; authorized cleanup packages may include named concrete Direction folders for deletion. | required per package result |
| Forbidden paths untouched | No `workflow/**`, unrelated `directions/**`, product repository, or unauthorized runtime-root paths changed. | required per package result |
| No unadmitted runtime root | No `directions_v3/<direction-id>/runtime/**` created without explicit package authority. | required per package result |
| Cleanup stale-reference validation | For authorized decommission packages, deleted Direction IDs have no active stale references outside allowed historical/legacy evidence. | required per package result |
| Entity coverage preserved | Registry entity count and interface coverage rows do not decrease. | required per package result |
| Completion matrix coverage | Every registry entity appears in `WORKFLOW_V3_COMPLETION_MATRIX.md`. | required per package result |
| Procedure stub completeness | Every unauthored procedure stub includes target role, workflow integration, future body scope, required outputs, closure shape, and STOP behavior. | required per package result |
| Procedure status/index sync | Registry entry -> procedure file exists -> status -> index labels are validated by `workflow_v3/tools/check_procedure_status_index_sync.py`. | required per package result |
| Eval completeness | Every eval includes PASS/WARN/FAIL criteria and recovery action. | required per package result |
| Project setup separation | Project UI, Project Files/Sources, request-only refresh, and do-not-upload categories reported separately. | required per package result |
| Project Instructions payload counts | If Project Instructions sources changed, UI payload marker counts measured against 8,000 hard max. | required per package result |
| EOF markers | Every new/edited Markdown file has `END_OF_FILE`. | required per package result |
| Diff validation | `git diff --check` passes or warnings are reported separately. | required per package result |

## Anti-flattening audit

Completion is valid only if these boundaries remain explicit:

- Direction Spine is not Direction Map.
- Direction Map is not roadmap, backlog, Work Graph, or unreviewed task list.
- Goal Evidence Graph is not a semantic primitive, accepted state by existence, roadmap, backlog, or global Work Graph.
- Active Unresolved Cut is not a Work Graph, backlog, launch authority, or the whole Direction becoming active.
- Active Front is not all active work or Work Graph.
- Work Graph is local to one Active Front and not global Direction Map.
- Work Contract is not route authority.
- Run, STAGE_RESULT, Evidence, and Codex commit are not Acceptance Decision.
- Parent Integration Result is not Acceptance Decision and cannot synthesize missing dependency/work evidence.
- Graph Delta, Upstream Escalation Packet, Downstream Delta Packet, and Derived Gate Check are not accepted state mutation by existence.
- FINISH_PACKET is not acceptance.
- NEXT_CHAT_CARD is not hidden continuation.
- Transfer Packet is not manual user assembly.
- Check Job is not material work.
- Dependency Chat is not next material chat or independent execution track.
- Runtime Console is not hidden controller.
- Project Instructions UI is not documentation storage.
- Project Files/Sources are not source authority.
- Repository commit is not actual ChatGPT Project update.
- legacy_evidence is not accepted v3 state.
- clean-start adoption is not migration.

## Completion finding

The repository completion framework finding is `repository_framework_coverage_complete` when all validation checks pass.

That finding is not runtime completion, Direction adoption, legacy migration/import, Project UI update, Project Files/Sources refresh, generated pack upload, product execution, or old Workflow OS decommission. It cannot be used as proof that Workflow v3 ordinary Direction runtime is live or ready without the separate packages and external actions named above.

END_OF_FILE: workflow_v3/completion/WORKFLOW_V3_REPOSITORY_COMPLETION_AUDIT.md
