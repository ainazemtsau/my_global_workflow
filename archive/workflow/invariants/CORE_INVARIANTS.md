---
artifact_control:
  namespace: workflow
  artifact_type: core_invariants
  status: single_material_run_chat_boundary_hardened
  owner: workflow_os
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
- No material work on more than one active target Obligation at a time.
- No broad, messy, anxious, speculative, or phase-jumping human input may be used for material work before Scope Triage.
- No off-scope user input may drive research, strategy, roadmap, execution, or structure creation not required by the target Obligation.
- No candidate structure may bypass Atomic Run / Single Responsibility.
- No `one_obligation_scope` pass when material output performs work outside the target Obligation and necessary dependencies.
- No old workflow semantic authority in new workflow.
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
- No user example becomes accepted state without explicit Receipt, Verify, and Commit.
- No user urgency, anxiety, or brainstorming creates execution readiness or authorizes phase jumping.
- No platform, channel, or tool mention becomes a commitment unless explicitly accepted through Receipt, Verify, and Commit.
- No structured-format requirement for human decisions when intent is clear.
- No needs_input verdict solely because the user omitted schema fields that can be safely defaulted or delegated.
- No silent default: every default applied from human input normalization must be recorded in the Receipt.
- No material run may end with technical Receipt/YAML only.
- No user is required to manually construct Codex commit instructions from a Receipt.
- No next-chat instruction may be only an Obligation ID without human-readable launch text.
- No `NEXT_CHAT_NEEDED` may be omitted when the next material target is a newly opened Obligation after commit verification.
- No ordinary Direction chat may start a newly opened material Obligation after verifying the commit for the previous material run.
- No same Direction / same product / same game may be used as sufficient reason for same-chat continuation.
- No LegacyImport / research / evidence extraction / execution readiness / CodexExecution / ProductExecution may start in a chat that was not opened for that target, unless it is a child run explicitly required for the current parent target and governed by child handoff rules.
- No roadmap / Horizon / Active Frontier / implementation work may start in a chat that was not opened for that target, unless it is a child run explicitly required for the current parent target and governed by child handoff rules.
- No user chat-boundary question may be bypassed by continuing workflow verification or next-run work.
- No parent chat switches to unrelated work merely because the chat can continue.
- If a commit is recommended, a Codex handoff must be provided or explicitly deferred with reason.
- No child run mutates Ledger.
- No child run closes parent Obligation.
- No child run makes parent-level final decision.
- No parent synthesis with missing required child results.
- No lost parent dependency when child runs are launched; provide Parent Recovery Block.
- No child launch without copy-paste prompt and return instructions.
- No child launch unless the child result is required for the current target Obligation.
- No child launch for future topics, blocked phases, or mere thoroughness.
- No Codex commit handoff may require an external wrapper.
- No commit-ready handoff without repository, worktree, branch, mode, allowed paths, forbidden paths, commit behavior, and push behavior.
- No user is required to infer Codex run boundaries from a Receipt.
- No partial Codex handoff may be labeled copy-paste runnable.
- No Codex repository maintenance card may omit separated project refresh fields when changed files affect ChatGPT Projects.
- No Codex repository maintenance card may omit Project Instructions UI payload character counts when Project Instructions UI sources change.
- No execution-ready receipt -> no CodexRun.
- No validation receipt -> no done.
- No direct implementation for mission-scale complex technical work.

## Enforcement

Invariant checks run during Verify and Commit.

Hard invariant failure blocks commit.

Invariant uncertainty must produce a residual Obligation, Context Request Card, or Human Decision Card.

Execution-specific invariants are listed in `workflow/invariants/EXECUTION_INVARIANTS.md`.

## Legacy Term Handling

Legacy terms such as `Direction Map`, `Active Goal`, and similar old workflow labels may appear only as demoted evidence, compatibility notes, or explicit non-authority examples.

They must not define accepted state in the new workflow.

END_OF_FILE: workflow/invariants/CORE_INVARIANTS.md
