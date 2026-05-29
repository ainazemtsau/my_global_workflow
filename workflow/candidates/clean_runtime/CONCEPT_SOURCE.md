---
artifact:
  id: CWR-CONCEPT-SOURCE-001
  title: Clean Workflow Runtime Concept Source
  type: concept_source
  status: candidate
  owner_module: architecture_canon
  scope: clean_runtime_candidate
  version: 0.1
---

# Clean Workflow Runtime Concept Source

## Purpose

Clean Workflow Runtime is a candidate rebuild architecture for long solo+AI projects. It aims to preserve accepted state, route control, memory quality, execution gates, review discipline, and continuation across many chats, tools, agents, repositories, and manual actions.

This file captures the original concept in compact form. It is not active runtime authority.

## Five Conceptual Layers

1. Direction Control: coarse global control over root result, success conditions, tracks, route, and high-level state.
2. Active Front: the small set of work currently in focus, separated into primary, support, watch, parked, and blocked surfaces.
3. Local Work Maps: detailed decomposition only for active work, including nodes, dependencies, readiness, and closeout criteria.
4. Memory System: promotion-controlled shared memory that prevents local scratch, node internals, and chat residue from becoming global truth automatically.
5. Review / Patch System: bounded review jobs that propose patches or blockers for parent/integration acceptance.

## Direction Control Summary

Direction Control owns the coarse project meaning: root result, success conditions, global spine, tracks, direction-level decisions, and major route state. It prevents the project from being rebuilt from local chat momentum or old documents.

Global planning stays coarse; local work maps are detailed only for active work. Direction Control should not become a full roadmap or task graph.

## Active Front Summary

Active Front selects the work that currently matters. It separates primary work from support, watch, parked, and blocked work, so the system can hold context without treating every known possibility as current work.

Active Front changes require explicit route/front transitions. A review, event, chat conclusion, or document cannot silently move the front.

## Local Work Map Summary

Local Work Maps decompose active work into bounded nodes, dependency edges, readiness checks, expected outputs, and closeout criteria. They exist because detailed planning is useful near execution but harmful when expanded globally.

Local maps are subordinate to Direction Control and Active Front. They can propose parent patches when local findings affect the route.

## Node Model Summary

Nodes are bounded work units inside Local Work Maps. A node has a contract, allowed inputs, forbidden scope, expected result, evidence requirement, dependencies, and closeout criteria.

Sibling nodes do not inspect arbitrary internal work from each other. Nodes may consume shared memory, parent contracts, allowed upstream outputs, and explicit evidence refs. Node outputs become shared memory only through promotion.

## Memory System Summary

Memory is a curated shared surface, not a dump of transcripts or artifacts. Candidate memory can come from node closeout, review findings, research, human decisions, execution evidence, or legacy import, but it becomes shared memory only after promotion.

The memory system records promotion, supersession, confidence, sources, and stale status. Node outputs become shared memory only through promotion.

## Documentation System Summary

Documentation stores artifacts, refs, generated views, packets, evidence, and candidate architecture. Documents, maps, roadmaps, and projections do not create truth by existence.

Generated summaries and dashboards must declare sources, generation context, freshness conditions, and non-authority status. Canonical facts should have one owner and be referenced rather than copied.

## Event System Summary

Events record facts that happened: run completed, blocker found, candidate memory produced, validation failed, human decision requested, patch proposed, or legacy artifact classified.

Events do not mutate state directly. They may trigger reaction queue items, review jobs, patch prompts, closeout checks, or escalation requests.

## Review / Patch System Summary

Review jobs are bounded checks. They may return no change, patch proposal, blocker report, discovery request, or parent decision request.

Review jobs propose; parent/integration accepts. Reviewers do not self-apply patches, and proposed changes do not become accepted state until accepted by the responsible integration path.

## Parallel Chat Model Summary

Parallel chats are child runs under parent contracts. Each child receives a bounded scope, allowed memory, forbidden scope, output contract, conflict policy, and return path.

Parallel chats require parent contracts and return reports. Child chats do not become parent state by producing confident text.

## Continuation Packet Summary

Continuation packets let a new chat or agent resume without assuming an eternal parent chat. A packet carries refs to accepted state, active front, local map, allowed memory, current contract, constraints, open decisions, and required return format.

Continuation packets are launch surfaces, not accepted truth by themselves.

## Execution Boundary Summary

Execution remains gated by target, readiness, validation, and accepted result evidence. An execution route does not mean immediate implementation.

Execution requires a target binding, execution-ready contract, validation plan, implementation or delegation, validation result, evidence, and accepted completion decision.

## Clean Rebuild / Legacy Strategy Summary

The current Workflow OS or any old workflow runtime can become legacy evidence for selective import. Legacy artifacts are evidence only until selectively imported.

Legacy artifacts do not become current authority by existence, age, detail, or emotional importance. Useful parts require classification, mapping, review, acceptance, and indexing.

## Minimal Runtime Kernel Summary

The minimal kernel explains how candidate work becomes accepted state. It needs Accepted State, Work Contract, Run, Evidence, Acceptance Decision, and Invariant.

Accepted state changes only through explicit, checkable transitions. A transition is valid only when a contract, run result, evidence, validation, invariant check, and acceptance decision support it.

## Core Invariants Summary

- Accepted state changes only through explicit, checkable transitions.
- Documents, maps, roadmaps, and projections do not create truth by existence.
- Global planning stays coarse; local work maps are detailed only for active work.
- Node outputs become shared memory only through promotion.
- Review jobs propose; parent/integration accepts.
- Events do not mutate state directly.
- Parallel chats require parent contracts and return reports.
- Execution remains gated by target, readiness, validation, and accepted result evidence.
- Legacy artifacts are evidence only until selectively imported.

## Final Architecture Summary

Clean Workflow Runtime is a candidate, technology-neutral runtime architecture. It separates semantic primitives from domain concepts and adapters, keeps one owner per mutable state surface, prevents hidden state changes, treats tool-specific agents as role implementations, and requires explicit acceptance before candidate outputs become accepted state.

END_OF_FILE: workflow/candidates/clean_runtime/CONCEPT_SOURCE.md
