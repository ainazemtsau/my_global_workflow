# Workflow v3 Rollout Setup

status: candidate_draft

## Purpose

This document defines the candidate rollout setup model for Workflow v3.

It explains how Workflow v3 should later be set up for real use across existing Directions while preserving the current Workflow OS as legacy and rollback, and while treating old Direction state as legacy evidence only.

This is setup design for parent/integration review and later bounded implementation packages. It does not activate Workflow v3.

## Candidate-only boundary

This document is candidate documentation only. It:

- does not activate Workflow v3;
- does not replace current Workflow OS;
- does not migrate active Directions;
- does not create `workflow_v3/**`;
- does not create `directions_v3/<direction-id>/runtime/**`;
- does not update Project Instructions UI;
- does not refresh Project Files/Sources;
- does not treat old Ledger, Obligations, Receipts or other old Direction records as accepted v3 state;
- does not delete, rename, move or decommission old Workflow OS files.

The existence of this file does not create production runtime authority, Direction accepted state, Project setup authority, migration authority or decommission authority.

## Naming rule

User-facing system name is Workflow v3.

Do not use "Pilot" in user-facing ChatGPT Project names.

"Pilot" may be used only as internal rollout mode, internal file/path history or candidate evidence label.

Existing historical candidate evidence may contain "Pilot"; do not reuse that wording as a user-facing Project name.

## Workflow v3 rollout model

Workflow v3 rollout means:

- clean production namespace after activation;
- one Direction runtime root per adopted Direction;
- old Workflow OS remains legacy and rollback;
- existing Directions are not adopted automatically;
- old Direction state is legacy evidence only;
- activation, migration/import, Project setup rollout and decommission are separate decisions.

No candidate document, dry-run, branch, commit, Project File cache or chat result makes Workflow v3 active by itself.

## Future production namespace

The future production namespaces are future-only proposals:

- `workflow_v3/`
- `workflow_v3/project_setup/`
- `workflow_v3/project_packs/`
- `directions_v3/<direction-id>/runtime/`

Namespace correction: earlier `workflow/runtime/**` and `directions/<direction-id>/runtime/**` proposals are superseded. Workflow v3 uses the clean roots `workflow_v3/**` and `directions_v3/<direction-id>/runtime/**`.

Path meanings:

- `workflow_v3/` = accepted Workflow v3 runtime rules after activation;
- `workflow_v3/project_setup/` = provider/project setup templates;
- `workflow_v3/project_packs/` = generated upload/cache packs;
- `directions_v3/<direction-id>/runtime/` = accepted v3 runtime state for one adopted Direction.

Do not create any of these paths from this candidate package. They require separate activation, Project setup or per-Direction adoption packages.

## Existing Directions clean-start strategy

Default adoption mode for an existing Direction is `clean_start_v3`.

Required sequence:

1. Choose one Direction.
2. Accept an explicit per-Direction adoption decision.
3. Create a new ChatGPT Project named `Workflow v3 — <Direction Name>`.
4. Create `directions_v3/<direction-id>/runtime/` only in a later allowed package.
5. Create v3 Direction Spine, Active Front, Current Status and Current Next Move from an explicit current decision.
6. Do not import old Direction files automatically.
7. Use old files only as `legacy_evidence`.
8. Require separate evidence and Acceptance Decision for any selective import.

Clean start means the v3 runtime begins from a current explicit decision, not from invented proof state or bulk-imported old records.

## Legacy evidence strategy

Old Direction files are `legacy_evidence`, not `accepted_v3_state`.

This includes:

- old Ledger;
- old Obligations;
- old Receipts index;
- old Commit scopes;
- old Dashboard;
- old Migration receipt;
- old `project_files`;
- old `project_setup`;
- old receipts / run history.

Allowed future adoption modes:

- `clean_start`;
- `bridge_only`;
- `selective_import`;
- `full_migration` only after separate migration policy;
- `no_adoption`.

Legacy evidence may inform a current decision, but it must not silently become Workflow v3 accepted state.

## ChatGPT Project strategy

Initial rollout should create new ChatGPT Projects for Workflow v3 rather than updating old ones.

Old Projects remain legacy and rollback. Updating old Projects is allowed only as a later stable migration or cleanup decision after Workflow v3 activation, rollout evidence and rollback requirements are understood.

New Projects make source authority clearer:

- old Project = old Workflow OS / rollback context;
- new Project = Workflow v3 candidate or adopted Direction context, depending on activation and adoption decisions.

