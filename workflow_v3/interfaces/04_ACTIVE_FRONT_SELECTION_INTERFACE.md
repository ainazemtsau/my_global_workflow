# Active Front Selection Interface

status: active_interface_layer

## Purpose

This interface defines how an Active Front is selected from the Direction Map.

## Required inputs

Active Front selection requires:

- exact Direction source authority;
- accepted Direction Spine;
- accepted or candidate Direction Map;
- current accepted/candidate/unresolved map labels;
- available evidence and accepted records;
- relevant Signals and Handler Results;
- known blockers and strategic uncertainties;
- user priorities or decisions if supplied.

## Candidate front packet

Every Candidate Active Front must include:

- candidate front name;
- source map areas;
- touched tracks;
- bottleneck or uncertainty;
- `why_now`;
- selection evidence;
- rejected/deferred alternatives;
- exit criteria;
- out of scope;
- first Work Graph seed;
- acceptance question.

## Selection criteria

Use these criteria as decision support:

- root outcome leverage;
- critical uncertainty reduction;
- dependency unlock;
- evidence speed;
- risk reduction;
- scope control;
- track coverage/balance;
- feasibility now;
- reversibility;
- explicit user priority/decision.

Scoring is decision support, not automatic truth.

## Acceptance

Accepted Active Front requires acceptance/update path.

A chat, Handler, Check Job, child chat, Codex run, or Progression Router Result may propose a front, but cannot accept it.

## Work Graph seed

The first Work Graph seed must derive from the Candidate Active Front exit criteria and boundaries. It must not import unrelated roadmap or Action Inbox items.

END_OF_FILE: workflow_v3/interfaces/04_ACTIVE_FRONT_SELECTION_INTERFACE.md
