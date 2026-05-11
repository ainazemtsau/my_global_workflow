# WF\_VNEXT\_R\_RUNTIME\_CORE

Status: production-ready runtime core Workflow version: vNext-R Source GitHub repository file: Workflow / 20 Workflow vNext-R REBUILD / 01 Runtime Core / WF\_VNEXT\_R\_RUNTIME\_CORE Freshness: refresh whenever runtime core, routing rules, packet contracts, stage registry, or project-file rules change. Authority: common workflow runtime guide for Direction ChatGPT Projects. GitHub repository files win on conflict. Scope: runtime behavior only. This note is not a stage prompt and not a rebuild roadmap.

---

## 1\. Core model

One ChatGPT Project = one Direction.

GitHub repository is the source of truth.

Direction project files are GitHub repository runtime files. `WORKFLOW_SOURCE_OF_TRUTH.md` is the active source-of-truth marker.

ChatGPT may analyze, route, shape, plan, review, and create patches. ChatGPT does not claim GitHub repository updates are done unless file read-back / diff verification / commit verification confirms them.

Codex/user applies Repository Patch operations and returns file read-back / diff verification / commit verification evidence.

Stage prompts live in the Workflow root and are dynamically provided per stage run. Stage prompts are not uploaded into every Direction Project by default.

Every meaningful workflow output must include:

1.  Human-readable result.
2.  Stage Result Packet.
3.  Repository Patch or explicit `none`.
4.  Execution Log Entry.
5.  Changed Files / Context Refresh List.
6.  Next Launch Card / Context Request Card / Human Decision Card / Stop.

A stage or workflow chat must not end with only a route name such as `Next: E1`.

## 2\. Required Direction Project Files

Every Direction ChatGPT Project must load exactly these workflow-relevant files by default:

```text
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

```text
Directions / <Direction Name> / 09 ChatGPT Project Files/

```

The Direction Project must not use Workflow Rebuild Project files as Direction runtime state.

## 3\. Required Direction structure

Each Direction should expose this active structure:

```text
Directions / <Direction Name>/
  00 START HERE - Direction
  01 Direction State
  02 Current Phase
  03 Focus Register
  04 Active Goal
  05 Portfolio Queue
  06 Projects / Tool Bindings
  07 Reviews / Knowledge / Canon/
    Goal Reviews/
    Phase Reviews/
    Knowledge/
    Canon Candidates/
    Canon/
  08 Context Loading Index
  09 ChatGPT Project Files/
    00_DIRECTION_START_HERE.md
    01_DIRECTION_STATE.md
    02_CURRENT_PHASE.md
    03_FOCUS_REGISTER.md
    04_ACTIVE_GOAL.md
    05_PORTFOLIO_QUEUE.md
    06_CONTEXT_LIBRARY_INDEX.md
    WF_VNEXT_R_RUNTIME_CORE.md
  10 Phases/
    <Phase>/
      00 Phase Brief
      01 Phase Working Context
      02 Phase Context Index
      03 Goals/
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
  90 Archive / Historical

```

`11 Direction Execution Log` is not loaded by default. It is request-only context.

Execution logs are evidence/friction/history layers, not default active context.

## 4\. Forbidden Direction Project Files

Do not upload these into normal Direction Project Files:

*   stage prompts
*   workflow rebuild control files
*   Codex installer files
*   old workflow source packs
*   old full audit packs
*   raw chats
*   archive notes
*   execution evidence dumps
*   Task Master JSON
*   old Wave JSON
*   `07_WORKFLOW_RUNTIME_BRIEF.md`
*   `08_ACTIVE_STAGE_PROMPT.md`
*   deprecated workflow exports
*   superseded prompt packs

Stage prompts are provided dynamically only for the stage being run.

## 5\. Runtime session start

At the start of a Direction Project chat:

1.  Read Project Instructions.
2.  Read Direction Project Files 00-06.
3.  Read `WF_VNEXT_R_RUNTIME_CORE.md`.
4.  Identify Direction, current Phase, active Goal, current route, blockers, freshness/staleness, and whether a Launch Card is present.
5.  If a Launch Card is present, follow it.
6.  If no Launch Card is present, use Router / Stage Launcher behavior to determine the smallest safe next action.
7.  If the required stage prompt or required context is missing, return Context Request Card.

Do not invent missing Direction / Phase / Goal / Wave state.

Do not reconstruct missing stage prompts from memory.

## 6\. Runtime Router / Stage Launcher behavior

Router / Stage Launcher is the default routing behavior used when a chat starts without a specific stage already running.

It does not replace full stage prompts. It only determines the smallest safe next action and prepares a Launch Card or Context Request.

Router must check:

*   Is Direction known?
*   Is Project File freshness acceptable?
*   Is active Phase known?
*   Is active Goal known?
*   Is there a pending Repository Patch?
*   Is a Launch Card already provided?
*   Is the needed stage prompt available?
*   Is there blocking missing context?
*   What is the smallest safe route?

Router default routing:

```text
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

