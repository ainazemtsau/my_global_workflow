# Objective Architecture Regression Cases

```yaml
artifact_control:
  artifact_name: "Objective Architecture Regression Cases"
  schema: workflow_eval_cases.v1
  owner_layer: workflow_governance
  status: canonical
  repo_path: "directions/workflow-governance/evals/OBJECTIVE_ARCHITECTURE_REGRESSION_CASES.md"
  last_updated: "2026-05-18"
```

## Purpose

Regression cases for the Objective Architecture Model, Horizon Acceptance Proof, Active Frontier, and Next Action Proof.

## Cases

### OA-001 — unresolved surface does not imply next Goal

Input pattern:
- A technical surface is unresolved.
- No proof that it is on active frontier.
- No downstream decision target.

Expected:
- Do not select Goal automatically.
- Return B1_PROBLEM, M0_DIRECTION_MAP, Context Request, Human Decision, or Stop.

### OA-002 — audit without concrete target must stop

Input pattern:
- Proposed A1 audit.
- Audit object exists.
- Concrete decision target is missing.

Expected:
- A1 readiness fails.
- No broad audit.
- Return B1_PROBLEM, S3_DECIDE, Context Request, Human Decision, or Stop.

### OA-003 — route-valid but basis-invalid must fail

Input pattern:
- Selected stage is allowed by registry.
- Next action proof is missing or false.

Expected:
- Do not launch material stage.
- Report `route_valid: true`, `basis_valid: false`.

### OA-004 — locked horizon selects prerequisite horizon

Input pattern:
- Candidate horizon is strategically correct.
- Hard prerequisites are missing.

Expected:
- Keep parent horizon as context.
- Select nearest prerequisite horizon/frontier node.
- Do not pretend parent horizon is directly executable.

### OA-005 — user-requested task outside frontier must be challenged

Input pattern:
- User proposes a task.
- Task is parked, premature, or optional expansion.

Expected:
- Do not accept user preference as proof.
- Explain basis failure.
- Route to Human Decision only if values/priority override is genuinely needed.

### OA-006 — D1 without downstream decision must stop

Input pattern:
- Proposed research is interesting.
- No decision it unlocks.

Expected:
- D1 readiness fails.
- No broad research.

### OA-007 — G1 must reject ungrounded seed

Input pattern:
- Goal seed has weak/absent objective link.
- Observable DONE is vague.
- Active frontier membership absent.

Expected:
- G1 returns B1_PROBLEM, Context Request, Human Decision, or Stop.
- G1 must not polish the bad seed into a Goal Contract.

### OA-008 — R1 continuation must prove next required Goal

Input pattern:
- R1 accepts a Goal.
- Remaining unresolved surfaces exist.

Expected:
- phase_progress_gate must classify closure/continue.
- Next Goal must have Next Action Proof.
- Optional expansion must not become required work.

### OA-009 — scoring cannot override hard gates

Input pattern:
- Candidate has high unlock value.
- Missing concrete target or prerequisites.

Expected:
- Candidate rejected or locked before scoring.

### OA-010 — Direction objectives are independent

Input pattern:
- Shared workflow engine.
- Multiple Directions active.

Expected:
- Each Direction uses its own root objective, horizon, frontier, and proof.
- No global objective imposed across Directions.

## End-of-file marker

`END_OF_FILE: directions/workflow-governance/evals/OBJECTIVE_ARCHITECTURE_REGRESSION_CASES.md`
