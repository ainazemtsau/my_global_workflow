# Transport and Interaction Protocol

status: candidate_draft

## Purpose

Этот файл описывает, как Workflow Runtime Rebuild переносит работу между чатами, Codex, GitHub, research agents, future providers и human actions.

Главная цель: работа не должна зависеть от памяти одного чата.

Каждая material work единица должна иметь:

1. вход — Launch Packet;
2. выполнение — Run через adapter или human action;
3. выход — Result Packet;
4. точный следующий шаг — Next Move;
5. acceptance отдельно от результата.

## Core rule

State lives in canonical storage / GitHub, not in chat memory.

Chat memory может помогать вести разговор, но не является source of truth. Если нужно понять accepted state, нужно смотреть canonical storage, verified repository files или явно переданный accepted record.

Project Files are context/cache, not truth.

Если Project Files конфликтуют с verified GitHub/canonical storage, canonical storage wins.

## What this protocol does not do

Этот Stage 2 protocol не определяет:

- production storage layout;
- Runtime Console details;
- detailed Signals / Handlers schema;
- Action Inbox cleanup rules;
- full machine schema;
- active runtime activation;
- Direction migration;
- Project Instructions rollout;
- product execution implementation.

## Basic lifecycle

```text
Launch Packet
→ material chat / adapter run / human action
→ Result Packet
→ exact Next Move
→ optional Acceptance Decision outside the chat result itself
```

Результат не становится Accepted State сам по себе.

Acceptance Decision должна быть явной. Она может принять, отклонить или вернуть результат на доработку.

## Start material chat algorithm

1. Parent/integration context выбирает один bounded target.
2. Для target формируется Launch Packet.
3. Launch Packet указывает source authority, supplied context, scope, boundaries, expected result, evidence and return destination.
4. Новый material chat проверяет, достаточно ли контекста.
5. Если контекста достаточно, chat выполняет bounded work.
6. Если контекста недостаточно, chat не угадывает state и возвращает blocked Result Packet.

Material chat must not start from vague memory such as:

- "continue where we left off";
- "do the next thing";
- "you know the workflow";
- "fix everything";
- "continue the project".

## Start material chat minimum context access check

At the start of material work, the adapter must check:

1. Do I know the target Direction / project / candidate package?
2. Do I know the current Work Contract?
3. Do I know the canonical source or verified source excerpts?
4. Do I know allowed and forbidden surfaces?
5. Do I know the expected output and evidence?
6. Do I know where the result returns?
7. Do I know what not to decide?

If any answer is no, the adapter must not invent missing state.

It should return:

```text
status: blocked
missing_context:
  - exact file/path/decision needed
reason:
  cannot verify source state safely
next_move:
  provide the missing context or verified source excerpt
```

## Close material chat algorithm

1. Summarize what was done.
2. State what was not done.
3. Provide evidence.
4. State source/read limitations.
5. State assumptions.
6. State unresolved decisions and residual risks.
7. Mark result as candidate unless accepted through a separate acceptance/update path.
8. Provide exact Next Move.

Every material chat ends with Result Packet + exact Next Move.

The chat must not end with only explanation. The user should not have to guess what to open, paste, verify, accept, or decide next.

## Launch child chat algorithm

Parent / Integration Chat may launch Child Chat only when:

- parent target is too broad for one chat;
- child work has its own bounded result;
- child output is needed for current parent synthesis;
- child work does not make parent-level final decisions;
- child result returns to parent.

Child Chat must receive a Launch Packet.

Child Launch Packet must include:

- parent target summary;
- child target;
- why the child result is needed;
- child in-scope boundaries;
- child out-of-scope boundaries;
- required evidence;
- exact return destination;
- what child must not decide.

Do not launch child chats for future topics, unrelated residuals, or mere thoroughness.

## Return child result algorithm

1. Child Chat returns Result Packet.
2. User pastes Child Result Packet into Parent / Integration Chat.
3. Parent classifies child output as candidate evidence.
4. Parent checks whether the child answered the bounded child target.
5. Parent either:
   - uses the result in parent synthesis;
   - asks for repair/missing evidence;
   - marks the child result unusable and explains why.
6. Parent remains responsible for parent-level synthesis and Next Move.

Child Chat does not accept parent result.

## Parent Recovery Block

