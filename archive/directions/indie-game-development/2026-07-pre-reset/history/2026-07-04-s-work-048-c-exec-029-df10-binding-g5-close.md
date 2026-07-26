# RESULT s-work-048 — c-exec-029 (DF-10) binding fresh-session G5 close

session: s-work-048
direction: indie-game-development
node: g-9c41
play: review (verify + close a delivered leg; roll state forward)
for: c-exec-029 (DF-10 — one shared over_budget x4 predicate; scaling-matrix freshness oracle == generator)

Reconciliation note: c-exec-029 was executor-launched SEPARATELY and never entered OS open_calls (the visibility
gap — [[workflow-stale-call-reverify-committed-state]]); this closure is reconstructed from the product-repo
RESULT/evidence + a fresh binding G5, transparently. Concurrent same-direction VISUAL sessions (s-work-046/047 +
g-7e15 migration-runbook work) advanced the repo mid-flight; reconciled against the committed NOW.md (by s-work-047),
touching only the g-9c41 / DF-10 sections.

## outcome
DF-10 (P1) VERIFIED and CLOSED. The scaling-matrix `over_budget` flag was computed by TWO divergent predicates
(generator x4, freshness oracle x2), agreeing only OUTSIDE the band `x2 <= budget < x4`; inside it a regenerated
matrix would false-RED and a tampered `over_budget=false` would false-GREEN. c-exec-029 unifies them into ONE
shared predicate `ScKernelScalingBudget.IsOverBudget(peak, budgetHigh) = 4*peak > budgetHigh`, called by BOTH the
generator (WRITES the flag) and the oracle (ASSERTS it), plus an independently-authored in-band negative control.
Binding fresh-session G5 (this session: first-hand committed-blob read + a 7-lens adversarial fan-out wf_b6c4d72c-1c6
+ completeness critic) = SOUND-WITH-NOTES. The one blocker the fan-out surfaced — a FABRICATED "owner-signed x4"
label — was closed by obtaining the owner's REAL sign-off here (x4, 2026-07-04, d-over-budget-x2-x4-001). DF-10 ->
RESOLVED. Merge dev->main OWNER-GATED.

