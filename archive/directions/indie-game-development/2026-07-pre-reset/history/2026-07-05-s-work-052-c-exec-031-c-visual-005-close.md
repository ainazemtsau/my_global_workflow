# RESULT s-work-052 — c-exec-031 (contract v15→v18 §Re-sync) + c-visual-005 (visual source-scan retirement): binding G5 close + merge

session: s-work-052
direction: indie-game-development
node: g-9c41 (+ g-7e15 for c-visual-005)
play: review (verify + close two delivered legs; merge; roll state)
for: c-exec-031 + c-visual-005

## outcome
Both delivered legs VERIFIED by binding fresh-session G5 and MERGED to GasCoopGame main; the infra runway to
c-exec-021 (Sc-reactions) is now CLEAR (repo on contract v18, source-scanners retired).
- c-exec-031 (§Re-sync v14→v18): MERGED @21f9c0f + PUSHED. synced_contract_version = 18.
- c-visual-005 (clean visual source-scan retirement): MERGED @26dd062 + PUSHED. Product origin/main = 26dd062.

## c-exec-031 — binding G5 SOUND (after a REV-2 fail-closed P1 fix)
Read GasCoopGame_dev @5486bd7 (round 1) then @13d48d1 (REV 2). 5-lens adversarial fan-out (wf_1b1d5d16-85e) + both
new self-tests run FIRST-HAND.
- v18 cited-artifact-existence (result-check.ps1), v16/v17 doctrine (AGENTS.md + tooling-hygiene carve-out named),
  additive/no-weaken, grandfather note, boundaries (ZERO Core) — ALL SOUND round 1.
- v15 review-scope-split (review-check.ps1) — ROUND 1 caught a real **P1 false-green in the anti-dodge**: the
  site→file regex stripped only one trailing `:<digits>`, so a class-sibling whose site was spelled `file:line:col`
  (the DEFAULT ripgrep/gcc/Roslyn format), `./file`, `file#Lnn`, `file:10-20`, `file (line 42)` mis-extracted and
  BYPASSED the in-diff membership test → an in-scope defect could be relabelled an out-of-scope class-sibling to
  dodge in-leg fixing. Reproduced first-hand. Ships in the deliver gate for every future frozen-spec leg → NOT-MET.
- FIX (REV 2 @3a5caba): the PREFERRED **fail-CLOSED** approach — the site must match a strict clean grammar
  (`^[A-Za-z0-9._/-]+(?::\d+)?$` + no `.`/`..`/empty segments); ANY other form THROWS (fails closed), so the next
  unanticipated spelling cannot silently reopen the hole. Pinned by an independent RED test-author (Case5a-e). I ran
  the extended v15 selftest first-hand: Case1 GREEN, Case2/3 RED, Case4 GREEN, Case5a-e (all 5 leaking forms) RED.
  Re-G5 SOUND (fix scoped to review-check.ps1; v16/v17/v18/additive unchanged from round 1).
