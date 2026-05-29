---
artifact:
  id: CWR-ARCHITECTURE-CANON-001
  title: Clean Workflow Runtime Architecture Canon
  type: architecture_canon
  status: candidate
  owner_module: architecture_canon
  scope: global_runtime_architecture
  version: 0.1
---

# Clean Workflow Runtime Architecture Canon

## Purpose

Module 0 defines the candidate architecture boundary for Clean Workflow Runtime. It exists to stabilize vocabulary, semantic primitives, domain boundaries, adapter boundaries, state-surface ownership, dependency rules, and invariants before any later module design.

Clean Workflow Runtime is not active runtime authority. It does not replace the current Workflow OS, does not mutate current Project setup or packs, and does not activate new execution protocols.

## Architecture Rule

The architecture follows a ports-and-adapters boundary. Core and domain modules define runtime meaning. Adapters implement roles through current or future technologies.

Core must not depend on tool names. Tool adapters must obey core and domain contracts.

ChatGPT, Codex, Claude Code, Deep Research, GitHub, and future agents are adapters / role implementations, not core primitives. Runtime roles are technology-neutral. Adapters may execute contracts and return evidence, but may not redefine runtime semantics.

## Layer Model

Clean Workflow Runtime has six candidate architecture layers:

| Layer | Responsibility |
|---|---|
| Architecture Canon Layer | Owns vocabulary, module boundaries, dependency rules, state-surface ownership rules, and invariants. |
| Runtime Kernel Layer | Owns accepted-state transition law and the contract-run-evidence-acceptance path. |
| Domain Module Layer | Owns bounded runtime surfaces such as Direction Control, Active Front, Work Graph, Memory, Events, Review/Patch, Execution Gateway, and Legacy Import. |
| Orchestration Layer | Owns launch, continuation, return, child-run routing, and parent recovery contracts. |
| Storage / Source-of-Truth Layer | Persists accepted state, candidates, evidence, refs, indexes, artifacts, and generated projections according to owner-module rules. |
| Adapter Layer | Implements roles using chats, coding agents, research agents, repositories, local devices, APIs, CI, browsers, or manual human action. |

Storage does not create truth by existence. It persists state according to accepted ownership and transition rules.

## Semantic Primitives

Semantic primitives are the minimum concepts without which the runtime cannot function.

| Primitive | Meaning | Legacy mapping |
|---|---|---|
| Accepted State | The currently accepted runtime state. It is not inferred from chat history, loose documents, dashboards, generated summaries, or tool output. | Ledger -> Accepted State |
| Work Contract | A bounded statement of work with target, intended result, scope, non-scope, allowed inputs, allowed actions, forbidden actions, expected outputs, evidence required, validation requirements, and return contract. | Obligation -> Work Contract |
| Run | One bounded execution of a Work Contract by a Runtime Role. | Operator -> Run |
| Evidence | Produced material supporting a candidate result, such as result reports, diffs, validation output, research sources, decision records, screenshots, test logs, artifact refs, or human confirmations. | Receipt -> Evidence / Acceptance Candidate |
| Acceptance Decision | A decision that accepts, rejects, modifies, blocks, or requests more evidence for a candidate result. | Verify + Commit -> Acceptance Decision / Accepted Transition |
| Invariant | A non-negotiable rule that valid runtime movement cannot violate. | Invariant -> Invariant |

Accepted State changes only through a valid accepted transition.

## Non-Primitives

These are not semantic primitives:

- ChatGPT
- Codex
- Claude Code
- Deep Research
- GitHub
- repository
- file
- document
- dashboard
- roadmap
- plan
- stage
- layer
- prompt
- schema
- pack
- Project Instructions UI
- event
- patch
- memory artifact
- node
- direction
- active front
- execution

They may be domain concepts, transport formats, storage surfaces, generated views, artifacts, or adapters, but they are not the irreducible kernel of the runtime.

## Domain Concepts

Domain concepts are meaningful runtime objects built on top of semantic primitives. They must not bypass the Runtime Kernel.

Primary domain concepts include Direction, Root Result, Success Conditions, Global Spine, Track, Active Front, Work Graph, Node, Composite Node, Executable Node, Local Work Map, Result Report, Node Closeout, Memory Artifact, Shared Memory, Decision Record, Event, Event Subscription, Review Job, Patch Proposal, Parent Integration Review, Continuation Packet, Child Work Packet, Parent Recovery Block, Execution Gateway, Legacy Import Candidate, Human Decision Record, and Validation Report.

## Adapter / Technology Concepts

Adapter concepts implement roles or storage and do not define runtime semantics.

Examples include ChatGPT, Codex, Claude Code, Deep Research, OpenAI Agents SDK, GitHub, local filesystem, CI runner, browser, spreadsheet, issue tracker, local terminal, manual human action, and future autonomous agent API.

Correct: CodeExecutor may be implemented by Codex.

Incorrect: Codex owns execution.

## State Surface Ownership

Every mutable state surface must have exactly one owner module. Other modules may read the surface through declared queries or propose changes through declared patch or result contracts.

General rule:

```text
one state surface -> one owner module -> declared mutation commands
```

Cross-module change rule:

```text
read -> propose -> integrate -> accept -> persist
```

Direct mutation of another module's owned surface is forbidden.

## Cross-Module Communication

Modules communicate through declared contract types only:

| Contract type | Meaning |
|---|---|
| Query | A read-only request for current or historical state. Queries must not mutate state. |
| Command | An intent to mutate a state surface owned by the receiving module. |
| Event | A recorded fact that something happened. Events do not mutate state directly. |
| Result Report | A bounded run return object describing what happened, what was produced, evidence, changes, blockers, and claimed parent impact. |
| Patch Proposal | A proposed change to a state surface. Patch proposals do not apply themselves. |
| Integration Decision | A decision by the responsible integration authority to accept, reject, modify, block, or request more evidence for a patch or result. |
| Artifact Ref | A reference to canonical content, used to prevent duplication of canonical facts. |

