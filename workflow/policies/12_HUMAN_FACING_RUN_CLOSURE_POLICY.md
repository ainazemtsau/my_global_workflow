---
artifact_control:
  namespace: workflow
  artifact_type: human_facing_run_closure_policy
  status: project_instruction_budget_hardened
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

After Codex returns, same-parent continuation is the default. The user should bring the Codex result back to the parent chat unless a next-chat criterion below is met.

When changed files affect ChatGPT Projects, the handoff must separate Project Instructions UI updates from Project Files/Sources refreshes.

When changed Project Instructions sources require UI updates, the handoff must report measured UI payload character counts.

### NEXT_CHAT_NEEDED

A new ChatGPT operator run is needed.

The response must provide an exact copy-paste prompt for the new chat.

`NEXT_CHAT_NEEDED` is exceptional, not default.

Use it only when context loss, explicit human request, unsafe scope change, model/tool limits, or a required split makes same-parent continuation unsafe or invalid.

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
- Human-readable result comes first.
- Do not burden the user with YAML unless it is needed for Receipt, Codex handoff, or exact transport.
- Receipt Cards are required for candidate or commit-worthy state, but ordinary clarifications can be plain language.
- If a Receipt needs persistence, the operator chat must output a complete and self-contained Codex Commit Handoff Card.
- Do not ask the user to open a new chat unless next-chat criteria are met.
- If next ChatGPT run is needed, output a human-readable copy-paste prompt, not only an Obligation ID.
- Obligation IDs may be shown, but must not be the only instruction.
- User-facing text should avoid workflow jargon unless needed.
- Internal IDs belong in technical appendix.

## Same Parent Chat Default

One bounded user problem should stay in one parent chat until terminal outcome when safe.

A parent chat may continue across multiple turns, Codex handoffs, Codex results, and child results while solving the same bounded problem.

Sequential internal steps are allowed only when they remain necessary to close the same bounded problem and each active target Obligation is declared.

The parent chat must not switch to unrelated work merely because it can continue.

`CODEX_COMMIT_NEEDED` is a repository persistence step, not a command to abandon the parent chat. The user returns the Codex result to the parent chat for synthesis, closure, or the next declared target Obligation in the same bounded problem.

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
- explicit `branch_policy`, where missing or ambiguous means `review_branch_required`
- worktree policy and main update policy when a direct-to-main path is allowed
- explicit no-main-merge setting
- separated project refresh requirements:
  - `project_instruction_ui_update_required`
  - `project_sources_files_refresh_required`
  - `request_only_sources_refresh_required`
  - `do_not_upload_as_project_file`
- `project_instruction_ui_payload_char_counts` when Project Instructions sources changed

The user should be able to paste one block into Codex without reconstructing the task from a Receipt or adding an external wrapper.

The response must not output only a Receipt plus a partial handoff.

The response must not say "send this to Codex" unless the pasted block is runnable as-is.

## Codex Direct-To-Main Closure Rule

Eligible simple single-Direction proof-state Codex handoffs should not require a second human "merge to main" turn after validation has already passed.

A handoff may set `branch_policy: direct_to_main_allowed` only when the commit is a simple single-Direction proof-state commit with exact allowed and forbidden paths and no workflow core, docs/setup, Project setup, migration, product implementation, execution package, legacy import, or multi-Direction changes.

Direct-to-main must not bypass validation. Codex must validate, commit, cleanly rebase onto `origin/main`, re-run validation, push `HEAD` directly to `origin/main`, and verify the remote `origin/main` SHA equals local `HEAD`.

Successful direct-to-main returns `DONE` with `origin_main_sha_after_push`, `local_head_sha`, `push_target`, `rebase_result`, `direct_to_main_eligibility_result`, and `whether_user_merge_turn_required: false`.

Failed direct-to-main returns `NEEDS_INPUT` with the exact blocker, such as validation failure, conflicted files, forbidden or unexpected paths, unsafe dirty tracked state, or push race that cannot be resolved after one retry. It must not end with a vague request to merge manually.

Workflow core/setup/risky changes and missing or ambiguous branch policy must use `review_branch_required`.

## Project Surface Refresh Rule

Project Instructions UI and Project Files/Sources are separate ChatGPT surfaces.

Codex handoffs and run closures must use `project_instruction_ui_update_required` when a repository instruction source changes and the user needs to paste updated text into the ChatGPT Project Instructions field.

Codex handoffs and run closures must use `project_sources_files_refresh_required` only for uploaded Project Files/Sources such as shared packs and Direction payload files.

Codex handoffs and run closures must use `request_only_sources_refresh_required` for request-only packs or exact sources that should be refreshed only if already uploaded or explicitly needed.

Codex handoffs and run closures must use `do_not_upload_as_project_file` for repository Project Instruction Source files such as `project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`.

Do not group Project Instructions UI updates under uploaded Project Files/Sources refresh, do not list `project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md` under Project Files/Sources refresh, and do not make default upload counts include Project Instructions.

When Project Instructions source files change, run closures must report the extracted UI payload character count for each changed source and state whether each is under the 8,000-character hard max, over the 7,200-character warning threshold, or at/below the 6,500-character target.

If the operator cannot produce a self-contained Codex handoff, it must clearly state the missing fields and return `BLOCKED_CONTEXT_NEEDED` or `CODEX_HANDOFF_BLOCKED`.

## Next Chat Rule

When terminal outcome is `NEXT_CHAT_NEEDED`, the response must include a plain-language prompt that can be pasted into a new ChatGPT chat.

The prompt may include Obligation IDs, but must also describe the work in normal language.

The response must state why same-parent continuation is unsafe or invalid.

END_OF_FILE: workflow/policies/12_HUMAN_FACING_RUN_CLOSURE_POLICY.md
