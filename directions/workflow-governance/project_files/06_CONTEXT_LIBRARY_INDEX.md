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

Load these files by default for Workflow Governance runtime.

In the ChatGPT Project, these files should be present as Project Files runtime cache so the chat does not depend on potentially truncated GitHub connector reads for core workflow behavior:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`
- `workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`
- `directions/workflow-governance/project_files/00_DIRECTION_START_HERE.md`
- `directions/workflow-governance/project_files/01_DIRECTION_STATE.md`
- `directions/workflow-governance/project_files/02_CURRENT_PHASE.md`
- `directions/workflow-governance/project_files/03_FOCUS_REGISTER.md`
- `directions/workflow-governance/project_files/04_ACTIVE_GOAL.md`
- `directions/workflow-governance/project_files/05_PORTFOLIO_QUEUE.md`
- `directions/workflow-governance/project_files/06_CONTEXT_LIBRARY_INDEX.md`
- `directions/workflow-governance/project_files/07_PHASE_MEMORY_INDEX.md`

GitHub remains the source of truth. Project Files are a runtime cache.

If GitHub and Project File cache conflict, use verified full GitHub read-back. If GitHub read is truncated, omitted, lacks tail verification, or cannot be verified, return Context Request instead of treating partial GitHub content as authority.

## Shared workflow context

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`
- `workflow/stage_prompts/`

Stage prompts are request-only by exact stage ID.

Do not bulk-load all stage prompts.

## Workflow Governance Maintenance Mode context

Workflow Governance Maintenance Mode may inspect workflow files directly as audit and repair targets.

Typical maintenance targets include:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/`
- `workflow/stage_registry/`
- `workflow/stage_prompts/`
- `workflow/transport/`
- `docs/CHATGPT_PROJECT_SETUP.md`
- `directions/*/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`
- `directions/*/project_files/00_DIRECTION_START_HERE.md`
- `directions/*/project_files/06_CONTEXT_LIBRARY_INDEX.md`

Stage prompts are request-only for execution, but they may be read by Codex/local audit or supplied as verified bundles when they are audit targets.

Do not bulk-load all stage prompts into ChatGPT Project Files.

For workflow maintenance tasks, do not require lifecycle stage prompts merely to continue the audit/repair process. Require an exact stage prompt only when the user explicitly asks to execute that stage or when exact prompt wording is material to the audit.

## Project setup

- `directions/workflow-governance/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`

Use this file when creating or updating the separate ChatGPT Project for Workflow Governance.

## Forbidden default context

Do not load these files as default Workflow Governance context:

- old Trilium rebuild files
- `01_WORKFLOW_REBUILD_CONTROL_PACK.md`
- `02_CURRENT_REBUILD_STATE.md`
- `03_CODEX_TRILIUM_INSTALLER_UNIVERSAL.md`

Load them only when the user explicitly asks to audit the historical rebuild process.

## Real Direction behavior context

Use `directions/*/project_files/` only when auditing real Direction behavior.

Do not load sibling Direction files by default.

## Shared workflow rollout context

When auditing or changing shared workflow runtime behavior, load/check all active Direction setup surfaces as needed:

```text
directions/workflow-governance/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
directions/solo-max-productive/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
directions/indie-game-development/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
directions/health-and-beauty/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
docs/CHATGPT_PROJECT_SETUP.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
```

For shared workflow changes, do not stop at Workflow Governance files. Check whether every active Direction Project needs Project Instructions or Project Files refresh.

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
