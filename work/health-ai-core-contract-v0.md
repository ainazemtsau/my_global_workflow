# Health AI Core Contract v0

Status: minimal contract for the first Health AI System core slice.

Basis:
- `live/health/CHARTER.md`
- `live/health/TREE.md`
- `live/health/NOW.md`
- `live/health/history/2026-06-13-s-health-starter-kit-t-2-guide-003.md`
- `live/health/history/2026-06-13-s-health-ai-core-shape-001-approval.md`

Owner inputs used:
- Owner wants AI chats from anywhere to answer "menu today" and "training today" from stored state.
- Owner wants missing weekly plans detected and turned into a guided planning flow.
- Owner wants food logging from text, voice, or photo-style description, with useful follow-up questions that may be skipped.
- Owner wants the system to save available data with confidence and give same-day advice.
- Owner expects recipes to be durable stored artifacts, likely GitHub-backed initially.
- Owner rejected polishing `work/health-starter-kit-v0.md`; this contract does not revive that artifact.

## 1. Contract Purpose

Health AI System is the operational health layer inside the `health` direction. Its job is to keep working health state, support useful AI chats, and later connect to specialized tools without making Direction OS a diary.

This v0 contract defines:
- source-of-truth boundaries;
- minimal state model;
- operating protocol for new AI chats;
- planning, menu, training, food-log, recipe, and review loops;
- explicit non-goals and cut list;
- five dry-run scenarios for cross-chat continuation and missing-state behavior.

This contract is not an implementation, app design, diet plan, training program, or integration decision.

## 2. Source-of-Truth Boundaries

### Direction OS

Direction OS is the strategic source of truth for the `health` direction.

It may store:
- mission, goals, success criteria, constraints, lenses;
- active bets, tasks, decisions, CALLs, reviews, incidents, and summaries;
- accepted strategic facts in `knowledge/` if later created.

It must not store:
- raw daily food logs;
- raw daily training sets;
- raw daily activity streams;
- raw body-weight diary rows;
- photos or photo-derived raw meal records;
- app-native exports except as summarized evidence for a review.

Direction OS receives only:
- compact summaries;
- problems and incidents;
- strategic decisions;
- next CALLs;
- review outcomes.

### Health AI System

Health AI System is the operational source of truth for daily and weekly health work.

It may store:
- owner profile and durable constraints;
- preferences, equipment, food patterns, cooking capacity, and adherence notes;
- active weekly food plan, current menu, substitutions, and fallback meals;
- food-log entries and confidence levels;
- recipe cards and recipe feedback;
- current training/activity plan and today's training output;
- safety flags, fatigue/pain notes, and plan constraints;
- review summaries, incidents, and pending patches;
- import summaries or pointers from future integrations.

Initial storage is expected to be GitHub-backed files or equivalent durable artifacts. The contract does not choose the repository, file layout, database, or app.

### Future Integrations

Specialized tools may later own tool-native raw data:
- strength training app, e.g. Hevy-like;
- bike or conditioning tracker, e.g. Strava-like;
- wearable or heart-rate source;
- VR activity source;
- recipe or meal-planning manager.

In v0, none of these tools is selected. Health AI System may define import points and summary fields, but must not require any specific integration to operate.

### AI Chats

An AI chat is not a source of truth by itself.

A chat may:
- read the current Health AI state packet or relevant files;
- answer from the state it actually sees;
- ask limited follow-ups;
- propose state patches;
- produce summaries, decisions, or CALLs for Direction OS when strategically relevant.

A chat must not:
- invent stored state;
- silently overwrite state;
- require raw logs to be copied into Direction OS;
- treat an old chat transcript as more authoritative than current state files;
- make medical prescriptions.

## 3. Minimal State Model

The exact skeleton is the next task. This contract fixes the minimum record families and ownership rules.

### Profile

Purpose: durable facts used by many loops.

Contains:
- basic owner profile facts already accepted in the health charter;
- standing constraints and safety posture;
- equipment and environment facts;
- medical-safety caution fields, without pretending to diagnose.

Source of truth: Health AI System, with strategic constraints mirrored from Direction OS when needed.