If multiple child chats are launched, parent should provide a Parent Recovery Block.

Parent Recovery Block exists so the user can recover the parent state even if the parent chat is long or interrupted.

It should include:

- parent target;
- children launched;
- expected child results;
- what has already returned;
- what is still missing;
- how to resume synthesis;
- what must not be decided by child chats.

Parent Recovery Block is not needed for every ordinary work chat. It is only needed when child coordination creates recovery risk.

## Launch Codex algorithm

Codex is used only for bounded implementation packages.

Codex receives Codex Work Package, which is a specialized Launch Packet.

ChatGPT creates Codex Work Package only when it can specify:

- repository;
- base ref / branch;
- target branch policy;
- goal;
- allowed paths;
- forbidden paths;
- required changes;
- validation commands/checks;
- stop conditions;
- commit/push instructions if persistence is allowed;
- requested return fields.

Codex must not decide route, product meaning, acceptance, scope expansion or future roadmap.

Codex output remains candidate evidence until verified and accepted.

## Verify Codex result algorithm

ChatGPT verifies Codex Result Packet before any acceptance/update step.

Verification checks:

- branch name;
- commit SHA if applicable;
- changed files;
- allowed paths compliance;
- forbidden paths untouched;
- required content changes made;
- validation results;
- markdown EOF markers where relevant;
- residual risks;
- project refresh requirements if setup/project surfaces changed.

If evidence is missing, ChatGPT must ask for exact missing evidence or classify result as not verifiable.

No validation means no done claim.

## Choose exact Next Move algorithm

Next Move is selected by asking:

1. Is the result blocked?
   - Next Move: provide missing source, decision, access, or revised scope.

2. Does the result need parent synthesis?
   - Next Move: paste this Result Packet into the parent/integration chat.

3. Does the result need Codex implementation?
   - Next Move: launch Codex with the provided Codex Work Package.

4. Does the Codex result need verification?
   - Next Move: paste Codex Result Packet back into the verifying ChatGPT chat.

5. Does the candidate result need acceptance?
   - Next Move: run parent/integration review or explicit Acceptance Decision.

6. Is the work fully accepted and closed?
   - Next Move: open the next material chat with a new Launch Packet, or stop if no next work is selected.

Next Move is not Accepted State. It is a transport instruction.

## Working without GitHub access

If a provider cannot read GitHub:

1. It may use the Launch Packet and attached verified excerpts.
2. It must mark that it worked without direct GitHub read.
3. It must not claim repository state beyond supplied evidence.
4. It must request exact missing files if the supplied excerpts are insufficient.
5. It must return source limitations in the Result Packet.

Allowed fallback sources:

- exact source excerpts pasted by user;
- uploaded files explicitly classified as cache/context;
- Codex read-only output;
- human-provided verification notes.

Not allowed:

- guessing repository state;
- treating stale Project Files as truth;
- claiming accepted state from chat memory.

## Portability rule

A material run should be portable across devices and providers.

That means:

- Launch Packet should be copy-pasteable;
- Result Packet should be copy-pasteable;
- canonical source references should use repo/path/ref when possible;
- no required state should live only in one chat;
- evidence should be summarized with enough detail to verify later;
- Next Move should say exactly where the result goes.

## Anti-micro-step rule

Do not split work merely because a tool can continue in tiny increments.

A material chat should produce one meaningful result.

A Codex run should produce one bounded implementation package.

Bad split:

```text
Chat 1: decide filename.
Chat 2: decide headings.
Chat 3: write first paragraph.
Chat 4: write second paragraph.
```

Good split:

```text
Chat 1: design Stage 2 transport draft package.
Codex run: persist the accepted five Stage 2 markdown files.
Parent review: verify whether Stage 2 is complete enough for Stage 3.
```

A small step is allowed only when the work is genuinely blocked, risky, externally constrained, or needs a human decision before continuing.

## Terminal closure

Every material chat must end with one of these outcomes:

- ready_for_parent_review;
- ready_for_codex;
- needs_human_decision;
- blocked_missing_context;
- blocked_failed_validation;
- rejected_or_needs_rework;
- closed_no_next_move;
- next_material_chat_required.

The exact Next Move must be written in human-readable form.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/TRANSPORT_AND_INTERACTION_PROTOCOL.md
