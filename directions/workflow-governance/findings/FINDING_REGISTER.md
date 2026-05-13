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
