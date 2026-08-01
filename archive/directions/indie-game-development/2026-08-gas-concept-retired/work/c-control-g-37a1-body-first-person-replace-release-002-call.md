# CALL c-control-g-37a1-body-first-person-replace-release-002

> **READY — PHYSICAL LEASE RELEASE ONLY.** The v34 replacement-close itself is already committed and must not be
> repeated. The owner closed the WIN-U2 Unity Editor; Direction then confirmed that PID 31516 and both Unity lock
> evidence paths are absent. This continuation performs only the exact selector release and readback.

direction: indie-game-development
track: t-body
for: t-2
node: g-37a1
to: executor
kind: engineering
repo: C:\projects\Unity\GasCoopGame_win-u2
issued: 2026-07-30 by s-repair-g-37a1-character-replacement-release-001

engineering_contract: 34
control_plane: v34 replacement physical-slot release continuation
target_root: c-exec-g-37a1-body-first-person-001
target_root_feature_pin: 31
planned_replaced_by: c-exec-g-37a1-body-first-person-minimal-002
slot: WIN-U2
target: Local
budget: one short control-only session; no product commit or feature work

## goal

Release the exact physical WIN-U2 lease still held by the already replaced Character root and prove by selector
readback that the slot is `AVAILABLE / none`, without repeating or changing any part of the committed replacement.

The Character business promise remains unchanged: the later fresh root will implement a first-person body that walks,
jumps, falls, lands, stands stably and climbs one simple cubic ledge by querying the cubic grid directly, with no
generated terrain mesh colliders and no first/third-person switch. This continuation implements none of that behavior.

## context

- The previous CALL returned `HOME: ESCALATE` only at terminal physical release. Its repository close succeeded:
  root `RELEASED / REPLACED`, old stage `PAIR-CANDIDATE`, feature pin 31, replacement pointer
  `c-exec-g-37a1-body-first-person-minimal-002`, `resume_from: PLAN`.
- Current clean permanent checkout is `slot/win-u2@c936211913907da8d45b4062ef81e000017d80e4`.
- Committed replacement receipt:
  `docs/measurements/root-receipts/c-exec-g-37a1-body-first-person-001/02-replaced.json`, SHA-256
  `7a759a969f58a210174ffe10fc80f658837b18b54074ad07e1674e5647b3319a`.
- Committed stage proof:
  `docs/measurements/stage-local-receipts/c-exec-g-37a1-body-first-person-001/00-replacement.json`, SHA-256
  `7fe00cbe9cc93fad1d761bb94e45ddaca85aa2748d9e369f2d52f998249c1074`.
- Receipt binds rejection `98e44b1fa71c0b9c0ac3f5cd332b956bedd9c6e0`, basis/salvage
  `993cb3494e8dae01785f601da331a170fbdd4ab8`, preserved ref
  `refs/gascoop-preserved/roots/c-exec-g-37a1-body-first-person-001/pre-replacement`, empty `carry`, and the exact
  17-path `stale` inventory. Every stale path is absent at HEAD and retained through the preserved ref.
- Fresh Direction-side verification after the owner's exact words `закрыл что дальше по character?` found Unity PID
  31516 absent, `Temp/UnityLockfile` absent and `Library/EditorInstance.json` absent. Git is clean.
- The read-only selector still correctly reports `CLAIMED`, lease
  `c-exec-g-37a1-body-first-person-001:PAIR-CANDIDATE`, endpoint `http://localhost:27497/p/39a0fb86`, and
  `availability: STOP`. That is the live custody to release, not evidence that replacement-close must rerun.

Re-read every ground from current Git and machine-local selector state before the one mutation. If Unity or either
lock path reappears, Git is no longer clean/on the permanent branch and committed HEAD, the receipt changes, or the
exact lease no longer matches, return one new `HOME: ESCALATE` without mutation.

## boundaries

- Do not rerun replacement salvage, rewrite either receipt, create another replacement commit, or modify any tracked
  or untracked product file.
- Do not create the planned replacement root or write its PLAN. Do not run PAIR-CANDIDATE, PAIR-FREEZE, BUILD,
  VALIDATE, REPORT, Deliver, the full suite, Unity, MCP, a game executable, or any Character feature stage.
- Do not delete lock files, kill a process, or manually edit the shared slot-state JSON. If Unity evidence is present,
  stop; do not work around it.
- Do not create, delete, move or switch worktrees or branches; no commit, push, fetch, merge, stash, reset, clean or
  force operation.
- The only authorized mutation is the selector's atomic transition for the exact existing lease:
  `.\pwsh.cmd tools\select-slot.ps1 -Slot WIN-U2 -Release -LeaseId c-exec-g-37a1-body-first-person-001:PAIR-CANDIDATE`.
  Immediately follow it with read-only `.\pwsh.cmd tools\select-slot.ps1 -Slot WIN-U2`.

## done_when

1. Fresh preflight proves the exact committed replacement receipt and stage proof unchanged, branch
   `slot/win-u2`, HEAD `c936211913907da8d45b4062ef81e000017d80e4`, clean checkout, no live Unity process for this
   checkout and neither Unity lock evidence path.
2. The live selector still names exactly `WIN-U2`, lifecycle `CLAIMED`, and lease
   `c-exec-g-37a1-body-first-person-001:PAIR-CANDIDATE` immediately before release.
3. The exact selector `-Release` transition succeeds once; no repository byte or Git ref changes.
4. Immediate read-only selector readback returns `lifecycle: AVAILABLE`, `lease: none`,
   `mcp-endpoint: unrecorded`, clean state and `availability: AVAILABLE` on the permanent branch.
5. Terminal HOME is `REPLACED` and records the unchanged replacement receipt/hash and HEAD, the release command,
   before/after selector values, clean checkout, zero changed product paths and confirmation that replacement-close,
   PLAN, feature, Unity/MCP, BUILD and Deliver did not run.

## return

Return `HOME: REPLACED` after exact `AVAILABLE / none` readback, or one genuine `HOME: ESCALATE` if a fresh blocker
appears. On success include the receipt path/hash, unchanged HEAD, exact lease released, selector before/after,
checkout cleanliness and zero changed product paths. State explicitly that the fresh Character root was not created;
only Direction may issue its contract-34 PLAN.

END_OF_FILE: live/indie-game-development/work/c-control-g-37a1-body-first-person-replace-release-002-call.md
