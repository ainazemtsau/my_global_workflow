---
artifact_control:
  namespace: direction_workflow_project_setup
  direction_id: solo-max-productive
  artifact_type: project_files_manifest
  project_name: "Solo Max Productive"
  status: u3_pack_model
  owner: workflow_os
---

# Solo Max Productive — Workflow Project Files Manifest

Project name: Solo Max Productive

Project Instructions source:

- `directions/solo-max-productive/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`

## Default Shared Project Packs

- `project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `project_packs/WORKFLOW_BASE_PACK.md`
- `project_packs/TRANSPORT_CORE_PACK.md`

## Direction Payload

- `directions/solo-max-productive/LEDGER.md`
- `directions/solo-max-productive/OBLIGATIONS.md`
- `directions/solo-max-productive/RECEIPTS_INDEX.md`
- `directions/solo-max-productive/COMMIT_SCOPES.md`
- `directions/solo-max-productive/DASHBOARD.md`
- `directions/solo-max-productive/MIGRATION_RECEIPT.md`

## Request-Only Capability Packs

- `project_packs/EXECUTION_HARNESS_PACK.md`

Load request-only capability packs only when an admitted task needs them.

## Request-Only Exact Canonical Files

If a pack summary is insufficient or exact schema/source text is material, request or load the exact canonical source file listed in the relevant pack `source_manifest`.

## Do Not Load By Default

- `workflow/**`
- `directions/solo-max-productive/project_setup/**`
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

1. Create ChatGPT Project named "Solo Max Productive".
2. Paste Project Instructions from `CHATGPT_PROJECT_INSTRUCTIONS.md`.
3. Upload the three default shared packs.
4. Upload the six Direction payload files.
5. Do not upload forbidden legacy files.
6. Run setup validation using `project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md` if needed.
7. Start with the next valid run shown by `DASHBOARD.md` / `OBLIGATIONS.md`.

## Project Files Count Summary

```yaml
default_upload_count: 9
default_shared_packs: 3
direction_payload_files: 6
request_only_execution_pack: 1
```

END_OF_FILE: directions/solo-max-productive/project_setup/PROJECT_FILES_MANIFEST.md
