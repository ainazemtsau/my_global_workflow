RESULT
outcome: |
  NOW.md hot-state hygiene repair: collapsed the out-of-schema `bet.current_truth` field (81 lines,
  original synthesis not duplicated anywhere) to a short current-status summary + pointers, and
  collapsed 5 already-answered `decisions` entries (d-gas-richness-tiers-001, d-simaudit-package-001,
  d-sparse-tick-kernel-001, d-demo-road-001, d-biglevels-tree9-001) to one-line "answered" pointers per
  the pre-existing NOW hygiene rule (answered decisions move out; only pending ones stay). NOW.md:
  584 → 393 lines.
  LOG.md hot-state hygiene repair: entries older than 2026-06-29 (193 lines, sessions 2026-06-11
  through 2026-06-28) moved VERBATIM — unedited — to history/LOG-archive-indie-game-development.md,
  leaving the most recent tail (2026-06-29 through 2026-07-02) in LOG.md unedited. LOG.md: 273 → 82
  lines. Fixed one broken cross-reference found during the archival pass: a LOG.md line pointed to
  `history/s-reshape-sparse-dominant-001.md`, which does not exist; corrected to the real file
  `history/2026-06-30-s-reshape-sparse-dominant-001.md`.
  Root cause and rule fix already logged separately (os/FRICTION.md, 2026-07-02 entries; os/**
  commits 1943a76 + 92826e8) — this session executes that fix against this direction's state.
evidence: |
  work/now-current-truth-snapshot-2026-07-02.md holds the full pre-repair current_truth text,
  verified byte-identical against the original NOW.md field before trimming.
  history/LOG-archive-indie-game-development.md holds the archived LOG entries, verified
  byte-identical against the original LOG.md lines before the split.
  All 5 collapsed decisions' "answered" summaries cite the same `source:`/history files each
  decision already carried — no new evidence was authored, only relocated pointers.
state_changes: |
  live/indie-game-development/NOW.md — bet.current_truth replaced; 5 decisions collapsed.
  live/indie-game-development/LOG.md — entries before 2026-06-29 removed (archived), one pointer
    fixed.
  live/indie-game-development/history/LOG-archive-indie-game-development.md — created (verbatim
    archive of the removed LOG entries).
  live/indie-game-development/work/now-current-truth-snapshot-2026-07-02.md — created (verbatim
    snapshot of the removed current_truth text).
  live/indie-game-development/LOG.md — one new line appended naming this repair.
captures: []
decisions_needed: []
play_check: |
  1. Name the contradiction — done: NOW.md/LOG.md hot-state hygiene drift (schema-drift fields,
     answered decisions left in place, LOG entries far past the one-line/≤2-sentence rule),
     already diagnosed and rule-fixed in the same-day maintenance session.
  2. Reconstruct — done: read NOW.md/LOG.md in full; cross-checked recoverability of every
     block against history/ and work/ before deciding pointer-collapse vs snapshot-first.
  3. Propose corrected state — done: batched proposal presented to the owner (this chat)
     before any file was written, per-file plan with exact recoverability findings.
  4. Confirm (owner) — done: owner confirmed with "ok" after reviewing the batched proposal
     (current_truth/decisions collapse for NOW.md, archive-only split for both LOG.md files,
     pointer collapse for TREE.md/CHARTER.md).
  5. Friction — done: no new FRICTION.md line needed; this session executes the fix already
     logged there this same day (2026-07-02 entries).
log: 2026-07-02 — repair (hot-state hygiene, s-repair-hotstate-hygiene-001, owner-confirmed): NOW.md current_truth + 5 answered decisions collapsed to pointers (584→393 lines); LOG.md archived pre-2026-06-29 entries verbatim to history/LOG-archive-indie-game-development.md + fixed one broken pointer (273→82 lines). → history/2026-07-02-s-repair-hotstate-hygiene-001.md
next: |
  None — hygiene repair complete for this direction. Ongoing work continues per NOW.next
  (Sc-kernel executor leg, c-exec-023).

END_OF_FILE: live/indie-game-development/history/2026-07-02-s-repair-hotstate-hygiene-001.md
