# FINDING_REGISTER

This is the canonical Workflow Governance finding register.

## Finding schema

```yaml
finding:
  finding_id:
  status:
  area:
  severity:
  confidence:
  evidence:
  recommendation:
  alternatives:
  patch_needed:
  approval_needed:
  next_action:
```

## Status values

- open
- accepted
- rejected
- deferred
- resolved
- needs_user_decision
- needs_research

## Severity values

- P0
- P1
- P2
- P3
- nonblocking

## Rules

- Evidence must cite GitHub paths or source-backed research references.
- Separate source-backed facts vs inference.
- Do not create a repository patch from a finding until approval.

## Findings

```yaml
finding:
  finding_id: WFG-FINDING-2026-05-13-001
  status: accepted
  area: github_context_transport
  severity: P1
  confidence: high
  evidence:
    - "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md returned with truncation marker during GitHub fetch."
    - "workflow/stage_prompts/C1_CODEX_GRAPH_PLAN.md returned with truncation marker during GitHub fetch."
    - "workflow/stage_prompts/C2_CODEX_EXECUTE.md returned with truncation marker during GitHub fetch."
    - "Base64 fetch did not provide a safe full-file workaround for the runtime core."
  recommendation:
    - "Use ChatGPT Project Files as runtime cache for core workflow files required in every chat."
    - "Treat truncated, omitted, or tail-unverified GitHub reads as blocking Context Request triggers."
    - "Treat truncated stage prompt reads as missing prompt context."
    - "Split long runtime/stage files later if needed."
  alternatives:
    - "Rely only on GitHub connector reads: rejected because required long files were observed truncated."
    - "Bulk-load all stage prompts into Project Files: rejected because stage prompts are request-only and this bloats context."
    - "Use base64 fetch as workaround: rejected because base64 response also truncated."
  patch_needed: true
  approval_needed: false
  next_action: "Apply WFG_PATCH_2026_05_13_GITHUB_LONG_FILE_READ_GUARD and refresh ChatGPT Project Files runtime cache."
```

```yaml
finding:
  finding_id: WFG-FINDING-2026-05-18-001
  status: accepted
  area: lifecycle_state_reconciliation
  severity: P1
  confidence: high
  evidence:
    - "Incident report: final F0 synthesis advanced the Goal artifact and execution log to pending R1 while Direction Project Files and Phase Brief remained pending E1."
    - "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md showed synthesis_formalized and parent_goal_completion_candidate."
    - "directions/indie-game-development/project_files/04_ACTIVE_GOAL.md still showed goal_shaped_pending_E1 and next_route E1_EXECUTION_BRIEF."
    - "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/execution_log.md had an END_OF_FILE marker before later entries."
  recommendation:
    - "Add mandatory Lifecycle State Reconciliation Gate to shared runtime behavior."
    - "Extend transport packets with project_files_state, fresh_sources_for_stage, lifecycle_state_reconciliation, and structural_integrity_validation."
    - "Require Codex repository maintenance to distinguish physical cached-file changes from logical runtime state changes."
    - "Require EOF markers to remain unique final tail markers and append before EOF."
  alternatives:
    - "Only repair Indie Game Project Files: rejected because the defect can recur in other Directions."
    - "Tell R1 to ignore Project Files: rejected because stale default cache can still misroute launches."
    - "Rely on manual user context: rejected because the Workflow target is autonomous stage handoff."
  patch_needed: true
  approval_needed: false
  next_action: "Apply wg_lsrg_runtime_hardening_2026_05_18 and refresh shared runtime Project Files in all active Direction Projects."
```
