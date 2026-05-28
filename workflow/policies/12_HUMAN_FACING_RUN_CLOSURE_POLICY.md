---
artifact_control:
  namespace: workflow
  artifact_type: human_facing_run_closure_policy
  status: single_material_run_chat_boundary_hardened
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

The user should be able to copy one block into Codex without adding repository, worktree, branch, mode, non-overlapping path boundaries, commit behavior, push behavior, or no-main-merge instructions.

After Codex returns, the Codex result returns to the same chat only for verification and closure of the current material run.

The same chat must not begin the next material Obligation after commit verification by default.

When changed files affect ChatGPT Projects, the handoff must separate Project Instructions UI updates from Project Files/Sources refreshes.

When changed Project Instructions sources require UI updates, the handoff must report measured UI payload character counts.

### NEXT_CHAT_NEEDED

A new ChatGPT operator run is needed.

The response must provide an exact copy-paste prompt for the new chat.

`NEXT_CHAT_NEEDED` is the default terminal outcome when the requested next material target differs from the current chat episode target, or when the current chat was not opened for that requested target.

Mandatory `NEXT_CHAT_NEEDED` triggers:

- next material target differs from the current chat episode target, including a newly opened Obligation after current run closure
- current chat was not opened for the requested LegacyImport target
- current chat was not opened for the requested research, evidence extraction, or import target
- current chat was not opened for the requested execution readiness target
- current chat was not opened for the requested CodexExecution or ProductExecution target
- current chat was not opened for the requested roadmap, Horizon, Active Frontier, or implementation target
- material chat-boundary or governance work would require a different target than the current chat episode
- context is long/noisy or the assistant missed a direct user question, and the requested material target cannot be confirmed as the current chat episode target

The same chat remains allowed for non-material explanation, verifying and closing the Codex result for the current handoff, failed validation repair for the same handoff, producing a recovery or next-chat prompt, and child-result synthesis required for the current parent target.

### COMPLETE_NO_COMMIT

The run is complete and no repository state change is needed.

### BLOCKED_CONTEXT_NEEDED

Missing context blocks safe progress.

The response must name the smallest blocking context.

### CODEX_HANDOFF_BLOCKED

Repository maintenance is needed, but the Operator cannot produce a self-contained Codex Commit Handoff Card because required run boundary fields are missing or exact non-overlapping path boundaries cannot be produced.

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
- Do not ask the user to open a new chat for non-material closure or same-handoff repair, but require it when next-chat criteria are met.
- If next ChatGPT run is needed, output a human-readable copy-paste prompt, not only an Obligation ID.
- Obligation IDs may be shown, but must not be the only instruction.
- User-facing text should avoid workflow jargon unless needed.
- Internal IDs belong in technical appendix.

## Single Material Run Chat Boundary

One chat handles one material Operator run plus Codex verification/closure.

Ordinary Direction chats default to one minimal bounded episode. Atomicity governs both the target Obligation and the chat episode boundary.

A Direction, product, game, long-term goal, Horizon, roadmap, or implementation stream is not itself a bounded chat problem.

`CODEX_COMMIT_NEEDED` is a repository persistence step. The user returns the Codex result to the same chat only to verify the commit result, repair failed validation for the same handoff, and close the current material run.

After commit verification, a different next material target must be launched in a new chat by default with `NEXT_CHAT_NEEDED` and an exact copy-paste prompt.

The same chat may still answer non-material questions, verify and close the current handoff, repair failed validation for the same handoff, provide recovery / next-chat prompts, or synthesize child results required for the current parent target.

## No Next Valid Run Closure

No-next-run recovery is an admission move, not execution. It uses `HUMAN_DECISION_NEEDED` or `NEXT_CHAT_NEEDED`.

If the chat was explicitly opened for a no-next-valid-run admission decision, return `HUMAN_DECISION_NEEDED` with bounded HumanDecision / ObligationAdmission options for admitting at most one next bounded Obligation.

If the current material run is closed, or the chat was not opened for no-next-run admission, return `NEXT_CHAT_NEEDED` with this exact copy-paste recovery prompt:

```text
Open the current Direction payload and handle no-next-valid-run recovery only. Treat the Direction as paused_for_admission, do not execute candidate routes, and make a bounded HumanDecision / ObligationAdmission decision for at most one next bounded Obligation. Candidate routes remain candidate until Receipt -> Verify -> Commit.
```

## Codex Handoff Rule

When terminal outcome is `CODEX_COMMIT_NEEDED`, the response must include:

- concise human explanation
- fully self-contained Codex Commit Handoff Card with non-overlapping path boundaries
- repository
- worktree
- branch
- mode
- exact allowed paths
- exact forbidden paths
- protected paths and files not to touch
- validation that no allowed path is matched by forbidden/protected path boundaries
- validation that changed files are an exact subset of allowed paths
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

### Path Boundary Consistency Rule

`fully self-contained` includes exact, non-overlapping path boundaries.

No file may be both allowed and forbidden. `allowed_paths` is the positive whitelist for changed files, and changed files must be validated as an exact subset of `allowed_paths`.

Codex handoffs must not protect sibling Directions with an overlapping blanket forbidden glob such as `directions/*/workflow/**` when `allowed_paths` includes `directions/<direction-id>/workflow/**`. Use non-overlapping `protected_paths` / `files_not_to_touch` plus exact changed-files subset validation.

If exact non-overlapping boundaries cannot be produced, the run closure must return `CODEX_HANDOFF_BLOCKED` and must not claim the handoff is copy-paste runnable.

## Codex Direct-To-Main Closure Rule

Eligible simple single-Direction proof-state Codex handoffs should not require a second human "merge to main" turn after validation has already passed.

A handoff may set `branch_policy: direct_to_main_allowed` only when the commit is a simple single-Direction proof-state commit with exact non-overlapping allowed and forbidden paths and no workflow core, docs/setup, Project setup, migration, product implementation, execution package, legacy import, or multi-Direction changes.

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

If the operator cannot produce a self-contained Codex handoff with exact non-overlapping path boundaries, it must clearly state the missing fields and return `BLOCKED_CONTEXT_NEEDED` or `CODEX_HANDOFF_BLOCKED`.

## Next Chat Rule

When terminal outcome is `NEXT_CHAT_NEEDED`, the response must include a plain-language prompt that can be pasted into a new ChatGPT chat.

The prompt may include Obligation IDs, but must also describe the work in normal language.

The response must state why the new chat is required. When the next target is newly opened after current run closure, the reason is Single Material Run Chat Boundary.

END_OF_FILE: workflow/policies/12_HUMAN_FACING_RUN_CLOSURE_POLICY.md
