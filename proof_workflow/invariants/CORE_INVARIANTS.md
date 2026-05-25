---
artifact_control:
  namespace: proof_workflow
  artifact_type: core_invariants
  status: gate_1_initial
  owner: proof_carrying_workflow_os
---

# Core Invariants

## Hard Invariants

- No obligation -> no work.
- No receipt -> no progress.
- No verification -> no commit.
- No commit -> no accepted state.
- No accepted receipts -> no confident document claim.
- No projection claim without accepted Receipt.
- No roadmap item without Obligation.
- No Codex/product execution without execution-ready Obligation and required precondition Receipts.
- No old workflow semantic authority in new proof workflow.
- No old Direction Map as Strategic Path Map truth.
- No old Active Goal as active Obligation.
- No child run mutates Ledger directly.
- No process macro marks work complete.
- No launch without Run Admission.
- No high-impact action without Human Gate where required.
- No single chat for non-atomic compound Obligation unless it returns split_required.
- No loaded context becomes accepted state without Receipt + Verify + Commit.
- No candidate context may be promoted to root objective, constraint, Horizon, Active Frontier, roadmap, or execution precondition without explicit acceptance.
- No Human Decision option may silently embed an unaccepted candidate constraint.
- No Project File or projection overrides committed Ledger state.
- No structured-format requirement for human decisions when intent is clear.
- No needs_input verdict solely because the user omitted schema fields that can be safely defaulted or delegated.
- No silent default: every default applied from human input normalization must be recorded in the Receipt.
- No material run may end with technical Receipt/YAML only.
- No user is required to manually construct Codex commit instructions from a Receipt.
- No next-chat instruction may be only an Obligation ID without human-readable launch text.
- If a commit is recommended, a Codex handoff must be provided or explicitly deferred with reason.
- No child run mutates Ledger.
- No child run closes parent Obligation.
- No child run makes parent-level final decision.
- No parent synthesis with missing required child results.
- No lost parent dependency when child runs are launched; provide Parent Recovery Block.
- No child launch without copy-paste prompt and return instructions.
- No Codex commit handoff may require an external wrapper.
- No commit-ready handoff without repository, worktree, branch, mode, allowed paths, forbidden paths, commit behavior, and push behavior.
- No user is required to infer Codex run boundaries from a Receipt.
- No partial Codex handoff may be labeled copy-paste runnable.
- No Codex repository maintenance card may omit Project Files refresh requirements when cached files are changed.
- No execution-ready receipt -> no CodexRun.
- No validation receipt -> no done.
- No direct implementation for mission-scale complex technical work.

## Enforcement

Invariant checks run during Verify and Commit.

Hard invariant failure blocks commit.

Invariant uncertainty must produce a residual Obligation, Context Request Card, or Human Decision Card.

Execution-specific invariants are listed in `proof_workflow/invariants/EXECUTION_INVARIANTS.md`.

## Legacy Term Handling

Legacy terms such as `Direction Map`, `Active Goal`, and similar old workflow labels may appear only as demoted evidence, compatibility notes, or explicit non-authority examples.

They must not define accepted state in the new proof workflow.

END_OF_FILE: proof_workflow/invariants/CORE_INVARIANTS.md
