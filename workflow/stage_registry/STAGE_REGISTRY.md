# 00 Stage Interface Index
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 6 — Stage Interface Registry Installed at: 2026-05-07T16:43:14.1696924+03:00 Source input: ChatGPT Step 6 output generated 2026-05-07 from validated current state after Step 5 Authority: Trilium canonical after read-back Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 00 Stage Interface Index

Interface version: stage-interface-v0.1

## Purpose

This note is the public registry for Workflow vNext-R stage interfaces.

It defines the shared interface rules for all stages and indexes the individual stage interface notes installed in this folder.

This registry defines boundaries only. It does not contain final prompt bodies, internal reasoning procedures, hidden instructions, or implementation-specific prompt text.

## Scope

Installed stage interface notes:

*   01 D0 Direction Setup Interface
*   02 P0 Phase Start Interface
*   03 I0 Capture Interface
*   04 G0 Goal Select Interface
*   05 G1 Goal Shape Interface
*   06 S3 Decide Interface
*   07 D1 Deep Research Interface
*   08 A1 Audit Interface
*   09 E1 Execution Brief Interface
*   10 F0 Fast Direct Interface
*   11 C1 Codex Graph Plan Interface
*   12 C2 Codex Execute Interface
*   13 B1 Problem Interface
*   14 R1 Review Distill Interface
*   15 P9 Phase Close Interface
*   16 R0 Recovery Close Interface

## Non-goals

This registry does not:

*   write final stage prompts;
*   define private chain-of-thought or hidden reasoning;
*   define stage-specific internal algorithms;
*   activate any stage globally;
*   overwrite old active Workflow vNext material.

## Authority references

The interface registry must remain compatible with these accepted rebuild contracts:

*   Workflow / 20 Workflow vNext-R REBUILD / 01 Foundation / 01 Operating Contract
*   Workflow / 20 Workflow vNext-R REBUILD / 01 Foundation / 02 Entity and State Model
*   Workflow / 20 Workflow vNext-R REBUILD / 01 Foundation / 03 Storage and Documentation Lifecycle
*   Workflow / 20 Workflow vNext-R REBUILD / 01 Foundation / 04 Boundary and Freshness Rules
*   Workflow / 20 Workflow vNext-R REBUILD / 01 Foundation / 05 Stage Interface Compatibility Contract
*   Workflow / 20 Workflow vNext-R REBUILD / 03 Transport Templates / 01 Stage Launch Card Template
*   Workflow / 20 Workflow vNext-R REBUILD / 03 Transport Templates / 02 Stage Result Packet Template
*   Workflow / 20 Workflow vNext-R REBUILD / 03 Transport Templates / 03 Context Request Card Template
*   Workflow / 20 Workflow vNext-R REBUILD / 03 Transport Templates / 04 Human Decision Card Template
*   Workflow / 20 Workflow vNext-R REBUILD / 03 Transport Templates / 05 Trilium Patch Template
*   Workflow / 20 Workflow vNext-R REBUILD / 03 Transport Templates / 06 Execution Log Entry Template
*   Workflow / 20 Workflow vNext-R REBUILD / 03 Transport Templates / 07 Documentation Maintenance Gate Template
*   Workflow / 20 Workflow vNext-R REBUILD / 03 Transport Templates / 08 Codex Wave Card Template
*   Workflow / 20 Workflow vNext-R REBUILD / 03 Transport Templates / 09 Codex Return Packet Template
*   Workflow / 20 Workflow vNext-R REBUILD / 03 Transport Templates / 10 Recovery Close Packet Template
*   Workflow / 20 Workflow vNext-R REBUILD / 04 Codex Bridge / 02 Codex Wave Card Contract
*   Workflow / 20 Workflow vNext-R REBUILD / 04 Codex Bridge / 03 Codex Return Packet Contract
*   Workflow / 20 Workflow vNext-R REBUILD / 05 Test Harness / 01 Stage Prompt Acceptance Checklist
*   Workflow / 20 Workflow vNext-R REBUILD / 05 Test Harness / 03 Scenario Test Format

## Shared public input contract

Every stage receives a Stage Launch Card.

Required launch fields:

*   workflow\_version
*   interface\_version
*   stage\_id
*   stage\_name
*   invocation\_reason
*   user\_request\_or\_trigger
*   current\_state\_ref
*   upstream\_packet\_ref
*   context\_bundle
*   freshness\_state
*   constraints
*   write\_authority
*   requested\_output\_shape
*   allowed\_next\_stage\_set
*   extension\_fields

A stage must not require private internals from any previous stage. It may rely only on public packets, explicit context, Trilium read-back references, and user-provided material.

## Shared public output contract

Every stage emits a Stage Result Packet or a valid alternative transport packet.

