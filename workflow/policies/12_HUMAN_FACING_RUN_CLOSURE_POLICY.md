---
artifact_control:
  namespace: workflow
  artifact_type: human_facing_run_closure_policy
  status: gate_3_1_initial
  owner: workflow_os
---

# Human-Facing Run Closure Policy

## Purpose

Human-facing output is the primary UI.

Human-Facing Run Closure is a runtime policy, not a semantic primitive.

Technical cards and YAML are appendix / transport.

Every material Operator chat must end with one clear terminal outcome.

Human-facing clarity is part of workflow correctness.

## Terminal Outcomes

### HUMAN_DECISION_NEEDED

The user must choose or answer.

The response must provide options in normal language and acceptable short replies.

### CODEX_COMMIT_NEEDED

A Receipt or commit-worthy delta exists and must be saved by Codex.

The response must provide a fully self-contained Codex Commit Handoff Card.

The user should be able to copy one block into Codex without adding repository, worktree, branch, mode, path boundaries, commit behavior, push behavior, or no-main-merge instructions.

### NEXT_CHAT_NEEDED

A new ChatGPT operator run is needed.

The response must provide an exact copy-paste prompt for the new chat.

### COMPLETE_NO_COMMIT

The run is complete and no repository state change is needed.

### BLOCKED_CONTEXT_NEEDED

Missing context blocks safe progress.

The response must name the smallest blocking context.

### CODEX_HANDOFF_BLOCKED

Repository maintenance is needed, but the Operator cannot produce a self-contained Codex Commit Handoff Card because required run boundary fields are missing.

The response must name the missing fields and must not claim the handoff is copy-paste runnable.

### STOP_UNSAFE_OR_OUT_OF_SCOPE

Work must stop because it is unsafe, out of scope, forbidden, or invariant-breaking.

## Human-Facing Response Order

Every material response should use this order:

1. What happened.
2. What was accepted / selected / produced.
3. What was explicitly not accepted.
4. What remains open or blocked.
5. What the user should do next.
6. Copy-paste block if Codex or next chat is needed.
7. Technical appendix with Receipt/Card/YAML only after human explanation.

## Hard Rules

- Do not end a material run with Receipt/YAML only.
- Do not require the user to understand or manually construct YAML.
- Do not require the user to manually build a Codex task from a Receipt.
- If a Receipt needs persistence, the operator chat must output a complete and self-contained Codex Commit Handoff Card.
- If next ChatGPT run is needed, output a human-readable copy-paste prompt, not only an Obligation ID.
- Obligation IDs may be shown, but must not be the only instruction.
- User-facing text should avoid workflow jargon unless needed.
- Internal IDs belong in technical appendix.

## Codex Handoff Rule

When terminal outcome is `CODEX_COMMIT_NEEDED`, the response must include:

- concise human explanation
- fully self-contained Codex Commit Handoff Card
- repository
- worktree
- branch
- mode
- exact allowed paths
- exact forbidden paths
- protected paths and files not to touch
- files to create/update
- validation requirements
- commit message and commit requirement
- push expectation
- explicit no-main-merge setting
- Project Files refresh requirements

The user should be able to paste one block into Codex without reconstructing the task from a Receipt or adding an external wrapper.

The response must not output only a Receipt plus a partial handoff.

The response must not say "send this to Codex" unless the pasted block is runnable as-is.

If the operator cannot produce a self-contained Codex handoff, it must clearly state the missing fields and return `BLOCKED_CONTEXT_NEEDED` or `CODEX_HANDOFF_BLOCKED`.

## Next Chat Rule

When terminal outcome is `NEXT_CHAT_NEEDED`, the response must include a plain-language prompt that can be pasted into a new ChatGPT chat.

The prompt may include Obligation IDs, but must also describe the work in normal language.

END_OF_FILE: workflow/policies/12_HUMAN_FACING_RUN_CLOSURE_POLICY.md
