# Chat Types

status: candidate_draft

## Purpose

Этот файл описывает рабочие interaction contexts.

Chat type is not a core runtime primitive. Это практическая форма взаимодействия с adapter или человеком.

Главное правило: тип чата не создает Accepted State. Accepted State меняется только через explicit acceptance/update path.

## Summary

```text
Runtime Console Chat / status view — read-only overview boundary
Work Chat — one meaningful result
Parent / Integration Chat — coordinates bounded synthesis
Child Chat — bounded sub-result for parent
Codex Run — bounded implementation package
Research / Check Job — evidence or freshness check
Human Action — manual external action with confirmation/evidence
```

## 1. Runtime Console Chat / status view

### Purpose

Показать пользователю текущее состояние и возможные next moves без выполнения material work.

Stage 3 later may define details. Stage 2 only sets the boundary.

### Input

- canonical state references;
- latest accepted records;
- open candidate items if supplied;
- user question about status.

### Output

- read-only status summary;
- visible uncertainty;
- possible candidate next moves;
- no state mutation.

### May do

- summarize current state;
- identify missing context;
- show candidate options;
- say which Launch Packet is needed next.

### Must not do

- mutate Accepted State;
- execute work;
- accept results;
- launch Codex directly;
- promote Memory;
- run Signals/Handlers logic as authority;
- become a hidden runtime controller.

### Where result returns

To the user. If material work is needed, it returns a Launch Packet for a Work Chat or Parent / Integration Chat.

## 2. Work Chat

### Purpose

Produce one meaningful result for one Work Contract.

### Input

- Launch Packet;
- bounded Work Contract;
- source references or verified excerpts;
- in-scope and out-of-scope boundaries;
- expected output;
- evidence requirements.

### Output

- Result Packet;
- exact Next Move.

### May do

- analyze;
- draft;
- design;
- verify supplied evidence;
- create a Codex Work Package if implementation is needed and authorized;
- produce a blocked Result Packet if context is insufficient.

### Must not do

- continue from vague memory;
- change route or acceptance criteria by itself;
- treat its own output as accepted;
- start unrelated work;
- launch future topics;
- require the user to infer the next step.

### Where result returns

Usually to the user or parent/integration chat. If it creates a Codex Work Package, Codex result must return to the verifying ChatGPT chat.

## 3. Parent / Integration Chat

### Purpose

Coordinate a bounded target that may require child chats, Codex results, research checks, or human decisions.

### Input

- parent Launch Packet;
- current target;
- known source references;
- any child Result Packets;
- any Codex Result Packets;
- Parent Recovery Block if needed.

### Output

- integrated Result Packet;
- synthesis;
- acceptance candidate;
- exact Next Move.

### May do

- split current target into child chats;
- issue child Launch Packets;
- maintain Parent Recovery Block;
- synthesize child results;
- verify whether child results answer the parent target;
- decide next transport step.

### Must not do

- use child chats for unrelated future work;
- let child chats mutate parent state;
- silently accept child results;
- keep working indefinitely after parent target is complete;
- turn into a global project manager without a bounded target.

### Where result returns

To parent review, acceptance/update path, Codex if persistence is needed, or next material chat after closure.

## 4. Child Chat

### Purpose

Produce one bounded sub-result needed by a Parent / Integration Chat.

### Input

- child Launch Packet from parent;
- parent target summary;
- exact child question/task;
- required return format;
- what child must not decide;
- return destination.

### Output

- child Result Packet;
- evidence;
- limitations;
- exact instruction to paste result back into parent.

### May do

- answer the bounded child question;
- produce child evidence;
- identify blockers;
- suggest residuals for parent to consider.

### Must not do

- decide parent acceptance;
- mutate canonical state;
- expand scope;
- create unrelated roadmap;
- launch Codex unless parent explicitly authorized that child to produce a Codex Work Package.

### Where result returns

Back to Parent / Integration Chat.

## 5. Codex Run

### Purpose

Perform bounded repository implementation or read/verification work under a Codex Work Package.

### Input

- Codex Work Package;
- repository;
- base ref;
- branch policy;
- allowed paths;
- forbidden paths;
- required changes;
- validation checks;
- stop conditions;
- requested return fields.

### Output

- Codex Result Packet;
- changed files;
- commit SHA if applicable;
- validation output;
- residual risks;
- project refresh requirements if applicable.

### May do

- inspect repository files;
- edit allowed files;
- run validation commands;
- commit/push if authorized;
- report blockers.

### Must not do

- decide product meaning;
- decide workflow route;
- decide acceptance;
- edit forbidden paths;
- broaden scope;
- hide validation failures;
- claim done without evidence.

### Where result returns

Back to the ChatGPT verification chat that created or owns the Codex Work Package.

## 6. Research / Check Job

### Purpose

Gather evidence, verify freshness, compare options, or check a claim.

### Input

- research/check Launch Packet;
- research question;
- source requirements;
- allowed and forbidden sources;
- expected evidence format;
- return destination.

### Output

- Result Packet with findings;
- source list;
- confidence/limitations;
- exact Next Move.

### May do

- search;
- compare sources;
- summarize evidence;
- identify uncertainty;
- recommend whether evidence is sufficient for parent review.

### Must not do

- make acceptance decisions;
- mutate state;
- convert findings into roadmap automatically;
- overclaim beyond evidence;
- treat trend/opinion as accepted project fact.

### Where result returns

Back to Work Chat or Parent / Integration Chat.

## 7. Human Action

### Purpose

Represent a manual external action that AI cannot or should not perform.

Examples:

- account setup;
- purchase;
- permission grant;
- local device action;
- UI confirmation;
- manual validation;
- sensitive decision.

### Input

- clear human instruction;
- safety/permission boundary;
- expected confirmation;
- what evidence to report;
- return destination.

### Output

- human confirmation;
- observed evidence;
- screenshots/logs if relevant;
- limitations or failure note.

### May do

- perform external manual step;
- confirm outcome;
- provide evidence.

### Must not do

- be silently assumed complete;
- create accepted state without explicit confirmation;
- be replaced by AI guess;
- require YAML from the user.

### Where result returns

Back to Work Chat, Parent / Integration Chat, or acceptance/update path.

## Practical rule

When unsure which type to use:

- one bounded result → Work Chat;
- multiple bounded sub-results for current target → Parent / Integration Chat + Child Chats;
- repository implementation → Codex Run;
- evidence/freshness → Research / Check Job;
- external/manual/sensitive step → Human Action;
- only "what is going on?" → Runtime Console Chat / status view.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/CHAT_TYPES.md
