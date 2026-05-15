# Stage Result Transport Template

```yaml
artifact_control:
  artifact_name: "Stage Result Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/STAGE_RESULT_PACKET.md"
  runtime_schema: stage_result.v1
  last_updated: "2026-05-13"
```

## Purpose

Defines the canonical transport template for a workflow stage result.

This file is a transport template. It is not a stage prompt and not routing authority.

## Branch / workstream result extension

Standard `stage_result.v1` remains the base stage-result packet.

A branch/workstream stage run that is launched under a parent Goal may return a compact workstream result using:

```text
workflow/transport/WORKSTREAM_RESULT_CARD.md
```

A Workstream Result Card is an input to parent synthesis. It is not a parent Goal review, parent Goal acceptance, Phase close, or shared state mutation.

## Transport authority boundary — AD-WF-RT-001

Route fields are snapshots only. They must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If a route snapshot conflicts with the registry, return route-conflict Context Request / B1_PROBLEM / Human Decision / Stop.

Packet fields in this template must remain compatible with `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md` until a later runtime-core reference cleanup changes packet-authority references.

## Transport invariants

- HTML is forbidden as transport.
- Use plain Markdown with YAML-style fields.
- Unknown extension fields must be tolerated by consumers.
- The result must not depend on private chain-of-thought.
- Any write request must be expressed through `repository_patch.v1`.
- A stage close must produce a next launch, context request, human decision, or stop.

## Canonical packet template

```yaml
workflow_packet: 1
type: stage_result
schema: stage_result.v1

stage:
  id:
  name:

return_state: DONE | NEEDS_INPUT | STUCK | PARTIAL | NOT_APPLICABLE
route:
next_stage:

direction_state_delta:
phase_state_delta:
goal_state_delta:
portfolio_delta:

human_decision_needed:
  yes_no:
  question:

what_changed:
  -

durable_decisions:
  -

temporary_context:
  -

open_questions:
  -

repository_patch:
  required: true | false
  summary:
  patch_id:

execution_log_entry:
  included: true | false
  target_log_path:
  persist: true | false

project_files_to_refresh:
  - file:
    reason:

context_for_next:
  carry_forward:
    -
  request_if_needed:
    -
  do_not_carry_forward:
    -

next_launch_card:
  created: true | false
  reason_if_not_created:

kernel_qa:
  status: PASS | PASS_WITH_EXCEPTIONS | BLOCKED
  exceptions:
    -

extensions: {}
```

## Validation anchors

- `workflow_packet: 1`
- `schema: stage_result.v1`
- `return_state`
- `repository_patch`
- `next_launch_card`

## End-of-file marker

`END_OF_FILE: workflow/transport/STAGE_RESULT_PACKET.md`
