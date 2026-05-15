# AD-WF-RT-001 — Single Runtime Authority Model

```yaml
artifact_control:
  artifact_name: "AD-WF-RT-001 Single Runtime Authority Model"
  schema: architecture_decision.v1
  owner_layer: runtime
  status: accepted
  repo_path: "workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md"
  freshness: refresh_when_runtime_authority_boundaries_change
  last_updated: "2026-05-13"
```

## Decision

Workflow vNext-R uses one authority per runtime rule category.

This decision is accepted as the minimal unblock authority model for routing, prompt boundary, prompt delivery, transport schema boundary, and runtime core boundary.

## Authority model

| Rule category | Authority |
| --- | --- |
| Canonical workflow source-of-truth marker | `WORKFLOW_SOURCE_OF_TRUTH.md` |
| Runtime behavior and precedence | `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md` |
| Long GitHub file read completeness | `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md` |
| Project Files runtime cache | `workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md` |
| Stage identity, prompt path/status, target runtime, activation, and normal stage-to-stage transitions | `workflow/stage_registry/STAGE_REGISTRY.md` |
| Stage-specific mission, inputs, gates, and constraints | exact file under `workflow/stage_prompts/<STAGE_ID>.md` |
| Canonical packet schemas and transport templates | `workflow/transport/*.md` |
| Packet use behavior, runtime precedence, formalization coupling, and repository maintenance rules | `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md` |
| Direction runtime state | `directions/<direction-id>/project_files/00-08` |

Runtime core must not maintain full packet schema bodies or duplicate registry stage tables.

Runtime core may contain compact behavior references, schema IDs, route-process rules, and pointers to canonical authority files.

If a packet field/template in runtime core conflicts with the matching canonical transport template, the canonical transport template wins for packet shape; runtime core still wins for behavior, approval/formalization, routing process, and repository maintenance rules.

If a stage identity, prompt path/status, activation, or `allowed_next` detail in runtime core conflicts with `STAGE_REGISTRY.md`, the registry wins.

## Routing authority

`workflow/stage_registry/STAGE_REGISTRY.md` is the only authority for normal stage-to-stage `allowed_next` transitions.

Runtime core, stage prompts, stage registry interfaces, and transport templates must not maintain independent allowed transition tables.

Terminal card types are not stage IDs. `Context Request`, `Human Decision`, and `Stop` are terminal outputs. They may be allowed terminal outcomes, but they do not create stage-to-stage transition authority.

## Route conflict rule

Route conflict is selected-route-vs-registry.

If a selected next stage is not allowed by the current stage row in `STAGE_REGISTRY.md`, the current run must return a route-conflict Context Request, B1_PROBLEM, Human Decision, or Stop according to the situation.

Do not compare prompt-maintained route lists against registry-maintained route lists. Prompt-maintained route lists are non-authoritative after this decision.

## Stage prompt boundary

Stage prompts are black-box stage-specific modules. They may define:

- stage mission;
- required inputs;
- stage-specific gates;
- stage-specific constraints;
- stage-specific output obligations.

Stage prompts must not be treated as authority for:

- `allowed_next` transition tables;
- packet schemas;
- repository maintenance branch policy;
- Project Files cache rules;
- GitHub long-file read completeness;
- cross-Direction rollout policy.

If a stage prompt contains an old route list or copied packet schema, the shared authority file wins.

## Runtime core boundary

`WF_VNEXT_R_RUNTIME_CORE.md` defines runtime behavior, precedence, routing process, formalization gates, Codex role separation, and repository maintenance rules.

It must not maintain a separate full `allowed_next` transition table. It may describe how to consult `STAGE_REGISTRY.md`.

## Prompt delivery model

Stage prompt file existence is not prompt availability in a chat.

Valid prompt delivery modes after this decision:

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

`manual_prompt_required` means the chat must request the exact stage prompt from the user/Codex and must not auto-fetch or reconstruct it.

`codex_verified_local_bundle` means Codex read the exact stage prompt from a local checkout, verified completeness, and supplied the prompt or bundle metadata.

## Transport boundary

`workflow/transport/*.md` is the canonical packet-template surface for transport packet shapes.

Canonical packet templates include, at minimum:

```text
workflow/transport/STAGE_LAUNCH_CARD.md
workflow/transport/STAGE_RESULT_PACKET.md
workflow/transport/CONTEXT_REQUEST_CARD.md
workflow/transport/HUMAN_DECISION_CARD.md
workflow/transport/REPOSITORY_PATCH.md
workflow/transport/EXECUTION_LOG_ENTRY.md
workflow/transport/DOCUMENTATION_MAINTENANCE_GATE.md
workflow/transport/CODEX_REPOSITORY_MAINTENANCE_APPLY.md
workflow/transport/CODEX_WAVE_CARD.md
workflow/transport/CODEX_RETURN_PACKET.md
workflow/transport/RECOVERY_CLOSE_PACKET.md
```

Runtime core remains authority for behavior, precedence, approval/formalization, route process, Codex role separation, repository maintenance rules, and Project Files refresh/reporting rules.

Any route fields in transport files are snapshots only. They must not override `STAGE_REGISTRY.md`.

If a transport packet route snapshot conflicts with the registry, return route-conflict Context Request / B1_PROBLEM / Human Decision / Stop.

## Minimal unblock policy

This decision authorizes minimal unblock changes:

1. declare registry as sole route authority;
2. replace runtime transition table with registry pointer;
3. replace `request_from_repository` with explicit prompt delivery modes;
4. neutralize prompt-maintained route lists;
5. mark transport/interface route lists as derived or non-authoritative;
6. require cache refresh reporting for all active Direction Projects when shared runtime cached files change.

## Deferred cleanup

Completed since this decision:

- transport templates were converted to canonical `workflow_packet: 1` / `schema: *.v1` packet shapes;
- stale prompt route-list authority was neutralized;
- stage prompt EOF markers were added;
- stale rebuild/test-active metadata was cleaned from runtime-facing prompt/interface/Codex surfaces;
- prompt slimming slices S1-S4 reduced copied maintenance/formalization/transport/schema boilerplate;
- runtime transport authority boundary was aligned so `workflow/transport/*.md` owns canonical packet templates;
- runtime-core packet schema bodies were replaced by transport references;
- duplicate runtime-core registry snapshot text was replaced with a pointer to `workflow/stage_registry/STAGE_REGISTRY.md`.

Deferred to later approved patches:

- split runtime core into smaller authority files only after boundary/reference cleanup is stable;
- backfill Workflow Governance Phase Memory if normal lifecycle history is needed.

## End-of-file marker

`END_OF_FILE: workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md`