## Dependency Rules

Adapters depend on orchestration, domain, and kernel contracts. The kernel never depends on adapters.

The inward dependency direction is:

```text
Adapter -> Orchestration -> Domain -> Kernel -> Architecture Canon
```

The Runtime Kernel must not mention ChatGPT, Codex, Claude Code, GitHub, Deep Research, project files, or product repositories. Each domain module owns one bounded state surface family. Events may trigger review queue items, patch proposals, closeout checks, or escalation requests, but events may not directly alter Direction Control, Active Front, Work Graph, Memory, Execution, or Legacy state.

Review jobs propose; parent/integration accepts. Only accepted integration can mutate accepted parent state. Adapter replacement must not require changing semantic primitives or domain definitions.

## Duplication Policy

Every canonical fact must have one owner artifact or state surface. Other artifacts should reference it by id, path, or ref instead of duplicating it.

Packets, dashboards, prompts, indexes, and generated summaries should carry refs plus short summaries, not full copies of canonical artifacts. Generated projections must include source refs, generated_at, generator module, freshness condition, and non-authority notice.

When a canonical artifact is replaced, the old artifact is marked superseded and points to the new artifact. Both cannot be simultaneously active for the same canonical fact.

Detailed workflow rules, schemas, and architecture documentation must not live in Project Instructions UI. Project Instructions UI may contain compact behavioral bootstrap only.

## Hidden State Change Prevention

Hidden state change is any accepted-state mutation not represented through explicit contract, evidence, validation, and acceptance. Hidden state changes are forbidden.

Examples include treating a chat conclusion as accepted state, treating a document as accepted because it exists, changing Active Front inside a review without patch/integration, promoting node output to shared memory without a promotion decision, treating a Codex result as done without validation evidence, treating a legacy artifact as current authority, treating user examples as binding requirements without explicit decision, or allowing event subscription to modify state directly.

All state-changing outputs must declare target surface, owner module, change kind, evidence, validation or acceptance rule, resulting status, and rollback/reopen condition when relevant.

## Architecture Invariants

| ID | Name | Rule |
|---|---|---|
| CWR-INV-001 | accepted_state_requires_transition | Accepted State changes only through a valid accepted transition. |
| CWR-INV-002 | one_state_surface_one_owner | Every mutable state surface has exactly one owner module. |
| CWR-INV-003 | no_adapter_as_core | Tools and technologies are adapters, not semantic primitives or domain owners. |
| CWR-INV-004 | no_chat_memory_as_state | Chat history is not accepted state. |
| CWR-INV-005 | no_document_as_progress | A document is progress only if it delivers, decides, unlocks, validates, preserves evidence, removes a blocker, or updates accepted route/control state. |
| CWR-INV-006 | no_event_mutation | Events record facts and trigger proposed reactions; they do not mutate accepted state. |
| CWR-INV-007 | review_proposes_integration_accepts | Review jobs propose changes; integration accepts or rejects them. |
| CWR-INV-008 | no_cross_node_internal_read | Nodes consume shared memory, parent contracts, allowed upstream results, and explicit evidence refs; they do not inspect arbitrary sibling internals. |
| CWR-INV-009 | shared_memory_requires_promotion | Node outputs become reusable shared memory only after promotion decision. |
| CWR-INV-010 | no_execution_without_gateway | Execution requires target binding, execution-ready contract, validation plan, execution result, validation evidence, and accepted completion. |
| CWR-INV-011 | no_parallel_without_parent_contract | Parallel child work requires parent contract, conflict policy, return contract, and integration plan. |
| CWR-INV-012 | no_legacy_authority | Legacy artifacts are evidence only until explicitly imported. |
| CWR-INV-013 | no_duplicate_canonical_truth | Canonical facts must not be duplicated across owner surfaces. |
| CWR-INV-014 | human_decisions_are_explicit | Human-owned decisions must be explicit, recorded, and not inferred from examples, anxiety, urgency, or casual phrasing. |
| CWR-INV-015 | acyclic_module_dependencies | Module dependencies must remain acyclic and point inward toward kernel/canon. |

## Canonical Module Sequence

1. M0 Architecture Canon
2. M1 Runtime Kernel
3. M2 Direction Control
4. M3 Active Front
5. M4 Work Graph / Node Model
6. M5 Runtime Roles / Operator Registry
7. M6 Orchestration / Continuation
8. M7 Memory System
9. M8 Documentation / Artifact System
10. M9 Event System
11. M10 Review / Patch / Integration
12. M11 Parallel Work / Child Runs
13. M12 Execution Gateway
14. M13 Legacy Import
15. M14 Human Interaction Model
16. M15 Evaluation / Invariant Test Suite

This sequence is dependency order, not an implementation roadmap.

## Non-Goals of Module 0

Module 0 does not define exact storage layout, define full schemas for all modules, implement runtime behavior, create Direction state, create product execution plans, create Codex execution tasks, decide product strategy, import legacy artifacts, or create Project Instructions UI payload.

## Acceptance Criteria for Architecture Canon

Architecture Canon is acceptable when semantic primitives are stable enough for Runtime Kernel design; domain concepts are separated from primitives; adapters are separated from roles and domain modules; the module list is bounded and acyclic; every known state surface has an owner module; cross-module mutation is forbidden except through declared contracts; duplication policy is explicit; hidden state change prevention is explicit; unresolved architecture decisions are listed; and Module 1 Runtime Kernel can be designed without redefining Module 0.

END_OF_FILE: workflow/candidates/clean_runtime/architecture/ARCHITECTURE_CANON.md
