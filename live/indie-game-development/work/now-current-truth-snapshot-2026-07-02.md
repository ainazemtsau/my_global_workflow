# NOW.md bet.current_truth — pre-repair snapshot (2026-07-02)

Verbatim copy of `live/indie-game-development/NOW.md`'s `bet.current_truth` field (81 lines) before the
2026-07-02 hot-state hygiene repair collapsed it to a short summary + pointer. Saved because this content
was original synthesis, not duplicated anywhere else in `history/`.

---

Sc-types AND Sc-weight delivered + merged (GasCoopGame origin/main @61b7923, --no-ff;
history/s-work-031.md + s-work-033.md). 2026-06-30 OWNER DESIGN PASS (s-design-gas-core-001)
LOCKED gas representation = sparse-dominant + env-derived dynamic typing + condition-waves.
The road RE-SHAPED 2026-06-30 (s-reshape-sparse-dominant-001, owner present, G9 + 3 forks
resolved): a NEW slice **Sc-rep** (re-represent dense→sparse-dominant + per-cell dominant-type
STAMP socket + preserve the collapse/expand seam + the FIRST hangar measurement) is shaped (G6)
and inserted AFTER Sc-weight, BEFORE Sc-reactions — it is now the active task (full shaped card:
work/character-road-shape-2026-06-29.md §SLICE Sc-rep). SPEC edited with owner G9: Факт-4
representation RESOLVED = sparse-dominant; §5 records the env-derived dynamic-typing core
requirement; §6 п.3 hangar re-homed to Sc-rep; §9.5 checksum-member list extended (stamp +
overlay, cell-keyed). Shape drafts adversarially vetted (workflow wf_967a4625-2a4: 29 findings →
24 survived → folded; 5 refuted). Sc-reactions / c-exec-021 is HELD + RE-SCOPED onto
sparse-dominant (work/c-exec-021-call.md banner: mix-overlay section rewritten, outcome-registry
kept OFF the Wave-2-LOCKED GridEvent bus, dense→sparse §Re-sync touchpoints listed, forks +
full re-hardening deferred to its shape; ADR shifts — Sc-rep=ADR-0021, c-021=next-free≈0022,
verify at tip). Owner forks resolved (took recommendations): (1) accept ~1-slice milestone tail
move (honest: 4th consecutive engine-only slice — pre-mortem-#2 tunnel; g-7e15 visual is the
parallel player-facing surface); (2) cell overflow (>K co-resident types) = LOUD THROW at the
representation (mass conserved, no silent loss; declared-sink is a reactions-design choice later);
(3) roster size = config, ~128 a suggested start, tunable without SPEC re-sign. 2026-07-01
(s-work-035): the Sc-rep executor CALL c-exec-022 is FRAMED + adversarially HARDENED as
work/c-exec-022-call.md, with §Re-sync v8→v9 first, named approach token, full Sc-rep gate
battery, v9 escape-class registry walk, and STOP discipline against dense fallback / hashmap /
silent overflow / dev2 edits. Sc-rep stays active awaiting the GasCoopGame_dev executor return.
2026-07-02 REVIEW + RECONCILE (s-repair-review-reconcile-001; durable review record =
work/review-gas-sim-visual-2026-07-02.md, 24/24 findings verified, 0 refuted): Sc-rep was EXECUTED 2026-07-01 in
GasCoopGame_dev WITHOUT the owner-present PLAN this CALL mandates (deviation, recorded) and sat UNCOMMITTED; the
owner checkpointed it = dev @adc3b9d. A REAL hangar measurement was then taken (dev @8db3ee1,
docs/measurements/sc-rep-hangar-real-measurement-2026-07-02.md): tick cost scales ~linearly with REGISTERED roster
(~9 ms/type at the 196k-cell hangar; roster-64 = 587 ms/tick avg; roster-128 extrapolates ≈1.16 s vs the 50–100 ms
tick budget; active cells CONSTANT at 1,562) — the tick kernel still expands sparse→dense per-species planes every
tick, so Sc-rep's honest scope = REPRESENTATION + CHECKSUM SCHEMA (the sparse-awake perf rationale is NOT delivered
by it). De-risk-wall verdict (kill_by 07-05): the wall FIRED correctly → recommendation = insert slice Sc-kernel
(active-front tick iteration) BEFORE Sc-reactions (d-sparse-tick-kernel-001 — SIGNED «да» by the owner
2026-07-02; draft CALL = work/c-exec-023-draft-call.md). Sc-rep remaining after the 2026-07-02 binding fresh G5
(COULD-NOT-REFUTE; one P2 test-gap — field-level storage guard — folded into Sc-kernel done_when): owner-eye →
owner-gated dev→main merge. VISUAL: c-visual-003 W1a CLOSED 2026-07-02 — owner-eye SIGNED WITH RESERVATIONS
(dev2 @40b94cc): foundation accepted, clean LP1–LP5 moves to a DESIGNED gas-demo-scene leg (next visual leg,
→ c-visual-004); W1b re-scoped (after the Sc-rep merge + a small owner-acked stamp read-API — see the CALL
banner). The Codex review-fix loop was STOPPED by the owner 2026-07-02 (fixes return via the normal contour
after G5).
2026-07-02 MERGED + PUSHED (s-work-037): Sc-rep + W1a merged to GasCoopGame main (origin/main @5442be0;
merges efaa6eb + b5675ea; conflicts resolved: RESULT.md = latest-merged-leg, Packages/config = dev superset;
one pre-pushed origin commit 2d85442 folded — content already contained). Full gate battery GREEN on merged
main FIRST-HAND: 1227/1227 headless + hygiene + zero-float/int-overflow/type-hardcode scans. (A 20-error
adapter-build scare = FALSE alarm: the root csproj files are Unity-generated, gitignored, and stale in the
main worktree — they regenerate on the next Editor open.) Owner's local package-manager edits parked in a
git stash on main. OWNER DIRECTIVE 2026-07-02: VISUAL track ON HOLD — «сначала разобраться с симуляцией»;
c-visual-004 NOT framed. Road position: Sc-rep CLOSED → next active work = frame Sc-kernel (c-exec-023).
2026-07-02 (later) SIM-PLAN AUDIT (s-research-gas-sim-plan-audit-001, owner-requested, his requirement
ladder given in-chat and binding over docs): 46-agent workflow wf_a299ecef-44e — 35 findings raised →
34 verified (1 refuted), ONE P1 (the TIER-1/2/3 richness escalation ladder — the plan's own answer to R1
«очень правдоподобно у игрока» — dropped from live state at the 06-29 NOW compaction; plan silently
plateaus at TIER-1 ~2:1 jets); 3 architect packages judged → richness-first ADOPTED-pending-owner.
Durable record = work/audit-gas-sim-plan-2026-07-02.md. Core verdict: architecture + both locks + the
signed road are CORRECT for the owner ladder (lockstep verdict rationale recorded; HELD clouds draft
stays held) — all fixes are ADDITIVE re-pins / gate extensions / dated-owned triggers, zero new build
slices before reactions. Decision batch d-simaudit-package-001 queued (+ d-biglevels-tree9-001 and
d-finer-grid-fork-001 texts broadened per the audit); the c-exec-023 framing MUST consume the audit's
§Package item 4 additions. 2026-07-02 (latest): the audit batch is DECIDED — owner «да» по всем 4
пунктам (package whole w/ 001b corrections; layered mass-conserving overflow; blast wave =
gameplay-load-bearing «как и остальные реакции»; July demo-road shape 07-10..15). d-biglevels-tree9-001
DECIDED (option 3 revised: huge-levels ambition KEPT, S4 dated triggers, squeeze only on measured
impossibility). Pre-decisions for the Sc-reactions shape recorded in the c-exec-021 note (items 15-17).
2026-07-02 (s-work-038): Sc-kernel FRAMED + HARDENED as work/c-exec-023-call.md — audit §Package item-4
additions (a–k) folded + a standard adversarial pass (wf_ff1612b9-ec5: 11→2 P2 folded [wake round-trip RED;
frozen-visual honesty], 9 refuted) + the batched G9 SPEC touch (item 8, S1–S10) SIGNED «все подтверждаю» in the
same session; d-gas-richness-tiers-001 RE-PINNED (P1), d-hangar-flood-fallback-001 armed-dormant, kill_by
2026-07-16. Road unchanged: next work = a fresh GasCoopGame_dev executor session opens c-exec-023 (owner-present
PLAN, base main @5442be0); the RESULT fills the SPEC §6 п.2 ceiling number.
2026-07-02 (s-shape-prep-screactions-001, owner present): the Sc-reactions PREP ran PARALLEL to the Sc-kernel
executor leg (per NOW.next license): shape forks (a)–(f) CLOSED with the owner in-session, and the c-exec-021
body was FULLY REWRITTEN at work/c-exec-021-call.md onto the current base (sparse-dominant, post-Sc-kernel) —
both banner generations retired into it, prior hardening kept as principle, rewrite adversarially checked vs
STATE (wf_8ab4a0cb-401: 36 raised → 10 machine-verified + 26 first-hand-adjudicated → ~22 distinct defects
folded, 0 construction-breaking). Key owner reframe: any-N ZONE mixing = the requirement, per-cell K = internal
config constant (the «5-газов не бывает» framing retired); old ReactionLayer demo tier = DELETE via
owner-pre-signed live-spec amendment (scoped: demo files + their SHALL lines only; bus/enum stays locked).
Sc-typing homed as the NAMED slice after Sc-reactions (accumulate-with-hysteresis). c-exec-021 = prepped,
awaits Sc-kernel GREEN to re-harden+fire. G1 untouched: Sc-kernel stays the active task.

END_OF_FILE: live/indie-game-development/work/now-current-truth-snapshot-2026-07-02.md
