# CALL c-control-g-37a1-body-first-person-replace-close-001

> **READY FOR DISPATCH — CHARACTER V34 REPLACEMENT CLOSE.** Publication repair is already present in WIN-U2 and
> must not be repeated. This CALL performs only the v34 control-plane close of the old frozen-authority root; it does
> not start a new PLAN, PAIR-CANDIDATE, Character implementation or Deliver stage.

direction: indie-game-development
track: t-body
for: t-2
node: g-37a1
to: executor
kind: engineering
repo: C:\projects\Unity\GasCoopGame_win-u2
issued: 2026-07-30 by s-repair-g-37a1-character-v34-replacement-route-001

engineering_contract: 34
control_plane: v34 frozen-authority replacement close
target_root: c-exec-g-37a1-body-first-person-001
target_root_feature_pin: 31
planned_replaced_by: c-exec-g-37a1-body-first-person-minimal-002
slot: WIN-U2
target: Local
budget: одна отдельная control-plane session; никакой feature execution

## dispatch status

**READY.** Read-only preflight on 2026-07-30 found:

- permanent branch `slot/win-u2`, clean local HEAD `8c84f90fcfd2b2a9d898451bea43560e29018d46`, tree
  `832d3cb0f06937f05dee205bb8954194d38208dc`;
- `validation.config` says `synced_contract_version: 34`, Git blob
  `6e157593bb27c5bb1b971f34c1699c5573a8032e`;
- the selector reports `CLAIMED` with lease
  `c-exec-g-37a1-body-first-person-001:PAIR-CANDIDATE`; this is the target root's own control-plane close, not a new
  slot claim;
- the old receipt chain freezes PLAN blob `346f9b41a62bb2eb43deac927c0b995b82b78da2`, while the owner-approved minimal
  PLAN at freeze commit `420d6f8d05984fbc9f15bc44591e8f9b2b928b69` and current HEAD is blob
  `bdf46175de22dfd78273305026d2a1a7a5ae6c69`;
- the minimal PLAN receipt exists at
  `docs/measurements/root-receipts/c-exec-g-37a1-body-first-person-001/minimal-mvp/00-plan.json`; its current Git blob
  is `4d365611a4e03e6a05374c611ea7bed2695dfe18` and its SHA-256 is
  `914f98cdc5d427d4f7d6d2c6ec45b59f49f30ca657a800d78e8d5aec90edfd62`;
- the immutable failed r2 evidence remains carrier `00012b6877c4512dd6d58303805660b8cffdc731`, RED
  `3cfecc766471bf2913b63784fbd2bcb64ef0988a`, process tip
  `8106170d7bfdd5cad705eeab248285fcd0621339`, with disposition
  `PAIR-FREEZE FAIL / NOT BUILD ELIGIBLE`;
- the last Character-local publication/proof commit before the later workflow merges is
  `98e44b1fa71c0b9c0ac3f5cd332b956bedd9c6e0`. These hashes are preflight grounds, not substitutes for re-deriving
  the exact predecessor, rejection identity and inventory from current repo authority.

The local branch is ahead of `origin/slot/win-u2`; no remote-equality claim is made here. Re-read every precondition
before mutation. If the branch, stamp, lease or receipt graph has changed incompatibly, return `ESCALATE` rather than
guessing.

## goal

Without delivery and without repairing or implementing Character behavior, terminally close the non-released pin-31
root `c-exec-g-37a1-body-first-person-001` as v34 `REPLACED`, preserve its failed and owner-approved history, name
`c-exec-g-37a1-body-first-person-minimal-002` as the planned replacement, and return one clean committed basis from
which Direction may later issue a fresh contract-34 root.

The business promise remains unchanged: a first-person body walks, jumps, falls, lands, stands stably and climbs one
simple cubic ledge by querying the cubic grid directly, with no generated terrain mesh colliders and no first/third
person switch. This control session does not implement or re-plan that promise.

## context

- Current Direction authority:
  `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\NOW.md`, task t-2.
- Frozen owner-approved minimal Character inputs are the exact PLAN/spec/tasks/proposal, decision page and ADR bound by
  `minimal-mvp/00-plan.json`. Their content may inform the later fresh root only through the committed replacement
  receipt and subsequent Direction CALL; this session transfers no draft and creates no new root package.
