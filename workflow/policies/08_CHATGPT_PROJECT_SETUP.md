---
artifact_control:
  namespace: workflow
  artifact_type: chatgpt_project_setup_principles
  status: single_material_run_chat_boundary_hardened
  owner: workflow_os
---

# ChatGPT Project Setup Principles

## Scope

This file defines active setup principles for ChatGPT Project setup in the Workflow OS repository.

Project setup files are storage/adapter surfaces. They do not create accepted Ledger state.

Use `workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md` for new ordinary Direction Workflow Projects.

## Project Types

There are two supported setup types:

- ordinary Direction Workflow Projects
- Workflow Governance Maintenance Project

Ordinary Direction Workflow Projects run the Workflow OS for one Direction.

The Workflow Governance Maintenance Project services the workflow repository as a maintenance, audit, debug, research, setup, Codex handoff, and Codex result verification console.

The existing universal direction project instructions template is not the correct template for the Workflow Governance Maintenance Console.

The maintenance console must not default to Dashboard/Obligations next-valid-run behavior, root objective confirmation, Obligation-controlled chat protocol, or Receipt Card output.

The maintenance console must not default-load Direction payload files.

## Universal Setup Model

New ordinary Direction Workflow Projects use one setup model:

- Project Instructions UI
- Universal Project Shell
- Shared Workflow Runtime Packs
- Direction Payload
- Optional Capability Packs
- Product Repo Execution Setup, handled separately in the target product repository

The Workflow Governance Maintenance Project uses its own Project Instructions and manifest:

- `directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`
- `directions/workflow-governance/workflow/project_setup/PROJECT_FILES_MANIFEST.md`

Its default upload set is:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md`
- `workflow/project_packs/PROJECT_PACKS_INDEX.md`
- `docs/CHATGPT_PROJECT_SETUP.md`
- `workflow/policies/08_CHATGPT_PROJECT_SETUP.md`

`PROJECT_PACKS_INDEX.md` is default only for the Workflow Governance Maintenance Project because that project is explicitly a setup and pack inspection console. It remains request-only for ordinary Direction Workflow Projects.

## Project Surface Taxonomy

Project Instructions UI:

- The ChatGPT Project settings field for project-specific behavior instructions.
- Users paste instruction text here.
- This is not an uploaded Project File/Source.

Project Files/Sources:

- Uploaded reference materials / project sources.
- Includes default shared workflow packs and Direction payload files for ordinary Direction Workflow Projects.
- Includes the maintenance-console default upload set for the Workflow Governance Maintenance Project.

Repository Project Instruction Source:

- Repository source or template used to produce Project Instructions UI text.
- It may live at `directions/<direction-id>/<active-project-setup>/CHATGPT_PROJECT_INSTRUCTIONS.md`.
- It is not a default Project File/Source upload.
- It must not store live Direction state.

Request-only sources:

- Files or packs loaded only when an admitted task requires them.
- Includes `workflow/project_packs/EXECUTION_HARNESS_PACK.md`.
- Includes `workflow/project_packs/PROJECT_PACKS_INDEX.md` for ordinary Direction Workflow Projects when exact setup inspection is needed.

## Correct Default Setup

1. Paste or update Project Instructions in the ChatGPT Project Instructions UI.
2. Upload or replace Project Files/Sources for the Project type:
   - ordinary Direction Workflow Projects: default shared packs plus Direction payload files.
   - Workflow Governance Maintenance Project: the maintenance-console default upload set only.

## Default Project Files/Sources

For ordinary Direction Workflow Projects, use packs as the default shared upload surface:

- `workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `workflow/project_packs/WORKFLOW_BASE_PACK.md`
- `workflow/project_packs/TRANSPORT_CORE_PACK.md`

For ordinary Direction Workflow Projects, upload Direction payload files individually:

- `directions/<direction-id>/<active-direction-state>/LEDGER.md`
- `directions/<direction-id>/<active-direction-state>/OBLIGATIONS.md`
- `directions/<direction-id>/<active-direction-state>/RECEIPTS_INDEX.md`
- `directions/<direction-id>/<active-direction-state>/COMMIT_SCOPES.md`
- `directions/<direction-id>/<active-direction-state>/DASHBOARD.md`
- `directions/<direction-id>/<active-direction-state>/MIGRATION_RECEIPT.md`

## Active Manifest Model

Direction-specific manifests use the pack model.

The older 31-file Project Files model is superseded.

Ordinary Direction default upload is three shared packs plus six Direction payload files.

Workflow Governance Maintenance Project default upload is the five-file maintenance-console set listed above.

Project Instructions source files are UI payload sources. They must not be uploaded as default Project Files/Sources, must not be included in the default upload count, and must not store live Direction state.

Direction payload files win for live state.

## Project Instructions UI Payload Budget

Project Instructions UI payloads are compressed behavioral control text, not workflow documentation, schema storage, or Project File substitutes.

Generated Project Instructions UI payloads must stay within this budget:

```yaml
hard_max_chars: 8000
target_max_chars: 6500
warning_threshold_chars: 7200
measured_scope: trimmed content between BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD and END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD
```

Validation fails if any generated UI payload exceeds 8,000 characters.

Warn and report if any generated UI payload exceeds 7,200 characters.

Target every generated UI payload at or below 6,500 characters.

Payloads must use compact imperative rules, avoid long explanations, avoid full schemas/card definitions, avoid full path lists when generic path rules are enough, and tell the model to inspect exact canonical files when needed.

