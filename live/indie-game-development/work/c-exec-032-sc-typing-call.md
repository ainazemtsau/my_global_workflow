# CALL c-exec-032-sc-typing -- Sc-typing PLAN: env-derived identity typing after Sc-reactions

Direction: indie-game-development / g-9c41 / Sc-typing -- the next CHARACTER ROAD node after Sc-reactions
(Sc-types -> Sc-weight -> Sc-rep -> Sc-kernel -> Sc-reactions -> Sc-typing -> Sc-damage).

This is a PRODUCT-REPO **PLAN-ONLY** executor CALL for `C:\projects\Unity\GasCoopGame_dev`.
It opens a fresh owner-present PLAN session. It must NOT write production code and must NOT author the independent
RED tests. Planning and execution are split: this PLAN freezes the contract; a later fresh BUILD session starts with
the independent RED test-author first, then builder.

## Authority / source bundle

- Direction state: `C:\my_global_workflow\live\indie-game-development\NOW.md` (Sc-reactions closed; immediate next
  is Sc-typing).
- Canon gas SPEC: `C:\my_global_workflow\live\indie-game-development\knowledge\g9c41-gas-engine-SPEC.md`,
  especially Fact 4 and the dynamic-typing paragraph in section 5.
- Sc-typing homing decision: `history/2026-07-02-s-shape-prep-screactions-001.md` -- owner-delegated placement,
  owner-agreed mechanism = accumulate-with-hysteresis, Sc-typing immediately after Sc-reactions.
- Sc-reactions frozen artifacts:
  - `openspec/changes/c-exec-021-sc-reactions/PLAN.md`
  - `openspec/changes/c-exec-021-sc-reactions/specs/sim-core/spec.md`
  - `docs/adr/ADR-E-0006-c-exec-021-sc-reactions.md`
  - `docs/results/c-exec-021.md`
- Product base known to the direction: GasCoopGame `origin/main @484084a`, `origin/dev @f5ba86a` after c-exec-021
  merge/push. The PLAN still re-derives HEAD first-hand.
- Current local observation before issuing this CALL: `GasCoopGame_dev` has pre-existing dirty
  `Packages/manifest.json` and `Packages/packages-lock.json`. Treat them as owner/local changes: do not revert or
  edit unless the PLAN proves they are required.

## Goal

Freeze the Sc-typing plan for env-derived gas identity: gas is one parent substance with many faces; at spawn it can
become a concrete type from local committed environment, and at runtime a cell can accumulate exposure to an
environment condition and flip its dominant type through hysteresis. This is DATA-driven and deterministic under
input-lockstep; a new typing row or concrete type adds zero core branches.

Approach token to evaluate, amend, or reject in the owner-present PLAN:
`env-typing-accumulate-hysteresis-stamp-flip`.

The PLAN should prefer the narrow engine-only identity slice:
- build the exposure accumulator + dominant-stamp flip path;
- make single-reactant env-response rows fire through Sc-typing, not through the Sc-reactions chemistry pass;
- keep temperature-keyed rows dormant until the Sc-damage/temp-feedback decision;
- reserve continuous "regime" reads unless the owner explicitly signs them into this slice.

## PLAN decisions to record owner-present

1. **Scope:** identity typing now vs identity + continuous regime read. Recommendation: identity only; regime is a
   derived read, moves no mass, and can wait unless it is nearly free.
2. **Live env channels:** which committed env-vector channels may drive this slice. Recommendation: density and any
   already-authoritative non-temperature channels first; temperature/radiation/catalyst rows stay schema-admitted but
   dormant until their layers exist.
3. **Exposure pacing:** owner-signed default threshold, accumulation rate, decay/cooldown, hysteresis gap, and max
   range. A spec-conformant build with flickery or instant-feeling flips is wrong.
4. **Data schema:** whether Sc-typing reuses the c-exec-021 single-reactant env-row data shape or introduces a
   separate `TypingRuleSet`. Either way, chemistry must still NOT fire single-reactant rows as reactions.
5. **Checksum member:** the accumulator is a new replicated per-cell state if stored. Record next-free
   `MeaningMembers` bit at tip, SKIP-ZERO discipline, cell-keying, isolation/distinctness tests, and byte-identity
   no-regression.
6. **Handshake hash:** typing rule rows, env-channel ids, thresholds, target type ids, decay/hysteresis values, and
   spawn-typing rows ride the compared `GasTypeRegistry.ContentHash()` canonically. Empty typing data folds nothing.
7. **Tick ordering:** typing reads committed/tick-start env, never live mid-tick. Record ordering relative to
   reaction pass, flow, telegraph, and stamp maintenance; no same-tick feedback loop.
