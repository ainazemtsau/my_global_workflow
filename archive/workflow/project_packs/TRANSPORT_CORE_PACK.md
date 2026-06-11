---
artifact_control:
  namespace: workflow_project_packs
  artifact_type: project_pack
  pack_name: TRANSPORT_CORE_PACK
  pack_type: runtime_cache_upload_convenience
  intended_load_mode: default_all_directions
  status: path_boundary_consistency_refreshed
  owner: workflow_os
  generated_from_ref: wg/codex-handoff-path-boundary-consistency-2026-05-28
  refreshed_for_receipt: null
  do_not_use_as_authority: true
  refresh_rule: "Regenerate and refresh this pack if any source_manifest file changes."
source_manifest:
  - workflow/policies/04_TRANSPORT_PROTOCOL.md
  - workflow/transport/OPERATOR_LAUNCH_CARD.md
  - workflow/transport/RECEIPT_CARD.md
  - workflow/transport/CONTEXT_REQUEST_CARD.md
  - workflow/transport/HUMAN_DECISION_CARD.md
  - workflow/transport/COMMIT_PACKET.md
  - workflow/transport/LEGACY_IMPORT_RECEIPT_CARD.md
  - workflow/transport/CODEX_COMMIT_HANDOFF_CARD.md
  - workflow/transport/CHILD_OBLIGATION_REQUEST_CARD.md
  - workflow/transport/CHILD_RESULT_RETURN_CARD.md
  - workflow/transport/PARENT_RECOVERY_BLOCK.md
---

# Transport Core Pack

## Cache Boundary

This pack is a ChatGPT Project Files/Sources runtime cache / upload convenience artifact.

It is not semantic authority.

Canonical source files listed in `source_manifest` remain authority.

If this pack conflicts with a verified canonical source file, the canonical source wins.

If any `source_manifest` file changes, regenerate and refresh this pack before using it as Project Files/Sources cache.

If an exact card schema is material to a run, request or load the canonical source card file from `source_manifest`.

## Core Transport

Transport cards serialize workflow movement. They do not create truth by themselves.

Technical cards are appendix/transport. They are not the primary user interface.

Human-readable result and terminal outcome should come first. Cards should follow when needed.

## Card Summary

Launch Card serializes one Operator invocation over one Obligation.

Receipt Card records a receipt-backed result, including claims, evidence, assumptions, context authority audit, scope audit, chat episode continuity, residual Obligations, invariant checks, verification policy result, and commit recommendation.

Receipt `scope_audit` names the target Obligation, in-scope input used, necessary dependencies, parked residual context, proposed residual Obligations, blocked/forbidden work, explicit decisions, candidate examples, child handoff need/reason, hidden acceptance check, and `one_obligation_scope`.

Receipt `parent_chat_continuity` records the chat episode target, material run count, whether a Codex result is verification-only, and whether the next material target requires a new chat and prompt.

Context Request Card asks for the smallest blocking context needed to continue safely.

Human Decision Card records a human-owned decision and its options, risks, defaults, and selected result.

Commit Packet proposes a candidate state transition for Verify and Commit. It is not accepted state until committed.

Legacy Import Receipt Card records evidence needed to import old data without treating legacy files as current truth.

Codex Commit Handoff Card is a self-contained repository maintenance instruction. It must include repository, worktree, branch, mode, branch policy, worktree policy, main update policy, allowed paths, forbidden paths, protected paths, path-boundary consistency, validation, commit behavior, push behavior, and separated project refresh requirements when ChatGPT Project surfaces are affected.

Codex Commit Handoff path boundaries are invalid if any allowed path is covered by forbidden or protected globs. `allowed_paths` is the changed-files whitelist; changed files must validate as an exact subset of it. Do not protect sibling Direction workflow files with an overlapping forbidden glob such as `directions/*/workflow/**` when the active Direction workflow path is allowed; use non-overlapping protected/not-to-touch paths plus exact changed-files validation.

`review_branch_required` is the default and fallback branch policy. `direct_to_main_allowed` may be used only for eligible simple single-Direction proof-state commits with exact non-overlapping path boundaries, full validation, clean rebase onto `origin/main`, post-rebase validation, `HEAD` push to `origin/main`, and remote SHA verification. Workflow core, docs/setup, Project setup, risky, migration, multi-Direction, product, execution-package, legacy-import, conflict, or unverifiable changed-path cases require review branch behavior.

Direct-to-main must stay in the existing Direction worktree. It must not switch to local `main`, use a global main worktree, bypass validation, or ask for a second human merge command after success.

Legacy merge fields do not authorize direct-to-main by themselves; the fast path requires `branch_policy: direct_to_main_allowed` and a matching main update policy.

Project refresh requirements must distinguish:

- `project_instruction_ui_update_required` for ChatGPT Project Instructions UI updates.
- `project_sources_files_refresh_required` for uploaded Project Files/Sources.
- `request_only_sources_refresh_required` for request-only packs or exact sources.
- `do_not_upload_as_project_file` for instruction source files such as `project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`.

When Project Instructions sources change, Codex handoff return fields must include `project_instruction_ui_payload_char_counts`.

Child Obligation Request Card, Child Result Return Card, and Parent Recovery Block support recursive child handoff. Child chats are launched only when needed for the current target Obligation, return results to the parent, and do not mutate parent Ledger state or make parent-level final decisions. Child chats do not replace the next-chat boundary after a completed material run.

## Exact Schema Fallback

Pack summaries are not a substitute for exact schemas.

When schema keys, required fields, or validation of a card are material, load the canonical card file from `source_manifest`.

END_OF_FILE: workflow/project_packs/TRANSPORT_CORE_PACK.md
