# 99_ONE_MESSAGE_PROJECT_FILES_BUNDLE.md

# How to use

Copy everything from `BEGIN CHATGPT PROJECT FILES BUNDLE` through `END CHATGPT PROJECT FILES BUNDLE` into one ChatGPT message.

The bundle is intentionally formatted as separate virtual files. Each source file has:

- `BEGIN FILE`
- file name
- source path
- source note ID
- content
- `END FILE`

# BEGIN CHATGPT PROJECT FILES BUNDLE

## BEGIN FILE 01/08: 00_DIRECTION_START_HERE.md

# 00_DIRECTION_START_HERE.md

## Current pointers

- Current Phase: `vNext One-Goal Smoke Test` -> `directions/solo-max-productive/ phases / vNext One-Goal Smoke Test`
- Active Goal: `none`
- Selected Goal candidate: `Create Lightweight Codex Small-Fix Lane`
- Current focus: shape selected Goal candidate.
- Next route: `G1_GOAL_SHAPE`

## Default Project Files to load

- `00_DIRECTION_START_HERE.md`
- `01_DIRECTION_STATE.md`
- `02_CURRENT_PHASE.md`
- `03_FOCUS_REGISTER.md`
- `04_ACTIVE_GOAL.md`
- `05_PORTFOLIO_QUEUE.md`
- `06_CONTEXT_LIBRARY_INDEX.md`
- `WF_VNEXT_R_RUNTIME_CORE.md`

## END FILE 01/08: 00_DIRECTION_START_HERE.md

## BEGIN FILE 02/08: 01_DIRECTION_STATE.md

# 01_DIRECTION_STATE.md

```
direction:
  name: Solo Max Productive
  id: TokWnxJOqNse
  state: active
  workflow_version: vNext-R
  current_phase_pointer: "directions/solo-max-productive/ phases / vNext One-Goal Smoke Test"
  active_goal_pointer: none
  selected_goal_candidate: "Create Lightweight Codex Small-Fix Lane"
  next_route: G1_GOAL_SHAPE
  last_updated: "2026-05-10"

```

## Project Files export state

- Last refresh: `2026-05-10`
- Required refresh: `none`
- Known stale files: `none known`

## END FILE 02/08: 01_DIRECTION_STATE.md

## BEGIN FILE 03/08: 02_CURRENT_PHASE.md

# 02_CURRENT_PHASE.md

```
current_phase:
  state: active
  phase_name: vNext One-Goal Smoke Test
  phase_path: "directions/solo-max-productive/ phases / vNext One-Goal Smoke Test"
  critical_constraint: "Verify the updated vNext-R lifecycle on one small real Goal."
  minimum_outcome: "Complete Create Lightweight Codex Small-Fix Lane and close/review cleanly."

```

## Guard state

- Active Goal unresolved: `no active Goal exists yet`
- Phase can close now: `no`
- Blocker: `selected Goal candidate must be shaped and completed`

## END FILE 03/08: 02_CURRENT_PHASE.md

## BEGIN FILE 04/08: 03_FOCUS_REGISTER.md

# 03_FOCUS_REGISTER.md

```
focus:
  current_focus: "Shape the selected small-fix lane Goal candidate."
  route_stage: G1_GOAL_SHAPE
  same_chat_allowed: false
  boundary_trigger: new_goal
  pending_state_carried: false
  pending_patch_pointer: none
  last_stage_result_pointer: none

```

## END FILE 04/08: 03_FOCUS_REGISTER.md

## BEGIN FILE 05/08: 04_ACTIVE_GOAL.md

# 04_ACTIVE_GOAL.md

```
active_goal:
  state: none
  goal_name: none
  goal_path: none
  phase_path: "directions/solo-max-productive/ phases / vNext One-Goal Smoke Test"
  current_wave: none

```

## Selected Goal candidate

`Create Lightweight Codex Small-Fix Lane`