## Recommended user-facing Project names

Recommended user-facing ChatGPT Project names:

- `Workflow v3 — <Direction Name>`
- `Workflow v3 — Sandbox`
- `Workflow v3 — Rollout Test`
- `Workflow v3 Governance — Maintenance Console`

Do not add a user-facing Project name that includes "Pilot".

## Ordinary Direction Project setup

An ordinary Workflow v3 Direction Project is for one adopted Direction.

Project Instructions UI uses a compact universal Workflow v3 Direction payload. Project Instructions sources are not Project Files/Sources.

Default Project Files/Sources include future shared runtime packs and selected Direction runtime current-state files. They do not include every record, run, node, archive or old Direction file.

Ordinary Direction Projects must not become governance maintenance consoles, migration tools or hidden runtime authorities.

## Governance / Maintenance Project boundary

`Workflow v3 Governance — Maintenance Console` is a separate special Project.

It may:

- audit repository;
- inspect exact files;
- design setup;
- create Codex handoffs;
- verify Codex results.

It must not:

- run Direction runtime by default;
- mutate Direction accepted state;
- use ordinary Direction Project setup;
- load ordinary Direction runtime files by default;
- become Runtime Console for a Direction.

This Project is for repository governance and setup maintenance, not ordinary Direction execution.

## Universal vs per-Direction instructions decision

Use universal core Project Instructions for ordinary Workflow v3 Direction Projects.

Per-Direction data lives in runtime state/config files, not in separate large Project Instructions.

A thin per-Direction manifest or wrapper is allowed when it identifies the Direction, runtime root, source refs and cache/source limitations.

Direction-specific customization lives under:

- `directions_v3/<direction-id>/runtime/config/`

This keeps behavior stable across Direction Projects while keeping Direction-specific facts in repository-controlled runtime state.

## Direction-specific data location

Accepted Direction-specific Workflow v3 data belongs under:

- `directions_v3/<direction-id>/runtime/state/`
- `directions_v3/<direction-id>/runtime/fronts/`
- `directions_v3/<direction-id>/runtime/records/`
- `directions_v3/<direction-id>/runtime/memory/`
- `directions_v3/<direction-id>/runtime/operations/`
- `directions_v3/<direction-id>/runtime/indexes/`
- `directions_v3/<direction-id>/runtime/config/`
- `directions_v3/<direction-id>/runtime/console/`

These paths are future-only until activation and per-Direction adoption decisions create them through allowed packages.

Old Direction payload files remain outside this accepted v3 state root unless separately bridged or imported by accepted policy.

## Project Files/Sources model

Project Files/Sources are cache/context, not truth.

Future shared packs:

- `workflow_v3/project_packs/RUNTIME_PROJECT_SHELL_PACK.md`
- `workflow_v3/project_packs/RUNTIME_BASE_PACK.md`
- `workflow_v3/project_packs/RUNTIME_TRANSPORT_PACK.md`
- `workflow_v3/project_packs/RUNTIME_CONSOLE_QUALITY_PACK.md`

Future default Direction files:

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
- current Active Front bundle: `FRONT.md`, `WORK_GRAPH.md`, `NODES_INDEX.md`

Do not upload all records, all runs, all nodes, archives or old Direction files by default.

If Project Files/Sources conflict with an exact repository read at ref/path, the repository read wins.

## Request-only sources

Request-only sources are loaded only when a Launch Packet, Check Job, Codex package, review or human decision needs them.

Examples:

- selected node workspace files;
- exact Work Contract records;
- exact Run records;
- exact Result Packet records;
- exact Evidence records;
- exact Acceptance Decision records;
- Memory Artifact files beyond `MEMORY_INDEX.md`;
- Handler configuration;
- raw run logs;
- archives;
- old Direction files used as `legacy_evidence`;
- candidate docs used for maintenance or integration review.

Request-only sources must be named by repo/path/ref or supplied as verified excerpts. If they are stale or unverified, the Result Packet must say so.

## AI-provider portability model

ChatGPT is one adapter, not the runtime.

Equivalent setup must be possible for:

- ChatGPT;
- Codex;
- Claude Code / future code assistant;
- Deep Research / research agents;
- GitHub context access;
- human actions;
- generic future AI provider.

Minimum provider contract:

- receives Launch Packet;
- performs bounded Run;
- returns Result Packet or evidence;
- states source limitations;
- does not create Accepted State;
- does not decide acceptance, route, product meaning or scope expansion.

