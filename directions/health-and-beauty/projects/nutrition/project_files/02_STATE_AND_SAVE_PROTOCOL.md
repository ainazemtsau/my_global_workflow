# 02 State And Save Protocol

```yaml
nutrition_project_file:
  schema: nutrition_project_file.v1
  project: "Питание"
  file: 02_STATE_AND_SAVE_PROTOCOL.md
  status: active
  purpose: durable_state_update_packet_codex_save_boundary_and_refresh_protocol
```

## State Authority

```yaml
state_authority:
  canonical_state_root: directions/health-and-beauty/projects/nutrition/state/
  chatgpt_project_files: refreshable_cache_only
  chat_history: non_authoritative
  codex: save_only_repository_maintenance_writer
```

Project `Питание` may propose durable state changes. It must not claim those changes were saved externally.

Codex may apply only user-approved packets and must return file read-back, diff, and forbidden-path evidence.

## Canonical State Files

```yaml
canonical_state_files:
  - directions/health-and-beauty/projects/nutrition/state/USER_NUTRITION_BASELINE.md
  - directions/health-and-beauty/projects/nutrition/state/CURRENT_NUTRITION_PLAN.md
  - directions/health-and-beauty/projects/nutrition/state/ACTIVE_WEEK_MENU.md
  - directions/health-and-beauty/projects/nutrition/state/WEEK_TRACKING_REPORT.md
  - directions/health-and-beauty/projects/nutrition/state/REVIEW_AND_NEXT_WEEK.md
```

## Durable Update Packet

After readable output, emit this packet when durable state should change:

```yaml
nutrition_state_update_packet:
  schema: nutrition_state_update_packet.v1
  source_project: "Питание"
  packet_status: proposed_for_user_approval
  external_write_claimed: false
  reason_for_update: []
  target_files: []
  updates:
    USER_NUTRITION_BASELINE.md:
      changed: false
      summary: []
    CURRENT_NUTRITION_PLAN.md:
      changed: false
      summary: []
    ACTIVE_WEEK_MENU.md:
      changed: false
      summary: []
    WEEK_TRACKING_REPORT.md:
      changed: false
      summary: []
    REVIEW_AND_NEXT_WEEK.md:
      changed: false
      summary: []
  pending_questions:
    blocking: []
    useful_later: []
  project_files_refresh_required_after_save: true
  next_recommended_action:
```

`packet_status` stays `proposed_for_user_approval` until the user explicitly approves saving.

## Codex Save Boundary

Codex may save only when the user provides a packet with:

```yaml
packet_status: approved_by_user
external_write_claimed: false
```

Codex must refuse or return NEEDS INPUT when:

- the packet is absent;
- approval is missing;
- a target file is outside the canonical state files;
- the packet asks Codex to decide nutrition content;
- the packet requires clinical, supplement, fasting, lab, training, cardio, or recovery advice;
- the repository file structure prevents a small safe edit.

Codex must not give nutrition advice.

## Project Files Refresh Protocol

After Codex returns save/read-back evidence, the user manually refreshes the ChatGPT Project Files cache from GitHub:

1. Upload or replace the five state files from `state/`.
2. Upload or replace these protocol files:
   - `00_NUTRITION_START_HERE.md`
   - `01_NUTRITION_LOOP_PROTOCOL.md`
   - `02_STATE_AND_SAVE_PROTOCOL.md`
   - `03_DRY_RUN_ACCEPTANCE.md`
3. Start a fresh Project chat and ask it to read `00_NUTRITION_START_HERE.md`.
4. Confirm the chat resumes from saved state without hidden memory or a giant pasted packet.

If Project Files are stale, ask the user to refresh the exact stale files. Do not invent current state.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/02_STATE_AND_SAVE_PROTOCOL.md`
