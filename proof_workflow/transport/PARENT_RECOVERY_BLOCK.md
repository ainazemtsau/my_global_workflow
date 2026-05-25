---
artifact_control:
  namespace: proof_workflow
  artifact_type: transport_card
  card_type: parent_recovery_block
  status: gate_4_0_initial
  owner: proof_carrying_workflow_os
---

# Parent Recovery Block

## Purpose

Parent Recovery Block preserves enough parent state for recovery if the parent chat is lost.

It is a human-usable transport adapter, not semantic authority.

## Required Shape

```yaml
parent_recovery_block:
  recovery_block_id: string
  parent_obligation_id: string
  parent_goal_plain: string
  child_requests:
    - child_request_id: string
      child_obligation_id: string
      required: true | false
      status: not_started | running | returned | blocked
  received_child_results: [string]
  missing_required_results: [string]
  synthesis_rules: [string]
  conflict_policy: string
  next_action_if_all_required_returned: string
  copy_paste_recovery_prompt: string
```

## Rules

- Recovery block must be human-usable.
- User can paste it into a new chat with child results.
- New parent chat can continue collection or synthesis.
- Recovery must not depend on old parent chat memory.
- Recovery block does not mutate Ledger.
- Recovery block does not close parent Obligation.

END_OF_FILE: proof_workflow/transport/PARENT_RECOVERY_BLOCK.md
