# Workflow v3 Runbooks

status: transitional_legacy_operational_namespace

## Purpose

This directory contains legacy or transitional operating paths for Workflow v3 work that have not yet been migrated into the Procedure Definition Framework.

Runbooks are human-readable and AI-usable operating references. They are not the canonical location for new or migrated Procedure Definition Framework procedures.

Canonical new or migrated procedures belong under:

```text
workflow_v3/procedures/**
```

and should use:

```text
*_PROCEDURE.md
```

## Transitional boundary

Do not add new Procedure Definition Framework procedures to this directory.

Do not keep a migrated procedure in this directory merely because an old registry entry pointed here.

Active registry entries must not point here. If a runbook-backed entrypoint is not migrated, represent it through a canonical stub procedure under `workflow_v3/procedures/**`.

Compatibility shims, if any, must be explicitly bounded by a later admitted repository update and must not replace the canonical procedure source.

## Non-authority boundary

Runbooks do not adopt Directions, create runtime roots, import legacy state, update actual ChatGPT Projects, refresh Project Files/Sources, upload packs, execute product work, or decommission the old Workflow OS by themselves.

## Transitional runbook index

These files remain as legacy/transitional operating references until their entrypoints are migrated or explicitly removed by a later cleanup package:

- `DIRECTION_BOOTSTRAP_RUNBOOK.md`
- `DIRECTION_SPINE_CHAT_RUNBOOK.md`
- `DIRECTION_MAP_CHAT_RUNBOOK.md`
- `ACTIVE_FRONT_SELECTION_RUNBOOK.md`
- `WORK_GRAPH_OPENING_RUNBOOK.md`
- `WORK_CONTRACT_RUNBOOK.md`
- `PARENT_CHILD_CHAT_RUNBOOK.md`
- `CODEX_HANDOFF_VERIFICATION_RUNBOOK.md`
- `PROJECT_SETUP_ROLLOUT_RUNBOOK.md`
- `RUNTIME_CONSOLE_RUNBOOK.md`

## Common operating rule

Every material run or review in the active procedure model closes with FINISH_PACKET, Result Packet, and Next Move Packet. State changes require explicit acceptance/update path.

END_OF_FILE: workflow_v3/runbooks/README.md
