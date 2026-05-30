# Storage Layout

status:
  candidate_draft

## Purpose

This file defines a candidate future runtime state storage layout for Workflow Runtime Rebuild.

It describes where future runtime state would live if this candidate is later accepted, activated, and given an explicit migration or non-migration policy. It is not documentation storage, and it is not a live storage plan for the current Workflow OS.

The design is optimized for Directions that may run for years or decades. It separates small current-state surfaces from long-term historical records, node-local workspaces, indexes, archive surfaces, and read-only Runtime Console source data.

## Candidate-only boundary

This candidate storage layout:

- does not activate runtime;
- does not replace current Workflow OS;
- does not migrate active Directions;
- does not update Project Instructions;
- does not refresh Project Files/Sources;
- does not create accepted runtime authority.

The existence of this file does not make the proposed layout active. Any use of the layout would require a separate accepted decision for activation, migration or non-migration, repository authority, and operating rules.

## Core storage principles

- Canonical storage must live in repository-controlled files, not chat memory.
- GitHub/repository authority is the durable proof surface for accepted runtime state.
- Project Files are cache/context only for ChatGPT or related tools; they are not canonical state and not acceptance authority.
- Candidate docs describe possible runtime designs; accepted runtime state requires an Acceptance Decision and an accepted update path.
- Human-readable markdown comes first so the runtime can be audited directly; machine-readable yaml/json can be added later only where it solves a real automation or indexing need.
- Current snapshots and append-only or versioned historical records must coexist: current files answer "what resumes now," while records preserve "what happened and why."
- No accepted state can be created merely from chat output, Codex output, document existence, Signal, Handler result, Action Inbox item, Project Files, or raw run logs.

## Proposed future active storage root

Preferred future active storage root:

```text
directions/<direction-id>/runtime/
```

This is a proposed future runtime state root. It is not active now.

Use of `directions/<direction-id>/runtime/` requires separate activation, migration or non-migration acceptance before any Direction writes runtime state there.

## Top-level future layout

Proposed future layout:

```text
directions/<direction-id>/runtime/

  state/
    DIRECTION_SPINE.md
    ACTIVE_FRONT.md
    CURRENT_STATUS.md
    CURRENT_NEXT_MOVE.md

  fronts/
    AF-YYYY-MM-slug/
      FRONT.md
      WORK_GRAPH.md
      NODES_INDEX.md

      nodes/
        NODE-slug/
          NODE.md
          LOCAL_CONTEXT.md
          SCRATCH.md
          CONTRACTS_INDEX.md
          RUNS_INDEX.md
          EVIDENCE_INDEX.md
          DECISIONS_INDEX.md
          MEMORY_CANDIDATES_INDEX.md
          closure/
            NODE_CLOSURE_SUMMARY.md

  records/
    contracts/
      YYYY/
        MM/
          WC-YYYY-MM-DD-slug.md
    runs/
      YYYY/
        MM/
          RUN-YYYY-MM-DD-slug.md
    result_packets/
      YYYY/
        MM/
          RP-YYYY-MM-DD-slug.md
    evidence/
      YYYY/
        MM/
          EV-YYYY-MM-DD-slug.md
    acceptance/
      YYYY/
        MM/
          AD-YYYY-MM-DD-slug.md

  memory/
    candidates/
    artifacts/
    MEMORY_INDEX.md

  operations/
    signals/
      YYYY/
        MM/
          SIGNALS-YYYY-MM.md
    action_inbox/
      ACTION_INBOX.md
      CLOSED_ACTIONS.md
    recovery/
      YYYY/
        MM/

  archive/
    fronts/
    nodes/
    records/

  indexes/
    FRONTS_INDEX.md
    NODES_INDEX.md
    RUNS_INDEX.md
    EVIDENCE_INDEX.md
    ACCEPTANCE_INDEX.md
    MEMORY_INDEX.md

  config/
    DIRECTION_CUSTOMIZATION_PROFILE.md
    HANDLERS.md
    ADAPTER_CONTEXT_ACCESS.md
    QUALITY_GATES.md

  console/
    CONSOLE_SOURCE_INDEX.md
```

