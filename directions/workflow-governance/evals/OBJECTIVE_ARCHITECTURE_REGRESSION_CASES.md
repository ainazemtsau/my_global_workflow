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

Regression cases for the Objective Architecture Model, Horizon Acceptance Proof, Active Frontier, Next Action Proof, and Minimum Sufficient Solution Proof.

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

### OA-011 — user examples are not requirements

Input pattern:
- User gives examples of possible implementation.
- User says or implies examples are just thoughts, possible approaches, or initial ideas.

Expected:
- G1/E1 classify examples as `nonbinding_idea` unless explicitly marked as requirements.
- At least one considered solution shape is not structurally derived from the user's examples.
- No component is accepted solely because the user mentioned it.

### OA-012 — burden is a hard constraint, not a score

Input pattern:
- User says the main requirement is low effort, low friction, speed, simplicity, or "not геморно".
- Proposed solution adds recurring templates, logs, reviews, reports, multiple chats, or manual formatting.

Expected:
- Human Burden Budget is required.
- Higher-burden solution fails unless it prevents a concrete safety, evidence, persistence, or correctness failure that the lower-burden option cannot handle.
- Candidate scoring cannot compensate for failed burden gate.

### OA-013 — component without necessity is parked or cut

Input pattern:
- Proposed solution includes an extra template, persistent artifact, report, workstream, role, or chat split.
- Removing it does not break a current acceptance predicate.

Expected:
- Component Necessity Test fails.
- Component is cut or parked with activation trigger.
- It cannot remain as "probably useful later."

### OA-014 — minimality cannot destroy completeness

Input pattern:
- Scope cutting leaves only a fragment.
- Fragment does not produce one complete user-visible loop.

Expected:
- Overcut Guard fails.
- Workflow selects a thin complete loop, not a micro-task.
- `solution_minimal` cannot be true while `complete_enough` is false.

### OA-015 — simple baseline must be considered

Input pattern:
- Multiple implementation paths exist.
- Proposed solution jumps directly to structured workflow, automation, or multi-agent/process design.

Expected:
- Workflow considers a no-new-system/manual/lightweight baseline before structured or automated variants.
- Rejection of the simpler baseline states the concrete failure it cannot handle.

### OA-016 — future-proofing requires proof

Input pattern:
- Proposed solution adds flexibility, persistence, automation, reporting, or structure for possible future use.
- Current acceptance predicates do not require it.

Expected:
- YAGNI-style gate rejects, cuts, or parks the future-proofing component.
- Component can be kept only if current acceptance, safety, evidence, persistence, or correctness requires it.

### OA-017 — low-burden nutrition-like planning case

Input pattern:
- User wants menu planning and food/intake tracking with minimal effort.
- Proposed solution adds multiple templates, heavy reporting, or complex process structure.

Expected:
- Minimum Complete Outcome is defined as one usable loop, such as weekly menu proposal -> low-burden intake feedback -> weekly summary -> adjusted next menu.
- Human burden is treated as dominant constraint unless safety or medical accuracy overrides it.
- Photos/notes may be accepted as lower-burden input if they satisfy the current loop.
- Heavy templates, detailed reports, or multi-chat structure are cut or parked unless Component Necessity Test proves current need.

## End-of-file marker

`END_OF_FILE: directions/workflow-governance/evals/OBJECTIVE_ARCHITECTURE_REGRESSION_CASES.md`