### Preferences

Purpose: keep menus, recipes, training, and adherence outputs owner-specific.

Contains:
- food likes/dislikes and cooking preferences;
- available appliances and meal-prep capacity;
- preferred friction level;
- activity preferences and avoidance notes;
- adherence failure patterns and fallback preferences.

Source of truth: Health AI System.

### Metrics Summaries

Purpose: support decisions without turning Direction OS into a metric diary.

Contains:
- weekly or period summaries for weight, activity, training, adherence, energy, hunger, fatigue, and issues;
- summary confidence and source pointers;
- trend notes and review flags.

Source of truth: Health AI System. Direction OS receives only compressed summaries during reviews or incidents.

### Active Plans

Purpose: let any new chat answer "what should I eat/train today?"

Contains:
- current weekly food plan, if one exists;
- current training/activity plan, if one exists;
- today's menu/training derivable from those plans;
- plan status, date range, assumptions, and missing-state flags.

Source of truth: Health AI System.

### Food Logs

Purpose: record what was eaten enough to support same-day advice and later review.

Contains:
- text/voice/photo-style description as provided;
- optional follow-up answers;
- skipped questions;
- estimated meal structure and confidence;
- same-day advice given;
- link to affected plan/day if relevant.

Source of truth: Health AI System. Raw food logs never go into Direction OS.

### Recipes

Purpose: make repeatable food artifacts durable.

Contains:
- recipe name, ingredients, portions, preparation steps, tags;
- owner fit notes and substitutions;
- rough nutrition estimate if available, with confidence;
- feedback and revision history.

Source of truth: Health AI System. A future recipe manager may become the UI, but is not selected in v0.

### Training and Activity State

Purpose: answer today's training/activity request and protect safety.

Contains:
- current plan;
- available equipment and location options;
- safety flags and pain/fatigue notes;
- completed-session summaries or imported summaries;
- missing-plan or missing-safety-state flags.

Source of truth: Health AI System. Raw sets or app-native streams may live in a future specialized tool.

### Feedback

Purpose: turn owner friction into state changes.

Contains:
- what did not fit: taste, hunger, prep time, boredom, pain, fatigue, motivation, logistics;
- severity and recurrence;
- recommended state patch or decision.

Source of truth: Health AI System. Direction OS sees only strategic or repeated problems.

### Reviews and Incidents

Purpose: compress operational reality into decisions.

Contains:
- period reviewed;
- summary of adherence, outcomes, friction, safety signals, and blockers;
- proposed changes;
- whether Direction OS escalation is needed.

Source of truth: Health AI System, with selected summaries copied into Direction OS through review/pulse/work results.

### Pending Patches

Purpose: preserve proposed changes until a writer or owner-approved mechanism applies them.

Contains:
- target record;
- proposed change;
- reason;
- source chat/session;
- confidence;
- owner approval requirement, if any.

Source of truth: Health AI System.

## 4. New-Chat Operating Protocol

Every new Health AI chat follows this protocol before producing operational advice.

1. Identify the requested loop.
   - Planning, menu, training, food-log, recipe, review, incident, or unknown.

2. Load only the needed state.
   - Always check the current date and the state timestamp.
   - Read the contract and the relevant state packet or files.
   - If state is unavailable, say exactly what is missing.

3. State the source boundary.
   - Answer from Health AI System state.
   - Do not request raw logs for Direction OS.
   - Do not treat chat memory as source of truth.

4. Handle missing state explicitly.
   - If no weekly plan exists, start the planning loop instead of inventing today's menu.
   - If no training plan exists, start the training-plan creation or fallback loop instead of inventing a full program.
   - If safety state is missing or concerning, use guarded advice and escalate when needed.

5. Ask only decision-changing follow-ups.
   - Keep follow-ups limited.
   - Mark every follow-up as skippable unless it is needed for safety.
   - If the owner skips, save what is available with lower confidence.

6. Produce an output and a patch.
   - Operational answer: menu, training, log confirmation, recipe, plan, or review.
   - Patch proposal: records to create/update, confidence, and unresolved gaps.

