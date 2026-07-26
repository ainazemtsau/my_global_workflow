# s-work-023 — work (g-9c41 / S1 → DONE; bet rolls to S2)

Date: 2026-06-28
Play: work
Input: c-exec-015 executor return (builder hand-back) — S1 scope S1a CLOSED + MERGED, 4 open decisions routed home for the direction to scope the next CALL.

## Context

The S1 (forced-flow) executor leg c-exec-015 returned GREEN and merged. The builder delivered
scope S1a (the forced-flow primitive) and explicitly did NOT author the next CALL, routing 4
decisions home: DISPLACEMENT (S1b) go/no-go, CAPACITY/PRESSURE, VELOCITY/momentum-tier, and the
SPARSE active-front solver.

This session (a) recorded the c-exec-015 return; (b) ran an adversarial sequencing check that
surfaced an UNCOMMITTED draft in work/ (gas-arch-reqs-matrix-2026-06-26.md) arguing the locked
input-lockstep integer grid structurally cannot do R7/R12 (50cm-precise reaction / level-spanning
split in a player-absent room, EVERYWHERE) and recommending candidate E (host-state-sync float
clouds, un-signing ADR-0010); (c) VERIFIED that claim first-hand against the committed canon
(knowledge/g9c41-gas-engine-SPEC.md) and the prior cloud-vs-grid analysis — facts hold, and E was
genuinely under-evaluated (the prior rejection only ever covered cross-CPU determinism, never
host-authority), so it was a legitimate open fork, not settled drift; (d) put the pivotal
requirement question + the 4-decision bundle to the owner with a staked recommendation.

OWNER DECISIONS (in-session): the requirement fork → «точно у игрока, грубо везде» (R7/R12-everywhere
is NOT a requirement; the canon AS-LOCKED already delivers deep interaction = coarse events
everywhere + full precision where the player is + 2-3 Ведро-3 rooms) → lockstep STANDS, no ADR-0010
un-lock, matrix archived as non-adopted. The 4-decision bundle → «весь пакет» (accept all).

## RESULT

