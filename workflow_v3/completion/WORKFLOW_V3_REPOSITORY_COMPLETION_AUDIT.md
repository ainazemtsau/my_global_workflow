# Workflow v3 Repository Completion Audit

status: active_repository_completion_framework

## Audit scope

This audit covers the repository-side Workflow v3 completion framework:

- completion matrix;
- clean-start adoption package model;
- canonical procedure stubs and runtime operation procedures;
- evals and validation gates;
- Project setup and pack source readiness alignment;
- index reconciliation.

It explicitly does not cover actual Direction adoption, runtime root creation, legacy import, ChatGPT Project UI update, Project Files/Sources refresh, request-only source refresh, generated pack upload, product execution, or old Workflow OS decommission.

## Required source authority

Material decisions must use exact repository files at a named repo/path/ref.

Project Files/Sources, pasted excerpts, prior chat summaries, generated packs, and candidate docs are cache/context. Candidate docs under `workflow/candidates/**` are design evidence only and not accepted Workflow v3 authority.

## Audit checklist

| Check | Required evidence | Status |
| --- | --- | --- |
| Base ref verified | `origin/main` SHA is at or after the accepted Workflow v3 templates package merge commit. | required per package result |
| Required reads completed | Root/source, accepted v3 docs, interfaces, templates, project setup sources, and project pack source model read from repository files. | required per package result |
| Allowed paths only | Changes limited to `workflow_v3/**`, `README.md`, and `directions_v3/README.md`. | required per package result |
| Forbidden paths untouched | No `workflow/**`, `directions/**`, product repository, or runtime-root paths changed. | required per package result |
| No runtime root | No `directions_v3/<direction-id>/runtime/**` created. | required per package result |
| Entity coverage preserved | Registry entity count and interface coverage rows do not decrease. | required per package result |
| Completion matrix coverage | Every registry entity appears in `WORKFLOW_V3_COMPLETION_MATRIX.md`. | required per package result |
| Procedure stub completeness | Every unauthored procedure stub includes target role, workflow integration, future body scope, required outputs, closure shape, and STOP behavior. | required per package result |
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
- Run, Result Packet, Evidence, and Codex commit are not Acceptance Decision.
- Parent Integration Result is not Acceptance Decision and cannot synthesize missing child/work evidence.
- Graph Delta, Upstream Escalation Packet, Downstream Delta Packet, and Derived Gate Check are not accepted state mutation by existence.
- Result Packet is not acceptance.
- Next Move Packet is not hidden continuation.
- Transfer Packet is not manual user assembly.
- Check Job is not material work.
- Child Chat is not next material chat or independent execution track.
- Runtime Console is not hidden controller.
- Project Instructions UI is not documentation storage.
- Project Files/Sources are not source authority.
- Repository commit is not actual ChatGPT Project update.
- legacy_evidence is not accepted v3 state.
- clean-start adoption is not migration.

## Completion finding

The repository completion framework is complete when all validation checks pass without requiring a real Direction adoption, runtime root, legacy import, Project UI update, Project Files/Sources refresh, generated pack upload, product execution, or old Workflow OS decommission.

END_OF_FILE: workflow_v3/completion/WORKFLOW_V3_REPOSITORY_COMPLETION_AUDIT.md
