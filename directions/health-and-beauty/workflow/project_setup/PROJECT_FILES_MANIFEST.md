---
artifact_control:
  namespace: direction_workflow_project_setup
  direction_id: health-and-beauty
  artifact_type: project_files_manifest
  project_name: "Health and Beauty"
  status: u3_pack_model
  owner: workflow_os
---

# Health and Beauty — Workflow Project Files Manifest

Project name: Health and Beauty

Project Instructions source:

- `directions/health-and-beauty/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`

## Default Shared Project Packs

- `proof_workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `proof_workflow/project_packs/PROOF_BASE_PACK.md`
- `proof_workflow/project_packs/TRANSPORT_CORE_PACK.md`

## Direction Payload

- `directions/health-and-beauty/workflow/LEDGER.md`
- `directions/health-and-beauty/workflow/OBLIGATIONS.md`
- `directions/health-and-beauty/workflow/RECEIPTS_INDEX.md`
- `directions/health-and-beauty/workflow/COMMIT_SCOPES.md`
- `directions/health-and-beauty/workflow/DASHBOARD.md`
- `directions/health-and-beauty/workflow/MIGRATION_RECEIPT.md`

## Request-Only Capability Packs

- `project_packs/EXECUTION_HARNESS_PACK.md`

Load request-only capability packs only when an admitted task needs them.

## Request-Only Exact Canonical Files

If a pack summary is insufficient or exact schema/source text is material, request or load the exact canonical source file listed in the relevant pack `source_manifest`.

## Do Not Load By Default

- `workflow/**`
- `directions/health-and-beauty/archive/**`
- `directions/*/project_files/**`
- `directions/*/project_setup/**`
- `directions/*/phases/**`
- `directions/*/execution_logs/**`
- `migration/**`
- product repo `.execution/**` unless operating inside the target product repo and explicitly admitted
- old vNext-R runtime/stage/transport files
- raw chats, archive notes, or old rebuild packs

## Refresh Rule

- If a Direction payload file changes, refresh that uploaded Project File.
- If a project pack changes, refresh that uploaded pack.
- If any canonical source file in a pack `source_manifest` changes, regenerate and refresh the pack before relying on it.
- GitHub remains source of truth; Project Files are runtime cache.

## Restoration Steps

1. Create ChatGPT Project named "Health and Beauty".
2. Paste Project Instructions from `CHATGPT_PROJECT_INSTRUCTIONS.md`.
3. Upload the three default shared packs.
4. Upload the six Direction payload files.
5. Do not upload forbidden legacy files.
6. Run setup validation using `project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md` if needed.
7. Start with the next valid run shown by `workflow/DASHBOARD.md` / `workflow/OBLIGATIONS.md`.

## Project Files Count Summary

```yaml
default_upload_count: 9
default_shared_packs: 3
direction_payload_files: 6
request_only_execution_pack: 1
```

END_OF_FILE: directions/health-and-beauty/workflow/project_setup/PROJECT_FILES_MANIFEST.md
