# RESULT s-work-046 — resolve d-visual-sourcescan-route-001 (visual route + delegated net call)

session: s-work-046
direction: indie-game-development
node: g-7e15 (VISUAL)
play: shape / work (act on an answered decision; frame the follow-on CALL)
date: 2026-07-04
follows: s-work-044 (binding G5 = NOT met on @3858752); built on the concurrent s-work-045 commit @0e5437a (c-028 close)

## outcome

The owner answered d-visual-sourcescan-route-001 and delegated the networking sub-question to me. Resolved:
OPTION 1 (re-derive clean on main v14). Framed the clean re-derive CALL **c-visual-005** and recorded the
networking decision. No product-repo change; no merge of the contaminated @3858752.

## owner input (2026-07-04, verbatim intent)

- «По визуалу всё окей» → visual accepted (owner-eye stands).
- «Шейдеры, естественно, нужны — это была главная задача» → the shader work (incl. the GasUber scene-depth
  occlusion "walls occlude the gas") is WANTED and KEPT (declared).
- «Сеть — я не знаю, но как-то там вылезло. Ты можешь сам сказать, нужно нам это, не нужно» → networking
  DELEGATED to me to decide.

## my delegated decision — FishNet networking: NOT now / PRESERVE

The FishNet work in @3858752 (pre-latch input buffering `MaxPreLatchInputsPerConnection`, peer-eligibility/auth
gating, disconnect discard, a convergence test suite) is real input-lockstep plumbing aligned with the LOCKED
netcode model (TREE #12). But I decided NOT to pull it into the road now, and to PRESERVE it, because:
1. OFF the current road — the active bet is the gas character road (Sc-reactions next); netcode is only a
   *candidate* row for the July demo-road shape (d-demo-road-001), not a framed slice. Pulling it in = an
   unplanned netcode slice jumping the queue (WIP / G1).
2. DORMANT — the bus has no non-test caller (only constructed in FishNetConvergenceTests); shipping unreviewed
   dormant netcode is exactly the "one wiring change from live" risk.
3. UNREVIEWED — no PLAN, no independent review, no EditMode net suite run in a real venue; it changes existing
   behavior (ineligible peers now SILENTLY dropped vs threw) — a semantic change that needs deliberate design review.
4. STALE base — written on contract v11 (46 behind v14 main).
PRESERVE mechanism: tag @3858752 as `ref/visual-sourcescan-leg-3858752` (step 0 of c-visual-005) so the diff is
never lost; its home = the July demo-road network-ladder / Sc-net candidate slice, where it gets a real PLAN + review.
Owner can override if his gut disagrees.

## route resolution — OPTION 1

- Do NOT merge @3858752 (binding-G5 NOT met, s-work-044).
- FRAMED c-visual-005 = work/c-visual-005-clean-sourcescan-retirement-call.md: a CLEAN, SINGLE-CONCERN re-derive on
  current main @cde4c3d (v14).
  - KEEP: delete the 4 visual *ScanTests.cs; retire the c-visual-003 SHADER/LAMP/SAMPLE scan wording in
    spec/tasks/ADR; the real math/acceptance tests (GasShaderMath.SceneDeviceDepth + its test, TypeId/roster
    acceptance tests are genuine); the GasUber occlusion feature (DECLARED) + duplicate-sampler compile fix; the
    Open Arena Jet + LP1 Proof camera fixes + minimal plumbing.
  - THE ONE FIX vs @3858752: the wiring smoke must be genuinely EXISTENCE-ONLY (File.Exists / type-component
    presence) — NO File.ReadAllText/Does.Contain/glob over source or shader TEXT (that residual scan was the very
    crutch this leg exists to retire).
  - DROP (out of scope): ALL FishNet networking (preserved on the tag); ALL gate/tooling edits (NEVER self-edit
    check.ps1 — dev_2 visual close = owner-eye + normal gates, NOT the engine "DELIVERED on `dev`" assertion, which
    v14 main STILL hardcodes; a branch-aware gate, if ever wanted, is a SEPARATE reviewed tools/ change with an ADR);
    the benchmark-scan concern (TypeId narrowing / GasRosterConfig / VoxelBenchmarkDirector); the dep bump.
  - Step 0: tag @3858752 + start from a clean main base (this also does the dev_2 reset the c-visual-004 guard needs).
- SEQUENCING: fire c-visual-005 (fresh GasCoopGame_dev_2, owner-present PLAN) BEFORE c-visual-004 Stage 1 — Stage 1
  then rebases onto the clean tip.

## evidence / grounding (first-hand)

- Current product main = @cde4c3d (v14). v14 `tools/check.ps1` L25 still hardcodes `DELIVERED on \`dev\`` (engine-only)
  → confirms the dev_2 visual close must NOT rely on that assertion, and confirms why @3858752 wrongly self-edited it.
- No framed `Sc-net` node exists in live/ (grep) → netcode is a candidate, not the current road → discard-now/preserve
  is correct.
- The @3858752 KEEP/DROP mapping was derived first-hand from its 32-file diff (s-work-044 record).

## state_changes (applied by this session as writer, committed locally)

- NOW.md updated-stamp → s-work-046 (built on s-work-045 @0e5437a).
- NOW.decisions: d-visual-sourcescan-route-001 → ANSWERED (option 1 + the net decision recorded).
- NOW.open_calls: += c-visual-005; c-visual-004 ⚠ note amended (route answered → c-visual-005 is the vehicle + does the reset).
- NOW.parallel_tracks g-7e15: appended the resolution.
- NOW.next VISUAL section: RESOLVED; "Still pending owner" drops d-visual-sourcescan-route-001.
- LOG.md += s-work-046; work/c-visual-005-clean-sourcescan-retirement-call.md created.
- NO TREE.md / CHARTER.md change (G9 clean). NO product-repo change. G1 intact (no new bet; g-9c41 spine untouched;
  c-visual-005 is a parallel-track CALL, not an active_task).

## captures

- The GasUber scene-depth occlusion ("walls occlude the gas") is now an owner-wanted, DECLARED visual feature —
  ensure c-visual-005 documents it in the spec/ADR so it is never again a smuggled change.
- The @3858752 FishNet diff is the starting reference for the July demo-road Sc-net candidate slice
  (tag ref/visual-sourcescan-leg-3858752).

## play_check
- Act on the answered decision — DONE (option 1 recorded; net decided).
- Frame the follow-on CALL — DONE (c-visual-005, single-concern, KEEP/DROP explicit, existence-only smoke, no gate self-edit).
- (owner) steps cite owner words — DONE («по визуалу всё окей» / «шейдеры … нужны» / net delegated).
- No TREE change without approval — HELD (none made).

## log
s-work-046 — resolved d-visual-sourcescan-route-001 (owner option 1 + my delegated net call): visual+shader kept
(occlusion declared); FishNet NOT now / PRESERVED (tag) for the future Sc-net slice; framed c-visual-005 (clean
re-derive on v14, wiring smoke existence-only, net/gate-tooling/TypeId dropped). No merge, no product change.

## next
Fire c-visual-005 in a FRESH GasCoopGame_dev_2 session (owner-present PLAN): step 0 tag @3858752 + reset dev_2 off
the polluted tip, then the clean re-derive on main @cde4c3d. Then c-visual-004 Stage 1 rebases onto the clean tip.
Engine road unchanged: c-exec-021 (Sc-reactions) remains the direction's IMMEDIATE per s-work-045.

END_OF_FILE: live/indie-game-development/history/2026-07-04-s-work-046-visual-sourcescan-route-resolve.md
