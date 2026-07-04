CALL c-exec-026
to: executor
kind: engineering
direction: indie-game-development
node: g-9c41
repo: C:\projects\Unity\GasCoopGame_dev
surface: cli
goal: |
  GasCoopGame's deliver gate enforces os/engineering contract v14: the property-layer (v12),
  refuted-register (v13) AND fix-class-closure (v14) axes become executable deliver dependencies
  with seeded-miss self-tests, and the repo stamps synced_contract_version 11→14. Strictly additive
  — no existing green gate weakened; every currently-delivered leg still delivers.
  (v14 is the fix DIRECTLY targeting the owner's "review loops every task" pain: a fixed finding
  closes only with a recorded class sweep, and a recurring class re-opens the fix — the first
  mechanical non-convergence hook. It is INERT in this repo until this §Re-sync wires it.)
context: |
  - Repo is at synced_contract_version 11 (v10 tools/review-check.ps1 + v11 tools/negative-control-check.ps1
    already wired with self-tests in check.ps1 -Deliver — verified). The debt is v12 + v13 + v14.
  - Binding contract text (workflow repo, at v14 on main — read for the gate detail, do not re-derive):
    C:\my_global_workflow\os\engineering\VALIDATION.md (§Property-layer, §Refuted-register, §Fix-class-closure),
    PROJECT_SETUP.md (§Strong-check clauses (f) property-layer, (g) refuted-register, (h) fix-class-closure
    + Done-when seeded-miss), CONTOUR.md (PROPERTY AUDIT stage + §b register walk + "A FIX IS A CHANGE"
    records the sweep BEFORE `fixed`), CONTRACT_VERSION (log lines 12, 13, 14).
  - v14's writer-side keystone is ALREADY live OS-side (coding-agent.md G10, keyed on the RESULT's own
    content — a fixed-finding report without per-finding class+sweep bounces at carry-back). This §Re-sync
    adds the PRODUCT-side teeth: the in-repo deliver check that catches it before the RESULT ever leaves.
  - Templates to MIRROR (identical -SelfTest seeded-miss + -Repo/-ChangeId per-change shape, each wired into
    check.ps1 -Deliver by a self-test call + a per-change loop): tools/review-check.ps1 (v10),
    tools/negative-control-check.ps1 (v11), tools/escape-class-check.ps1 (v9). tools/coverage-check.ps1 is
    where the v12 prop: token joins the existing exists:/approach-token logic.
  - Grandfather precedent already in validation.config: review_evidence_grandfathered /
    negative_control_grandfathered / escape_class_walk_grandfathered (the pre-convention non-archived set).
  - Expanded itemized scope, REFUTED.md seed cases, and per-part done_when live in the "Expanded scope"
    section BELOW this packet (same file) — input evidence for the planner, not a binding spec.
  - Base off a clean main (@38ab715; merge the delivered c-exec-025-w1b first, or a fresh worktree off main).
