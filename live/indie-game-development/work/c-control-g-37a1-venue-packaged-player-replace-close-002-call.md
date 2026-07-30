# CALL c-control-g-37a1-venue-packaged-player-replace-close-002

> **RETURNED REPLACED — DO NOT REDISPATCH.** Terminal receipt commit
> `e4eba767898ffee774cfde428094b729f7bf3e81` released the old root and WIN-U3. Direction consumed this HOME and
> activated `c-exec-g-37a1-venue-packaged-player-minimal-002` as the fresh contract-34 PLAN root.

> **READY — PREFLIGHT CONTRACT CORRECTED AFTER GENUINE ESCALATE.** The prior CALL incorrectly required WIN-U3 to be
> `AVAILABLE` even though the old target root lawfully owns it as `CLAIMED / PAIR-CANDIDATE`. It also treated the
> historical published Re-sync commit as the current/future replacement basis. Neither is a valid STOP for the
> target root's own v34 process-close. No product byte changed during the failed attempt.

direction: indie-game-development
track: t-venue
for: t-3
node: g-37a1
to: executor
kind: engineering
repo: C:\projects\Unity\GasCoopGame_win-u3
issued: 2026-07-30 by s-repair-g-37a1-venue-replacement-preflight-correction-001

engineering_contract: 34
control_plane: v34 frozen-authority replacement close
target_root: c-exec-g-37a1-venue-packaged-player-001
target_root_feature_pin: 31
planned_replaced_by: c-exec-g-37a1-venue-packaged-player-minimal-002
slot: WIN-U3
target: Local
budget: одна отдельная control-plane session; никакой feature execution

## dispatch status

**READY under the target root's existing lease.** Fresh read-only preflight on 2026-07-30 found:

- permanent branch `slot/win-u3`, clean local HEAD `9c9a068e3b3223e2de36d50e59f6e83e682feb00`, tree
  `18580f6159ce0f7f5b11b3d6ac38589d4b2b7a6a`;
- `origin/slot/win-u3` remains at historical Re-sync commit
  `bdf4a7aa9a1cc22cd131586ba11c4e87726b30cf`; local is 22 commits ahead. Remote equality is not a preflight
  requirement for this local target-root continuation;
- `validation.config` contains `synced_contract_version: 34`, Git blob
  `f754601e1e127f33b98194eb1876bac4a4698bb9`;
- `refs/backup/pre-v34-cleanup/slot/win-u3` resolves to
  `bdf4a7aa9a1cc22cd131586ba11c4e87726b30cf`;
- the real selector reports `CLAIMED`, lease
  `c-exec-g-37a1-venue-packaged-player-001:PAIR-CANDIDATE`, state CLEAN. Its `availability: STOP` is the correct result
  for a *fresh slot selection* and is expected here: this session continues the exact root named by that lease and
  must neither claim nor steal the slot;
- old root receipt
  `docs/measurements/root-receipts/c-exec-g-37a1-venue-packaged-player-001/01-pair-candidate-r1.json` has Git blob
  `50bab9b54b7f8c1509b8d95653500f1aafb43741`, state `ACTIVE`, stage `PAIR-CANDIDATE`;
- rejection commit `2a66cd10756ae17dff709a85d2e6f499f31e3dd4` resolves; old PLAN/carrier/RED/tests/tools are still present, as
  expected before replacement salvage;
- root-lifecycle scan is GREEN; no replacement receipt, `replaced_by` or `carry`/`stale` has yet been committed.

Re-read every ground against current Git and repo authority before mutation. STOP only if checkout becomes dirty, the
branch/stamp changes incompatibly, the lease no longer names the exact target root, the rejection/receipt identities
do not resolve, or v34 cannot produce a legal clean basis. Do **not** STOP merely because the owned slot is not
`AVAILABLE`, because local HEAD descended beyond the historical Re-sync proof, or because the existing remote branch
lags the clean local checkout.

## goal

Without delivery and without repairing the rejected feature candidate, process-close the old non-released pin-31 root
`c-exec-g-37a1-venue-packaged-player-001` as v34 `REPLACED`, name
`c-exec-g-37a1-venue-packaged-player-minimal-002` as its planned replacement, and return Direction the new clean
committed basis created by the replacement transaction.

The business promise remains unchanged: the owner launches the game by double-clicking a built player, can relaunch
it into the same configured start state, M7 is green and the build can produce a screenshot. This control session does
not implement or re-plan that promise.

## context

- Current Direction authority:
  `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\NOW.md`, task t-3.
- Binding rejection evidence:
  `docs/measurements/c-exec-g-37a1-venue-packaged-player-001-pair-freeze-r1-refutation.json` and
  `docs/reviews/pair-freeze-c-exec-g-37a1-venue-packaged-player-001-r1.md`; verdict
  `PAIR_FREEZE_RETRY_1_REFUTATION_BLOCKED`, eligibility `NOT_ELIGIBLE_FOR_BUILD`.
