# RESULT — s-repair-007 (repair, 2026-06-13) — reconcile stale Fable-5 model labels in NOW.md

```yaml
RESULT s-repair-007
direction: indie-game-development
play: repair
node: g-9c41
outcome: |
  NOW.md no longer contradicts the frontier-model decision. The active_tasks t-1/t-2/t-3
  `kind` labels and the bet `forecast` — which still named "Fable 5" / "the Fable-5 window" —
  are relabeled to the decided builder (Opus 4.8; Fable 5 unavailable). t-1's `kind` now
  points to next.model_routing as the single source of the build-model routing, so the model
  is no longer duplicated into a field that silently drifts. No task status, goal, done_when,
  appetite, kill_by, bet selection, or next CALL changed — this is reconciliation, not progress.
evidence: |
  Contradiction (branch wt/indie-game-development code-review, finding #2): NOW.md
  active_tasks t-1.kind "executor (Fable 5)" (and t-2.kind, t-3.kind "Fable 5 if before
  2026-06-22, else Opus 4.8", and forecast "the Fable-5 window catches the hardest net tasks")
  contradicted the SAME file's next.model_routing and history/s-decide-001.md (LOG 2026-06-13
  "decide"): "Fable 5 unavailable … BUILD = Claude Code + Opus 4.8". s-decide-001 scoped its
  own state_changes to "no task/bet change", which left these executor-model fields stale.
  Reconstruction (authority order: the decision record + next.model_routing outrank the stale
  labels): the builder is Opus 4.8; the Fable-5 window no longer exists, so the forecast clause
  asserting one is simply false. Faithful propagation of an already-made decision.
state_changes: |
  live/indie-game-development/NOW.md:
    - active_tasks t-1.kind: "executor (Fable 5)" -> "executor (Opus 4.8 — Fable 5 unavailable;
      build model per next.model_routing)".
    - active_tasks t-2.kind: "executor (Fable 5)" -> "executor (Opus 4.8 — Fable 5 unavailable)".
    - active_tasks t-3.kind: "executor (Fable 5 if before 2026-06-22, else Opus 4.8)"
      -> "executor (Opus 4.8 — Fable 5 unavailable)".
    - active_bet.forecast: dropped the now-false "the Fable-5 window catches the hardest net
      tasks" clause -> "the plan kills this risk first (the hardest net task t-1 runs first)".
    - Nothing else touched: t-1 stays `ready`, bet g-9c41 stays active, kill_by/appetite/cut_list
      intact, next stays CALL c-exec-002.
  live/indie-game-development/LOG.md: repair line appended.
captures:
  - "code-review also flagged, NOT fixed in this repair (routed where the rules put them): (a) `decide`
     is not one of the 9 plays and s-decide-001 is not a full RESULT packet (no play_check/outcome/
     evidence/log) that G10 should have bounced — an OS-rule gap (no sanctioned home for recording an
     owner decision); logged to os/FRICTION.md, belongs in a MAINTENANCE session. (b) NOW.md task
     statuses use `ready`/`blocked_on <id>` while schema/direction-files.md allows only
     open|active|blocked|done — pre-existing & systemic; logged to os/FRICTION.md to reconcile
     schema<->practice in MAINTENANCE."
  - "next (c-exec-002) context cites repo artifacts (CoreBuildMarker placeholder, FNV-1a) absent from
     s-setup-001 evidence — low confidence; the executor reads ground truth from the repo at PLAN, so
     left as-is."
  - "repo canonization (new GasCoopGame + Unity 6.3 LTS into CHARTER.md) flagged by 3 sessions' captures
     is not yet in c-frame-002's recorded scope — now ripe for shape/pulse triage since setup is DONE."
decisions_needed: []
play_check: |
  1 name-the-contradiction: done (NOW.md kind/forecast labels named Fable 5 vs next.model_routing +
    s-decide-001 = Fable 5 unavailable / Opus 4.8).
  2 reconstruct: done (history/s-decide-001.md + NOW.next.model_routing outrank the stale labels;
    builder = Opus 4.8; the Fable-5 window no longer exists — artifacts/decision over labels).
  3 propose-corrected-state: done (4 NOW.md edits, one-line justification each; shown to the owner
    in the review reply diff).
  4 confirm (owner): done — owner instruction «проблемы не выглядят сложными если можешь то сделай
    фикс для них» (apply the review fixes); the four reconciliations were shown before applying.
  5 friction: no FRICTION line for THIS repair — the stale labels are a one-off under-scoped
    state_change in s-decide-001, not an OS hole. The OS-rule gaps the review exposed (no `decide`
    play; NOW status-schema drift) ARE logged to os/FRICTION.md, where rule-defect friction belongs.
log: |
  repair: reconciled stale Fable-5 executor labels (t-1/t-2/t-3 kind + bet forecast) with the
  Opus-4.8 routing decided in s-decide-001; t-1 kind now points to next.model_routing as the
  single source. No task/bet/status change.
next: |
  Unchanged — NOW.next stays CALL c-exec-002 (t-1 build on GasCoopGame; full packet in NOW.md `next`).
```

END_OF_FILE: live/indie-game-development/history/s-repair-007.md