Use `G1_GOAL_SHAPE` to create/activate a canonical Goal. Legacy child material under `04 Active Goal` was moved to archive and is not active.

## END FILE 05/08: 04_ACTIVE_GOAL.md

## BEGIN FILE 06/08: 05_PORTFOLIO_QUEUE.md

# 05_PORTFOLIO_QUEUE.md

## Canon rule

This file is a ChatGPT Project File projection. It does not outrank GitHub Direction files.

## Current queue state

Current Phase: `phases / vNext One-Goal Smoke Test`

Active Goal: `none`

Selected candidate: `Create Lightweight Codex Small-Fix Lane`

Next route: `G1_GOAL_SHAPE`

Legacy active-goal material has been moved to historical archive and is not current active Goal state.

## END FILE 06/08: 05_PORTFOLIO_QUEUE.md

## BEGIN FILE 07/08: 06_CONTEXT_LIBRARY_INDEX.md

# 06_CONTEXT_LIBRARY_INDEX.md

## Canon rule

This file is a projection. If it conflicts with GitHub Direction files, GitHub Direction files wins.

## Default context

Load the Direction Project Files default set. Current Phase is `vNext One-Goal Smoke Test`; active Goal is `none`.

## Request-only context

- Current Phase working context and execution log.
- Selected candidate details for `Create Lightweight Codex Small-Fix Lane`.
- Historical legacy active-goal material only when explicitly requested.

## Archive boundary

`archived/historical material` is archive/pointer-only and must not be default-loaded.

## Tool boundary

Concrete smart-workflow setup must be read back before Codex execution. Task Master/Serena/Basic Memory/project validators are support evidence, not DONE authority.

## END FILE 07/08: 06_CONTEXT_LIBRARY_INDEX.md

## BEGIN FILE 08/08: WF_VNEXT_R_RUNTIME_CORE.md

# WF_VNEXT_R_RUNTIME_CORE

Status: production-ready runtime core Workflow version: vNext-R Source GitHub Direction files note: Workflow / 20 Workflow vNext-R REBUILD / 01 Runtime Core / WF_VNEXT_R_RUNTIME_CORE Freshness: refresh whenever runtime core, routing rules, packet contracts, stage registry, or project-file rules change. Authority: common workflow runtime guide for Direction ChatGPT Projects. GitHub Direction files source wins on conflict. Scope: runtime behavior only. This note is not a stage prompt and not a rebuild roadmap.

## 1. Core model

One ChatGPT Project = one Direction.

GitHub Direction files is the source of truth.

Direction Project Files are refreshed exports/projections from GitHub Direction files, not canon.

ChatGPT may analyze, route, shape, plan, review, and create patches. ChatGPT does not claim GitHub Direction files updates are done unless read-back/export refresh confirms them.

Codex/user applies Repository Patch operations and returns read-back evidence.

Stage prompts live in the Workflow root and are dynamically provided per stage run. Stage prompts are not uploaded into every Direction Project by default.

Every meaningful workflow output must include:

- Human-readable result.
- Stage Result Packet.
- Repository Patch or explicit `none`.
- Execution Log Entry.
- Project Files Refresh List.
- Next Launch Card / Context Request Card / Human Decision Card / Stop.

A stage or workflow chat must not end with only a route name such as `Next: E1`.

## 2. Required Direction Project Files

Every Direction ChatGPT Project must load exactly these workflow-relevant files by default:

```
00_DIRECTION_START_HERE.md
01_DIRECTION_STATE.md
02_CURRENT_PHASE.md
03_FOCUS_REGISTER.md
04_ACTIVE_GOAL.md
05_PORTFOLIO_QUEUE.md
06_CONTEXT_LIBRARY_INDEX.md
WF_VNEXT_R_RUNTIME_CORE.md

```

These files are the default active context.

They are exported from:

```
Directions / <Direction Name> / project_files/

```

The Direction Project must not use Workflow Rebuild Project files as Direction runtime state.

## 3. Required Direction structure

