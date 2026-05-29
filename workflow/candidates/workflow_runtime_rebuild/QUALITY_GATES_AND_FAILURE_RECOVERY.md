# Quality Gates and Failure Recovery

status: candidate_draft

## Purpose

This file defines simple quality gates and failure recovery rules for Workflow Runtime Rebuild Stage 3.

The goal is to block false done, unsafe transitions and hidden state changes without creating an enterprise governance system.

Quality Gate means:
  a check that must pass before a result can be treated as safe for the next step.

Failure Recovery means:
  what to return when the gate fails.

A failed gate does not mean the whole project failed. It means the current run must block, repair, request a human decision or drop/supersede a stale candidate.

## Core rule

No hidden state change.

No validation means no done claim.

No accepted-state mutation from chat output, Codex output, Project Files, Signal, Handler result, Action Inbox item, Check Job result or document existence alone.

If acceptance is unclear, the safe result is blocked or needs human decision.

## Quality gate categories

### context/source gate

Checks:

- source authority is identified;
- required repository/path/ref is known;
- GitHub/canonical read is complete when exact state matters;
- Project Files are classified as cache/context;
- missing or stale source is visible;
- read limitations are stated.

Blocks when:

- required source is missing;
- source read is truncated or tail-unverified;
- stale Project Files are treated as truth;
- repository state is guessed.

Recovery:

- blocked Result Packet;
- repair Next Move to retrieve exact source;
- Check Job for source verification.

### scope gate

Checks:

- one bounded target;
- in-scope and out-of-scope boundaries;
- no unrelated continuation;
- no phase jump;
- no mixing of independent jobs;
- no "fix everything" package.

Blocks when:

- work becomes compound without triage;
- material chat starts unrelated work;
- Codex package has unclear allowed/forbidden paths.

Recovery:

- split required;
- park residual Action Inbox items;
- rewrite Launch Packet;
- human decision request if scope choice is unclear.

### evidence gate

Checks:

- expected evidence is defined;
- result includes evidence or explicit no-evidence reason;
- validation outputs are present when required;
- evidence matches the Work Contract;
- conflicting evidence is named.

Blocks when:

- result claims done without evidence;
- validation is absent;
- evidence does not support the claim.

Recovery:

- Check Job;
- blocked Result Packet;
- same-package repair;
- reject result as not verifiable.

### acceptance gate

Checks:

- result is marked candidate unless accepted through explicit path;
- Acceptance Decision is explicit;
- unclear acceptance is not inferred;
- user confirmation is recorded when needed.

Blocks when:

- chat treats its own output as accepted;
- Codex output is treated as accepted;
- human action is assumed complete without confirmation.

Recovery:

- parent/integration review;
- human decision request;
- acceptance/update path;
- return result for rework.

### Codex validation gate

Checks:

- branch name;
- commit SHA when committed;
- changed files;
- allowed paths;
- forbidden paths unchanged;
- validation results;
- EOF markers for markdown;
- residual risks;
- project refresh requirements.

Blocks when:

- Codex changed forbidden paths;
- validation failed;
- changed files are missing or unverifiable;
- markdown EOF markers are missing;
- Codex returns only "done."

Recovery:

- Codex repair package for same scope;
- rejected_scope_violation;
- rejected_validation_failed;
- blocked_missing_codex_evidence.

### child return gate

Checks:

- child chat had Launch Packet;
- child result returns to parent;
- child did not decide parent acceptance;
- parent verifies whether child answered target;
- missing child returns are visible.

Blocks when:

- child result is missing;
- child expanded scope;
- child made parent-level decision.

Recovery:

- Parent Recovery Block;
- request missing child result;
- rerun child with narrower Launch Packet;
- mark child result unusable.

### Action Inbox hygiene gate

Checks:

- each item has reason;
- relation is known;
- priority is set;
- when_to_run or stale_condition exists;
- duplicates are merged;
- stale items are dropped or superseded;
- handler flood is detected.

Blocks when:

- Action Inbox becomes trash bin;
- too many Handler candidates are created;
- items have no run condition.

Recovery:

- inbox hygiene pass;
- merge duplicates;
- drop stale items;
- restrict handler;
- convert only selected item into Check Job or Launch Packet.

### no hidden state change gate

Checks:

- Signal remains fact;
- Handler remains candidate generator;
- Action Inbox remains candidate queue;
- Console remains read-only;
- adapter output remains candidate;
- Memory requires promotion.

Blocks when:

- any layer silently mutates accepted state;
- Handler executes work;
- Console accepts result;
- Action Inbox auto-runs.

Recovery:

- rollback/reject candidate step;
- blocked Result Packet;
- explicit acceptance review;
- repair docs or packet.