## Request-Only Execution Harness

`workflow/project_packs/EXECUTION_HARNESS_PACK.md` is request-only.

Do not default-load the Execution Harness Pack unless execution readiness, product repo setup, CodexRun, validation, human-guided execution, or complex technical mission work is admitted.

For ordinary Direction Workflow Projects, `workflow/project_packs/PROJECT_PACKS_INDEX.md` is request-only unless exact setup inspection requires it.

Execution is not a semantic primitive.

Codex is not the execution system.

CodexRun is a gated Operator family inside execution.

## Stored Project Setup Files

Universal project setup sources live under:

- `workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md`
- `workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md`
- `workflow/project_setup/UNIVERSAL_PROJECT_FILES_MANIFEST_TEMPLATE.md`
- `workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md`

Per-Direction generated setup files live under:

- `directions/<direction-id>/<active-project-setup>/`

## Context Authority Setup Rule

For ordinary Direction Workflow Projects, Project Files/Sources may provide context, but only committed Ledger and Receipts provide accepted state.

Loaded domain files must be treated as candidate_context unless the Ledger says otherwise.

For the Workflow Governance Maintenance Project, GitHub repository state is source of truth and Project Files/Sources are cache. Load exact affected files on demand. Ledger, Obligation, and Receipt concepts are analyzed subject matter unless the user explicitly asks to inspect or validate runtime state.

## No Next Valid Run Setup Rule

For ordinary Direction Workflow Projects, if Dashboard/Obligations show no next valid run, no open next obligation, or empty `next_valid_runs`, treat the Direction as `paused_for_admission`.

In `paused_for_admission`, do not execute candidate routes or proposed Obligations. The Project may only offer a bounded HumanDecision / ObligationAdmission choice for at most one next bounded Obligation, or return `NEXT_CHAT_NEEDED` with an exact recovery prompt when the chat was not opened for admission.

Candidate routes and proposed Obligations remain candidate until Receipt -> Verify -> Commit.

This ordinary Direction rule does not apply to the Workflow Governance Maintenance Project. The maintenance console must not default to Dashboard/Obligations next-valid-run behavior.

## Human Input Setup Rule

Workflow Projects should not require users to answer in YAML.

Terse or spoken answers must be normalized when intent is clear.

## Run Closure Setup Rule

Workflow Projects must not make the user build Codex tasks manually from Receipts.

Material runs must end with a human-readable terminal outcome and any needed copy-paste handoff.

Workflow Projects must expect Codex Commit Handoff Cards to be fully self-contained.

Codex Commit Handoff Cards must declare `branch_policy`. Missing or unclear branch policy means `review_branch_required`.

Generated Codex handoffs must not contain allowed/forbidden/protected path overlap. `allowed_paths` is the changed-files whitelist; validation must prove changed files are an exact subset of `allowed_paths` and no allowed path is matched by `forbidden_paths` or protected sibling globs. Do not use `directions/*/workflow/**` as forbidden when the active Direction workflow path is allowed; protect siblings with exact allowed-path validation and concrete protected/not-to-touch paths.

Ordinary Direction Project chats may emit `direct_to_main_allowed` only for eligible simple single-Direction proof-state commits after exact path boundaries and validation requirements are known. Workflow core, docs/setup, Project setup, migrations, multi-Direction changes, product implementation, execution packages, legacy imports, risky changes, uncertain validation, or unverifiable changed-file sets must use `review_branch_required`.

Direct-to-main guidance must state that Codex stays in the existing Direction worktree, does not switch to local `main`, does not use a global main worktree, validates before and after clean rebase onto `origin/main`, pushes `HEAD` to `origin/main`, verifies the remote SHA, and does not ask for a second human merge command after success.

Handoffs and run closures must separate Project Instructions UI updates from Project Files/Sources refreshes using:

- `project_instruction_ui_update_required`
- `project_sources_files_refresh_required`
- `request_only_sources_refresh_required`
- `do_not_upload_as_project_file`

Do not list `directions/<direction-id>/<active-project-setup>/CHATGPT_PROJECT_INSTRUCTIONS.md` under Project Files/Sources refresh.

If a Codex handoff is not self-contained, the correct response is to ask the Operator chat to regenerate the handoff.

## Legacy Non-Authority

Old workflow runtime files, old stage prompts, old transport files, old Direction project files, and old project setup files must not be default authority for the workflow.

They may be loaded only as explicitly identified legacy evidence for a Legacy Import Obligation.

## Ordinary Direction Chat Rule

For ordinary Direction Workflow Projects, one active target Obligation may be worked materially at a time.

One chat = one material Operator run plus Codex verification/closure.

Same Direction / same product / same game does not imply same chat.

After each committed material run, the next material Obligation must start in a new chat by default with `NEXT_CHAT_NEEDED` and an exact launch prompt.

The same chat is allowed only for non-material explanation, verifying the Codex result for the current handoff, failed validation repair for the same handoff, or producing a recovery / next-chat prompt.

If the work is compound, the chat must scope-triage, decompose only what is required for the current target Obligation, return child prompts governed by child handoff rules, or return `split_required` instead of pretending completion.

Child chats serve the current parent target Obligation. They are not a substitute for the new-chat boundary after a completed material run.

The Workflow Governance Maintenance Project uses one concrete maintenance problem per chat and does not use Obligation framing as the controlling chat protocol by default.

END_OF_FILE: workflow/policies/08_CHATGPT_PROJECT_SETUP.md
