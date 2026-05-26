---
artifact_control:
  namespace: workflow
  artifact_type: recursive_child_handoff_policy
  status: gate_4_0_initial
  owner: workflow_os
---

# Recursive Child Handoff Policy

## Purpose

Recursive Child Handoff lets a parent Operator invocation decompose a large or compound Obligation into focused child Obligation requests that can be handled in additional chats.

Recursive Child Handoff is a runtime policy, not a semantic primitive.

The core concept is recursive decomposition, not parallel execution.

## Child Runs

Large or compound Obligations may create child Obligation requests.

Child runs are normal Operator invocations over child Obligations.

Parent may create multiple child requests, but this is not a separate parallel mode.

Children can be launched in these orders:

- `run_now`
- `run_after`
- `optional`
- `blocked_until`

## Parent Responsibilities

Parent must explain in normal language why child runs are needed.

Parent must provide copy-paste prompts for each child.

Parent must tell the user what to bring back.

Parent must identify which child results are required and which are optional.

Parent must provide a Parent Recovery Block when multiple child chats are launched or when parent state would be hard to reconstruct from memory.

## Child Result Rules

Child result must be compact and parent-facing.

Parent synthesis waits for required child results.

Missing required child result blocks synthesis.

Conflicting child results require explicit conflict resolution or human decision.

Child runs must not mutate Ledger.

Child runs must not close parent Obligation.

Child runs must not make parent-level final decisions.

## Parent Recovery

Parent chat loss must be recoverable with Parent Recovery Block.

If parent chat is lost, user can open a new chat and paste:

- Parent Recovery Block
- child results already received

The new parent chat can continue collection or synthesis without depending on old parent chat memory.

## User-Facing Pattern

Use plain user instructions such as:

```text
Открой N новых чатов.

Вставь prompt #1 в первый чат.

Вставь prompt #2 во второй чат.

Верни результат сюда.

Если этот чат потеряется, открой новый чат и вставь Parent Recovery Block вместе с уже полученными child results.
```

## Synthesis Boundary

Parent synthesis may use child results as candidate input.

Parent synthesis must cite child result IDs.

Parent synthesis must not treat child results as committed Ledger state.

Parent synthesis must not close the parent Obligation until the parent Operator produces a Receipt that passes Verify and Commit policy.

END_OF_FILE: workflow/policies/13_RECURSIVE_CHILD_HANDOFF_POLICY.md