### minimal context gate

Checks:

- current chat has enough context to do the bounded work;
- supplied context is classified;
- missing context is requested precisely;
- broad context loading is avoided when not needed.

Blocks when:

- chat proceeds from vague memory;
- it asks user for unnecessary large context;
- it cannot identify target, scope or source authority.

Recovery:

- exact Context Request as blocked Result Packet;
- ask for specific path/ref/excerpt;
- narrow Launch Packet;
- stop material work.

## Failure cases and recovery

### GitHub unavailable

Problem:
  Exact repository state cannot be verified.

Recovery output:
  blocked Result Packet with source_read limitation.
  Next Move: provide verified excerpts, restore GitHub access or run Codex read-only source check.

Do not:
  guess repository state.

### Project Files stale

Problem:
  Uploaded context may not match canonical source.

Recovery output:
  source_signal plus candidate Check Job.
  Next Move: verify exact GitHub file before material work.

Do not:
  treat Project Files as source of truth.

### missing source

Problem:
  Required file/path/ref is absent or unreadable.

Recovery output:
  blocked Result Packet with exact missing path/ref.
  Next Move: retrieve source or revise scope.

### work chat off-scope

Problem:
  Chat begins work outside Launch Packet.

Recovery output:
  scope_signal and scope repair.
  Next Move: return to Work Contract or create split/park residual item.

### child chat did not return

Problem:
  Parent cannot synthesize because child result is missing.

Recovery output:
  Parent Recovery Block.
  Next Move: paste missing child result, rerun child or narrow parent target.

### parent chat lost/too long

Problem:
  Parent context cannot safely continue.

Recovery output:
  Parent Recovery Block if available; otherwise blocked Result Packet.
  Next Move: open new parent/integration chat with recovery block and known returned results.

### Codex validation failed

Problem:
  Codex returned failed checks.

Recovery output:
  rejected_validation_failed or needs_codex_repair_same_package.
  Next Move: send repair package with same allowed paths or reject result.

### Codex changed forbidden paths

Problem:
  Codex breached path boundary.

Recovery output:
  rejected_scope_violation.
  Next Move: inspect diff, revert forbidden changes, rerun with stricter package if still needed.

### handler creates too many candidates

Problem:
  Handler flood makes Action Inbox unusable.

Recovery output:
  inbox_signal and hygiene pass.
  Next Move: merge/drop/supersede items, tighten Handler condition.

### Action Inbox grows stale

Problem:
  Old candidates no longer relate to Active Front or accepted decisions.

Recovery output:
  Action Inbox hygiene gate result.
  Next Move: drop, supersede or refresh items.

### conflicting evidence

Problem:
  Two sources/results disagree.

Recovery output:
  evidence_signal and Check Job.
  Next Move: verify source authority and decide which evidence is usable.

### acceptance unclear

Problem:
  Result exists but no explicit Acceptance Decision exists.

Recovery output:
  acceptance_signal.
  Next Move: parent/integration review or human decision request.

## Required recovery outputs

Use the smallest sufficient recovery output.

### blocked Result Packet

Use when work cannot safely continue.

Must include:

- status;
- blocker;
- missing_context or failed_gate;
- what was not done;
- source/read limitations;
- exact Next Move.

### repair Next Move

Use when the same package can be repaired.

Must include:

- failed gate;
- repair target;
- allowed paths or scope;
- forbidden changes;
- validation needed;
- return destination.

### human decision request

Use when the next safe step depends on user judgment.

Must include:

- decision needed;
- options;
- tradeoff;
- recommended default if any;
- consequence of not deciding.

### parent recovery block

Use when parent/child coordination can be lost.

Must include:

- parent target;
- children launched;
- results returned;
- missing returns;
- current synthesis state;
- resume instruction.

### Codex repair package

Use when Codex can repair within the same bounded scope.

Must include:

- same repository and branch context;
- exact failed validation;
- allowed paths;
- forbidden paths;
- repair goal;
- validation commands;
- requested return fields.

### drop/supersede stale item

Use when an Action Inbox item is no longer useful.

Must include:

- item;
- reason for drop or supersede;
- replacement item if any;
- evidence or accepted decision that made it stale.

## Keeping this simple

Do not create a full Event System.

Do not require YAML from the user.

Do not turn every warning into a blocker.

Use hard blocking only when proceeding would create false done, unsafe transition, hidden acceptance, source confusion or scope violation.

Use watch/candidate items for ordinary risks.

Use Check Job when evidence is needed.

Use human decision request when judgment is needed.

Use Codex repair only when repository work is bounded and verifiable.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/QUALITY_GATES_AND_FAILURE_RECOVERY.md
