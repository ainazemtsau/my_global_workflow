# RESULT — s-work-033 (work: apply c-exec-020 Sc-weight RESULT; close slice; roll to Sc-reactions)

play: work · bet: g-9c41 (CHARACTER ROAD) · task: Sc-weight · date: 2026-06-30

## outcome

The CHARACTER ROAD's slice 2 — **Sc-weight (per-type vertical buoyancy: heavy SINKS / light RISES / neutral NO-drift,
a CREEPING integer Z-face bias, ENGINE-ONLY)** — is DELIVERED, merged, and pushed (GasCoopGame main @61b7923), and
**closed against all 10 done_when with a BINDING fresh-session G5 = COULD-NOT-REFUTE**. Sc-weight → done;
c-exec-020 → delivered; the bet rolls to **Sc-reactions** (parked→active; CALL c-exec-021 to be framed in a fresh
OS session — the builder does NOT author it). G1 intact (1 active task). No TREE/CHARTER change (G9 untouched).

## evidence

Reconciled the executor RESULT against work/c-exec-020-call.md's 10 done_when (the writer-held independent copy):
every bullet carries a named disposition; the recorded `approach:` = `per-type-buoyancy-bias-creeping-front` MATCHES
the CALL's mandated token (data, NOT a sort); both RESULT amendments carry real owner-ack tokens (test-assertion
correction; P1#3 documentation) — no fabricated approval, no unowned cut.