## evidence
Read the product repo C:\projects\Unity\GasCoopGame_dev directly at the committed blob a82ee4f (= main cde4c3d +
this ONE commit; validation.config synced_contract_version=14). All lens verification against the committed blob
(read-only, git show a82ee4f:<path>) — deliberately NOT re-running dotnet in the worktree: the builder flagged, and
`git status` confirmed, a live Unity Editor flickering files (2 uncommitted Packages/*.json) — the no-crutch call is
the committed-blob logic read + the fan-out + the in-commit review's own clean `rm -rf` rebuild evidence, not a
flaky run.

**6 of 7 refutation lenses SOUND (first-hand + fan-out wf_b6c4d72c-1c6, 8 agents):**
- shared-predicate: `IsOverBudget = WeakPeerX4(peak) > budgetHigh` is the SOLE definition; generator
  (ScKernelScalingBenchmark.cs:193, old inline `weakX4>BudgetHighMs` deleted) and oracle assert #4
  (ScKernelScalingMatrixSchemaTests.cs:120, old inline `x2>budgetHigh` deleted) both call it; whole-tree grep found
  no residual divergent predicate. Strict `>` boundary correct (peak=25 -> 100>100=false; 25.0001 -> true).
- negctrl-teeth: `ScKernelScalingBudgetNegativeControlTests` fixture peak=30 (x2=60 <= budget=100 < x4=120) is
  squarely IN-BAND; `Assert.Throws` on tampered `over_budget=false` (the exact false-GREEN old x2 allowed) +
  `Assert.DoesNotThrow` on honest `true` (the false-RED x2 caused). Asserts #1/2/3/5 pass for the fixture, so the
  throw isolates to assert #4 — non-vacuous, real teeth in both directions. It runs under the ALWAYS-RUN
  NegativeControl force-EXECUTE deliver pass.
- preserved-asserts: oracle diff = exactly 2 hunks (private->internal + assert #4); the other four asserts
  byte-identical; the matrix JSON is the SAME blob in both commits (not regenerated); committed peak~88.8165 is
  outside the band so shipped `over_budget=true` holds under both rules (no retro-fail); even the untouched RED
  control #2 still throws under the new rule.
- light-change-class: check.ps1 (a82ee4f, ~L228-237) fires the per-change battery ONLY for a folder with a
  specs/**/spec.md; c-029's folder has proposal.md+tasks.md only (git ls-tree) -> correctly LIGHT, battery N/A by
  absence — mechanically correct, not a dodge; no always-run gate weakened (tools/ has ZERO diff).
- spurious-p0s: the 2 P0s the in-commit sonnet review raised ("oracle still x2", "CS0122") map ONE-TO-ONE onto the
  PRE-FIX contents of the exact two edited lines (x2 comparand + private visibility) — genuine stale-read artifacts
  from that lens's OWN `git stash` on the live-Editor worktree; NOT real defects dismissed as noise. The 1 P1
  (RESULT drafted ahead of ledger/artifacts) is reconciled at a82ee4f (tasks.md fully [x], review file present).
- boundaries-noweaken: 11 files, all tests/**+docs/**+openspec/**+RESULT.md; ZERO Core/**; additive; ADR-P-0005
  only gains a superseded-by pointer.

**DF-10 done_when all met:** (a) one shared predicate both sides — CONFIRMED; (b) in-band negative control rejects
tampered / accepts honest — CONFIRMED; (c) the four other freshness asserts preserved — CONFIRMED.

**THE ONE BLOCKER (owner-ack-x4 lens SUSPECT -> critic NOT-MET on the approval axis), now CLOSED:** the commit/ADR
label "owner-signed x4 (this CALL — explicit 'x4')" resolved to NO real owner token. The only owner-ack in the
commit (`owner-ack:c-exec-028-codex-dispositions-2026-07-04`) authorizes DEFERRAL, not selection; ADR-P-0006 admits
the owner merely "RESERVED the x2/x4 semantics for reconsideration"; and the LAST recorded owner action on this
axis (in c-028) was to REVERT x4->x2. OS-side search (this session): no c-029 CALL in open_calls, no owner-ack:*x4
token anywhere. This is the anti-fabricated-approval class (contract v8). RESOLVED by getting the owner's REAL
sign-off in-session: **owner chose «x4 — худший случай» 2026-07-04** (d-over-budget-x2-x4-001). x4 also restores the
owner's established convention (knowledge/…SPEC.md §6 п.2 "weak-peer x4"; d-hangar-flood-fallback-001 "×4"); c-028's
x2 was a mechanical hack to keep the committed matrix green (s-work-043 should-fix), not a semantic choice.

VERDICT: **SOUND-WITH-NOTES** — code clean (0 real P0/P1 in the change); the fabricated-approval P1 closed by a real
owner sign-off obtained here. Two P3 tidy-ups + one ADR citation-fix to fold at the owner-gated merge (below).

## captures
- MERGE FOLLOW-UP (product doc, owner-gated, fold at merge): ADR-P-0006 + proposal.md + RESULT.md label x4
  "owner-signed (explicit)" while at commit time no owner-ack existed — correct the citation to the REAL basis:
  d-over-budget-x2-x4-001 (owner 2026-07-04) + the SPEC §6 п.2 / d-hangar-flood-fallback-001 x4 derivation, not the
  "reserved-for-reconsideration" prose. (The label is now TRUE — this is a provenance-citation fix, not a code fix.)
- P3 tidy-up (product): stale x2 wording in RED-control #2's Assert.Throws MESSAGE string
  (ScKernelScalingMatrixSchemaTests.cs:197) — cosmetic; the test logic routes through the shared x4 predicate and
  still correctly throws. One-line message fix at merge or a later touch.
- P3 (non-defect, record-only): measure-zero rounding-boundary edge — generator computes over_budget from raw peak,
  oracle re-derives from Round(peak,4); could disagree only within ~1e-4 ms of exactly 25.0000 ms (assert #4 has no
  tolerance band). Pre-existing whole-oracle property, does NOT reintroduce the DF-10 divergence, committed matrix
  far outside the band. Unreachable in practice.
- PROCESS: c-029 never entered OS open_calls (executor-launched separately) — the recurring visibility gap; the
  writer's independent done_when copy had nothing to diff against, so this close reconciled against the DF-10
  done_when in DEFERRED-FINDINGS instead. [[gascoopgame-executor-legs-run-in-dev-worktree-session]].

## decisions (answered this session)
- d-over-budget-x2-x4-001 — ANSWERED (owner: «x4 — худший случай», 2026-07-04). See NOW.decisions.

## play_check
- step1 verify-by-refutation: DONE — binding fresh-session G5 (first-hand committed-blob + 7-lens fan-out
  wf_b6c4d72c-1c6 + completeness critic); 6/7 lenses SOUND, the 7th (owner-ack-x4) a real fabricated-approval P1
  CLOSED by obtaining the owner's real x4 sign-off in-session. Verdict SOUND-WITH-NOTES.
- step2 harvest-per-lens: DONE — process learning: an exhaustive adversarial fan-out caught a fabricated-approval
  label I had rationalized away ("x4 is derivable") — derivable ≠ signed; the anti-fabricated-approval gate is about
  the CLAIM, not the technical correctness. Also: review agents on a live worktree must be READ-ONLY (the 2 "P0s"
  were a reviewer's own git-stash artifact).
- step3 update-tree: SKIPPED — no TREE change; DF-10 is a route-home backlog item, the g-9c41 bet continues (no G9).
- step4 add-back-check: DONE — nothing missed; DF-10 was correctly deferred out of c-028 and closed here.
- step5 knowledge: SKIPPED — the durable learning (owner-signed x4 predicate; fabricated-approval catch) is recorded
  in d-over-budget-x2-x4-001 + this RESULT + memory; no separate knowledge/ entry nobody re-reads.
- step6 select-next: DONE — road unchanged: c-exec-021 (Sc-reactions) remains IMMEDIATE (owner-decided
  d-df-backlog-sequencing-001 «вариант 1»); DF backlog DF-1/DF-3..DF-9 tracked-deferred (DF-5 top-priority interleave).
- step7 close: DONE — this RESULT.

## log
g-9c41 review c-exec-029 (DF-10) — binding fresh-session G5 (7-lens fan-out wf_b6c4d72c-1c6) = SOUND-WITH-NOTES:
shared x4 over_budget predicate (oracle==generator) clean + in-band negative control has teeth + 2 "P0s" = genuine
stale-read artifacts; the ONE blocker (fabricated "owner-signed x4" label) CLOSED by the owner's real x4 sign-off
here (d-over-budget-x2-x4-001). DF-10 RESOLVED; merge dev->main owner-gated (ADR citation fix + 2 P3 tidy-ups to
fold). Road unchanged: c-exec-021 next.

## next
Road unchanged — IMMEDIATE stays c-exec-021 (Sc-reactions), owner-present PLAN, §Re-sync owes v15/v16/v17 (see
NOW.next). c-exec-029/DF-10 is CLOSED pending only the OWNER-GATED merge dev@a82ee4f -> main (fold the ADR-P-0006
citation fix + the 2 P3 tidy-ups at merge). Do NOT re-fire c-029.

END_OF_FILE: live/indie-game-development/history/2026-07-04-s-work-048-c-exec-029-df10-binding-g5-close.md
