---
artifact_control:
  namespace: proof_workflow
  artifact_type: system_overview
  status: gate_1_initial
  owner: proof_carrying_workflow_os
---

# Proof-Carrying Workflow OS

## Purpose

Proof-Carrying Workflow OS is a clean workflow kernel for making work state explicit, verifiable, and transportable across chats, tools, repositories, and future runtime surfaces.

The system exists to answer four questions before state is accepted:

- What Obligation is being worked?
- Which Operator was invoked?
- What Receipt was produced?
- Which verified Ledger delta was committed?

## Clean-Room Boundary

This namespace is a new proof workflow. It does not inherit semantic authority from the legacy workflow architecture.

Legacy workflow files, old project setup files, and old direction files may be inspected later only as migration evidence. They become new workflow facts only through Legacy Import Receipts that pass verification and commit.

This Gate 1 install performs no migration. It creates only the shared kernel and protocol documentation under `proof_workflow/`.

## Tier Model

### Tier 0: Semantic Kernel

The canonical semantic primitives are:

- Ledger
- Obligation
- Operator
- Receipt
- Invariant

Only these primitives define accepted workflow meaning.

### Tier 1: Runtime Protocols And Policies

Protocols govern movement through the kernel:

- Obligation Admission
- Run Admission
- Obligation Selection
- Operator Selection
- Decompose
- Invoke
- Verify
- Commit
- Commit Scope Policy
- Synthesize
- Project
- Learn
- Context Authority Policy
- Human Input Normalization Policy
- Human-Facing Run Closure Policy
- Recursive Child Handoff Policy
- Transport
- Proof Policy
- Human Gate Policy
- Tool / Execution Gate Policy
- Execution Harness Policy

Protocols are rules for movement. They are not additional semantic primitives.

### Tier 2: Runtime Adapters And Operational Forms

Adapters serialize, request, route, or project runtime state. Examples include Launch Card, Receipt Card, Context Request Card, Human Decision Card, Human Action Card, Codex Commit Handoff Card, Codex Execution Launch Card, Execution Receipt Card, Project Setup Receipt Card, Validation Receipt Card, Child Obligation Request Card, Child Result Return Card, Parent Recovery Block, Operator Catalog, Process Macro, Projection Document, Dashboard, Strategic Path Map Projection, Horizon Projection, Active Frontier View, and Inter-Scope Request.

Adapters do not create truth. They may carry claims, point to evidence, or request action, but accepted state requires a verified Receipt committed to the Ledger.

### Tier 3: Physical Storage And Tooling

Physical storage and tooling include GitHub files, Markdown documents, YAML sidecars, ChatGPT Project Files, API databases, Codex workspaces, and external tools / MCP.

Storage preserves and transports state. Storage does not create accepted state by itself.

## Gate 2 Execution Harness

Gate 2 execution specifications live under `proof_workflow/execution/`.

Execution remains kernel-derived: `Obligation -> Operator -> Receipt -> Verify -> Commit`.

Codex execution launch and execution receipt cards are Tier 2 adapters. They do not create new semantic primitives and do not revive a stage system.

## Core Doctrine

Kernel is authority.

Protocols govern movement.

Adapters serialize or project.

Documents do not create truth.

Processes and macros do not create truth.

Compatibility layers do not create truth.

Roadmaps do not create truth.

Loaded context does not create truth.

Human users do not need to speak in schemas; workflow normalizes clear intent into Receipts.

Human-facing clarity is part of workflow correctness.

Only verified Receipts committed to the Ledger create accepted state.

## Non-Authority Rules

A document may project accepted Ledger state, but it cannot make a claim accepted by writing it down.

A process macro may propose Obligations, select an Operator, or prepare transport, but it cannot mark work complete.

A projection may summarize, filter, or arrange accepted Receipts, but it must not introduce unsupported claims.

A roadmap is valid only as a projection over accepted Receipts and open Obligations.

## Migration Boundary

No Direction is migrated by this namespace install.

No future `directions/<direction-id>/proof/` files are created by this run.

Old workflow files are legacy evidence only. They are not design authority, runtime authority, or accepted state for the new proof workflow.

END_OF_FILE: proof_workflow/00_PROOF_CARRYING_WORKFLOW_OS.md