Each Direction should expose this active structure:

```
Directions / <Direction Name>/
  00 START HERE - Direction
  01 Direction State
  02 Current Phase
  03 Focus Register
  04 Active Goal
  05 Portfolio Queue
  06 Projects / Tool Bindings
  knowledge/canon/
    Goal Reviews/
    Phase Reviews/
    Knowledge/
    Canon Candidates/
    Canon/
  06_CONTEXT_LIBRARY_INDEX.md
  project_files/
    00_DIRECTION_START_HERE.md
    01_DIRECTION_STATE.md
    02_CURRENT_PHASE.md
    03_FOCUS_REGISTER.md
    04_ACTIVE_GOAL.md
    05_PORTFOLIO_QUEUE.md
    06_CONTEXT_LIBRARY_INDEX.md
    WF_VNEXT_R_RUNTIME_CORE.md
  phases/
    <Phase>/
      00 Phase Brief
      01 Phase Working Context
      02 Phase Context Index
      goals/
        <Goal>/
          00 Goal Contract / Brief
          01 Goal Working Context
          02 Goal Context Index
          03 Waves/
          04 Execution Log
          05 Goal Review
      04 Phase Execution Log
      05 Phase Review
  11 Direction Execution Log
  archived/historical material

If Direction is missing:
  route to D0_DIRECTION_SETUP or Context Request.

If active Phase is missing:
  route to P0_PHASE_START.

If active Phase exists and no active Goal exists:
  route to G0_GOAL_SELECT or G1_GOAL_SHAPE depending on candidate/human seed.

If selected candidate or Goal seed exists but Goal Contract is missing:
  route to G1_GOAL_SHAPE.

If Goal Contract exists and execution basis is missing:
  route to E1_EXECUTION_BRIEF or F0_FAST_DIRECT.

If execution is blocked:
  route to B1_PROBLEM.

If Goal is ready for review:
  route to R1_GOAL_REVIEW_DISTILL.

If Phase is ready to close:
  route to P9_PHASE_CLOSE.

prompt_delivery:
  mode: embedded_in_launch_card | pasted_in_current_chat | attached_export | request_repository_file
  stage_prompt_source_path:
  stage_prompt_version:
  stage_prompt_status:
  prompt_text_included: true | false
  prompt_text: null

```

Rules:

```
If prompt_text_included: true:
  execute using the provided prompt.

If prompt_text_included: false and prompt is available as attachment/current chat:
  execute using the provided prompt.

If prompt_text_included: false and prompt is not available:
  return Context Request Card.

workflow_packet: 1
type: context_request
schema: context_request.v1
reason:
blocking: true | false

requested_context:
  - kind: project_file | repository_file_export | stage_prompt | codex_return | evidence | user_decision | other
    title:
    repository_path:
    file_name_suggested:
    why_needed:
    required: true | false
    freshness_required: fresh | any | latest_available

current_state:
  direction:
  phase:
  goal:
  route_attempted:

after_provided:
  action: continue_current_stage | run_stage | regenerate_launch_card | recheck_state
  stage_id:
  expected_next_output:

instructions_for_user:
  - exact thing to paste/export/upload

```

Rules:

Do not guess missing context.

Do not continue material work if blocking context is missing.

If context is non-blocking, proceed and list it as `request_if_needed`.

## 9. Human Decision Card Contract

Use Human Decision Card when the workflow needs a real human-owned conclusion.

Examples:

- strategic priority choice;
- irreversible/high-impact scope decision;
- Canon acceptance;
- ambiguous Goal/Phase close;
- route choice where trade-off is material;
- permission for risky or destructive change.

Required format:

```
workflow_packet: 1
type: human_decision
schema: human_decision.v1

decision:
  question:
  why_needed:
  blocking: true | false

options:
  - id:
    label:
    tradeoff:
    consequence:

recommendation:
  option_id:
  rationale:
  confidence: low | medium | high

what_changes_based_on_answer:
  - if:
    then:

after_decision:
  action: continue_current_stage | run_stage | regenerate_launch_card | stop
  stage_id:

If blocking:
  return Context Request Card.

If non-blocking:
  mark it as optional/request_if_needed.

```

