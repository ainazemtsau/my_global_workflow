# Procedure Definition Canon

status: active_procedure_framework

## Purpose

A Workflow v3 procedure is a source-aware, outcome-gated work contract executed inside RUN after START selects exactly one entrypoint.

A procedure defines how a bounded kind of work is performed, what sources are authoritative, which gates must pass, when expansion is allowed, and what output must be returned.

## Boundaries

A procedure is not:

- a prompt;
- a template;
- the chat lifecycle;
- acceptance;
- storage mutation;
- a hidden router;
- permission to switch procedures during RUN.

START selects the procedure through `workflow_v3/control_plane/PROCEDURE_REGISTRY.md`. RUN executes only that selected procedure. FINISH_REQUEST, Result Packet, and Event Loop Closure remain controlled by `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md`.

## Procedure file model

Procedure files should use compact markdown sections for:

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
- checkpoint policy;
- output contract;
- eval / quality checks;
- stop conditions;
- procedure closure requirements.

Do not bury routing logic in project instructions. Keep registry entries compact and place execution detail in the procedure file.

## Canonical location and naming

The canonical location for new or migrated Procedure Definition Framework procedures is:

```text
workflow_v3/procedures/**
```

Use procedure naming for new or migrated Procedure Definition Framework files:

```text
*_PROCEDURE.md
```

Do not preserve obsolete `*_RUNBOOK.md`, `*_PLAYBOOK.md`, or runbook/playbook directory placement merely because a pre-migration registry entry pointed there.

During migration, existing registry entries may temporarily point to legacy runbook, formation, or other operational paths only as coexistence for not-yet-migrated procedures. That coexistence is not precedent for new or migrated procedures.

After a procedure is migrated into this framework, update `workflow_v3/control_plane/PROCEDURE_REGISTRY.md` so `procedure_ref` points to the canonical migrated procedure file. Remove, archive, or explicitly mark the old runbook/playbook file as a compatibility shim through a separately admitted repository update path.

Any exception to canonical location or naming must be explicit, bounded, and justified in the migration plan and registry delta. Silent path-preserving migration is not allowed.

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

Gates must test material sufficiency. They must not be decorative status labels.

## Complexity levels

Use the smallest level that can satisfy the output contract:

- `inline` - short answer or tiny non-state-sensitive result.
- `standard` - normal source-sensitive procedure without separate checkpoints.
- `checkpointed` - user-visible checkpoint needed before later stages.
- `research_backed` - external or current-source research is needed and bounded.
- `delegated_or_tool_mediated` - child/check/Codex/provider work is needed.

The selected complexity can be recorded only after START has read the selected procedure source.

## Checkpoints

Checkpoints are internal RUN gates. They are not lifecycle phases.

Checkpoints are not Signals by default. Emit a Signal only when the checkpoint reveals a notable workflow fact such as a blocking source issue, validation failure, scope drift, acceptance ambiguity, or missing child/check/Codex result.

FINISH_REQUEST remains the only lifecycle transition from RUN to FINISH.

## Expansion

Optional expansion must be bounded by the selected procedure. Expansion may include research, child chat, check job, Codex handoff, or tool-mediated work only when the procedure and run surface allow it.

Expansion does not authorize independent material work, hidden mutation, acceptance, or procedure switching.

## Closure

Procedure closure must:

- satisfy or explicitly fail the output contract;
- state source limitations and unresolved gates;
- emit FINISH_REQUEST before FINISH when the lifecycle requires it;
- use Result Packet and Event Loop Closure as defined by `CHAT_FINISH_PROTOCOL.md`;
- select exactly one primary next move at closure.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_DEFINITION_CANON.md