# RESULT — s-repair-now-hygiene-002 (call: owner-plain-2026-06-30-now-strictness)

direction: indie-game-development   play: repair   node/task: g-9c41+g-7e15/NOW-hygiene

## outcome

NOW.md is repaired back to trustworthy hot state after the post-compaction visual-track drift:

- c-visual-003 is now registered in open_calls as the issued visual Wave 1 CALL awaiting RESULT.
- NOW.updated points to this repair.
- history_pointers name the visual re-plan, wave plan, and c-visual-003 CALL.
- NOW.next is now a full CALL packet (`CALL c-frame-021`) for the Sc-reactions framing session, not an anonymous nested prose object.
- work/c-visual-003-call.md no longer carries the stale fixed-hour budget wording.

The stable entrypoint remains NOW.md; no rotation/rename was introduced.

## evidence

- live/indie-game-development/NOW.md: open_calls contains only c-visual-003; decisions contains only the unresolved d-coop-interdependence-repin-001; next begins with `CALL c-frame-021`.
- live/indie-game-development/work/c-visual-003-call.md: budget now says owner-gated cadence with no fixed hour quota.
- live/indie-game-development/LOG.md: repair line appended.
- Source reconstruction used: history/s-visual-010.md, work/c-visual-003-call.md, work/gas-visual-wave-plan-2026-06-29.md, history/s-work-033.md, history/2026-06-30-c-exec-020-sc-weight-result.md.

## state_changes

- NOW.md:
  - set `updated: 2026-06-30 by s-repair-now-hygiene-002`;
  - keep active bet g-9c41 and active task Sc-reactions unchanged;
  - set open_calls to the genuinely awaiting visual CALL c-visual-003 with path work/c-visual-003-call.md;
  - add a history pointer for s-visual-010, gas-visual-wave-plan-2026-06-29.md, and c-visual-003-call.md;
  - replace anonymous `next: CALL:` prose with full `CALL c-frame-021` packet for framing c-exec-021.
- work/c-visual-003-call.md:
  - replace `~40-60 min/day` with owner-gated visual-track cadence and explicit `no fixed hour quota`.
- LOG.md:
  - append: `2026-06-30 — repair (NOW hygiene, s-repair-now-hygiene-002): registered issued visual CALL c-visual-003 in open_calls, refreshed NOW.updated/history pointers, made NOW.next a full CALL c-frame-021 for Sc-reactions framing, and removed fixed-hour wording from work/c-visual-003-call.md.`
- history/:
  - add this RESULT as history/s-repair-now-hygiene-002.md.

## captures

- Maintenance candidate: writer/audit should enforce that any RESULT creating or rewriting a ready/open/issued `work/*call*.md` must do exactly one of: put it in NOW.next if it is the immediate continuation, put it in NOW.open_calls if it is issued/in-flight and awaiting RESULT, or mark it explicitly draft/not-issued.
- Maintenance candidate: any RESULT that writes NOW.md should update the top `updated:` line.
- Maintenance candidate: audit should flag a ready CALL artifact referenced by LOG/history as `next/open` but absent from both NOW.next and NOW.open_calls.
- Maintenance candidate: a lint for stale fixed-hour quota wording should cover current live CALL artifacts after the quota-cleanup repair.

## decisions_needed

[]

## play_check

- 1 Name the contradiction: done — ready c-visual-003 existed in work/history, but NOW.open_calls was empty; NOW.next was not a full CALL packet.
- 2 Reconstruct: done — newest-first through LOG/history/work; s-work-033 closed c-exec-020 and rolled to Sc-reactions; s-visual-010 issued c-visual-003 as visual Wave 1 and awaited a fresh executor RESULT.
- 3 Propose corrected state: done — compact state only; no TREE/CHARTER change; no NOW rotation.
- 4 Confirm: done — owner asked: "давай сделаем этот repair и давай подумаем как мы можем сделать записьв NOW более жесткой".
- 5 Friction: captured for maintenance instead of editing os/** in this live repair session, to keep the repair scoped and avoid mixing OS maintenance with direction state.

## log

repair NOW hygiene: registered c-visual-003, normalized NOW.next, removed stale fixed-hour wording.

## next

CALL c-frame-021
to: session
direction: indie-game-development
play: work
node: g-9c41
task: Sc-reactions
goal: |
  The next CHARACTER-ROAD executor CALL -- c-exec-021 (Sc-reactions: integer
  chemistry between weight-class types) -- is framed + adversarially hardened and
  ready as a self-contained artifact under work/, for a fresh GasCoopGame_dev
  session to open with a PLAN (owner present).
context: |
  live/indie-game-development/NOW.md (Sc-reactions = the active task).
  live/indie-game-development/knowledge/g9c41-gas-engine-SPEC.md (reactions =
  data axes, not N²; Факт-4).
  live/indie-game-development/work/character-road-shape-2026-06-29.md (the road;
  Sc-reactions slice).
  live/indie-game-development/history/2026-06-30-c-exec-020-sc-weight-result.md
  (the Sc-weight substrate it builds on).
  Decision d-coop-interdependence-repin-001: fold co-op interdependence into
  this PLAN as its recommended home.
  GasCoopGame main @61b7923 (base at-or-after; §Re-sync confirms HEAD first).
boundaries: |
  The builder does NOT author this CALL -- the direction frames it. ENGINE-ONLY
  unless the shape says otherwise; do not reopen ADR-0002; renumber the engine
  ADR off the dev2 visual-track number collision at the cross-track merge.
done_when: |
  work/c-exec-021-call.md exists and is hardened: goal = integer reactions
  between weight-class types (telegraph + bang, co-op interdependence pressure),
  per-type DATA not code-branching, determinism preserved, the usual gate
  battery; ready for a fresh GasCoopGame_dev session opening with a PLAN.
return: |
  A hardened c-exec-021 CALL artifact; NOW.next repointed to it.
budget: one framing session (+ an adversarial-hardening workflow).

END_OF_FILE: live/indie-game-development/history/s-repair-now-hygiene-002.md