- Process signal (worth keeping): the builder's in-session single-model Sonnet G5 MISSED this P1 (it probed
  backslash/no-line but not the editor-anchor forms); the fresh cross-session Opus 5-lens G5 caught it — the binding
  fresh-session G5 is load-bearing, not ceremony. (A cross-family Codex pass remains an optional extra; a same-family
  fresh-session Claude G5 is a valid binding pass per direction-os rule #3.)
- DF-11 (2 pre-existing P3s in review-check.ps1: Int32-overflow on a >10-digit finding-# in the message; a negative
  Rounds accepted) → LATENT backlog, low priority.

## c-visual-005 — binding G5 SOUND (render-only)
Verified first-hand @fbab24f: the 4 v17-banned behavior-source-scanners
(GasVisual/{GasLightBinder,GasUberShader,GoodSample,SingleCustomEditor}ScanTests.cs) DELETED; the wiring smoke is
now EXISTENCE-ONLY (`File.Exists`; grep confirmed no `Does.Contain`/`ReadAllText`-over-source/retired-markers/globs
— the crutch is genuinely retired). Real visual changes preserved (GasUber depth-occlusion `GASUBER_DEPTH_CLAMP`,
render-feature depth wiring, GasShaderMath + GasShaderDepthMathTests, Open-Arena-Jet + LP1 camera/replay,
GasRoomScene). Owner-eye «работает» (2026-07-05); 1331/1331 headless. Its own fresh-session G5 caught + fixed a
RESULT evidence nit (the report named the retired classes while claiming a clean grep — the cited-artifact-ahead
class, fixed). SOUND.

## merge reconciliation (the fiddly part)
- c-031 → main: clean --no-ff merge from bbe86eb (dev = main + 4 commits). @21f9c0f.
- c-visual-005 → main: dev2 was based on cde4c3d — 2 merges BEHIND main (pre-c-029/c-030) and predated RESULT-per-leg
  (c-030). Only ONE conflict (RESULT.md: dev2 modified it, main deleted it via c-030's rename). Resolved: root
  RESULT.md kept DELETED (RESULT-per-leg), the leg's report extracted to docs/results/c-visual-005.md (cites no
  docs/reviews/docs-adr path → passes v18). Post-merge: the c-031 `source_scan_ban_grandfathered_pending_c-visual-005`
  grandfather (validation.config list+note + the AGENTS.md `## Contract v17` bullet) DISCHARGED, since the 4 files are
  now deleted. validation.config JSON re-validated (synced=18). @26dd062.

## captures
- docs/results/c-visual-005.md carries the dev2 status `DELIVERED-on-dev2` (a render leg on dev2, -Deliver-exempt);
  the engine result-check status regex wants `DELIVERED on \`dev\``, so a future -Deliver fallback-all pass (HEAD==main,
  no branch delta — rare) would flag it. Trivial 1-line fix if it ever bites; not worth touching now.
- Product working tree carries the unrelated MCP-bridge Packages/*.json flicker (both dev worktrees) — not in scope.

## play_check
- step1 verify-by-refutation: DONE — c-031 binding G5 (5-lens wf_1b1d5d16-85e + first-hand selftests): NOT-MET round 1
  (P1), SOUND after the REV-2 fail-closed fix (Case5a-e run first-hand). c-visual-005: SOUND first-hand (source-scan
  retirement genuine + owner-eye).
- step2 harvest-per-lens: DONE — learning: an in-session single-model G5 missed a deliver-gate P1 the fresh
  cross-session G5 caught; the binding fresh-session G5 stays a real gate. And the fail-CLOSED-on-grammar pattern
  (reject the unknown form, don't just widen the regex) is the right fix for a parse-based gate.
- step3 update-tree: SKIPPED — no TREE change; both are infra/render sub-legs, the g-9c41 bet continues.
- step4 add-back-check: DONE — nothing missed.
- step5 knowledge: SKIPPED — captured in this RESULT + the product CONTRACT_VERSION/ADR-P-0008 records.
- step6 select-next: DONE — c-exec-021 (Sc-reactions) is now IMMEDIATE, on a clean v18 base.
- step7 close: DONE — this RESULT.

## log
g-9c41 review — c-exec-031 (§Re-sync v14→v18) + c-visual-005 (visual source-scan retirement) both binding-G5 SOUND +
MERGED (@21f9c0f / @26dd062) + PUSHED. c-031 round-1 P1 (v15 anti-dodge site-parse false-green) FIXED fail-closed
REV-2 (Case5a-e run first-hand); v16/v17/v18 SOUND. c-visual-005: 4 v17-scanners deleted, existence-only smoke,
owner-eye. Grandfather DISCHARGED. GasCoopGame on contract v18. DF-11 → LATENT. Next = c-exec-021 on a clean base.

## next
c-exec-021 (Sc-reactions) — re-harden + fill §PENDING from the Sc-kernel/W1b RESULTs, fire in a FRESH owner-present
PLAN (the direction writes the CALL). The infra runway is clear: GasCoopGame main @26dd062 is on contract v18, gated
by the current rules. Do NOT re-fire c-031 / c-visual-005.

END_OF_FILE: live/indie-game-development/history/2026-07-05-s-work-052-c-exec-031-c-visual-005-close.md
