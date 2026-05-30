# First Pilot Direction Plan

status:
candidate_draft

## Purpose

This document defines the first safe pilot Direction for Workflow Runtime Rebuild.

It does not activate runtime, does not replace current Workflow OS, does not migrate active Directions, does not create directions/<pilot-id>/runtime/ yet, and does not update Project setup.

The plan is for parent/integration review and future bounded pilot design only. It does not start the pilot and does not make Workflow v3 active authority.

## Candidate-only boundary

- this plan is candidate documentation only;
- pilot execution is not started by this file;
- no production namespace is created;
- no current Workflow OS files are edited;
- no active Direction is migrated;
- no Project Instructions UI is updated;
- no Project Files/Sources are refreshed;
- candidate docs remain non-authoritative until future explicit acceptance.

Project setup shorthand for this plan:

- no Project Instructions UI update;
- no Project Files/Sources refresh.

## Recommended pilot model

pilot_type: new_test_direction

pilot_id: pilot-v3-sandbox

human_title: Workflow v3 Sandbox Pilot

adoption_mode: clean_start_only

existing_active_directions: no_adoption

bridge_only: not for first pilot

selective_import: forbidden for first pilot

full_migration: forbidden until separate migration policy

recommended_default: use a new synthetic but realistic test Direction, not an existing real Direction

Why this is the safest default:

- it avoids importing old accepted state;
- it avoids Project setup impact;
- it avoids active Direction migration;
- it gives rollback by simply leaving candidate unused or reverting candidate branch.

## Pilot Direction boundary

The pilot may test:

- ordinary human text normalization;
- candidate Direction Spine;
- Active Front selection;
- local Work Graph;
- first Work Contract;
- Launch Packet;
- Result Packet;
- exact Next Move;
- candidate evidence classification;
- source/scope/evidence/acceptance gates.

The pilot must not test:

- production rollout;
- global activation;
- active Direction migration;
- current Workflow OS replacement;
- Project setup rollout;
- Codex implementation beyond later candidate-doc persistence if separately authorized;
- real product implementation;
- bridge/import from old Workflow OS.

## Candidate-only pilot storage root

Future candidate-only pilot dry-run root:

```text
workflow/candidates/workflow_runtime_rebuild/pilots/pilot-v3-sandbox/
```

Rules:

- do not create this root in this persistence step;
- it may be created only by a later explicit pilot execution package;
- it is candidate evidence storage, not active runtime state;
- it must not be uploaded as active Project Files/Sources.

## Future accepted pilot runtime root

Future accepted pilot root:

```text
directions/pilot-v3-sandbox/runtime/
```

Rules:

- do not create this path now;
- it may be created only after explicit pilot-start or pilot-acceptance decision;
- it is not proof of global activation;
- all non-pilot Directions remain under current Workflow OS unless separately accepted.

What would later live under it:

- state/DIRECTION_SPINE.md
- state/ACTIVE_FRONT.md
- state/CURRENT_STATUS.md
- state/CURRENT_NEXT_MOVE.md
- fronts/AF-YYYY-MM-pilot-bootstrap/FRONT.md
- fronts/AF-YYYY-MM-pilot-bootstrap/WORK_GRAPH.md
- fronts/AF-YYYY-MM-pilot-bootstrap/NODES_INDEX.md
- fronts/AF-YYYY-MM-pilot-bootstrap/nodes/NODE-pilot-bootstrap/NODE.md
- LOCAL_CONTEXT.md
- CONTRACTS_INDEX.md
- RUNS_INDEX.md
- EVIDENCE_INDEX.md
- DECISIONS_INDEX.md
- MEMORY_CANDIDATES_INDEX.md
- records/contracts/
- records/runs/
- records/result_packets/
- records/evidence/
- records/acceptance/
- memory/
- operations/signals/
- operations/action_inbox/
- operations/recovery/
- indexes/
- config/
- console/

## Pilot Work Graph seed

Active Front:

AF-001 — Pilot bootstrap and first bounded run

Nodes:

1. NODE-001-boundary-confirmation
   Confirms clean-start, candidate-only, no migration, no Project setup changes.
2. NODE-002-direction-spine-draft
   Normalizes ordinary human text into candidate Direction Spine.
3. NODE-003-active-front-selection
   Selects one small Active Front and states out-of-scope boundaries.
4. NODE-004-local-work-graph-seed
   Creates local Work Graph with nearby nodes only, not global roadmap.
5. NODE-005-first-work-contract-launch-packet
   Produces first Work Contract and Launch Packet for a Work Chat.
6. NODE-006-result-packet-and-acceptance-review
   Verifies the Work Chat result remains candidate and closes with exact Next Move.

## First Work Contract

work_contract_id:
WC-PILOT-V3-001-bootstrap-direction-spine-front-graph

target:
Produce the candidate Direction Spine, Active Front, local Work Graph seed, and next Work Contract for pilot-v3-sandbox.

in_scope:

- candidate-only runtime pilot bootstrap
- clean-start Direction model
- Direction Spine
- Active Front
- local Work Graph seed
- first Work Contract
- Launch Packet
- Result Packet closure

out_of_scope:

- repository mutation during pilot Work Chat
- Project setup changes
- active Directions
- migration
- bridge/import
- Codex launch
- current Workflow OS replacement
- production activation