boundaries: |
  - Additive only: no existing gate/self-test weakened; the full pre-existing -Deliver battery stays green.
    If a new gate would retro-fail an already-delivered non-archived leg, GRANDFATHER that leg (owner-governed
    validation.config list) — never loosen the gate. This is the hard invariant of every §Re-sync.
  - v12 is PILOT: wire + prove via seeded-miss + grandfather all current changes; do NOT retrofit prop: tokens
    onto delivered core files or c-exec-025. Real bite = the next new core-algorithm change.
  - INFRA ONLY: tools/**, validation.config, docs/reviews/REFUTED.md, docs/adr/**, docs/FRICTION.md. No
    Core/Field/sim code, no goldens, no feature acceptance tests. Engine worktree GasCoopGame_dev — NEVER dev_2.
  - STOP + escalate as an owner decision (never a silent default): if detecting the `core algorithm` change-class
    (the v12 trigger) has no existing convention to key on; or if CsCheck cannot be added under license/offline
    constraints (propose FsCheck 3.x — do not skip the property framework).
done_when: |
  v13 refuted-register: docs/reviews/REFUTED.md exists (schema row-id|seam/invariant|claim|why-refuted|marker|
  review-id|date), seeded with the real prior refutations (buoyancy per-band rejection; checked-arithmetic/
  CheckForOverflowUnderflow-on-core rejection; the FRICTION 2026-07-02 REFUTED list). tools/refuted-register-check.ps1
  mirrors review-check.ps1 and its -SelfTest goes RED on each of: a refuted finding with no refuted-register: line,
  a register line naming a row absent from REFUTED.md, a register:<row-id> marker resolving nowhere — GREEN on a
  well-formed review; wired into check.ps1 -Deliver (grandfather-aware). review-check.ps1 accepts register:<row-id>
  as a valid refutation marker only when it resolves. The spec-silence/escape-class walk marks a REFUTED row that
  names a seam the frozen spec touches still-holds|re-opened (unmarked touching row FAILs). validation.config gains
  refuted_register_grandfathered.
  v12 property-layer (PILOT): CsCheck added under a [Category("Property")] convention; coverage-check.ps1 requires,
  for a change whose PLAN change-class is core algorithm, a prop:<TestClass>.<TestMethod> token per headless
  deliverable-coverage row, matched to an owner-signed property table in the frozen spec naming the test per class
  (permutation-metamorphic, fault-injection-all-exit-paths, multi-actor-one-tick, boundary-biased); its -SelfTest
  goes RED on a missing token, a token naming a non-[Category("Property")] or table-absent test, and a table missing
  one of the four classes — N/A for a non-core-algorithm change. validation.config gains property_layer_grandfathered
  (all current changes).
  v14 fix-class-closure: in docs/reviews/review-<id>.md, a `fixed <commit>` finding disposition closes ONLY
  with a recorded `sweep:` line — a class token, each sibling site closed `<commit>|n/a because <reason>`, PLUS
  a seeded-miss/negative-control token per class VARIANT when the finding is itself a gate/scan/oracle false-green
  (the c-visual-004 pattern: a //-only fix must carry the /* */ + commented-include + raw-text variants). A
  later-round finding row whose `invariant/class` equals an earlier `fixed` row's class RE-OPENS that row and
  counts as ONE recurring class toward the rounds/escalation cap (the first mechanical non-convergence hook —
  a string-compare inside the review file, not anyone's memory). Extend tools/review-check.ps1 (or a sibling
  fix-class-check.ps1): -SelfTest goes RED on (a) a `fixed` disposition with no `sweep:` line, (b) a later-round
  finding matching an earlier fixed row's class that was not reopened; wired into check.ps1 -Deliver. CONTOUR's
  "A FIX IS A CHANGE" records the sweep BEFORE `fixed`. validation.config gains a v14 grandfather list for the
  current non-conforming non-archived changes.
  Closure: validation.config synced_contract_version 11→14 with its note appended (v12+v13+v14 lines, same voice as
  v6–v11); tools/check.ps1 -Deliver GREEN end-to-end on the repo as-is (new self-tests pass AND every currently-
  delivered non-archived leg still delivers via grandfathering — transcript attached); ADR-P-0004 records the
  re-sync (what wired, grandfather rationale, v12 PILOT scope); a FRESH-session different-model-family G5 refutes
  that each seeded-miss truly goes RED-without-fix / GREEN-with-fix (not a self-authored green), recorded in
  docs/reviews/review-c-exec-026-resync.md (this frozen infra change itself satisfies the v10 review-evidence gate).
return: |
  RESULT routed HOME to indie-game-development/g-9c41: commits + the full check.ps1 -Deliver transcript (green,
  showing the new self-tests and the grandfathered-skip lines), the two new/extended scripts, REFUTED.md with its
  seed rows, the two grandfather lists, the bumped stamp, ADR-P-0004, and the fresh-session G5 refutation record.
  dev→main merge + push OWNER-GATED. next = return to g-9c41 (the §Re-sync debt is cleared; the feature road
  resumes at c-exec-021 Sc-reactions).
budget: |
  One infra leg, but THREE contract versions (v12 + v13 + v14). Natural split if the fire-time estimate exceeds
  ~2× a focused half-day: {v13 refuted-register + v14 fix-class-closure} first — both extend the SAME review-file
  structure + tools/review-check.ps1, and both have their writer-side keystone already live OS-side, so they are
  the coherent lighter half — then {v12 property-layer} (the CsCheck framework add) as a second CALL; escalate the
  split. No new runtime dependency beyond CsCheck (that IS the approved v12 mechanism, not a scope change).

---

## Expanded scope (context for the planner — input evidence, NOT a binding spec)

Itemized done_when, split at the natural v13 / v12 seam. Mirror the existing `-SelfTest` + per-change gate shape.

