# RESULT — s-work-012 (g-9c41 Wave 2): apply c-exec-009 + c-exec-010 (hardening CLOSED) + independently verify the baseline + UNHOLD t-3 (GO on t-3 ∥ t-4)

direction indie-game-development / bet g-9c41 / Wave 2 / play work (apply executor RESULTs + resume the held leg, owner present).

## outcome

- The review-driven CONSOLIDATION+HARDENING leg **t-5 (c-exec-009)** RETURNED + is APPLIED home → **t-5 DONE**. Fix #3 split: Part A (StableId→Core) in c-exec-009; Part B (the TopologyConformance derive-mismatch admission gate) spun out as its own leg **c-exec-010**, which also RETURNED + is closed.
- **Independently re-verified the baseline FIRST-HAND** (workflow wf_a94b5ed9, 4 agents) — did NOT trust the closing RESULT, because the RESULT discloses a concurrent ChatGPT/Codex briefly ran in the same `dev` worktree (then stopped by the owner). Verdict = **CLEAN-GREEN / HONEST-CLOSE / GO**.
- **GO on parallel:** the clean baseline resolves the Core/Field+Replication collision that held t-3 → **t-3 (c-exec-007) UNHELD**. t-3 ∥ t-4 now run in PARALLEL on the clean baseline; parallel-safety re-verified.
- **One genuinely NEW constraint surfaced for t-4/R1 (real Dungeon Architect):** c-exec-010 made `TopologyConformance.Check` an ACTIVE admission gate that REJECTS any document whose volume/portal/surface `StableId != derive(geometry)`. So the real DA reader MUST emit plain logical geometry and route THROUGH `SceneTopologyComposer.Compose` (which derives every id) — a DA-own-id path is now rejected at the Core boundary (silent-pass impossible). This is GOOD (the gate protects the real-DA wiring) but must be an explicit t-4 done_when + RED test.

## evidence (re-derived first-hand on the CLEAN dev tip cb73e82, wf_a94b5ed9 — not cited from the builder RESULT)

- `tools/check.ps1` → core build 0 errors / 0 warnings; headless **402/402** (0 failed, 0 skipped); hygiene OK; "OK: all gates green", exit 0.
- `tools/check.ps1 -Deliver` → GREEN; strong-check enablement all 4 enrolled change-ids over the 70% floor: chunk-apply-before-advance **93.06%**, fielddelta-apply-atomicity **82.5%**, stableid-derivation-in-core **86.67%**, topology-derive-mismatch-gate **90.07%**; spec-silence audits present; deliverable-coverage 12/12/12/7 promises disposed; coverage OK; exit 0. Worktree clean before+after.
- **3 fixes REAL** (independent test-author RED tests + mutation enrollment): #1 FieldDelta.Apply validate-before-mutate (22d548b; `FieldDeltaApplyAtomicityTests`); #2 chunk apply-before-advance (4396ded; `CoarseChunkFollowerApplyAtomicityTests` — hash unchanged after throw AND high-water NOT advanced; RevisionBarrier.TryAccept body untouched, additive non-mutating `WouldAccept` peek only); #3 Part A StableId→Core (a9eecde; `TopologyStableIdsDerivationTests`, formula moved verbatim, adapter `TopologyIds` forwards, no duplication) + Part B conformance gate (300b812; `TopologyConformanceDeriveMismatchTests` with its OWN spec-transcribed FNV oracle).
- **R13/R14 hold:** `grep '^\s*using (UnityEngine|FishNet|Unity\.)'` across `Assets/GasCoopGame/Core/**` = zero matches; the relocated `Core/Field/Coarse/Replication/*` + `TopologyStableIds` + `TopologyConformance` compile engine-free under `core/GasCoopGame.Core.csproj` (0/0). `FishNetChunkChannel : ICoarseChunkLink` is under `Net/` (edge). `.meta` GUIDs preserved on the rename.
- **LOCK byte-identical:** `git diff 8aee8a8..cb73e82` and the full `d17e691^..cb73e82` range touch no codec/barrier/hash mutation-logic — the only codec/barrier file changed is `RevisionBarrier.cs` (additive `WouldAccept` peek; `TryAccept` body unchanged). Host→2-client bit-exact path unchanged (validation/ordering guards only).
- **Honesty:** both legs' closing RESULTs ran a FRESH-SESSION G5 (different model) → COULD-NOT-REFUTE; the 8 G5 assertions re-checked first-hand all TRUE. The 2 owner-gated blockers are correctly NAMED/deferred (NOT self-marked): (i) owner-run Unity compile + PlayMode CoarseVisibleSlice via MCP (edge change under Net/, outside the headless csproj); (ii) real-UDP FishNet deferred (WSAENOBUFS). Concurrent-Codex provenance handled (CloudyCode re-verified; every load-bearing claim corroborated against the committed tree).
- **Minor/cosmetic (non-blocking):** the c-exec-010 RESULT has an editorial "68 vs 59" inconsistency in two headers (the migration broke 59 tests, not 68; the 59 is the honest re-measured number — independently reverted+remeasured 59 failed/343 passed of 402; nothing masked).
- Builder RESULTs live at GasCoopGame_dev @8aee8a8 (c-exec-009 close) and @cb73e82 (c-exec-010 close); dev tip cb73e82, worktree clean. None pushed (owner-gated).

