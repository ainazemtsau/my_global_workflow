---
artifact_control:
  namespace: workflow_project_packs
  artifact_type: project_pack_index
  pack_name: PROJECT_PACKS_INDEX
  pack_type: runtime_cache_upload_convenience_index
  intended_load_mode: request_only
  status: u1_initial
  owner: workflow_os
  generated_from_ref: main@14bc73b11c609787e5919989a6e3fb6de2450c9e
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
---

# Project Packs Index

## Pack Boundary

Project Packs are ChatGPT Project Files runtime cache / upload convenience artifacts.

They are not semantic authority.

Canonical source files remain separate and remain authority.

If a pack conflicts with a verified canonical source file, the canonical source wins.

If any file listed in a pack `source_manifest` changes, regenerate and refresh that pack before relying on it as Project Files cache.

If this index conflicts with a pack or canonical source file, the more specific canonical source wins.

## Default Load Recommendation

For ordinary Direction Workflow Projects, default upload can be reduced to:

- `workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `workflow/project_packs/WORKFLOW_BASE_PACK.md`
- `workflow/project_packs/TRANSPORT_CORE_PACK.md`
- Direction payload files under `directions/<direction-id>/proof/`

Direction payload files are the Direction Ledger, Obligations, Receipts index, Commit scopes, Dashboard, and Migration receipt.

## Request-Only Capability Packs

Use `workflow/project_packs/EXECUTION_HARNESS_PACK.md` only when the Direction Project intentionally works on execution readiness, CodexRun, validation, complex technical missions, human-guided execution, or product repo technical memory.

The execution harness pack is not a default load for every chat.

Future optional request-only packs may include:

- `workflow/project_packs/MIGRATION_LEGACY_IMPORT_PACK.md`
- `workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md`

Those future pack names are reserved only as recommendations. They are not created by this U1 patch.

## Exact Schema Fallback

Pack summaries reduce upload burden, but they do not replace exact canonical schemas.

If a pack summary is insufficient or a card schema is material, load the canonical source file from the pack `source_manifest`.

This is especially important for transport cards, execution launch cards, receipt cards, validation cards, and commit handoff cards.

## Legacy Boundary

Do not use old vNext-R workflow/runtime, stage registry, stage prompts, old transport, or old Direction `project_files/00-08` as default Project Files load.

Old files may be used only as legacy evidence through an admitted legacy import workflow.

END_OF_FILE: workflow/project_packs/PROJECT_PACKS_INDEX.md
