# Project Setup Integration

status: candidate_draft

## Purpose

This document designs how future Workflow Runtime Rebuild Projects should use ChatGPT Project setup.

This is integration design only. It does not activate runtime, migrate Directions, change current Workflow OS Projects, or update any current Project setup surface.

## Candidate-only boundary

This document:

- does not activate runtime;
- does not replace current Workflow OS;
- does not migrate active Directions;
- does not edit current workflow/core, workflow/policies, workflow/project_setup, workflow/project_packs, directions or docs;
- does not update Project Instructions UI;
- does not refresh Project Files/Sources;
- does not make candidate docs active authority.

## Design principles

- Project Instructions UI is compact behavior bootstrap, not documentation or state.
- Project Files/Sources are cache/context only.
- request-only sources are loaded only when a Launch Packet or admitted task needs exact context.
- GitHub/canonical repository storage wins over Project Files cache.
- Every material chat still needs Launch Packet, bounded scope, Result Packet and exact Next Move.
- Adapter output remains candidate until explicit Acceptance Decision / acceptance-update path.

## Future ChatGPT Project types

Future Direction Runtime Project:

- one ChatGPT Project per future runtime Direction after activation;
- focused on a single Direction runtime root and its current active work;
- not shared across unrelated Directions.

Runtime Console mode:

- a read-only status/navigation mode inside a Direction Runtime Project;
- optionally a separate read-only Project later if operational practice shows that separation is useful;
- not a material execution surface.

Workflow Governance Maintenance Project:

- remains a separate maintenance console for repository governance and Workflow OS maintenance;
- must not become a Direction runtime executor;
- must not mutate Direction accepted state through maintenance-console context.

## Project Instructions UI role

Future Project Instructions UI should contain only compact behavioral control:

- project mode;
- source authority rules;
- context classification;
- Launch Packet / Result Packet / exact Next Move requirements;
- Runtime Console read-only boundary;
- no hidden accepted state;
- no stale Project Files as truth;
- no schema dump or long documentation.

Instruction sources are not default Project Files/Sources.

## Project Files/Sources role

Project Files/Sources should provide orientation and current working context only.

They may include shared future runtime packs and selected Direction runtime files. They cannot prove:

- accepted state;
- latest repository content;
- successful implementation;
- acceptance;
- active runtime authority.

## Future default Project Files/Sources

The following shared packs are future-only names, not active files:

- `workflow_v3/project_packs/RUNTIME_PROJECT_SHELL_PACK.md`
- `workflow_v3/project_packs/RUNTIME_BASE_PACK.md`
- `workflow_v3/project_packs/RUNTIME_TRANSPORT_PACK.md`
- `workflow_v3/project_packs/RUNTIME_CONSOLE_QUALITY_PACK.md`

The following future Direction runtime default files may come from `directions_v3/<direction-id>/runtime/`:

- `state/DIRECTION_SPINE.md`
- `state/ACTIVE_FRONT.md`
- `state/CURRENT_STATUS.md`
- `state/CURRENT_NEXT_MOVE.md`
- `console/CONSOLE_SOURCE_INDEX.md`
- `operations/action_inbox/ACTION_INBOX.md`
- `config/DIRECTION_CUSTOMIZATION_PROFILE.md`
- `config/ADAPTER_CONTEXT_ACCESS.md`
- `config/QUALITY_GATES.md`
- `memory/MEMORY_INDEX.md`

The current Active Front bundle may be uploaded/refreshed when identified by `ACTIVE_FRONT.md`:

- `fronts/<current-active-front>/FRONT.md`
- `fronts/<current-active-front>/WORK_GRAPH.md`
- `fronts/<current-active-front>/NODES_INDEX.md`

Do not require uploading all fronts, all nodes, all raw runs or all records by default.

## Request-only sources

The following sources are request-only:

