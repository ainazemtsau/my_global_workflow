# 06 Context Library Index - Workflow Governance

```yaml
artifact_control:
  artifact_name: "06 Context Library Index - Workflow Governance"
  schema: context_library_index.v1
  owner_layer: persistence
  status: canonical
  repo_path: "directions/workflow-governance/project_files/06_CONTEXT_LIBRARY_INDEX.md"
  default_load: yes
  freshness: fresh
  last_updated: "2026-05-12"
```

## Default context

Load these files by default for Workflow Governance runtime:

- `directions/workflow-governance/project_files/00_DIRECTION_START_HERE.md`
- `directions/workflow-governance/project_files/01_DIRECTION_STATE.md`
- `directions/workflow-governance/project_files/02_CURRENT_PHASE.md`
- `directions/workflow-governance/project_files/03_FOCUS_REGISTER.md`
- `directions/workflow-governance/project_files/04_ACTIVE_GOAL.md`
- `directions/workflow-governance/project_files/05_PORTFOLIO_QUEUE.md`
- `directions/workflow-governance/project_files/06_CONTEXT_LIBRARY_INDEX.md`
- `directions/workflow-governance/project_files/07_PHASE_MEMORY_INDEX.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`

## Shared workflow context

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`
- `workflow/stage_prompts/`

Stage prompts are request-only by exact stage ID.

Do not bulk-load all stage prompts.

## Real Direction behavior context

Use `directions/*/project_files/` only when auditing real Direction behavior.

Do not load sibling Direction files by default.

## Governance context

Findings/register files:

- `directions/workflow-governance/findings/FINDING_REGISTER.md`
- `directions/workflow-governance/findings/OPEN_FINDINGS.md`
- `directions/workflow-governance/findings/ACCEPTED_CHANGES.md`
- `directions/workflow-governance/findings/REJECTED_OR_DEFERRED.md`

Evals files:

- `directions/workflow-governance/evals/WORKFLOW_EVAL_SUITE.md`
- `directions/workflow-governance/evals/STAGE_REGRESSION_MATRIX.md`
- `directions/workflow-governance/evals/TRANSPORT_CONTRACT_CHECKLIST.md`
- `directions/workflow-governance/evals/REAL_DIRECTION_TEST_CASES.md`

Research files:

- `directions/workflow-governance/research/RESEARCH_SOURCE_REGISTER.md`
- `directions/workflow-governance/research/WEEKLY_RESEARCH_DIGEST.md`
- `directions/workflow-governance/research/BEST_PRACTICE_MAP.md`

## Phase Memory Index default context amendment

Default Direction Project Files include:

- `directions/workflow-governance/project_files/07_PHASE_MEMORY_INDEX.md`

Use `07_PHASE_MEMORY_INDEX.md` as compact phase-history context before P0 proposes a new Phase after closure.