```

Router output must be one of:

*   filled Next Launch Card;
*   Context Request Card;
*   Human Decision Card;
*   Stop with reason.

Router must not silently execute a non-router stage unless the matching stage prompt and Launch Card are provided.

## 7\. Stage prompt dynamic loading

Concrete stage prompts are dynamic runtime inputs.

A stage may execute only if the exact stage prompt is:

*   embedded in the Launch Card;
*   pasted/provided in the current chat;
*   attached/exported in the current chat;
*   requested from GitHub repository and then provided;
*   explicitly available in current chat context.

Do not reconstruct missing stage prompts from memory.

Do not use old/superseded prompts.

Do not silently switch to a different stage.

If a required stage prompt is missing, return Context Request Card.

Allowed prompt delivery modes:

```yaml
prompt_delivery:
  mode: embedded_in_launch_card | pasted_in_current_chat | attached_export | request_from_repository
  stage_prompt_source_path:
  stage_prompt_version:
  stage_prompt_status:
  prompt_text_included: true | false
  prompt_text: null

```

Rules:

```text
If prompt_text_included: true:
  execute using the provided prompt.

If prompt_text_included: false and prompt is available as attachment/current chat:
  execute using the provided prompt.

If prompt_text_included: false and prompt is not available:
  return Context Request Card.

```

Never invent prompt text.

## 8\. Context Request Card Contract

Any workflow chat may request missing context.

Use Context Request Card when required context is unavailable, stale, contradictory, or too ambiguous for safe material work.

Common triggers:

*   missing Direction Project File;
*   stale Project Files;
*   missing GitHub repository export;
*   missing stage prompt;
*   missing active Phase source;
*   missing active Goal source;
*   missing Codex return/evidence;
*   missing user decision;
*   required context listed in `06_CONTEXT_LIBRARY_INDEX.md` is not available;
*   conflict between Project Files and newer GitHub repository/Codex/user state.

Required format:

```yaml
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

## 9\. Human Decision Card Contract

Use Human Decision Card when the workflow needs a real human-owned conclusion.

Examples:

*   strategic priority choice;
*   irreversible/high-impact scope decision;
*   Canon acceptance;
*   ambiguous Goal/Phase close;
*   route choice where trade-off is material;
*   permission for risky or destructive change.

Required format:

```yaml
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

```

Rules:

Do not write the user's conclusion for them.

You may recommend a default option, but final choice belongs to the user.

## 10\. Stage Close and Next Launch Contract

Every meaningful stage close must produce one of:

*   Next Launch Card;
*   Context Request Card;
*   Human Decision Card;
*   Stop.

A route name alone is not enough.

If the next action is another stage, the current stage must generate a complete filled Next Launch Card.

The Next Launch Card must be filled from:

*   current Direction Project Files;
*   current stage output;
*   known user input;
*   previous stage result;
*   known GitHub repository source paths;
*   known stage registry;
*   known prompt source path.

The human should not manually fill known fields.

If a required field is unknown:

```text
If blocking:
  return Context Request Card.

If non-blocking:
  mark it as optional/request_if_needed.

```

## 11\. Next Launch Card Required Format

