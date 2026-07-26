# s-work-038 — Sc-kernel FRAMED + G9 SPEC batch (2026-07-02)

Direction: indie-game-development / g-9c41 / Sc-kernel · play: work · owner present.

## Readable summary

Framed the Sc-kernel executor CALL **c-exec-023** (engine-only: re-point the authoritative gas tick at the sparse
store / active cells so per-tick cost scales with ACTIVE cells, not registered roster × domain cells; behavior
byte-identical to post-Sc-rep; determinism ADR-0002). Consumed the 2026-07-02 sim-plan audit §Package **item-4**
additions (a–k) into the CALL and ran the batched **G9 SPEC touch** (item 8, S1–S10). A standard adversarial
hardening pass (wf_ff1612b9-ec5, 6 diverse-lens finders → per-finding adversarial verify) raised 11, confirmed 2
(both P2, folded), refuted 9. Owner reviewed the full decision brief and signed **«все подтверждаю»** — the binding
G9 signature on the exact SPEC edits + kill_by. Applied as writer and committed.

Two P2 folds:
- **wake round-trip RED** — Sc-kernel introduces byte-sleep/wake as NEW behavior; no gate forced a sleep→wake
  correctness test, so a cell could byte-sleep and never re-wake on incoming flux/breach/impulse (silent R2 «sim
  everywhere» violation) while every other gate passed. Added a leg1 RED: settle→sleep→re-wake byte-identical to the
  retained dense oracle; planted "slept cell ignores incoming flux/breach/impulse" MUST trip. RESERVED wake rows stay
  seam-only.
- **frozen-visual honesty** (audit words-vs-docs-006) — the 07-24 milestone bullet over-claimed the frozen visual
  (W1b / two-type visual) as a live carrier. Corrected: while visual is on hold the SOLE live player-facing terminus
  = Sc-reactions telegraph+bang; the frozen visual is not cited as an anti-tunnel counterweight (R7 unchanged).

Also re-pinned the **richness ladder** decision (d-gas-richness-tiers-001, the audit's single P1 — dropped at the
06-29 compaction) with the lock-name correction folded (TIER-3 reopens the no-stored-velocity REPRESENTATION
boundary, NOT the netcode lock ADR-0002), and created **d-hangar-flood-fallback-001** (armed-dormant; auto-opens
only if the Sc-kernel flooded-hangar capture is over the weak-peer budget).

kill_by = **2026-07-16** (leg1 checkpoint): if roster-independence (≤~20% roster-1-vs-64 hangar delta) or
byte-identity can't hold with a sparse kernel → KILL + re-shape, no silent rebaseline, no appetite extension.
A flooded-over-budget number is NOT a kill (opens d-hangar-flood-fallback-001).

Next = a fresh GasCoopGame_dev executor session opens c-exec-023 with an owner-present PLAN (base = GasCoopGame main
@5442be0). The Sc-kernel RESULT fills the SPEC §6 п.2 LEVEL-DESIGN CONTRACT ceiling number. c-exec-021 (Sc-reactions)
re-shape prep may start in parallel; it does not fire until Sc-kernel GREEN.

## RESULT

