# Workflow Source of Truth

Status: active

Purpose: repository authority locator and active-workflow bootstrap sentinel.

This file answers only bootstrapping questions:

- which repository is canonical
- whether the current active workflow namespace is active or legacy
- where exact authority must be read from when material workflow work depends on it

This file is not semantic authority, not runtime policy, not accepted Direction state, not a Receipt, not a project pack, and not a replacement for exact canonical files.

Canonical AI workflow repository: `ainazemtsau/my_global_workflow`.

Active Workflow OS namespace: `workflow/**`.

Current Workflow OS / rollback namespace: `workflow/**`.

Workflow v3 clean-start skeleton namespace: `workflow_v3/**`.

Old Direction evidence namespace for Workflow v3: `directions/**`.

Future Workflow v3 Direction namespace: `directions_v3/**`.

If this file conflicts with a verified canonical file under `workflow/**`, the canonical `workflow/**` file wins for the current Workflow OS.

If this file conflicts with a verified canonical file under `workflow_v3/**`, the canonical `workflow_v3/**` file wins for Workflow v3 skeleton boundaries.

If exact state matters, inspect the exact repository file from GitHub `main` instead of relying on uploaded ChatGPT Project Files/Sources cache.

## Canonical Authority Boundary

Workflow OS semantics, runtime protocols, policies, transport schemas, project setup rules, validation rules, execution rules, and storage rules are governed by verified files under `workflow/**`.

Workflow v3 skeleton boundaries, setup sources, and clean-start namespace rules are governed by verified files under `workflow_v3/**`.

Direction accepted proof state is governed by verified Direction payload files and committed Ledger/Receipt state under the relevant active Direction payload directory.

Old Direction files under `directions/**` are legacy evidence for Workflow v3 unless a verified bridge/import/adoption policy says otherwise. Future Workflow v3 Direction runtime state belongs under `directions_v3/<direction-id>/runtime/**` only after an explicit adoption package creates it.

Workflow Governance uses its active workflow payload under:

- `directions/workflow-governance/workflow/**`

Ordinary Direction Workflow Projects use the active payload directory declared by their setup/manifest files.

ChatGPT Project Files/Sources, project packs, setup docs, projections, dashboards, copied snippets, and uploaded files are cache/context unless traced to verified repository state and, where required, committed Ledger/Receipt state.

## Project Setup Boundary

ChatGPT Project setup has separate surfaces:

- Project Instructions UI
- Project Files/Sources
- repository Project Instruction Sources
- request-only sources

Repository files named `CHATGPT_PROJECT_INSTRUCTIONS.md` are sources for the Project Instructions UI. They are not default Project Files/Sources.

The Workflow Governance Maintenance Project may upload this file as part of its default maintenance-console context, but this file remains an authority locator, not semantic authority.

## Legacy Boundary

The pre-proof vNext-R main snapshot is preserved at:

- legacy branch: `legacy/vnext-r-main-before-proof-os-2026-05-25`
- legacy tag: `vnext-r-main-before-proof-os-2026-05-25`

Old vNext-R workflow files, old Direction `project_files/00-08`, old Direction Map, Active Goal, Current Phase, Portfolio Queue, old transport, old stage prompts, and `repository_patch.v1` are legacy evidence only unless explicitly imported by the current workflow.

## Read Completeness

A truncated, omitted, or tail-unverified repository read is not sufficient authority for material workflow work.

If material work depends on a file whose full content cannot be verified, return a Context Request naming the exact path and blocker.

END_OF_FILE: WORKFLOW_SOURCE_OF_TRUTH.md
