# Procedure Definition Canon

status: active_procedure_framework

## Purpose

A Workflow v3 procedure is a source-aware, outcome-gated work contract executed inside RUN after START selects exactly one owner entrypoint.

A procedure defines how a bounded kind of work is performed, what sources are authoritative, which gates must pass, when expansion is allowed, how utility decisions are made, and what output must be returned.

## Boundaries

A procedure is not:

- a prompt;
- a template;
- the chat lifecycle;
- acceptance;
- direct ChatGPT storage mutation unless selected through `storage_update_adapter`;
- a hidden router;
- permission to switch procedures during RUN.

START selects the owner procedure through `workflow_v3/control_plane/PROCEDURE_REGISTRY.md`. RUN executes only that selected owner procedure. Utility/adapter packets may be used as internal RUN gates through the global Utility Use Gate under `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md`; they do not select a new owner procedure.

FINISH_REQUEST, FINISH_PACKET, Result Packet, and Next Move Packet remain controlled by `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md`.

## Procedure class model

Procedure files must align with the registry `procedure_class`:

- `core_material` - owns a material workflow task.
- `utility_adapter` - prepares bounded utility packets or external handoffs.
- `verification_adapter` - verifies returned evidence.
- `storage_adapter` - performs admitted storage mutation only from exact packages.
- `readonly_console` - reads or summarizes without material execution.

Detailed class semantics live in `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md` and should not be duplicated as a second router.

## Procedure file model

Procedure files should use compact markdown sections for:

- status and procedure class;
- purpose;
- trigger / when to use;
- when not to use;
- required inputs;
- source requirements;
- context classification;
- complexity selector;
- stage cards;
- gates;
- optional expansion;
- research policy;
- utility decision gate and adapter policy;
- external handoff and return policy;
- checkpoint policy;
- output contract;
- eval / quality checks;
- stop conditions;
- procedure closure requirements.

Do not bury routing logic in project instructions. Keep registry entries compact and place execution detail in the procedure file.

## Canonical Location and Naming

The canonical location for Workflow v3 Procedure Definition Framework procedures is:

```text
workflow_v3/procedures/**
```

Use procedure naming for Procedure Definition Framework files:

```text
*_PROCEDURE.md
```

Do not preserve obsolete `*_RUNBOOK.md`, `*_PLAYBOOK.md`, or runbook/playbook directory placement as active procedure source.

Every active registry entry must point to a canonical procedure file under `workflow_v3/procedures/**`.

Detailed procedure body authoring happens in separate bounded `author_workflow_procedure` chats. Until authored, the canonical procedure file may be a self-contained stub target spec.

Any exception to canonical location or naming must be explicit, bounded, and justified in the authoring plan and registry delta.

## Self-contained Stub Procedure Requirements

A stub procedure must include:

- purpose;
- trigger;
- non-trigger;
- required inputs;
- procedure class;
- target workflow role;
- workflow integration;
- future body outline;
- output contract;
- STOP behavior until authored;
- procedure closure using FINISH_PACKET, Result Packet, and Next Move Packet.

A stub is sufficient registry source only for selecting and stopping. It must not execute detailed procedure logic until a later bounded `author_workflow_procedure` run authors the body.

## Stage Card model

Each material stage should be expressed as a Stage Card with:

```text
stage_id:
purpose:
activation conditions:
inputs:
required intermediate output:
gate:
checkpoint rule:
expansion rule:
stop behavior:
```

Simple procedures may have one or two Stage Cards. Complex procedures may use more, but stages must still be reviewable and outcome-gated.

## Gate outcomes

Allowed gate outcomes:

- `PASS` - continue or close with requirements met.
- `PASS_WITH_RISK` - continue or close while naming bounded limitations.
- `REWORK` - repeat or repair the current stage before continuing.
- `EXPAND` - activate an allowed expansion path.
- `STOP` - halt the current procedure and return a blocked or exception result.
- `TRANSFER` - produce a bounded handoff or next-surface packet.
- `RUN_EXTERNAL_HANDOFF` - pause RUN with a complete external utility packet when the selected owner procedure needs external evidence before completion.
- `RUN_EXTERNAL_RETURN` - resume the same selected owner procedure after returned external evidence is provided.

Gates must test material sufficiency. They must not be decorative status labels.

## Complexity levels

Use the smallest level that can satisfy the output contract:

- `inline` - short answer or tiny non-state-sensitive result.
- `standard` - normal source-sensitive procedure without separate checkpoints.
- `checkpointed` - user-visible checkpoint needed before later stages.
- `research_backed` - external or current-source research is needed and bounded.
- `delegated_or_tool_mediated` - child/check/Codex/provider work is needed. Utility resources may be used only as bounded packets or gates under the selected owner procedure.

The selected complexity can be recorded only after START has read the selected procedure source.

## Checkpoints

Checkpoints are internal RUN gates. They are not lifecycle phases.

Checkpoints return typed gate outputs such as `PASS`, `PASS_WITH_RISK`, `REWORK`, `EXPAND`, `STOP`, `TRANSFER`, `RUN_EXTERNAL_HANDOFF`, or `RUN_EXTERNAL_RETURN`. Blocking source issues, validation failures, scope drift, acceptance ambiguity, missing child/check/Codex results, and missing external returns must become typed stop, repair, transfer, external-handoff, or check-job outputs rather than a separate routing event.

FINISH_REQUEST remains the only lifecycle transition from RUN to FINISH.

## Expansion

Optional expansion must be bounded by the selected owner procedure. Expansion may include research, child chat, check job, Codex handoff, embedded Codex-return verification, provider work, or tool-mediated work when the global Utility Use Gate passes.

Expansion does not authorize independent material work, hidden mutation, acceptance, or procedure switching.

External Codex/storage utility writes may occur inside the same owner RUN only through Utility Use Gate, write gate, exact path boundaries, validation, and verified RUN_EXTERNAL_RETURN.

## Utility Decision Gate

Owner procedures may invoke registered utility resources during RUN when needed to complete the selected work.

Procedures do not need to pre-enumerate every utility. Procedure-specific docs may customize common utility choices or forbid utilities for source, safety, policy, or write-boundary reasons, but global utility access is not blocked by absent prelisting.

## Utility / Adapter Policy

A procedure that commonly uses utilities should state:

```text
common_utility_choices:
forbidden_utility_categories:
external_handoff_policy:
external_return_policy:
embedded_verification_policy:
storage_boundary:
```

Utility/adapter policy must reference `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md` as the authority for class and category semantics.

A utility packet produced inside RUN is not a new owner procedure. A standalone utility adapter run is selected by START only when the user's primary request is the utility artifact.

## Closure

Procedure closure must:

- satisfy or explicitly fail the output contract;
- state source limitations and unresolved gates;
- resolve, verify, or explicitly block any required external return before FINISH_REQUEST;
- emit FINISH_REQUEST before FINISH when the lifecycle requires it;
- use FINISH_PACKET, Result Packet, and Next Move Packet as defined by `CHAT_FINISH_PROTOCOL.md`;
- select exactly one primary next move at closure;
- never start a new material lifecycle after FINISH in the same chat.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_DEFINITION_CANON.md
