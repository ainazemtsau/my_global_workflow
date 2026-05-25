---
artifact_control:
  namespace: proof_workflow_project_packs
  artifact_type: project_pack
  pack_name: UNIVERSAL_PROJECT_SHELL_PACK
  pack_type: runtime_cache_upload_convenience
  intended_load_mode: default_all_directions
  status: u1_initial
  owner: proof_carrying_workflow_os
  generated_from_ref: main@14bc73b11c609787e5919989a6e3fb6de2450c9e
  do_not_use_as_authority: true
  refresh_rule: "Regenerate and refresh this pack if any source_manifest file changes."
source_manifest:
  - WORKFLOW_SOURCE_OF_TRUTH.md
  - README.md
  - AGENTS.md
  - docs/CHATGPT_PROJECT_SETUP.md
  - docs/CODEX_APP_SETUP.md
  - docs/NEW_DEVICE_BOOTSTRAP.md
  - proof_workflow/08_CHATGPT_PROJECT_SETUP.md
  - proof_workflow/09_STORAGE_LAYOUT_POLICY.md
  - proof_workflow/10_CONTEXT_AUTHORITY_POLICY.md
  - proof_workflow/11_HUMAN_INPUT_NORMALIZATION_POLICY.md
  - proof_workflow/12_HUMAN_FACING_RUN_CLOSURE_POLICY.md
  - proof_workflow/13_RECURSIVE_CHILD_HANDOFF_POLICY.md
---

# Universal Project Shell Pack

## Cache Boundary

This pack is a ChatGPT Project Files runtime cache / upload convenience artifact.

It is not semantic authority.

Canonical source files listed in `source_manifest` remain authority.

If this pack conflicts with a verified canonical source file, the canonical source wins.

If any `source_manifest` file changes, regenerate and refresh this pack before using it as Project Files cache.

## Project Source Of Truth

GitHub repository `ainazemtsau/my_global_workflow` is the canonical AI workflow source while `WORKFLOW_SOURCE_OF_TRUTH.md` says `active`.

The active workflow authority is `proof_workflow/**`.

ChatGPT Project Files are runtime cache. They do not create accepted proof state.

Direction proof state lives under:

```text
directions/<direction-id>/proof/
```

Only verified Receipts committed to the Direction Ledger create accepted Direction state.

## Default Load Boundary

New proof Projects should not load old vNext-R workflow files, old stage files, old transport files, or old Direction `project_files/00-08` by default.

Old Direction data is legacy evidence only until imported through:

```text
Legacy Import Receipt -> Verify -> Commit
```

Old Direction Map, Active Goal, Current Phase, Portfolio Queue, project setup files, phases, and execution logs are not accepted proof state by being present in the repository.

## Context Authority

Loaded context is not accepted state.

Every material use of loaded context must classify it as accepted Ledger state, committed Receipt, current human input, candidate context, projection context, legacy evidence, instruction context, or unknown.

Candidate context may support questions, options, assumptions, or candidate Obligations. It must not become root objective, constraint, Horizon, Active Frontier, roadmap, execution precondition, or accepted claim without explicit human decision or committed Receipt.

## Human Input

Human users do not need to reply in YAML, schemas, or formal card syntax.

Terse or spoken human answers may be normalized when intent is clear. Normalization must be recorded and must not create hidden acceptance.

## Run Closure

Every material response must end with a clear terminal outcome for the user.

Return the human-readable result first. Technical cards belong after the explanation.

If a Codex commit is needed, provide a fully self-contained Codex Commit Handoff Card with repository, worktree, branch, mode, allowed paths, forbidden paths, validation, commit behavior, push behavior, and Project Files refresh requirements.

If child chats are needed, provide copy-paste child prompts, state what results must return, and include a Parent Recovery Block when multiple children are launched.

END_OF_FILE: proof_workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md
