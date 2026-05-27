---
artifact_control:
  namespace: workflow
  artifact_type: runtime_protocols
  status: single_material_run_chat_boundary_hardened
  owner: workflow_os
---

# Runtime Protocols

## Type Boundaries

Semantic primitives are Ledger, Obligation, Operator, Receipt, and Invariant.

Runtime protocols govern how primitives move.

Context Authority classifies loaded context before it is used as a claim basis.

Scope Triage classifies broad human input before material work.

Human Input Normalization converts clear natural-language human choices into structured Receipt fields.

Operator Independence prevents user urgency, examples, or channel mentions from bypassing workflow validity.

Human-Facing Run Closure packages terminal outcome and handoff for the user.

Single Material Run Chat Boundary keeps ordinary Direction chats to one material Operator run plus Codex verification/closure by default.

Recursive Child Handoff packages child requests, child results, and parent recovery for compound Obligations.

Adapters serialize protocol inputs and outputs.

Projections render accepted state for human use.

Storage preserves files, records, and tool state.

## Core Invocation Formula

```text
Operator(Obligation) -> Receipt
```

Atomic Run / Single Responsibility:

- only one active target Obligation may be worked materially at a time
- broad user input must be scope-triaged before material work
- material output may use only the input relevant to the current target Obligation and necessary dependencies
- off-scope but useful input must be parked as candidate/residual context
- candidate structure cannot bypass atomicity
- `one_obligation_scope` cannot pass if material output performs research, strategy, roadmap, execution, or structure creation not required by the target Obligation

Single Material Run Chat Boundary:

- ordinary Direction ChatGPT chats default to one material Operator run / one minimal bounded episode
- Atomicity governs both the active material target Obligation and the chat episode boundary
- a Direction, product, game, long-term goal, Horizon, roadmap, or implementation stream is not itself a bounded chat problem
- Codex result returns to the same chat only to verify and close the current run
- after commit verification, the next material target must launch in a new chat by default

The same chat may still answer non-material questions, verify failed commits, repair the current handoff, provide recovery prompts, or produce the exact next-chat prompt.

If a chat receives a compound Obligation that cannot be completed atomically, it must return `split_required` or produce child Obligations through Decompose.

Sequential internal steps are allowed only when they remain necessary to close the same chat episode target and each active target Obligation is declared.

## Context Authority

Purpose: classify loaded context by authority before it is used in an Operator invocation, Human Decision Card, Receipt, projection, or commit.

Every material Operator invocation must classify context before using it as claim basis.

Candidate context cannot be used as accepted state.

Project Files, projections, legacy files, and loaded domain material provide context only unless traced to committed Ledger state or current human input.

Output: context authority classification, required caveats, and blockers when authority is unknown or insufficient.

## Scope Triage Before Material Work

Purpose: classify broad, messy, anxious, speculative, or phase-jumping human input before material work begins.

Scope triage runs after Context Authority classification and before producing material output when input spans more than the target Obligation.

Required categories:

- `target_obligation`
- `in_scope_used`
- `necessary_dependencies`
- `parked_residual_context`
- `proposed_residual_obligations`
- `blocked_or_forbidden`
- `explicit_decisions`
- `candidate_examples`

The Operator may use `in_scope_used` and necessary dependencies for the current target Obligation.

The Operator must preserve useful off-scope concerns as parked residual context or proposed residual Obligations, without acting on them prematurely.

Scope triage must be recorded in the Receipt when the run produces candidate or commit-worthy state.

## Operator Independence / Effectiveness Over Agreement

Purpose: protect workflow validity and project effectiveness when user input contains urgency, anxiety, examples, brainstorming, or platform/channel/tool mentions.

User examples are candidate_context by default.

User urgency is not execution readiness.

User anxiety or brainstorming does not authorize phase jumping.

Platform, channel, or tool mentions are not commitments unless explicitly accepted through Receipt, Verify, and Commit.

The Operator optimizes for workflow validity, evidence quality, and project effectiveness, not immediate agreement.

## Human Input Normalization

Purpose: normalize clear terse, informal, spoken, messy, or unstructured human input into structured Receipt fields.

It runs before or during Human Gate and Receipt creation when user input is unstructured.

It converts clear natural-language human choices into structured Receipt fields.

It must preserve Context Authority.

It must not require users to answer in YAML or schema format when intent is clear.

It may apply explicit procedural defaults that preserve openness, delegate to child Obligations, or classify unresolved details as candidate/unknown.

It must not accept substantive claims that were not explicit in the selected option or current human input.

Output: normalized decision, selected option if any, defaults applied, fields not accepted, residual Obligations, and remaining ambiguity.

## Human-Facing Run Closure

Purpose: end every material Operator invocation with a clear human-facing terminal outcome and any needed handoff.

It runs at the end of every material Operator invocation.

It does not create new semantic work.

It packages terminal outcome and handoff for the user.

If a commit-worthy Receipt exists, it must provide a Codex Commit Handoff Card or an explicit deferral reason.

If another ChatGPT operator run is needed, it must provide a human-readable copy-paste prompt, not only an Obligation ID.