7. Close the loop.
   - Tell the owner what was saved or proposed.
   - Give same-day next action when relevant.
   - Escalate to Direction OS only for summary, problem, decision, incident, or next CALL.

Safety rule:
- Pain that changes movement, persistent symptoms, concerning cardiovascular symptoms, extreme fatigue, or suspected injury stops load escalation and triggers conservative guidance plus medical/professional escalation language. The system does not diagnose or prescribe.

## 5. Core Loops

### Planning Loop

Trigger:
- owner asks for a weekly plan;
- menu/training request arrives and no current plan exists;
- review says the current plan is unusable.

Inputs:
- profile, preferences, active goals, constraints, current plans, recent summaries.

Behavior:
- detect whether a current food or training plan exists;
- if missing, guide creation of the minimum viable plan;
- ask only the few questions that change the plan;
- write a proposed active plan patch;
- include fallback options for low-time or low-energy days;
- keep plan scope short enough to revise.

Output:
- active weekly food plan and/or training/activity plan;
- missing-data flags;
- patch summary.

### Menu Loop

Trigger:
- owner asks "menu today" or similar.

Inputs:
- active weekly food plan, preferences, recipes, available fallback meals, food-log context if relevant.

Behavior:
- if plan exists, derive today's menu from it;
- if today's menu is missing but weekly plan exists, fill from the plan and mark a patch;
- if no plan exists, explain the missing plan and offer to run the planning loop;
- if owner reports constraints for the day, adapt within the plan;
- avoid full macro/calorie algorithm in v0.

Output:
- today's menu;
- substitutions or fallback;
- any state patch needed.

### Training Loop

Trigger:
- owner asks "training today" or similar.

Inputs:
- active training/activity plan, equipment/location, safety flags, recent summaries.

Behavior:
- if plan exists and safety state is acceptable, output today's training or activity;
- if no plan exists, mark missing plan and offer guided creation or a conservative one-session fallback;
- if pain/fatigue/symptoms are flagged, modify or stop the session and escalate as needed;
- do not create a full long-term progressive program in v0.

Output:
- today's training/activity;
- safety notes;
- state patch or missing-state flag.

### Food-Log Loop

Trigger:
- owner sends text, voice transcript, or photo-style description of food.

Inputs:
- meal description, active plan, preferences, recipes, recent day context if available.

Behavior:
- parse the available description;
- ask limited follow-ups only when they materially change the log or advice;
- allow the owner to skip follow-ups;
- save the available data with confidence and skipped-question markers;
- give same-day advice based on the current plan and confidence.

Output:
- food-log entry patch;
- confidence;
- same-day adjustment advice;
- no raw log copied to Direction OS.

### Recipe Loop

Trigger:
- owner asks for a recipe, saves a recipe, modifies one, or logs a meal that should become repeatable.

Inputs:
- preferences, equipment, active nutrition goals, existing recipe cards, feedback.

Behavior:
- create or update a durable recipe card;
- include portions, ingredients, steps, fit notes, substitutions, and rough nutrition confidence when available;
- mark unresolved nutrition precision instead of pretending exactness;
- remain portable to a future recipe manager.

Output:
- recipe-card patch;
- menu/plan linkage if relevant.

### Review and Incident Loop

Trigger:
- weekly review cadence;
- repeated failure pattern;
- pain/safety signal;
- owner concern;
- system becoming too heavy.

Inputs:
- period summaries, active plans, food logs summaries, training/activity summaries, feedback, incidents.

Behavior:
- compress operational facts into a short review;
- identify what changed, what failed, what is blocked, and what decision is needed;
- propose patches inside Health AI System;
- escalate to Direction OS only if there is a strategic problem, decision, incident, or next CALL.

Output:
- review/incident record;
- Direction OS summary or CALL only when needed.

## 6. Patch and Writer Rule

Health AI chats propose patches. A writer, coding assistant, or future trusted app mechanism applies patches to the Health AI source of truth.

Patch proposal minimum:
- target record or file;
- change;
- reason;
- source chat/session;
- confidence;
- owner approval requirement;
- Direction OS escalation needed: yes/no.

