# RESULT — s-visual-013 (work, g-7e15 / c-visual-006) — 2026-07-06

Checkpoint the product merge/push for c-visual-006 without closing the Direction-OS open_call.

## outcome

GasCoopGame c-visual-006 is integrated to product `origin/main`: merge `c21c6bd` brings `dev2 @866544f`
(`38dd61f` + `866544f`) into `main`, and integration gate-fix `d4c4b35` sits on top so the merged main tip
passes `-Deliver`. This is a product-integration checkpoint, not a Direction-OS close: c-visual-006 remains in
`NOW.open_calls` pending a valid OS close/review with the required binding close evidence.

## evidence

- Product git: `origin/main` and `git ls-remote origin refs/heads/main` both resolve to
  `d4c4b351a97e66e1201716f163b7b842221c3393`.
- Product history: `d4c4b35` -> `c21c6bd`; `c21c6bd` parents are `0dd823b` and `866544f`; `866544f` is an ancestor of
  the pushed tip.
- Product verification on `d4c4b35`: `.\pwsh.cmd tools/check.ps1 -Deliver` -> PASS (core build, 1335 headless tests,
  hygiene/scans, per-leg RESULT gate, negative controls, review/coverage self-tests, final "OK: all gates green").
- Product evidence files exist in the checkout: `docs/results/c-visual-006.md` and
  `docs/measurements/c-visual-006-depthfix-gameview-wall-locked.png`,
  `docs/measurements/c-visual-006-depthfix-gameview-room.png`,
  `docs/measurements/c-visual-006-depthfix-gameview-high.png`.
- During merge-tip verification, `-Deliver` initially failed on pre-existing main doc wording in
  `docs/results/c-visual-005.md` (`MERGED to main` did not satisfy the product result-status gate). I made the
  minimal product docs-only fix `d4c4b35` preserving the merge note inside the gate-compatible
  `DELIVERED on \`dev\` (...)` status line, then re-ran `-Deliver` green and pushed.
- OS apply hygiene: before writing this checkpoint, rebased the local Direction-OS worktree over `origin/main @4f26136`
  (contract v19). The only conflict was append-only `os/FRICTION.md`; both independent 2026-07-06 entries were kept.

## state_changes

- `NOW.md`: `updated` -> `2026-07-06 by s-visual-013`.
- `NOW.md open_calls[c-visual-006].note`: replaced the FIRE-READY text with a PRODUCT MERGE/PUSH CHECKPOINT:
  product `origin/main @d4c4b35`, merge `c21c6bd` contains `dev2 @866544f`, `-Deliver` PASS on merge-tip, artifacts
  present, and `OPEN_CALL STAYS PENDING`.
- `NOW.md parallel_tracks[g-7e15].state`: records Stage 2 product merge/push checkpointed but not Direction-OS-closed.
- `NOW.md next`: keeps the c-exec-021 continuation as the active next CALL and notes that the parallel visual track is
  product-merged/pushed but still pending close evidence.
- `LOG.md`: appended the s-visual-013 checkpoint line.
- `history/`: added this file.
- No `TREE.md` / `CHARTER.md` change. No task marked done. No open_call cleared.

## captures

- Product result-status gate is brittle to post-merge wording: "MERGED to main" is human-true but gate-red; the safe
  wording is `DELIVERED on \`dev\` (merged to main ...)`.

## decisions_needed

None.

## play_check (play: work)

1. Recite — DONE: opening contract restated c-visual-006 as a product integration/checkpoint job, not an OS close.
2. Owner inputs (owner) — DONE: owner input was "c-visual-006 формально закрыт на dev2" and "Прошу direction OS проверить, смержить `dev2` в `main` и запушить."
3. Do the work — DONE: verified product git, found merge already present on `origin/main`, fixed the merge-tip deliver blocker, reran `-Deliver` green, pushed `origin/main @d4c4b35`, and restored the product checkout to `dev2`.
4. Self-check — DONE: checked pushed remote SHA, merge ancestry, artifact existence, product worktree cleanliness, and the Direction-OS guard; c-visual-006 remains in `open_calls`.
5. Close — DONE: this checkpoint RESULT; no task-done/review transition because the required Direction-OS close evidence is not present in this session.

## log

s-visual-013 (2026-07-06) — work/checkpoint (g-7e15/c-visual-006): verified GasCoopGame origin/main carries c-visual-006 via merge c21c6bd (parents 0dd823b + 866544f) plus integration gate-fix d4c4b35; pushed origin/main to d4c4b35; ran `.\pwsh.cmd tools/check.ps1 -Deliver` on d4c4b35 -> PASS (1335 headless, gates green). Direction-OS close intentionally NOT applied: c-visual-006 stays in open_calls pending a valid OS close/review with binding close evidence; builder handback/product gates/merge are evidence input only.

## next

CALL: `work/c-exec-021-continuation-call.md` remains the active next CALL for the engine track. Parallel visual
c-visual-006 is product-merged/pushed but remains pending a valid OS close/review with binding close evidence.

END_OF_FILE: live/indie-game-development/history/2026-07-06-s-visual-013-c-visual-006-product-merge-checkpoint.md