evidence_required:

- candidate Direction Spine present
- Active Front present
- local Work Graph seed present
- source limitations stated
- candidate-state notice present
- exact Next Move present
- no hidden accepted-state mutation

## First Launch Packet

Note: The parent/integration chat must supply the current candidate baseline ref when launching the dry-run. The sample must not be treated as a fixed source ref.

```text
LAUNCH PACKET

target:
Bootstrap pilot-v3-sandbox as a clean-start Workflow v3 test Direction.

why_now:
Test whether Workflow Runtime Rebuild can take ordinary human input through Direction Spine, Active Front, Work Graph, Work Contract, Result Packet and exact Next Move without activating runtime or migrating active Directions.

source_refs:
repo: ainazemtsau/my_global_workflow
ref: <current candidate baseline ref supplied by parent/integration review>
candidate_path: workflow/candidates/workflow_runtime_rebuild/

context_included:
Candidate runtime docs are the design baseline.
No active Direction payload is supplied.
No existing Direction state is imported.

pilot_input:
"I want a safe sandbox pilot to test Workflow v3 on a small realistic long-project scenario. It should prove that the runtime can keep work bounded between chats without migrating any active Direction."

in_scope:

- normalize pilot input into candidate Direction idea
- draft candidate Direction Spine
- select one Active Front
- create local Work Graph seed
- define next Work Contract
- close with Result Packet and exact Next Move

out_of_scope:

- accepting pilot as active state
- creating directions/pilot-v3-sandbox/runtime/
- creating candidate pilot storage root
- editing repository files
- launching Codex
- updating Project Instructions UI
- refreshing Project Files/Sources
- migrating or reading active Directions
- replacing current Workflow OS

expected_result:
Candidate pilot bootstrap packet containing Direction Spine, Active Front, local Work Graph seed, first Work Contract, Result Packet, and exact Next Move.

evidence_required:

- source authority classification
- candidate-state notice
- explicit not-done list
- limitations and assumptions
- no-activation/no-migration/no-Project-setup-change statement

return_to:
Parent / integration review for Workflow Runtime Rebuild.

blocked_if:

- required candidate baseline files cannot be read
- the task starts depending on active Direction state
- user asks to migrate an active Direction
- Project setup update becomes necessary
- runtime activation becomes implied

must_not_decide:

- pilot acceptance
- global activation
- Workflow OS replacement
- migration/import policy
- Project setup rollout
```

## Acceptance criteria

- new test Direction selected, not existing real Direction;
- clean start only;
- all pilot planning remains under candidate package;
- directions/pilot-v3-sandbox/runtime/ is future-only;
- Project setup remains untouched;
- active Workflow OS remains untouched;
- active Directions remain untouched;
- Work Graph seed and first Work Contract exist;
- Launch Packet is copy-pasteable;
- Result Packet requirements are explicit;
- rollback criteria are defined;
- evidence requirements are defined;
- exact Next Move is defined.

## Rollback criteria

Rollback triggers:

- any forbidden path changed;
- directions/** created or edited;
- current Workflow OS files changed;
- Project setup update implied;
- Project Files/Sources refresh implied;
- bridge/import/migration started;
- candidate output treated as accepted production state;
- Codex result lacks validation evidence;
- pilot attempts to replace current Workflow OS.

Rollback action:

- reject the pilot result;
- revert candidate branch if forbidden paths changed;
- leave candidate unused if no execution happened;
- require a new bounded repair package before any further pilot work.

## Evidence required before pilot acceptance

- full list of files changed;
- proof all changed files are allowed;
- EOF marker check for markdown;
- source/read limitations;
- Result Packet from pilot Work Chat;
- candidate Direction Spine;
- Active Front;
- Work Graph seed;
- first Work Contract;
- Launch Packet;
- exact Next Move;
- no Project setup refresh required;
- no active Direction touched;
- human/parent acceptance decision if pilot proceeds.

## Project setup constraints

- no Project Instructions UI update;
- no Project Files/Sources refresh;
- no request-only source refresh unless later explicitly requested as evidence;
- candidate docs must not be uploaded as active Project Files/Sources;
- no Project setup manifests changed;
- if future Project setup changes become necessary, they require separate accepted package with payload counts and refresh categories.

## What must not be touched

- workflow/core/**
- workflow/policies/**
- workflow/project_setup/**
- workflow/project_packs/**
- workflow/transport/**
- workflow/execution/**
- directions/**
- docs/**
- current Project Instructions UI
- current Project Files/Sources
- current Workflow OS runtime files
- active Direction payload files
- old clean_runtime candidate

## Risks and open decisions

Risks:

- candidate docs mistaken for active authority;
- synthetic pilot too shallow;
- accidental Project setup update;
- accidental directions/<pilot-id>/runtime/ creation;
- Action Inbox becomes backlog;
- Runtime Console becomes hidden controller;
- clean-start pass does not prove migration.

Open decisions:

- exact pilot domain text;
- whether later pilot execution writes candidate evidence under pilots/pilot-v3-sandbox/;
- pilot acceptance authority;
- whether successful pilot leads to activation planning or another pilot;
- future Project setup package remains separate.

## Terminal outcome

ready_for_parent_review_and_codex_persistence_only

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/FIRST_PILOT_DIRECTION_PLAN.md