## 11. Next Launch Card Required Format

## 12. Next Stage Launch Bundle

If Codex is available after a stage closes, Codex may prepare a complete Next Stage Launch Bundle.

A Launch Bundle contains:

- Next Launch Card.
- Exact next stage prompt export from GitHub Direction files.
- Required extra context exports, if any.
- Updated Project Files refresh list.
- Copy-paste instructions for the next ChatGPT chat.

Codex must not invent prompt text. It must read the installed stage prompt from GitHub Direction files and include source path/version/status.

Launch Bundle is convenience packaging. The underlying authority remains:

```
Launch Card + Stage Prompt + Direction Project Files + Runtime Core

```

## 13. Stage Result Packet Contract

Required format:

Rules:

Use exception-only Kernel QA by default.

Use full coverage matrix only for Deep, Audit, Codex, workflow/model edits, or blocked work.

## 14. Repository Patch Contract

ChatGPT creates patches. Codex/user applies them. Updates are canonical only after write + read-back/export refresh.

Required format:

Rules:

Do not claim a GitHub Direction files update is complete without read-back/export refresh.

Prefer `replace_section` for stable notes.

Do not physically delete notes unless explicitly approved.

Mark stale/superseded material instead of deleting by default.

## 15. Execution Log Contract

Every meaningful workflow event must include Execution Log Entry.

Required format:

Rules:

Execution Log Entry is part of the stage output.

If `persist: true`, it must appear in Repository Patch operations.

If `persist: false`, it still documents why the event is not persisted.

Execution logs are request-only context, not default Project Files.

## 16. Execution Log target routing

Choose target log path by active state:

```
If active Goal exists:
  target = Directions / <Direction> / phases / <Phase> / goals / <Goal> / 04 Execution Log

Else if active Phase exists:
  target = Directions / <Direction> / phases / <Phase> / 04 Phase Execution Log

Else:
  target = Directions / <Direction> / 11 Direction Execution Log

persist: false

```

Examples of pure checks:

- Project setup check;
- state read-only inspection;
- non-material route preview.

## 17. Documentation Maintenance Gate

Run Documentation Maintenance Gate when any of these occurs:

- Goal Review;
- Phase Close;
- durable Direction change;
- Context Loading Index change;
- workflow/model change;
- documentation update;
- Canon/Knowledge candidate creation;
- stale/superseded material discovered.

Required format:

```
documentation_maintenance_gate:
  required: true | false
  reason:

stable_docs_checked:
  - 01 Direction State
  - 02 Current Phase
  - 03 Focus Register
  - 04 Active Goal
  - 05 Portfolio Queue
  - 06_CONTEXT_LIBRARY_INDEX.md
  - relevant Knowledge / Canon / domain docs

updates:
  - note_path:
    action: replace_section | append_delta | mark_stale | split | merge | archive_pointer
    reason:

stale_or_superseded:
  - note_path:
    reason:
    replacement_pointer:

knowledge_updates:
  - target_note:
    summary:

canon_candidates:
  - target_note:
    summary:

context_loading_index_updates:
  - summary:

project_files_to_refresh:
  - file:
    reason:

00 START HERE - Direction changed
  -> 00_DIRECTION_START_HERE.md

01 Direction State changed
  -> 01_DIRECTION_STATE.md

02 Current Phase changed
  -> 02_CURRENT_PHASE.md

03 Focus Register changed
  -> 03_FOCUS_REGISTER.md

04 Active Goal changed
  -> 04_ACTIVE_GOAL.md

05 Portfolio Queue changed
  -> 05_PORTFOLIO_QUEUE.md

06_CONTEXT_LIBRARY_INDEX.md changed
  -> 06_CONTEXT_LIBRARY_INDEX.md

WF_VNEXT_R_RUNTIME_CORE changed
  -> WF_VNEXT_R_RUNTIME_CORE.md

Workflow / 20 Workflow vNext-R REBUILD / 06 Stage Prompts

```