**Part A — v13 refuted-register:**
1. `docs/reviews/REFUTED.md` — schema `row-id | seam/invariant | claim | why-refuted | marker | review-<id> | date`, SEEDED so the register is not born empty: the ratified buoyancy per-band rejection (per-species TEMPERATURE is the named seam; Codex's period-2 fix rejected), the v12 "checked arithmetic / CheckForOverflowUnderflow on core" rejection (defined-wrap is a protected lockstep-determinism contract), and the workflow FRICTION 2026-07-02 REFUTED list (Russian red-test manifest; STOP-4 deviation veto; unsigned in-repo hash approvals; InspectCode). Each row carries its original marker.
2. `tools/refuted-register-check.ps1` (mirror `review-check.ps1`): for each `docs/reviews/review-<id>.md` carrying a `refuted` finding, the review has a `refuted-register:` line naming the appended row id(s) (`none` legal ONLY with zero refuted rows), and every `refuted` finding resolves to an existing `REFUTED.md` row; a `register:<row-id>` marker must resolve. `-SelfTest` seeded-miss RED on: (a) refuted-with-no-register-line, (b) register-line-naming-absent-row, (c) register-citation-resolving-nowhere; GREEN on a well-formed review. Wired into `check.ps1 -Deliver` (self-test call + grandfather-aware per-change loop).
3. `tools/review-check.ps1` extended: `register:<row-id>` accepted as a valid refutation-verification marker (alongside `G5|KERNEL-G5`) ONLY when it resolves to a REFUTED.md row. Its `-SelfTest` gains a positive (register-cited refuted PASSES) and a negative (resolving-nowhere FAILS). No existing case weakened.
4. Spec-silence / escape-class walk (`tools/escape-class-check.ps1` or the audit it drives) extended: a `REFUTED.md` row naming a module/seam the frozen spec touches must be marked `still-holds | re-opened <why>` — an unmarked touching row FAILs deliver. `-SelfTest` seeded-miss for the unmarked-touching-row case.
5. `validation.config` gains `refuted_register_grandfathered` (the current non-conforming non-archived set), owner-governed note.

**Part B — v12 property-layer (PILOT):**
6. CsCheck added to the test project (FsCheck 3.x only if the repo already carries F# — it does not) under a `[Category("Property")]` convention; the property suite runs (match how NegativeControl/Benchmark categories are handled in `check.ps1`).
7. `tools/coverage-check.ps1` extended: for a `core algorithm` PLAN change-class, every `headless` deliverable-coverage row carries a `prop:<TestClass>.<TestMethod>` token (same mechanical form as the existing `exists:` for engine rows) matched to an owner-signed `## Property coverage` table in the frozen spec naming, per class, the `[Category("Property")]` test that discharges it: **permutation-metamorphic, fault-injection-all-exit-paths, multi-actor-one-tick, boundary-biased**. `-SelfTest` seeded-miss RED on: (a) core-algorithm headless row with no `prop:` token, (b) token naming a table-absent or non-`[Category("Property")]` test, (c) property table missing one of the four classes; GREEN on a conforming core-algorithm change; N/A (delivers) for a non-core-algorithm change. Wired into `check.ps1 -Deliver`.
8. `validation.config` gains `property_layer_grandfathered` (all current non-archived changes — PILOT, no retrofit), owner-governed note.

**Part C — v14 fix-class-closure (the owner's "review loops every task" fix):**
12. In `docs/reviews/review-<id>.md`, a `fixed <commit>` finding disposition closes ONLY with a recorded `sweep:` line: a class token, each sibling site closed `<commit>|n/a because <reason>`, PLUS a seeded-miss/negative-control token per class VARIANT when the finding is a gate/scan/oracle false-green (witness c-visual-004: a `//`-only strip must also carry `/* */`, commented-include, raw-text).
13. A later-round finding row whose `invariant/class` equals an earlier `fixed` row's class RE-OPENS that row and counts as ONE recurring class toward the rounds/escalation cap — the first mechanical non-convergence hook (string-compare inside the review file, not memory).
14. Extend `tools/review-check.ps1` (or a sibling `fix-class-check.ps1`): `-SelfTest` RED on (a) `fixed`-without-`sweep:`, (b) a later-round finding matching an earlier fixed row's class not reopened; wired into `check.ps1 -Deliver`. CONTOUR "A FIX IS A CHANGE" records the sweep BEFORE `fixed`. `validation.config` gains a v14 grandfather list.

**Both — closure:**
9. `validation.config: synced_contract_version` 11→14 + note appended (v12 + v13 + v14 lines, same voice as v6–v11).
10. `tools/check.ps1 -Deliver` GREEN end-to-end on the repo AS-IS (all new self-tests pass AND every currently-delivered non-archived leg still delivers — run it, attach the transcript). ADR-P-0004 records the re-sync.
11. Binding G5: a FRESH read-only different-family session refutes that each seeded-miss truly goes RED-without / GREEN-with; verdict in `docs/reviews/review-c-exec-026-resync.md`.

END_OF_FILE: live/indie-game-development/work/c-exec-026-resync-v12-v13-call.md