Output: terminal outcome, human-readable next action, optional Codex Commit Handoff Card, optional next-chat prompt, and technical appendix.

Single Material Run Chat Boundary is the default ordinary Direction user experience: one chat handles one material Operator run plus Codex verification/closure.

`CODEX_COMMIT_NEEDED` returns to the same chat only so the current Codex result can be verified, repaired if needed, and closed.

After a commit is verified, opening the next material Obligation requires `NEXT_CHAT_NEEDED` by default with an exact copy-paste launch prompt.

The parent chat must not start a different material target merely because the Direction, product, game, roadmap, or implementation stream is the same.

## Recursive Child Handoff

Purpose: create focused child Obligation requests for a compound parent Obligation and recover parent work if the parent chat is lost.

Recursive Child Handoff is runtime policy, not a semantic primitive.

Child runs are ordinary Operator invocations over child Obligations.

Child requests may run now, after dependencies, or after a blocking condition clears only when the child result is required for the current target Obligation.

Do not launch child chats for future topics, blocked phases, or mere thoroughness.

Parent must provide copy-paste child prompts, return instructions, and Parent Recovery Block when needed.

Child results return to the parent chat. The parent remains responsible for synthesis.

Output: child request cards, child result expectations, parent recovery block, and synthesis readiness rules.

## Obligation Admission

Purpose: decide whether a proposed work item may become an open Obligation.

Inputs:

- proposed obligation statement
- source Receipt or human request
- acceptance conditions
- verification policy
- constraints

Output: open Obligation, rejected proposal, or Context Request Card.

## Run Admission

Purpose: decide whether an Operator invocation may begin.

Checks:

- target Obligation is open
- Operator is eligible
- required context is present
- Commit Scope is known
- human and tool gates are satisfied or explicitly deferred
- forbidden actions are clear

Output: approved Launch Card or blocking card.

## Obligation Selection

Purpose: choose the next eligible open Obligation under the current Commit Scope, Horizon orientation, constraints, and verification policy.

Output: selected Obligation or no eligible Obligation.

## Operator Selection

Purpose: choose the Operator whose purpose, evidence policy, and gate requirements fit the selected Obligation.

Output: selected Operator and selection rationale.

## Decompose

Purpose: split a compound Obligation into child Obligations that can each be handled by one Operator invocation.

Decompose may create Child Obligation Request Cards.

Child requests may run now or after dependencies only when needed for the current target Obligation.

Child runs do not mutate Ledger, close parent Obligations, or make parent-level final decisions.

Recursion:

```text
compound Obligation -> child Obligations -> child Receipts -> Synthesize -> parent Receipt
```

## Invoke

Purpose: execute one approved Operator invocation over one Obligation.

Inputs are serialized by an Operator Launch Card or equivalent adapter.

Output is a Receipt Card or a blocking transport card.

## Verify

Purpose: test whether a Receipt satisfies its verification policy and preserves invariants.

Output: pass, fail, or needs input.

## Commit

Purpose: apply a verified Ledger delta to the target Commit Scope.

Commit accepts, rejects, or defers a Receipt's delta proposal.

## Commit Scope Policy

Purpose: define which part of the Ledger an approved commit may mutate.

Commit Scope is runtime authority policy over the Ledger. It is not a sixth semantic primitive.

## Synthesize

Purpose: combine accepted child Receipts into a parent Receipt without inventing unsupported claims.

Synthesis reads child result cards and accepted child Receipts where available.

Synthesis must cite child result IDs or child Receipt IDs.

Parent synthesis waits for required child results.

Missing required child results block synthesis.

Parent recovery works from a Parent Recovery Block plus child results already received.

## Project

Purpose: render accepted Ledger state into documents, dashboards, maps, or views.

Projection output must cite source Receipt IDs or mark claims unsupported or unresolved.

## Learn

Purpose: create learning Obligations or operator notes from failures, uncertainty, validation results, or repeated patterns.

Learning notes are not accepted state until represented by verified Receipts and committed.

## Transport

Purpose: serialize context and handoff between chats, humans, tools, and storage.

Transport artifacts are not authority unless they contain or point to valid Receipts.

## Verification Policy

Purpose: define required claim roles, evidence kinds, confidence labels, and verification checks for a Receipt.

Verification policy is typed by claim and risk, not a linear hierarchy.

## Human Gate Policy

Purpose: identify decisions that belong to the human and must not be written by the workflow.

Human gates block commit or invocation until the required decision is supplied.

## Tool / Execution Gate Policy

Purpose: define when external tools, Codex workspace activity, repository mutation, product execution, release, or irreversible action may be invoked.

Gate 1 treated Codex and product execution as future gated Operator concepts.

Gate 2 adds execution harness policy under `workflow/execution/` without adding semantic primitives.

No CodexRun may start without target binding, setup status, acceptance predicate, validation plan, allowed and forbidden surfaces, verification policy, and launch card.

No done claim is valid without a Validation Receipt.

Complex Technical Mission direct implementation is denied; mission-scale work must route through the complex mission protocol before slice execution.

END_OF_FILE: workflow/core/02_RUNTIME_PROTOCOLS.md