Verified FIRST-HAND (not on the executor's word):
- GasCoopGame main @61b7923 is the real Sc-weight merge; chain EXEC 95629be → PLAN d265607 → base Sc-types 7d08882.
- The merge is ENGINE-ONLY (5 Core files + scan + ADR-0019/openspec/mutation + 6 ScWeight* tests + additive engine
  debug scene); ZERO deletions; the parallel dev2 VISUAL track (LabGasViewSource.cs, LabGasField.cs, ADR-0016) is
  PRESENT + unmodified on main — boundary held (the raw EXEC-diff deletions were a cross-branch artifact).

BINDING fresh-session G5 (wf_ea71e2d6-f1c — separate from the EXEC session; the EXEC's Sonnet G5 was a same-session
pre-pass): 6 adversarial seam-refuters + a live gate-runner + a referee over the MERGED code. Verdict =
PASS_COULD_NOT_REFUTE on all 10 seams (buoyancy-creeps-not-sorts · settles-against-the-true-kpEff-term · no-pop ·
conserves-mass · carry-clean · data-driven-no-dispatch · weight-override-folded-into-ContentHash ·
per-tick-checksum-derived-sound · ports-the-law-not-CoarseBandStep's-sort · single-type-no-regression) + headless-gate
+ visual-track-boundary; zero blocking findings. Referee re-verified independently: buoyancy adds per open Z-face →
face-adjacency ⇒ ≤1 Z-cell/tick (no column loop / capacity-fill / sort); antisymmetric apply + clamp + atomic throw
(conservation) and carry taken from the gradient accumulator before buoyancy (never banked); resolved effectiveWeight[i]
folded into ComputeContentHash right after effectiveKp[i]; DERIVED (no new MeaningMembers bit); default registry
byte-identical (buoyancy gate `weightDelta!=0` skipped). LIVE gate: dotnet test Core = 1059/1059 (ScWeight 31/31);
zero-float + int-overflow + type-hardcode scans pass RED-control self-tests AND the gate; committed mutation json =
73.23% (181 killed + 5 timeout / 254 valid) ≥ 70; far-tier CoarseSpecies/CoarseBandStep git-diff EMPTY.

Owner manual-acceptance recorded in the RESULT: owner-eye ✅ («работает») + merge ✅.

## state_changes

- NOW.md header → updated: 2026-06-30 by s-work-033.
- NOW.bet.current_truth → Sc-types + Sc-weight both DELIVERED+merged (main @61b7923); road rolls to Sc-reactions.
- NOW.tasks → Sc-weight active→done LEAVES the hot list; Sc-reactions ENTERS as the active task (status active,
  CALL c-exec-021 to be framed + hardened in a fresh OS session). G1 = 1 active task.
- NOW.next_slices → Sc-reactions removed (promoted to active task); Sc-damage retained.
- NOW.open_calls → c-exec-020 cleared (its RESULT arrived); list now empty.
- NOW.next → inline framing CALL: frame + adversarially harden c-exec-021 (Sc-reactions) in a fresh OS session,
  owner present at PLAN; fold d-coop-interdependence-repin-001; base at-or-after main @61b7923.
- NOW.sources / history_pointers → add the Sc-weight delivered + s-work-033 pointers.
- LOG.md → append the s-work-033 line.
- history/ → 2026-06-30-c-exec-020-sc-weight-result.md (executor RESULT verbatim + merge facts + G5 outcome) and
  this file (s-work-033.md).

## captures (triage at the Sc-reactions framing / pulse — NOT acted on here)

- G5 note-only #1: GasCoopGame `ScWeightBuoyancyTests` planted-instant-sort sub-assertion is an arithmetic tautology
  (11·mass > 4·mass; never runs the flow on the planted field) — a VACUOUS test discriminator. The Sc-weight
  realization is sound (no-pop guaranteed by face-adjacency + the outflow clamp), but the RED CONTROL is weak →
  harden it (run a real instant-sort planting through VoxelFaceFlow) when the Sc-reactions independent-test-author
  next touches Voxel tests, or as a small product cleanup. Product-repo test-quality, not a slice defect.
- G5 note-only #2: GasCoopGame `docs/measurements/c-exec-020-owner-eye-checklist.md` cites a stale "977 tests" vs
  the real 1059 — trivial doc nit in a non-gate confidence doc.
- ADR-0019 cross-track number collision: the engine Sc-weight ADR-0019 double-books the dev2 visual track's
  c-visual-002 S2 ADR-0019 (same pattern as 0012/0016/0018). The DIRECTION renumbers one at the eventual
  cross-track merge — bookkeeping, not a blocker.

## decisions_needed

None new. d-coop-interdependence-repin-001 stays pending and becomes directly actionable at the Sc-reactions PLAN
(its recommended home) — surfaced to the framing session, not answered here.

## play_check

1. Recite — done: restated Sc-weight goal/done_when (per-type vertical buoyancy, creeping bias not sort) + the bet
   g-9c41 (CHARACTER ROAD).
2. Owner inputs (owner) — skipped (one line): not owner-content — an engineering slice; owner's role is the
   manual-acceptance eyeball (recorded ✅) + merge gate (recorded ✅), not authored content.
3. Do the work — done: the executor leg (c-exec-020) already returned; digested its RESULT, ran the binding
   fresh-session G5 over the merged code.
4. Self-check — done: compared the RESULT against all 10 done_when point-by-point (deliverable reconciliation) +
   the G5 refutation = COULD-NOT-REFUTE; evidence is the merged commits/gates/G5, not a claim.
5. Close — done: RESULT; Sc-weight → done; next = framing CALL for Sc-reactions (the next task in the bet; the
   road continues, so NOT a review — review is for when the whole bet's tasks are exhausted).

## log

2026-06-30 — work (g-9c41 / Sc-weight / c-exec-020 → DONE; s-work-033): applied the Sc-weight executor RESULT —
per-type vertical buoyancy (heavy sinks / light rises / neutral no-drift, creeping integer Z-face bias, ENGINE-ONLY)
DELIVERED + merged + pushed (GasCoopGame main @61b7923) + BINDING-G5 COULD-NOT-REFUTE; road rolls to Sc-reactions.

## next

CALL (inline, framing session — see NOW.next): frame + adversarially harden c-exec-021 (Sc-reactions: integer
chemistry between weight classes — telegraph + bang, co-op interdependence pressure) in a fresh OS session, owner
present at PLAN; fold d-coop-interdependence-repin-001; base at-or-after GasCoopGame main @61b7923. The builder does
NOT author the CALL.

END_OF_FILE: live/indie-game-development/history/s-work-033.md