8. **Wake triggers:** bind the reserved env-vector-delta wake row for the live channels used by Sc-typing. Lazy
   catch-up on wake is not equivalent when env varied while asleep.
9. **Spawn-time parent typing:** decide whether parent/typeless gas becomes a concrete type via the same resolver in
   this slice. Recommendation: include if it uses the same data path; otherwise record an explicit follow-up, not a
   silent cut.
10. **Mass/stamp invariants:** identity flip changes type identity without accidental mass change, stale TypeIds, lane
    leaks, or K/capacity surprises. A thrown typing tick is atomic: mass/stamp/exposure/telegraph/bias/queue/Tick
    unchanged.
11. **Vedro classification:** expected vedro-2 shared coarse mechanic. Reconfirm. No vedro-1 detail bubble and no
    vedro-3 mechanic unless the owner deliberately signs a larger slice.
12. **ADR:** bind the next free `ADR-E-*` at tip; filename embeds `c-exec-032-sc-typing`.

## Boundaries / STOP

- PLAN-only: no production code, no test-author files, no builder tests, no result-doc delivery claim.
- No Sc-damage: no damage, health, body/object/loot physics, wall breach, live temperature feedback, heat field, or
  `GasType.Instance` gameplay unless the owner consciously re-scopes the slice.
- No condition-wave build; the c-exec-021 deferred wave fork stays parked.
- No visual/dev2 work and no c-visual-007 changes.
- No canon/cartography work and no `gas_coop_game_canon` edits.
- No ReactionLayer delete/amendment; that is a separate owner-gated cleanup.
- No dense-plane resurrection, no type-id hardcode dispatch, no float on authoritative path, no ADR-0002 reopen.
- Do not touch the pre-existing `Packages/*` local diffs unless the PLAN explicitly proves they are in scope.

## Future BUILD done_when that the PLAN must freeze

The PLAN's frozen spec/ledger should include, at minimum:

1. Independent RED test-author FIRST in the later BUILD session, spec-only, before production code. Builder may not
   edit those tests.
2. Data-driven env typing: a NEW typing row + NEW concrete target type added as data only causes a flip; a hardcoded
   type branch fails.
3. Accumulate-with-hysteresis: exposure must build over ticks before flip; below-threshold / insufficient-duration
   / noisy boundary inputs do not flicker or instant-flip.
4. Single-reactant env rows fire only through Sc-typing, not through the chemistry reaction pass. Existing
   c-exec-021 "does not fire this slice" intent is preserved or explicitly superseded by the new independent
   test-author.
5. Spawn-time parent typing either works through the same data resolver or is explicitly out-of-scope with a named
   follow-up.
6. Accumulator checksum socket: SKIP-ZERO, cell-keyed, additive, isolation + distinctness REDs, default/empty typing
   byte-identical to current goldens.
7. Handshake divergence/convergence: every load-bearing typing data field affects `ContentHash()`; authoring order
   does not; unknown target type/env channel is a loud build error.
8. Committed-env ordering: typing reads tick-start/committed env only. A planted same-tick env feedback or
   order-dependent apply fails.
9. Wake-source binding: env-vector delta wakes sleeping gas for live channels; no lazy backfill substitute.
10. Mass/stamp/atomicity: type flips conserve declared mass exactly, clear stale TypeIds, do not leak lanes, and
    leave the field byte-unchanged on every throw path.
11. No-regression: no typing rules / inactive conditions preserve Sc-reactions byte-identity and loopback
    determinism.
12. Strong-check battery: spec-silence audit with full escape-class walk, deliverable coverage, negative controls,
    property coverage for core algorithm classes, mutation >= configured floor, review evidence, and
    `tools/check.ps1 -Deliver` green on `dev`.
13. Owner-eye confidence (not a gate, no self-marking): in a debug scene, a gas exposed to a chosen non-temperature
    environment visibly accumulates then flips, and does not flicker at the boundary.

## Return

Return a RESULT home to Direction OS with:

- created planning artifacts under `openspec/changes/c-exec-032-sc-typing/` (`proposal.md`, `PLAN.md`,
  `specs/sim-core/spec.md`, `tasks.md`);
- ADR-E decision file or draft as required by repo convention;
- exact owner decisions and signed properties;
- explicit BUILD executor CALL for the next fresh session, whose first build step is the independent RED test-author;
- evidence that no production code/tests were changed in the PLAN session;
- current base sha, contract version, dirty-worktree handling, and any STOP/owner questions.

## Budget

One owner-present PLAN session. If Sc-typing splits into identity, spawn typing, regime, or wake-trigger sublegs,
return the split as the PLAN output and stop; do not silently widen the build.

END_OF_FILE: live/indie-game-development/work/c-exec-032-sc-typing-call.md