This registry is a runtime registry, not the prompt-development roadmap.

Do not infer "first stage to develop" from this table. Prompt development order belongs to the rebuild state, not to Direction runtime.

### Core routing behavior

Stage ID

Name

Runtime role

Prompt source

ROUTER_STAGE_LAUNCHER

Router / Stage Launcher

Determine smallest safe next action; produce Launch Card / Context Request / Human Decision / Stop.

06 Stage Prompts / ROUTER_STAGE_LAUNCHER

D0_DIRECTION_SETUP

Direction Setup

Create or repair a Direction container.

06 Stage Prompts / D0_DIRECTION_SETUP

P0_PHASE_START

Phase Start

Start/update current Phase by Critical Constraint and Minimum Outcome.

06 Stage Prompts / P0_PHASE_START

I0_CAPTURE

Capture / Triage

Route raw inputs without doing the work.

06 Stage Prompts / I0_CAPTURE

G0_GOAL_SELECT

Goal Select

Select/create one candidate for Goal shaping.

06 Stage Prompts / G0_GOAL_SELECT

G1_GOAL_SHAPE

Goal Shape / Ruthless Cut

Shape WHAT/WHY/DONE and cut scope before HOW.

06 Stage Prompts / G1_GOAL_SHAPE

S3_DECIDE

Decide

Resolve a real decision with options/constraints/human conclusion.

06 Stage Prompts / S3_DECIDE

D1_DEEP_RESEARCH

Deep Research

Research external evidence gaps and synthesize implications.

06 Stage Prompts / D1_DEEP_RESEARCH

A1_AUDIT

Audit / Challenge

Challenge high-risk/failed/irreversible plans or claims.

06 Stage Prompts / A1_AUDIT

E1_EXECUTION_BRIEF

Execution Brief

Produce minimum HOW, validation, context, and Codex card if needed.

06 Stage Prompts / E1_EXECUTION_BRIEF

F0_FAST_DIRECT

Fast Direct

Execute small reversible work directly with verification.

06 Stage Prompts / F0_FAST_DIRECT

C1_CODEX_GRAPH_PLAN

Codex Graph Plan

Build/validate project-local execution graph from Wave Card.

06 Stage Prompts / C1_CODEX_GRAPH_PLAN

C2_CODEX_EXECUTE

Codex Execute

Execute validated graph and return evidence/return-state.

06 Stage Prompts / C2_CODEX_EXECUTE

B1_PROBLEM

Problem Router

Classify blocker before solving and route recovery.

06 Stage Prompts / B1_PROBLEM

R1_GOAL_REVIEW_DISTILL

Goal Review / Distill

Review Goal, distill durable knowledge, update state/docs.

06 Stage Prompts / R1_GOAL_REVIEW_DISTILL

P9_PHASE_CLOSE

Phase Close

Close/pause Phase and distill phase-level outcomes.

06 Stage Prompts / P9_PHASE_CLOSE

R0_RECOVERY_CLOSE

Recovery Close

Close mixed/interrupted sessions and reconstruct safe handoff.

06 Stage Prompts / R0_RECOVERY_CLOSE

### Runtime lifecycle order

Normal runtime lifecycle:

```
D0_DIRECTION_SETUP
  -> P0_PHASE_START
  -> I0_CAPTURE / G0_GOAL_SELECT / G1_GOAL_SHAPE
  -> S3_DECIDE / D1_DEEP_RESEARCH / A1_AUDIT if needed
  -> E1_EXECUTION_BRIEF
  -> F0_FAST_DIRECT or C1_CODEX_GRAPH_PLAN -> C2_CODEX_EXECUTE
  -> B1_PROBLEM if blocked
  -> R1_GOAL_REVIEW_DISTILL
  -> P9_PHASE_CLOSE when Phase outcome is reached
  -> next P0_PHASE_START or Direction pause/archive

```

