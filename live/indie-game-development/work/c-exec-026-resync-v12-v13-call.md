# CALL c-exec-026 — §Re-sync GasCoopGame 11→13: property-layer (v12) + refuted-register (v13) (ENGINE INFRA, GasCoopGame_dev)

> OPENS AFTER: owner merges+pushes the OS v13 change (branch `maint/sheaf-admm-borrows`, commits 2beec18 + 2a64e13)
> to workflow-repo main — the builder reads the binding contract text from a SYNCED os/engineering checkout. v12
> (property-layer) is already on OS main @2716bf4; v13 (refuted-register) rides that branch. Until v13 is on main
> this CALL cannot fire (nothing to sync TO).
>
> Base = GasCoopGame main @ current (v11 + ADR-P-0003, review/negative-control/escape-class gates all wired). Fires
> in a FRESH GasCoopGame_dev session/worktree — NEVER dev_2. This is a `tools/` + `validation.config` + `docs/`
> INFRA edit (NOT Core/Field) — it does not touch the authoritative sim path, so byte-identity is trivially
> preserved and it does not conflict with feature legs. Sequence it AFTER c-exec-025-w1b merges to main, or on a
> clean dev worktree off main. dev→main merge + push OWNER-GATED.

Direction: indie-game-development / g-9c41 — engineering-contract §Re-sync (infra propagation, NOT a Sc-kernel feature leg). Trigger: PROJECT_SETUP §Re-sync (the repo is BEHIND: os/engineering CONTRACT_VERSION current=13, repo synced_contract_version=11).

## goal (outcome, not method)

The GasCoopGame deliver gate (`tools/check.ps1 -Deliver`) enforces os/engineering contract v12 (property-layer) and v13 (refuted-register) as executable deliver dependencies with seeded-miss self-tests — the same "Enabled ≠ written" wiring the v9/v10/v11 re-syncs already landed — so the repo's stamp truthfully reads `synced_contract_version: 13` and no future core-algorithm leg or refuting review can reach DELIVERED without the new evidence. STRICTLY ADDITIVE: no existing green gate weakened; every currently-delivered leg still delivers (via grandfathering, exactly as v10/v11 did).

## context

- Binding contract text (read from SYNCED os/engineering after the merge above):
  - v13 refuted-register — `os/engineering/VALIDATION.md` §Refuted-register; `os/engineering/CONTOUR.md` (VALIDATE + §b walk extension); `os/engineering/PROJECT_SETUP.md` §Strong-check clause (g) + Done-when seeded-miss; `os/engineering/CONTRACT_VERSION` log line 13.
  - v12 property-layer — `VALIDATION.md` §Property-layer + G2; `CONTOUR.md` PROPERTY AUDIT stage + §b; `PROJECT_SETUP.md` §Strong-check clause (f); CONTRACT_VERSION log line 12.
- WORKING TEMPLATES already in the repo (mirror their exact shape — `-SelfTest` seeded-miss + `-Repo/-ChangeId` per-change mode, wired into `check.ps1 -Deliver` with a self-test call + a per-change loop): `tools/review-check.ps1` (v10), `tools/negative-control-check.ps1` (v11), `tools/escape-class-check.ps1` (v9). `tools/coverage-check.ps1` is where the v12 `prop:` token check joins the existing `exists:`/approach-token logic.
- Grandfathering precedent: `validation.config` already carries `escape_class_walk_grandfathered`, `review_evidence_grandfathered`, `negative_control_grandfathered` — the pre-convention non-archived changes (c-exec-017/018/019/020/023 + the c-visual-00x set). v12 and v13 need the SAME lists so wiring does not retro-fail green legs.
- Live frozen changes at fire (must all still deliver GREEN after wiring): the grandfathered set above + `c-exec-025-w1b-dominant-read` (dev). `docs/reviews/review-c-exec-024-sc-kernel-cleanup.md` already exists (v10 artifact).
- Model routing (memory gascoopgame-engineering-model-routing): BUILD = Claude Code; the binding G5 refutation of the wiring = a FRESH session, different family (Codex/GPT), read-only.

## boundaries / STOP

- INFRA-ONLY: `tools/**`, `validation.config`, `docs/reviews/REFUTED.md`, `docs/adr/**`, `docs/FRICTION.md`. Do NOT touch Core/Field/sim code, goldens, or any acceptance test of a feature leg. No golden rebaseline.
- ADDITIVE ONLY — the hard invariant of every §Re-sync (memory feedback-os-changes-dont-break-what-works): no existing gate/self-test weakened; the full pre-existing `-Deliver` battery stays green. If wiring a new gate would retro-fail an already-delivered non-archived leg, the fix is to GRANDFATHER that leg (owner-governed list, as v10/v11 did) — NEVER to loosen the gate.
- v12 is PILOT-scoped per the contract: wire the mechanism + prove it with the seeded-miss self-test, and grandfather all current non-archived changes. Do NOT retrofit `prop:` tokens onto already-delivered core files or c-exec-025. Its real bite is the NEXT new `core algorithm` frozen change.
- If the fire-time estimate exceeds ~2× budget, SPLIT at the Part A / Part B seam below and do Part A (v13) first — its writer-side keystone is already live OS-side, and it is the lighter half — then escalate the split as a second CALL. Do not silently half-build one part.
- STOP + escalate (do not substitute) if: CsCheck cannot be added under the repo's license/offline constraints (propose FsCheck 3.x or surface — do not skip the property framework); or reading the PLAN change-class mechanically (for the v12 `core algorithm` trigger) has no existing convention to key on (surface the ambiguity, propose the smallest convention, let the owner sign it — do not invent a silent default).

## done_when

