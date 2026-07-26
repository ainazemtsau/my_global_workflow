# RESULT s-work-051 — frame c-exec-031 (GasCoopGame §Re-sync v14→v18)

session: s-work-051
direction: indie-game-development
node: g-9c41
play: shape (frame an executor CALL)
for: c-exec-031 (GasCoopGame §Re-sync of the engineering contract v14→v18)

## outcome
Owner asked to frame the §Re-sync leg (previously folded into c-021's own start). Framed **c-exec-031** — a medium
INFRA/run-contract leg that brings GasCoopGame from synced_contract_version 14 to 18 in one pass, so c-exec-021
(Sc-reactions) fires on a current base and is gated by the current review rules. STRICTLY ADDITIVE. CALL =
work/c-exec-031-resync-v15-v18-call.md.

## what it wires (each mechanically, + seeded-miss — not prose)
- v15 review-scope-split → tools/review-check.ps1 (scope+site columns, class-sibling routed-pointer, the
  site-diff-membership anti-dodge, the v14 sweep out-of-diff routed disposition).
- v16 tool-unavailable-STOP → AGENTS.md run-contract (STOP + owner-contact + written-owner-ack; prose, no script).
- v17 source-scan-ban → AGENTS.md rule + the TOOLING-HYGIENE carve-out named explicitly
  (hygiene.ps1 / benchmark-discoverability-check.ps1 / excluded-category-check.ps1 PERMITTED, NOT deleted).
- v18 cited-artifact-existence → tools/result-check.ps1 (the always-run RESULT gate c-exec-030 extracted): every
  leg's cited docs/reviews/review-*.md / docs/adr/*.md path, repo-rooted, must EXIST at HEAD; omitted citation
  untouched; cross-repo/prose/stub out of scope. 4-case independently-authored seeded-miss.
- bump synced_contract_version 14→18.

## key scope decisions folded into the CALL
- ⚠ CROSS-TRACK: the 4 GasVisual/*ScanTests.cs (v17-banned behavior-evidence scanners still on main) are OWNED by
  c-visual-005 (the visual clean re-derive) — c-031 does NOT delete them (a concurrent delete would collide);
  grandfather-pending in validation.config, c-visual-005 removes them + the grandfather entry.
- Contour = the c-024/026/028/030 tooling pattern: NO frozen openspec folder → per-change battery N/A by absence;
  independent RED test-author FIRST + fresh-session G5 + ADR-P-0008.
- Base = GasCoopGame main @bbe86eb (post c-030 merge). Engine worktree GasCoopGame_dev — NEVER dev_2.
- STOP-clauses: touch no Core/sim/visual/dev_2 file; grandfather (never loosen) if a new gate would retro-fail an
  already-delivered leg; a v18 retro-fail of a committed RESULT is grandfathered with owner-ack, not loosened.

## play_check
- shape: DONE — framed the §Re-sync CALL from the CONTRACT_VERSION v15/v16/v17/v18 §Re-sync-owed clauses (verbatim
  mirror), verified the wiring targets exist on product main (review-check.ps1, result-check.ps1, the 4 scan-tests,
  the tooling-hygiene scanners), self-hardened the known traps (v17 scanner classification + cross-track grandfather).
- cut: DF-5 is NOT in this leg (already RESOLVED by c-030); the visual scan-test deletion is NOT in this leg (owned
  by c-visual-005). No G9/TREE change; the g-9c41 bet continues.
- next: fire c-exec-031 in a fresh GasCoopGame_dev session (executor); on GREEN + binding G5 → c-exec-021.

## log
g-9c41 shape/frame — c-exec-031 (GasCoopGame §Re-sync v14→v18: review-scope-split + tool-unavailable-STOP +
source-scan-ban + cited-artifact-existence) FRAMED. Each version mechanically wired + seeded-miss; tooling-hygiene
scanners PERMITTED; the 4 GasVisual/*ScanTests.cs grandfathered-pending-c-visual-005 (cross-track). Contour =
c-024/026/028/030 (no frozen folder); ADR-P-0008; base @bbe86eb. Fires FIRST, then c-exec-021.

## next
Fire c-exec-031 in a FRESH GasCoopGame_dev session (work/c-exec-031-resync-v15-v18-call.md). dev→main merge + push
OWNER-GATED. On GREEN + binding fresh-session G5 → the repo is on v18 → c-exec-021 (Sc-reactions) fires on a clean
base (re-harden + fill §PENDING, fresh owner-present PLAN).

END_OF_FILE: live/indie-game-development/history/2026-07-04-s-work-051-c-exec-031-resync-framed.md