Router may enter any appropriate point based on current Direction state.

### Allowed high-level transitions

```
ROUTER_STAGE_LAUNCHER -> any stage or Context Request / Human Decision / Stop

D0_DIRECTION_SETUP -> P0_PHASE_START

P0_PHASE_START -> I0_CAPTURE | G0_GOAL_SELECT | G1_GOAL_SHAPE

I0_CAPTURE -> G0_GOAL_SELECT | G1_GOAL_SHAPE | S3_DECIDE | B1_PROBLEM | Stop

G0_GOAL_SELECT -> G1_GOAL_SHAPE

G1_GOAL_SHAPE -> F0_FAST_DIRECT | E1_EXECUTION_BRIEF | S3_DECIDE | D1_DEEP_RESEARCH | A1_AUDIT | B1_PROBLEM | Stop

S3_DECIDE -> G1_GOAL_SHAPE | E1_EXECUTION_BRIEF | R1_GOAL_REVIEW_DISTILL | Stop

D1_DEEP_RESEARCH -> S3_DECIDE | G1_GOAL_SHAPE | E1_EXECUTION_BRIEF | Stop

A1_AUDIT -> S3_DECIDE | G1_GOAL_SHAPE | E1_EXECUTION_BRIEF | R1_GOAL_REVIEW_DISTILL | Stop

E1_EXECUTION_BRIEF -> F0_FAST_DIRECT | C1_CODEX_GRAPH_PLAN | B1_PROBLEM | Stop

F0_FAST_DIRECT -> R1_GOAL_REVIEW_DISTILL | E1_EXECUTION_BRIEF | B1_PROBLEM | Stop

C1_CODEX_GRAPH_PLAN -> C2_CODEX_EXECUTE | B1_PROBLEM | Context Request | Stop

C2_CODEX_EXECUTE -> R1_GOAL_REVIEW_DISTILL | E1_EXECUTION_BRIEF | B1_PROBLEM | Stop

B1_PROBLEM -> continue_current_stage | E1_EXECUTION_BRIEF | G1_GOAL_SHAPE | S3_DECIDE | R1_GOAL_REVIEW_DISTILL | Stop

R1_GOAL_REVIEW_DISTILL -> G0_GOAL_SELECT | G1_GOAL_SHAPE | P9_PHASE_CLOSE | P0_PHASE_START | Stop

P9_PHASE_CLOSE -> P0_PHASE_START | G0_GOAL_SELECT | Direction pause/archive | Stop

R0_RECOVERY_CLOSE -> ROUTER_STAGE_LAUNCHER | Context Request | Stop

```

Unknown stage IDs must produce Context Request Card or Proposed Registry Amendment. Do not guess.

## 23. Stop rules

Return NEEDS_INPUT / Context Request instead of material work if:

- Direction identity is missing;
- required Project Files are missing;
- active Phase state is required but missing/contradictory;
- active Goal state is required but missing/contradictory;
- stage prompt is missing;
- required context listed in Context Loading Index is missing;
- Project Files are stale and freshness matters;
- pending Repository Patch must be applied/refreshed before continuing;
- source-of-truth conflict exists;
- Codex return/evidence is required but unavailable;
- human-owned decision is blocking.

Return STUCK if material work already started and state/tool evidence is polluted or contradictory enough that safe correction cannot continue.

## 24. Production use rule

This runtime core is intended for normal Direction workflow use.

It is not a test-only file.

It must not contain rebuild step instructions, prompt-development roadmap instructions, or temporary testing hacks.

Rebuild/project-development instructions belong in the Workflow Rebuild Project, not in normal Direction runtime Projects.

## END FILE 08/08: WF_VNEXT_R_RUNTIME_CORE.md

# END CHATGPT PROJECT FILES BUNDLE