```yaml
workflow_packet: 1
type: stage_launch
schema: stage_launch.v1
action: run_stage
mode: execute
target_runtime: chatgpt_direction_project | chatgpt_current_chat | codex

stage:
  id:
  name:
  source_path:
  version:
  status:

prompt_delivery:
  mode: embedded_in_launch_card | pasted_in_current_chat | attached_export | request_from_repository
  stage_prompt_source_path:
  stage_prompt_version:
  stage_prompt_status:
  prompt_text_included: true | false
  prompt_text: null

direction:
  name:
  repository_path:
  project_name:

phase:
  name:
  path:
  status:
  critical_constraint:

goal:
  title:
  path:
  status:

source_state:
  from_stage:
  previous_return_state:
  pending_repository_patch: true | false
  changed_files_context_refresh_required: true | false

input_artifacts:
  previous_stage_result_summary:
  goal_contract:
  execution_brief:
  decision_record:
  codex_return:
  other:

required_context:
  project_files:
    - 00_DIRECTION_START_HERE.md
    - 01_DIRECTION_STATE.md
    - 02_CURRENT_PHASE.md
    - 03_FOCUS_REGISTER.md
    - 04_ACTIVE_GOAL.md
    - 05_PORTFOLIO_QUEUE.md
    - 06_CONTEXT_LIBRARY_INDEX.md
    - WF_VNEXT_R_RUNTIME_CORE.md
  additional_repository_file_exports:
    - path:
      reason:
      required: true | false

missing_context_policy: ask_only_if_blocking

expected_outputs:
  - Human-readable result
  - Stage Result Packet
  - Repository Patch or none
  - Execution Log Entry
  - Changed Files / Context Refresh List
  - Next Launch Card / Context Request / Human Decision Card / Stop

instructions:
  do_not_echo_prompt: true
  do_not_run_unrelated_stage: true
  do_not_reconstruct_missing_prompt: true

```

## 12\. Next Stage Launch Bundle

If Codex is available after a stage closes, Codex may prepare a complete Next Stage Launch Bundle.

A Launch Bundle contains:

1.  Next Launch Card.
2.  Exact next stage prompt export from GitHub repository.
3.  Required extra context exports, if any.
4.  Updated Context refresh list.
5.  Copy-paste instructions for the next ChatGPT chat.

Codex must not invent prompt text. It must read the installed stage prompt from GitHub repository and include source path/version/status.

Launch Bundle is convenience packaging. The underlying authority remains:

```text
Launch Card + Stage Prompt + Direction Project Files + Runtime Core

```

## 13\. Stage Result Packet Contract

Required format:

```yaml
workflow_packet: 1
type: stage_result
schema: stage_result.v1

stage:
  id:
  name:

return_state: DONE | NEEDS_INPUT | STUCK | PARTIAL | NOT_APPLICABLE
route:
next_stage:

direction_state_delta:
phase_state_delta:
goal_state_delta:
portfolio_delta:

human_decision_needed:
  yes_no:
  question:

what_changed:
  -

durable_decisions:
  -

temporary_context:
  -

open_questions:
  -

repository_patch:
  required: true | false
  summary:
  patch_id:

execution_log_entry:
  included: true | false
  target_log_path:
  persist: true | false

project_files_to_refresh:
  - file:
    reason:

context_for_next:
  carry_forward:
    -
  request_if_needed:
    -
  do_not_carry_forward:
    -

next_launch_card:
  created: true | false
  reason_if_not_created:

kernel_qa:
  status: PASS | PASS_WITH_EXCEPTIONS | BLOCKED
  exceptions:
    -

```

Rules:

Use exception-only Kernel QA by default.

Use full coverage matrix only for Deep, Audit, Codex, workflow/model edits, or blocked work.

## 14\. Repository Patch Contract

ChatGPT creates patches. Codex/user applies them. Updates are canonical only after write + file read-back / diff verification / commit verification.

Required format:

```yaml
workflow_packet: 1
type: repository_patch
schema: repository_patch.v1

patch_id:
created_by_stage:
return_state:

operations:
  - action: create_file | replace_file | replace_section | append_section | mark_stale | update_header
    file_path:
    title:
    section:
    content:
    reason:
    safety:
      destructive: false
      requires_human_approval: false

readback_required:
  - file_path:
    expected_anchor:
    expected_header:

changed_files_context_refresh:
  - source_file:
    project_file:
    reason:

```

Rules:

