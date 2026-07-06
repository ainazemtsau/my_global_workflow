# RESULT — repair s-repair-nowmd-001 (2026-07-06)

play: repair
direction: indie-game-development
base_commit: ef25259 (s-work-056), working tree clean
trigger: owner — «NOW.md 729 строк / 8076 слов, впятеро над потолком ~150; как исправить эту проблему». Owner approved the repair diff («да»).

## 1. What diverged
NOW.md had grown to 753 lines / ~8k words — ~5× the schema soft ceiling (~150,
os/schema/direction-files.md). Every section carried the exact drift classes the schema names:
- `bet.current_truth` (~34 lines) — the out-of-template running-narrative field the schema names verbatim as drift.
- `tasks[].status_note` + `kill_by` (~70 lines) — fields absent from the task template (id/goal/done_when/status).
- `open_calls` (~135 lines) — closed/superseded CALLs kept as `#` comment blocks (violates pending-only).
- `decisions` (~255 lines) — 13 answered/discharged decisions retained (violates pending-only).
- `next` (~68 lines) — a status digest, not the required single CALL/pointer.
- `next_slices` / `history_pointers` / `parallel_tracks` (verbose) / `sources` — fields outside the NOW template.

This is instance #3 of the hot-state-bloat class (FRICTION 2026-06-29 = #1, 2026-07-02 = #2). The 2026-07-02
maintenance fix installed the ~150-line ceiling + "pointers, not evidence" + audit/pulse/repair routing, but
EXPLICITLY deferred the per-direction TRIM to a separate repair session — which was never run for indie NOW.md.
Per that entry's own litmus, instance #3 → the cause is audit/pulse not being physically run, not a missing rule.

## 2. Reconstruction (repair step 2)
All trimmed content is recoverable — every closed open_call and answered decision carries a `Record:`/`source:`
pointer to history/ or work/; the writer already stores each full RESULT verbatim in history/ (169 files; LOG.md
indexes them); git holds the pre-repair NOW.md at ef25259. No work/ snapshot needed (repair.md step 3). The two
genuinely-pending decisions (d-marketing-wake-001, d-coop-interdependence-repin-001) verified against the file's
own line 751 ("Still pending owner: …").

CONCURRENCY RECONCILED: s-work-056 (ef25259) landed mid-session (the session-start snapshot was at s-work-055 /
3065f96) and added an owner clarification to c-visual-006 — «шипучий режим» = the two-colour preview LABEL only
(no bubbling/particle/boiling FX); the base gas passport is required for every gas; an extensible render-only
attachment path is reserved but NO special look modules are built in Stage 2. Preserved in the trimmed
c-visual-006 open_call note + the g-7e15 track line (checked git show ef25259 before writing).

## 3. Corrected state (repair step 3)
NOW.md collapsed to the schema template, 753 → 106 lines:
- bet: node / goal / appetite / kill_by (dropped current_truth, status, sources).
- tasks: one active slice Sc-reactions (done Sc-kernel/Sc-rep recited in bet.goal; detail in LOG/history).
- open_calls: c-exec-021 + c-visual-006 only (all closed `#`-comment calls dropped).
- decisions: d-marketing-wake-001 + d-coop-interdependence-repin-001 only (13 answered dropped).
- parallel_tracks: one state line per track (g-7e15 / g-d3a8 / g-2f8c / codex-sidecar).
- next: single CALL pointer → work/c-exec-021-call.md.
Road, TREE, CHARTER unchanged. Nothing marked done that was not already done (Sc-reactions = active, not done).

## state_changes
- NOW.md ← the corrected 106-line file.
- LOG.md ← one repair entry appended (naming what diverged).
- history/2026-07-06-s-repair-nowmd-001.md ← this RESULT.

## next (unchanged by the repair)
CALL: work/c-exec-021-call.md — fire c-exec-021 (Sc-reactions) in a fresh owner-present GasCoopGame_dev PLAN.

## Friction / recurrence (repair step 5 — NOT fixed here; os/** belongs to a maintenance session on main)
Instance #3 of hot-state bloat. Per the 2026-07-02 litmus, the durable fix is not another rule but running
audit/pulse on a cadence (the deferred trim + the unrun weekly hot-state-hygiene pulse). Candidate = pulse
automation (os/adapters/runtime.md), blocked on the `claude -p` login issue. NOT actioned in this session:
editing os/FRICTION.md from a direction worktree would repeat the 2026-07-03 "os/** committed on a direction
branch" mistake — raise it as a maintenance REQUEST on main. Also observed: LOG.md is 343 lines and format-drifted
(date-first entries at top vs dash/session-id-first at bottom) → a separate rotation/repair, not done here.

END_OF_FILE: live/indie-game-development/history/2026-07-06-s-repair-nowmd-001.md