Provider-specific features may improve execution, but they must not change runtime authority or acceptance boundaries.

## GitHub setup instructions for new user/account/provider

New users, accounts or providers need:

- GitHub account with repo access;
- read access to `ainazemtsau/my_global_workflow`;
- write access only for providers that create branches or commits;
- exact repo/path/ref source references for every material source read;
- branch policy: `review_branch_required` by default;
- clear rule that Project Files are cache, not truth.

Exact source references should name:

- repository: `ainazemtsau/my_global_workflow`;
- ref: branch, tag or commit SHA;
- path: exact repository path;
- read status: complete, excerpted, unavailable or unverified.

If no GitHub access is available, use verified excerpts and mark limitations. The provider must not claim repository state outside supplied evidence.

Codex and other code assistants must return:

- branch;
- commit SHA when committed;
- changed files;
- validation;
- forbidden path check;
- EOF marker check;
- residual risks.

## Rollback and coexistence model

Before activation, rollback means leaving the candidate unused.

After activation, old Workflow OS remains available.

Old Projects remain rollback.

Workflow v3 Projects can be abandoned without deleting old Workflow OS.

The v3 Direction runtime root can be stopped or ignored if rollback is needed.

No rollback is credible if old Workflow OS files are deleted, renamed or destructively rewritten.

Coexistence ends only for a specific surface or Direction after accepted evidence proves that Workflow v3 covers the required behavior and rollback remains possible.

## Proposed repository files to create later

Immediate candidate file created by this package:

- `workflow/candidates/workflow_runtime_rebuild/WORKFLOW_V3_ROLLOUT_SETUP.md`

Later production files, explicitly not to create now:

- `workflow_v3/README.md`
- `workflow_v3/RUNTIME_MODEL.md`
- `workflow_v3/STORAGE_LAYOUT.md`
- `workflow_v3/PROJECT_SETUP_MODEL.md`
- `workflow_v3/ACTIVATION_POLICY.md`
- `workflow_v3/project_setup/UNIVERSAL_DIRECTION_RUNTIME_PROJECT_INSTRUCTIONS.md`
- `workflow_v3/project_setup/CHATGPT_PROJECT_SETUP.md`
- `workflow_v3/project_setup/CODEX_SETUP.md`
- `workflow_v3/project_setup/GENERIC_AI_PROVIDER_SETUP.md`
- `workflow_v3/project_setup/PROJECT_FILES_MANIFEST_TEMPLATE.md`
- `workflow_v3/project_packs/RUNTIME_PROJECT_SHELL_PACK.md`
- `workflow_v3/project_packs/RUNTIME_BASE_PACK.md`
- `workflow_v3/project_packs/RUNTIME_TRANSPORT_PACK.md`
- `workflow_v3/project_packs/RUNTIME_CONSOLE_QUALITY_PACK.md`
- `directions_v3/<direction-id>/runtime/**` only after per-Direction adoption decision.

## Exact allowed next implementation slices

Slice 1: persist this candidate rollout setup doc and README index only.

Slice 2: optional naming cleanup of older candidate docs, separate package only.

Slice 3: production `workflow_v3/` skeleton, separate activation package only.

Slice 4: one Direction runtime root, separate per-Direction adoption package only.

No slice may combine activation, migration/import, Project setup rollout and decommission unless a later package explicitly authorizes that combined scope.

## Risks and open decisions

Risks and open decisions:

- activation authority;
- first real Direction adoption choice;
- bridge/import policy;
- exact provider setup files;
- payload budgets/manifests;
- whether Runtime Console remains mode or separate Project;
- historical "Pilot" wording cleanup;
- decommission criteria for old Workflow OS.

Additional rollout risk: old Project Files or old Direction payloads may look authoritative to a provider unless the Launch Packet and Project setup classify them as cache or `legacy_evidence`.

## Validation expectations

Validation should prove:

- file exists;
- EOF marker exists;
- README indexes the file;
- candidate-only wording present;
- no production runtime paths created;
- no `directions/**` paths changed;
- no current workflow core/policy/setup/pack/transport/execution paths changed;
- no `docs/**` path changed;
- no Project setup refresh implied;
- no user-facing Project name contains "Pilot".

## Terminal outcome

ready_for_parent_review_and_codex_persistence_verification

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/WORKFLOW_V3_ROLLOUT_SETUP.md
