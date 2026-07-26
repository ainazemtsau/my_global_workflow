CALL c-work-grid-v1-launch-control-handoff-001

to: session
direction: indie-game-development
track: grid
play: work
node: g-4b92
task: v1-launch-control-handoff
issued: 2026-07-21 (s-review-grid-v1-executor-plan-001)

goal: |
  Для Grid V1 существует один owner-readable planning-only launch-control handoff, который фиксирует
  законные prerequisites и бинарную admission-границу для возможного будущего G01, пока product root
  и engineering CALL остаются закрыты.

context: |
  Binding review `history/2026-07-21-s-review-grid-v1-executor-plan-001.md` could not refute the
  accepted authority `work/grid-v1-executor-plan.md` against the locally observed clean current product
  snapshot `f6e4f725543514bd67441d4be9ca181392f48c73`. Grid remains parallel and unretired; product progress
  is 0/11. G01 is the future docs-only legacy-fence/authority-supersession leg and has not been issued.

  Current product authority is v31 and current launch/venue/serialization rules outrank historical
  worktree plans. The accepted plan, its binding review receipt, current product refs/contract/registry,
  dependency receipts and exact G01 proof/rollback boundary must all be pinned again at any later start.

boundaries: |
  Owner-present planning/read-only work only. Do not mutate the product repo, allocate or create a slot,
  branch, worktree, root or lease, run Unity/tests/build/benchmark/Deliver, or issue G01, PAIR-CANDIDATE,
  BUILD or any engineering CALL — even after the owner verdict in this session.

  Do not amend the accepted executor plan, weaken current v31 gates, infer venue from historical plans,
  launch G02+, count review as product progress, create Wind/Water placeholders, or retire `g-4b92`.
  A material conflict returns one exact correction position; uncertainty never becomes launch permission.

done_when: |
  1. `work/grid-v1-g01-launch-control-handoff.md` explains in owner-readable language what future G01
     would and would not authorize, and pins the accepted plan plus binding review receipt.
  2. It records the exact later admission checklist: freshly read product refs/v31 contract/registry,
     closed prerequisites, accepted-plan identity, old-CALL non-relaunch, one clean owner-selected venue,
     no competing mutating Core/product-wide docs owner, exact allowed surfaces, proof and rollback.
  3. It preserves G01 as docs-only authority supersession, keeps G02 closed until accepted supersession,
     and states that no historical plan/CALL or dashboard row is launch authority.
  4. The owner receives one binary disposition — `ADMIT LATER G01 PLAN ROOT` or `CORRECTION FIRST` —
     with a recommendation and gives actual words that are recorded without opening engineering work.
  5. Grid remains parallel/unretired at 0/11; no product mutation/root/CALL/test or other Grid leg exists.

return: |
  One launch-control artifact, the owner's exact binary verdict words, surviving blocker if any, and a
  normal Direction RESULT that opens no engineering continuation.

budget: one owner-present planning session
surface: any

END_OF_FILE: live/indie-game-development/work/c-work-grid-v1-launch-control-handoff-001-call.md
