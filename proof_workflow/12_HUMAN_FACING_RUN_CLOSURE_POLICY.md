---
artifact_control:
  namespace: proof_workflow
  artifact_type: human_facing_run_closure_policy
  status: gate_3_1_initial
  owner: proof_carrying_workflow_os
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

The response must provide a full Codex Commit Handoff Card.

### NEXT_CHAT_NEEDED

A new ChatGPT operator run is needed.

The response must provide an exact copy-paste prompt for the new chat.

### COMPLETE_NO_COMMIT

The run is complete and no repository state change is needed.

### BLOCKED_CONTEXT_NEEDED

Missing context blocks safe progress.

The response must name the smallest blocking context.

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
- If a Receipt needs persistence, the operator chat must output a complete Codex Commit Handoff Card.
- If next ChatGPT run is needed, output a human-readable copy-paste prompt, not only an Obligation ID.
- Obligation IDs may be shown, but must not be the only instruction.
- User-facing text should avoid workflow jargon unless needed.
- Internal IDs belong in technical appendix.

## Codex Handoff Rule

When terminal outcome is `CODEX_COMMIT_NEEDED`, the response must include:

- concise human explanation
- full Codex Commit Handoff Card
- exact allowed paths
- exact forbidden paths
- files to create/update
- validation requirements
- commit message
- push expectation
- Project Files refresh requirements

The user should be able to paste the handoff into Codex without reconstructing the task from a Receipt.

## Next Chat Rule

When terminal outcome is `NEXT_CHAT_NEEDED`, the response must include a plain-language prompt that can be pasted into a new ChatGPT chat.

The prompt may include Obligation IDs, but must also describe the work in normal language.

END_OF_FILE: proof_workflow/12_HUMAN_FACING_RUN_CLOSURE_POLICY.md
