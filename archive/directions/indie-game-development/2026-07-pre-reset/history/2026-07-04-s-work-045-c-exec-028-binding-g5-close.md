# RESULT s-work-045 — c-exec-028 binding fresh-session G5 close

session: s-work-045
direction: indie-game-development
node: g-9c41
play: review (verify + close a delivered leg; roll state forward)
for: c-exec-028 (tools/ benchmark-hardening — DF-2 + d-benchmark-category-gate-001)

Reconciliation note: s-work-044 was taken by a concurrent same-direction VISUAL review committed d62359f
mid-flight (g-7e15 source-scan retirement, NOT met). This session reconciled against the committed NOW.md and
touches ONLY the g-9c41 / c-exec-028 sections, preserving that session's g-7e15 changes.

## outcome
c-exec-028 VERIFIED SOUND by a binding fresh-session G5 (this session, first-hand on the SHIPPED [Explicit]
state) and CLOSED. GasCoopGame tooling can no longer be silently POISONED (DF-2) or silently BYPASSED
(d-benchmark-category-gate-001) by a [Category]-tagged test. The bench-tax every mutation leg paid is cleared at
the ROOT: the benchmark is [Explicit] again -> Stryker skips it by construction; mutation.ps1 is byte-identical
to pre-c-028 (zero file moves, no stash). The g-9c41 bet stays ACTIVE; the character road resumes at c-exec-021
(Sc-reactions). DF-2 -> RESOLVED; d-benchmark-category-gate-001 -> DISCHARGED. Route-home backlog DF-1 +
DF-3..DF-9 registered as tracked-deferred (DF-10 already executor-launched in a separate session).

## evidence
Read the product repo C:\projects\Unity\GasCoopGame directly @ origin/main cde4c3d (validation.config
synced_contract_version=14). Binding fresh-session G5 run FIRST-HAND on the SHIPPED [Explicit] state
(docs/reviews/review-c-exec-028-benchmark-tooling.md rounds 1-4 reviewed the SUPERSEDED stash approach; the
round-2 binding Codex KERNEL-G5 was on the stash tip 99825b3 — the final [Explicit] redesign b2ff0d6+cde4c3d had
NO binding G5 until now):

- **DF-2 root fix:** live benchmark = `[TestFixture, Explicit, Category("Benchmark")]` (grep: single fixture);
  `git diff e0e4f5a..cde4c3d -- tools/mutation.ps1` EMPTY (byte-identical); mutation witness recorded in cde4c3d
  (~13.9 min, no poison). Approach switched stash->[Explicit] under
  `owner-ack:c-exec-028-explicit-redesign-2026-07-04` (non-convergence "same class 2x = stop" fired after the
  stash hit the multi-step-file-mutation atomicity class 3x -> owner directed the root fix).
- **hygiene.ps1 carve-out narrow + STRENGTHENING** (diff read first-hand): `[Explicit]` allowed IFF a file
  carries `Category("Benchmark")`; `[Ignore]` still banned; regex tightened to `(?:\[|,)\s*Explicit\b`, which
  ALSO closes the pre-existing combined-attribute hole (`[TestFixture, Explicit, ...]`) the old `\[` form missed.
  No existing green gate weakened.
- **benchmark-discoverability-check.ps1 (force-DISCOVER):** category-AWARE source-scan (not category-blind
  `--list-tests`), strips `//`+`/* */` comments, method-REAL (`[Test]`/`[UnityTest]`, not `[TestFixture]`),
  category-WIDE (all files), REQUIRES `[Explicit]`. Ran `-SelfTest` -> GREEN (5 cases: well-formed GREEN;
  Bench-mistag / absent / methodless / not-[Explicit] each RED). Ran real gate -> GREEN.
- **excluded-category-check.ps1 (general rule):** parses the real check.ps1:88 `--filter`, splits on `&`,
  requires each `TestCategory!=X` to own a counterpart; comment decoy ignored; bare uncountered `Foo` rejected.
  Ran `-SelfTest` -> GREEN; real gate -> GREEN (2 exclusions: NegativeControl force-EXECUTE, Benchmark
  force-DISCOVER).
- **ScKernelScalingMatrixSchemaTests freshness asserts:** x2==2*peak, x4==4*peak, peak==max(ms_by_roster),
  over_budget==(x2>budget_high_ms), naive.flooded_ms_peak==peak + 2 RED controls. Ran
  `dotnet test --filter FullyQualifiedName~ScKernelScalingMatrixSchemaTests` -> 3/3 GREEN on the real committed
  matrix. x2-vs-x4 oracle/generator disagreement owner-acked out-of-scope -> DF-10 (fix touches the generator;
  shipped assert stays x2, green off-band).
- **Wiring:** check.ps1 -Deliver invokes both new gates + 3 seeded-miss self-tests (diff read). Full -Deliver
  exit 0 / 1325 tests per the review record + the owner-gated merge; not re-run this session (every NEW surface
  verified directly instead).
- **Boundaries/debris:** git diff = the 7 claimed files (+ RESULT/DEFERRED/ADR-P-0005/review); no Core/sim/golden
  touched; no `openspec/changes/c-exec-028` folder (per-change battery N/A by absence); working tree clean (only
  an unrelated `.codex/config.toml` local edit), no `.benchoff` debris.
