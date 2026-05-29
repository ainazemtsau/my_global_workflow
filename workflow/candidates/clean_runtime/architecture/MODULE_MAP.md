---
artifact:
  id: CWR-MODULE-MAP-001
  title: Clean Workflow Runtime Module Map
  type: module_map
  status: candidate
  owner_module: architecture_canon
  scope: global_runtime_architecture
  version: 0.1
---

# Clean Workflow Runtime Module Map

## Purpose

This file defines candidate Clean Workflow Runtime module boundaries, state surface ownership, mutation paths, dependencies, and module design acceptance criteria.

A module is a bounded context with one primary responsibility and one owned state surface family. A module is not a folder, prompt, technology, or chat.

One mutable state surface has exactly one owner module. Other modules may read, emit events, return reports, or propose patches. Other modules may not directly mutate non-owned state surfaces.

## Module Purpose Table

| Module | Purpose |
|---|---|
| M0 Architecture Canon | Owns architecture vocabulary, primitive/domain/adapter classification, module boundaries, dependency rules, and invariant catalog. |
| M1 Runtime Kernel | Owns accepted transition law, Work Contract lifecycle, Evidence semantics, validation semantics, and Acceptance Decision legality. |
| M2 Direction Control | Owns root result, success conditions, global spine, tracks, direction-level refs, and coarse route state. |
| M3 Active Front | Owns primary, support, watch, parked, and blocked active work surfaces. |
| M4 Work Graph / Node Model | Owns node registry, node status, local maps, dependency edges, readiness, and completion criteria. |
| M5 Runtime Roles / Operator Registry | Owns role taxonomy, capability registry, adapter bindings, role constraints, and substitution policy. |
| M6 Orchestration / Continuation | Owns continuation packets, launch packets, return packets, parent recovery blocks, and run routing records. |
| M7 Memory System | Owns shared memory index, memory artifact status, decision memory, promotion records, and supersession records. |
| M8 Documentation / Artifact System | Owns artifact taxonomy, frontmatter policy, canonical ref policy, generated-doc policy, and archive policy. |
| M9 Event System | Owns event journal, event schemas, subscription registry, and reaction queue creation rules. |
| M10 Review / Patch / Integration | Owns review jobs, review queue, patch proposals, integration decisions, and integration receipts. |
| M11 Parallel Work / Child Runs | Owns child run registry, conflict policy, missing child policy, parent recovery block, and integration order. |
| M12 Execution Gateway | Owns execution readiness, target binding, validation plans, execution receipts, validation receipts, and executor adapter contracts. |
| M13 Legacy Import | Owns legacy index, import candidates, classification records, mapping records, import decisions, and rejected import records. |
| M14 Human Interaction Model | Owns human-facing console views, human decision prompts, input normalization records, and approval/challenge records. |
| M15 Evaluation / Invariant Test Suite | Owns invariant tests, transcript tests, module boundary tests, anti-pattern catalog, and eval results. |

## Ownership Table

| State surface | Owner module | Includes |
|---|---|---|
| Architecture state surface | M0 Architecture Canon | Canonical terminology, module map, dependency rules, invariant catalog, no-duplication policy, hidden-state-change policy. |
| Accepted transition surface | M1 Runtime Kernel | Accepted/candidate distinction, Work Contract lifecycle, Evidence semantics, validation semantics, Acceptance Decision semantics, invariant gate. |
| Direction control surface | M2 Direction Control | Direction id, root result, success conditions, global spine, tracks, direction-level refs, high-level blocked/watch/parked states. |
| Active front surface | M3 Active Front | Primary active work, support work, watch, parked, blocked, selected front rationale. |
| Work graph surface | M4 Work Graph / Node Model | Node registry, node status, dependency edges, local work maps, ready/locked/blocked computation, completion criteria. |
| Role registry surface | M5 Runtime Roles / Operator Registry | Runtime roles, capability declarations, adapter bindings, role constraints, substitution policy. |
| Orchestration surface | M6 Orchestration / Continuation | Continuation packets, launch packets, result return packets, parent recovery blocks, run routing records. |
| Memory surface | M7 Memory System | Shared memory index, memory artifact status, promotion records, decision memory, supersession records, confidence/review status. |
| Documentation / artifact surface | M8 Documentation / Artifact System | Artifact type taxonomy, required metadata, canonical ref policy, generated projection policy, archive policy. |
| Event surface | M9 Event System | Event journal, event status, event type registry, subscription registry, reaction queue creation rules. |
| Review / patch surface | M10 Review / Patch / Integration | Review jobs, review queue, patch proposals, integration decisions, integration receipts. |
| Parallel work surface | M11 Parallel Work / Child Runs | Child run registry, parent recovery block, conflict policy, missing child policy, integration order. |
| Execution surface | M12 Execution Gateway | Execution-ready status, target binding, validation plan, execution handoff, execution receipt, validation receipt, executor adapter contract. |
| Legacy import surface | M13 Legacy Import | Legacy artifact inventory, import candidate records, mapping records, rejected import records, accepted import records. |
| Human interaction surface | M14 Human Interaction Model | Human-facing summaries, human decision prompts, normalized human input records, human approval/challenge records. |
| Evaluation surface | M15 Evaluation / Invariant Test Suite | Invariant tests, boundary tests, transcript audit tests, anti-pattern catalog, failing examples, passing examples. |