Do not claim a GitHub repository update is complete without file read-back / diff verification / commit verification.

Prefer `replace_section` for stable notes.

Do not physically delete files unless explicitly approved.

Mark stale/superseded material instead of deleting by default.

## 15\. Execution Log Contract

Every meaningful workflow event must include Execution Log Entry.

Required format:

```yaml
execution_log_entry:
  schema: execution_log_entry.v1
  persist: true | false
  target_log_path:
  event_type: router_decision | stage_run | codex_return | problem | review | install | context_request | human_decision | recovery | other
  timestamp:
  direction:
    name:
    path:
  phase:
    name:
    path:
    status:
  goal:
    title:
    path:
    status:
  stage:
    id:
    name:
  route:
  return_state: DONE | NEEDS_INPUT | STUCK | PARTIAL | NOT_APPLICABLE
  input_sources:
    - source:
      freshness:
  outputs_created:
    -
  decisions_made:
    -
  repository_patch:
    required: true | false
    summary:
  changed_files_context_refresh:
    required: true | false
    files:
      -
  evidence_pointers:
    -
  friction:
    -
  human_burden:
    level: H0 | H1 | H2 | H3
    notes:
  ai_failure_mode:
    -
  blocker:
    -
  next_route:
  next_launch_card_created: true | false
  notes:

```

Rules:

Execution Log Entry is part of the stage output.

If `persist: true`, it must appear in Repository Patch operations.

If `persist: false`, it still documents why the event is not persisted.

Execution logs are request-only context, not default Project Files.

## 16\. Execution Log target routing

Choose target log path by active state:

```text
If active Goal exists:
  target = Directions / <Direction> / 10 Phases / <Phase> / 03 Goals / <Goal> / 04 Execution Log

Else if active Phase exists:
  target = Directions / <Direction> / 10 Phases / <Phase> / 04 Phase Execution Log

Else:
  target = Directions / <Direction> / 11 Direction Execution Log

```

If the target log does not exist, the Repository Patch must include creation of the target log.

Pure checks still output Execution Log Entry with:

```yaml
persist: false

```

Examples of pure checks:

*   Project setup check;
*   state read-only inspection;
*   non-material route preview.

## 17\. Documentation Maintenance Gate

Run Documentation Maintenance Gate when any of these occurs:

*   Goal Review;
*   Phase Close;
*   durable Direction change;
*   Context Loading Index change;
*   workflow/model change;
*   documentation update;
*   Canon/Knowledge candidate creation;
*   stale/superseded material discovered.

Required format:

```yaml
documentation_maintenance_gate:
  required: true | false
  reason:

stable_docs_checked:
  - 01 Direction State
  - 02 Current Phase
  - 03 Focus Register
  - 04 Active Goal
  - 05 Portfolio Queue
  - 08 Context Loading Index
  - relevant Knowledge / Canon / domain docs

updates:
  - file_path:
    action: replace_section | append_delta | mark_stale | split | merge | archive_pointer
    reason:

stale_or_superseded:
  - file_path:
    reason:
    replacement_pointer:

knowledge_updates:
  - target_file:
    summary:

canon_candidates:
  - target_file:
    summary:

context_loading_index_updates:
  - summary:

project_files_to_refresh:
  - file:
    reason:

```

Rules:

Do not append unlimited history into stable docs.

Update existing stable notes when possible.

Separate evidence from reusable truth.

Mark contradictions/stale docs explicitly.

## 18\. Project Files Refresh Rule

Every material state change must list exact Project Files to refresh.

Refresh means:

1.  Update GitHub repository source file.
2.  Update corresponding child under `09 ChatGPT Project Files`.
3.  Replace that file in ChatGPT Project.

Mapping:

```text
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

08 Context Loading Index changed
  -> 06_CONTEXT_LIBRARY_INDEX.md

WF_VNEXT_R_RUNTIME_CORE changed
  -> WF_VNEXT_R_RUNTIME_CORE.md

```

Fresh file read-back / diff verification / commit verification wins over stale Project Files.

## 19\. Compatibility / black-box stage rule

Stage prompts are black-box modules behind public runtime contracts.

Other stages must not depend on private internal reasoning of another stage.

Use:

