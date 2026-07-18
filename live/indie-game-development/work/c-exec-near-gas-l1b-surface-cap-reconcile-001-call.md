# CALL c-exec-near-gas-l1b-surface-cap-reconcile-001

to: executor
direction: indie-game-development
track: core
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: L1B-Capture
issued: 2026-07-18 (s-work-near-gas-l1b-surface-cap-stop-001)

goal: |
  NearGas L1B carrier chain имеет один binding authority-backed freeze-parent/cap basis и однозначный
  disposition для `de1cc87c5f2e6eb7018571e65d7e95691044c8e9`, не выдающий over-cap surface за RED-eligible.

context: |
  Owning frozen product change ID remains `c-exec-near-gas-l1b-plan-001`. Stable Direction stage/call ID for
  this reconciliation is `c-exec-near-gas-l1b-surface-cap-reconcile-001`; do not create an alias or mutate the
  frozen OpenSpec change. This is a read-only authority/evidence reconciliation, not PLAN, SURFACE, RED or BUILD.

  Completed SURFACE-REFREEZE thread `019f7463-8e65-7fe3-98c9-458429bad2eb` produced published carrier
  `de1cc87c5f2e6eb7018571e65d7e95691044c8e9` with sole parent
  `787cd52534e4a6878be1f16b16cda8bb685ae23c`. Its immediate-parent manifest is exactly
  `Assets/GasCoopGame/Core/Field/NearGas/NearGasSimulation.cs`, +28/-6; Git blob
  `b7962e751d250d0c1c6bf5d0050fb1e8e7d186c1`, SHA-256
  `04FF0C4F5557DA3A57ACEB32BCE38485468116EBE4B708B299A30020C9D66A87`. Boundary build GREEN,
  baseline 1793/1793 GREEN, hygiene GREEN, independent diff review PASS. Immutable prior RED
  `0d0cea14f47cc28d29919e5cf4404da3b5b15836` remains preserved but invalidated by the carrier change.

  Cap conflict is binding STOP evidence. Immediate correction-parent diff `787cd525..de1cc87c` is +28/-6 and
  was declared <=400. Direction's existing Surface authority instead records original cumulative freeze parent
  `409ef4a7cf661fd5639a74364b7cd0469a673031`. Exact Git numstat `409ef4a7..de1cc87c` is:
  `NearGasSimulation.cs` +417/-3; `VoxelField.Reactions.cs` +37/-6; `VoxelField.cs` +105/-1; total added
  production-source lines = 559, which exceeds 400 by 159. Even `409ef4a7..787cd525` already has 537 additions.
  Therefore `de1cc87c` is not RED-eligible until authority resolves whether `freeze-parent` is the immediate
  correction parent or the original cumulative carrier parent. No count or convenience may silently choose one.

  Current canonical product owner-direct protocol was introduced at product `dev` commit
  `e9d6bfd5` and supersedes stale routing assumptions: explicit owner slot selection is launch authority;
  registry is descriptive; Direction pins no path, branch, checkout, switch, creation or publication action.
  The completed Surface session's unauthorized branch action is not precedent. Owner restored WIN-U3 to its prior
  current branch at exact RED `0d0cea14`, clean, while `de1cc87c` remains preserved locally/remotely. Treat those
  facts as evidence only; do not mutate or re-route any product workspace in this leg.

  launch:
    lane: A / NearGas core, read-only authority reconciliation
    venue: owner-selected product slot/task only; Direction pins no path, branch, checkout or ref action
    machine: PC
    base: Git objects 409ef4a7, 787cd525, de1cc87c and 0d0cea14 are evidence, never checkout instructions
    conflict_surface: none; product tree and refs are read-only
    depends_on: completed Surface artifact plus the immediate-vs-cumulative cap contradiction above
    merge_queue: n/a — no product mutation, commit, merge or push
    gates: current owner-direct protocol at e9d6bfd5; registry descriptive, explicit owner slot selection authoritative

boundaries: |
  Product repository, refs, worktrees, branches, registry, code, tests, test support, frozen PLAN/spec/tasks,
  decision page, ADR, RESULT/review files and dashboards are read-only. Do not create or switch a branch; do not
  checkout, reset, stash, clean, rebase, commit, merge, push, reserve, backfill or edit anything. Do not run a new
  SURFACE, RED/RED-REFREEZE, BUILD, mutation, G5, Deliver or product gate; ordinary read-only Git object inspection
  is the only product action. Do not reinterpret the 400-line rule by preference, reuse the 28-line immediate diff
  as proof of the cumulative rule, or reduce/split code in this leg. No Direction task/status close or L1B delivery.

done_when: |
  1. Fresh canonical product authority at/after `e9d6bfd5`, the frozen L1B PLAN/decision authority and the existing
     Direction Surface evidence each have their exact relevant freeze-parent/cap clauses cited with precedence;
     owner-direct launch/registry semantics are reported without any branch or workspace mutation.
  2. Git readback independently confirms parents, manifests and per-file numstat for `409ef4a7..787cd525`,
     `787cd525..de1cc87c` and `409ef4a7..de1cc87c`, including totals 537, 28 and 559 added production lines or
     reports an exact identity mismatch. Prior RED `0d0cea14` preservation is read-only evidence, not eligibility.
  3. The handback distinguishes the two competing meanings of `freeze-parent`, names the binding authority and
     precedence if one is mechanically resolvable, and gives one exact disposition for `de1cc87c`: cap-MET evidence
     eligible for a later Direction decision, cumulative over-cap STOP requiring a new reduction/split route, or
     unresolved authority conflict requiring an owner decision brief with 2–3 options and a recommendation.
  4. No RED-REFREEZE or duplicate SURFACE is opened, no product/ref/worktree mutation occurs, and the handback does
     not claim `de1cc87c` RED-eligible while the 559-vs-400 conflict remains unresolved.
  5. HOME returns exact sources/clauses, Git commands and outputs, arithmetic, owner-direct protocol disposition,
     every done_when disposition, preserved cuts and the one lawful next-stage class or blocker; it authors no
     successor CALL and makes no BUILD, G5, Deliver or L1B completion claim.

return: |
  Product CAP-BASIS RECONCILIATION RESULT HOME: status; stable IDs; exact canonical authority clauses and
  precedence; owner-direct/registry/branch-action disposition; exact parents/manifests/numstat and 537/28/559
  arithmetic; disposition of `de1cc87c` and preserved invalidated RED `0d0cea14`; every done_when disposition;
  cuts and unrelated-work preservation; exact eligible next-stage class, owner decision brief or blocker.
  No product mutation and no successor CALL.

budget: one focused read-only session; stop immediately on unreadable authority or Git identity mismatch
surface: product-repo Codex session

END_OF_FILE: live/indie-game-development/work/c-exec-near-gas-l1b-surface-cap-reconcile-001-call.md