- Historical Re-sync proof:
  `docs/measurements/c-resync-g-37a1-venue-contract-v34-001-proof.json`. It proves contract installation at its own
  commit; it is not the replacement transaction's future `basis_commit`.
- Rejected live surfaces include old carrier `Assets/GasCoopGame/Editor/PackagedPlayerBuild.cs`,
  `Assets/Tests/EditMode/PackagedPlayer/**`, `tools/packaged-player-evidence-check.ps1`,
  `tools/packaged-player-evidence-check.selftest.ps1` and `tools/verify-packaged-player.ps1`.
- V34 authority is `validation.config`, `tools/root-lifecycle-check.ps1` and `tools/stage-local-check.ps1`. Derive the
  exact predecessor hash and full salvage inventory from them and current Git; explanatory hashes in this CALL are
  grounds, not authority.
- The previous attempt returned genuine `HOME: ESCALATE` before mutation because its CALL required `AVAILABLE` and
  fixed the historical Re-sync commit as basis. Direction accepted that STOP and issued this corrected successor.
- The saved minimal replacement draft in Direction is not launch authority and is not executed in this session.

## boundaries

- Only v34 process-close of the old root. Do not write a new PLAN, production behavior, carrier, RED, tests or feature
  tools; do not run PAIR-CANDIDATE, PAIR-FREEZE, BUILD, VALIDATE, REPORT, Deliver or a game executable.
- Continue only under the exact existing lease
  `c-exec-g-37a1-venue-packaged-player-001:PAIR-CANDIDATE`. Do not request an `AVAILABLE` slot, do not claim another
  lease and do not release the slot except through the terminal replacement receipt required by v34.
- Do not use `bdf4a7aa…` or current `9c9a068e…` as a predeclared replacement `basis_commit`. The basis is the new clean
  committed result of exact salvage/stale removal; the receipt binds it after it exists.
- Preserve old commits, rejection evidence, receipts, manifests and a full `refs/*` history ref. Do not rewrite Git
  history or relabel the old PAIR-CANDIDATE as PASS/delivered.
- The replacement receipt inventories exactly every v34-required frozen path and predecessor stage output. Each entry
  receives a byte-bound `carry` or `stale` disposition and reason. Carried paths remain byte-identical; stale paths are
  absent from the new clean basis and current gate scope.
- No uncommitted draft transfer. The planned replacement id is a pointer only; it is not created here.
- Do not create, delete, move or switch worktrees or branches; no stash/reset/clean/force operations. Normal
  non-force publication/read-back of the existing permanent branch is allowed only if the repo's v34 terminal-close
  procedure requires it, and must occur after the exact replacement commit exists.
- If the exact target lease, receipt graph, rejection identity or salvage inventory cannot pass v34 without weakening
  a check, return one genuine `ESCALATE` with that new blocker.

## done_when

1. Preflight re-proves contract 34, `slot/win-u3`, Target Local, clean checkout and the exact target-root lease. It
   records selector `availability: STOP` as expected for the owned slot and performs no fresh selection/claim.
2. The old root receives a committed replacement receipt with `state: RELEASED`, terminal verdict `REPLACED`, exact
   predecessor hash, old feature pin 31, replacement pin 34 and
   `replaced_by: c-exec-g-37a1-venue-packaged-player-minimal-002`.
3. The receipt binds rejection commit `2a66cd10756ae17dff709a85d2e6f499f31e3dd4`, a resolving preserved full ref,
   `resume_from: PLAN`, and the newly created clean `basis_commit == salvage_commit`.
4. Exact salvage covers all v34-required frozen and predecessor-output paths. Every item appears exactly once in
   `carry` or `stale`; carried bytes are unchanged, stale/superseded paths are absent from basis/HEAD, and old evidence
   remains resolvable through the preserved ref and commits.
5. Replacement-owned root-lifecycle, cleanliness and stage-local replacement checks are GREEN. Receipt flags confirm
   no delivery claim, downstream gates, full suite, feature execution, draft transfer or branch/worktree mutation.
6. The replacement commit is on the existing `slot/win-u3`, checkout is clean, and any repo-required non-force
   publication is read back exactly. Historical remote lag before the transaction is recorded but is not itself a
   failure.
7. Terminal HOME is `REPLACED` with receipt path/hash, old lifecycle/stage/pin, preserved ref, rejection/basis commits,
   complete `carry`/`stale`, changed control-plane paths and confirmation that feature/Deliver did not run. The new
   PLAN is not automatically launched.

## return

Return `HOME: REPLACED` or one genuine `HOME: ESCALATE`. On `REPLACED`, include the committed receipt and its hash,
target-root lifecycle, `replaced_by`, `resume_from`, preserved ref, rejection/salvage/basis commits, exact
`carry`/`stale`, checkout cleanliness, checks run, publication/read-back if required and all changed paths. Explicitly
state that no packaged-player feature stage ran and only Direction may issue the fresh contract-34 PLAN.

END_OF_FILE: live/indie-game-development/work/c-control-g-37a1-venue-packaged-player-replace-close-002-call.md