Required result fields:

*   workflow\_version
*   interface\_version
*   stage\_id
*   stage\_name
*   status
*   human\_summary
*   inputs\_used
*   outputs\_created
*   state\_delta
*   decisions\_or\_recommendations
*   evidence\_or\_context\_refs
*   write\_plan\_or\_patch
*   execution\_log\_entry
*   next\_route
*   compatibility\_report
*   extension\_fields

Valid result statuses:

*   complete
*   partial
*   blocked
*   needs\_input
*   escalated\_to\_human
*   recovery\_required

Valid next\_route types:

*   next\_stage\_launch\_card
*   context\_request\_card
*   human\_decision\_card
*   codex\_wave\_card
*   recovery\_close\_packet
*   stop

## Shared write target policy

Stages do not write directly to Trilium unless the Launch Card grants explicit write authority.

When write authority is absent, a stage must emit a Trilium Patch Template or Codex Wave Card.

Permitted write target families:

*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] /
*   Rebuild draft amendment mode: Workflow / 20 Workflow vNext-R REBUILD / 10 Draft Amendments /
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] /
*   Codex bridge mode: \[authorized Codex wave record path from Launch Card\]
*   Execution log mode: \[authorized execution log path from Launch Card\]

Forbidden write target families:

*   Workflow / 20 Workflow vNext-R REBUILD / 07 Stage Prompts / before the relevant Step 7.x approval
*   any path outside Workflow / 20 Workflow vNext-R REBUILD unless direction opt-in write authority is explicit
*   old active Workflow vNext material unless separately approved in a final activation step
*   deletion of notes unless explicit human approval is present

## Compatibility, core, and extension rules

Core fields are the stable public contract.

Core field rules:

*   Required core fields must be read strictly.
*   Required core fields must be emitted when applicable.
*   A stage must report missing required core fields through a Context Request Card or Recovery Close Packet.
*   A stage must not invent upstream authority when a core reference is absent.

Extension field rules:

*   Unknown extension fields must be tolerated on read.
*   Unknown extension fields must not break routing.
*   Unknown extension fields may be echoed or preserved.
*   A stage may write only its own namespaced extension fields.
*   Extension namespaces must use extensions.\[stage\_id\].\[field\_name\].
*   Extension fields must not override required core fields.
*   Downstream stages must not depend on an extension field unless the Launch Card explicitly declares that dependency.

Versioning rules:

*   Current interface version: stage-interface-v0.1.
*   Breaking changes require a new interface version and a migration note.
*   Nonbreaking additions must be optional extension fields.
*   Final prompt bodies written in Step 7+ must conform to this interface registry.

## Registry table

| Stage | Public role | Primary output | Allowed next stages |
| --- | --- | --- | --- |
| D0 | Direction setup | Direction Charter / Direction State | P0, I0, G0, G1, R0 |
| P0 | Phase start | Phase Start Packet | I0, G0, G1, F0, D1, A1, C1, P9, R0 |
| I0 | Capture | Capture Ledger | G0, G1, F0, D1, A1, B1, R1, P9, R0 |
| G0 | Goal select | Goal Selection Packet | G1, F0, D1, A1, R1, P9, R0 |
| G1 | Goal shape | Shaped Goal Brief | S3, E1, F0, D1, A1, B1, G0, R0 |
| S3 | Decide | Decision Record | E1, C1, D1, A1, G1, F0, P9, R0 |
| D1 | Deep research | Research Dossier | G1, S3, E1, A1, R1, B1, R0 |
| A1 | Audit | Audit Report | G1, S3, E1, C1, B1, R1, R0 |
| E1 | Execution brief | Execution Brief | C1, C2, F0, R1, P9, B1, R0 |
| F0 | Fast direct | Direct Output Packet | R1, P9, G1, E1, B1, R0 |
| C1 | Codex graph plan | Codex Graph Plan / Wave Card Draft | C2, E1, G1, B1, R0 |
| C2 | Codex execute | Codex Return Packet | R1, P9, B1, C1, E1, R0 |
| B1 | Problem | Problem Report / Repair Plan | G1, S3, D1, A1, E1, C1, P9, R0 |
| R1 | Review distill | Review Distill Packet | P9, G1, E1, D1, A1, F0, R0 |
| P9 | Phase close | Phase Close Packet | P0, D0, R1, R0, stop |
| R0 | Recovery close | Recovery Close Packet | retry\_previous\_stage, P0, G1, E1, C1, P9, stop |

## Acceptance anchors

*   Every stage has a public input contract.
*   Every stage has a public output contract.
*   Allowed next stages are defined.
*   Write target families are defined.
*   Compatibility/core/extensions rules are defined.
*   No final prompt body is present.