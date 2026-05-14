# 06_CONTEXT_LIBRARY_INDEX.md

```yaml
artifact_control:
  artifact_name: "06_CONTEXT_LIBRARY_INDEX.md"
  schema: context_loading_index.v1
  owner_layer: persistence
  status: projection
  source_file: "directions/solo-max-productive/project_files/06_CONTEXT_LIBRARY_INDEX.md"
  default_load: yes
  freshness: fresh
  last_refresh_at: "2026-05-14"
  refresh_source: "P0-2026-05-14-exocortex-app-foundation-repair"
```

## Default context

Load these files by default for Solo Max Productive runtime.

In the ChatGPT Project, these files should be present as Project Files runtime cache so the chat does not depend on potentially truncated GitHub connector reads for core workflow behavior:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`
- `workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`
- `directions/solo-max-productive/project_files/00_DIRECTION_START_HERE.md`
- `directions/solo-max-productive/project_files/01_DIRECTION_STATE.md`
- `directions/solo-max-productive/project_files/02_CURRENT_PHASE.md`
- `directions/solo-max-productive/project_files/03_FOCUS_REGISTER.md`
- `directions/solo-max-productive/project_files/04_ACTIVE_GOAL.md`
- `directions/solo-max-productive/project_files/05_PORTFOLIO_QUEUE.md`
- `directions/solo-max-productive/project_files/06_CONTEXT_LIBRARY_INDEX.md`
- `directions/solo-max-productive/project_files/07_PHASE_MEMORY_INDEX.md`

GitHub remains the source of truth. Project Files are a runtime cache.

If GitHub and Project File cache conflict, use verified full GitHub read-back. If GitHub read is truncated, omitted, lacks tail verification, or cannot be verified, return Context Request instead of treating partial GitHub content as authority.

## EXOCORTEX foundation context for G1

Required for the next `G1_GOAL_SHAPE` run:

- `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/source_materials/EXOCORTEX_CONCEPT_SEED_FULL.md`
- P0 result / repository patch / Codex return from `P0-2026-05-14-exocortex-app-foundation-repair`
- User correction: current workflow remains the construction workflow; EXOCORTEX is the future application and should replace current workflow only after radical superiority/full readiness.

Purpose:

- Shape `EXOCORTEX Product Foundation Definition`.
- Treat EXOCORTEX as the future target application / personal external brain.
- Preserve current ChatGPT + GitHub + Codex workflow as the construction workflow.
- Define product/application foundation: target system, principles, core loop, conceptual subsystem map, buildable foundation, non-goals, and validation criteria.
- Do not execute the old proof Goal.
- Do not treat the old replacement candidate as current.
- Do not implement the app during G1.
- Do not choose tech stack or full architecture before the appropriate later route.
- Do not treat `EXOCORTEX_CONCEPT_SEED_FULL.md` as an executable implementation roadmap.

If GitHub read of `EXOCORTEX_CONCEPT_SEED_FULL.md` is truncated or lacks tail verification, request one of:

- manual paste/upload as chat attachment;
- split/chunked export with tail verification;
- Codex read-only local verification/export.

## Superseded Goal comparison context

Request only if G1 needs comparison material:

- `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/00_GOAL_CONTRACT.md`
- `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/01_GOAL_WORKING_CONTEXT.md`
- `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/02_GOAL_CONTEXT_INDEX.md`
- `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/execution_log.md`

Use old Goal files only as superseded comparison material.

## Request-only context

- `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/source_materials/EXOCORTEX_CONCEPT_SEED_FULL.md`

Load for EXOCORTEX foundation shaping. Do not treat as an executable implementation roadmap.

## Archive boundary

- Archived or historical material is pointer-only and must not be default-loaded.
- vNext One-Goal Smoke Test is historical/test state for this route, not current active work.
- Create Lightweight Codex Small-Fix Lane is not current active Goal state unless explicitly reactivated.
- Personal Workflow App Kernel Min Proof is superseded as an execution target and should be used only as comparison/provenance unless explicitly reactivated by a later human decision.
- Personal Workflow System Core and MVP Definition is superseded as the current replacement candidate by the approved EXOCORTEX App Foundation phase repair.

## Phase Memory Index default context amendment

Required default Project Files include:

- `07_PHASE_MEMORY_INDEX.md`

Use `directions/solo-max-productive/project_files/07_PHASE_MEMORY_INDEX.md` as compact phase-history context before P0 proposes a materially new Phase after closure or restart.
