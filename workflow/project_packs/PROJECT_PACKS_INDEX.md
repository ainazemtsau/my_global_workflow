---
artifact_control:
  namespace: workflow_project_packs
  artifact_type: project_pack_index
  pack_name: PROJECT_PACKS_INDEX
  pack_type: runtime_cache_upload_convenience_index
  intended_load_mode: default_workflow_governance_maintenance_request_only_ordinary_directions
  status: single_material_run_chat_boundary_hardened
  owner: workflow_os
  generated_from_ref: wg/single-material-run-chat-boundary-2026-05-27
  refreshed_for_receipt: null
  do_not_use_as_authority: true
  refresh_rule: "Regenerate and refresh this index if any source_manifest file changes."
source_manifest:
  - WORKFLOW_SOURCE_OF_TRUTH.md
  - workflow/README.md
  - docs/CHATGPT_PROJECT_SETUP.md
  - workflow/policies/08_CHATGPT_PROJECT_SETUP.md
  - workflow/policies/09_STORAGE_LAYOUT_POLICY.md
  - workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md
  - workflow/project_packs/WORKFLOW_BASE_PACK.md
  - workflow/project_packs/TRANSPORT_CORE_PACK.md
  - workflow/project_packs/EXECUTION_HARNESS_PACK.md
  - workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md
---

# Project Packs Index

## Pack Boundary

Project Packs are ChatGPT Project Files/Sources runtime cache / upload convenience artifacts.

They are not semantic authority.

Canonical source files remain separate and remain authority.

`WORKFLOW_SOURCE_OF_TRUTH.md` is an authority locator and bootstrap sentinel only, not semantic authority.

If a pack conflicts with a verified canonical source file, the canonical source wins.

If any file listed in a pack `source_manifest` changes, regenerate and refresh that pack before relying on it as Project Files/Sources cache.

If this index conflicts with a pack or canonical source file, the more specific canonical source wins.

This index is default for the Workflow Governance Maintenance Project and request-only for ordinary Direction Workflow Projects. Do not upload it by default for ordinary Direction Workflow Projects unless exact setup inspection needs it or it is already uploaded and must be refreshed.

Project Instructions UI is separate from Project Files/Sources. Repository instruction sources such as `directions/<direction-id>/<active-project-setup>/CHATGPT_PROJECT_INSTRUCTIONS.md` are pasted into the ChatGPT Project Instructions field and are not uploaded as default Project Files/Sources.

Project Instructions UI payloads must stay below the 8,000-character hard max, target 6,500 characters, and warn above 7,200 characters.

Codex handoffs must use separated project refresh fields, including payload character counts when instruction sources change.

Codex handoffs must declare `branch_policy`. `review_branch_required` is the default and is required for workflow core/setup, docs/setup, Project setup, risky, migration, multi-Direction, product, execution-package, legacy-import, conflict, or unverifiable changed-path work. `direct_to_main_allowed` is limited to eligible simple single-Direction proof-state commits and still requires validation, clean rebase onto `origin/main`, `HEAD` push to `origin/main`, and remote SHA verification without switching to local `main` or using a global main worktree. Legacy merge flags do not authorize this fast path by themselves.

## Default Load Recommendation

For ordinary Direction Workflow Projects, default upload is:

- `workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `workflow/project_packs/WORKFLOW_BASE_PACK.md`
- `workflow/project_packs/TRANSPORT_CORE_PACK.md`
- Direction payload files under the Direction's active payload directory listed by its Project Files manifest.

Direction payload files are the Direction Ledger, Obligations, Receipts index, Commit scopes, Dashboard, and Migration receipt.

Default upload count excludes Project Instructions UI sources.

The default packs now summarize Atomic Run / Single Responsibility, Scope Triage Before Material Work, Operator Independence / Effectiveness Over Agreement, Single Material Run Chat Boundary, child-handoff gating, Receipt scope audit, and next-chat default after committed material runs.

For the Workflow Governance Maintenance Project, `GOVERNANCE_MAINTENANCE_PACK.md` contains the detailed Real Transcript Review procedure: short natural-language triggers plus pasted completed transcript, P0 Single Responsibility / Atomic Run as the first mandatory gate, lifecycle surface detection, relevant-only surface checks, Codex handoff/result verification when applicable, stable transcript defect classes, and explicit terminal outcome. The Project Instructions UI only bootstraps this procedure.

For the Workflow Governance Maintenance Project, default upload is different:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md`
- `workflow/project_packs/PROJECT_PACKS_INDEX.md`
- `docs/CHATGPT_PROJECT_SETUP.md`
- `workflow/policies/08_CHATGPT_PROJECT_SETUP.md`

`WORKFLOW_SOURCE_OF_TRUTH.md` is included here as maintenance-console bootstrap context, not as semantic authority.

`workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md` is default only for the Workflow Governance Maintenance Project.

It is not default for ordinary Direction Workflow Projects.

Ordinary Direction Workflow Projects still use Universal Shell, Workflow Base, Transport Core, and Direction payload files.

The maintenance console should not default-load Direction payload files.

## Request-Only Capability Packs

Use `workflow/project_packs/EXECUTION_HARNESS_PACK.md` only when the Direction Project intentionally works on execution readiness, CodexRun, validation, complex technical missions, human-guided execution, or product repo technical memory.

The execution harness pack is not a default load for every chat.

No `workflow/project_packs/MIGRATION_LEGACY_IMPORT_PACK.md` file is currently present. Treat that filename as future-only/non-present unless a future committed source adds it.

`workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md` is an actual pack for the Workflow Governance Maintenance Project, not a future optional ordinary Direction Project pack.

## Exact Schema Fallback

Pack summaries reduce default upload burden, but they do not replace exact canonical schemas.

If a pack summary is insufficient or a card schema is material, request or load the canonical source file from the pack `source_manifest`.

This is especially important for transport cards, execution launch cards, receipt cards, validation cards, and commit handoff cards.

## Legacy Boundary

Do not use old vNext-R workflow/runtime, stage registry, stage prompts, old transport, or old Direction `project_files/00-08` as default Project Files/Sources load.

Old files may be used only as legacy evidence through an admitted legacy import workflow.

END_OF_FILE: workflow/project_packs/PROJECT_PACKS_INDEX.md