## state_changes

- NOW.md active_bet.phase: appended the 2026-06-19 s-work-012 line (baseline closed + re-verified GREEN; t-3 unheld; the new t-4 DA gate).
- NOW.md active_tasks: **t-5 → done**; **t-3 → active (UNHELD)** carrying the post-consolidation forward-constraints.
- NOW.md open_calls: **c-exec-009 → done**; **added c-exec-010 → done** (full note incl. the t-4 DA forward-constraint); **c-exec-007 → open (UNHELD)** with forward-constraints. (c-exec-008 unchanged — open, continues.)
- NOW.md next: replaced — RUN c-exec-007 (resume) ∥ c-exec-008 (continue) on the clean baseline; parallel-safety + shared-golden flag + 4 residual owner-run items + push owner-gated.
- LOG.md: appended the s-work-012 line.

## captures

- The c-exec-010 "68 vs 59" header inconsistency is editorial only (corrected number is the honest one); flag for the eventual Wave-2 node review, not a defect to act on now.
- NEW shared golden between the two parallel legs = TopologyConformance/TopologyStableIds (the geometry-derive law). Decoupled only while t-4 routes the real DA through SceneTopologyComposer.Compose AND t-3 does not alter TopologyStableIds — either is STOP-and-report.

## decisions_needed

- none — owner asked to start t-3 ∥ t-4; verification = GO; legs handed to run.

## play_check

- "1 Recite — done: restated the held t-3 + the c-exec-009/010 close + the owner's ask (start t-3 ∥ t-4)."
- "2 Owner inputs — engineering apply, not owner-content; owner present (asked to start both: «давай посмотри сможем ли мы вместе стартануть t3 и t4»)."
- "3 Do the work — re-verified the baseline first-hand (wf_a94b5ed9), applied the c-exec-009/010 close, unheld t-3, surfaced the t-4 DA forward-constraint."
- "4 Self-check — every close claim re-derived first-hand on the clean tree (not trusted), given the concurrent-Codex provenance; -Deliver GREEN + G5 corroborated."
- "5 Close — RESULT; next = run c-exec-007 ∥ c-exec-008; review the Wave-2 node when both return."

## log

work (g-9c41/Wave2, s-work-012): applied c-exec-009 + c-exec-010 (hardening t-5 DONE) + independently re-verified the baseline first-hand (wf_a94b5ed9 — CLEAN-GREEN/HONEST/GO, -Deliver 402/402, 4 mutation scores ≥70, R13/R14 + LOCK byte-identical, fresh-session G5 could-not-refute); UNHELD t-3; t-3 ∥ t-4 GO; new t-4 DA-must-route-through-SceneTopologyComposer gate.

## next

RUN **c-exec-007 (t-3, resume in a fresh work session)** ∥ **c-exec-008 (t-4, continue)** on the clean baseline; each opens with a PLAN (owner present). t-4/R1 binds the NEW DA→geometry-derived-id gate (+ a RED derive-mismatch test). When both return → review the Wave-2 node g-9c41. Residual owner-run (both legs, not self-markable): Unity PlayMode CoarseVisibleSlice via MCP; real-UDP FishNet (WSAENOBUFS); t-4 owner-eye LOOK (R3); t-4 guide-loop (R2). Full CALLs → history/s-work-010.md §c-exec-007 / §c-exec-008.

END_OF_FILE: live/indie-game-development/history/s-work-012.md
