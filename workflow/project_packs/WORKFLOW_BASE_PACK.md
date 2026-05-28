---
artifact_control:
  namespace: workflow_project_packs
  artifact_type: project_pack
  pack_name: WORKFLOW_BASE_PACK
  pack_type: runtime_cache_upload_convenience
  intended_load_mode: default_all_directions
  status: overblocking_admission_guardrails_refreshed
  owner: workflow_os
  generated_from_ref: wg/overblocking-admission-guardrails-fix
  refreshed_for_receipt: null
  do_not_use_as_authority: true
  refresh_rule: "Regenerate and refresh this pack if any source_manifest file changes."
source_manifest:
  - workflow/core/00_WORKFLOW_OS.md
  - workflow/core/01_SEMANTIC_KERNEL.md
  - workflow/core/02_RUNTIME_PROTOCOLS.md
  - workflow/policies/03_VERIFY_AND_COMMIT_POLICY.md
  - workflow/policies/05_OPERATOR_CATALOG_POLICY.md
  - workflow/policies/06_PROJECTION_POLICY.md
  - workflow/policies/07_MIGRATION_PROTOCOL.md
  - workflow/invariants/CORE_INVARIANTS.md
  - workflow/evals/MIGRATION_VALIDATION_CHECKLIST.md
---

# Workflow Base Pack

## Cache Boundary

This pack is a ChatGPT Project Files runtime cache / upload convenience artifact.

It is not semantic authority.

Canonical source files listed in `source_manifest` remain authority.

If this pack conflicts with a verified canonical source file, the canonical source wins.

If any `source_manifest` file changes, regenerate and refresh this pack before using it as Project Files cache.

## Semantic Kernel

Tier 0 semantic primitives are only:

- Ledger
- Obligation
- Operator
- Receipt
- Invariant

Execution, stage, layer, roadmap, Direction, pack, project, file, schema, dashboard, and document are not semantic primitives.

## Runtime Law

The workflow movement is:

```text
Obligation -> Operator -> Receipt -> Verify -> Commit
```

One material Operator invocation works over one Obligation and returns a Receipt or blocking card.

A Receipt is receipt-backed candidate state. It does not mutate the Ledger until Verify and Commit accept it under the relevant Commit Scope.

Commit Scope is runtime policy for Ledger mutation. It is not a semantic primitive.

No next valid run is `paused_for_admission`: not executable and not terminal by default. Recovery is admission, not execution: if opened for admission, make a bounded HumanDecision / ObligationAdmission move for at most one next bounded Obligation; otherwise return `NEXT_CHAT_NEEDED` with an exact recovery prompt. Candidate routes and proposed Obligations remain candidate until Receipt -> Verify -> Commit.

## Atomic Run And Scope Discipline

Only one active target Obligation may be worked materially at a time.

Broad, messy, anxious, speculative, or phase-jumping human input must be scope-triaged before material work.

Use only `in_scope_used` and necessary dependencies for the current target Obligation.

Park useful off-scope input as residual context or proposed residual Obligations.

Candidate structure cannot bypass Atomic Run / Single Responsibility. `one_obligation_scope` fails if material output performs research, strategy, roadmap, execution, or structure creation not required by the target Obligation.

Operator Independence means user examples are candidate_context by default, urgency is not execution readiness, anxiety or brainstorming does not authorize phase jumping, and platform/channel/tool mentions are not commitments without Receipt, Verify, and Commit.

## Single Material Run Chat Boundary

Ordinary Direction chats default to one material Operator run plus Codex verification/closure.

Atomicity governs both the active target Obligation and the chat episode boundary.

Codex results return to the same chat to verify/close the current run or repair failed validation for the same handoff. After commit verification, a different next material Obligation requires `NEXT_CHAT_NEEDED` by default with an exact launch prompt unless the current chat was opened for that same target.

Same Direction / same product / same game is not sufficient reason for same-chat continuation.

## Truth And Projection

Documents, dashboards, maps, roadmaps, and projections do not create truth.

When a Dashboard shows empty `next_valid_runs`, any recovery guidance must be `projection_only: true` and `creates_truth: false`; it may identify candidates but cannot admit Obligations or strategy.

A Strategic Path Map is valid only as a projection from accepted Receipts and open Obligations.

A roadmap item without an Obligation is invalid.

Business-facing summaries must not claim more than accepted Receipts prove.

## Legacy And Migration

Old workflow files and old Direction files may become accepted state only through Legacy Import Receipt, Verify, and Commit.

Legacy data may be inspected as evidence when an admitted Obligation asks for that. Inspection alone does not import or accept the data.

## Execution Boundary

No Codex/product execution may begin without an execution-ready Obligation and required precondition Receipts.

Execution remains governed by the same kernel path:

```text
Obligation -> Operator -> Receipt -> Verify -> Commit
```

No validation means no done claim for execution work.

## Project Refresh Boundary

Repository maintenance handoffs must report separated project refresh requirements when changed files affect ChatGPT Projects.

If Project Instructions UI sources change, handoffs must report measured payload character counts and must not list instruction sources as uploaded Project Files/Sources.

END_OF_FILE: workflow/project_packs/WORKFLOW_BASE_PACK.md
