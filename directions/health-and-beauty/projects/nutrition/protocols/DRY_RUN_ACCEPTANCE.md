# Dry Run Acceptance Protocol

Status: active

Use this protocol for synthetic validation only. It is not live nutrition execution.

## Required Checks

1. Global Strategy first start creates `DEEP_RESEARCH_REQUEST` and does not finalize strategy or generate menu.
2. Weekly Planning start creates one-week `WEEKLY_PLAN` and does not generate concrete menu.
3. Menu Chat requires `WEEKLY_PLAN` and creates menu, shopping list, and prep plan.
4. Tracking Chat requires `WEEKLY_PLAN` plus `ACTIVE_WEEK_MENU`, keeps pending questions, and has `durable_github_update: false` by default.
5. Week Close reviews `WEEK_TRACKING_REPORT`, reports unresolved items, prepares history/progress save packet, creates `NEXT_WEEK_INPUTS`, and closes the weekly chat.
6. Project Files refresh lets a fresh chat continue from GitHub-backed files without hidden memory or a giant pasted state packet.

## Evidence To Capture

```yaml
dry_run_evidence:
  project_instructions_version:
  project_files_uploaded:
  prompt_used:
  observed_behavior:
  pass:
  failure_notes:
  screenshots_or_transcript_pointer:
```

External save claims are valid only with Codex read-back/diff evidence.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/protocols/DRY_RUN_ACCEPTANCE.md
