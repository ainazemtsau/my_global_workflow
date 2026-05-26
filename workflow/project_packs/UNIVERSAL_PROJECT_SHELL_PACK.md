---
artifact_control:
  namespace: workflow_project_packs
  artifact_type: project_pack
  pack_name: UNIVERSAL_PROJECT_SHELL_PACK
  pack_type: runtime_cache_upload_convenience
  intended_load_mode: default_all_directions
  status: project_instruction_budget_hardened
  owner: workflow_os
  generated_from_ref: wg/project-instruction-budget@R-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001
  refreshed_for_receipt: R-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001
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

GitHub repository `ainazemtsau/my_global_workflow` is the canonical AI workflow source while `WORKFLOW_SOURCE_OF_TRUTH.md` says `active`.

The active workflow authority is `workflow/**`.

ChatGPT Project surfaces are runtime cache. They do not create accepted state.

Project Instructions UI is the ChatGPT Project settings field where behavior instructions are pasted.

Project Files/Sources are uploaded reference materials.

Repository files named `CHATGPT_PROJECT_INSTRUCTIONS.md` are Project Instructions UI payload sources. They are not default Project Files/Sources and must not be included in default upload counts.

Project Instructions UI payloads must be compact behavior instructions: hard max 8,000 characters, target 6,500, warn above 7,200. Count only trimmed content between the BEGIN/END UI payload markers.

Direction proof state lives under:

```text
directions/<direction-id>/
```

Workflow Governance is the self-hosted governance Direction and uses `directions/workflow-governance/workflow/` for active proof payload, not the Direction root:

```text
directions/workflow-governance/workflow/
```

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

If a Codex commit is needed, provide a fully self-contained Codex Commit Handoff Card with repository, worktree, branch, mode, allowed paths, forbidden paths, validation, commit behavior, push behavior, and separated project refresh requirements.

Refresh requirements must use `project_instruction_ui_update_required`, `project_sources_files_refresh_required`, `request_only_sources_refresh_required`, and `do_not_upload_as_project_file`.

Do not list `project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md` under Project Files/Sources refresh.

When Project Instructions sources change, report `project_instruction_ui_payload_char_counts`.

Same-parent continuation is the default for one bounded user problem, including after `CODEX_COMMIT_NEEDED`, Codex results, and child results.

`NEXT_CHAT_NEEDED` is exceptional. Ask for a new chat only when same-parent continuation is unsafe or invalid, and explain why.

If child chats are needed for the current target Obligation, provide copy-paste child prompts, state what results must return, and include a Parent Recovery Block when multiple children are launched.

Do not launch child chats for future topics, blocked phases, unrelated residual work, or mere thoroughness. Child results return to the parent chat for synthesis.

END_OF_FILE: workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md