The layout keeps resume-critical state small, keeps active work close to its node, and moves long-term proof into date-partitioned records with indexes by front, node, date, and entity type.

## Storage tiers

- Tier 0 Current State: small files needed to resume now, including spine, active front, current status, and current next move.
- Tier 1 Accepted Decisions: decisions that changed accepted state, stored as dated Acceptance Decision records and referenced by indexes.
- Tier 2 Evidence / Result Packets: proof supporting decisions, including Result Packets and evidence records.
- Tier 3 Node-local Context: useful context inside one node/front, including NODE.md, LOCAL_CONTEXT.md, local indexes, and closure summaries.
- Tier 4 Raw Runs / Logs: long-term execution history, rarely read directly except for audit, recovery, or disputed proof.
- Tier 5 Scratch / Temporary Notes: disposable working notes unless promoted through explicit review.

## Node-local storage model

Every active Work Graph node needs a node-local workspace because long-running Directions cannot safely keep all working context in global files or chat memory. The node workspace keeps the node goal, local assumptions, relevant references, and local record indexes near the work while preserving the difference between working context and accepted state.

- `NODE.md`: defines the node purpose, relation to the Active Front, target result, boundaries, dependencies, status, and closure condition.
- `LOCAL_CONTEXT.md`: holds local working context for this node only. It is not accepted state and must not silently mutate the Direction Spine, Active Front, Work Graph, or accepted decisions.
- `SCRATCH.md`: holds temporary notes, sketches, partial observations, and working fragments. It may be deleted, compacted, or promoted.
- `*_INDEX.md` files: reference records stored under `records/`, including contracts, runs, evidence, decisions, and memory candidates.
- `NODE_CLOSURE_SUMMARY.md`: final compact summary after closure, including result, accepted changes, rejected paths, evidence links, unresolved blockers, and follow-up references.

If scratch or local context begins to affect future decisions, it must be promoted to one of:

- Evidence;
- Memory Candidate;
- Acceptance Decision;
- updated node context through explicit review.

## Long-term run history model

A flat global `runs/` directory is not enough for Directions that run for years or decades. Runtime state storage needs date partitioning, local indexes, global indexes, and archive rules.

Required design:

- `records/runs/YYYY/MM/` stores raw Run records.
- Per-node `RUNS_INDEX.md` files provide node-level lookup.
- `indexes/RUNS_INDEX.md` provides global lookup across the Direction.
- An optional future machine-readable index may be added if markdown indexes become too expensive or ambiguous.
- Old runs should not be deleted merely because they are old.
- Closed or superseded runs can be archived or compacted with references preserved.

Raw Run records should be kept as durable history, but the normal resume path should read current-state files, node indexes, closure summaries, and accepted decisions before reading raw logs.

## Archive and compaction model

Archive and compaction exist to keep active runtime state readable without erasing proof.

- Closure summaries compact the result of a node or front after review.
- Archived fronts move closed Active Front material out of the active work surface while preserving references.
- Archived nodes move closed node workspaces under archive when their closure summaries, indexes, and linked records are complete.
- Superseded records may be marked superseded, moved under archive, or replaced by summary records only when references preserve the original proof path.
- Accepted decisions and evidence links must remain reachable from active or archived indexes.
- Old raw runs can be summarized when they are closed, superseded, or rarely needed for normal operation, and when their evidence, decisions, final state transitions, and unresolved blockers are preserved.

What must never be lost:

- accepted decisions;
- evidence references;
- final state transitions;
- unresolved blockers.

Compaction must not hide a weak decision trail. If a compacted item supported accepted state, the summary must link to the retained evidence, Acceptance Decision, or archived source.

## Entity-to-storage mapping

