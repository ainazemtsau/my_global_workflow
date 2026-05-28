---
artifact_control:
  namespace: workflow_project_packs
  artifact_type: project_pack
  pack_name: UNIVERSAL_PROJECT_SHELL_PACK
  pack_type: runtime_cache_upload_convenience
  intended_load_mode: default_all_directions
  status: no_next_valid_run_recovery_refreshed
  owner: workflow_os
  generated_from_ref: wg/no-next-run-recovery-protocol-2026-05-28
  refreshed_for_receipt: null
  do_not_use_as_authority: true
  refresh_rule: "Regenerate and refresh this pack if any source_manifest file changes."
source_manifest:
  - WORKFLOW_SOURCE_OF_TRUTH.md
  - README.md
  - AGENTS.md
  - workflow/README.md
  - docs/CHATGPT_PROJECT_SETUP.md
  - docs/CODEX_APP_SETUP.md
  - docs/NEW_DEVICE_BOOTSTRAP.md
  - workflow/policies/08_CHATGPT_PROJECT_SETUP.md
  - workflow/policies/09_STORAGE_LAYOUT_POLICY.md
  - workflow/policies/10_CONTEXT_AUTHORITY_POLICY.md
  - workflow/policies/11_HUMAN_INPUT_NORMALIZATION_POLICY.md
  - workflow/policies/12_HUMAN_FACING_RUN_CLOSURE_POLICY.md
  - workflow/policies/13_RECURSIVE_CHILD_HANDOFF_POLICY.md
---

# Universal Project Shell Pack

## Cache Boundary

This pack is a ChatGPT Project Files/Sources runtime cache / upload convenience artifact.

It is not semantic authority.

Canonical source files listed in `source_manifest` remain authority.

If this pack conflicts with a verified canonical source file, the canonical source wins.

If any `source_manifest` file changes, regenerate and refresh this pack before using it as Project Files/Sources cache.

## Project Source Of Truth

GitHub repository `ainazemtsau/my_global_workflow`, branch `main`, is the exact repository source while `WORKFLOW_SOURCE_OF_TRUTH.md` says `active`.

`WORKFLOW_SOURCE_OF_TRUTH.md` is a bootstrap authority locator, not semantic authority.

Verified canonical files under `workflow/**`, Direction metadata, and Direction Project Files manifests govern setup.

ChatGPT Project Files/Sources and project packs are runtime cache. They do not create accepted state.

Project Instructions UI is the ChatGPT Project settings field where behavior instructions are pasted.

Project Files/Sources are uploaded reference materials.

Repository files named `CHATGPT_PROJECT_INSTRUCTIONS.md` are Project Instructions UI payload sources. They are not default Project Files/Sources and must not be included in default upload counts.

Project Instructions UI payloads must be compact behavior instructions: hard max 8,000 characters, target 6,500, warn above 7,200. Count only trimmed content between the BEGIN/END UI payload markers.

For ordinary Direction Workflow Projects, active Direction payload files are:

```text
LEDGER.md
OBLIGATIONS.md
RECEIPTS_INDEX.md
COMMIT_SCOPES.md
DASHBOARD.md
MIGRATION_RECEIPT.md
```

These files are uploaded from the Direction active payload directory declared by `direction.meta.yml` and/or the Direction `PROJECT_FILES_MANIFEST.md`. Do not hard-code `directions/<direction-id>/proof/`, `directions/<direction-id>/project_setup/`, or Direction root payload paths.

For new ordinary Direction Workflow Projects, the preferred setup location is:

```text
directions/<direction-id>/workflow/project_setup/
```

Existing Directions may have a different declared active setup directory. Read it from exact `direction.meta.yml` and the exact Project Files manifest.

Only verified Receipts committed to the Direction Ledger create accepted Direction state.

## Default Load Boundary

Default setup is:

1. Paste or update Project Instructions in the ChatGPT Project Instructions UI.
2. Upload Project Files/Sources: default shared packs plus Direction payload files.

New Workflow Projects should not load old vNext-R workflow files, old stage files, old transport files, or old Direction `project_files/00-08` by default.

Old Direction data is legacy evidence only until imported through:

