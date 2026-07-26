# RESULT — s-work-031 (work: close Sc-types / c-exec-019)

session: s-work-031
direction: indie-game-development
node: g-9c41
task: Sc-types (FIRST slice of the CHARACTER ROAD, d-character-road-001)
play: work
date: 2026-06-29
input: owner plain message — «c-exec-019 Sc-types — DELIVERED + MERGED + PUSHED»

## outcome

Sc-types — the multi-gas META-TYPE/TYPE param substrate (ENGINE-ONLY), the FIRST character-road slice — is
DELIVERED + MERGED + PUSHED and now BINDING-G5-VERIFIED. The engine carries MORE THAN ONE gas type, types behave
visibly differently via a 3-layer DATA-DRIVEN param structure (R15), and the two day-one sockets (TypeId-in-checksum,
content-hashed canonical registry) are laid so weight/reactions/damage and later DLC/lore types plug in without a
schema migration or a desync. The task closes `done`; the bet rolls to Sc-weight.

## evidence (verified FIRST-HAND, not on the owner's word)

- **Merge:** GasCoopGame `origin/main` @`7d08882` = "Merge dev into main: c-exec-019 Sc-types …" (dev→main --no-ff,
  exec @34e19fb, PLAN @11ef4b9). Local main == origin/main. All deliverables present on disk + in the tree:
  `Assets/GasCoopGame/Core/Field/Types/{GasMetaType,GasParentParams,GasType,GasTypeRegistry}.cs`, the 8
  `tests/GasCoopGame.Core.Tests/Field/Types/ScTypes*Tests.cs`, `tools/type-hardcode-scan.ps1`,
  `docs/adr/ADR-0018-sc-types-multi-gas-param-substrate.md`, `docs/measurements/mutation-c-exec-019-sc-types.json`,
  `openspec/changes/c-exec-019-sc-types/`.
- **Builder RESULT** (`C:/projects/Unity/GasCoopGame_dev/RESULT.md`): status DELIVERED; `check.ps1 -Deliver` GREEN
  (948/948 at build), mutation 76.74% (475/619) ≥70, dense `[species][cell]` rep (ADR-0018 D1) + numeric
  revisit-trigger `type_count×active_cell ≥ 200 000` / tripwire ≥4 types; per-type spread Kp the only live lever;
  TypeId checksum member rep-conditional + additive; content-hashed canonical `GasTypeRegistry`; both zero-float +
  int-overflow scans extended to `Core/Field/Types`; ZERO-LEGACY (RED-first independent test-author); in-build
  fresh-session Sonnet 4.6 G5 could-not-refute on 6 seams.

## binding fresh-session G5 (THIS session)

Per the CALL's own discipline line ("a FRESH-SESSION G5 … COULD-NOT-REFUTE is the bar") the binding G5 runs in a
session separate from the build — the builder's in-session Sonnet pass is a strong pre-pass. Ran as workflow
`wf_a07586c0-22f`: 7 adversarial seam-refuters over the REAL merged code + a referee.

- **Binding verdict: COULD-NOT-REFUTE → mark-done. ZERO blocking findings.** (5 seams could-not-refute, 2 weakened
  with note-only findings.)
- Provenance: 3 refuters independently re-derived the pre-slice golden by `git archive`-replaying tip @2117341 →
  byte-identical 13-tick `MeaningChecksum` vector ⇒ the no-regression / additive / byte-identical-single-default
  claims are genuine, not self-fulfilling. One refuter ran `check.ps1 -Deliver` end-to-end → GREEN (now 1028/1028;
  the 948→1028 delta = later dev2 visual-track merges grew the shared baseline; all pass).
- STOP-discipline held: frozen far-tier `CoarseSpecies` git-diff EMPTY (adb9255..34e19fb); no weight/buoyancy /
  reaction/chemistry / damage/temperature / visual / float creep on the authoritative path (token-scanned); ADR-0002
  (input-lockstep) not reopened.
- The two weakened seams (NON-blocking, carried as planner notes):
  1. **type-hardcode scan completeness** — `tools/type-hardcode-scan.ps1` forbids only the enum/switch token
     superset; a `Dictionary<int,Func<…>>` keyed by TypeId or an `if(typeId==N)` chain evades it (reproduced). The
     delivered `Core/Field/Types` has ZERO hardcoded type branch (pure `type ?? meta ?? parent` + canonical
     `Array.Sort` + dict lookup; flow reads `EffectiveSpreadKp(s)` positionally), and done_when #3b is scoped exactly
     to switch/enum-over-TypeId — so the property holds in fact; only the future-guard is weaker than its header
     claims. → broaden the scan (or soften the header) BEFORE the first per-type-DISPATCH slice.
  2. **settle-floor vs resolution** — `MinSpreadKp=12` (= 2×VoxelFaces.Count) is on RAW Kp, but stability depends on
     `kpEff = Kp*spf`; at the test/default spf=4 the floor over-protects ~2.4x (raw Kp 6–11 actually settle). SAFE
     (rejects conservatively; no slosher enters production; baseline Kp=12 stays the fastest admitted type), but the
     Kp=4 negative control in `ScTypesSettleOracleTests` Test4b discriminates only the genuinely-sloshing sub-class.
     → re-derive the floor against `kpEff` if resolution or the floor ever changes (carry to Sc-weight).
  Other notes: only the mutation summary JSON is committed (StrykerOutput gitignored — matches contract); RESULT/
  tasks.md record 948/948 while live is now 1028/1028 (cosmetic); the per-plane `(s, TypeIdAt(s))` checksum loop is
  largely redundant with the registry `ContentHash` today (belt-and-suspenders; carries real per-cell data when canon
  §4 шов 5 / ADR-0018 D1/D4 trips).

