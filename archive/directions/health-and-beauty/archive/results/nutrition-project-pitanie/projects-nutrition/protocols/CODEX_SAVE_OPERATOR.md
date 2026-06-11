# Codex Save Operator Protocol

Status: active

Codex is a save-only repository maintenance writer for Project `Питание` nutrition state. Codex does not interpret nutrition content, create nutrition advice, or decide what should be eaten.

## Required Input

Codex may write only from a user-approved packet:

```yaml
nutrition_state_update_packet:
  schema: nutrition_state_update_packet.v1
  packet_status: approved_by_user
  external_write_claimed: false
  target_files:
    - path:
      operation: create_or_update
      content:
```

If `packet_status` is not `approved_by_user`, Codex must refuse to write and ask for explicit approval.

## Allowed Nutrition State Targets

```text
directions/health-and-beauty/projects/nutrition/state/USER_PROFILE_AND_CONSTRAINTS.yml
directions/health-and-beauty/projects/nutrition/research/DEEP_RESEARCH_REQUEST.md
directions/health-and-beauty/projects/nutrition/research/DEEP_RESEARCH_RESULT.md
directions/health-and-beauty/projects/nutrition/research/DEEP_RESEARCH_SYNTHESIS.md
directions/health-and-beauty/projects/nutrition/state/GLOBAL_NUTRITION_PLAN.md
directions/health-and-beauty/projects/nutrition/state/NUTRITION_HISTORY.md
directions/health-and-beauty/projects/nutrition/state/PROGRESS_METRICS.md
directions/health-and-beauty/projects/nutrition/weeks/ACTIVE_WEEK_POINTER.md
directions/health-and-beauty/projects/nutrition/weeks/current/WEEKLY_PLAN.md
directions/health-and-beauty/projects/nutrition/weeks/current/ACTIVE_WEEK_MENU.md
directions/health-and-beauty/projects/nutrition/weeks/current/WEEK_TRACKING_REPORT.md
directions/health-and-beauty/projects/nutrition/weeks/current/WEEK_REVIEW.md
directions/health-and-beauty/projects/nutrition/weeks/current/NEXT_WEEK_INPUTS.md
```

`directions/health-and-beauty/projects/nutrition/state/USER_PROFILE_AND_CONSTRAINTS.md` is legacy compatibility input only. Do not use it as the canonical Global Strategy save target.

Project protocol files may be changed only by an approved workflow execution route, not by ordinary nutrition-state save.

## Validation

After writing, Codex must provide:

- `git diff -- directions/health-and-beauty/projects/nutrition`
- changed-file list;
- file read-back of updated anchors;
- confirmation that no sibling Direction, workflow runtime, or old setup path was touched unless explicitly approved;
- Project Files refresh list.
- for Global Strategy saves, confirmation that profile, research request, research result, research synthesis, and final plan stayed separated.

## Refusal Conditions

Refuse or return `NEEDS INPUT` if the packet:

- targets forbidden paths;
- contains live clinical/medical instructions that require human/domain review;
- asks Codex to decide nutrition content;
- asks for hidden memory state;
- asks for durable write after every tracking message by default.
- asks to save a generic Global Strategy plan without separated profile, research result, and synthesis artifacts.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/protocols/CODEX_SAVE_OPERATOR.md
