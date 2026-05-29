---
artifact:
  id: CWR-ROLE-TAXONOMY-001
  title: Clean Workflow Runtime Role Taxonomy
  type: role_taxonomy
  status: candidate
  owner_module: runtime_roles_operator_registry
  scope: global_runtime_architecture
  version: 0.1
---

# Clean Workflow Runtime Role Taxonomy

## Purpose

This file separates runtime roles from concrete technologies. A role is a responsibility in the runtime. An adapter is a current or future implementation of a role.

The same technology may implement multiple roles, and the same role may be implemented by different technologies.

## Role vs Adapter Distinction

Correct:

```text
Role: CodeExecutor
Adapter: Codex

Role: RuntimeIntegrator
Adapter: ChatGPT parent/integration chat
```

Explicitly forbidden:

- Codex owns execution.
- ChatGPT owns state.
- Claude is a module.
- GitHub is memory.

## Runtime Roles

| Role | Responsibility | Must not do |
|---|---|---|
| HumanOwner | Owns human intent, major acceptance, risk tolerance, preference, taste, and human-only decisions. | Be silently inferred from casual examples. |
| RuntimeIntegrator | Integrates child results, review outputs, patch proposals, memory candidates, and execution evidence into parent state. | Fabricate evidence, accept hidden state change, or bypass owner-module mutation rules. |
| WorkPlanner | Turns active composite work into a local work map or executable child contracts. | Create a global roadmap, execute composite nodes directly, or mutate accepted state without integration. |
| Worker | Performs bounded non-code work under a Work Contract. | Change parent state directly, inspect forbidden memory, or expand beyond contract. |
| Researcher | Performs bounded external or internal research and returns cited evidence with confidence and implications. | Turn research into route change directly or present speculative findings as accepted state. |
| Reviewer | Performs bounded review of a target or question. | Mutate state directly, broaden into strategy, or admit execution by itself. |
| MemoryCurator | Classifies and promotes candidate outputs into memory. | Promote local scratchpad as shared truth, duplicate canonical facts, or mutate node status directly. |
| CodeExecutor | Performs bounded code/product/repository changes after execution gates pass. | Begin without execution-ready contract, expand target, decide product route, or claim done without validation evidence. |
| ValidationRunner | Runs checks required by a validation plan. | Lower validation requirements after failure or convert unavailable validation into passed validation. |
| StorageAdapter | Reads/writes canonical files, refs, indexes, and artifacts under owner-module authorization. | Treat cache as authority, treat Project Instructions UI as schema storage, or mutate content without authorization. |
| Orchestrator | Launches bounded runs and manages return routing. | Decide acceptance by itself or launch parallel work without parent contract. |
| HumanActionExecutor | Performs manual external actions that cannot or should not be automated. | Let AI claim completion without human confirmation. |

## Current Suggested Adapter Bindings

| Adapter | May implement roles | Notes |
|---|---|---|
| ChatGPT | RuntimeIntegrator, WorkPlanner, Worker, Reviewer, MemoryCurator, Orchestrator | ChatGPT may implement RuntimeIntegrator, WorkPlanner, Worker, Reviewer, MemoryCurator, Orchestrator. It must not own accepted state by chat memory. |
| Codex | CodeExecutor, ValidationRunner, repository patch StorageAdapter | Codex may implement CodeExecutor, ValidationRunner, and repository patch StorageAdapter. It must not own route or execution semantics. |
| Claude Code | CodeExecutor, ValidationRunner | Claude Code may implement CodeExecutor and ValidationRunner. |
| Deep Research | Researcher | Deep Research may implement Researcher. |
| GitHub | StorageAdapter | GitHub may implement StorageAdapter. File existence or repository presence is not memory or semantic authority. |
| Human user | HumanOwner, HumanActionExecutor | Human user may implement HumanOwner and HumanActionExecutor. |

## Adapter Registry Shape

Each adapter binding should declare:

```yaml
adapter_binding:
  id:
  adapter_name:
  implements_roles:
  capabilities:
  limitations:
  allowed_surfaces:
  forbidden_surfaces:
  input_contracts:
  output_contracts:
  validation_support:
  human_approval_required_for:
  replacement_notes:
```

## Role Invariants

| ID | Name | Rule |
|---|---|---|
| ROLE-INV-001 | role_not_tool | A role must not require one specific tool unless the document is explicitly an adapter contract. |
| ROLE-INV-002 | one_run_one_contract | A role performs a bounded Run under a Work Contract. |
| ROLE-INV-003 | output_must_return | Every non-trivial role run returns a Result Report, Evidence, or explicit Blocker. |
| ROLE-INV-004 | reviewer_cannot_integrate_own_patch | A Reviewer may propose a patch, but integration must decide. |
| ROLE-INV-005 | executor_cannot_define_target | A CodeExecutor may execute target-bound work, but cannot define the target itself. |
| ROLE-INV-006 | human_acceptance_explicit | Human-owned decisions require explicit recorded selection or confirmation. |

END_OF_FILE: workflow/candidates/clean_runtime/architecture/ROLE_TAXONOMY.md
