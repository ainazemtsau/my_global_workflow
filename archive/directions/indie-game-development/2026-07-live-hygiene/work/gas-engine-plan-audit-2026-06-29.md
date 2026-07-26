# Gas-engine plan audit — 2026-06-29 (s-work-029)

Full-plan gap audit triggered by the owner after the buoyancy gap surfaced («раз у нас оказались такие проблемы,
давай сделаем анализ всего плана»). Method: multi-agent audit `wf_59afe6f0-426` — 8 lenses (model→slice coverage,
built-vs-planned, deps/sequencing, open-questions, lock/burial/ADR, player-feel, scope-honesty, cross-track) → each
candidate gap refute-verified against the COMMITTED canon AND the real built code (GasCoopGame origin/main @adb9255) →
synthesis. 70 agents, 53 raised → **37 verified**. This file is the durable record.

## Overall health

The FOUNDATION (50cm near-grid, forced-flow jets, multiplayer-determinism proof) is solid, honestly scoped, decisions
mostly recorded not lost. The big hole is the BRIDGE to the stated jewel: every thing that makes gas FEEL like a character
— multiple gas TYPES, heavy-sinks/light-rises WEIGHT, REACTIONS, gas that HURTS you — is real in the design model but lives
nowhere on the build schedule (all crammed into one open-ended "S6+, later" line). Same shape as the buoyancy gap, repeated
5-6×. Second concern: direction — the planned next step (S3) is far-tier plumbing for big levels that don't exist yet, while
the visible near-gas character work is undecided/unscheduled. Nothing is broken or dangerously hidden — these are gaps of
SEQUENCING and HONEST SIZING, mostly fixable now with planning decisions, not code.

## THEME 1 — The jewel has no road (the big one)

- **No ordered route from today's single grey gas to "characterful gas"** [important, NOW—planning] — types/weight/
  reactions/type-damage/temperature/wind are all dumped in one "S6+, one at a time" line with no order, even though they
  depend on each other (no reactions without 2 types; no type-damage without types). Each surfaces as a surprise priority
  fight (buoyancy = the first). ROOT CAUSE behind the rest of this theme.
- **Buoyancy (heavy sinks / light rises) built nowhere, on no slice** [important, NOW-decide/later-build] — canon §3
  promises weight-drift; code has none (verified); S3 "height" is far-tier plumbing, a different thing. Parked as
  d-buoyancy-near-weight-priority-001, still no slice.
- **The engine carries exactly ONE gas** [important, name-slice-now/build-later] — code hardcodes species=1 (verified).
  Headline "each type feels different" has no 2nd gas to stand on. Arrays are multi-gas-ready (extension, not rewrite), but
  it's only a backlog ellipsis. Load-bearing under types/reactions/type-damage AND the visual character probe.
- **Gas that HURTS you (dose/damage) has no slice** [important, name-now/build-later] — canon makes a firm dose-from-coarse
  promise; no damage code in the new engine (only in the retired legacy tier). The first real reason to CARE about gas is
  unscheduled past S6.
- **Reactions + temperature exist only on the OLD gas; S5/S6 are REBUILDS not "flip a switch"** [watch, size-honestly] —
  breach/temperature/reactions were written mid-June against the retired old system; the new grid has none. Don't budget
  S5/S6 as "turn on existing features."
- **"Blended cell during a reaction" has no data shape, no slice** [minor, later] — needs types+reactions first; pin to that
  future work so it isn't forgotten.

## THEME 2 — Direction risk: next step is big-level plumbing while near-gas waits

- **Next slice = S3 far-room height-plumbing, but you may want near weight first; the call is open** [important, NOW] —
  S3 only matters at ~150 rooms. The near-feel jewel is further back. The buoyancy-vs-far-tier priority is captured
  (d-buoyancy-...) and unanswered. Answer BEFORE any S3 build.
- **S3 would bolt new height layers onto the 2-band code marked for deletion, and runs BEFORE S4 deletes it** [watch,
  PLAN-guard] — the retired "height-bands" idea quietly grows new responsibilities. Decide S3-vs-S4 order (near-buoyancy
  next sidesteps it).
- **S4 is sized like a "body swap" but is really build-far-rep-from-scratch + retire-the-legacy-tier** [watch, size-honestly]
  — collapse/expand is a placeholder copy; two gas systems have never been connected. Not a quick swap.

## THEME 3 — Co-op safety nets & the two-player promise have quiet holes

- **Forced-coop is now FROZEN design, but its engine node was dropped** [important, re-pin NOW] — the signed co-op rule
  (shared gas must force teamwork) has NO engine affordance + the "co-op interdependence proof" node (c-map-004) was pushed
  to a task that was never created/ran. Risk: discovering it as a HARD blocker the day you build the first co-op gas moment.
- **The sync-safety scans skip the far-tier folder (Coarse/)** [important, NOW before S3] — the two determinism scans only
  cover 3 folders; Coarse/ (sync-critical, and S3 adds more there) is skipped → a green build could hide a two-player
  desync. No bad code there today; it's a safety-net hole. Close with a self-test before S3.
- **A determinism decision the canon ordered BEFORE the first force mechanic was skipped** [watch, reserved-danger] —
  S1 shipped jets/wind/valves without the cross-detail-flow number + the player-position fingerprint. Harmless today (pushes
  only move gas); becomes a blocker the moment a mechanic ties a gas-push to a player BODY (displacement, carried emitter).