```text
Legacy Import Receipt -> Verify -> Commit
```

Old Direction Map, Active Goal, Current Phase, Portfolio Queue, project setup files, phases, and execution logs are not accepted state by being present in the repository.

## Context Authority

Loaded context is not accepted state.

Every material use of loaded context must classify it as accepted Ledger state, committed Receipt, current human input, candidate context, projection context, legacy evidence, instruction context, or unknown.

Candidate context may support questions, options, assumptions, or candidate Obligations. It must not become root objective, constraint, Horizon, Active Frontier, roadmap, execution precondition, or accepted claim without explicit human decision or committed Receipt.

If Dashboard/Obligations show no next valid run, no open next obligation, or empty `next_valid_runs`, the ordinary Direction state is `paused_for_admission`, not executable. Candidate routes remain candidate, and proposed Obligations remain candidate, until Receipt -> Verify -> Commit.

Broad, messy, anxious, speculative, or phase-jumping user input must be scope-triaged before material work into `in_scope_used`, `necessary_dependencies`, `parked_residual_context`, `proposed_residual_obligations`, `blocked_or_forbidden`, `explicit_decisions`, and `candidate_examples`.

Only the current target Obligation, accepted state, explicit current decisions, and necessary dependencies may drive material output.

User examples are candidate_context by default. User urgency, anxiety, and brainstorming do not authorize phase jumps. Platform, channel, or tool mentions are not commitments without Receipt, Verify, and Commit.

## Human Input

Human users do not need to reply in YAML, schemas, or formal card syntax.

Terse or spoken human answers may be normalized when intent is clear. Normalization must be recorded and must not create hidden acceptance.

Useful off-scope concerns should be preserved as parked residual context or proposed residual Obligations without acting on them prematurely.

The operator optimizes for workflow validity, evidence quality, and project effectiveness, not immediate agreement.

## Run Closure

Every material response must end with a clear terminal outcome for the user.

Return the human-readable result first. Technical cards belong after the explanation.

No-next-run recovery returns `HUMAN_DECISION_NEEDED` only when the chat was opened for admission; otherwise return `NEXT_CHAT_NEEDED` with an exact recovery prompt. It must not trigger execution.

If a Codex commit is needed, provide a fully self-contained Codex Commit Handoff Card with repository, worktree, branch, mode, `branch_policy`, allowed paths, forbidden paths, validation, commit behavior, push behavior, and separated project refresh requirements.

Missing or unclear `branch_policy` means `review_branch_required`. Use `direct_to_main_allowed` only for eligible simple single-Direction proof-state commits. Workflow core/setup, docs/setup, Project setup, migration, multi-Direction, product/execution work, risky changes, conflicts, or uncertain validation require review branch behavior.

Direct-to-main must keep Codex in the existing Direction worktree, must not switch to local `main` or use a global main worktree, and must verify `origin/main` SHA after pushing `HEAD:main`.

Refresh requirements must use `project_instruction_ui_update_required`, `project_sources_files_refresh_required`, `request_only_sources_refresh_required`, and `do_not_upload_as_project_file`.

Do not list `directions/<direction-id>/<active-project-setup>/CHATGPT_PROJECT_INSTRUCTIONS.md` under Project Files/Sources refresh.

When Project Instructions sources change, report `project_instruction_ui_payload_char_counts`.

Single Material Run Chat Boundary is the default for ordinary Direction chats: one material Operator run plus Codex verification/closure.

Codex results return to the same chat only to verify/close the current run. After commit verification, the next material Obligation requires `NEXT_CHAT_NEEDED` by default with an exact launch prompt.

Same Direction / same product / same game is not sufficient reason for same-chat continuation. Same chat remains allowed for non-material explanation, failed validation repair for the same handoff, recovery prompts, and child result synthesis required for the current target.

If child chats are needed for the current target Obligation, provide copy-paste child prompts, state what results must return, and include a Parent Recovery Block when multiple children are launched.

Do not launch child chats for future topics, blocked phases, unrelated residual work, or mere thoroughness. Child results return to the parent chat for synthesis. Child chats are not a substitute for the next-chat boundary after a completed material run.

END_OF_FILE: workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md
