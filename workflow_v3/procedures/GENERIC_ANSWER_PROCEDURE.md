# Generic Answer Procedure

status: active_procedure

canonical_role: registry entrypoint `generic_answer`

## Purpose

Use `generic_answer` as the readonly default guidance surface for lightweight answers, clarification, default guidance, and request-normalization that do not depend on current canonical repository state, Direction runtime state, accepted state, mutation, recovery, Codex/check/child/adaptor work, or current Next Move.

It may help the user understand a problem, clarify intent, compare options, normalize a request into a better START goal, or draft/tighten START wording. Routing guidance is allowed only as non-executing guidance; this procedure must not select, execute, or silently switch into a specialized procedure.

## Trigger / When to Use

- User asks a bounded, non-state-sensitive question.
- The answer can be given from stable context already present in the admitted prompt.
- The response does not require repository mutation, acceptance, runtime state, or current Next Move.
- User needs lightweight clarification, option explanation, default guidance, or START-goal drafting/tightening.

## When Not to Use

- Do not use when the answer depends on current repository or Direction runtime state.
- Do not use for acceptance, recovery, Codex, storage, or Next Move work.
- Do not use to mutate repository/runtime state, accept candidate work, persist storage, run recovery, launch Codex/check/child/adaptor work, or claim current accepted state.
- Do not use to execute, select, or silently switch into any specialized procedure.
- Do not use to continue material execution, perform hidden routing execution, or route a semantic next step as work.

## Required Inputs

- bounded lightweight question;
- enough non-state-sensitive context to answer without exact current source reads.

## Source Requirements

No exact repository source read is required by default. State limitations when exact source was not read.

If the answer depends on current repo/runtime state, STOP and escalate to registry lookup.

## Context Classification

Default classification is current human input plus non-state-sensitive context. If canonical source, accepted state, runtime state, Project Files cache/context, legacy_evidence, mutation authority, recovery evidence, Codex/check/child/adaptor output, or current Next Move becomes material, this procedure is the wrong entrypoint.

Routing guidance classification:

- allowed: non-executing explanation of possible registry fit, missing inputs, or START-goal wording;
- forbidden: selecting the entrypoint, starting RUN, launching child/adaptor work, treating guidance as a route decision, or continuing with specialized procedure work.

## Complexity Selector

- `inline`: default.
- `standard`: use only for a slightly longer explanation that remains non-state-sensitive.
- `research_backed`: allowed only when the user asks an up-to-date or external question and it remains non-state-sensitive.
- `checkpointed` and `delegated_or_tool_mediated`: not used by this procedure.

## Stage Cards

```text
stage_id: answer_fit
purpose: Confirm the question is lightweight and non-state-sensitive.
activation conditions: Always.
inputs: User question and available non-state-sensitive context.
required intermediate output: Fit decision and source limitation.
gate: PASS if no current repo/runtime state is needed; STOP if state-sensitive.
checkpoint rule: None by default.
expansion rule: Only bounded external research when the user asks for up-to-date/external information and no state-sensitive source is involved.
stop behavior: Escalate to registry lookup.
```

```text
stage_id: answer
purpose: Provide the bounded answer with limitations.
activation conditions: answer_fit passes.
inputs: Question, stable context, optional allowed external research.
required intermediate output: Answer draft with limitations.
gate: PASS if the answer stays within non-state-sensitive scope; PASS_WITH_RISK if limitations are material but acceptable.
checkpoint rule: None.
expansion rule: None.
stop behavior: Return escalation if the answer becomes state-sensitive.
```

## Gate Outcomes

- `PASS`: answer is lightweight and non-state-sensitive.
- `PASS_WITH_RISK`: answer is useful but limitations must be stated.
- `STOP`: answer depends on current repo/runtime state, acceptance, Codex, recovery, or current Next Move.

## Optional Expansion

No expansion by default. External research is allowed only when the user asks an up-to-date/external question and the answer remains non-state-sensitive.

## Research Policy

Research is forbidden unless the user asks an up-to-date/external question. Research must not be used to infer current repository, runtime, acceptance, or Next Move state.

## Checkpoint Policy

No checkpoint by default.

## Child / Adapter Policy

```text
child_call_policy:
  - never inside generic_answer
  - do not emit CHILD_PROCEDURE_CALL, UTILITY_CALL, Codex handoff, check job, storage packet, child chat, research child, or adaptor launch
  - do not verify child/adaptor returns
  - if child/adaptor work is needed, return explicit escalation instead of opening or implying the call
```

## Completion Contract

```text
completion:
  result: bounded lightweight answer, clarification, default guidance, START-goal help, or explicit escalation
  proof: answer avoids current-state claims and treats routing guidance as non-executing; limitations are stated
  blocked_if: question depends on repository state, Direction runtime state, accepted state, acceptance, mutation, storage, recovery, code-assistant/check/child/adaptor work, or current Next Move
```
## Output Contract

```text
answer:
limitations:
escalation_if_state_sensitive:
```

## Eval / Quality Checks

- Answer does not claim current repository or runtime state unless exact source was read under another procedure.
- Limitations name any missing exact source.
- Escalation is explicit when state-sensitive work appears.
- Routing guidance is explicitly non-executing and does not become specialized procedure selection.
- No child/adaptor call is emitted or implied inside `generic_answer`.

## Stop Conditions

- answer depends on current repo state;
- answer depends on Direction runtime state;
- answer depends on accepted state, acceptance, storage, Codex/check/child/adaptor work, recovery, or current Next Move;
- user requests mutation, execution, acceptance, storage, recovery, child/adaptor launch, or current-state verification;
- user asks for routing guidance that would require executing, selecting, or silently switching into a specialized procedure;
- material/state-sensitive routing is needed rather than non-executing guidance.

## Procedure Closure

Return the output contract directly for non-material inline answers. If lifecycle FINISH is active, close through CLOSURE_CHECK, FINISH_PACKET, and NEXT_CHAT_CARD or no_next_chat_needed continuation.

END_OF_FILE: workflow_v3/procedures/GENERIC_ANSWER_PROCEDURE.md