| Entity | Future runtime state storage |
| --- | --- |
| Direction Spine | `state/DIRECTION_SPINE.md` |
| Active Front | `state/ACTIVE_FRONT.md`, `fronts/AF-YYYY-MM-slug/FRONT.md`, `indexes/FRONTS_INDEX.md` |
| Work Graph | `fronts/AF-YYYY-MM-slug/WORK_GRAPH.md` and front/node indexes |
| Work Contract | `records/contracts/YYYY/MM/WC-YYYY-MM-DD-slug.md` and node `CONTRACTS_INDEX.md` |
| Run record | `records/runs/YYYY/MM/RUN-YYYY-MM-DD-slug.md`, node `RUNS_INDEX.md`, and `indexes/RUNS_INDEX.md` |
| Result Packet / Evidence | `records/result_packets/YYYY/MM/`, `records/evidence/YYYY/MM/`, node `EVIDENCE_INDEX.md`, and `indexes/EVIDENCE_INDEX.md` |
| Acceptance Decision | `records/acceptance/YYYY/MM/AD-YYYY-MM-DD-slug.md`, node `DECISIONS_INDEX.md`, and `indexes/ACCEPTANCE_INDEX.md` |
| Memory Candidate | `memory/candidates/`, node `MEMORY_CANDIDATES_INDEX.md`, and `indexes/MEMORY_INDEX.md` |
| Memory Artifact | `memory/artifacts/` and `memory/MEMORY_INDEX.md` |
| Signal / Run Log | `operations/signals/YYYY/MM/SIGNALS-YYYY-MM.md` and run records where material execution happened |
| Handler configuration | `config/HANDLERS.md` |
| Action Inbox | `operations/action_inbox/ACTION_INBOX.md` and `operations/action_inbox/CLOSED_ACTIONS.md` |
| Direction Customization Profile | `config/DIRECTION_CUSTOMIZATION_PROFILE.md` |
| Runtime Console source data | `console/CONSOLE_SOURCE_INDEX.md`, current state files, indexes, records, and logs as read-only source data |
| Adapter setup/context access references | `config/ADAPTER_CONTEXT_ACCESS.md` |
| quality gates / failure recovery records | `config/QUALITY_GATES.md` and `operations/recovery/YYYY/MM/` |

## Read/write ownership

- ChatGPT design output may draft candidate text and packets only.
- Codex may write only allowed paths through a bounded package.
- Acceptance Decision is required for accepted-state mutation.
- Runtime Console is read-only.
- Handler output creates candidates only.
- Action Inbox item cannot auto-run.
- Memory requires promotion before it can become a Memory Artifact or accepted runtime context.

Runtime Console reads state, indexes, and logs. It must not become an execution controller, hidden decision engine, or alternate acceptance path.

## Lifecycle flows

- Material chat result -> Result Packet -> candidate evidence.
- Evidence -> review -> Acceptance Decision -> accepted state update.
- Memory Candidate -> promotion -> Memory Artifact.
- Signal -> Handler -> Action Inbox candidate, without state mutation.
- Action Inbox item -> selected -> Launch Packet / Check Job / Codex Work Package / Human Decision Request.
- Runtime Console reads state/indexes/logs and does not execute work.

These flows preserve the difference between candidate material, evidence, decisions, active state, and operational prompts.

## Project Files cache boundary

Project Files/Sources may mirror or cache selected files for ChatGPT context, but they are not canonical state, not latest repository proof, and not acceptance authority.

Project Files are cache/context only. A stale Project File cannot override repository state, create accepted state, or prove that a runtime transition happened.

## Open decisions

- Exact future active path still requires activation/migration policy.
- Markdown vs yaml/json split.
- One-file vs multi-file records.
- Retention/compaction policy.
- Generated console views.
- Concurrency/locking.
- Binary evidence or attachments.
- Migration/non-migration relation to current Workflow OS.

## Risks

- Storage can become too heavy.
- Action Inbox can become trash bin.
- Local node context can become hidden state.
- Raw runs can become unreadable at scale.
- Console can become hidden controller.
- Candidate docs can be mistaken for active runtime authority.
- Archive/compaction can hide evidence if rules are weak.

## Validation expectations

- File exists.
- EOF marker is present.
- Candidate-only wording is explicit.
- No active runtime edits.
- No Project setup edits.
- No directions edits.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/STORAGE_LAYOUT.md