- selected node workspace: `NODE.md`, `LOCAL_CONTEXT.md`, `CONTRACTS_INDEX.md`, `RUNS_INDEX.md`, `EVIDENCE_INDEX.md`, `DECISIONS_INDEX.md`, `MEMORY_CANDIDATES_INDEX.md`;
- `SCRATCH.md`, unless explicitly needed;
- exact Work Contract records;
- exact Run records;
- exact Result Packet records;
- exact Evidence records;
- exact Acceptance Decision records;
- Memory Artifact files beyond `MEMORY_INDEX.md`;
- Handler configuration when handler behavior is being inspected;
- raw run logs and archives;
- detailed packet/schema docs when exact schema is material;
- Codex / implementation / validation capability packs;
- project setup index or installer docs for setup inspection only.

## Source authority rules

The source authority hierarchy is:

- accepted activation / migration decision controls whether future runtime is active;
- future production runtime source files control runtime rules only after activation;
- Direction accepted state lives under `directions_v3/<direction-id>/runtime/` only after activation;
- GitHub/repository exact file read at ref/branch wins over Project Files cache;
- Project Files/Sources are cache/context only;
- Chat output, Codex output, Result Packet, Project File, Signal, Handler result, Action Inbox item or document existence cannot create accepted state by itself;
- candidate docs under `workflow/candidates/workflow_runtime_rebuild/` are not active authority.

## Relation to directions_v3/<direction-id>/runtime/

The proposed runtime root stores:

- `state/`
- `fronts/`
- `records/`
- `memory/`
- `operations/`
- `archive/`
- `indexes/`
- `config/`
- `console/`

Project setup files may later live under:

- `directions_v3/<direction-id>/runtime/project_setup/`

Those files are adapter/setup surfaces, not accepted state by themselves.

## Runtime Console context access

Runtime Console reads:

- current state files;
- Console source index;
- indexes;
- Action Inbox;
- active-front bundle;
- recent evidence/records only when supplied or requested.

It may:

- summarize status;
- expose uncertainty;
- list blockers;
- produce candidate Launch Packet or Check Job text.

It must not:

- execute material work;
- mutate accepted state;
- accept evidence;
- promote Memory;
- launch Codex directly;
- silently close Action Inbox items;
- become hidden runtime controller.

## Refresh model

Refresh reporting uses these categories:

- `project_instruction_ui_update_required`
- `project_sources_files_refresh_required`
- `request_only_sources_refresh_required`
- `do_not_upload_as_project_file`

GitHub commits do not update ChatGPT Project surfaces.

If Project Instructions source changes, paste updated UI payload and report character count.

If future shared pack source changes, regenerate/refresh that uploaded Project File/Source.

If future Direction runtime default file changes, refresh that uploaded source before a dependent material run.

If request-only source changes, refresh/load it only when the admitted task depends on it.

Candidate doc changes do not trigger active Project refresh.

## Difference from current Workflow OS setup

Current Workflow OS ordinary Direction Projects use shared workflow packs plus Direction payload files.

Current Direction payload is Ledger / Obligations / Receipts index / Commit scopes / Dashboard / Migration receipt.

Future runtime setup would use Direction Spine / Active Front / Work Graph / Work Contract / Run / Evidence / Acceptance / Memory / Signals / Action Inbox / Next Move.

Current Workflow Governance Maintenance Project remains a repository maintenance console.

Future Runtime Console is not the same as Workflow Governance Maintenance Console.

Current setup remains active until a separate activation plan is accepted.

## Future production namespace proposal

Proposed future production namespaces, without creating or activating them:

- `workflow_v3/`
- `workflow_v3/project_setup/`
- `workflow_v3/project_packs/`
- `directions_v3/<direction-id>/runtime/`

Namespace correction: earlier `workflow/runtime/**` and `directions/<direction-id>/runtime/**` future-path proposals are superseded by `workflow_v3/**` and `directions_v3/<direction-id>/runtime/**`.

Current candidate documentation remains under:

- `workflow/candidates/workflow_runtime_rebuild/`

The production namespace proposal requires separate activation acceptance before use.

## Validation expectations

- file exists;
- README index includes `PROJECT_SETUP_INTEGRATION.md`;
- EOF marker exists;
- candidate-only wording is explicit;
- no active runtime files changed;
- no current Project setup files changed;
- no directions files changed.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/PROJECT_SETUP_INTEGRATION.md
