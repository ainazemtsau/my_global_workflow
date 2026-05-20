# 01 - Global Strategy Chat Protocol

Status: active

Purpose: first setup or rare global strategy rebuild only.

## Required Inputs

- `state/USER_PROFILE_AND_CONSTRAINTS.md`
- user answers to missing strategic inputs
- Deep Research result, but only after `DEEP_RESEARCH_REQUEST` has been produced and run

## First-Start Sequence

```yaml
sequence:
  - read_existing_profile_if_available
  - collect_strategic_intake_only
  - state_preliminary_hypothesis_if_useful
  - output_DEEP_RESEARCH_REQUEST
  - stop_before_final_strategy
```

The first start must output `DEEP_RESEARCH_REQUEST`.

The first start must not:

- finalize `GLOBAL_NUTRITION_PLAN`;
- create `WEEKLY_PLAN`;
- generate a concrete menu;
- generate shopping list or prep plan;
- collect week logistics as the main task.

## DEEP_RESEARCH_REQUEST Format

```yaml
DEEP_RESEARCH_REQUEST:
  user_profile_summary:
  goal_and_constraints:
  acceptable_strictness:
  low_friction_requirement: true
  calories_or_BJU_or_named_diet_may_be_needed:
  foods_to_include_or_exclude_if_known:
  research_objective:
  specific_research_questions:
    - question:
      why_it_matters:
  expected_output_format_for_strategy_synthesis:
    - practical_strategy_options
    - evidence_quality_notes
    - tradeoffs
    - recommended_low_friction_default
```

## After Deep Research

Only after the user supplies the Deep Research result:

1. Synthesize the result.
2. Create `GLOBAL_NUTRITION_PLAN`.
3. Produce a save packet targeting `state/GLOBAL_NUTRITION_PLAN.md` and any approved profile updates.
4. Tell the user to refresh Project Files after Codex read-back/diff evidence.
5. Close the Global Strategy Chat.

## Output Boundary

Readable answer first. YAML only for `DEEP_RESEARCH_REQUEST` or approved save packet.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/01_GLOBAL_STRATEGY_CHAT_PROTOCOL.md
