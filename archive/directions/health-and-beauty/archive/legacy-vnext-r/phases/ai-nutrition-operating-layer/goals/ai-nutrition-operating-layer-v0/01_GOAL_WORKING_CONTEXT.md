# Goal Working Context — AI Nutrition Operating Layer v0

## Direction

`directions/health-and-beauty`

## Phase

`Собрать AI-операционный слой питания без тяжёлого трекинга`

Path:

`directions/health-and-beauty/phases/ai-nutrition-operating-layer`

## Phase fit

This Goal directly advances the active Phase minimum outcome: an AI Nutrition Operating Layer v0 that connects state, active menu, modes, exceptions, recipes/prep, review, storage, and context refresh.

## Working interpretation

This Goal is not about writing one menu or creating one nutrition chat.

It is about building a practical ChatGPT-based operating layer that can handle menu planning, daily food decisions, exceptions, recipes, prep, state summaries, and context refresh.

## Scope in

- AI nutrition command/process layer.
- Nutrition State Packet.
- Active Menu object.
- Daily Nutrition Operator mode.
- Menu Architect mode.
- Recipe / Prep Builder mode.
- Review / State Update mode.
- Exception-only tracking protocol.
- Day-correction logic.
- Storage/save protocol.
- Restart/context-refresh rules.
- Sample flows for validation.
- Optional use of existing menu/prep/equipment notes only if available and useful.

## Non-goals

- MacroFactor-centered workflow.
- Heavy calorie/macro ledger.
- Tracking every meal by default.
- Self-hosted tracker setup.
- API/import automation.
- Perfect Notion/Trillium database design.
- Huge recipe vault.
- Daily food log as source of truth.
- Medical or clinical nutrition plan.
- Full health architecture redesign.
- Executing the nutrition system inside G1.
- Reducing the Goal to menu creation only.

## Scope cuts

- No database setup in v0.
- No tracker migration.
- No automation.
- No full recipe library.
- No perfect storage tooling decision.
- No detailed meal-by-meal history.
- No nutrition optimization beyond process scaffolding.
- No Codex product/project execution from G1.

## Deferred candidates

- Tool-specific storage implementation in Notion, Trillium, GitHub, or another system.
- Actual menu generation from full personal baseline.
- Recipe vault expansion.
- MacroFactor comparison or selective integration.
- Food inventory/prep automation.
- Long-term analytics.

## Constraints

- MacroFactor is not central.
- Heavy detailed tracking is out of scope by default.
- One long ChatGPT chat must not be the sole persistent memory.
- Menu is an object inside the AI operating layer, not the whole Goal.
- Durable state should be saved as compact objects, not daily noise.

## Risk triggers

Escalate or stop if:

- user requests clinical/medical nutrition advice;
- work starts requiring full tracker or database setup;
- persistent storage requires repository/tool writes without approval;
- existing MacroFactor materials conflict with the new operating layer;
- Goal expands into full health architecture;
- validation cannot be done without missing user-owned preferences/baseline;
- any stage attempts product/project execution before E1.

## Assumptions

- The Goal should produce a reusable operating layer, not run a diet intervention.
- Missing personal baseline/preferences can be represented as required input fields or placeholders in v0.
- Actual storage tooling can remain abstract until E1 or later execution.
- Existing MacroFactor materials are historical evidence only.
- The output should be small enough to test immediately through sample flows.

## Required context for next stage

Required:

- Direction Project Files 00-06.
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.
- `workflow/stage_registry/STAGE_REGISTRY.md`.
- `workflow/stage_prompts/E1_EXECUTION_BRIEF.md`.
- Current Phase brief.
- Current Phase working context.
- This Goal Contract.
- This Goal Working Context.

Request only if needed:

- Existing menu / prior nutrition menu materials.
- Nutrition baseline and preferences.
- Current kitchen equipment notes: air fryer, multicooker, vacuum sealer.
- Recipe/prep notes.
- Storage/tool preference notes: Trillium, Notion, GitHub, ChatGPT connections, or other.
- Prior MacroFactor files as historical evidence only.

## Allowed actions for E1

- Produce minimum execution brief.
- Define exact v0 artifact structure.
- Define validation flow.
- Decide whether execution can be F0_FAST_DIRECT or needs Codex planning.
- Request only blocking missing context.
- Keep storage protocol tool-agnostic unless bindings are verified.

## Forbidden actions

- Do not execute the Goal inside E1.
- Do not run old MacroFactor Wave 1.
- Do not start tracker/database setup.
- Do not create detailed calorie/macro ledger.
- Do not assume Notion/Trillium/GitHub/automation bindings are available.
- Do not make one ChatGPT thread the only memory layer.
- Do not reduce the Goal to menu creation only.

## Context loading notes

- Default-load Project Files 00-06 and runtime core.
- Do not default-load archived MacroFactor material.
- Load historical MacroFactor files only if needed as evidence.
- Stage prompts remain request-only.
- Next stage prompt source path: `workflow/stage_prompts/E1_EXECUTION_BRIEF.md`.

## Source freshness notes

- Current source read from main commit `692724800ea19243b89c49c6bf5e99d3e14da5dc`.
- P0 patch is reported merged and pushed to main.
- No active Goal existed before this G1 formalization.
