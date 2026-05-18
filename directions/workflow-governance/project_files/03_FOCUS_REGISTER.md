# 03 Focus Register - Workflow Governance

```yaml
artifact_control:
  artifact_name: "03 Focus Register - Workflow Governance"
  schema: focus_register.v1
  owner_layer: persistence
  status: canonical
  repo_path: "directions/workflow-governance/project_files/03_FOCUS_REGISTER.md"
  default_load: yes
  freshness: fresh
  last_updated: "2026-05-12"
```

## Current focus

Bootstrap a durable Workflow Governance Direction for Workflow Steward Audit work.

## Active focus lanes

| Lane | Status | Notes |
| --- | --- | --- |
| Runtime contract audit | ready | Use `evals/WORKFLOW_EVAL_SUITE.md`. |
| Lifecycle logic audit | ready | Focus on phase, goal, review, closure, and routing behavior. |
| Objective architecture / basis-validity hardening | active | Implement and validate Horizon Acceptance Proof, Active Frontier, and Next Action Proof. |
| UX/human burden audit | ready | Identify unnecessary wall-of-text, unclear approvals, or manual burden. |
| Context hygiene audit | ready | Check default loads, prompt request rules, and cross-Direction boundaries. |
| Real usage friction audit | ready | Capture friction from actual Direction usage. |
| External best-practice/research audit | ready | Use source-backed facts vs inference. |

## Mandatory cross-Direction rollout focus

Shared workflow runtime changes must include a cross-Direction rollout check.

When Workflow Governance changes shared runtime/core/registry/source-of-truth/project-setup behavior, check all active Directions:

- `directions/workflow-governance`
- `directions/solo-max-productive`
- `directions/indie-game-development`
- `directions/health-and-beauty`

Check at minimum:

- Project Instructions source/update need;
- Project Files runtime cache file list;
- `00_DIRECTION_START_HERE.md` default Project Files list;
- `06_CONTEXT_LIBRARY_INDEX.md` default context;
- Project Files cache refresh requirements.

## Focus constraints

- No repository patch until approval.
- No product/project execution.
- Stage prompts request-only by exact stage ID.
- No bulk-loading all stage prompts.
