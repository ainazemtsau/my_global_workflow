---
artifact_control:
  namespace: workflow
  artifact_type: migration_protocol
  status: gate_1_initial
  owner: workflow_os
---

# Migration Protocol

## Clean-Room Migration Rule

Old workflow files are legacy evidence only.

Old semantics are not authority in the new workflow.

No old stage/layer/phase/goal/process concept may become accepted state by being copied, renamed, or default-loaded.

Legacy material becomes new workflow fact only through a Legacy Import Receipt that passes verification and commit.

## Legacy Import Receipt Requirement

Every imported claim must record:

- source path
- imported claim
- claim role
- evidence kind
- whether the claim is accepted for the new Ledger
- whether user confirmation is required
- rejected or legacy-only reason when not accepted
- contamination check
- proposed Ledger delta

## Specific Demotions

Old Direction Map is not accepted Strategic Path Map.

Old Active Goal is not active Obligation.

Old Current Phase is not Ledger state.

Old Portfolio Queue is not obligation backlog.

Old stage prompts are not Operators.

Old transport packets are not canonical new transport.

Old project files are not workflow source of truth.

## Receipt-Backed Migration

Migration itself must be receipt-backed.

Each migration action requires:

- admitted Obligation
- selected Operator
- produced Receipt
- evidence references
- contamination check
- Verify result
- Commit result

## Migration Gates

Gate 0: read-only inventory.

Gate 1: shared kernel namespace install.

Gate 2: pilot direction proof skeleton.

Gate 3: end-to-end dry run.

Gate 4: all active directions initialized.

Gate 5: project setup switch.

Gate 6: old workflow legacy/do-not-load.

This run implements only Gate 1.

## Non-Migration Boundary For Gate 1

Gate 1 must not:

- create `directions/<direction-id>/proof/`
- import real Direction facts
- edit old workflow files
- edit old project setup files
- produce migration receipts for real Directions

END_OF_FILE: workflow/policies/07_MIGRATION_PROTOCOL.md
