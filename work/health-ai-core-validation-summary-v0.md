# Health AI Core Validation Summary v0

Status: compact validation summary for Direction OS.

Scope:
- synthetic/minimal seed states only;
- no raw daily health data stored in Direction OS;
- no app, database, integration, recipe-manager, detailed diet, or full training program built or selected.

Verdict:
- The Health AI Core Contract v0 plus State Skeleton v0 are usable enough for review and for shaping the next nutrition/training-system slice.
- No blocking contradiction was found.
- Non-blocking gap: the contract implies guidance through the new-chat protocol and loops, while the skeleton makes guidance/governance first-class. A later contract revision should promote guidance/investigation explicitly if the core continues.

## Flow Validation

1. No weekly plan exists -> system guides plan creation.
   - Seed: profile and partial preferences exist; active weekly food plan is missing.
   - Expected route: `today_menu` detects missing plan and routes to `weekly_planning`.
   - Result: pass. Contract scenario 1 and skeleton fields `STATE_INDEX.missing_required_state`, `state/active_plans.md.plan_gaps`, and `weekly_planning` support explicit missing-state behavior and a short planning patch.

2. Today's menu requested -> system answers from plan/preferences or marks missing plan.
   - Seed: current weekly food plan, preferences, fallback meals, and recipe references exist.
   - Expected route: `today_menu` derives today's menu or proposes a patch when today's slot is absent.
   - Result: pass. Contract scenario 2 and skeleton records `nutrition/weekly_plans/<week-id>.md`, `state/preferences.md`, recipes, and active plan refs provide the needed state without choosing a recipe app.

3. Food log with skipped follow-ups -> system saves available data with confidence and gives same-day advice.
   - Seed: active food plan exists; owner gives an intentionally incomplete meal note and skips details.
   - Expected route: `food_log` records available data, skipped questions, confidence, plan match, and same-day advice.
   - Result: pass. Contract scenario 3 and skeleton template `nutrition/food_logs/<date>.md` include `skipped_questions`, `confidence`, `same_day_advice`, and Health-AI-only raw-log ownership.

4. Today's training requested -> system answers from current plan/safety state or marks missing plan.
   - Seed: current training/activity plan exists, with safety state either normal or cautionary.
   - Expected route: `today_training` reads plan and safety, outputs a bounded today session/activity, or marks missing/concerning state.
   - Result: pass. Contract training loop and skeleton records `state/training_activity.md`, `training/plan_summaries/<plan-id>.md`, `state/safety.md`, and the training output template cover current-plan, missing-plan, and caution cases without creating a full progressive program.

5. Review/incident -> system compresses summary and Direction OS escalation.
   - Seed: synthetic period summaries show either repeated adherence friction or a safety/training concern.
   - Expected route: `weekly_review` or `incident` writes compressed Health AI review/incident records and sends Direction OS only summary/problem/decision/CALL if needed.
   - Result: pass. Contract scenario 5 and skeleton templates for weekly review and incident include `direction_os_output` while excluding raw daily logs.

## Guidance/Governance Check

Check A: "What should I do next?"
- Seed: current phase exists, active plan gap exists, no urgent safety incident.
- Expected route: `guidance` reads index, strategy, current phase, next actions, summaries, and incidents; returns one next best action, why now, not-now boundary, fallback, and whether child work or Direction OS escalation is needed.
- Result: pass. Skeleton sections `governance/next_actions.md`, `procedures/guidance.md`, and `roles/registry.md` support health-director behavior while keeping one chat = one primary procedure.

Check B: bounded problem investigation.
- Seed: a repeated progress/adherence problem is visible in summaries, but cause is unclear.
- Expected route: `investigation` creates a bounded queue item with trigger, hypothesis, scope, questions, data needed, child-work need, result summary, proposed patches, and Direction OS escalation flag.
- Result: pass. Skeleton `governance/investigation_queue.md` and `procedures/investigation.md` cover the accepted health-team contour without broad unbounded research.

## Direction OS Boundary

Allowed Direction OS output:
- this compact validation summary;
- no blocker found;
- non-blocking contract-vs-skeleton gap noted;
- next review CALL.

Excluded from Direction OS:
- raw food log entries;
- raw training sets;
- raw daily check-ins;
- meal photos or meal descriptions;
- app-native exports.

END_OF_FILE: work/health-ai-core-validation-summary-v0.md
