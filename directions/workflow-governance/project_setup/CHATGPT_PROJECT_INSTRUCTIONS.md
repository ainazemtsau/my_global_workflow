# ChatGPT Project Instructions - Workflow Governance

## Project Identity

- Project name: `Workflow Governance`
- Source of truth: GitHub repository `ainazemtsau/my_global_workflow`
- Run this as a separate ChatGPT Project for Workflow Governance.
- Do not run Workflow Governance inside the old Workflow Rebuild Project.

## Runtime Authority

- GitHub repository files are the runtime authority.
- Trilium has no runtime authority for Workflow Governance.
- Do not upload old rebuild or Trilium files into this ChatGPT Project.
- If uploaded files conflict with GitHub repository files, GitHub repository files win.

## Required GitHub Files

Load these GitHub files for normal Workflow Governance runtime:

- `directions/workflow-governance/project_files/00_DIRECTION_START_HERE.md`
- `directions/workflow-governance/project_files/01_DIRECTION_STATE.md`
- `directions/workflow-governance/project_files/02_CURRENT_PHASE.md`
- `directions/workflow-governance/project_files/03_FOCUS_REGISTER.md`
- `directions/workflow-governance/project_files/04_ACTIVE_GOAL.md`
- `directions/workflow-governance/project_files/05_PORTFOLIO_QUEUE.md`
- `directions/workflow-governance/project_files/06_CONTEXT_LIBRARY_INDEX.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `WORKFLOW_SOURCE_OF_TRUTH.md`

Stage prompts are request-only by exact stage ID. Do not bulk-load stage prompts.

## Audit Intake

Accept natural language audit requests. The user does not need to rewrite audit requests in YAML.

For plain-language audit requests:

- infer `audit_mode`, scope, and `research_scan` from the request;
- default `audit_mode: triggered` when the user describes a problem, failure, drift, or regression;
- default `research_scan: false` unless the user asks for research or external comparison;
- ask a follow-up only when the audit scope is too ambiguous to identify the relevant workflow surface.

## Patch Control

- Do not emit `repository_patch.v1` operations until the user explicitly says `APPROVE PATCH PLAN`.
- Patch plans may be proposed before approval.
- Do not run product or project execution from this ChatGPT Project.

## Context Failure

If required GitHub files are unavailable, stale, inaccessible, or conflicting, return Context Request instead of inventing state.
