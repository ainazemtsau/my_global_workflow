---
artifact:
  id: CWR-PACKAGE-README-001
  title: Clean Workflow Runtime Candidate Package
  type: candidate_package_readme
  status: candidate
  owner_module: architecture_canon
  scope: clean_runtime_candidate
  version: 0.1
---

# Clean Workflow Runtime Candidate Package

## Package Status

status: candidate

Clean Workflow Runtime is a candidate architecture package. It is not active runtime authority, and it does not replace the current Workflow OS.

Current Workflow OS behavior remains governed by the existing canonical workflow files. This package exists only as an isolated design reference for future module-design chats and later integration reviews.

## Intended Use

Use these files to give future Clean Workflow Runtime module-design chats a stable Module 0 baseline without relying on chat memory or duplicating large context.

Future modules should be designed against Module 0 and returned for integration review before repository persistence. Repository persistence should happen only after accepted drafts and explicit checkpoint review.

## Non-Authority Warning

This package does not mutate current Workflow OS runtime behavior, Project setup, packs, Direction state, ledgers, obligations, receipts, dashboards, manifests, or execution protocols.

Documents, maps, roadmaps, and projections do not create truth by existence. Candidate Clean Workflow Runtime documents are design inputs only until explicitly reviewed and accepted through the active Workflow OS governance process.

## File Index

| File | Purpose |
|---|---|
| `workflow/candidates/clean_runtime/CONCEPT_SOURCE.md` | Compact source concept for the Clean Workflow Runtime candidate. |
| `workflow/candidates/clean_runtime/architecture/ARCHITECTURE_CANON.md` | Module 0 architecture canon, vocabulary, primitive boundary, and invariants. |
| `workflow/candidates/clean_runtime/architecture/MODULE_MAP.md` | Candidate module boundaries, ownership, mutation paths, and dependencies. |
| `workflow/candidates/clean_runtime/architecture/ROLE_TAXONOMY.md` | Runtime roles separated from concrete technologies and adapters. |
| `workflow/candidates/clean_runtime/architecture/MODULE_CHAT_PROTOCOL.md` | Protocol for starting, closing, and reviewing future module-design chats. |
| `workflow/candidates/clean_runtime/architecture/OPEN_ARCHITECTURE_DECISIONS.md` | Unresolved decisions intentionally left open by Module 0. |
| `workflow/candidates/clean_runtime/architecture/NEXT_MODULE_LAUNCH_PACKET.md` | Ready-to-copy launch packet for Module 1. |

## Next Intended Module

Module 1 — Runtime Kernel

END_OF_FILE: workflow/candidates/clean_runtime/README.md