## owner-authorized amendment (recorded)

The frozen settle-oracle criterion `VoxelStepResult.ActiveFaces == 0` was INFEASIBLE under the frozen integer flow
law (the proven ≤4-unit carry-seep "micro-breathing" keeps `ActiveFaces ≥ 1` forever, valid OR sub-floor). Owner
present 2026-06-29 authorized Option 1 — amend the criterion to LOW-AMPLITUDE rest (amplitude is the discriminator
the carried `VoxelFaceFlowSettleTests` already use), re-author ONLY the settle test, flow law UNTOUCHED (byte-identity
preserved). `owner-ack:esc-c-exec-019-settle-criterion-2026-06-29` (banner in the frozen spec, line 199). G5
confirmed the banner present + flow law byte-identical ⇒ a governed test-criterion correction, not a regression-hider.

## state_changes (applied by this session as its own writer)

- NOW.md active_tasks Sc-types: `status: active → done` (close note + evidence + binding-G5 verdict + amendment).
- NOW.md active_tasks Sc-weight: `status: parked → active` (bet rolls; CALL c-exec-020 to be framed; 2 G5 planner-notes attached).
- NOW.md open_calls c-exec-019: `status: framed → delivered`.
- NOW.md `next` IMMEDIATE NEXT rewritten: frame + harden the Sc-weight executor CALL (c-exec-020) in a fresh OS session.
- NOW.md `next` PUSH block: + s-work-031 commit line.
- LOG.md: + the s-work-031 writer line.

## captures

- G5 planner-note (carry to c-exec-020): re-derive the monotone-settle floor against `kpEff=Kp*spf`, not raw Kp.
- G5 planner-note (carry to c-exec-020 / Sc-reactions): broaden `tools/type-hardcode-scan.ps1` (dict-of-delegates /
  if(typeId==N) evasion) or soften its "strongest guarantee" header before the first per-type-DISPATCH slice.
- Cosmetic: refresh the 948/948 → 1028/1028 headless count in the builder RESULT/ledger if a future audit cares.
- Informational: the per-plane `(s, TypeIdAt(s))` checksum loop is redundant with `ContentHash` until the
  sparse-dominant per-cell-id slice (canon §4 шов 5) trips.

## decisions_needed

None. (mark-done is unambiguous; the settle-criterion amendment was owner-authorized in the build session; the
direction is already set to the character road.)

## play_check (work)

1. Recite — DONE: restated Sc-types goal/done_when + the g-9c41 bet it serves.
2. Owner inputs (owner) — N/A: Sc-types is an engineering slice, not owner-content (no food/voice/schedule); no owner
   inputs to gather. (Owner's report «DELIVERED + MERGED + PUSHED» is the trigger; the owner-authorized settle
   amendment is cited from the build session.)
3. Do the work — DONE: located + read the builder RESULT; verified the merge + all deliverables FIRST-HAND on
   GasCoopGame main @7d08882; ran the binding fresh-session G5 (wf_a07586c0-22f).
4. Self-check — DONE: compared the delivered code against done_when seam-by-seam via 7 adversarial refuters + referee
   = could-not-refute, zero blocking.
5. Close — DONE: this RESULT; Sc-types → done; bet rolls to Sc-weight; next = frame c-exec-020.

## log

2026-06-29 — writer (g-9c41 / Sc-types / c-exec-019): Sc-types DELIVERED + MERGED + PUSHED + binding-G5 could-not-refute
(GasCoopGame main @7d08882); active→done; bet rolls to Sc-weight; next = frame c-exec-020.

## next

CALL — frame + adversarially harden the **Sc-weight** executor leg (c-exec-020) in a fresh OS session:
- goal: per-type vertical buoyancy on the near grid — heavy gas SINKS, light gas RISES, tunable strength per
  meta-type via an integer bias on flow through Z-faces, a CREEPING front (canon §3 «buoyancy-BIAS, не сортировка»;
  per-column instant sort FORBIDDEN/§7-buried). Keys off Sc-types.
- context: NOW.md active_tasks Sc-weight; canon §3; the FROZEN far-tier `CoarseSpecies` weight/heat integer law
  (ADR-0005) to PORT into the near path BEFORE S4 deletes it; subsumes d-buoyancy-near-weight-priority-001; the 2 G5
  planner-notes above.
- boundaries: ENGINE-ONLY (no visual hookup); no reactions/damage; lock = ADR-0002; integer-only authoritative path;
  per-column instant sort near = STOP.
- done_when: per-type Z-bias (heavy sinks / light rises); RED non-monotone-conservation + no-pop (no vertical
  teleport) oracle; determinism preserved (loopback hash green; new code in BOTH scan roots — and re-derive the
  settle floor against kpEff); -Deliver GREEN + mutation ≥70 + fresh-session G5; ZERO-LEGACY; owner-eye.
- return: a RESULT routed HOME; dev→main merge + push owner-gated.
- budget: one slice (may SPLIT at the PLAN).

END_OF_FILE: live/indie-game-development/history/s-work-031.md
