# 05 Review And Sync

```yaml
nutrition_project_file:
  schema: nutrition_project_file.v1
  project: "Питание"
  file: 05_REVIEW_AND_SYNC.md
  status: active
  purpose: day_week_review_carryover_and_state_update_packets
```

## Review Protocol

For day or week review, produce:

- short readable summary;
- keep/change/remove list;
- what worked;
- what created friction;
- preference discoveries;
- next-cycle delta;
- pending questions;
- update packet if durable state should change.

## Review Template

```yaml
review_result:
  schema: nutrition_review_result.v1
  period: daily | weekly | cycle
  source_events: []
  keep: []
  change: []
  remove: []
  discovered_preferences: []
  next_cycle_delta:
    menu_changes: []
    prep_storage_changes: []
    fallback_changes: []
  pending_questions:
    blocking: []
    useful_later: []
```

## State Update Packet

Use this packet after readable output when durable state should change:

```yaml
nutrition_state_update_packet:
  schema: nutrition_state_update_packet.v1
  source_project: "Питание"
  packet_status: proposed_for_user_approval
  external_write_claimed: false
  reason_for_update: []
  target_files:
    - directions/health-and-beauty/projects/nutrition/project_files/01_NUTRITION_BASE.md
    - directions/health-and-beauty/projects/nutrition/project_files/02_MENU_PREFERENCES.md
    - directions/health-and-beauty/projects/nutrition/project_files/03_ACTIVE_CYCLE.md
    - directions/health-and-beauty/projects/nutrition/project_files/04_TRACKING_AND_EXCEPTIONS.md
    - directions/health-and-beauty/projects/nutrition/project_files/05_REVIEW_AND_SYNC.md
  updates:
    nutrition_base:
      changed: false
      summary: []
    menu_preferences:
      changed: false
      summary: []
    active_cycle:
      changed: false
      summary: []
    tracking_and_exceptions:
      changed: false
      summary: []
    review_and_sync:
      changed: false
      summary: []
  pending_questions:
    blocking: []
    useful_later: []
  next_recommended_action:
```

The packet is a proposal until the user approves saving. Do not claim that it has been saved.

## Fresh Chat Carryover

When the user wants a new chat or context is long, output:

- current baseline summary;
- menu preferences summary;
- active cycle summary;
- current day/week position;
- important events and exceptions;
- latest review;
- pending questions;
- next recommended action;
- latest update packet status.

## Durable Update Triggers

Update this file when:

- a day/week/cycle review is completed;
- a carryover block is created;
- the latest packet status changes;
- review rules or recurring friction patterns should be preserved.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/05_REVIEW_AND_SYNC.md`