## State Surface Mutation Table

| State surface | Owner / mutator | Other modules may do | Forbidden |
|---|---|---|---|
| Architecture vocabulary | M0 Architecture Canon | Propose architecture patch. | Redefine terms locally. |
| Accepted transition law | M1 Runtime Kernel | Report invariant issue. | Bypass acceptance. |
| Root result / success conditions / global spine | M2 Direction Control | Propose direction patch. | Mutate from review or event directly. |
| Active primary/support/watch/parked/blocked | M3 Active Front | Propose route/front patch. | Expand into full roadmap. |
| Node registry / local maps / dependencies | M4 Work Graph / Node Model | Propose node patch. | Edit node state directly from other modules. |
| Role taxonomy / adapter bindings | M5 Runtime Roles / Operator Registry | Propose capability update. | Hard-code tools into core. |
| Continuation / launch / return packets | M6 Orchestration / Continuation | Request launch or integration. | Treat packets as accepted truth. |
| Shared memory / decisions / promotion | M7 Memory System | Propose promotion candidate. | Treat arbitrary node internals as shared memory. |
| Artifact types / refs / docs policy | M8 Documentation / Artifact System | Propose artifact policy patch. | Treat documents as progress by existence. |
| Event journal / subscriptions | M9 Event System | Emit events. | Let an event directly change state. |
| Review queue / patches / integration decisions | M10 Review / Patch / Integration | Submit review result. | Let reviewer self-apply patch. |
| Child runs / parent recovery | M11 Parallel Work / Child Runs | Request child run. | Run parallel work without parent contract. |
| Execution readiness / validation / receipts | M12 Execution Gateway | Request execution route. | Run Codex/product execution without gates. |
| Legacy import index / mappings | M13 Legacy Import | Submit legacy evidence. | Treat legacy as authority by existence. |
| Human decision prompts / normalized input | M14 Human Interaction Model | Ask for human decision. | Infer hidden acceptance. |
| Evals / invariant tests | M15 Evaluation / Invariant Test Suite | Report defects. | Let eval mutate runtime state. |

## Dependency Graph

```text
M0 Architecture Canon
  -> M1 Runtime Kernel
    -> M2 Direction Control
    -> M3 Active Front
    -> M4 Work Graph / Node Model
    -> M5 Runtime Roles / Operator Registry
      -> M6 Orchestration / Continuation
        -> M7 Memory System
        -> M8 Documentation / Artifact System
        -> M9 Event System
        -> M10 Review / Patch / Integration
        -> M11 Parallel Work / Child Runs
        -> M12 Execution Gateway
        -> M13 Legacy Import
        -> M14 Human Interaction Model
        -> M15 Evaluation / Invariant Test Suite
```

Precise dependency constraints:

- M1 depends on M0 only.
- M2-M4 depend on M0-M1.
- M5 depends on M0-M1 and remains adapter-neutral.
- M6 depends on M1-M5.
- M7-M10 depend on M1-M6 as needed.
- M11 depends on M3-M6 and M10.
- M12 depends on M1, M4, M5, M6, and M10.
- M13 depends on M0, M1, M7, M8, and M10.
- M14 depends on read models from M2-M13.
- M15 depends on contracts from all modules but does not mutate them.
- Adapters depend on M5, M6, and M12 contracts, never the reverse.

## Module Design Acceptance Checklist

A module design is acceptable only if it declares:

- owned state surface;
- non-owned state surfaces it reads;
- commands it accepts;
- events it emits;
- result reports it consumes or produces;
- patch proposals it may create;
- exact surfaces it is forbidden to mutate;
- invariants it must respect;
- adapter-neutral role assumptions;
- open questions.

END_OF_FILE: workflow/candidates/clean_runtime/architecture/MODULE_MAP.md
