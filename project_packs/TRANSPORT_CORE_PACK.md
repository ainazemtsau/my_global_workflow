---
artifact_control:
  namespace: workflow_project_packs
  artifact_type: project_pack
  pack_name: TRANSPORT_CORE_PACK
  pack_type: runtime_cache_upload_convenience
  intended_load_mode: default_all_directions
  status: u1_initial
  owner: workflow_os
  generated_from_ref: main@14bc73b11c609787e5919989a6e3fb6de2450c9e
  do_not_use_as_authority: true
  refresh_rule: "Regenerate and refresh this pack if any source_manifest file changes."
source_manifest:
  - 04_TRANSPORT_PROTOCOL.md
  - transport/OPERATOR_LAUNCH_CARD.md
  - transport/RECEIPT_CARD.md
  - transport/CONTEXT_REQUEST_CARD.md
  - transport/HUMAN_DECISION_CARD.md
  - transport/COMMIT_PACKET.md
  - transport/LEGACY_IMPORT_RECEIPT_CARD.md
  - transport/CODEX_COMMIT_HANDOFF_CARD.md
  - transport/CHILD_OBLIGATION_REQUEST_CARD.md
  - transport/CHILD_RESULT_RETURN_CARD.md
  - transport/PARENT_RECOVERY_BLOCK.md
---

# Transport Core Pack

## Cache Boundary

This pack is a ChatGPT Project Files runtime cache / upload convenience artifact.

It is not semantic authority.

Canonical source files listed in `source_manifest` remain authority.

If this pack conflicts with a verified canonical source file, the canonical source wins.

If any `source_manifest` file changes, regenerate and refresh this pack before using it as Project Files cache.

If an exact card schema is material to a run, request or load the canonical source card file from `source_manifest`.

## Core Transport

Transport cards serialize workflow movement. They do not create truth by themselves.

Technical cards are appendix/transport. They are not the primary user interface.

Human-readable result and terminal outcome should come first. Cards should follow when needed.

## Card Summary

Launch Card serializes one Operator invocation over one Obligation.

Receipt Card records a receipt-backed result, including claims, evidence, assumptions, residual Obligations, invariant checks, verification policy result, and commit recommendation.

Context Request Card asks for the smallest blocking context needed to continue safely.

Human Decision Card records a human-owned decision and its options, risks, defaults, and selected result.

Commit Packet proposes a candidate state transition for Verify and Commit. It is not accepted state until committed.

Legacy Import Receipt Card records evidence needed to import old data without treating legacy files as current truth.

Codex Commit Handoff Card is a self-contained repository maintenance instruction. It must include repository, worktree, branch, mode, allowed paths, forbidden paths, validation, commit behavior, push behavior, and Project Files refresh requirements.

Child Obligation Request Card, Child Result Return Card, and Parent Recovery Block support recursive child handoff. Child chats do not mutate parent Ledger state or make parent-level final decisions.

## Exact Schema Fallback

Pack summaries are not a substitute for exact schemas.

When schema keys, required fields, or validation of a card are material, load the canonical card file from `source_manifest`.

END_OF_FILE: project_packs/TRANSPORT_CORE_PACK.md
