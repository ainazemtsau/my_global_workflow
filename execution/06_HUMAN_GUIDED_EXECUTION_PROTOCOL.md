---
artifact_control:
  namespace: workflow
  artifact_type: human_guided_execution_protocol
  status: gate_2_initial
  owner: workflow_os
---

# Human-Guided Execution Protocol

## Purpose

Human-guided execution is used for website, app, account, purchase, local tool, device, external UI, credential, permission, or manual tasks where automation is unsafe, unavailable, or inappropriate.

The workflow may guide.

The human performs sensitive or manual action.

Human confirmation receipt is required before the workflow treats the action as completed evidence.

## Human Action Card

A Human Action Card is required before asking the human to act.

It must include exact steps, expected visible result, stop conditions, evidence to return, and a human confirmation receipt section.

## Stop Conditions

Stop and return for guidance when any of these appear:

- irreversible action
- payment or purchase
- permission prompt
- secret exposure
- UI mismatch
- unexpected warning
- validation mismatch

## Confirmation

Human confirmation may support a Receipt only when the confirmation includes what was done, what was observed, evidence returned, deviations, and whether any stop condition appeared.

END_OF_FILE: execution/06_HUMAN_GUIDED_EXECUTION_PROTOCOL.md
