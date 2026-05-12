# WORKFLOW_EVAL_SUITE

This file defines audit lenses for Workflow Governance.

## Audit lenses

### runtime contract audit

Checks whether runtime packets, formalization control, repository patch behavior, and stage launch/return contracts remain coherent.

### lifecycle logic audit

Checks phase, goal, review, closure, router, and recovery transitions.

### UX/human burden audit

Checks whether the workflow asks too much of the user, produces wall-of-text, hides decisions, or fails to provide reviewable work product before formalization.

### context hygiene audit

Checks default loads, stage prompt request rules, Direction boundaries, and whether context is stale, excessive, or cross-contaminated.

### real usage friction audit

Checks issues observed in real Direction use, including confusing next routes, approval ambiguity, or Codex repository maintenance friction.

### external best-practice/research audit

Checks source-backed facts vs inference from external research and whether any workflow change is justified.

## Rule

Findings must go through `FINDING_REGISTER.md`. No repository patch until approval.