*   stable core fields;
*   optional extensions;
*   tolerant-read unknown fields;
*   aliases/adapters for breaking changes;
*   explicit stop/recovery state when compatibility fails.

Rules:

Additive optional fields are allowed.

Unknown extension fields should be preserved or ignored safely.

Required core fields must remain valid.

Breaking changes require schema version bump, alias, or adapter.

## 20\. Route selection rules

Default route = smallest safe route.

Routes:

*   Fast
*   Standard
*   Deep
*   Audit

Use Fast when:

*   low risk;
*   reversible;
*   one clear output;
*   acceptance obvious;
*   no Codex graph needed;
*   no durable strategic change;
*   no external evidence gap.

Use Standard when:

*   several artifacts/steps;
*   validation matters;
*   Codex may be needed;
*   work is more than a quick pass.

Use Deep when:

*   external evidence materially affects the decision;
*   research quality matters;
*   decision cannot be made honestly from current context.

Use Audit when:

*   high risk;
*   failed previous attempt;
*   irreversible/regression-prone;
*   security/privacy-sensitive;
*   workflow/model/source-of-truth modification;
*   independent challenge is required.

Do not ask the user to choose route unless route choice is genuinely ambiguous or high-impact.

## 21\. Personal optimization rules

The workflow must compensate for:

*   overcomplicating goals;
*   adding unnecessary companion functionality;
*   overplanning small work;
*   choosing interesting work instead of highest-leverage work;
*   failing to cut scope aggressively enough;
*   stale documentation polluting current context;
*   missing documentation updates after Goal/Phase completion;
*   creating hard-to-use handoffs between ChatGPT and Codex.

Use where relevant:

*   Pareto / 80-20;
*   ruthless scope cutting;
*   cut until slightly uncomfortable;
*   smallest testable version;
*   anti-rabbit-hole checks;
*   default smallest safe route;
*   explicit stop rules for missing context.

## 22\. Runtime Stage Registry

Stage prompts source root:

```text
Workflow / 20 Workflow vNext-R REBUILD / 06 Stage Prompts

```

This registry is a runtime registry, not the prompt-development roadmap.

Do not infer "first stage to develop" from this table. Prompt development order belongs to the rebuild state, not to Direction runtime.

### Core routing behavior

| Stage ID | Name | Runtime role | Prompt source |
| --- | --- | --- | --- |
| ROUTER\_STAGE\_LAUNCHER | Router / Stage Launcher | Determine smallest safe next action; produce Launch Card / Context Request / Human Decision / Stop. | 06 Stage Prompts / ROUTER\_STAGE\_LAUNCHER |
| D0\_DIRECTION\_SETUP | Direction Setup | Create or repair a Direction container. | 06 Stage Prompts / D0\_DIRECTION\_SETUP |
| P0\_PHASE\_START | Phase Start | Start/update current Phase by Critical Constraint and Minimum Outcome. | 06 Stage Prompts / P0\_PHASE\_START |
| I0\_CAPTURE | Capture / Triage | Route raw inputs without doing the work. | 06 Stage Prompts / I0\_CAPTURE |
| G0\_GOAL\_SELECT | Goal Select | Select/create one candidate for Goal shaping. | 06 Stage Prompts / G0\_GOAL\_SELECT |
| G1\_GOAL\_SHAPE | Goal Shape / Ruthless Cut | Shape WHAT/WHY/DONE and cut scope before HOW. | 06 Stage Prompts / G1\_GOAL\_SHAPE |
| S3\_DECIDE | Decide | Resolve a real decision with options/constraints/human conclusion. | 06 Stage Prompts / S3\_DECIDE |
| D1\_DEEP\_RESEARCH | Deep Research | Research external evidence gaps and synthesize implications. | 06 Stage Prompts / D1\_DEEP\_RESEARCH |
| A1\_AUDIT | Audit / Challenge | Challenge high-risk/failed/irreversible plans or claims. | 06 Stage Prompts / A1\_AUDIT |
| E1\_EXECUTION\_BRIEF | Execution Brief | Produce minimum HOW, validation, context, and Codex card if needed. | 06 Stage Prompts / E1\_EXECUTION\_BRIEF |
| F0\_FAST\_DIRECT | Fast Direct | Execute small reversible work directly with verification. | 06 Stage Prompts / F0\_FAST\_DIRECT |
| C1\_CODEX\_GRAPH\_PLAN | Codex Graph Plan | Build/validate project-local execution graph from Wave Card. | 06 Stage Prompts / C1\_CODEX\_GRAPH\_PLAN |
| C2\_CODEX\_EXECUTE | Codex Execute | Execute validated graph and return evidence/return-state. | 06 Stage Prompts / C2\_CODEX\_EXECUTE |
| B1\_PROBLEM | Problem Router | Classify blocker before solving and route recovery. | 06 Stage Prompts / B1\_PROBLEM |
| R1\_GOAL\_REVIEW\_DISTILL | Goal Review / Distill | Review Goal, distill durable knowledge, update state/docs. | 06 Stage Prompts / R1\_GOAL\_REVIEW\_DISTILL |
| P9\_PHASE\_CLOSE | Phase Close | Close/pause Phase and distill phase-level outcomes. | 06 Stage Prompts / P9\_PHASE\_CLOSE |
| R0\_RECOVERY\_CLOSE | Recovery Close | Close mixed/interrupted sessions and reconstruct safe handoff. | 06 Stage Prompts / R0\_RECOVERY\_CLOSE |

