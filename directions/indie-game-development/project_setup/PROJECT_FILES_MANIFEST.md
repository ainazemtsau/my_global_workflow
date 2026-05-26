---
artifact_control:
  namespace: direction_proof_project_setup
  direction_id: indie-game-development
  artifact_type: project_files_manifest
  project_name: "Indie Game Development — Proof"
  status: u3_pack_model
  owner: proof_carrying_workflow_os
---

# Indie Game Development — Proof Project Files Manifest

Project name: Indie Game Development — Proof

Project Instructions source:

- `directions/indie-game-development/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`

## Default Shared Project Packs

- `proof_workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `proof_workflow/project_packs/PROOF_BASE_PACK.md`
- `proof_workflow/project_packs/TRANSPORT_CORE_PACK.md`

## Direction Payload

- `directions/indie-game-development/LEDGER.md`
- `directions/indie-game-development/OBLIGATIONS.md`
- `directions/indie-game-development/RECEIPTS_INDEX.md`
- `directions/indie-game-development/COMMIT_SCOPES.md`
- `directions/indie-game-development/DASHBOARD.md`
- `directions/indie-game-development/MIGRATION_RECEIPT.md`

## Request-Only Capability Packs

- `proof_workflow/project_packs/EXECUTION_HARNESS_PACK.md`

Load request-only capability packs only when an admitted task needs them.

## Request-Only Exact Canonical Files

If a pack summary is insufficient or exact schema/source text is material, request or load the exact canonical source file listed in the relevant pack `source_manifest`.

## Do Not Load By Default

- `workflow/**`
- `directions/indie-game-development/project_files/**`
- `directions/*/project_files/**`
- other Direction `project_setup/**` folders
- `directions/*/phases/**`
- `directions/*/execution_logs/**`
- `migration/**`
- product repo `.execution/**` unless operating inside the target product repo and explicitly admitted
- old runtime, stage, and transport files from previous workflow systems
- raw chats, archive notes, or old rebuild packs

## Refresh Rule

- If a Direction payload file changes, refresh that uploaded Project File.
- If a project pack changes, refresh that uploaded pack.
- If any canonical source file in a pack `source_manifest` changes, regenerate and refresh the pack before relying on it.
- GitHub remains source of truth; Project Files are runtime cache.

## Restoration Steps

1. Create ChatGPT Project named "Indie Game Development — Proof".
2. Paste Project Instructions from `CHATGPT_PROJECT_INSTRUCTIONS.md`.
3. Upload the three default shared packs.
4. Upload the six Direction payload files.
5. Do not upload forbidden legacy files.
6. Run setup validation using `proof_workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md` if needed.
7. Start with the next valid run shown by `DASHBOARD.md` / `OBLIGATIONS.md`.

## Project Files Count Summary

```yaml
default_upload_count: 9
default_shared_packs: 3
direction_payload_files: 6
request_only_execution_pack: 1
```

END_OF_FILE: directions/indie-game-development/project_setup/PROJECT_FILES_MANIFEST.md