**Part A — v13 refuted-register:**
1. `docs/reviews/REFUTED.md` exists with the schema `row-id | seam/invariant | claim | why-refuted | marker | review-<id> | date`, SEEDED with the real prior refutations so the register is not born empty: the ratified buoyancy per-band rejection (memory gascoopgame-buoyancy-perband-ratified — per-species TEMPERATURE is the named seam, Codex's period-2 fix rejected), the v12 "checked arithmetic / CheckForOverflowUnderflow on core" rejection (defined-wrap is a protected lockstep-determinism contract), and the REFUTED list from workflow FRICTION 2026-07-02 (Russian red-test manifest; STOP-4 deviation veto; unsigned in-repo hash approvals; InspectCode). Each seed row carries its original marker.
2. `tools/refuted-register-check.ps1` (mirror `review-check.ps1`): for each `docs/reviews/review-<id>.md` carrying a `refuted` finding, the review has a `refuted-register:` line naming the appended row id(s) (`none` legal ONLY with zero refuted rows), and every `refuted` finding resolves to an existing `REFUTED.md` row; a finding marker `register:<row-id>` must resolve to an existing row. `-SelfTest` seeded-miss proves each independently RED: (a) refuted finding with no `refuted-register:` line, (b) `refuted-register:` naming a row absent from REFUTED.md, (c) a `register:<row-id>` marker resolving nowhere; and a well-formed review PASSES. Wired into `check.ps1 -Deliver` (self-test call + per-change loop, grandfather-aware).
3. `tools/review-check.ps1` extended: `register:<row-id>` accepted as a valid refutation-verification marker (alongside `G5|KERNEL-G5`) ONLY when it resolves to a REFUTED.md row — so a re-derived-and-registered refutation closes by citation. Its `-SelfTest` gains a positive case (register-cited refuted PASSES) and a negative (register citation resolving nowhere FAILS). No existing review-check case weakened.
4. The spec-silence / escape-class walk (`tools/escape-class-check.ps1` or the audit it drives) extended: a `REFUTED.md` row naming a module/seam the frozen spec touches must be marked `still-holds | re-opened <why>` in the spec's audit — an unmarked touching row FAILS deliver, same surface as an unmarked escape class. `-SelfTest` seeded-miss for the unmarked-touching-row case.
5. `validation.config` gains `refuted_register_grandfathered` seeded with the current non-archived non-conforming changes (the same set as `review_evidence_grandfathered` + c-exec-025 if applicable), with the owner-governed note.

**Part B — v12 property-layer (PILOT):**
6. CsCheck added to the test project (FsCheck 3.x fallback only if the repo already carries F# — it does not, so CsCheck) under a `[Category("Property")]` convention; the property suite runs (inner loop or a dedicated pass — match how NegativeControl/Benchmark categories are handled in `check.ps1`).
7. `tools/coverage-check.ps1` extended: for a change whose PLAN change-class is `core algorithm`, every `headless` deliverable-coverage row carries a `prop:<TestClass>.<TestMethod>` token (same mechanical form as the existing `exists:` for engine rows) matched to an owner-signed `## Property coverage` table in the frozen spec naming, per required class, the `[Category("Property")]` test that discharges it: **permutation-metamorphic, fault-injection-all-exit-paths, multi-actor-one-tick, boundary-biased**. `-SelfTest` seeded-miss proves RED: (a) a `core algorithm` change's headless row with no `prop:` token, (b) a `prop:` token naming a test absent from the table or not `[Category("Property")]`, (c) a property table missing one of the four classes; and a conforming `core algorithm` change PASSES, and a non-`core algorithm` change is N/A (delivers). Wired into `check.ps1 -Deliver`.
8. `validation.config` gains `property_layer_grandfathered` seeded with all current non-archived changes (PILOT: no retrofit), owner-governed note.

**Both — closure:**
9. `validation.config: synced_contract_version` 11 → 13, and its note appended with the v12 + v13 lines (what each gate is, which script enforces it, seeded-miss present) in the same voice as the existing v6–v11 note.
10. `tools/check.ps1 -Deliver` GREEN end-to-end on the repo AS-IS: all new self-tests pass AND every currently-delivered non-archived leg still delivers (grandfathering verified — run it and paste the transcript). ADR-P-0004 records the §Re-sync (what wired, grandfather rationale, PILOT scope for v12).
11. Binding G5: a FRESH read-only session, different model family, tries to REFUTE that the two gates actually bite — specifically that each seeded-miss truly goes RED without its fix and GREEN with it (not a self-authored green). Its verdict recorded in `docs/reviews/review-c-exec-026-resync.md` (this infra change is itself frozen-spec-worthy; it must satisfy the v10 review-evidence gate it lives beside).

## return

RESULT routed HOME: commits + the full `check.ps1 -Deliver` transcript (green, showing the new self-tests and the grandfathered-skip lines), the two new/extended scripts, `REFUTED.md` with its seed rows, the two grandfather lists, the bumped stamp, ADR-P-0004, and the fresh-session G5 refutation record. dev→main merge + push OWNER-GATED. On GREEN → GasCoopGame is at contract v13; the writer-side v13 keystone (already live OS-side) now has its product-side teeth; the next core-algorithm leg is the v12 pilot. `next` = return to g-9c41 (the §Re-sync debt is cleared; feature road resumes at c-exec-021 Sc-reactions per NOW).

## budget

One focused infra leg (two gate scripts on proven templates + a framework add + seeding + self-tests + stamp/ADR). Larger than a feature mini-CALL because it is two contract versions; if fire-time estimate >2× this, split at the Part A / Part B seam (Part A = v13 first) and escalate — per boundaries. No new runtime dependency beyond the CsCheck test-only package (that IS the approved v12 mechanism, not a scope change).

END_OF_FILE: live/indie-game-development/work/c-exec-026-resync-v12-v13-call.md
