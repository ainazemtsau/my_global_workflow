# CALL c-exec-004 — g-9c41 / t-3 (kill-gate finale: sustained-load VERDICT + stream LOCK)

> 🔴 **SUPERSEDED 2026-06-23 (pre-ADR-0010 history).** Builds on the OLD host single-writer / chunked-delta stream («band sim Wave 2») — RETIRED by input-lockstep (ADR-0010) + the slice methodology. Authority now = `knowledge/g9c41-gas-engine-SPEC.md` (the canon). Kept for history only; do NOT build from it.

> Copy-paste this whole CALL into a fresh chat in the GasCoopGame **dev** worktree
> (`C:\projects\Unity\GasCoopGame_dev`). It opens with an interactive PLAN (you present).
> Framed s-work-005 (2026-06-15); hardened via wf `frame-c-exec-004-t3` (draft + 3 adversarial lenses:
> scope-creep / kill-gate-completeness / over-prescription). Builds ON the frozen t-2 stream
> (ADR-0003 v2, C1–C22) — does NOT redesign it.

```
to: executor (coding agent)   repo: GasCoopGame   kind: engineering
direction: indie-game-development   node: g-9c41   task: t-3
parent: s-work-005 (recorded the c-exec-003 return + framed this)

goal: |
  Under a SUSTAINED breach wave, host + 2 clients keep the reconstructed field bit-exact-when-it-should-be
  and bounded-when-it-can't with BOTH clamps engaged — and the STEADY (not peak) change-traffic is measured
  against the aggregate clamp so the bet's central question gets a crisp PASS/FAIL VERDICT: does the
  chunked-delta gas stream hold under load, or does the kill-gate trip. With that verdict in hand, the
  wire-format + revision barrier are declared LOCKED — frozen as the precondition the band sim (Wave 2)
  will build on — and t-3 proves the layer fabric is REAL by showing a CROSS-LAYER interaction (a
  reaction/heat event drives the temperature layer to respond) on the locked stream, with the REAL
  controlled breach running UNDER that sustained load. This is the 2026-06-30 kill-gate moment: t-3 either
  pronounces "stream holds, LOCK it, roll to Wave 2" or it trips the gate. The gate has TWO distinct
  failure halves (per NOW.md kill_by) that route to DIFFERENT exits: (i) per-tick consistency cannot be
  made to hold after reasonable iteration -> P6 model/vendor spike (FishNet<->NGO, 1-2wk timebox);
  (ii) the steady dirty-rate irrecoverably blows the aggregate clamp -> narrow to the Barotrauma-hybrid
  contingency (client-local diffusion + threshold corrections). t-3 PRONOUNCES the sustained verdict t-2
  deliberately deferred (t-2 recorded peak only, clampVerdict stamped "DEFERRED-T3"); it does NOT redesign
  the t-2 stream and does NOT re-open ADR-0003 v2 C1-C22.

leg_opens_with: |
  PLAN — interactive, plan mode, owner present, frontier model (Opus 4.8 high-effort, owner-facing), in the
  product-repo dev worktree C:\projects\Unity\GasCoopGame_dev (branch dev; FIRST sync dev to current main
  HEAD — t-2 landed on main via merges b9edbce + 30f9e45; confirm dev is at/ahead of that tip before any
  work, C1-C22 intact). NO CODE until ADR + a default-FAIL G0 ledger are frozen and owner-approved; then
  autonomous build legs.

  FIRST PLAN STEP — read, do not re-litigate: AGENTS.md + CLAUDE.md (run contract + the NEW
  `pwsh tools/check.ps1 -Deliver` closing-RESULT.md gate); ADR-0003 v2 §Consequences/§Verdict + the FROZEN
  C1-C22; the t-2 RESULT `cuts` list (history/2026-06-15-c-exec-003-t-2-result.md) and the archived
  c-exec-003 "boundaries/Out-of-scope"; the living spec openspec/specs/sim-core/spec.md (14 reqs);
  work/converge-g-9c41.md §WHAT-C; and os/FRICTION.md if present.

  C-ROW DISCIPLINE — t-3 OPENS four rows and only EXTENDS two t-2-FROZEN rows (do NOT re-derive frozen
  magnitudes): t-3 OPENS/closes C7 (channel reliability), C9 (keyframe cadence K), C13 (fault-injection
  scope), C14 (per-chunk min-resend). t-3 only EXTENDS the two rows t-2 already FROZE — C16 repro-constants
  (inherit the t-2 values; ADD the sustained-wave schedule + measurement window) and C18 measurement schema
  (inherit the t-2 schema; ADD the steady-window aggregate + flip clampVerdict). t-2's frozen C16/C18 values
  are NOT re-opened.

  PLAN must DECIDE + FREEZE (in ADR-0004, or ADR-0003 v3 — PLAN decides which; C1-C22 stay UNTOUCHED, t-3
  only ADDS), each pulled from the `cuts` list:
    (a) the SUSTAINED-LOAD test shape — what "sustained breach wave" concretely means: a repeated/extended
        breach schedule vs one long high-dirty-rate run; the run length; how many converged-settle cycles it
        must contain; the integer dirty-load generator that keeps the channel hot long enough to read a
        STEADY rate (not t-2's single peak-through-breach). The FROZEN t-2 per-run constants (runTicks=300,
        breachTick=120) are the per-cycle UNIT the sustained wave repeats/extends, not a fresh single-run
        length re-derived and relabelled "sustained."
    (b) the steady-dirty-rate VERDICT predicate — a SINGLE binary machine-evaluable predicate over the
        committed per-tick series that returns PASS or FAIL with NO human judgement at evaluation time. The
        "irrecoverable vs transient catch-up" distinction must be ENCODED AS PART OF that predicate (e.g. a
        bounded backlog-drain deadline measured in ticks/settles), not left as prose to interpret post-run.
        Over what window, with what aggregate-clamp value (carry ADR-0003's 275 KB/s unless PLAN re-opens
        with reason). If PLAN cannot reduce the verdict to such a predicate, THAT escalates to the owner
        before any build. This is the kill-gate arithmetic — pin it before code.
    (c) the PRODUCTION channel reliability decision (C7) — t-2 shipped only a test-side drop+delay decorator
        over a reliable-ordered prod channel; t-3 DECIDES + REALIZES the REAL channel (unreliable-sequenced
        vs reliable-ordered) and the fault model it must survive in production, with the seeded
        fault-injection PROMOTED from test-decorator to a gated production property. The steady-rate verdict
        (b) MUST be measured WITH the chosen production fault model ACTIVE, not only on a clean channel — an
        honest verdict survives the real loss model.
    (d) periodic keyframe cadence K (C9) — t-2 used on-quiesce residual flush + on-demand snapshot only;
        PLAN decides whether sustained load FORCES a periodic K (and its value) or quiescence-only still
        suffices, and pins recovery-under-sustained-load.
    (e) per-chunk min-resend interval (C14) — the per-chunk rate limiter t-2 named as a t-3 extension point:
        in or out, and if in, the deterministic interval.
    (f) real-uplink vs loopback+software-clamp — DECIDE explicitly whether the sustained measurement is
        loopback with software clamps (t-2's environment) or a real link, and STATE the honesty boundary the
        verdict carries (which numbers are environment-independent: the byte size + per-tick dirty-chunk
        COUNT; which are not).
    (g) the CROSS-LAYER mechanism — the minimal deterministic toy reaction/heat MECHANISM by which a P2
        cross-layer event drives the temperature layer (LayerKey1) to respond. Its CEILING is a single
        deterministic integer rule (the exact rule is ADR-0004's to fix); it only needs to demonstrate the
        P0->P1->P2->P3 coupling path is REAL and hash-consistent on the reconstructed-cells domain, NOT to
        model heat. (Frozen t-2 facts to ride, not re-decide: the P0->P1->P2->P3 phases and LayerKey1 are
        already frozen — cite them, do not re-shape them.)
    (h) whether mid-run late-join becomes a t-3 GATE — DEFAULT is it stays bet-2-deferred (per the cut_list;
        t-2 kept it green-but-ungated). PLAN promotes it to a t-3 gate ONLY if the sustained-load verdict's
        honesty genuinely requires a join-baseline, and records the reason.
    (i) the LOCK declaration's exact content — what specifically becomes frozen-immutable-for-Wave-2 (wire
        format + revision-barrier form + the C-rows t-3 closes: C7/C9/C13/C14), recorded so Wave 2's band
        sim builds on a contract that cannot silently move.

model_routing: |
  BUILD = Claude Code + Opus 4.8 (planner frontier/high-effort owner-facing; builder default-tier
  autonomous, one feature smallest-first, reuse-first on the frozen t-2 contracts). VALIDATE = Codex +
  GPT-5.5 — read-only, fresh-context, different family, did NOT author; reproduces the dotnet core + the
  sustained-load dual-mode gates + the steady-rate verdict arithmetic as a regression check; MUST NOT
  certify the transport/PlayMode axis from a dotnet run, and MUST independently re-derive the verdict
  PASS/FAIL from the committed per-tick series via the frozen predicate (not trust the builder's
  clampVerdict flag). Weaker model = gate-runner, never authority. Binding acceptance = green gates +
  evidence + owner spot-review on the novel netcode AND on the kill-gate VERDICT itself (s-decide-001; the
  verdict is the bet-deciding judgement — owner confirms it). Fallback chain so overnight legs survive
  provider errors.

context: |
  Pointers — input evidence for PLAN, NOT a binding spec (PLAN + ADR own the HOW):

  - THE FROZEN t-2 FOUNDATION (build ON it, do NOT redo): delivered GREEN to main (code merge b9edbce,
    OpenSpec close 30f9e45; dotnet 71/71, FishNet PlayMode 6/6 over Tugboat 127.0.0.1 loopback). ADR-0003 v2
    freezes C1-C22: ONE codec lossless at Q=1/deadband0, lossy at deadband=Q=16 + per-client 150 KB/s +
    aggregate host 275 KB/s clamps; clients reconstruct WITHOUT running the sim; kill-gate hash domain =
    reconstructed FIELD CELLS only (pinned Fnv1a64 fold, NOT whole SimState.Hash()). Layer fabric:
    LayerRegistry (ascending-LayerKey, no dict enumeration) + a separate RevisionFeed/IGridEventBus;
    single-writer-per-(LayerKey,phase) registry-minted token (duplicate registration throws); pinned phases
    P0 commands/breach -> P1 layer-sim -> P2 cross-layer events -> P3 publish; gas=LayerKey0,
    temperature=LayerKey1 (sibling int[], consumes zero gas RNG, proven by an RNG-conservation guard).
    Breach = a TickInput.Command on the lockstep ITickInputBus (peers agree the tick); host flips one
    RoomGraph portal Closed->Open at breachTick; FIELD STATE IS NOT in the input bus. Revision barrier never
    applies a stale (lower-revision) chunk, recovers bit-exact at the next converged settle (proven by an
    independent host-accepted-revision oracle). Frozen constants: Q=16, deadband=16, settle N=16,
    runTicks=300, breachTick=120, peers {1,2,3}. Determinism: integer-only, no wall-clock, seeded RNG,
    engine-free core (R13), networking edge-only (R12/R14). Source: ADR docs/adr/ADR-0003-gas-field-state-
    stream.md v2; measurement artifacts docs/measurements/g9c41-t2-{lossless,lossy}.json
    (framingIncluded:false, clampVerdict currently "DEFERRED-T3" — t-3 flips it in NEW t-3 artifacts, see
    done_when p5) + scene-profile-g9c41-t2.json (sceneProfileHash=10953502479008948765) +
    repro-constants-g9c41-t2.json. Goldens: lossless cell-hash 17841808856690891867, breach cell-hash
    16144683277153780402 (must stay green).

  - THE PRECISE t-2 CUTS = t-3's raw material (from the t-2 RESULT `cuts`): sustained-breach-load clamp
    VERDICT (t-2 recorded peak only — t-3 PRONOUNCES the sustained verdict, the CORE of this leg);
    unreliable-sequenced PRODUCTION channel (t-2 = test-decorator only, prod stayed reliable-ordered);
    real-uplink bandwidth (t-2 = loopback only); periodic keyframe K (C9, t-2 = quiesce-flush + on-demand
    only); per-chunk min-resend (C14, named extension point); mid-run late-join (kept green, not gated).

  - AUTHORITATIVE t-3 done_when (the 4 NOW.md points + the s-shape-004 re-scope, made machine-testable
    here): NOW.md active_tasks t-3.

  - THE KILL-GATE FRAME (NOW.md active_bet kill_by): checkpoint 2026-06-30 = if per-tick consistency can't
    be made to hold after reasonable iteration -> P6 model/vendor spike (1-2wk timebox: FishNet<->NGO,
    last-resort rollback); if the steady dirty-rate irrecoverably blows the aggregate clamp -> narrow to the
    Barotrauma-hybrid (client-local diffusion + threshold corrections). These are TWO DISTINCT exits for TWO
    DISTINCT failure halves — the RESULT must name WHICH half failed. next_if_true: stream LOCKED -> roll to
    Wave 2 (band sim + grid from DA + temperature layer). Hard wall 2026-07-24 (G3, never extended).

  - CONVERGE SET (ratify, don't re-derive): work/converge-g-9c41.md §WHAT-C — the t-3-OPEN rows are NAMED
    there: C7 channel reliability (own-decision->PLAN/G7), C9 keyframe-K (magnitude->PLAN / scope), C13
    fault-injection scope (scope->G7), C14 min-resend (open->PLAN). The two rows t-3 only EXTENDS (already
    frozen in t-2): C16 repro-constants, C18 measurement schema. ADR freezes the t-3-OPEN magnitudes against
    that named set; it does not touch frozen C16/C18 values.

  - BET RULES (load-bearing, NOW.md active_bet.rules): R12 player-host only; R13 engine-free pure-C# core,
    Unity = adapters only; R14 net is an edge wrapper at the DI root, never in business logic; gas rides OUR
    custom chunked-delta channel regardless of vendor.

  - t-1 CONTRACTS to reuse (do NOT redesign): the ITickInputBus seam + SimHostFactory.CreateNetworked DI
    point, SimState/Fnv1a64 pinned-order hashing, the FishNetTickInputBus adapter. ADR-0002 (lockstep,
    field-never-networked-as-inputs).

  - RUN CONTRACT + the NEW closing-report gate: repo AGENTS.md + CLAUDE.md, validation.config (core_build =
    the R13 boundary gate), `pwsh tools/check.ps1` -> "OK: all gates green". As of 2026-06-15 every leg MUST
    close with a structured RESULT.md at repo root, gated by `pwsh tools/check.ps1 -Deliver` (FAILS on
    absent/under-filled RESULT.md — a prose summary does NOT count). REVIEW.md rubric; openspec lifecycle
    propose->apply->verify->archive (archiving is part of done). Editor/transport loop = the free IvanMurzak
    Unity MCP; no CI on the transport/PlayMode axis (Unity Personal = no unattended activation).

boundaries: |
  - DO NOT redesign or re-litigate the FROZEN t-2 stream. ADR-0003 v2 C1-C22 are immutable here — the ONE
    codec, the lossless/lossy duality, Q=16/deadband=16/N=16/clamps 150/275, the reconstructed-FIELD-CELLS
    hash domain, the LayerRegistry + RevisionFeed + single-writer token, the pinned P0->P3 phases,
    breach-as-TickInput.Command, the revision barrier. t-3 BUILDS ON these and only ADDS (ADR-0004 or v3
    with C1-C22 untouched). Touching a frozen constant or the codec = a blocker that escalates to the owner,
    not a builder decision. t-3 must NOT mutate the committed t-2 measurement artifacts (g9c41-t2-*.json) —
    it writes NEW t-3 artifacts; the clampVerdict flip happens in the t-3 artifacts, not by editing the
    frozen t-2 ones.

  - DO NOT redesign the proven t-1 core: engine-free boundary (R13; core_build is the gate), the determinism
    contract (no float/double, unchecked, no wall-clock, seeded RNG, pinned hash order, stable input order),
    the t-1 goldens + the t-2 cell-hash goldens (17841808856690891867 / 16144683277153780402) stay green (a
    broken golden = blocker). No FishNet prediction/[Replicate]/[Reconcile]/NetworkTransform/SyncVars for the
    field; field state stays OFF the input bus.

  - Net model LOCKED for the IN-LEG build — no P6 / vendor re-open inside this leg; FishNet stays. (P6 is the
    kill-gate EXIT if the consistency half fails, not an in-leg option.)

  - OUT of t-3 (bet-2, OUT — per s-shape-004 + the t-2 cuts): the band/sector solver, the T2 per-cell grid,
    structural collapse / level-wide destruction (OUT forever per R9), multiple gas TYPES / real reaction
    CONTENT. THE CROSS-LAYER CEILING: t-3 proves reaction/heat->temperature as a deterministic MECHANISM on
    the TOY layers — its ceiling is a single deterministic integer rule (e.g. a breach/reaction event at cell
    c bumps temperature[c] by a frozen constant via one P2 event; ADR-0004 fixes the exact rule). Anything
    beyond a constant-delta integer response is OUT of t-3. It must demonstrate the coupling PATH is real and
    hash-consistent, NOT model heat, and must not grow into the band sim.

  - PLAN OWNS THE DESIGN — the CALL deliberately does NOT pre-decide magnitudes that belong in ADR-0004: the
    channel-reliability choice (C7), the keyframe cadence K (C9), the sustained-load test shape, the
    steady-rate verdict window/predicate, the min-resend interval (C14), the cross-layer rule, the
    divergence-bound threshold (carry the t-2 primitive Q unless PLAN re-opens with reason — done_when states
    the PROPERTY, ADR-0004 carries the number), the telemetry schema field names/values (extends C18 —
    ADR-0004's, not the CALL's), and real-uplink-vs-loopback are ALL PLAN/ADR work. The CALL pins WHAT must be
    true and HOW it is checked (the acceptance bar in done_when); it does not pin the numbers. (c-exec-003 was
    critiqued for over-prescribing — keep the direction<->contour boundary clean.)

  - Builder must NOT edit validation.config / the G0 ledger / the living spec / REVIEW.md / acceptance
    criteria, nor touch the vendored Packages/com.firstgeargames.fishnet/. Nothing under _scratch/ is
    committed. Work ONLY in the dev worktree, never the main checkout (owner keeps Unity open on main). Merge
    dev->main is owner-authorized at the final report.

done_when: |
  Each NOW.md t-3 point is made mechanically verifiable by a runnable check; the new design values (sustained
  test shape, steady-rate verdict predicate + window, channel reliability, keyframe K, min-resend, late-join
  gate decision, cross-layer rule) are FROZEN in ADR-0004/v3 + the default-FAIL G0 ledger BEFORE build and the
  builder cannot change them. C1-C22 untouched.

  (p1) SUSTAINED-LOAD CONSISTENCY HOLD, both clamps engaged — an automated test runs host + 2 clients through
    the FROZEN sustained breach wave (the shape ADR-0004 fixes) with deadband + per-client + aggregate clamps
    ALL live and proven engaged (a silently-disabled clamp = a red negative test, reusing the t-2 over-budget
    negative-test discipline). Machine-checked EVERY tick over the whole sustained run: (a) bounded divergence
    — divergence(tick) = max over hashed field cells of |client_cell - host_cell| after dequantization <= the
    frozen threshold ADR-0004 carries (the t-2 primitive recommends = Q; any tick exceeding it is a
    reconstruction bug, not lossy behaviour); AND (b) convergence to bit-exact at EVERY converged settle
    (settle = host dirty-chunks == 0 for N ticks, reused from t-2's settle predicate), including each
    post-breach re-equilibration settle in the wave. The test asserts the wave contains >= the frozen number
    of non-vacuous settle cycles (so "holds under load" is exercised repeatedly, not once). A SEPARATE
    lossless run (deadband off, Q=1) stays per-tick bit-exact over the sustained wave — the correctness
    oracle. Lossless and lossy MUST share the same reconstruction code path (anti-gaming).

  (p2) THE STEADY-DIRTY-RATE VERDICT — crisp, measured, machine-checkable, ARITHMETIC not judgement. The leg
    PRONOUNCES the verdict t-2 deferred: over the frozen measurement window of the sustained wave, the STEADY
    (not peak) aggregate dirty-chunk wire rate is measured in bytes/sec and evaluated by a SINGLE binary
    predicate frozen in ADR-0004/the G0 ledger BEFORE the run — the predicate encodes the window AND the
    "irrecoverable vs transient catch-up" test (e.g. a bounded backlog-drain deadline) so it returns PASS or
    FAIL with no human interpretation. The leg FAILS its own gate if the verdict is computed by human
    judgement rather than that frozen predicate. The verdict is measured WITH the chosen production fault
    model (C7) ACTIVE — not only on a clean channel. The result is recorded as a hard PASS/FAIL ledger line
    and the t-3 artifact's clampVerdict flips from "DEFERRED-T3" to "HOLD" or "BLOWN". FAIL = steady rate
    irrecoverably blows the aggregate clamp per that predicate -> the leg does NOT silently pass; it returns
    the verdict = kill-gate-trip, naming the contingency (this is the dirty-rate half -> Barotrauma-hybrid).
    The worst-case window is honestly chosen, not cherry-picked, and the environment-honesty boundary
    (loopback+software-clamp vs real-uplink) is stated alongside it.

  (p3) CROSS-LAYER INTERACTION proven on the locked stream, with a NEGATIVE oracle — an automated test shows a
    P2 cross-layer event (the toy reaction/heat rule ADR-0004 fixes) drives the temperature layer (LayerKey1)
    to respond deterministically, riding the pinned P0->P1->P2->P3 phases, and that the temperature layer's
    reconstructed cells stay consistent host-vs-clients on the SAME reconstructed-cells hash domain — under
    the sustained breach load, not in isolation. A NEGATIVE test proves the coupling is REAL: with the P2
    reaction/heat event SUPPRESSED (seeded variant), the temperature layer does NOT show the response — so a
    coincidentally-consistent temperature layer cannot pass the cross-layer check vacuously. The REAL
    controlled breach (RoomGraph portal Closed->Open via TickInput.Command) runs UNDER the sustained load,
    not as a standalone one-shot.

  (p4) THE LOCK DECLARATION — gated behind BOTH p1 AND p2 passing together. The stream wire-format + revision
    barrier (+ the C-rows t-3 closes: channel reliability C7, keyframe K C9, fault scope C13, min-resend C14)
    are declared LOCKED in ADR-0004/v3 as the immutable precondition for Wave 2's band sim, recorded so the
    band sim builds on a contract that cannot silently move. The LOCK fires ONLY when p1 (consistency holds)
    AND p2 (verdict=HOLD) are BOTH true; if EITHER is false the stream is NOT LOCKED and the leg routes to
    contingency. The two failure halves are DISTINCT and route differently: p1-FAIL (per-tick consistency
    cannot be made to hold) -> P6 model/vendor spike; p2-FAIL (steady rate BLOWN) -> Barotrauma-hybrid
    contingency. The RESULT must name WHICH half failed.

  (p5) REPRODUCIBLE BUILD + MACHINE-READABLE TELEMETRY — the sustained run is reproducible from frozen
    constants (seed, sustained-wave schedule, breach schedule, measurement window) reusing the t-2 scene
    profile byte-for-byte where applicable (or a frozen t-3 extension, hash-pinned). Telemetry emitted as NEW
    committed machine-readable artifacts under docs/measurements/ (NOT by editing the frozen t-2 artifacts)
    with a fixed schema EXTENDING t-2's C18 schema (the full per-tick series + the steady-window aggregate +
    the flipped clampVerdict + the environment-honesty flag; exact field names are ADR-0004's, inheriting
    t-2's schema shape); both lossless and lossy modes emit distinct non-empty artifacts covering the
    sustained wave — a silently-dropped mode is a mechanical FAIL. Fault-injection (now PRODUCTION-channel,
    per the C7/C13 decision) is exercised by >=1 deterministic seeded variant, and the steady-rate verdict
    (p2) is measured with it active.

  (p6) PROCESS + the NEW CLOSING-RESULT.md GATE — ADR-0004/v3 owner-approved before code; the default-FAIL G0
    ledger frozen (every entry opened failing, flipped only on opened evidence as a runnable command or
    file:line; builder never edits ledger/spec/criteria/config); all repo gates green on dev
    (`pwsh tools/check.ps1` -> "OK: all gates green"); the openspec change for t-3 archived; _scratch clean.
    THE LEG CLOSES with a structured RESULT.md at repo root that PASSES `pwsh tools/check.ps1 -Deliver`
    (absent/under-filled = a hard gate FAIL; a prose summary does NOT satisfy it). The builder ROUTES that
    RESULT home to the direction indie-game-development and does NOT author the next task CALL. Merge
    dev->main is owner-authorized at the final report.

return: |
  A structured closing RESULT.md at repo root (passing `pwsh tools/check.ps1 -Deliver`) carrying: PR/commits
  on dev (+ owner-authorized merge to main); green gate outputs (tools/check.ps1) + the sustained-wave dotnet
  artifacts (validator-reproducible) + the FishNet/PlayMode transport-axis confirmation under sustained load
  (MCP-run or owner-run, state which); the default-FAIL G0 ledger in FINAL state (entries passing with opened
  evidence); the sustained-load consistency evidence (bounded-divergence-every-tick + bit-exact-at-every-settle
  across the wave; lossless per-tick bit-exact); THE STEADY-DIRTY-RATE VERDICT stated crisply as PASS (HOLD ->
  LOCK) or FAIL (BLOWN -> Barotrauma-hybrid), computed by the frozen predicate (not by judgement), with the
  measured steady rate vs the aggregate clamp, the production fault model it was measured under, and the
  environment-honesty boundary; if the verdict FAILS, WHICH half failed (consistency p1 -> P6 spike, or
  dirty-rate p2 -> Barotrauma-hybrid); the cross-layer reaction->temperature evidence on the reconstructed-cells
  domain (incl. the suppressed-event negative oracle); the committed NEW telemetry artifacts (schema extending
  t-2's C18, clampVerdict flipped; t-2 artifacts untouched); ADR-0004 or ADR-0003 v3 (Status/Context/Decision/
  owner echo-numbered Rn/alternatives/consequences + the frozen t-3 design values, C1-C22 untouched); the LOCK
  declaration content; validator REVIEW.md (file:line, severity, nit cap 10; dotnet gates reproduced); manual
  owner-acceptance steps generated from the SAME verification scripts the validator ran; assumptions, anything
  cut, cost.

  HANDBACK (explicit): t-3's RESULT comes HOME to the direction indie-game-development (workflow-OS). The OS
  writer records t-3 = done and the OS frames any follow-on — review for BET CLOSE if the verdict is PASS + the
  LOCK holds + the wall allows (early finish -> shape bet-2), or the contingency route (P6 spike if consistency
  p1 failed, Barotrauma-hybrid if dirty-rate p2 BLOWN) / bet-2 SHAPING if the verdict trips. The builder does
  NOT author the next task CALL; owner conversational signals trigger the report, never replace it. Surface
  blockers early; stop if infeasible or 2x over budget.

budget: |
  t-3 ONLY (sustained-breach-load consistency HOLD + the steady-rate VERDICT + cross-layer reaction->temperature
  + the LOCK declaration + reproducible telemetry). OUT: band sim, sector subdivision, T2 grid, real gas
  types/reaction content, structural collapse, fp16 wire (bet-2/later). One focused interactive PLAN with the
  owner first (the sustained-load + verdict + channel + cross-layer design -> ADR-0004/v3 + the G0 ledger), then
  a few autonomous build legs against the FIXED walls: the 2026-06-30 kill-gate CHECKPOINT (this leg IS that
  verdict moment) and the 2026-07-24 G3 hard wall (never extended). Each build leg <= a focused half-day
  human-equivalent, one feature smallest-first; split larger at shape. Overnight legs run the dotnet/in-memory
  sustained-load correctness path as the PRIMARY autonomous evidence; the FishNet/PlayMode confirmation is a
  gated checkpoint that may wait for the owner without marking the leg failed. Retries <=2 in-context + 1
  fresh-context per gate, hard cap 3; same finding class twice = non-convergence -> stop + escalate. Escalate
  (the only mid-run owner contact) on: retry budget exhausted, non-convergence, a VERDICT=BLOWN or a
  consistency-cannot-hold finding (the kill-gate trips — the owner decides contingency vs kill, not the
  builder), an out-of-plan decision (new dependency/scope/irreversible/a frozen-constant change), a verdict that
  cannot be reduced to a binary predicate, or a sandbox/permission boundary. Tier-2 actions
  (merge/publish/delete non-versioned) + any new dependency are never auto-approved regardless of PLAN approval.

owner_decisions (decided AT the PLAN — not blocking dispatch):
  1. ADR vehicle: NEW ADR-0004 vs ADR-0003 v3 (C1-C22 untouched either way). Rec: ADR-0004 (a new concern =
     the sustained verdict + LOCK; v-bumping ADR-0003 risks the appearance of re-opening its frozen C1-C22).
  2. Sustained-measurement environment: loopback + software clamps (t-2's env, fast, honesty-caveated) vs a
     real uplink (slower, may eat budget). Rec: loopback + software clamps WITH the honesty boundary stated
     (byte size + per-tick dirty-chunk COUNT are environment-independent; real-link latency/loss is NOT).
  3. Production channel reliability (C7): unreliable-sequenced vs reliable-ordered + the fault model the
     verdict must survive. Rec: PLAN decides on merits + realizes it, promoting t-2's test-decorator
     fault-injection to a gated production property; the steady-rate verdict is measured with it active.
  4. Mid-run late-join: a t-3 GATE or stays bet-2-deferred? Rec: stays bet-2-deferred (default) unless the
     verdict's honesty genuinely requires a join-baseline (record the reason).
  5. Periodic keyframe cadence K (C9): does sustained load FORCE a periodic K (and value), or does
     quiescence-only recovery still suffice? Rec: PLAN decides from the sustained-wave shape; pin
     recovery-under-load either way.
  6. Confirm kill-gate routing in ADR-0004: a p1 failure (consistency cannot hold) -> P6 model/vendor spike;
     a p2 failure (steady rate BLOWN) -> Barotrauma-hybrid contingency; the owner decides contingency-vs-kill
     if the gate trips, not the builder.

surface: |
  Executor leg = a fresh session in the product-repo dev worktree C:\projects\Unity\GasCoopGame_dev; opens with
  an interactive PLAN (owner present, plan mode, frontier model) that freezes ADR-0004/v3 + the default-FAIL G0
  ledger, then autonomous build legs. The closing RESULT.md at repo root (gated by
  `pwsh tools/check.ps1 -Deliver`) routes home to the direction; the OS frames any follow-on.
```