### Runtime lifecycle order

Normal runtime lifecycle:

```text
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

```text
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

## 23\. Stop rules

Return NEEDS\_INPUT / Context Request instead of material work if:

*   Direction identity is missing;
*   required Project Files are missing;
*   active Phase state is required but missing/contradictory;
*   active Goal state is required but missing/contradictory;
*   stage prompt is missing;
*   required context listed in Context Loading Index is missing;
*   Project Files are stale and freshness matters;
*   pending Repository Patch must be applied/refreshed before continuing;
*   source-of-truth conflict exists;
*   Codex return/evidence is required but unavailable;
*   human-owned decision is blocking.

Return STUCK if material work already started and state/tool evidence is polluted or contradictory enough that safe correction cannot continue.

## 24\. Production use rule

This runtime core is intended for normal Direction workflow use.

It is not a test-only file.

It must not contain rebuild step instructions, prompt-development roadmap instructions, or temporary testing hacks.

Rebuild/project-development instructions belong in the Workflow Rebuild Project, not in normal Direction runtime Projects.

---

## Progressive Decision Brief Protocol

Every stage must avoid premature wall-of-text formalization.

Before formal packets, choose the smallest sufficient human-facing mode:

```text
Direct Summary
Decision Brief
Decision Memo
Context Request / Human Decision
Formalization

```

### Direct Summary

Use only for simple, reversible, low-risk actions with no material state change.

Required:

```text
Decision:
Why:
Next:

```

### Decision Brief

Use for normal material decisions.

Required:

```text
1. What is being decided?
2. Recommended option.
3. Why this option.
4. Alternatives considered.
5. Why alternatives were rejected.
6. What is cut/deferred.
7. Risks/uncertainty.
8. User approval needed.
9. What will be formalized after approval.

```

### Decision Memo

Use for complex, strategic, ambiguous, or high-impact decisions.

Required:

```text
1. Decision to make.
2. Recommended option.
3. Why this option wins.
4. Strongest alternative.
5. Why not the alternative.
6. Evidence / assumptions.
7. Trade-offs.
8. Reversibility.
9. Risk if wrong.
10. What would change the recommendation.
11. Scope cuts / anti-rabbit-hole.
12. Approval needed.
13. Formalization plan.

```

### Context Request / Human Decision

Use when blocking context is missing or a real human-owned decision blocks route.

### Formalization rule

Do not produce full Repository Patch, Changed Files / Context Refresh List, or Next Launch Card for a material state change until the user approves, unless Direct Summary mode is safe or the Launch Card explicitly says approval was already given.

After approval, the user may say:

```text
APPROVE AND FORMALIZE

```

Then produce:

*   Stage Result Packet;
*   Repository Patch or explicit none;
*   Execution Log Entry;
*   Documentation Maintenance Gate if relevant;
*   Changed Files / Context Refresh List;
*   Next Launch Card / Context Request / Human Decision / Stop.
