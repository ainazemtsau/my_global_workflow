# CALL c-visual-008 — Stage 3.5: Idle Life + Motion Smoothness — RENDER-ONLY

> FIRE-READY 2026-07-09 (s-work-065). Inserted after c-visual-007 Stage 3
> delivered and was merged+pushed to GasCoopGame `origin/main@9d6f8ded`, before
> Stage 4 starts. Owner observed that the gas body still reads too static when
> stationary, motion onset reads jerky/low-frame, and the surrounding scene can
> feel muddy. This leg repairs that readability gap without faking sim flow.
>
> Base for planning is GasCoopGame `origin/main@9d6f8ded` with c-visual-007
> `dev2@1c99a907` already merged. First product action is to verify/sync the
> visual checkout to that main tip (or a fresh branch/worktree from it), clean
> head, and contract v19 behavior: owner-readable PLAN, then separate BUILD.

- direction: indie-game-development
- node: g-7e15 (VISUAL track)
- play: work (executor leg — GasCoopGame render layer)
- repo: C:\projects\Unity\GasCoopGame_dev_2
- kind: engineering
- runs_in: a FRESH GasCoopGame PLAN session first, then a separate FRESH BUILD session after owner plan approval
- base: GasCoopGame `origin/main@9d6f8ded`; verify c-visual-007 `1c99a907` is present and checkout is clean before planning
- plan_source: live/indie-game-development/work/gas-visual-plan-v2-2026-07-02.md plus c-visual-007 close evidence

## goal
One real gas no longer reads as dead/static when stationary, no longer reads as missing frames when motion starts, and the scene clarity around/through the gas is honestly understood on the Stage-2 half-res render path.

## context
- c-visual-007 delivered Stage 3 on the Stage-2 half-res path: single-gas visual, owner choices band count 2 and opacity ceiling 0.72, LP1-LP5 pass with caveats, no fake visual-only jet, Core/sim diff empty.
- Owner's follow-up playtest raised three visual gaps: stationary gas is completely static; gas-only motion starts in a sparse/jerky way; the gas/scene can read muddy, as if the surrounding environment is also being blurred.
- `work/gas-visual-plan-v2-2026-07-02.md` says the renderer already has Perlin-Worley noise, deblock warp, detail erosion, self-shadow, HG light, toon bands, curl/billow motion, IGN dither, shell rim/fresnel and warning-edge recolour. This leg must audit whether those levers are enabled, visible, temporally continuous and tuned on the delivered path before inventing new machinery.
- Stage 4 ("Три характера + шкала опасности") remains unopened. It should not start until this single-gas body/motion readability debt is resolved or honestly routed.
- Source-of-truth honesty stays binding: idle internal life may animate internal density/noise/lighting/erosion inside the existing gas body, but must not move the gameplay gas boundary, center of mass, danger state, or imply a false directed flow.

## scope
1. Audit the delivered Stage 3 render path in motion and identify why stationary gas reads frozen: disabled/ineffective curl-billow/noise phase, update cadence, replay sampling, half-res upsample/composite, low amplitude, or another named cause.
2. Add render-only idle internal life for stationary gas: subtle internal drift/billow/detail evolution that is visible in owner-eye A/B while the true gas placement and gameplay state remain stationary.
3. Smooth motion onset/readability: reduce the "missing frames" / jerky gas-only movement impression through legal render-side temporal continuity, interpolation, phase continuity or presentation tuning. If real smooth directed flow needs sim velocity, face-flow, a denser view grid, or new source data, STOP and return that as a future movement-data spec instead of faking it.
4. Check clarity/muddiness: compare gas-off/gas-on and outside-gas/through-gas views. Confirm whether the whole scene is being unnecessarily blurred by half-res upsample/composite, or whether the softness is only expected volumetric occlusion inside the gas.
5. Record owner-visible A/B evidence against c-visual-007 baseline in at least three regimes: stationary cloud, first movement onset, and an open/no-wall or room-edge view.

## boundaries
- RENDER-ONLY: ZERO `Core/**`, sim, network, reaction, Sc-sense, damage, or gameplay edits.
- No new gas types, no Stage 4 archetypes, no danger ladder, no blind lineup, no frontier-blend work.
- No Stage 5/6 work: no flood perf spectacle, teammate readability, residue, sparse VFX accents, particles, Feel/MMFeedbacks, or post effects as an acceptance crutch.
- No fake visual-only jet, no invented velocity field, no render-side movement that contradicts the current sim/GridView data.
- VFX/particles may be named as a later optional accent only; they do not count as fixing the gas body in this leg.
- No self-written source-text scanner as behavior evidence. Render behavior requires real Unity/live-MCP/PlayMode evidence plus owner-eye A/B.
- Required Unity Editor/MCP/headless license unavailable = STOP and ask the owner to launch/approve; no workaround.
- Do not push/merge product main from this executor leg unless a later owner-gated close explicitly authorizes it.

## done_when
- Contract v19 discipline is confirmed: PLAN and BUILD are separate sessions; the PLAN is owner-readable and stops before build; BUILD starts fresh from the frozen approved plan.
- The product checkout base is recorded: GasCoopGame `origin/main@9d6f8ded` with c-visual-007 `1c99a907` included, or a documented STOP if that cannot be made true.
- The c-visual-007 baseline is captured/recorded before tuning, and every accepted visible change is A/B'd against it.
- Stationary gas has visible subtle internal life while its boundary/placement/danger remains honest/static; the owner can compare baseline vs changed clip/bookmark.
- Motion onset no longer reads as missing frames/jerky in the selected evidence. If render-only current data cannot achieve that honestly, the RESULT says so and routes a future movement-data/view-grid/performance-readability spec.
- Clarity evidence exists for gas-off/gas-on and outside/through-gas views; no unintended whole-scene blur remains. If softness is inherent to the current half-res path, the RESULT records the exact limitation.
- No fake visual-only jet or false flow is added; `git diff -- Core/**` is empty.
- `docs/results/c-visual-008.md` and measurement/evidence notes exist and route the RESULT home.
- `tools/result-check.ps1 -Repo . -ChangeId c-visual-008` PASS; normal `tools/check.ps1` green; `tools/check.ps1 -Deliver` is run and reported. If full `-Deliver` is still blocked only by pre-existing c-exec-021/c-visual-005 MERGED-status docs on main, the c-visual-008 RESULT must name that unrelated gate blocker and still provide per-leg result-check green.

## return
- PLAN session return: owner-approved Stage 3.5 plan + frozen build handoff; c-visual-008 stays open.
- BUILD session return: RESULT home with outcome, evidence, A/B clips/bookmarks/screens, check output, Core/sim diff proof, any cuts with owner-ack, and a recommendation whether Stage 4 can start or whether a movement-data slice must be framed first.

## budget & rigor
One owner-present PLAN session plus one focused BUILD session. If fixing motion honestly needs sim velocity/face-flow/new view data, STOP and split; do not hide the gap with visual-only directionality.

parent: s-work-065

END_OF_FILE: live/indie-game-development/work/c-visual-008-stage3-5-motion-clarity-call.md
