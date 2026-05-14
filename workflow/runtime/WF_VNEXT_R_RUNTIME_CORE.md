# WF\_VNEXT\_R\_RUNTIME\_CORE

Status: production-ready runtime core
Workflow version: vNext-R
Source GitHub repository file: `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
Freshness: refresh whenever runtime core, routing rules, packet contracts, stage registry, or project-file rules change.
Authority: common workflow runtime guide for Direction ChatGPT Projects. GitHub repository files win on conflict.
Scope: runtime behavior only. This file is not a stage prompt and not a rebuild roadmap.

---

## 1\. Core model

One ChatGPT Project = one Direction.

GitHub repository is the source of truth.

Direction project files are GitHub repository runtime files. `WORKFLOW_SOURCE_OF_TRUTH.md` is the active source-of-truth marker.

ChatGPT may analyze, route, shape, plan, review, and create patches. ChatGPT does not claim GitHub repository updates are done unless file read-back / diff verification / commit verification confirms them.

Codex/user applies Repository Patch operations and returns file read-back / diff verification / commit verification evidence.

Stage prompts live in the Workflow root and are dynamically provided per stage run. Stage prompts are not uploaded into every Direction Project by default.

Every formalized workflow output must include:

1.  Human-readable result.
2.  Stage Result Packet.
3.  Repository Patch or explicit `none`.
4.  Execution Log Entry.
5.  Changed Files / Context Refresh List.
6.  Next Launch Card / Context Request Card / Human Decision Card / Stop.

A stage or workflow chat must not end with only a route name such as `Next: E1`.

FIRST RESPONSE IS NOT FORMAL CLOSE. For material work, the first response is a reviewable work product unless formalization is already approved.

### 1.1 Human-facing presentation rule

Technical workflow packets are transport, not the primary user interface.

The first visible layer of a workflow response must be readable without inspecting YAML. Put the highest-value information first:

1. what is happening;
2. what will be done next;
3. why this is the right next move;
4. what is in scope and out of scope;
5. what the user must approve, provide, copy, or run.

Machine-readable packets such as `stage_launch.v1`, `stage_result.v1`, `repository_patch.v1`, `execution_log_entry.v1`, `context_request.v1`, and `human_decision.v1` remain mandatory when formalization, launch, apply, validation, or copy-paste transport is required. They must appear after the human-readable result under:

```text
Technical appendix — copy only if launching/applying/validating
```

Do not put raw YAML, launch cards, repository patch packets, or workflow-management metadata above the human-readable result unless the user explicitly asks for packet-only output.

Stage-specific output shapes are content requirements, not mandatory headings for every case. Use adaptive headings and formatting that fit the situation. Include only management-of-workflow details that affect the user's immediate decision, approval, copy/paste action, context refresh, repository maintenance, execution readiness, or next action.

For normal runtime outputs, prefer this visible order:

1. Result / recommendation / next action.
2. Why this.
3. What will be done and what is cut.
4. Risks, assumptions, or required approval.
5. Technical appendix with copyable packets, only when needed.

If a launch card is being prepared for the next chat, summarize it first in plain text. The full `stage_launch.v1` packet goes in the technical appendix.

Human-facing prose should answer in the user's language when the user's language is clear. Packet field names, schema keys, stage IDs, repository paths, file names, and exact command/card tokens remain canonical English.

### 1.2 Packet template authority boundary

Canonical packet templates live in:

```text
workflow/transport/*.md
```

Runtime core remains authority for runtime behavior, precedence, approval/formalization rules, repository maintenance rules, route process, Codex role separation, and Project Files refresh/reporting rules.

Until the later runtime-core packet-schema reference cleanup is applied, this file may still contain embedded packet examples or compatibility blocks. Those examples must be treated as reference/fallback text, not as packet-template authority.

If a runtime-core packet example conflicts with the matching transport template, use the canonical transport template for packet shape and this runtime core for behavior.

## 2. Required Direction Project Files

Every Direction ChatGPT Project must load the Direction Project Files 00-07 by default from:

```text
directions/<direction-id>/project_files/

```

Required Direction Project Files:

```text
00_DIRECTION_START_HERE.md
01_DIRECTION_STATE.md
02_CURRENT_PHASE.md
03_FOCUS_REGISTER.md
04_ACTIVE_GOAL.md
05_PORTFOLIO_QUEUE.md
06_CONTEXT_LIBRARY_INDEX.md
07_PHASE_MEMORY_INDEX.md

```

Every Direction ChatGPT Project must also load the shared runtime core:

```text
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md

```

Do not create or require local copies at `directions/<direction-id>/project_files/WF_VNEXT_R_RUNTIME_CORE.md`.

These files are the default active context.

The Direction Project must not use Workflow Rebuild Project files as Direction runtime state.

If `07_PHASE_MEMORY_INDEX.md` is missing for an existing Direction, treat the Direction as needing a Phase Memory backfill or Context Request before creating a materially new Phase after a previous Phase close.

## 3. Required Direction structure

Each Direction should expose this active GitHub structure:

```text
directions/<direction-id>/
  AGENTS.md
  README.md
  direction.meta.yml
  project_files/
    00_DIRECTION_START_HERE.md
    01_DIRECTION_STATE.md
    02_CURRENT_PHASE.md
    03_FOCUS_REGISTER.md
    04_ACTIVE_GOAL.md
    05_PORTFOLIO_QUEUE.md
    06_CONTEXT_LIBRARY_INDEX.md
    07_PHASE_MEMORY_INDEX.md
  knowledge/
    canon/
    decisions/
    patterns/
    reviews/
  domain_docs/
  phases/
    <phase-id>/
      phase_close_summary.md
  execution_logs/
    11_DIRECTION_EXECUTION_LOG.md
  projects/

```

`11 Direction Execution Log` is not loaded by default. It is request-only context.

Execution logs are evidence/friction/history layers, not default active context.

`07_PHASE_MEMORY_INDEX.md` is the compact default-loaded Phase Memory Bridge. It is not an execution log and must not become a full retrospective. Detailed closed-Phase information lives in `directions/<direction-id>/phases/<phase-id>/phase_close_summary.md`.

## 3.1 Phase Memory Bridge

The Phase Memory Bridge is the required durable runtime link between a closed Phase and the next Phase start.

Required files:

```text
directions/<direction-id>/project_files/07_PHASE_MEMORY_INDEX.md
directions/<direction-id>/phases/<phase-id>/phase_close_summary.md
```

`07_PHASE_MEMORY_INDEX.md` is default-loaded Project File context. It must stay compact and must include:

- latest closed Phase pointer;
- closed Phase ledger entries;
- carryovers;
- do-not-repeat items;
- duplicate Phase patterns to avoid;
- recommended next Phase candidates;
- recommended next Phase exclusions;
- pointers to detailed close summaries and evidence.

`phase_close_summary.md` is request-only detailed Phase memory. It must include:

- Phase objective and closure verdict;
- delivered outcomes;
- Goals completed, excluded, or left open;
- files/docs/artifacts created;
- durable decisions;
- lessons learned;
- constraints discovered;
- carryovers;
- do-not-repeat items;
- duplicate patterns to avoid;
- recommended next Phase candidates;
- recommended next Phase exclusions;
- source/evidence pointers.

P9_PHASE_CLOSE must update both files when formally closing a Phase. Phase closure is incomplete if the Phase status changes but the Phase Memory Bridge is not updated in the same approved repository patch.

P0_PHASE_START must read `07_PHASE_MEMORY_INDEX.md` before proposing a materially new Phase when the trigger is previous Phase completed, no active Phase, restart after closure, or user asks for next Phase. If the compact index is missing, stale, contradictory, or insufficient, P0 must return a Context Request naming the exact missing repository path. If the compact index points to a latest close summary and P0 needs detail to avoid repetition, P0 must request/load that exact `phase_close_summary.md`.

P0 must show a visible anti-duplicate line before approval:

```text
Почему это не повтор прошлой фазы:
<concrete delta>
```

If no concrete delta exists, P0 must not create a new Phase. It must choose continue/repair/carryover/context-request/human-decision/stop instead.

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
2.  Read Direction Project Files 00-07.
3.  Read shared runtime core at `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.
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

## Research and Fast Direct Routing Boundary

Research-needed work must not be performed inside a non-research stage.

If Router, E1_EXECUTION_BRIEF, F0_FAST_DIRECT, or any other stage detects that the next safe action depends on current external facts, source-backed synthesis, current tool/platform behavior, material research, or unresolved architecture/tooling assumptions, the stage must route to `D1_DEEP_RESEARCH`, return Context Request, or return B1_PROBLEM according to `workflow/stage_registry/STAGE_REGISTRY.md` and the runtime prompt contract.

F0_FAST_DIRECT is allowed only when all of these are true:

- the work is one active Goal and one bounded execution slice;
- acceptance is concrete and checkable;
- artifact(s), target path(s), allowed changes, forbidden changes, and validation anchors are explicit;
- no external/current research is required;
- no architecture/tooling/storage/source-of-truth decision is unresolved;
- no graph/wave planning is required;
- no multi-file/multi-tool coordination is required beyond a direct repository patch;
- no Codex product/project execution is required;
- no security/privacy/permission/secret/tool-binding risk exists;
- no stale or contradictory context blocks safe execution.

If any item is false or unknown, do not route to F0. Route to the smallest safer stage allowed by `STAGE_REGISTRY.md`:

- `D1_DEEP_RESEARCH` for external/current evidence gaps;
- `E1_EXECUTION_BRIEF` for missing execution brief;
- `C1_CODEX_GRAPH_PLAN` for decomposition, graph/wave, or multi-file/multi-tool planning;
- `S3_DECIDE` or Human Decision for material tradeoffs;
- `B1_PROBLEM` for unclear problem/frame;
- Context Request for missing blocking context;
- Stop for unsafe or contradictory launches.

A stage must not route to F0 merely because the requested output seems short. F0 requires explicit readiness, not apparent size.

Route conflict rule: route conflict is selected-route-vs-registry. If the selected next stage is not allowed by `STAGE_REGISTRY.md`, return a route-conflict Context Request or B1_PROBLEM. Do not improvise and do not execute another stage's work inside the current stage.

Stage prompt route lists are not independent authority. If a prompt-maintained route list conflicts with `STAGE_REGISTRY.md`, the registry wins.

## 7\. Stage prompt dynamic loading

Concrete stage prompts are dynamic runtime inputs.

A stage may execute only if the exact stage prompt is available in the current run through one of these delivery modes:

- `prompt_text_embedded`: exact prompt text is embedded in the Launch Card.
- `prompt_attachment_provided`: exact prompt text is attached/exported in the current chat.
- `manual_prompt_required`: prompt text is not available; the chat must request the exact prompt from the user/Codex and must not execute the stage yet.
- `codex_verified_local_bundle`: Codex read the exact prompt from a local checkout, verified completeness, and supplied the prompt or a verified launch bundle.

Do not reconstruct missing stage prompts from memory.

Do not use old/superseded prompts.

Do not silently switch to a different stage.

If a required stage prompt is missing, truncated, omitted, lacks tail verification when tail verification is required, or is not available in current chat context, return Context Request Card.

Allowed prompt delivery modes:

```yaml
prompt_delivery:
  mode: prompt_text_embedded | prompt_attachment_provided | manual_prompt_required | codex_verified_local_bundle
  stage_prompt_source_path:
  stage_prompt_version:
  stage_prompt_status:
  prompt_text_included: true | false
  prompt_text: null
  source_commit:
  line_count:
  byte_count:
  tail_anchor_or_eof_verified: true | false
  execute_allowed: true | false
```

Rules:

```text
If prompt_text_included: true and the prompt is complete:
  execute using the provided prompt.

If mode: prompt_attachment_provided and the attached/exported prompt is complete:
  execute using the provided prompt.

If mode: codex_verified_local_bundle and Codex verifies completeness:
  execute using the supplied verified prompt or launch bundle.

If mode: manual_prompt_required:
  return Context Request for the exact stage prompt path.

If prompt_text_included: false and the prompt is not otherwise available:
  return Context Request Card.

If a GitHub read of the exact prompt is truncated, omitted, or lacks required tail verification:
  treat the prompt as unavailable for that run.
```

Never invent prompt text.

`request_from_repository` is deprecated and must not be used for new launch cards. Use `manual_prompt_required` or `codex_verified_local_bundle`.

## 8\. Context Request Card Contract

Use Context Request Card when required context is unavailable, stale, contradictory, or too ambiguous for safe material work.

Canonical packet template:

```text
workflow/transport/CONTEXT_REQUEST_CARD.md
```

Runtime behavior rules:

- do not guess missing context;
- do not continue material work if blocking context is missing;
- request only the smallest exact blocking context set;
- if context is non-blocking, proceed and list it as `request_if_needed`;
- name exact repository paths when repository context is required;
- do not infer unseen content from memory, search snippets, compact results, earlier chats, or partial GitHub output.

Common triggers:

- missing Direction Project File;
- stale Project Files;
- missing GitHub repository export;
- missing stage prompt;
- missing active Phase source;
- missing active Goal source;
- missing Codex return/evidence;
- missing user decision;
- required context listed in `06_CONTEXT_LIBRARY_INDEX.md` is not available;
- conflict between Project Files and newer GitHub repository/Codex/user state.

Use the canonical transport template for packet shape. Runtime core owns the behavior above.

## 8.5 GitHub Long File Read Guard

A GitHub repository file read is not full-file authority when the response is truncated, omitted due to tool response token budget, lacks an expected tail anchor, or cannot verify that the chat saw the end of the file.

When material work depends on such a file, the workflow must stop and return a Context Request naming the exact repository path. The chat must not infer unseen content from memory, search snippets, compact results, earlier chats, or partial GitHub output.

Stage prompt special rule: if an exact stage prompt file is truncated or lacks tail verification, the prompt is considered unavailable for that run. The stage must not execute until the prompt is supplied manually, split into smaller files, chunk-exported with tail verification, or verified by Codex read-only local checkout.

Detailed guard rules live in:

```text
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
```

Core workflow files required in every Direction Project chat should be manually loaded as ChatGPT Project Files runtime cache according to `WORKFLOW_RUNTIME_CACHE_MANIFEST.md`.

## 9\. Human Decision Card Contract

Use Human Decision Card when the workflow needs a real human-owned conclusion.

Canonical packet template:

```text
workflow/transport/HUMAN_DECISION_CARD.md
```

Runtime behavior rules:

- do not write the user's conclusion for them;
- present concrete options and consequences;
- recommend a default only when justified;
- final choice belongs to the user;
- after the decision, route according to the registry and runtime state;
- do not use Human Decision as a substitute for missing context.

Examples:

- strategic priority choice;
- irreversible/high-impact scope decision;
- Canon acceptance;
- ambiguous Goal/Phase close;
- route choice where trade-off is material;
- permission for risky or destructive change.

Use the canonical transport template for packet shape. Runtime core owns the behavior above.

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

If the next action is another stage, the current stage must generate a complete filled Next Launch Card.

Canonical packet template:

```text
workflow/transport/STAGE_LAUNCH_CARD.md
```

Runtime behavior rules:

- a route name alone is not enough;
- the human should not manually fill known fields;
- the launch must be filled from current Direction Project Files, current stage output, known user input, previous stage result, known GitHub repository source paths, known stage registry, and known prompt source path;
- if a required field is unknown and blocking, return Context Request;
- if a field is optional/non-blocking, mark it as optional or `request_if_needed`;
- use `workflow/stage_registry/STAGE_REGISTRY.md` for route authority;
- stage prompt availability must use approved prompt delivery modes only;
- do not reconstruct missing prompt text;
- do not execute downstream stage work inside the current stage.

Prompt delivery modes allowed for new launches:

```text
prompt_text_embedded
prompt_attachment_provided
manual_prompt_required
codex_verified_local_bundle
```

Deprecated repository-request prompt delivery must not be used.

Use the canonical transport template for packet shape. Runtime core owns the behavior above.

## 11.5 Codex Role Separation Contract

Codex has separate runtime roles. Do not collapse them into a generic allowed/forbidden state.

Codex product/project execution means implementation against a concrete product/project workspace, product repository, game proof, application code, Task Master execution graph, external tool binding, validation command run, or project file mutation that changes the product/project itself. Codex product/project execution is allowed only through the correct execution route after E1/C1/C2 readiness, verified project/tool bindings, scope, validation, permissions, and explicit route.

Codex repository maintenance means applying an approved repository_patch.v1 to workflow or Direction GitHub files, appending execution logs, updating runtime markdown, and returning file read-back / diff verification / commit verification evidence. Codex repository maintenance is allowed after the patch is approved and must stay inside the approved repository paths.

Codex read-only audit/validation means reading repository files, checking packet/schema consistency, verifying diffs, validating anchors, or reporting issues without writing. Codex read-only audit/validation is allowed when requested and does not count as product/project execution.

Codex launch bundle preparation means packaging a Next Launch Card, exact stage prompt source path/version/status, required context exports, and copy-paste instructions for the next ChatGPT run. Codex launch bundle preparation is allowed when needed and must not invent prompt text or bypass stage routing.

When a stage says Codex product/project execution is blocked, that restriction does not block approved repository maintenance, read-only audit/validation, or launch bundle preparation unless the stage explicitly says all Codex roles are blocked.

## 11.6 Hard First Response and Adaptive Reviewable Work Product Gate

Rule precedence:

1. Safety / Context Request / Human Decision / Stop
2. Hard First Response / Formalization Gate
3. Stage-specific Reviewable Work Product Quality Standard
4. Mandatory Close Compiler
5. Packet schemas

FIRST RESPONSE IS NOT FORMAL CLOSE.

`mode: execute` means run stage reasoning; mode: execute does not authorize formalization.

Mandatory Close Compiler applies only in Formalization Mode.

Response-depth model:

- R0 Direct Result
- R1 Reviewable Brief
- R2 Decision Memo
- R3 Work Product Preview
- R4 Context Request / Human Decision
- R5 Formalization

Launch/output schema split:

```yaml
expected_first_response_outputs:
  - Direct Result / Reviewable Brief / Decision Memo / Work Product Preview
  - planned_patch_summary
  - planned_formalization_summary
  - approval request
  - Context Request / Human Decision / Stop when needed

expected_after_approval_outputs:
  - stage_result.v1
  - repository_patch.v1
  - execution_log_entry.v1
  - changed_files_context_refresh
  - stage_launch.v1 / context_request.v1 / human_decision.v1 / stop.v1
  - codex_repository_maintenance_apply.v1 when repository_patch.required = true or operations are non-empty

expected_outputs:
  compatibility: fallback_only_do_not_override_formalization_control
```

Generic `expected_outputs` is compatibility fallback only. It must not override `formalization_control`, first-response rules, approval state, or the hard gate.

forbidden-before-approval list:

Before approval, material stages must not output:

- `stage_result.v1`
- `repository_patch.v1` with non-empty operations
- `execution_log_entry.v1` as final formal packet
- `changed_files_context_refresh.required = true`
- executable `stage_launch.v1`
- `codex_repository_maintenance_apply.v1`

allowed-before-approval list:

- Direct Result
- Reviewable Brief
- Decision Memo
- Work Product Preview
- planned_patch_summary
- planned_formalization_summary
- approval request
- Context Request
- Human Decision
- Stop

Reviewable Work Product Quality Standard:

A reviewable first response must be substantive enough for the user to judge the recommendation. It must include:

- what is being decided / produced
- recommendation or proposed artifact
- why this
- alternatives considered
- why not alternatives
- scope cuts / deferred items
- risks / assumptions
- what would change the recommendation
- what needs approval
- what will be formalized after approval

Formal packets are allowed only after:

- user says `APPROVE AND FORMALIZE`;
- or `direct_formalization_allowed = true` with explicit approval_state;
- or Direct Result mode is safe for non-material low-risk work.

## 11.6.1 Reviewable Work Product and Formalization Control

Every stage must produce a reviewable work product or decision layer before formal packets, non-empty repository_patch.v1 operations, or executable next-stage launch when material work is being proposed.

Required first-response modes:

- Compact Direct Result
- Reviewable Brief
- Decision Memo / Work Product Preview
- Context Request / Human Decision
- Formalization

Core rule: `mode: execute` runs stage reasoning only. It does not authorize full formal packets, non-empty repository_patch.v1.operations, executable next-stage launch, or changed_files_context_refresh.required = true unless formalization is approved.

Default behavior when `formalization_control` is absent:

```yaml
formalization_control:
  first_response_mode: reviewable_brief
  formalization_policy: proposal_first
  approval_state:
    material_change_approved: false
    repository_patch_approved: false
    approval_source: none
  formalization_trigger: APPROVE AND FORMALIZE
```

Reviewable Brief required fields:

1. What I’m proposing
2. Proposed substance
3. Why this shape
4. Alternatives considered
5. Why not alternatives
6. Scope cuts
7. Risks / assumptions
8. What I need from you
9. If approved, I will formalize

Decision Memo / Work Product Preview required fields:

1. Decision / work product being reviewed
2. Recommended content
3. Full proposed structure
4. Key claims / principles
5. Alternatives considered
6. Why not alternatives
7. What would change the recommendation
8. Scope cuts / deferred items
9. Risks / assumptions / confidence
10. Approval options
11. Formalization plan
12. What will NOT happen until approval

Proposed substance is mandatory for artifact-producing, phase-changing, goal-shaping, planning, review, and decision stages. It must summarize the actual contents of the artifact, Goal Contract, Phase, plan, review, decision, or patch being proposed.

Before approval:

- use planned_patch_summary instead of non-empty repository_patch.v1 operations;
- use planned_changed_files_context_refresh instead of changed_files_context_refresh.required = true;
- use prepared_but_not_executable_next_launch instead of executable stage_launch.v1 when the launch depends on unapproved writes;
- do not emit formal packets as the final state for a material change.

Non-empty repository_patch.v1 operations may be produced only if formalization_policy = direct_formalization_allowed and repository_patch_approved = true, or the user explicitly says APPROVE AND FORMALIZE in this stage chat. Direct formalization also requires material_change_approved = true, an explicit approval_source, and no remaining material ambiguity.

Any stage-prompt instruction that says to always include formal packets, produce repository_patch, set changed_files_context_refresh.required = true, or emit an executable next launch is a formalization-phase instruction unless the stage is in a safe Compact Direct Result case or direct formalization is explicitly approved.

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

Every meaningful stage close must produce a Stage Result Packet unless the run stops before a formal close and returns Context Request, Human Decision, or Stop.

Canonical packet template:

```text
workflow/transport/STAGE_RESULT_PACKET.md
```

Runtime behavior rules:

- include the stage identity and return state;
- include route / next-stage information when applicable;
- include durable decisions and what changed;
- include repository patch status or explicit none;
- include execution log status;
- include Project Files refresh impact;
- include context for next stage;
- include next launch status or reason not created;
- use exception-only Kernel QA by default;
- use full coverage matrix only for Deep, Audit, Codex, workflow/model edits, or blocked work.

Use the canonical transport template for packet shape. Runtime core owns the behavior above.

## 14\. Repository Patch Contract

ChatGPT creates Repository Patch packets. Codex or the user applies them. Repository updates are canonical only after write plus file read-back / diff verification / commit verification.

Canonical Repository Patch template:

```text
workflow/transport/REPOSITORY_PATCH.md
```

### 14.1 Repository Patch behavior

Runtime behavior rules:

- do not physically delete files unless explicitly approved;
- prefer scoped operations over vague append behavior;
- every patch must name exact paths;
- all content-bearing writes must include validation/read-back anchors;
- no writes outside named approved paths;
- do not claim repository updates are complete without read-back / diff verification / commit verification;
- if `repository_patch.operations = []`, then changed-files/context-refresh required must be false unless another approved write changed cached files;
- stale labels or cleanup needs without a patch go into cleanup candidates or context-for-next.

Use the canonical transport template for patch shape. Runtime core owns the approval, safety, and verification behavior above.

### 14.2 Approval and formalization coupling

Before approval/formalization, use planned patch summaries instead of non-empty `repository_patch.v1.operations`.

Non-empty repository patch operations may be emitted only after:

- explicit approval/formalization; or
- direct formalization is allowed with explicit material-change and repository-patch approval state.

Repository patch approval does not authorize product/project execution.

### 14.3 Codex Repository Maintenance Apply

If a stage emits `repository_patch.required = true` or non-empty `repository_patch.v1.operations` after approval/formalization, it must also output:

```text
NEXT ACTION: RUN CODEX REPOSITORY MAINTENANCE APPLY/READ-BACK
```

Canonical Codex repository maintenance apply template:

```text
workflow/transport/CODEX_REPOSITORY_MAINTENANCE_APPLY.md
```

Repository maintenance is not product/project execution.

Codex repository maintenance must:

- apply only the approved `repository_patch.v1` operations;
- not infer extra cleanup;
- not run product/project execution;
- not create Task Master graph unless explicitly part of approved product execution route;
- not modify sibling Directions unless explicitly listed;
- return commit SHA or explicit no-commit reason;
- return diff verification and file read-back evidence;
- return Project Files cache refresh requirements;
- return forbidden-path confirmation to the same ChatGPT stage thread.

### 14.4 Direct-main maintenance policy

For repository maintenance in `ainazemtsau/my_global_workflow`, the default branch policy is direct-main maintenance unless the approved patch explicitly says otherwise:

```text
target branch: main
create branch: false
create PR: false
commit directly: true
push directly: true
pull before apply: true
conflict policy: scoped path conflicts only
```

Do not create a branch as fallback unless the user explicitly overrides this policy.

Stop and return NEEDS_INPUT only on scoped conflicts: same-file/path overlap, forbidden-path touch, failed validation, or pull/push conflicts affecting approved patch paths.

### 14.5 Changed Files / Context Refresh coupling

Every repository maintenance apply/read-back must report whether manual Project Files refresh is required.

If a cached shared runtime file or Direction Project File changed, manual refresh requirements must name:

- affected ChatGPT Project;
- repository path changed;
- Project File cache name;
- refresh reason;
- whether refresh blocks the next material run.

## 15\. Execution Log Entry Contract

Execution logs record observable workflow events, inputs, outputs, validation, decisions, write requests, and next routes without exposing private reasoning.

Canonical packet template:

```text
workflow/transport/EXECUTION_LOG_ENTRY.md
```

Runtime behavior rules:

- log observable facts and public rationale, not private chain-of-thought;
- every meaningful workflow event should include an Execution Log Entry;
- if `persist: true`, the matching repository patch must include the log write;
- log entries must not claim a write occurred without read-back / diff verification / commit verification;
- execution logs are evidence/friction/history layers, not default active context.

Use the canonical transport template for packet shape. Runtime core owns the behavior above.

## 16\. Execution Log target routing

Choose target log path by active state:

```text
If active Goal exists:
  target = directions/<direction-id>/phases/<phase-id>/goals/<goal-id>/execution_log.md

Else if active Phase exists:
  target = directions/<direction-id>/phases/<phase-id>/phase_execution_log.md

Else:
  target = directions/<direction-id>/execution_logs/11_DIRECTION_EXECUTION_LOG.md

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

Documentation Maintenance Gate decides whether documentation maintenance is required before or after workflow/model changes, durable Direction changes, Goal Review, Phase Close, context loading changes, documentation updates, or stale material discovery.

Canonical packet template:

```text
workflow/transport/DOCUMENTATION_MAINTENANCE_GATE.md
```

Runtime behavior rules:

- distinguish proposed documentation changes from applied documentation changes;
- do not claim documentation was updated without read-back / diff verification / commit verification;
- context refresh must name exact files;
- mark stale/superseded material only with explicit paths and reasons;
- documentation updates must stay scoped to the approved stage/result/patch;
- if documentation maintenance changes cached Project Files or runtime cache files, manual refresh must be reported.

Use the canonical transport template for packet shape. Runtime core owns the behavior above.

## 18\. Project Files Refresh Rule

Every material state change must list exact GitHub files to update or refresh in context.

Refresh means:

1.  Update GitHub repository source file.
2.  Report the changed file path in the Changed Files / Context Refresh List.
3.  If attached Project files are used as a fallback, replace only the matching GitHub export file.

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

06_CONTEXT_LIBRARY_INDEX.md changed
  -> 06_CONTEXT_LIBRARY_INDEX.md

Shared runtime core changed
  -> workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md

```

Fresh file read-back / diff verification / commit verification wins over stale attached Project files.

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
workflow/stage_prompts/

```

This registry is a runtime registry, not the prompt-development roadmap.

Do not infer "first stage to develop" from this table. Prompt development order belongs to the rebuild state, not to Direction runtime.

### Core routing behavior

| Stage ID | Name | Runtime role | Prompt source |
| --- | --- | --- | --- |
| ROUTER\_STAGE\_LAUNCHER | Router / Stage Launcher | Determine smallest safe next action; produce Launch Card / Context Request / Human Decision / Stop. | workflow/stage_prompts/ROUTER_STAGE_LAUNCHER.md |
| D0\_DIRECTION\_SETUP | Direction Setup | Create or repair a Direction container. | workflow/stage_prompts/D0_DIRECTION_SETUP.md |
| P0\_PHASE\_START | Phase Start | Start/update current Phase by Critical Constraint and Minimum Outcome. | workflow/stage_prompts/P0_PHASE_START.md |
| I0\_CAPTURE | Capture / Triage | Route raw inputs without doing the work. | workflow/stage_prompts/I0_CAPTURE.md |
| G0\_GOAL\_SELECT | Goal Select | Select/create one candidate for Goal shaping. | workflow/stage_prompts/G0_GOAL_SELECT.md |
| G1\_GOAL\_SHAPE | Goal Shape / Ruthless Cut | Shape WHAT/WHY/DONE and cut scope before HOW. | workflow/stage_prompts/G1_GOAL_SHAPE.md |
| S3\_DECIDE | Decide | Resolve a real decision with options/constraints/human conclusion. | workflow/stage_prompts/S3_DECIDE.md |
| D1\_DEEP\_RESEARCH | Deep Research | Research external evidence gaps and synthesize implications. | workflow/stage_prompts/D1_DEEP_RESEARCH.md |
| A1\_AUDIT | Audit / Challenge | Challenge high-risk/failed/irreversible plans or claims. | workflow/stage_prompts/A1_AUDIT.md |
| E1\_EXECUTION\_BRIEF | Execution Brief | Produce minimum HOW, validation, context, and Codex card if needed. | workflow/stage_prompts/E1_EXECUTION_BRIEF.md |
| F0\_FAST\_DIRECT | Fast Direct | Execute small reversible work directly with verification. | workflow/stage_prompts/F0_FAST_DIRECT.md |
| C1\_CODEX\_GRAPH\_PLAN | Codex Graph Plan | Build/validate project-local execution graph from Wave Card. | workflow/stage_prompts/C1_CODEX_GRAPH_PLAN.md |
| C2\_CODEX\_EXECUTE | Codex Execute | Execute validated graph and return evidence/return-state. | workflow/stage_prompts/C2_CODEX_EXECUTE.md |
| B1\_PROBLEM | Problem Router | Classify blocker before solving and route recovery. | workflow/stage_prompts/B1_PROBLEM.md |
| R1\_GOAL\_REVIEW\_DISTILL | Goal Review / Distill | Review Goal, distill durable knowledge, update state/docs. | workflow/stage_prompts/R1_GOAL_REVIEW_DISTILL.md |
| P9\_PHASE\_CLOSE | Phase Close | Close/pause Phase and distill phase-level outcomes. | workflow/stage_prompts/P9_PHASE_CLOSE.md |
| R0\_RECOVERY\_CLOSE | Recovery Close | Close mixed/interrupted sessions and reconstruct safe handoff. | workflow/stage_prompts/R0_RECOVERY_CLOSE.md |

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

### Phase Progress Gate and Phase Closure Contract

Every active Phase must expose enough closure information for post-Goal routing.

The Phase state should include:

```yaml
phase_closure_contract:
  closure_criteria:
    - criterion:
      evidence_required:
  phase_work_map:
    required_for_closure:
      - goal_id:
        status:
        evidence:
    optional_expansion:
      - candidate_id:
        status:
        reason_optional:
  first_phase_closing_candidate_if_known:
  after_goal_gate_policy:
    phase_progress_gate after R1: required
    R1 must not route directly to G0 only because Active Goal is none: true
    G0 allowed only after Phase Continue decision: true
    P9 required when completed Goal may satisfy Phase Minimum Outcome: true
    Context Request required when Phase Closure Contract is missing: true
```

After R1 accepts or verifies a Goal, the workflow must run a `phase_progress_gate` before selecting more Goals.

`phase_progress_gate` checks:

- whether the completed Goal satisfies or may satisfy the current Phase Minimum Outcome;
- whether remaining Goals are required_for_closure or optional_expansion;
- whether the Phase should route to `P9_PHASE_CLOSE`, continue to `G0_GOAL_SELECT`, pause, request context, or ask for a human decision.

Routing rules:

- R1 must not route directly to G0 only because Active Goal is none.
- G0 allowed only after Phase Continue decision, such as `continue_with_required_goals`.
- P9 required when completed Goal may satisfy Phase Minimum Outcome.
- Human Decision required when closure vs continuation is strategic/ambiguous.
- Context Request required when Phase Closure Contract is missing.
- Optional expansion must not be mistaken for required next Goal.

### Allowed high-level transitions

Do not maintain a transition table in this runtime core.

Normal stage-to-stage `allowed_next` transitions are defined only in:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

Runtime core may describe route-selection process, safety gates, and routing heuristics, but it must not duplicate the registry transition table.

Terminal card types are not stage IDs:

```text
Context Request
Human Decision
Stop
```

These are terminal outputs. They may be allowed outcomes, but they must not be treated as stage-to-stage transition authority.

If a selected next stage is not allowed by `STAGE_REGISTRY.md`, return a route-conflict Context Request or B1_PROBLEM. Do not guess and do not silently execute a different stage.

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

This legacy section is superseded by `## 11.6 Hard First Response and Adaptive Reviewable Work Product Gate`. Use that section for first-response modes, Proposed substance, approval, formalization, repository_patch.v1, changed_files_context_refresh, and executable next-stage launch rules.

## End-of-file marker

`END_OF_FILE: workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
