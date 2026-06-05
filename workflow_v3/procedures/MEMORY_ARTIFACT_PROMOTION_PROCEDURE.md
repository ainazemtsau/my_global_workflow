# Procedure: Memory Artifact Promotion

title: Memory Artifact Promotion
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/MEMORY_ARTIFACT_PROMOTION_PROCEDURE.md
entrypoint: promote_memory_artifact
procedure_boundary: formation_chat

## purpose

Self-contained target spec for promoting a Memory Candidate to a Memory Artifact. The detailed procedure body is not authored yet.

## target_role

Promote a Memory Candidate to Memory Artifact only when reusable, source-backed, scoped, and bounded by when_to_load / when_not_to_use / refresh rules.

## workflow_integration

Keeps long-term memory useful without polluting context or replacing accepted state.

## when_to_use

- START selected `promote_memory_artifact`.
- A Memory Candidate needs promotion review.

## when_not_to_use

- Do not promote raw chat notes.
- Do not override canonical state.
- Do not create broad always-load memory.

## required_inputs

- Memory Candidate;
- source references;
- proposed scope of use;
- refresh/expiry expectations.

## future_body_scope

- review Memory Candidate;
- verify source refs;
- define scope_of_use;
- define loading and exclusion rules;
- define refresh/expiry;
- propose Memory Index update candidate using `workflow_v3/templates/MEMORY_INDEX_TEMPLATE.md` when promoted;
- return promoted Memory Artifact candidate.

## future_body_must_not

- promote raw chat notes;
- override canonical state;
- create broad always-load memory.

## required_outputs_when_authored

- promoted Memory Artifact candidate or blocked result;
- source references and loading rules;
- Memory Index update candidate if promoted;
- refresh/expiry rule;
- CLOSURE_CHECK;
- FINISH_PACKET;
- NEXT_CHAT_CARD or no_next_chat_needed.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes Memory Artifact promotion target role
  blocked_if: selected for execution before detailed body is authored
```
## stop_behavior_until_authored

```text
CLOSURE_CHECK:
  status: blocked
  result: PROCEDURE_BODY_NOT_AUTHORED
  evidence: canonical stub exists and describes target role
  not_done: author detailed body in separate bounded author_workflow_procedure run
FINISH_PACKET:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  evidence: canonical stub source and target role are present
  residual_risks: detailed body is not authored
NEXT_CHAT_CARD:
  title: Author this procedure body
  why: PROCEDURE_BODY_NOT_AUTHORED
  main_procedure_to_start: author_workflow_procedure
  context_to_paste: this procedure file and target role
  expected_result: authored detailed procedure body
  evidence_or_return_needed: updated procedure source with completion block
  start_instruction: START with author_workflow_procedure for this file
```

## procedure_closure_shape

- CLOSURE_CHECK
- FINISH_PACKET
- NEXT_CHAT_CARD or no_next_chat_needed

END_OF_FILE: workflow_v3/procedures/MEMORY_ARTIFACT_PROMOTION_PROCEDURE.md
