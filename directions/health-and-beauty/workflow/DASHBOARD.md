---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: dashboard_projection
  status: h1_baseline_measurements_collected_downstream_not_started
  owner: proof_carrying_workflow_os
---

# Health and Beauty Dashboard

Direction: Health and Beauty

Proof state: Baseline Measurements collected; downstream work not started.

Root objective: Снижение массы тела на 35 кг: с текущих 125 кг примерно до 90 кг, при сохранении или минимальной потери физической силы, общей физической формы, гибкости/подвижности и функционального самочувствия; построение управляемой системы, где ChatGPT помогает вести питание, тренировки, трекинг, исследования и решения с минимальной нагрузкой на пользователя.

Accepted receipts:

- R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26
- R-HB-CONSTRAINTS-DEFINE-2026-05-26
- R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27
- R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27
- R-HB-STRATEGIC-MAP-PROJECTION-CREATE-2026-05-27
- R-HB-HORIZON-SELECT-2026-05-27
- R-HB-H1-MINIMAL-DAILY-OPS-CORE-DEFINE-2026-05-27
- R-HB-H1-PROGRAM-BLUEPRINT-DEFINE-2026-05-27
- R-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE-2026-05-27
- R-HB-H1-NEXT-BOUNDED-RUN-SELECT-2026-05-27
- R-HB-H1-FIRST-PROGRAM-BLUEPRINT-ACTIVATE-FOR-DAILY-OPS-2026-05-27
- R-HB-H1-AFTER-ACTIVATION-NEXT-BOUNDED-RUN-SELECT-2026-05-28
- R-HB-BASELINE-MEASUREMENTS-COLLECT-2026-05-28

Constraints:

- accepted by R-HB-CONSTRAINTS-DEFINE-2026-05-26

Success semantics:

- accepted by R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27

Objective delta:

- resolved by R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27

Strategic Path Map:

- projection committed at directions/health-and-beauty/workflow/projections/STRATEGIC_PATH_MAP.md
- primary projected path: Health Operating Project Bootstrap

Selected Horizon:

- H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP
- selected by R-HB-HORIZON-SELECT-2026-05-27
- selection intent: MINIMAL-USABLE-CORE-FIRST / Minimal usable Daily Ops core first.
- scope boundary: Horizon selection only; downstream implementation not started.
- downstream implementation: not_started

Daily Ops Core:

- Daily Intake Gateway
- Food Event Protocol
- Training Event Protocol
- Plan Authority Contract
- Tool Abstraction Contract
- GitHub-backed State Contract
- Context Pollution Control
- Review / Escalation Gate

Program Blueprint Route:

- route_id: HYBRID_BASELINE_INFORMED_RESEARCHED_STARTER_BLUEPRINT
- authority: future Workflow-approved Program Blueprint receipt
- tools/apps/templates: input/evidence/tool surfaces only, not authority
- external trainer/dietitian: optional review/escalation, not hard requirement
- baseline: useful input, not hard blocker for route selection
- downstream implementation: not_started

First Program Blueprint:

- blueprint_id: HB-H1-FIRST-PROGRAM-BLUEPRINT-CANDIDATE-2026-05-27
- status: limited Daily Ops authority for boundaries/gates/escalation/Plan Authority Contract only
- nutrition: principles only; no calories, macros, meals, menu, recipes, or shopping list
- training: principles only; no exercises, sets, reps, sessions, split, progression, 12-week or annual plan
- gym: available optional future training surface via bicycle commute
- bicycle commute: user-estimated about 30 minutes one way; future plan must account for it as possible load/recovery factor
- baseline: required-now fields accepted; unresolved fields gated for future prescription
- review_gates: authority, medical safety, nutrition conversion, training conversion, baseline sufficiency, review escalation, implementation
- downstream implementation: not_started

Latest closed Obligation:

- O-HB-BASELINE-MEASUREMENTS-COLLECT
- admitted by R-HB-H1-AFTER-ACTIVATION-NEXT-BOUNDED-RUN-SELECT-2026-05-28
- status: closed / accepted
- satisfied by R-HB-BASELINE-MEASUREMENTS-COLLECT-2026-05-28
- scope: baseline collection only; no prescriptions, implementation, roadmap, Active Frontier, Codex/product execution, or legacy import

Tool boundary:

- Hevy / H-E-V-Y is candidate tool surface for workout logging/social/training records, not accepted program authority.
- HomeLab and Mealie/Miali Recipes are optional candidate infrastructure, not hard requirements.

Baseline Measurements:

- anthropometrics collected: 35M, 182 cm, 125 kg, BMI estimate 37.7, target weight context about 90 kg
- waist/photos policy: unknown/deferred
- safety: no chronic conditions, hypertension, cardiovascular conditions, diabetes, or specific joint limits reported; BP/HR/labs/medications unknown/deferred and not waived
- activity/training: low steps, very low recent training, prior strength/VR/boxing/Beat Saber/cardio/P90X/judo/martial arts experience, about 10 pushups; formal strength/cardio/mobility checks deferred/gated
- schedule/tracking capacity: high time availability for about 6 months, ChatGPT-first photo/voice/short text tracking, low manual burden; exact weekly schedule and maximum daily tracking minutes unknown/deferred
- gym/bike practicals: gym access via bicycle commute recorded as optional future surface; gym not required now; about 30 minutes one way user estimate; exact distance, route safety, parking/storage, weather, membership, equipment, and facilities unknown/deferred

Open critical Obligations:

- none

Proposed next bounded runs:

- O-HB-H1-NUTRITION-PLAN-CREATE: not admitted
- O-HB-H1-TRAINING-PLAN-CREATE: not admitted
- O-HB-H1-DAILY-OPS-IMPLEMENTATION-READINESS-DEFINE: not admitted
- O-HB-H1-DAILY-OPS-CHATGPT-PROJECT-SETUP: not admitted

Forbidden now:

- Active Frontier selection
- roadmap
- Codex/product execution
- product/project implementation
- ChatGPT Project setup
- Health Operating Project implementation
- diet/training prescription as accepted plan
- meal plan
- calorie/macro prescription
- training plan
- gym schedule
- cycling prescription
- accepted 12-week plan
- annual plan
- tracking implementation
- legacy import

Next valid run:

- none admitted by this commit unless future bounded run is created by later human input

Projection warning: Strategic Path Map remains projection context. The selected Horizon, Minimal Daily Ops Core operating shell, Program Blueprint Route, first Program Blueprint limited Daily Ops authority, and baseline measurement collection are accepted by Receipt, but this commit does not create Active Frontier, roadmap, execution, ChatGPT Project setup, Health Operating Project implementation, diet/training prescription, nutrition plan, meal plan, calorie prescription, macro prescription, training plan, gym schedule, cycling prescription, accepted 12-week plan, annual plan, tracking implementation, or legacy import.

END_OF_FILE: directions/health-and-beauty/workflow/DASHBOARD.md
