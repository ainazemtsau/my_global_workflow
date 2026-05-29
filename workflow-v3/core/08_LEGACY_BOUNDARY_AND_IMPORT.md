---
artifact_control:
  namespace: workflow_v3
  artifact_type: core_spec
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Legacy Boundary And Import

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Preservation Statement

This v3 scaffold does not archive, delete, move, rename, or supersede existing workflow data.

Existing data remains available for later import as evidence.

Current runtime and old data remain preserved in place. This scaffold creates no current Direction state and does not mutate existing `directions/**`.

## Authority Boundary

- Legacy/current artifacts are evidence, not v3 authority.
- Existing workflow files remain governed by their current rules.
- V3 candidate files cannot reinterpret old proof state.
- V3 candidate files cannot create accepted receipts, ledgers, or obligations for current workflow.

## Future Import Process Required

Any reuse of old or current data requires a future import/review process with:

- Source path.
- Intended v3 destination.
- Classification.
- Evidence value.
- Authority status.
- Reviewer or parent acceptance.
- Memory promotion decision.
- Reopen or rollback condition.

## Import Classification

```yaml
import_classification:
  source_path:
  source_kind:
  candidate_use:
  evidence_value:
  authority_status: evidence_only
  proposed_destination:
  required_review:
  accepted_by:
  promotion_target:
  reopen_condition:
```

Classification options:

- evidence_only
- historical_context
- reusable_decision_candidate
- reusable_memory_candidate
- obsolete_or_superseded_context
- do_not_import

## Selective Migration Only

- Import only what is useful for the v3 direction or pilot.
- Do not bulk promote old documents.
- Do not infer accepted v3 state from old names, folders, or ledgers.
- Do not treat old Direction state as current v3 state.
- Preserve legacy/current workflow data in place until a separate reviewed action says otherwise.

END_OF_FILE: workflow-v3/core/08_LEGACY_BOUNDARY_AND_IMPORT.md
