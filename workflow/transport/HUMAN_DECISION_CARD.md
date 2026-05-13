# Human Decision Transport Template

```yaml
artifact_control:
  artifact_name: "Human Decision Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/HUMAN_DECISION_CARD.md"
  runtime_schema: human_decision.v1
  last_updated: "2026-05-13"
```

## Purpose

Defines the canonical transport template for a human-owned decision.

Use this when the workflow needs an explicit user conclusion before it can safely continue.

## Transport authority boundary — AD-WF-RT-001

This template is not routing authority. Route fields are snapshots only.

The registry remains authoritative for stage IDs and normal stage-to-stage routing.

## Transport invariants

- HTML is forbidden as transport.
- Use plain Markdown with YAML-style fields.
- Unknown extension fields must be tolerated by consumers.
- Do not write the user's conclusion for them.
- Present options clearly and state tradeoffs.
- Do not default to destructive, global, irreversible, or active-workflow-changing actions.

## Canonical packet template

```yaml
workflow_packet: 1
type: human_decision
schema: human_decision.v1

decision:
  question:
  why_needed:
  blocking: true | false

options:
  - id:
    label:
    tradeoff:
    consequence:

recommendation:
  option_id:
  rationale:
  confidence: low | medium | high

what_changes_based_on_answer:
  - if:
    then:

after_decision:
  action: continue_current_stage | run_stage | regenerate_launch_card | stop
  stage_id:

extensions: {}
```

## Validation anchors

- `workflow_packet: 1`
- `schema: human_decision.v1`
- `decision`
- `options`
- `after_decision`

## End-of-file marker

`END_OF_FILE: workflow/transport/HUMAN_DECISION_CARD.md`
