# RESULT — s-repair-g-37a1-exec-call-contract-001

play: repair · node: g-37a1 · direction: indie-game-development · date: 2026-07-28

The venue CALL was bounced by the product repository before any change was made. The bounce was
correct: the defect was ours, in four places.

**Protocol note, stated rather than hidden:** this is a second leg in the same physical chat as
`s-shape-g-37a1-core-bet-001`, which normally ends at its commit. It was run here because the defect
is this leg's own, the owner was blocked in front of it, and sending him to a fresh chat to fix our
mistake is precisely the manager overhead he has objected to. Its scope is strictly the four defects
below; nothing else in state was touched.

---

## What was wrong, and why the executor was right

1. **Wrong workspace.** The CALL sent work to `C:\projects\Unity\GasCoopGame_dev`. That is `WIN-CTRL`,
   the integration slot; feature WIP there is forbidden.
2. **No slot.** The product contract requires **the OWNER** to name exactly one of
   `WIN-U1..WIN-U4` in the task message, and explicitly forbids the agent from choosing one — which is
   why the executor asked rather than guessed.
3. **No contract pin.** Every newly issued engineering root CALL carries `engineering_contract: <int>`;
   the current version is **31**.
4. **No entry stage, and an already-satisfied clause.** The CALL asked for «a named scene in Build
   Settings» without naming one, while the allowed start scene is already the only one there.

**Root cause:** the shape leg wrote engineering CALLs without reading the product repository's own
`AGENTS.md`.

## What was established first-hand

- All four slots are free: `tools/select-slot.ps1 -Slot WIN-U<N>` returns `lifecycle: AVAILABLE`,
  `lease: none` for U1, U2, U3 and U4.
- **The live selector contradicts the registry table, and the selector wins.**
  `docs/engineering/WORKTREE_REGISTRY.md` still shows `DRAINING` / `PRESERVED-PAUSED` rows for U2, U3
  and U4. Those are historical row states, not the live lifecycle.
- **A compiled product leg is a five-stage ladder, not one chat:** PLAN → PAIR-CANDIDATE → binding
  fresh PAIR-FREEZE refutation → BUILD → mutation/NegativeControl/property/review/Deliver/G5 gates →
  report. Direction issues ONE root CALL; the product repo carries the leg through the ladder itself
  and returns only a terminal REPORT or a genuine ESCALATE.

## What the executor got right beyond the contract

It narrowed the work. With the allowed start scene already the only one in Build Settings, the scene
clause was already satisfied, so the leg shrinks to what is genuinely missing: the build script and the
packaged player. That narrowing is adopted.

---

```
RESULT
session: s-repair-g-37a1-exec-call-contract-001
play: repair
node: g-37a1
outcome: checkpoint=false; three executor CALLs repaired against the product's engineering contract; no requirement, task, lane, appetite or kill_by changed

evidence:
  - executor bounce (product session, 2026-07-28): "CALL остановлен до любых изменений: он противоречит локальному контракту репозитория" — four cited defects, zero changes, dev clean at 1a6373b84b6bf4da95a24efc3015e23b9ba5d419
  - C:\projects\Unity\GasCoopGame_dev\AGENTS.md — owner-direct slot rule (owner names exactly one of WIN-U1..WIN-U4; the agent must ask and never choose), WIN-CTRL is integration-only, four permanent slots pinned to slot/win-u1..u4 with Target Local, no fifth slot, tools/select-slot.ps1 as the read-only availability check with non-available or branch-mismatch = STOP
  - same file — contract v29/v31: every newly issued engineering root CALL carries an integer engineering_contract pin, successors inherit it; cycle for a newly pinned compiled leg is PLAN -> PAIR-CANDIDATE -> PAIR-FREEZE -> BUILD -> gates -> report; a v30/v31 pinned root records stage receipts on the product side and only its terminal REPORT or genuine ESCALATE returns to Direction
  - live read-only selector, 2026-07-28: WIN-U1, WIN-U2, WIN-U3, WIN-U4 all "lifecycle: AVAILABLE", "lease: none" — contradicting the older DRAINING / PRESERVED-PAUSED rows still present in docs/engineering/WORKTREE_REGISTRY.md

state_changes:
  work/c-exec-g-37a1-venue-packaged-player-001-call.md:
    - slot WIN-U1 named with its path, branch and Target Local, plus the pre-flight selector re-check and the STOP condition
    - engineering_contract: 31 and stage: PLAN added; the ladder and the return rule stated
    - GasCoopGame_dev removed as the workspace and named explicitly as forbidden for feature work
    - done_when clause 1 (a named scene in Build Settings) DROPPED as already satisfied; the leg narrowed to the build script and the packaged player; the remaining clauses renumbered
    - a "what was fixed" section added so the next reader sees the defect rather than repeating it
  work/c-exec-g-37a1-body-first-person-001-call.md: same contract header with slot WIN-U2, applied before it could bounce; workspace corrected
  work/c-exec-g-37a1-coop-two-machines-001-call.md: same contract header; slot deliberately left unchosen, to be picked by the owner from the free slots at unblock time
  NOW.md:
    - updated: by s-repair-g-37a1-exec-call-contract-001
    - open_calls notes for the venue, body and co-op calls record the bounce, the fix and the narrowing
    - issues: i-direction-to-product-call-contract-001 added
  LOG.md: one line appended
  history/2026-07-28-s-repair-g-37a1-exec-call-contract-001.md: this file

captures:
  - docs/engineering/WORKTREE_REGISTRY.md rows for WIN-U2/U3/U4 read DRAINING or PRESERVED-PAUSED while the live selector reports all four AVAILABLE. Product-side hygiene, not a Direction issue; worth a product maintenance leg so nobody reads the table as authority.
  - If a corrected root CALL bounces a second time, the fix stops being clerical: the route becomes an OS maintenance leg for a cross-repo CALL checklist rather than another hand-patched CALL.

decisions_needed: []

play_check:
  scope: exactly the four bounced defects plus the identical defect in the two sibling executor CALLs; no requirement line, criterion, task, lane, appetite, kill_by, forecast or owner ruling touched
  slot_authority: the OWNER names the slot per the product contract; this leg RECOMMENDS WIN-U1 for the venue and WIN-U2 for the body, both verified free, and the owner's pasted message carries the name
  G1: the bet, its five tasks and the WIP limit of 5 are unchanged
  G5: nothing is marked done; the venue call returns to `ready` with a corrected packet
  protocol: second leg in one physical chat, declared above rather than hidden; the alternative was to send the owner to a fresh chat to fix our own defect

log: the venue CALL was bounced and the bounce was right - four contract defects, all ours, and all three executor CALLs are repaired

next: c-exec-g-37a1-venue-packaged-player-001 (slot WIN-U1) and c-exec-g-37a1-body-first-person-001 (slot WIN-U2) are dispatchable again; c-work-g-37a1-topology-boundary-001 and c-work-g-37a1-render-backend-decision-001 were never affected
```

END_OF_FILE: live/indie-game-development/history/2026-07-28-s-repair-g-37a1-exec-call-contract-001.md
