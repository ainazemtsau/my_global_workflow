# Active Front Selection Interface

status: active_interface_layer

## Purpose

This interface defines how an Active Front is selected from the Direction Map.

## Required inputs

Active Front selection requires:

- exact Direction source authority;
- accepted Direction Spine;
- accepted or candidate Direction Map;
- Goal Evidence Graph and Active Unresolved Cut when available;
- current accepted/candidate/unresolved map labels;
- available evidence and accepted records;
- relevant lifecycle facts and prior stage, finish, or evidence records;
- known blockers and strategic uncertainties;
- user priorities or decisions if supplied.

## Candidate front packet

Every Candidate Active Front must include:

- candidate front name;
- source map areas;
- source Active Unresolved Cut or Goal Evidence Graph nodes when available;
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

- root criticality;
- bottleneck relief;
- critical uncertainty reduction;
- dependency unlock;
- evidence value;
- risk reduction;
- scope control;
- track coverage/balance;
- success-dimension balance;
- WIP/capacity;
- feasibility now;
- reversibility;
- explicit user priority/decision.

Scoring is decision support, not automatic truth.

## Acceptance

Accepted Active Front requires acceptance/update path.

A chat, Check Job, child chat, Codex run, STAGE_RESULT, FINISH_PACKET, or NEXT_CHAT_CARD may propose a front, but cannot accept it.

## Work Graph seed

The first Work Graph seed must derive from the Candidate Active Front exit criteria and boundaries. It must not import unrelated roadmap or unreviewed task-list items.

Front exit criteria must tie to Goal Evidence Graph nodes or Direction Map claims when those structures exist.

END_OF_FILE: workflow_v3/interfaces/04_ACTIVE_FRONT_SELECTION_INTERFACE.md