```RESULT
session: s-work-023
direction: indie-game-development
play: work
node: g-9c41
task: S1

outcome: |
  S1 FORCED-FLOW SLICE CLOSED. c-exec-015 scope S1a (the forced-flow primitive — decaying
  directional-bias impulse-events on the S0 face-flow: jet-emitter w/ lateral confinement +
  ВЫБРОС + ВЕТЕР/fork-split + one-way VALVE + ±1 bias-floor + ledger-honesty + one curated scene
  + class-wide int*int overflow scan) delivered + merged, INSIDE the locked integer model (no
  stored velocity). The architecture FORK raised by an uncommitted draft
  (work/gas-arch-reqs-matrix-2026-06-26.md — "lockstep can't do R7/R12-everywhere -> candidate E
  host-state-sync float clouds, un-sign ADR-0010") was surfaced by an adversarial sequencing
  check, VERIFIED first-hand against the canon (facts hold; the prior cloud-vs-grid analysis only
  ever evaluated clouds on cross-CPU determinism, never host-authority -> E was genuinely
  under-evaluated, not settled drift), and put to the owner as the pivotal requirement question.
  OWNER: «точно у игрока, грубо везде» -> deep interaction = full precision where the player is
  (+2-3 Ведро-3 rooms) + coarse events everywhere, which the canon AS-LOCKED already delivers.
  => lockstep STANDS, no ADR-0010 un-lock, no architecture change; matrix -> archived as
  NON-ADOPTED history. The 4 builder-returned decisions accepted as a bundle. The bet ROLLS to S2.

evidence: |
  - Builder hand-back: origin/main @0adae83 (970 green), tools/check.ps1 -Deliver GREEN on dev;
    fresh-session G5 (Sonnet, different family) COULD-NOT-REFUTE; Codex by-class CLEAN; owner-eye
    «работает». Source RESULT = GasCoopGame/RESULT.md; docs/c-exec-015-spike-findings.md;
    docs/research/capacity-pressure-2026-06-27.md; docs/measurements/c-exec-015-active-set-under-forcing.md.
  - Canon cross-check (first-hand, knowledge/g9c41-gas-engine-SPEC.md): Факт-1 input-lockstep lock
    (line 31; un-lock = owner-signed ADR-0010, line 12); collapse(region) coarse_mass[layer] = a
    position-less integer SUM (line 79); reaction trigger reads coarse totals not fine cells (line
    85); Ведро-3 sub-room-for-all-peers limited to ~2-3 designated rooms (line 90).
  - work/gas-cloud-vs-grid-analysis-2026-06-26.md: every "decisive" cloud-kill is
    cross-CPU-determinism-class (desync / double-claim / checksum) — zero host-authority evaluation;
    confirms candidate E was under-evaluated, validating the surface but mooted by the owner's answer.

state_changes:
  NOW.md:
    - active_tasks.S1.status -> done (evidence above; S1b ВЫДАВЛИВАНИЕ split out + CUT).
    - active_tasks += S2 (active): executor (GasCoopGame) MULTIPLAYER LOCKSTEP LOOPBACK; goal =
      same per-tick MeaningChecksum on 2 PROCESSES (loopback, ONE machine; integer cross-CPU GIVEN);
      determinism BY CONSTRUCTION; needs an executor CALL framed (next).
    - open_calls.c-exec-015.status -> done (evidence).
    - decision_inbox += d-clouds-fork-resolved-001 (fork resolved; lockstep stands; matrix archived;
      CARRY: re-run cloud-vs-grid on host-auth model IF ever reconsidered).
    - decision_inbox += d-displacement-s1b-cut-001 (CUT to backlog; re-entry trigger = first
      body-dams-gas moment; cheap cosmetic-by-canon default if re-entered).
    - decision_inbox += d-pressure-signal-on-demand-001 (read-only signal on-demand; baseline
      back-pressure ALREADY ships — hand-back's "enforcement absent" corrected; cap/compression
      deferred; S5 destructibility seam needs the signal by then).
    - decision_inbox.d-sparse-solver-defer-001 += UPDATE: relabel "deferred-UNVALIDATED" (active set
      near-dense under forcing -> ~100x win in doubt; gating spike's first job = under-forcing bench).
    - decision_inbox.d-gas-richness-tiers-001 += UPDATE: S1a velocity status — TIER-3 reserved,
      trigger ARMED (open-space still ~2:1; «работает» was on confined cubes); re-trigger = one
      honest no-walls open-space jet look at the COMBAT slice = signed evidence for ADR-0010.
    - next -> rewritten (S1 done + fork resolved + S2 framing + 4-decision bundle + carried items).
  work/:
    - move work/gas-arch-reqs-matrix-2026-06-26.md -> work/archive/ with a NOT-ADOPTED banner.
  LOG.md: append one line.
  history/s-work-023.md: full RESULT saved.

captures:
  - VELOCITY re-trigger lands at the COMBAT slice (S6-class): one no-walls confinement-tuned
    open-space jet owner-eye look; if it can't read as a tight jet -> that look is the ADR-0010
    trigger. Carry so the corridor 27x can't silently answer the open-space 2:1 question.
  - IF host-authority is ever reconsidered, work/gas-cloud-vs-grid-analysis must be RE-RUN on the
    host-auth model (its kills are determinism-class, void under single host). On the record.

decisions_needed: []   # all resolved in-session (fork + 4-decision bundle)

play_check:
  - "1 Recite: done — S1 forced-flow goal/done_when restated; executor leg c-exec-015 returned."
  - "2 Owner-inputs: n/a — engineering executor return, not owner-content."
  - "3 Do-the-work: done — applied the c-exec-015 return; verified the architecture-fork claim
     first-hand against the committed canon before surfacing (evidence over claim)."
  - "4 Self-check: done — S1a output matched done_when (forced-flow primitive green + fresh-session
     G5 COULD-NOT-REFUTE + owner-eye «работает»); S1b displacement cut, not a gap."
  - "5 Close (owner): the fork + 4-decision bundle put to the owner with options + a staked
     recommendation; owner = «точно у игрока, грубо везде» + «весь пакет»; next = frame the S2 CALL."

log: "work g-9c41/S1 -> DONE; S2 rolled; clouds-fork resolved (lockstep stands), 4 decisions accepted."

next: |
  CALL (frame the S2 executor leg) — a fresh OS work-session authors c-exec-016 for S2
  (multiplayer lockstep loopback): ingest canon §5 S2 + Факт-1 + the S0/S1 artifacts, classify
  ведро, set boundaries (no stored velocity / no float authoritative path / no re-flux-as-gate =
  STOP-escalate), done_when = 2-process loopback MeaningChecksum byte-identical incl. forced-flow +
  concurrent same-face writes + follower hash parity + zero-float scan + -Deliver GREEN +
  fresh-session G5. Then a fresh GasCoopGame_dev build session opens it with a PLAN (owner present,
  §Re-sync contract FIRST). The fork resolution means S2 hardens the lockstep apparatus deliberately.
```

END_OF_FILE: live/indie-game-development/history/s-work-023.md
