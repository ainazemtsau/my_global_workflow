# s-converge-002 — converge resolve (g-9c41): owner signs temperature + destruction + extensibility; bet re-shape routed (option A)

- **date:** 2026-06-14
- **play:** converge (resolve movement)
- **node:** g-9c41
- **input:** owner voice over several turns → confirmed R1–R13 + "да, A"
- **role:** session → became its own writer after RESULT (agent-CLI on this repo)

## What the owner resolved (G7 sign-off)

Three open design questions closed in his own words (full text in work/converge-g-9c41.md §RESOLVED):
- **Temperature** = a thin DYNAMIC layer in the core (own structure + minimal sim, sibling of gas, on the
  grid event bus, subscribes to events) — to PROVE layer-extensibility + cross-system interaction, NOT for
  gameplay (that's g-d3a8). Not static. (R1–R6)
- **Destruction** = real but CONTROLLED, LOCAL breach (explosion/player → hole → topology change → gas
  flows); no scripted breach, no collapse/structural physics; shards deferred. Maps onto the designed
  "add a breach portal to immutable volumes" — only the trigger changes. (R7–R10)
- **Extensibility** = build extensible SEAMS, minimal IMPLEMENTATIONS now (no future functionality early —
  protects G3 / 24.07). Already the architecture's spine. (R11–R13)

These re-shape what the bet must prove. Owner approved the DIRECTION ("да, A"); the specific re-shaped
done_when needs G9 in-session approval → routed to shape c-shape-004 (drafted in next).

## RESULT

```yaml
RESULT s-converge-002 (call: converge resolve, g-9c41)
direction: indie-game-development   play: converge   node/task: g-9c41 (resolve checkpoint)
outcome: |
  Three design questions in the g-9c41 converge set are owner-signed and recorded as RESOLVED-1/2/3 in
  work/converge-g-9c41.md: temperature = thin dynamic LAYER (not static, not gameplay), destruction = real
  CONTROLLED breach→topology (not scripted, not collapse), extensibility = extensible seams + minimal impls.
  Added glossary term G:temperature; superseded I21's static-temperature + scripted-breach clauses; §SIGNOFF
  → partial. The owner approved option A (the bet's job becomes "prove a minimal-but-REAL layered
  architecture over the network": gas + thin temperature layer + real controlled destruction-topology,
  extensible seams, network-first). The specific bet re-shape is drafted as a card and routed to shape
  c-shape-004 for G9 approval; the bet/tasks/c-exec-003 are UNCHANGED until then.
evidence: |
  work/converge-g-9c41.md §RESOLVED-1/2/3 + §SIGNOFF (owner words "да, A" + R1–R13); G:temperature row;
  I21 annotated PARTIALLY SUPERSEDED. Grounding cited from brief §3.2 (reactions read a temperature window +
  carry enthalpy → temperature↔reactions loop), §3.7 (topology change = breach portal on immutable volumes),
  §3.8 (why static was chosen). Reaction CONTENT confirmed deferred to g-d3a8 (brief line: "Реакции —
  отложены в дизайн") — so nothing about reactions/temperature was decided behind the owner.
state_changes: |
  PRODUCT: work/converge-g-9c41.md — + G:temperature; + §RESOLVED-1/2/3; §SIGNOFF Resolve → PARTIAL;
    I21 annotated (partial supersede). (LOG END_OF_FILE trailer restored — dropped in an earlier edit.)
  NOW.md: open_calls += c-shape-004 (queued — re-shape g-9c41 bet under option A, G9 in-session). active_bet,
    active_tasks (t-1/t-2/t-3), c-exec-003, NOW.next UNCHANGED (re-shape applies only on c-shape-004 approval).
  LOG.md: + converge-resolve line → history/s-converge-002.md (+ restored END_OF_FILE trailer).
  history/: + s-converge-002.md.
captures:
  - "reaction CONTENT (which gases react, the role of temperature, hysteresis windows) is g-d3a8 design (parked); the brief proposed temperature-in-reactions from SS13/SS14 precedent — a research proposal, NOT an owner decision. Surfaced to the owner; not lost (lives in the brief for g-d3a8 to consume)."
  - "owner's governing core principle (record for shape + future nodes): extensible SEAMS, minimal IMPLEMENTATIONS now — the YAGNI/extensibility balance; do not gold-plate future functionality against the fixed appetite."
decisions_needed:
  - id: d-converge-001
    status: answered (A)   # carried — already resolved at s-decide-002
  # the re-shape's specific done_when is a G9 in-session approval (c-shape-004), not a decision_inbox item
play_check:
  - "resolve: done — temperature/destruction/extensibility signed by the owner (his words), recorded §RESOLVED-1/2/3; G:temperature added; I21 superseded-in-part; §SIGNOFF Resolve → PARTIAL."
  - "grounding: done — checked the brief before answering (why static §3.8; reactions §3.2 deferred-to-design; topology §3.7); owner's worry about smuggled/stale data answered honestly (temperature-in-reactions = a research proposal, not his decision)."
  - "route: re-shape is owner-approved in DIRECTION (A) but its done_when needs G9 in-session approval → c-shape-004 drafted (next); bet untouched until approved."
log: "2026-06-14 — converge resolve (g-9c41, s-converge-002): owner signed temperature (thin dynamic layer), destruction (real controlled breach, no scripted/collapse), extensibility (extensible seams + minimal impls) into work/converge-g-9c41.md §RESOLVED-1/2/3; G:temperature added; I21 superseded-in-part. Approved option A → bet re-shape (core proves minimal-but-real layered architecture over net) routed to shape c-shape-004 (G9). Bet/c-exec-003 unchanged until approved. → history/s-converge-002.md"
next: |
  CALL c-shape-004 — RE-SHAPE CARD (g-9c41 bet, option A) — owner G9 approval required before apply.
  to: session   play: shape   node: g-9c41
  proposed_bet_goal: |
    Core proves a MINIMAL-but-REAL layered architecture over the network: the seam carries multiple
    system-layers (gas + a thin temperature layer), they interact via grid events, a real controlled
    wall-breach changes topology and gas flows — all networked-consistent and on EXTENSIBLE seams.
    (Was: "networked chunked-delta spike on a toy field".)
  proposed_done_when_delta (over the current bet done_when): |
    1. (unchanged) chunked-delta stream LOCKED: 2 clients reconstruct, consistency across the breach
       (kill-gate "A"). Network-first — riskiest dies first.
    2. (new) the seam is proven MULTI-LAYER: the stream carries >=2 independent layers (gas + a thin
       temperature scalar), both reconstructed consistently. Cheapest insurance vs the most expensive
       core mistake (R12); the layer registry (C21) + revision feed (C12) already exist in the contracts.
    3. (changed) REAL controlled breach: a destructible wall is breached (explosion/player) -> hole ->
       topology change (a breach portal) -> gas flows; no scripted, no collapse (RESOLVED-2). Replaces
       the "scripted breach" stand-in; same designed topology mechanism (brief §3.7), real trigger.
    4. (new) cross-layer interaction visible: a reaction/heat event -> the temperature layer responds
       (RESOLVED-1/R4/R5) — trivial sims, real seam.
    5. (new) everything on EXTENSIBLE seams (RESOLVED-3): a new layer/driver plugs in without core edits
       (proven by temperature being added as the 2nd layer through the same seam).
    6. (unchanged) min-spec budget, harness, debug surfaces, reproducibility.
  proposed_task_staging (network-first preserved): |
    - t-1 (done) — unchanged (engine-free 3-mode core + networked handshake).
    - t-2 (in flight, c-exec-003) — stays the stream-LOCK spike; widen the toy field to carry >=2 trivial
      layers (gas + a constant/near-trivial temperature scalar) to prove the seam is multi-layer (cheap —
      the registry is already its job). Breach = the topology-change test. Real temperature DYNAMICS +
      cross-layer interaction stay out of t-2.
    - t-3 — re-framed from "breach-load only" to "the layered-architecture proof on the LOCKED stream":
      real controlled wall-breach -> topology -> both layers react + cross-layer event (reaction heat ->
      temperature), networked-consistent, extensible seams.
  honest_trades (G3 — appetite FIXED 2026-07-24, re-SHAPE not extend): |
    - sims stay TRIVIAL (temperature = scalar rise/decay; gas = toy diffusion; ONE destructible wall).
      Real band sim / real gas types / reaction CONTENT / real visual stay cut to bet-2 / g-d3a8.
    - ⚠ CLIP RISK (criteria 6/8, target ~2026-07-10): adding the 2nd layer + real breach may push the
      first spectacular clip. Shape decides: clip slips slightly, OR something else tightens. THIS is the
      main trade to settle in-session.
  done_when (of c-shape-004): owner-approved re-shaped bet done_when + task staging + a real cut list
    (G6); TREE/NOW updated under G9 (owner_approved); c-exec-003 heads-up issued if t-2 framing shifts.
  surface: claude or cli; the heavy shape can use the multi-agent rigor.
```

END_OF_FILE: live/indie-game-development/history/s-converge-002.md
