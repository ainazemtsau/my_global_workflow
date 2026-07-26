# Review: sim (g-9c41) + visual (g-7e15) plans — 2026-07-02

Owner-requested direction review (sim + visual tracks only). Method: multi-agent workflow `wf_ea65be05-e09`
(33 agents: 4 deep readers — SPEC / sim CALLs / visual docs / product-repo ground truth → 5 critics by lens
→ adversarial verify of every high/medium finding against the files). 38 raised → 24 verified (**0 refuted**)
+ 4 low hygiene. This file is the durable record; per-finding file:line evidence lives in the workflow
transcript (session-temp) and is summarized here.

## Headline verdicts

1. **State drift (both tracks), CONFIRMED:** NOW.md claimed both CALLs «await execution» while c-exec-022
   (Sc-rep) was already BUILT (82 staged files, +7020/−427, UNCOMMITTED, RESULT.md «DELIVERED», no fresh G5)
   and c-visual-003 W1a was already EXECUTED on dev2 (7 commits, owner-eye tuning, finding «demo level needs
   design»). Fixed 2026-07-02: owner checkpointed dev @adc3b9d + dev2 @d25b0b2; OS reconciled
   (s-repair-review-reconcile-001). Root pattern = executor legs skipping the owner-present PLAN + RESULT
   never routed home + parallel Codex review-fix sessions piling more uncommitted changes (loop stopped by
   owner 2026-07-02).
2. **Sc-rep does not deliver sparse-awake (CONFIRMED, then MEASURED):** the tick kernel still expands the
   sparse store into dense per-species planes every tick (OldMassScratch/CopyPlane over ALL cells per
   registered species → dense face-flow → rebuild sparse). Real measurement (dev @8db3ee1): hangar 196k cells,
   active CONSTANT 1,562 — 18 ms/tick @roster-1 → 587 ms @roster-64 (~9 ms per registered type; roster-128
   ≈ 1.16 s vs the 50–100 ms budget; weak peer 2–4× worse). No slice gate binds tick cost (cache-shape/GC-zero/
   byte-identical all bind the STORE). Honest Sc-rep scope = representation + checksum schema.
   → d-sparse-tick-kernel-001 (Sc-kernel BEFORE reactions), draft work/c-exec-023-draft-call.md.
3. **Hangar gate was vacuous (CONFIRMED):** the recorded artifact was active_cells=128 (the golden's cell
   count, a stand-in) — the SPEC §6 п.3 «single unmeasured number» stayed unmeasured while the 07-05 de-risk
   wall was keyed to it. Fixed: real measurement taken 2026-07-02 → the wall FIRED (see #2).
4. **LOUD THROW co-residency bomb (PARTIAL→held):** K=3 overlay (max 4 co-resident types/cell); a 5th type
   arriving via ordinary flow throws in the normal tick commit → deterministic ALL-PEER halt under lockstep.
   Owner-signed and correct for Sc-rep itself, but its defusal was a CIRCULAR pointer (c-022 → «reactions
   design later», c-021 banner 7b → «the same surface Sc-rep decides»). Fixed: named fork added to the
   c-exec-021 shape agenda (banner item 13) + adversarial 5-type-junction RED required.
5. **Review-repair semantic drift inside Sc-rep (PARTIAL):** repairs changed shipped S1 behavior (forced-flow
   destination back-pressure, temperature saturation) outside the tiny golden's coverage. Mitigation verified:
   the back-pressure repair enforces the SPEC's KEPT capacity law (d-roomfull-001) that shipped S1 violated;
   disclosed in RESULT; full S1 RW1-RW10 battery re-ran green. Residual: binding fresh G5 must audit the
   repair diffs against the S1/c-exec-015 oracles explicitly.
6. **Visual W1b targets a non-existent read-path (CONFIRMED):** «G channel = real dominantTypeId» — no such
   path on dense (RealGasViewSource hardcodes G=0/TypeCount=1; dense has no per-cell dominant id); the real
   provider is Sc-rep's STAMP, consumed by zero adapters; c-exec-022 forbade visual hookup. Fixed: W1b
   re-scoped (banner on c-visual-003) — after Sc-rep merge + a small owner-acked engine read-API.
7. **«Finer grid near player» is on NO engine slice (CONFIRMED):** the wave-plan's «(g-9c41 roadmap)» wording
   hid it. Render levers buy sub-cell RICHNESS, not SILHOUETTE. → d-finer-grid-fork-001 (owner).
8. **Schedule findings:** 08-31 Steam-page prerequisites all on PARKED nodes, no wake dates (a ready
   marketing restart CALL exists, undated) → d-marketing-wake-001. Oct-5 demo has NO road (nothing between
   Sc-damage and a submittable co-op demo; networked gas parked ~S4) → d-demo-road-001. The 10-05 wishlist
   gate is near-predetermined toward «below» (owner's own q-foundation anchor ~1–3k vs the 7–10k bar) —
   surface, don't imply Oct EA is likely. 07-24 milestone wording was stale («Waves A→B») — fixed in NOW.
9. **Huge-levels promise (TREE #9) has no surviving path (PARTIAL):** only S4 rollup can carry ~12.8M cells
   (~64× weak-core ceiling); S4 deferral undated; «smaller levels» fallback = silent canon drop.
   → d-biglevels-tree9-001 (owner).
10. **Coherence/hygiene (fixed this session where additive):** ADR numbering fiction (repo = namespaced
    ADR-P-0001 / Sc-rep = ADR-E-0001; OS docs asserted flat 0021/0022 — banners corrected; standing rule:
    OS docs never pre-assign ADR numbers); c-exec-021 = two-generation palimpsest (corrections added,
    rewrite-at-shape required, incl. stale checksum-bit 1<<6 and contract v8); wave2 knowledge files lacked
    the redirect banners SPEC §9 claims (added; gload-probes probe-3 «fine-grain co-location before
    detonation» is INVERTED by SPEC §3 — flagged); locked-slices banner extended (ADR-0010 citation, old
    Fact-4 wording); TREE g-9c41 marked read-through-SPEC + consolidation queued; Coarse/ scan-root hole
    folded into the Sc-kernel draft.

## Also verified as GOOD (for honesty)

Velocity exceptional (7 engine merges 06-26..06-30; Sc-rep built in a day). Gate discipline + adversarial
hardening genuinely working (0 of 24 findings refuted ≠ sloppy criticism — every claim survived file-level
refutation). Road order (representation before reactions) correct. Visual re-plan (judge on the real sim,
never-worse, one control panel) sound — W1a produced a real owner-tuned result + a useful finding.

## Dispositions

- Fixed in this session (s-repair-review-reconcile-001): state reconciliation (NOW/calls/banners), real
  hangar measurement recorded (product dev @8db3ee1), knowledge redirect banners, ADR corrections,
  c-exec-021 shape agenda additions, W1b re-scope, wave-plan honesty note, TREE note.
- Owner decisions queued in NOW.decisions: d-sparse-tick-kernel-001 (**the big one**), d-finer-grid-fork-001,
  d-demo-road-001, d-marketing-wake-001, d-biglevels-tree9-001.
- Remaining process steps: fresh-session G5 on Sc-rep → owner-eye → owner-gated merge; then Sc-kernel (if
  signed); then c-exec-021 shape with banner items 11-14; then W1a sign + W1b.
- Queued (owner-present, not this session): TREE g-9c41 node consolidation; SPEC §1 one-line ADR-namespace
  note; os/** standing-rule change (maintenance-gated) if the owner wants the ADR rule OS-wide.

END_OF_FILE: live/indie-game-development/work/review-gas-sim-visual-2026-07-02.md
