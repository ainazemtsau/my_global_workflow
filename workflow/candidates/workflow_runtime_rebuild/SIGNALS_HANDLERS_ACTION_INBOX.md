# Signals / Handlers / Action Inbox

status: candidate_draft

## Purpose

This file defines the simple operational control layer for Workflow Runtime Rebuild.

It covers:

- Signal;
- Handler;
- Action Inbox;
- Action Inbox Item lifecycle;
- Check Job;
- relation to Next Move.

This is not a production Event System. It is a small control layer that helps long projects notice facts, hold useful follow-up candidates and avoid losing important checks.

## Core rule

Signal is a fact.

Handler creates a candidate action.

Action Inbox stores useful candidate actions.

None of these change Accepted State by themselves.

A Signal does not change state.

A Handler result does not change state.

An Action Inbox Item does not change state.

Accepted State changes only through the explicit acceptance/update path defined by the runtime model.

## Signal semantics

A Signal is a recorded fact worth noticing.

Examples:

- a source file could not be read;
- a Project File may be stale;
- Codex validation failed;
- a child chat did not return;
- an Action Inbox item became stale;
- conflicting evidence appeared;
- user raised an off-scope concern;
- acceptance is unclear.

A Signal is not:

- a command;
- a task assignment;
- a decision;
- an acceptance;
- a state mutation;
- an automatic route change.

Signal answers: "What happened or was observed?"

It does not answer: "What must be done?"

## Minimal signal categories

Keep categories small.

Recommended defaults:

1. source_signal
   Facts about source access, source freshness, missing files, stale Project Files or GitHub unavailability.

2. scope_signal
   Facts about work becoming too broad, off-scope, phase-jumped or mixed with another job.

3. evidence_signal
   Facts about missing, weak, conflicting or failed evidence.

4. acceptance_signal
   Facts about unclear acceptance, rejected result, candidate result needing review or hidden acceptance risk.

5. adapter_signal
   Facts from ChatGPT, Codex, Claude Code, Deep Research, GitHub, future AI providers or human actions.

6. inbox_signal
   Facts about Action Inbox growth, stale items, duplicate candidates or handler flood.

7. recovery_signal
   Facts that require recovery: lost parent chat, missing child result, failed validation, blocked run.

Direction-specific signals may exist, but they must not override the core rule: Signal is fact only.

## Run log / signal history

Signals should be recorded in a lightweight run log or signal history.

Minimum useful fields:

- signal_id or short label;
- category;
- observed_fact;
- source or origin;
- related Direction Spine / Active Front / Work Graph / Work Contract / Run when known;
- severity: info, watch, needs_attention, blocking;
- timestamp or run reference when available;
- handler_status: not_handled, handled, ignored, superseded;
- resulting_candidate_action_id if a Handler created one;
- limitation if the fact is based on incomplete source access.

The log is evidence history, not Accepted State.

A Signal in the log can support later review, but it does not accept anything by itself.

## Handler semantics

A Handler is a rule or small process that reacts to a Signal.

Handler output is candidate action only.

A Handler may:

- classify a Signal;
- decide that no action is needed;
- create an Action Inbox Item;
- suggest a Check Job;
- suggest a repair Next Move;
- suggest a candidate Launch Packet.

A Handler must not:

- execute material work;
- mutate Accepted State;
- accept evidence;
- launch Codex by itself;
- silently close an issue;
- change Direction Spine, Active Front or Work Graph by itself;
- become a hidden controller.

Handler answers: "What candidate action should be considered?"

It does not answer: "What is accepted now?"

## Default handlers

Default handlers are generic and apply across directions.

Suggested default handlers:

1. missing_source_handler
   Signal: required source missing or unreadable.
   Candidate action: create blocked Result Packet or Check Job to retrieve exact source.

2. stale_context_handler
   Signal: Project Files or supplied context may be stale.
   Candidate action: verify canonical GitHub source before material work.

3. scope_drift_handler
   Signal: chat mixed multiple jobs or jumped phase.
   Candidate action: split, park residuals or return to bounded Work Contract.

4. failed_validation_handler
   Signal: Codex validation failed.
   Candidate action: same-package Codex repair or blocked Result Packet.

5. unclear_acceptance_handler
   Signal: candidate result lacks explicit acceptance.
   Candidate action: parent review / Acceptance Decision request.

6. child_missing_handler
   Signal: child chat result missing.
   Candidate action: Parent Recovery Block update.

7. inbox_hygiene_handler
   Signal: Action Inbox duplicates, grows stale or floods.
   Candidate action: merge, drop, supersede or prioritize items.

## Direction-specific handlers

Direction-specific handlers are allowed when a direction has real recurring needs.

Examples:

- game_design_risk_handler;
- technical_validation_watch_handler;
- nutrition_plan_stale_handler;
- research_freshness_handler.

They live in the Direction customization layer, not in the core runtime model.

Direction-specific handlers may create candidate actions, but they must not bypass accepted-state rules.

## Action Inbox purpose

Action Inbox is a small queue of useful candidate actions that should not interrupt the current bounded work.