- **S5 breach can silently desync unless the "which sub-slots are open" bitmap joins the checksum FIRST** [watch, S5-PLAN
  first-action] — today only the COUNT is checksummed; breach makes the SHAPE matter. Canon warns; not yet on the S5 task.
- **The "does the 2nd player feel it?" check is required but never added to the slice checklist** [minor, before first
  gameplay slice] — exists only as a recommendation; never enforced.

## THEME 4 — Honest-labelling: a few "done" labels mean less than they sound

- **The big-room speed trick (sparse-awake) isn't built — the hangar number isn't the real big-hall test** [watch] — every
  cell computes every tick; the "active" register only feeds the checksum, not the math. ~100× claim in doubt under jets.
  Tracked (d-sparse-solver-defer-001); never read a green result as "big halls proven."
- **"S2 Multiplayer done" = a one-machine determinism test; gas isn't sent over the network yet** [watch] — networking code
  has zero mention of the gas field (verified). Real networked gas ~S4. Already honestly named; optional label rename to
  "Lockstep determinism proof (loopback)".
- **"S1 done" does NOT mean a body pushes gas aside — that half was deliberately cut** [watch] — owner-accepted cut
  (d-displacement-s1b-cut-001) with a named re-entry trigger. Just read the label right.
- **The visual track's "two different gases" headline is a FAKED-data demo — the real engine still has one gas** [important,
  NOW before signing the active visual leg] — the lab can show 2 types only via hand-authored fake blobs; fed real sim, both
  collapse to one. Judge the sign-off knowing 2-type character is a PREVIEW until a multi-species engine slice lands.
- **The canon spec is STALE vs what shipped, and the anti-drift rule says to trust the stale text** [important, NOW-cheap] —
  (1) the model section never mentions the forced-flow system (wind/gust/fork/valve/jet) actually shipped in S1; (2) the
  spine still shows S1 as "spawn-burst + body-shove" and S2 as a single "multiplayer" step (S1=forced-flow; S2 split into 2
  delivered). A planning session reading the spec literally would trust the stale text. Cheap to fix.

## THEME 5 — Tidy-up (low-stakes)

- **Fact 4 self-contradicts: canon says chemistry table is "data day-one"; engine has none; schedule puts it S6+** [minor,
  NOW-5min] — reconcile the wording (drop a stub now OR accept reactions-as-later + fix Fact 4).
- **The gas-TYPE data socket the canon promised day-one is missing** [minor, record-now/S6-build] — no per-cell type marker,
  no type slot in the checksum → reaching types (S6) is a real schema add (the migration the canon wanted to avoid), not a
  pure behaviour add. Record the honesty note.
- **Working buoyancy/weight/heat code exists — but only in the far tier S4 will delete** [minor, port-before-delete] — the
  old far-model has 4 species + weight + "heavy sinks/hot rises", proven integer math. Add a one-line note to the buoyancy
  decision: REUSE/port that law before S4 deletes the only copy.
- **The old v1 gas "Layers" demo is now dead code (orphaned), which Fact 6 forbids** [minor, small cleanup leg] — kept
  deliberately + test-covered, but nothing wires it; it confused this very audit (3 gas tiers). Delete next time you touch
  the engine.
- **Two ADR-0012 files (engine S1 forced-flow + visual seam) both on main** [minor, NOW-5min] — decision numbers ambiguous;
  rename one (the visual one pre-wrote the rule).
- **Stale "ADR-0010" lock mentions linger in finished-task text + memory** [minor, next maintenance pass] — the active slice
  (S3) is already correct (ADR-0002); just dead-text find-replace.
- **The player "detail bubble" is a full canon pillar, deferred, but never pinned to a slice — and the hangar fallback leans
  on it** [watch, one-line pin] — two deferred items (bubble + hangar fallback "all-peers-all-bubbles") lean on each other;
  pin the bubble to a slice + record the dependency.

## TOP 5 to act on (from the audit)

1. **Decide priority NOW** — answer buoyancy-vs-far-tier (d-buoyancy-...) before any S3 build. Near weight is visible +
   character-defining + a small near-only slice; S3 is big-level plumbing you don't need yet. Steers the whole next stretch.
2. **Draw the missing "character road"** — decide ONCE the ordered mini-spine: gas TYPES → weight/buoyancy → reactions →
   type-damage/temperature; lift each out of "S6+, one at a time" into named, dependency-tagged slices. Root fix behind ½ the findings.
3. **Name a real multi-gas (TYPES) engine slice** — one gas today; headline has no foundation; visual runs on fake 2-type
   data; reactions/type-damage blocked behind it. Extension, not rewrite — but stop being a backlog ellipsis.
4. **Close the two co-op safety holes before S3** — (a) add Coarse/ to the determinism scans + a self-test; (b) re-pin the
   dropped co-op-interdependence node so the now-FROZEN forced-coop design has an owned engine slice.
5. **Refresh the source-of-truth spec** (cheap, high-leverage) — fold forced-flow into the model section, update the stale
   S1/S2 spine lines, fix Fact 4's contradiction, rename the duplicate ADR-0012. The spec is what every build session must
   trust over its own memory; keeping it ahead of drift is the exact failure this project fights.

END_OF_FILE: live/indie-game-development/work/gas-engine-plan-audit-2026-06-29.md
