# E1 Execution Brief — Project `Питание` operational setup v0

```yaml
artifact_control:
  artifact_name: "E1 Execution Brief — Project Питание operational setup v0"
  schema: execution_brief.v1
  owner_layer: goal_evidence
  direction: directions/health-and-beauty
  phase_id: ai-nutrition-operating-layer
  goal_id: nutrition-project-operational-setup-v0
  stage_id: E1_EXECUTION_BRIEF
  status: formalized
  created_at: "2026-05-18"
```

## 1. Route decision

Selected next route: `F0_FAST_DIRECT`.

Execution topology: `single_direct`.

F0 is the smallest safe route because the next execution slice is one bounded, reversible, text-artifact setup package with concrete validation checks. It does not require nutrition research, a storage/tool architecture decision, Codex product/project execution, graph/wave planning, or Phase close.

The long-lived Project `Питание` setup package must be stored as a Direction-level setup asset:

```text
directions/health-and-beauty/project_setup/pitanie/PROJECT_PITANIE_SETUP_PACKAGE.md
```

The active Goal folder stores only workflow evidence and pointers, not the long-lived setup package.

## 2. Objective

Prepare a manual-install setup package for a separate ChatGPT Project named `Питание`.

The package must let the user manually:

1. create a new ChatGPT Project `Питание`;
2. paste Project Instructions;
3. upload or attach the setup package as Project source/context;
4. start the first Project chat using a bootstrap prompt;
5. initialize Nutrition Base / missing inputs / Active Cycle behavior without turning the process into mandatory detailed food logging.

This Goal prepares setup/protocol artifacts and validation dry-runs. It does not physically create the ChatGPT Project and does not claim the Project is installed.

## 3. Smallest safe slice

F0 must create one primary artifact:

```text
directions/health-and-beauty/project_setup/pitanie/PROJECT_PITANIE_SETUP_PACKAGE.md
```

Required sections:

1. Project Instructions for `Питание`;
2. Bootstrap prompt / first chat prompt;
3. Nutrition Base / Snapshot template;
4. Menu Preferences template;
5. Active Cycle object;
6. Tracking Protocol;
7. Review & Sync Protocol;
8. Manual install guide;
9. Dry-run test pack.

Missing baseline or preferences must not block the setup package. F0 must represent missing data as explicit missing inputs, unknown/defaulted fields, and confidence labels.

## 4. Acceptance → validation map

| Acceptance-floor item | Artifact/check | Evidence required |
|---|---|---|
| Project Instructions drafted | `PROJECT_PITANIE_SETUP_PACKAGE.md` contains a copy-pasteable Project Instructions block | Read-back confirms Project role, boundaries, low-friction tracking, and forbidden clinical/heavy-tracking behavior |
| Nutrition Base / Snapshot drafted or missing inputs explicit | Package contains Nutrition Base / Snapshot template | Read-back confirms known/unknown/defaulted/confidence fields and no invented baseline |
| Menu Preferences drafted or missing inputs explicit | Package contains Menu Preferences template | Read-back confirms missing inputs and no MacroFactor/heavy-ledger revival |
| Active Cycle structure drafted | Package contains menu, shopping list, recipes, prep plan, storage, fallback, replacement logic | Read-back confirms all required subsections |
| Tracking Protocol drafted | Package covers photo, voice, text, approximate/exact, unanswered questions, pending/unknown/defaulted fields, confidence impact | Read-back confirms normal menu-following is not mandatory logging |
| Review & Sync Protocol drafted | Package contains day/week review and durable sync/update packet | Read-back confirms no unverified tool/storage binding |
| 2–3 scenarios paper-tested or dry-run | Package contains cycle planning, meal-event, missing-answer dry-runs; optional review/sync dry-run | Read-back confirms dry-runs are validation examples, not real diet prescription |

## 5. F0 implementation sequence

1. Load this E1 brief and the shaped Goal Contract / Working Context.
2. Load or request the prior design/protocol artifact if needed:

   ```text
   directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0/03_AI_NUTRITION_OPERATING_LAYER_V0.md
   ```

3. Draft the package at the Direction-level setup path.
4. Keep the package copy-pasteable for manual Project installation.
5. Include a bootstrap prompt that starts a fresh Project `Питание` chat without requiring perfect baseline data.
6. Include dry-runs as validation scenarios only.
7. Do not generate a real user menu/diet unless separately routed and approved.
8. Validate by read-back anchors and acceptance map.

## 6. Scope lock

Allowed:

- create the Direction-level setup package;
- include Project Instructions;
- include bootstrap prompt;
- include Nutrition Base / Snapshot template;
- include Menu Preferences template;
- include Active Cycle structure;
- include Tracking Protocol;
- include Review & Sync Protocol;
- include manual install guide;
- include 2–3 dry-runs.

Forbidden:

- creating the ChatGPT Project inside workflow;
- claiming Project `Питание` is installed;
- concrete diet/menu prescription as the default deliverable;
- clinical or disease-specific nutrition;
- MacroFactor-centered workflow as default;
- mandatory calorie/macro ledger;
- food database/API/import automation;
- huge recipe vault;
- full body-transformation plan;
- training/cardio/recovery/supplement decisions;
- Phase close.

## 7. Context requirements for F0

Required:

- this E1 brief;
- active Goal Contract / Working Context;
- active Direction Project Files 00–08;
- runtime core and stage registry;
- exact F0 stage prompt.

Request if needed:

- prior AI Nutrition Operating Layer v0 design/protocol artifact;
- existing menu or old nutrition card;
- nutrition baseline and preferences;
- kitchen equipment notes;
- recipe/prep notes;
- storage/tool preference notes.

Missing baseline/preferences are not blockers. Missing required protocol context is a blocker only if F0 cannot safely avoid inventing setup rules.

## 8. Stop conditions for F0

Stop or return Context Request if:

- exact `F0_FAST_DIRECT` prompt is unavailable;
- required Goal Contract / Working Context is unavailable or contradictory;
- F0 cannot access enough prior protocol context to avoid inventing the nutrition operating model;
- user asks for clinical/disease-specific diet;
- user asks for real menu/diet prescription rather than setup package;
- current platform-specific UI claims are required but cannot be verified;
- storage/tool automation is required before setup;
- target path changes away from Direction-level setup asset without human decision;
- any patch would touch sibling Directions or runtime/shared workflow files.

## 9. Next-stage formalization control

E1 approval formalizes this execution brief only.

F0 artifact formalization is not pre-approved. F0 must first produce a reviewable package preview / planned patch unless the user explicitly approves direct formalization in the F0 stage chat.

F0 target artifact:

```text
directions/health-and-beauty/project_setup/pitanie/PROJECT_PITANIE_SETUP_PACKAGE.md
```

## 10. End state expected after F0

F0 is successful when the Direction-level setup package exists, passes read-back validation, and contains a manual install guide that the user can follow to create Project `Питание`.

Parent Goal review via `R1_GOAL_REVIEW_DISTILL` becomes appropriate only after the setup package and dry-runs satisfy the active Goal acceptance floor.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/02_EXECUTION_BRIEF.md`