- The old r2 carrier/RED/manifests/receipt remain evidence of the failed route. They must stay reachable through Git and
  a preserved full ref, while every path disposed `stale` is absent from the clean replacement basis and current gate
  scope.
- V34 authority is `validation.config`, `tools/root-lifecycle-check.ps1` and `tools/stage-local-check.ps1`. The exact
  predecessor receipt, rejection commit, salvage inventory and `carry`/`stale` split are derived from those checks and
  current Git, not from the explanatory hashes above.
- The owner authorized repairing the Character frontier with the exact words:
  `давай  починим что нуно что бы запустить character`.

## boundaries

- Only v34 process-close of the old root. Do not write the new PLAN or new root package; do not run PAIR-CANDIDATE,
  PAIR-FREEZE, BUILD, VALIDATE, REPORT or Deliver; do not launch a game executable.
- Do not repeat the retired `body-plan-publication-unblock` work. PLAN publication tooling is already installed and the
  minimal PLAN receipt already exists.
- Do not edit Character production behavior, gameplay assets, scenes, prefabs, packages or ProjectSettings. Do not
  open Unity Editor or Unity MCP.
- Do not repair, relabel or reinterpret the failed r2 carrier/RED. Preserve the old commits, manifests, receipts and a
  full `refs/*` ref as immutable evidence; no Git history rewrite.
- The replacement receipt must inventory exactly every frozen path and predecessor stage output required by v34. Each
  entry gets a byte-bound `carry` or `stale` disposition and reason. Carried paths remain byte-identical; stale paths
  are absent from the clean basis and current HEAD. A prose claim that files are “non-authority” is insufficient.
- No uncommitted draft transfer. The planned replacement id is a pointer only; it is not created or made runnable here.
- Do not create, delete, move or switch worktrees or branches; no stash/reset/clean/force operations. If a clean
  committed basis cannot be produced within the v34 replacement mechanism, return one genuine `ESCALATE`.
- If the two receipt lineages under the old change id cannot be reconciled into one exact legal predecessor without
  changing frozen identities, stop with the exact receipt/hash conflict. Do not choose a predecessor by recency alone.

## done_when

1. Preflight re-proves directly in WIN-U2: contract 34, permanent branch/Target Local, clean start, exact target lease,
   and a resolvable non-released pin-31 root. Any drift is named.
2. One exact predecessor receipt and one rejection/salvage commit are derived from current v34 authority. The receipt
   records the predecessor hash; the preserved full ref retains its history.
3. A committed root receipt keeps the old root's feature pin 31 and stage, sets lifecycle `state: RELEASED`, terminal
   verdict `REPLACED`, replacement schema `gascoop-root-replacement.v34`, `replacement_pin: 34`, and exact
   `replaced_by: c-exec-g-37a1-body-first-person-minimal-002`.
4. The receipt records `resume_from: PLAN`, clean `basis_commit`, identical `salvage_commit`, `checkout_clean: true`,
   and false values for delivery claim, downstream gates, full suite, draft transfer and branch/worktree mutation.
5. The salvage inventory exactly covers all v34-required frozen and predecessor-output paths. Every item is bound to
   the rejection bytes and appears exactly once in `carry` or `stale`; stale/superseded paths are absent from the clean
   basis/HEAD, while old evidence remains resolvable through the preserved ref and commits.
6. Only replacement-owned lifecycle/cleanliness/replacement checks run and are GREEN. No feature or delivery outcome is
   claimed; Character behavior, the failed r2 meaning and task t-2 remain unchanged.
7. The replacement close and its evidence are committed on `slot/win-u2`; checkout is clean. HOME returns exactly
   `REPLACED` with receipt path/hash, old root stage/pin, preserved ref, rejection/basis commits, complete
   `carry`/`stale` dispositions, changed control-plane paths and confirmation that feature/Deliver did not run.

## return

Return `HOME: REPLACED` or one genuine `HOME: ESCALATE`. On `REPLACED`, include the committed product receipt and its
hash, target-root lifecycle, `replaced_by`, `resume_from`, preserved ref, rejection/salvage/basis commits, exact
`carry`/`stale`, checkout cleanliness, checks run and all changed paths. Explicitly state that the planned replacement
root was not created, no Character feature stage ran, and only Direction may issue the fresh contract-34 PLAN.

END_OF_FILE: live/indie-game-development/work/c-control-g-37a1-body-first-person-replace-close-001-call.md