```yaml
RESULT s-work-038:
  direction: indie-game-development
  play: work
  node: g-9c41
  task: Sc-kernel
  outcome: |
    Sc-kernel executor CALL c-exec-023 FRAMED + HARDENED (owner present) and issued into open_calls; the 2026-07-02
    sim-plan audit §Package item-4 additions (a–k) folded into the CALL; the batched G9 SPEC touch (item 8, S1–S10)
    applied to knowledge/g9c41-gas-engine-SPEC.md under owner signature «все подтверждаю»; the audit's single P1
    (dropped richness ladder) repaired by re-pinning d-gas-richness-tiers-001 with the lock-name correction;
    d-hangar-flood-fallback-001 created armed-dormant; kill_by set 2026-07-16. Standard adversarial hardening run
    (wf_ff1612b9-ec5: 11 raised → 2 P2 confirmed+folded, 9 refuted). No lock reopened, no gate weakened, no TREE edit,
    zero new build slices before reactions — everything additive.
  evidence:
    - work/c-exec-023-call.md (framed + hardened CALL; approach token active-front-tick-kernel-over-sparse-store; 10 done_when; kill_by; JEWEL GUARD)
    - knowledge/g9c41-gas-engine-SPEC.md (G9 batch S1–S10 applied; provenance banner under "Дата сборки"; §3 lock-name separation; §5 S3/S4/S5 lines; §6 п.2 contract + п.3 Burst/Jobs→engine-free + fallback reorder + п.4 strata + п.9 richness ladder + п.10 cross-type capacity)
    - NOW.md (task Sc-kernel → framed-awaiting-executor + kill_by; open_calls += c-exec-023; decisions += d-gas-richness-tiers-001 [re-pin] + d-hangar-flood-fallback-001; next rewritten; current_truth + history_pointers + next_slices updated)
    - hardening workflow wf_ff1612b9-ec5 (6 lenses × adversarial verify; 2 P2 folded: wake round-trip RED, frozen-visual honesty)
  state_changes:
    - "work/c-exec-023-call.md: CREATED (framed + hardened Sc-kernel executor CALL)."
    - "work/c-exec-023-draft-call.md: SUPERSEDED banner added (points to the framed CALL; kept as history)."
    - "knowledge/g9c41-gas-engine-SPEC.md: provenance banner + G9 batch S1–S10 (all additive; details above). owner_approved: «все подтверждаю» 2026-07-02."
    - "NOW.md task Sc-kernel: status signed-awaiting-framing → framed-awaiting-executor; done_when → framed battery (work/c-exec-023-call.md); kill_by added (2026-07-16); status_note updated."
    - "NOW.md open_calls: += c-exec-023 (to executor, for g-9c41/Sc-kernel, issued 2026-07-02)."
    - "NOW.md decisions: += d-gas-richness-tiers-001 (RE-PINNED, P1 fix, lock-name corrected); += d-hangar-flood-fallback-001 (armed-dormant)."
    - "NOW.md next_slices[0]: draft-call pointer → framed work/c-exec-023-call.md."
    - "NOW.md bet.current_truth: appended s-work-038 framing note."
    - "NOW.md next: rewritten (fresh GasCoopGame_dev executor PLAN; c-exec-021 prep parallel; visual-hold honesty note)."
    - "NOW.md history_pointers: += sim-plan audit + Sc-kernel framing pointers."
    - "LOG.md: appended s-work-038 line."
    - "history/2026-07-02-s-work-038-sc-kernel-framed.md: CREATED (this file)."
  captures: []
  decisions_needed:
    - "None new this session. Standing pending (unchanged): d-finer-grid-fork-001 (dormant while visual on hold), d-marketing-wake-001, d-coop-interdependence-repin-001. d-hangar-flood-fallback-001 is armed-dormant (owner acts only if the Sc-kernel flooded capture is over budget)."
  play_check:
    - "1 Recite: DONE — restated Sc-kernel goal/done_when + the g-9c41 bet it serves."
    - "2 Owner inputs (owner): DONE — owner-content = the exact G9 SPEC edits (S1–S10) + kill_by; presented as a full readable Russian decision brief; owner signed «все подтверждаю» (binding G9 signature + kill_by 2026-07-16 confirmed). The audit package shape was pre-approved «да по всем 4 пунктам»; this session collected the signature on the concrete text."
    - "3 Do the work: DONE — framed c-exec-023 (call:executor), folded audit item-4 (a–k), ran the standard adversarial hardening pass (wf_ff1612b9-ec5), drafted the G9 SPEC batch (S1–S10)."
    - "4 Self-check: DONE — done_when vs audit item-4 a–k checked point-by-point; 2 confirmed hardening findings folded (wake round-trip RED, frozen-visual honesty); 9 refuted (anchor conventions / already-bound gates)."
    - "5 Close: DONE — this RESULT; next = c-exec-023 executor CALL. Task Sc-kernel stays active (framed-awaiting-executor); NOT the last task of the bet, so next is an executor CALL, not review."
  log: "work (g-9c41/Sc-kernel; s-work-038): Sc-kernel FRAMED + HARDENED as c-exec-023 (audit item-4 folded, adversarial pass 11→2 P2 folded/9 refuted) + G9 SPEC batch S1–S10 SIGNED «все подтверждаю»; d-gas-richness-tiers-001 re-pinned (P1), d-hangar-flood-fallback-001 armed; kill_by 2026-07-16; next = fresh GasCoopGame_dev executor PLAN."
  next:
    call: c-exec-023
    to: executor
    for: g-9c41 / Sc-kernel
    where: a FRESH C:\projects\Unity\GasCoopGame_dev session (base = GasCoopGame main @5442be0)
    goal: "The authoritative gas tick computes over the sparse store / active cells directly (cost ∝ active cells, not roster × domain cells), behavior byte-identical to post-Sc-rep goldens, determinism preserved — per the full packet work/c-exec-023-call.md."
    open_with: "an owner-present PLAN (the c-exec-022 PLAN deviation must not repeat)."
    note: "On GREEN → re-harden + fire the held c-exec-021 (Sc-reactions). dev→main merge + push owner-gated. c-exec-021 re-shape PREP may run in parallel now."
```

END_OF_FILE: live/indie-game-development/history/2026-07-02-s-work-038-sc-kernel-framed.md