- **CONTRACT v17 CROSS-CHECK** (surfaced during reconciliation): OS CONTRACT_VERSION is now **17** (aa59ba5),
  banning self-written source-scanners as BEHAVIOR evidence (witness = the visual track's 1728-line
  SourceScanText.cs proving render/shader behavior). c-028's two new gates ARE self-written source-scanners — but
  of the **TOOLING/TEST-SUITE-HYGIENE family** (like the contract-blessed hygiene.ps1), asserting
  present+correctly-tagged, NOT product behavior (the discoverability gate explicitly disclaims runtime
  "would-run"). v17's "engine-free logic = real headless tests" clause + the untouched hygiene-scanner family both
  stand -> v17 **PERMITS** them. c-028 was built on the actual v14 base before v17, so it is not retroactively
  governed. Verdict UNCHANGED.

**VERDICT: SOUND — 0 P1, 0 P2.** One P3 (hygiene/discoverability co-presence is file-level not method-level —
same class as owner-deferred DF-9, honestly documented in the script). Not a defect, not a c-028 regression.

## captures
- §Re-sync scope for c-021 is **v14->v17** (not "v14" as the CALL/NOW said) — the OS shipped v15/v16/v17
  concurrently with c-028. The v17 source-scan-ban must CONSCIOUSLY classify c-028's own benchmark-discoverability
  + excluded-category gates as tooling/test-suite-hygiene (permitted, hygiene.ps1 family) NOT behavior-evidence
  (banned) — my read is clearly the former; record it at §Re-sync so the ban does not reflexively delete
  legitimate integrity gates.
- DF-5 (P1, gate-integrity) is the backlog item that arguably JUMPS the c-021 queue: check.ps1:64
  (Assert-NoUnstagedTrackedChanges checks only git diff-files) + review-check.ps1:90 (accounts only
  Reviewed-commit..HEAD) ignore STAGED changes -> a staged uncommitted source/tool/test change can pass -Deliver
  absent from review evidence, weakening the deliver gate itself. Feeds d-df-backlog-sequencing-001.
- Product working tree carries an unrelated locally-modified `.codex/config.toml` (not part of c-028).

## decisions_needed
- **d-df-backlog-sequencing-001** — c-exec-028 cleared the bench-tax; the pre-agreed next is c-exec-021. The c-028
  Codex KERNEL-G5 routed a 9-item route-home backlog (DF-1, DF-3..DF-10) — 5 P1; DF-10 already executor-launched.
  How to sequence the rest vs the c-021 road?
  - Option 1 [recommended]: c-021 next (main road); DF-1/DF-3/DF-4/DF-6-9 tracked-deferred with wake-triggers;
    consider ONLY DF-5 for a queue-jump (it weakens the deliver gate itself).
  - Option 2: a small P1-DF batch FIRST (DF-5 + DF-3/DF-4), then c-021. Bad-because: delays the feature road again
    right after an infra leg.
  - Option 3: fire c-021 now, defer all DFs. Bad-because: leaves DF-5 (a live gate blind spot) open under every
    subsequent -Deliver green.
  - Recommendation: Option 1 — most DFs are latent, the feature road is overdue; but DF-5 is a genuine
    gate-integrity hole, decide consciously.

## play_check
- step1 verify-by-refutation: DONE — binding fresh-session G5 on the SHIPPED [Explicit] state; SOUND, 0 P1/P2
  (gates + matrix tests run first-hand; v17 cross-check resolved as permit).
- step2 harvest-per-lens: DONE (thin, infra) — process learning: the non-convergence "same class 2x = stop" rule
  fired correctly (stash atomicity 3x -> owner switched to the root [Explicit]).
- step3 update-tree: SKIPPED (no TREE change) — c-028 is an infra sub-leg; the g-9c41 bet continues (no G9).
- step4 add-back-check: DONE — nothing missed; the stash approach was SUPERSEDED by a better one, not a cut.
- step5 knowledge: SKIPPED — durable learning lives in the product ADR-P-0005 + DEFERRED-FINDINGS + the
  os/engineering contract; no OS knowledge/ entry nobody re-reads.
- step6 select-next: DONE — next = c-exec-021 (pre-agreed, owner-decided d-nextcall-tooling-vs-c021-001);
  DF-backlog sequencing surfaced as d-df-backlog-sequencing-001 (G7).
- step7 close: DONE — this RESULT.

## log
g-9c41 review c-exec-028 — binding fresh-session G5 SOUND (0 P1/P2, first-hand on the SHIPPED [Explicit] state):
DF-2 root-fixed via [Explicit] (owner-ack), new gate-integrity gates have real teeth (self+real+matrix run
first-hand), v17 cross-check = permit (tooling-hygiene not behavior-evidence); leg CLOSED, bench-tax cleared;
next = c-exec-021 (§Re-sync now owes v15/v16/v17).

## next
Pointer -> live/indie-game-development/work/c-exec-021-call.md (Sc-reactions; PREPPED, forks (a)-(f) closed). At
fire time run its §Re-sync — repo at v14, OS now v17, owes v15 (review-scope-split) + v16 (tool-unavailable-STOP)
+ v17 (source-scan-ban; classify c-028's scanner-gates as tooling-hygiene, do NOT delete) — + full re-hardening +
fill §PENDING, then fire in a FRESH owner-present PLAN (the direction writes the CALL). May be re-ordered by the
owner's answer to d-df-backlog-sequencing-001.

END_OF_FILE: live/indie-game-development/history/2026-07-04-s-work-045-c-exec-028-binding-g5-close.md
