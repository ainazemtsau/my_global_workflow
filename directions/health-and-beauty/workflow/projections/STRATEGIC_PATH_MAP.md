---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: strategic_path_map_projection
  projection_id: P-HB-STRATEGIC-PATH-MAP-2026-05-27
  status: projection_only
  owner: proof_carrying_workflow_os
---

# Health and Beauty Strategic Path Map Projection

Projection status: projection only, not accepted truth by itself.

Source receipts:

- R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26
- R-HB-CONSTRAINTS-DEFINE-2026-05-26
- R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27
- R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27

Accepted root objective:

Снижение массы тела на 35 кг: с текущих 125 кг примерно до 90 кг, при сохранении или минимальной потери физической силы, общей физической формы, гибкости/подвижности и функционального самочувствия; построение управляемой системы, где ChatGPT помогает вести питание, тренировки, трекинг, исследования и решения с минимальной нагрузкой на пользователя.

## Operating Model

This Direction needs two different layers:

```text
Health Workflow Project
└─ governs strategic decisions, Receipts, Horizons, boundaries, and major changes

Health Operating Project / Daily Ops
└─ later daily operational work
   ├─ food log: photo / voice / short text
   ├─ training log: Heavy / text / Apple Watch
   ├─ weight + body metrics
   ├─ daily check-in
   ├─ weekly review
   ├─ plan adjustment protocol
   ├─ research request protocol
   └─ escalation back to Workflow when a strategic decision is needed

The Health Operating Project is not created by this projection. It is a projected strategic path and likely first Horizon candidate.

Projection Map
Root Objective
└─ Минус 35 кг: 125 → ~90 кг while preserving strength/function
   ├─ Path A: Health Operating Project Bootstrap
   │  └─ create the future daily working project and operating protocols
   ├─ Path B: Baseline + Safety Measurements
   │  └─ collect starting data and safety boundaries
   ├─ Path C: Nutrition Operating System
   │  └─ strict menu, batch-prep, portions, fallback, food tracking
   ├─ Path D: Training + Activity Operating System
   │  └─ strength preservation, cardio/activity, mobility, joint-safe progression
   └─ Path E: Review + Adaptation + Research Loop
      └─ weekly review, plan adjustment, research requests, escalation rules
Strategic Paths
HB-PATH-A-HEALTH-OPERATING-PROJECT-BOOTSTRAP — Health Operating Project Bootstrap

Purpose: create the working operational project where the user will later track food, training, weight/body metrics, daily check-ins, weekly reviews, plan changes, and research requests. This is the bridge between proof workflow decisions and daily execution.

Candidate examples only:

ChatGPT Project setup for Daily Ops
project instructions for operational use
food intake protocol
training intake protocol
body metrics protocol
daily check-in protocol
weekly review protocol
plan adjustment protocol
research request protocol
escalation back to Workflow protocol
HB-PATH-B-BASELINE-SAFETY-MEASUREMENTS — Baseline + Safety Measurements

Purpose: collect initial measurements and safety guardrails required before precise diet, training, or high-load changes.

Candidate examples only:

waist circumference
blood pressure
resting heart rate
baseline weight trend
strength battery
cardio baseline
mobility baseline
safety stop checklist
HB-PATH-C-NUTRITION-OPERATING-SYSTEM — Nutrition Operating System

Purpose: build a strict, low-friction nutrition process with menu-first planning, batch-prep, preweighed portions, fallback rules, and simple tracking.

Candidate examples only:

strict menu
repeated meals
batch cooking
food photo/voice tracking
preweighed portions
deviation repair protocol
HB-PATH-D-TRAINING-ACTIVITY-OPERATING-SYSTEM — Training + Activity Operating System

Purpose: build the process for preserving strength, rebuilding conditioning, logging training, managing VR/cardio/bike work, and avoiding reckless joint loading.

Candidate examples only:

Heavy workout log
dumbbell strength tracking
Apple Watch activity/recovery signals
VR cardio
bicycle once purchased
walking/steps progression
mobility checks
HB-PATH-E-REVIEW-ADAPTATION-RESEARCH-LOOP — Review + Adaptation + Research Loop

Purpose: create the recurring mechanism for weekly review, plan adjustment, research requests, and escalation back to Workflow when a strategic decision is needed.

Candidate examples only:

weekly review
stuck/snvack diagnosis
research request
plan adjustment proposal
strategy escalation back to Workflow
Candidate Horizon Options

No Horizon is selected by this projection.

Candidate options for the next human decision:

H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP
Label: Health Operating Project Bootstrap
Reason: strongest first candidate because the user needs a separate operational project to actually run daily food/training/tracking work, while Workflow remains the strategic proof layer.
H2_BASELINE_AND_7_DAY_START
Label: Baseline + 7-day start
Reason: candidate if the user wants immediate practical movement before building the full operating project.
H3_NUTRITION_FIRST_STRICT_MENU_SYSTEM
Label: Nutrition-first strict menu system
Reason: candidate because nutrition is the main weight-loss lever and the user prefers strict menu/batch-prep.
H4_TRAINING_PRESERVATION_FOUNDATION
Label: Training-preservation foundation
Reason: candidate because success requires preserving strength and function.

Projection recommendation only:

H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP appears to be the strongest first Horizon candidate.
This is not a selected Horizon and must be confirmed by a separate human decision receipt.
Boundary

This projection does not create:

Health Operating Project implementation
ChatGPT Project setup or instructions
Daily Ops files
Horizon selection
Active Frontier
roadmap
diet plan
training plan
fast-start protocol
tracking implementation
product/project implementation
Codex/product execution

END_OF_FILE: directions/health-and-beauty/workflow/projections/STRATEGIC_PATH_MAP.md
