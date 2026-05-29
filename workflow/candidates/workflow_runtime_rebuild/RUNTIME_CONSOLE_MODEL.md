# Runtime Console Model

status: candidate_draft

## Purpose

Runtime Console is a read-only view of a Direction.

It helps the user answer:

- What is going on?
- What is currently active?
- What is blocked?
- What candidate actions are waiting?
- What evidence exists?
- What is the exact Next Move?

Runtime Console is not a place to execute material work.

It is a status, audit and navigation surface.

## Read-only boundary

The console is read-only.

It may show state, summarize verified records, expose uncertainty, list candidate actions and propose candidate Next Move options.

It must not:

- mutate Accepted State;
- accept evidence;
- promote Memory;
- execute Work Contracts;
- launch Codex directly;
- close Action Inbox items silently;
- change Direction Spine;
- change Active Front;
- run Handlers as authority;
- become a hidden runtime controller.

Console output can become input to a later Work Chat, Check Job, Codex Work Package or acceptance/update path, but only through explicit user action or accepted process.

## Status views

### Direction Spine view

Direction Spine view shows:

- Root Result;
- Success Conditions;
- Spine Points;
- Tracks;
- accepted progress;
- unresolved high-level decisions;
- what is not part of the Direction Spine.

Purpose:
  Show the stable axis of the Direction without turning it into a full roadmap.

### Active Front view

Active Front view shows:

- current Active Front;
- why it is selected;
- relation to Direction Spine;
- current focus boundary;
- what is explicitly out of scope;
- whether the front is blocked or moving.

Purpose:
  Prevent work from spreading across the whole project.

### Work Graph / Node view

Work Graph / Node view shows:

- local nodes for current Active Front;
- selected node;
- dependencies;
- open Work Contract;
- recent Runs;
- evidence status;
- whether node is ready, blocked, running, returned or needs acceptance.

Purpose:
  Show the local working structure without creating a global graph of everything.

### Action Inbox view

Action Inbox view shows:

- open candidate actions;
- relation for each item;
- priority;
- when_to_run or stale_condition;
- owner;
- status;
- duplicates;
- stale or superseded items;
- items that may become Check Jobs.

Purpose:
  Keep useful deferred candidates visible without becoming a trash bin.

### Signals / Run Log view

Signals / Run Log view shows:

- recent Signals;
- source or origin;
- severity;
- related Run or Work Contract;
- handler_status;
- resulting candidate actions;
- limitations.

Purpose:
  Show why candidate actions exist and where risks came from.

### Codex / Adapter Runs view

Codex / Adapter Runs view shows:

- recent Codex runs;
- branch / commit when returned;
- changed files;
- validation status;
- forbidden path check;
- residual risks;
- other adapter outputs;
- source limitations.

Purpose:
  Make tool output verifiable instead of relying on "done" claims.

### Next Move view

Next Move view shows:

- exact current Next Move;
- reason for this Next Move;
- destination: new Work Chat, parent review, Codex, Check Job, human decision or stop;
- what must be pasted or opened;
- what must not be decided by the next adapter;
- blocker if no safe Next Move exists.

Purpose:
  The user should not guess the next step.

### Blocked / Parked / Watch view

Blocked / Parked / Watch view shows:

- blocking conditions;
- parked residuals;
- watch items;
- stale checks;
- human decisions needed;
- source/access blockers;
- items that should be dropped or superseded.

Purpose:
  Separate "cannot proceed" from "not now" from "watch later."

## What console may do

Runtime Console may:

- summarize status from supplied canonical records;
- classify visible uncertainty;
- show stale/missing context warnings;
- list candidate Action Inbox items;
- show possible candidate Next Move options;
- produce candidate Launch Packet text;
- produce candidate Check Job text;
- produce a human decision request;
- recommend that material work should not start yet;
- show why an Active Front or Next Move appears selected.

## What console must not do

Runtime Console must not:

- perform the material work it describes;
- decide acceptance;
- update canonical storage;
- mark a candidate result accepted;
- run Codex directly;
- convert a candidate Launch Packet into completed work;
- hide source limitations;
- treat Project Files as truth when canonical source is required;
- keep working indefinitely as a normal Work Chat.

## Candidate Launch Packet / Next Move generation

Console may produce candidate Launch Packet or candidate Next Move only as text for user review.

Example boundary:

- Allowed:
  "Here is the candidate Launch Packet for the next Work Chat."

- Forbidden:
  "I have launched the next Work Chat and accepted the result."

A candidate packet must still include:

- target;
- source_refs;
- context included;
- in scope;
- out of scope;
- expected result;
- evidence required;
- return destination;
- blocked_if;
- what the next adapter must not decide.

## Common user requests

### "покажи статус"

Console should return:

- Direction Spine summary;
- Active Front;
- current Work Graph / Node;
- open blockers;
- Action Inbox highlights;
- exact Next Move;
- source limitations.

It should not start work.

### "покажи эту ноду"

Console should return:

- node purpose;
- relation to Active Front;
- current Work Contract if any;
- dependencies;
- evidence status;
- open risks;
- candidate Next Move.

It should not execute the node.

### "покажи Action Inbox"

Console should return:

- open items grouped by blocking/high/normal/low/stale;
- reason and relation for each item;
- suggested hygiene actions;
- candidate items that could become Check Jobs.

It should not auto-run the items.

### "почему выбран этот front?"

Console should return:

- relation to Direction Spine;
- accepted reason if available;
- evidence or decision that selected it;
- uncertainty if selection is not verified;
- whether human decision is needed.

It should not invent accepted rationale.

### "что blocked?"

Console should return:

- blockers;
- missing context;
- failed validation;
- missing child returns;
- unclear acceptance;
- stale source risks;
- candidate repair Next Move.

It should not claim done while blockers remain.

## Console closure

Every console response should end with one of these:

- no_material_work_started;
- candidate_next_move_available;
- blocked_missing_context;
- human_decision_needed;
- launch_packet_candidate_ready;
- check_job_candidate_ready;
- no_safe_next_move.

Console closure must be clear enough that the user knows whether to act, ask, verify, decide or stop.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/RUNTIME_CONSOLE_MODEL.md
