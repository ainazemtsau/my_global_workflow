# RESULT s-work-049 — cancel the visual-split, frame the GasCoopGame merge-safety leg

session: s-work-049
direction: indie-game-development
node: g-9c41
play: shape (re-scope an approach + frame an executor CALL)

## outcome
Owner reframed: `indie-game-development` is the general UMBRELLA direction (business + this game, and — in
theory — future games), so splitting the visual facet into its own PEER direction is redundant/wrong. Decision:
**the gas-visual direction split is CANCELLED.** g-7e15 stays a parallel track under the umbrella. The collision
pain is handled WITHOUT the split — OS side by the concurrency-hygiene rule already shipped (@c3a7002), product
side by a new small leg. The owner's ORIGINAL primary pain was product-repo MERGE CONFLICTS in GasCoopGame
(RESULT.md etc.), which I had not addressed (I had fixed the OS-side collision + proposed the split). That is now
framed as **c-exec-030**.

## what changed
- Migration runbook `work/gas-visual-split-migration-plan.md` → **SHELVED** (banner at top; reference only, do
  NOT execute). Kept in case a genuine direction split is ever needed (a real 2nd game).
- **c-exec-030 FRAMED** (`work/c-exec-030-result-per-leg-and-df5-call.md`) — a small GasCoopGame INFRA leg:
  (1) RESULT.md → per-leg file (parallel dev/dev_2 legs stop colliding — witness f43aa39 "Fix parallel-leg
  collisions … consolidated RESULT"; + append-only ledgers merge=union + an ADR-number convention);
  (2) DF-5 (P1 gate-integrity) — check.ps1 -Deliver sees STAGED changes (closes the review-evidence bypass).
  Batched (owner "можно заодно") — both are check.ps1/deliver tooling. ADDITIVE, no gate weakened.
- NOW.md: open_calls += c-exec-030; `next` carries the VISUAL-SPLIT-CANCELLED note + the parallel-safety plan;
  DF-5 folded into c-exec-030. updated → s-work-049.

## evidence / root cause (GasCoopGame, read directly)
Single root RESULT.md (~13.6 KB) REWRITTEN by every leg → parallel legs conflict + manual "consolidate".
Git witnesses on main: f43aa39 "Fix parallel-leg collisions on dev … consolidated RESULT"; e0e4f5a "… RESULT
consolidated"; f43aa39 "renumber throw-atomicity ADR-E-0004->0005" (shared ADR-number counter). check.ps1 reads
RESULT.md for the deliver field-gate. DF-5: check.ps1:64 (git diff-files only, ignores staged) + review-check.ps1:90
(Reviewed-commit..HEAD only). `.gitattributes` has no markdown merge driver.

## concurrency note
Reconciled against heavy same-direction concurrency: a parallel session merged DF-10 (c-exec-029) to GasCoopGame
main (db8576f, @f926958) while this session ran; NOW.md moved twice mid-edit. Took the next free ids (session
s-work-049, CALL c-exec-030) and re-applied on the fresh committed NOW. This is the residual shared-NOW friction
the (rejected) split would have removed — accepted, handled by hygiene + re-sync.

## play_check
- reframe/judge-independently: DONE — owner umbrella framing → split redundant; the OS's native parallelism is separate directions, but a facet of one game is not a peer, and the cheap fixes suffice (MAINTENANCE "extract the problem, judge the mechanism").
- cancel: DONE — runbook shelved (not executed; no live/** split applied, so nothing to unwind).
- frame: DONE — c-exec-030 CALL written + recorded in open_calls (goal outcome, boundaries, done_when, return).
- close: this RESULT.

## log
g-9c41: visual-split CANCELLED (owner — indie-game-development stays the umbrella); framed c-exec-030 (GasCoopGame RESULT-per-leg + DF-5, small infra leg) to kill product-repo merge conflicts; runbook shelved; next = c-exec-030 then c-021.

## next
Fire c-exec-030 in a fresh GasCoopGame_dev session (small infra leg) BEFORE c-021 and c-visual-005 run
concurrently — it clears the parallel-leg merge conflicts + closes DF-5. Then the engine road resumes at c-021
(§Re-sync owes v15/v16/v17). dev→main merges owner-gated.

END_OF_FILE: live/indie-game-development/history/2026-07-04-s-work-049-cancel-visual-split-frame-c-exec-030.md
