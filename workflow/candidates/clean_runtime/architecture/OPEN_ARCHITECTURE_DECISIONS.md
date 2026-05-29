---
artifact:
  id: CWR-OPEN-ARCHITECTURE-DECISIONS-001
  title: Clean Workflow Runtime Open Architecture Decisions
  type: open_architecture_decisions
  status: candidate
  owner_module: architecture_canon
  scope: global_runtime_architecture
  version: 0.1
---

# Clean Workflow Runtime Open Architecture Decisions

## Purpose

This file records unresolved Module 0 architecture decisions. These decisions are intentionally not forced inside Module 0 because later module design or integration review may need sharper evidence.

## Decisions

| ID | Decision | Current candidate position |
|---|---|---|
| UAD-001 | Final naming of semantic primitives. | Use clean neutral names as canonical: Accepted State, Work Contract, Run, Evidence, Acceptance Decision, Invariant. Keep old terms as legacy mapping. |
| UAD-002 | Whether Acceptance Decision is primitive or kernel protocol. | Module 0 treats it as a primitive candidate. Module 1 should decide whether it remains primitive or becomes transition protocol. |
| UAD-003 | Exact storage layout. | Module 0 defines ownership, not final filesystem or storage layout. Resolve in Documentation / Artifact System or storage design. |
| UAD-004 | Schema format. | Candidate options include Markdown + YAML frontmatter, YAML files, JSON schema, or hybrid markdown docs with machine-readable appendices. |
| UAD-005 | Module count / possible future consolidation. | Keep M0-M15 boundaries for now. Future consolidation candidates include Documentation + Memory, Review/Patch + Event, Parallel Work + Orchestration, and Human Interaction + Orchestration. |
| UAD-006 | Ownership of integration. | Candidate split: Kernel owns legality; Review/Patch owns integration workflow; target module owns persisted state surface. |
| UAD-007 | Event journal mutability. | Candidate rule: event records are append-only; handling status is a projection/index or append-only follow-up event. |
| UAD-008 | Human decision state ownership. | Candidate split: Human Interaction captures and normalizes; Memory or Decision Memory persists accepted decision records after integration. |
| UAD-009 | Generated projections as views vs artifacts. | Candidate rule: generated projections are views or generated artifacts, never authority. |
| UAD-010 | Adapter registry granularity. | Role Registry defines abstract capabilities; adapter-specific detail lives in adapter contracts. |
| UAD-011 | Legacy import threshold. | Legacy Import should define a classification matrix for import, rejection, or evidence-only retention. |
| UAD-012 | Major route change human approval. | Direction Control and Human Interaction should define which irreversible/high-risk route changes require HumanOwner approval. |
| UAD-013 | Strictness of one state surface / one owner. | Candidate rule: one persisted owner per surface; cross-effects move through events, reports, or patches. |
| UAD-014 | Relation to Project setup and packs. | Later integration must decide whether these files are repo-only, request-only sources, or Project Files. Module 0 does not update Project setup or packs. |

END_OF_FILE: workflow/candidates/clean_runtime/architecture/OPEN_ARCHITECTURE_DECISIONS.md