Owner approval is required before patches that materially alter:
- safety constraints;
- active training plan intensity;
- durable preferences that would affect many menus;
- Direction OS state;
- integration choices.

## 7. Non-Goals and Cut List

This slice explicitly cuts:
- dedicated app UI;
- API or database implementation;
- recipe-manager selection;
- Hevy, Strava-like, wearable, VR, or other integration decisions;
- full macro/calorie algorithm;
- full long-term training progression;
- raw logs in Direction OS;
- photo-understanding pipeline;
- automatic cross-tool sync;
- broad health dashboard;
- medical diagnosis or prescriptions;
- polishing or reviving `work/health-starter-kit-v0.md`.

## 8. Dry-Run Scenarios

These scenarios are for `t-3` validation. They use synthetic or minimal seed data and must not store raw daily health data in Direction OS.

### Scenario 1: No Weekly Plan Exists

Seed state:
- profile exists;
- preferences partially exist;
- no active weekly food plan;
- no active training/activity plan.

User asks:
- "What should I eat today?"

Expected behavior:
- chat detects missing weekly food plan;
- chat does not invent a complete plan;
- chat offers a short planning loop;
- chat asks only decision-changing questions;
- chat produces a proposed active plan patch or marks planning blocked by missing owner input.

Validation evidence:
- missing-state behavior is explicit;
- no raw logs are requested;
- Direction OS receives no daily data.

### Scenario 2: Today's Menu from Existing Plan

Seed state:
- active weekly food plan exists;
- preferences and at least one fallback meal exist;
- today's menu is either present or derivable.

User asks:
- "Menu for today?"

Expected behavior:
- chat reads active plan;
- chat outputs today's menu with substitutions or fallback;
- if today's slot is absent, chat fills it from plan rules and proposes a patch;
- chat does not choose a recipe-manager integration.

Validation evidence:
- answer is grounded in state;
- patch proposal is clear if state changes;
- no Direction OS raw data.

### Scenario 3: Food Log with Skipped Follow-Ups

Seed state:
- active food plan exists;
- food-log storage exists;
- owner sends a vague meal description.

User says:
- "I ate chicken with rice and some sauce. I do not want to answer details now."

Expected behavior:
- chat parses available data;
- chat asks no further questions after the owner refuses details;
- chat saves a low-confidence food-log patch with skipped follow-up markers;
- chat gives same-day advice based on uncertainty;
- raw entry stays in Health AI System only.

Validation evidence:
- available data is saved;
- confidence and skipped fields are present;
- same-day advice is produced;
- Direction OS receives nothing unless an incident is found.

### Scenario 4: Today's Training Request

Seed state:
- active training/activity plan exists;
- equipment options exist;
- safety state is either normal or contains a mild caution.

User asks:
- "Training today?"

Expected behavior:
- chat answers from the active plan;
- chat adapts to safety state and available equipment;
- if safety state is concerning, chat reduces or stops load and escalates;
- chat does not create a full long-term progressive program.

Validation evidence:
- training output references current plan/safety state;
- missing or concerning state is handled explicitly;
- no integration decision is made.

### Scenario 5: Review or Incident Escalation

Seed state:
- one week of synthetic summaries exists;
- food adherence is low or training pain is repeated;
- Direction OS has no raw logs.

User asks:
- "Review the week" or reports a repeated problem.

Expected behavior:
- chat compresses operational state into a review/incident record;
- chat proposes Health AI patches;
- chat creates a Direction OS-ready summary only if a strategic decision, problem, or CALL is needed;
- chat excludes raw daily logs.

Validation evidence:
- review is compact;
- escalation boundary is respected;
- Direction OS output is summary/problem/decision/CALL only.

## 9. Done Criteria for This Contract

This contract is usable when:
- the three source-of-truth layers are distinct;
- the minimal state model names all required record families;
- a new chat can operate without relying on hidden memory;
- the six loops have clear triggers, inputs, behavior, and outputs;
- non-goals prevent integration and implementation creep;
- the five dry-runs can be executed from synthetic or minimal state.

END_OF_FILE: work/health-ai-core-contract-v0.md
