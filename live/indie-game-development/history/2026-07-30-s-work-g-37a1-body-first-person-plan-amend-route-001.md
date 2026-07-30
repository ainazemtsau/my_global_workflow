# RESULT s-work-g-37a1-body-first-person-plan-amend-route-001

call: owner direction replacing `c-exec-g-37a1-body-first-person-001`
direction: indie-game-development · track: t-body · play: work · node/task: g-37a1/t-2
date: 2026-07-30

## outcome

The Character root is routed to a new, separate PLAN-AMEND session. The former PAIR-CANDIDATE r2 is left exactly in
`PAIR-FREEZE FAIL / NOT BUILD ELIGIBLE`; it is not repaired and gives no BUILD authority. t-2 remains active.

The successor `c-exec-g-37a1-body-first-person-plan-amend-001` replaces the expanded plan scope with the owner's
minimal first-person MVP: placeholder body, walk, jump/fall/landing, stable grounding, a simple cubic ledge, direct
cubic-grid collision without generated mesh colliders, first person only, and a small position/facing output seam.
Every named exclusion is explicit. The successor permits only documents in its immediate planning session and forbids
opening Unity Editor.

The CALL preserves `engineering_contract: 31` as a same-leg successor and keeps product change_id
`c-exec-g-37a1-body-first-person-001`. Its executable receipt stage is `PLAN`, because the pinned v31 receipt checker
does not recognize a literal `PLAN-AMEND` stage; the separate session job is named PLAN-AMEND. This is the requested
planning reset without falsifying the lifecycle vocabulary or moving the failed r2 chain backward.

## evidence

- Owner's exact ruling in this leg: “Текущий пакет PAIR-CANDIDATE r2 оставить в статусе **PAIR-FREEZE FAIL / NOT BUILD
  ELIGIBLE**. Не продолжать его ремонт и не запускать BUILD.”
- Owner's exact workflow: “PLAN-AMEND → owner approval → fresh PAIR-CANDIDATE (только минимальный carrier и тесты,
  без поведения) → отдельный PAIR-FREEZE review → BUILD только после PASS.”
- Owner's exact planning boundary: “Планирование провести в новой отдельной сессии, только с документами. Unity
  Editor на этой стадии не открывать.”
- Fresh Direction state before apply: t-2 `active`, lane `t-body`, old root CALL
  `c-exec-g-37a1-body-first-person-001` registered as the lane's sole ready root.
- Read-only product snapshot at `C:/projects/Unity/GasCoopGame_win-u2`: branch `slot/win-u2`, clean worktree, HEAD
  `8106170d7bfdd5cad705eeab248285fcd0621339`; r2 carrier `00012b6877c4512dd6d58303805660b8cffdc731`;
  r2 RED `3cfecc766471bf2913b63784fbd2bcb64ef0988a`; r2 receipt
  `docs/measurements/root-receipts/c-exec-g-37a1-body-first-person-001/01-pair-candidate-r2.json`.
- `tools/root-lifecycle-check.ps1` in the pinned product contract recognizes `PLAN`, `PAIR-CANDIDATE`, `PAIR-FREEZE`,
  `BUILD`, `VALIDATE`, `REPORT`, not `PLAN-AMEND`; same-leg successors preserve their pin. Direction contract current
  is 32, so this already-issued lineage is not silently upgraded.
- New self-contained CALL:
  `live/indie-game-development/work/c-exec-g-37a1-body-first-person-plan-amend-001-call.md`.

No Unity process, Editor, MCP action, product write, test, BUILD or network action was performed in this Direction leg.

## state_changes

1. `NOW.md` — `updated` set to 2026-07-30 by this session.
2. `NOW.md.open_calls` — remove the old lane root `c-exec-g-37a1-body-first-person-001`; register
   `c-exec-g-37a1-body-first-person-plan-amend-001` as the sole `ready` root in `t-body`, serving t-2, with the r2
   FAIL/no-BUILD note. Preserve every unrelated lane, call, issue, task, bet and forecast field.
3. Add `work/c-exec-g-37a1-body-first-person-plan-amend-001-call.md` as the complete successor CALL.
4. Prepend one LOG line and save this full RESULT in history.

t-2 remains `active`. No task, track, WIP limit, CHARTER or TREE field changes.

## captures

None.

## decisions_needed

None in Direction. The new PLAN-AMEND session must obtain the owner's exact approval of its artifact before any fresh
PAIR-CANDIDATE starts.

## play_check

1. **Recite** — done: t-2 goal/done_when and active bet g-37a1 were read from fresh state.
2. **Owner inputs (owner)** — done: the owner supplied the exact minimal scope, exclusions, stage order and
   docs-only/no-Unity boundary in this leg; no unanswered Direction choice remains.
3. **Do the work** — done: one same-lane engineering successor was authored; Direction defines outcome/evidence while
   the product PLAN owns technical HOW.
4. **Self-check** — done: all eight owner scope/exclusion groups are represented; r2 remains FAIL; PAIR-CANDIDATE is
   carrier/tests-only; PAIR-FREEZE is separate; BUILD is PASS-gated; immediate session is docs-only.
5. **Close** — done: the old root id is cleared, one successor is registered in the same lane, and unrelated state is
   preserved.

G1: one active bet and one root in t-body remain. G3: appetite is unchanged. G5: neither t-2 nor r2 is marked done or
PASS. G7: no new unresolved Direction decision. G9: CHARTER/TREE untouched. G10: all work steps recorded and the
owner's exact words cited.

## log

По точному указанию владельца PAIR-CANDIDATE r2 оставлен PAIR-FREEZE FAIL / NOT BUILD ELIGIBLE без ремонта и BUILD;
выпущен successor на отдельный docs-only PLAN-AMEND, который срезает Character до минимального first-person MVP и
сохраняет обязательные PAIR-CANDIDATE → PAIR-FREEZE → BUILD gates.

## next

`c-exec-g-37a1-body-first-person-plan-amend-001` — `ready`, track `t-body`, task t-2, slot WIN-U2. Full self-contained
payload: `live/indie-game-development/work/c-exec-g-37a1-body-first-person-plan-amend-001-call.md`.

END_OF_FILE: live/indie-game-development/history/2026-07-30-s-work-g-37a1-body-first-person-plan-amend-route-001.md
