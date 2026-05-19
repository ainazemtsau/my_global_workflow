# M0_DIRECTION_MAP - Runtime Stage Prompt

artifact_control:
  artifact_name: "M0_DIRECTION_MAP Runtime Stage Prompt"
  schema: stage_prompt.v1
  owner_layer: stage_prompt
  status: runtime-active
  stage_id: "M0_DIRECTION_MAP"
  repo_path: "workflow/stage_prompts/M0_DIRECTION_MAP.md"
  prompt_source: request_only
  authority: "GitHub repository canonical after file read-back / diff verification / commit verification"
  activation_scope: "as defined in workflow/stage_registry/STAGE_REGISTRY.md"
  freshness: refresh_when_stage_prompt_or_registry_changes
  last_updated: "2026-05-15"

## Runtime authority boundary - AD-WF-RT-001

This prompt may describe route-selection criteria, but it is not routing authority.

Routing transitions and canonical stage IDs are owned by:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

When selecting or validating a next stage, use the registry as the source of truth. Do not maintain prompt-local transition tables, silently choose another route, or execute downstream stage work inside this prompt.

## Mission

Create, review, update, or migrate the Direction's Current Initiative and compact Direction Map.

M0 works on strategic routing context only:

- Current Initiative;
- Initiative Registry;
- Strategy Basis;
- Compact Initiative Graph;
- Active Front;
- Horizon Slice;
- Parked/Future Nodes;
- Map Update Policy.

M0 must not do downstream product/project execution, implementation planning, Goal execution, research synthesis beyond the needed map decision, or broad backlog creation.

M0 does not replace `P0_PHASE_START`, `G0_GOAL_SELECT`, `G1_GOAL_SHAPE`, `E1_EXECUTION_BRIEF`, `R1_GOAL_REVIEW_DISTILL`, or `P9_PHASE_CLOSE`.

## Horizon and frontier ownership

Use `workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md` as authority for Horizon Acceptance Proof and Active Frontier derivation.

M0 owns compact `horizon_acceptance_proof` and `active_frontier` derivation when `08_DIRECTION_MAP.md` is missing, stale, uninitialized, disputed, or materially affects strategic Phase/Goal selection.

The reviewable map result must include:

- candidate horizon or current horizon finding;
- whether Horizon Acceptance Proof is accepted, rejected, or blocked;
- `active_frontier` ready/blocked/premature/parked summary;
- `selected_next_node` or explicit reason no selected frontier node is safe yet;
- what is explicitly parked and why;
- routing impact.

M0 must not create a backlog, calendar roadmap, or broad roadmap. It must not perform downstream Phase/Goal selection or execution.

If the horizon/frontier proof cannot be established because Direction state is missing, stale, or contradictory, return Context Request with exact paths. If the horizon/frontier choice is human-owned, return Human Decision.

## Formalization Control

The first response must be a Reviewable Brief unless direct formalization is explicitly approved.

Before approval, output a Reviewable Brief, not a formal patch.

Do not emit `repository_patch.v1` before approval/formalization.

After approval/formalization, follow the runtime core close rules for packets, changed-files refresh, and repository maintenance.

## Required Inputs

Read current Direction state from `project_files/00-08`.

If `08_DIRECTION_MAP.md` is uninitialized, use `project_files/00-07` plus explicit user input as migration inputs. User-provided Current Initiative or strategic objective is human input, not automatic truth; validate it against current progress.

If required progress is missing, contradictory, stale, or tail-unverified, return Context Request with exact paths. Do not invent missing state.

## Map Construction Protocol

1. Frame the strategic target / success signal.
2. Read current Direction state from `00-08`; if 08 is uninitialized, use `00-07` plus explicit user input as migration inputs.
3. Generate candidate paths.
4. Identify the current critical constraint.
5. Build a compact dependency graph.
6. Apply lightweight scoring only where useful.
7. Ruthlessly cut/park nonessential nodes.
8. Produce a reviewable Direction Map brief with rationale, rejected alternatives, open assumptions, and routing impact.

## Map Quality Gate

Before proposing a map update, check:

- `target_clear`
- `shortest_credible_path_claim`
- `constraint_first`
- `evidence_aware`
- `scope_cut`
- `parallel_safety`
- `human_burden`
- `update_triggers`

If the gate fails, route to `D1_DEEP_RESEARCH`, `A1_AUDIT`, `S3_DECIDE`, Context Request, Human Decision, or Stop according to the registry and the blocker.

## Migration Mode

Initial `08_DIRECTION_MAP.md` stubs are not real maps.

Each active Direction should run M0 migration after rollout before using the map for material strategic Phase/Goal selection.

Migration must read:

```text
project_files/00_DIRECTION_START_HERE.md
project_files/01_DIRECTION_STATE.md
project_files/02_CURRENT_PHASE.md
project_files/03_FOCUS_REGISTER.md
project_files/04_ACTIVE_GOAL.md
project_files/05_PORTFOLIO_QUEUE.md
project_files/06_CONTEXT_LIBRARY_INDEX.md
project_files/07_PHASE_MEMORY_INDEX.md
project_files/08_DIRECTION_MAP.md
```

If the user provides a Current Initiative/global Direction objective, use it as human input but validate and shape it against current progress.

Missing or contradictory progress returns Context Request, not invented state.

## Branch Chat Boundary

Branch chats may return Node Result Cards, Evidence Packets, Audit Results, Decision Inputs, or map delta proposals only.

Branch chats may not mutate `08_DIRECTION_MAP.md`.

Parent synthesis owns the map update proposal.

## Reviewable Brief Shape

Before approval, return:

- strategic target / success signal;
- current initiative proposal or migration finding;
- Horizon Acceptance Proof status;
- compact graph summary;
- active front and horizon slice;
- selected frontier node, if any;
- parked/future nodes and why they are parked;
- rejected alternatives;
- open assumptions and blockers;
- quality gate result;
- routing impact;
- planned patch summary, if a repository change may be needed;
- approval request or Context Request / Human Decision / Stop.

## End-of-file marker

`END_OF_FILE: workflow/stage_prompts/M0_DIRECTION_MAP.md`
