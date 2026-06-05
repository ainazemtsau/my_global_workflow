# Generic Answer Procedure

status: active_procedure

## Purpose

Use `generic_answer` only for lightweight answers that do not depend on current canonical repository state, Direction runtime state, acceptance, Codex, recovery, or current Next Move.

## Trigger / When to Use

- User asks a bounded, non-state-sensitive question.
- The answer can be given from stable context already present in the admitted prompt.
- The response does not require repository mutation, acceptance, runtime state, or current Next Move.

## When Not to Use

- Do not use when the answer depends on current repository or Direction runtime state.
- Do not use for acceptance, recovery, Codex, storage, or Next Move work.
- Do not use to continue material execution or route a semantic next step.

## Required Inputs

- bounded lightweight question;
- enough non-state-sensitive context to answer without exact current source reads.

## Source Requirements

No exact repository source read is required by default. State limitations when exact source was not read.

If the answer depends on current repo/runtime state, STOP and escalate to registry lookup.

## Context Classification

Default classification is current human input plus non-state-sensitive context. If canonical source, accepted state, runtime state, Project Files cache/context, or legacy_evidence becomes material, this procedure is the wrong entrypoint.

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

## Completion Contract

```text
completion:
  result: bounded lightweight answer with limitations or explicit escalation
  proof: answer avoids current-state claims unless exact source was read; limitations are stated
  blocked_if: question depends on repository state, Direction runtime state, acceptance, mutation, recovery, code-assistant work, or current next move
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

## Stop Conditions

- answer depends on current repo state;
- answer depends on Direction runtime state;
- answer depends on acceptance, Codex, recovery, or current Next Move;
- user requests mutation, execution, or procedure routing beyond lightweight answer.

## Procedure Closure

Return the output contract directly for non-material inline answers. If lifecycle FINISH is active, close through FINISH_REQUEST, FINISH_PACKET, Result Packet, and Next Move Packet.

END_OF_FILE: workflow_v3/procedures/GENERIC_ANSWER_PROCEDURE.md
