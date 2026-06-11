---
artifact_control:
  namespace: workflow
  artifact_type: validation_protocol
  status: gate_2_initial
  owner: workflow_os
---

# Validation Protocol

## Purpose

Validation is an Obligation, not an afterthought.

Every execution plan must define a stack-specific validation profile without hardcoding one stack.

Unity, Web, Python, mobile, data, infrastructure, and document pipelines are examples only.

## Validation Ladder

Validation levels:

- L0 self-check
- L1 static / compile / lint / type / schema
- L2 unit
- L3 integration
- L4 runtime
- L5 user-visible / screenshot / manual / UI/gameplay
- L6 regression
- L7 independent review / subagent

Each required level must pass or block commit.

Each omitted level must be marked `not_required` with a reason.

## Validation Receipt

Validation must return a Validation Receipt that records the required/omitted matrix, commands or checks run, evidence, failures, validation gaps, and whether commit is allowed.

No validation receipt -> no done.

## Validation Gap

If the environment cannot run validation, return `validation_gap`.

When the gap requires external local access, credentials, UI action, payment, permission, or sensitive manual operation, emit a Human Action Card.

Validation gaps block done claims unless an accepted verification policy explicitly permits a narrower partial result.

END_OF_FILE: workflow/execution/04_VALIDATION_PROTOCOL.md
