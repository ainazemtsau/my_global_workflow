# CALL c-exec-g-37a1-body-first-person-plan-amend-001


> **RETIRED 2026-07-31 — DO NOT DISPATCH.** The bet `g-37a1` was closed with verdict `obsolete` (the owner changed the game concept). Every CALL issued under it is dead regardless of the status written below. This file is preserved as evidence of what was decided, never as a frontier. The live frontier is `live/indie-game-development/NOW.md`, which currently has `bet: null` and no open calls. See `history/2026-07-31-s-review-g-37a1-obsolete-concept-change-001.md`.

direction: indie-game-development
track: t-body
for: t-2
node: g-37a1
to: executor (engineering same-leg successor, product repo)
kind: engineering
repo: C:\projects\Unity\GasCoopGame_win-u2
issued: 2026-07-30 by s-work-g-37a1-body-first-person-plan-amend-route-001

engineering_contract: 31
stage: PLAN — executable receipt name; the separate session job is PLAN-AMEND
slot: **WIN-U2** — existing worktree `C:\projects\Unity\GasCoopGame_win-u2`, branch `slot/win-u2`, Target **Local**
product change_id: **remains `c-exec-g-37a1-body-first-person-001`**
budget: one fresh docs-only PLAN-AMEND session now; every later product stage is a separate fresh session

## goal

An owner-approved and frozen plan defines the smallest first-person Character MVP that can become the body for t-2,
with the former expanded scope removed. The plan is eligible only for a fresh PAIR-CANDIDATE; it does not claim BUILD
eligibility.

## context

The Direction task remains t-2: the body walks, jumps, falls, lands, stands stably on the ground, and can jump onto a
simple cubic ledge while collision is computed by direct queries against the cubic grid. The current Direction state is
`C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\NOW.md`; the original root CALL is
`live/indie-game-development/work/c-exec-g-37a1-body-first-person-001-call.md`.

The existing product package is
`openspec/changes/c-exec-g-37a1-body-first-person-001/`. Its PAIR-CANDIDATE r2 snapshot ends at slot commit
`8106170d7bfdd5cad705eeab248285fcd0621339`, with carrier commit
`00012b6877c4512dd6d58303805660b8cffdc731`, RED commit
`3cfecc766471bf2913b63784fbd2bcb64ef0988a`, and receipt
`docs/measurements/root-receipts/c-exec-g-37a1-body-first-person-001/01-pair-candidate-r2.json`.

The owner's binding ruling of 2026-07-30 is exact:

- “Текущий пакет PAIR-CANDIDATE r2 оставить в статусе **PAIR-FREEZE FAIL / NOT BUILD ELIGIBLE**.”
- “Не продолжать его ремонт и не запускать BUILD.”
- Replace the former expanded scope with a minimal first-person MVP:
  a capsule or simple placeholder; walking; jump, fall and landing; stable ground standing; jumping onto a simple
  cubic ledge; collision by direct cubic-grid query; no generated mesh colliders; first person only; a simple output
  of position and facing direction for possible future interactions.
- Explicitly outside this MVP: character model and all animation; procedural animation; interaction system;
  player-player collision; network socket/rebase/restart scenarios; final camera and visual polish.
- Required route: PLAN-AMEND → owner approval → fresh PAIR-CANDIDATE containing only the minimal carrier and tests,
  with no behavior → separate PAIR-FREEZE review → BUILD only after PASS.
- Planning runs in a new separate session, changes documents only, and does not open the Unity Editor.

Contract pin 31 has an executable receipt vocabulary of `PLAN → PAIR-CANDIDATE → PAIR-FREEZE → BUILD`; therefore the
fresh root's receipt stage is `PLAN`, while the human/session job is PLAN-AMEND. This successor inherits pin 31 and
does not bundle Re-sync. The old r2 commits, manifests, receipts and FAIL status remain immutable evidence; the new
root starts a new receipt chain for the same product change_id rather than moving the failed chain backward.

## boundaries

- **This immediate session is documents only.** It may amend the current PLAN/proposal/spec/tasks, the Character ADR
  and owner decision page, plus the minimum process receipt/leg documents required to freeze the amended plan.
- Do not open Unity Editor or Unity MCP. Do not import assets, touch scenes/prefabs/project settings, or run an Editor
  as a substitute for planning evidence.
- Do not edit production code, carrier code, tests or test support in PLAN-AMEND. Do not repair, rewrite, re-freeze or
  reuse the r2 carrier/RED pair as launch authority.
- Do not launch PAIR-CANDIDATE or BUILD in this planning session. Owner approval closes the plan session; later stages
  are separate fresh sessions.
- Do not design or reserve the excluded systems. Position/facing output is only a small read seam; it is not an
  interaction framework, network contract, animation system or final camera architecture.
- Do not widen t-2, change the active bet, or touch Direction state from the product repo.
- Preserve the existing package path and change_id unless the product contract proves that impossible; if impossible,
  return one complete ESCALATE instead of inventing a workaround.

## done_when

1. The owner-readable amended plan states one minimal deliverable and maps every included capability: placeholder,
   walk, jump, fall, land, stable grounding, one simple cubic ledge, direct grid collision, first-person-only view, and
   position/facing output.
2. The plan explicitly lists every excluded item from the owner's ruling and contains no acceptance row, fixture,
   socket, carrier member or “future-proofing” obligation for those items.
3. The technical boundary is small and explicit: logical solid/open answers come directly from a cubic-grid query;
   generated terrain mesh colliders are not an authority or fallback; no first/third-person switch exists.
4. The acceptance ledger classifies each retained obligation exactly once as `behavioral-red` or `evidence-only` and
   defines only the minimum fixtures needed to prove the retained MVP. The owner decision page is at most 400 words,
   and every named fixture is fully defined or omitted.
5. The plan freezes the next stage's scope: a fresh PAIR-CANDIDATE may add or correct only the minimal
   non-behavioral carrier plus tests/test-support and mandatory sidecars; it contains no movement/collision behavior.
6. The owner reviews the exact amended artifact and approves it in their own words. Without that verdict, remain in
   PLAN and do not issue or start PAIR-CANDIDATE.
7. The old r2 pair remains recorded as `PAIR-FREEZE FAIL / NOT BUILD ELIGIBLE`; no old carrier/RED byte is repaired and
   no BUILD authority points to it.
8. The frozen plan records the only allowed continuation: fresh PAIR-CANDIDATE → separate binding PAIR-FREEZE
   refutation → BUILD only on PASS. A FAIL returns to planning or stops; it never leaks into BUILD.
9. Product-local docs/plan publication checks required by the pinned contract are green, the diff for this session is
   documentary/process-only, and the session records that Unity Editor was not opened.

## return

Pin 31 remains in force for this lineage. The product root stays registered through its separate fresh stages and
returns HOME only with a gated terminal REPORT or a genuine ESCALATE. The PLAN-AMEND session itself stops after the
owner's exact approval and committed PLAN receipt; it does not continue into PAIR-CANDIDATE in the same session.

Any attempt to preserve the former expanded scope, repair r2, add behavior during PAIR-CANDIDATE, skip the separate
PAIR-FREEZE review, or open BUILD without PASS is a STOP and must be reported, not worked around.

END_OF_FILE: live/indie-game-development/work/c-exec-g-37a1-body-first-person-plan-amend-001-call.md