It holds:

- deferred questions;
- risks;
- ideas;
- check jobs;
- stale checks;
- follow-ups;
- possible repairs;
- things to ask the user later.

Action Inbox is not:

- a trash bin;
- a roadmap;
- a global backlog;
- a hidden project manager;
- an automatic execution queue;
- a place to store every thought.

## Action Inbox item requirements

Every item must have enough context to be useful later.

Minimum fields:

- item_id or short label;
- title;
- reason;
- relation: Direction Spine, Active Front, Work Graph node, Work Contract, Run, Evidence, Memory or general direction;
- source_signal_id if created by Handler;
- candidate_action;
- priority: low, normal, high, blocking_candidate;
- when_to_run or stale_condition;
- owner: user, parent chat, work chat, Codex, research/check, human action;
- expected_output;
- close_condition;
- status.

Optional fields:

- created_from;
- evidence_needed;
- blocked_by;
- supersedes;
- duplicate_of;
- expiry_date or expiry_condition;
- notes.

## Item lifecycle

Recommended lifecycle:

1. proposed
   Item was created by user, Handler or chat.

2. triaged
   Item is classified as useful, duplicate, stale, off-scope or blocking candidate.

3. selected
   Item is selected for action.

4. converted
   Item becomes a Launch Packet, Check Job, human decision request or Codex Work Package.

5. running
   Related work is in progress elsewhere.

6. returned
   Result Packet returned and awaits review.

7. closed
   Item is resolved, dropped, superseded or accepted through separate path.

8. stale
   Item is no longer useful unless refreshed.

Allowed closures:

- done_with_evidence;
- dropped_not_useful;
- duplicate_merged;
- superseded;
- blocked_until_source_available;
- accepted_elsewhere;
- rejected_out_of_scope.

## Selecting an Action Inbox item

An item may be selected when:

- it supports the current Active Front;
- it blocks safe progress;
- its stale condition triggered;
- it is needed for acceptance;
- it prevents false done;
- the user explicitly chooses it.

Do not select an item merely because it exists.

Do not allow old low-value items to pull the workflow away from the current Active Front.

## Running an item

Running an item means converting it into one of these:

- Launch Packet for a Work Chat;
- Check Job;
- Codex Work Package;
- Human action request;
- parent review question;
- explicit human decision request;
- drop/supersede action.

The Action Inbox Item itself is not the run.

The converted packet or request must carry scope, boundaries, expected output and return destination.

## Check Jobs

A Check Job is a bounded verification or analysis task.

It is used for:

- source freshness;
- evidence quality;
- regression check;
- consistency check;
- comparing claims;
- verifying whether a risk is real;
- reviewing whether a candidate is ready for acceptance.

Check Job differs from Work Chat:

- Work Chat produces material project work for a Work Contract.
- Check Job checks, verifies, researches or audits a bounded question.
- Check Job can support acceptance, but does not accept state.
- Check Job can create evidence, but evidence remains candidate until reviewed.

A Check Job should have:

- question;
- why it matters;
- sources to check;
- allowed/forbidden sources;
- expected finding format;
- confidence/limitations;
- return destination;
- next move if blocked.

## Relation to Next Move

Next Move is the exact next instruction after a material chat or decision.

Action Inbox can influence Next Move only by proposing candidate actions.

Examples:

- If source is missing, Next Move may be: "retrieve exact file and rerun."
- If Codex validation failed, Next Move may be: "send same-package repair to Codex."
- If acceptance is unclear, Next Move may be: "run parent acceptance review."
- If nothing is safe to run, Next Move may be: "human decision required."

Next Move remains a transport instruction, not Accepted State.

## Anti-trash-bin rules

1. No item without reason.
2. No item without relation.
3. No item without when_to_run or stale_condition.
4. No duplicate items; merge them.
5. No permanent vague items like "think about this later."
6. No item may auto-run.
7. No item may mutate state.
8. Old items must be dropped, refreshed or superseded.
9. Action Inbox must not replace Direction Spine or Work Graph.
10. Handler flood must trigger inbox_hygiene_handler.

## Simple examples

Example 1: stale Project File

Signal:
  Project Files may not match GitHub source.

Handler:
  stale_context_handler.

Candidate Action Inbox Item:
  Verify exact repository file before next material work.

Possible Next Move:
  Run Check Job to read GitHub path/ref and compare with supplied cache.

Example 2: Codex validation failed

Signal:
  git diff --check failed.

Handler:
  failed_validation_handler.

Candidate Action Inbox Item:
  Send same-package repair to Codex, allowed paths unchanged.

Possible Next Move:
  Paste repair package into Codex and return result to verification chat.

Example 3: off-scope user idea

Signal:
  User raised launch marketing question during technical design run.

Handler:
  scope_drift_handler.

Candidate Action Inbox Item:
  Park marketing question as candidate future track check, do not run now.

Possible Next Move:
  Continue current technical Work Contract; revisit item only when Active Front supports it.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/SIGNALS_HANDLERS_ACTION_INBOX.md
