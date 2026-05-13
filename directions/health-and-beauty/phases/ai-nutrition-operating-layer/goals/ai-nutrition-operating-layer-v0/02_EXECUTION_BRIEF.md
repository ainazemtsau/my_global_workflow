# E1 Execution Brief — AI Nutrition Operating Layer v0

```yaml
artifact_control:
  artifact_name: "E1 Execution Brief — AI Nutrition Operating Layer v0"
  schema: execution_brief.v1
  owner_stage: E1_EXECUTION_BRIEF
  status: formalized
  created_at: "2026-05-13"
  direction: directions/health-and-beauty
  phase: directions/health-and-beauty/phases/ai-nutrition-operating-layer
  goal: directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0
```

## Route decision

Selected route: `D1_DEEP_RESEARCH`

E1 rejects `F0_FAST_DIRECT` for now because the next safe action depends on current ChatGPT/project/connector/tool behavior and unresolved storage/source-of-truth architecture.

## Research Need Gate

```yaml
research_need_gate:
  research_required: true
  reason:
    - current_tool_or_platform_behavior
    - architecture_or_storage_tradeoff
    - source_quality_or_freshness_matters
    - user_explicitly_requested_research
  research_depth_hint: scoped
```

## Objective for D1

Research the minimal operational architecture for AI Nutrition Operating Layer v0 before the final v0 document is created.

D1 should answer:

```text
What is the smallest low-friction architecture for using ChatGPT as an AI nutrition operating layer without one endless chat, heavy tracking, or unverified storage/tool assumptions?
```

## D1 research scope

D1 should research:

- whether a separate ChatGPT Project "Питание" is the right container;
- how to use short operational chats instead of one long degraded chat;
- where persistent state should live;
- what ChatGPT can read automatically;
- what ChatGPT can update only with confirmation or manual save blocks;
- feasibility of Notion / Google Drive / GitHub / Project files / manual save block as storage/source options;
- how to keep user input minimal: a few words, photo, "ate off-menu", "skipped", "overeating", "hungry";
- how to avoid tracker/database setup while still preserving state;
- restart/context-refresh protocol for weeks/months of use.

## Explicit exclusions

D1 must not research or implement:

- diet science;
- clinical nutrition;
- MacroFactor workflow;
- self-hosted tracker setup;
- detailed calorie/macro ledger;
- API/import automation;
- perfect Notion/Trillium/GitHub database design;
- huge recipe vault;
- final AI Nutrition Operating Layer v0 artifact.

## Expected result after D1

D1 should return to:

```text
E1_EXECUTION_BRIEF
```

if research makes the architecture clear enough for execution brief, or route to:

```text
S3_DECIDE
```

if evidence leaves a meaningful human-owned storage/tooling/privacy tradeoff.
