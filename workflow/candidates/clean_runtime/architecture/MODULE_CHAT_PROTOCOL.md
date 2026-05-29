---
artifact:
  id: CWR-MODULE-CHAT-PROTOCOL-001
  title: Clean Workflow Runtime Module Chat Protocol
  type: module_chat_protocol
  status: candidate
  owner_module: architecture_canon
  scope: global_runtime_architecture
  version: 0.1
---

# Clean Workflow Runtime Module Chat Protocol

## Purpose

This protocol defines how future Clean Workflow Runtime module-design chats start, stay bounded, return results, and reach integration review. It is candidate guidance only and is not active runtime authority.

## Required Model

One module design chat handles one bounded module or one explicitly paired module. New module chats start from the Module 0 candidate docs plus a specific launch packet. Module chats do not mutate repository state.

Module chats return drafts, unresolved decisions, integration risks, and acceptance criteria. Parent/integration chat reviews module output against Module 0. Codex persistence happens only at checkpoints after accepted drafts.

## Generic Launch Packet Template

```text
TASK: Design Module <N> — <Module Name> for Clean Workflow Runtime.

BASELINE:
- Use Module 0 candidate architecture docs as the accepted design baseline for this chat.
- Treat Clean Workflow Runtime as candidate architecture, not active runtime authority.
- Do not mutate repository state.

SCOPE:
- Design only <bounded module or explicitly paired modules>.
- Use Module 0 semantic primitives: Accepted State, Work Contract, Run, Evidence, Acceptance Decision, Invariant.
- Preserve adapter neutrality.
- Preserve one state surface / one owner.

DELIVERABLES:
- <module draft file list>
- unresolved module decisions
- integration risks against Module 0
- acceptance criteria for the next dependent module

FORBIDDEN:
- Do not design unrelated modules in detail.
- Do not create product execution tasks.
- Do not create Codex execution tasks.
- Do not activate Clean Workflow Runtime.
- Do not treat chat output as accepted repository state.
```

## Generic Module Result Packet Template

```text
MODULE RESULT PACKET

module:
  id:
  name:
  status: draft

drafts:
  - title:
    summary:
    canonical_refs:

unresolved_decisions:
  - id:
    question:
    options:
    recommendation:

integration_risks:
  - risk:
    affected_module_0_rule:
    proposed_mitigation:

acceptance_criteria:
  - criterion:

scope_control:
  out_of_scope_items_detected:
  repository_mutation: none
```

The phrase module result packet refers to the bounded return object from the module-design chat to parent/integration review.

## Integration Review Checklist

The integration review checklist is:

- Confirms the module used Module 0 semantic primitives without redefining them.
- Confirms adapter names are not promoted into core runtime semantics.
- Confirms one mutable state surface has one owner module.
- Confirms all cross-module changes use query, event, result report, patch proposal, command, or integration decision contracts.
- Confirms no hidden state change is introduced.
- Confirms no module directly mutates another module's owned state surface.
- Confirms unresolved decisions are named instead of silently decided.
- Confirms acceptance criteria are concrete and checkable.
- Confirms repository persistence is deferred until accepted checkpoint review.

## Anti-Patterns

- designing many modules at once.
- turning module design into product roadmap.
- using Codex to decide architecture.
- treating chat output as accepted repo state.
- expanding into execution implementation.

END_OF_FILE: workflow/candidates/clean_runtime/architecture/MODULE_CHAT_PROTOCOL.md
