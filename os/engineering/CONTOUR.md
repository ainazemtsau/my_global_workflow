# Engineering contour — how product code gets built

The second loop of the OS: what happens after a `call:executor (kind: engineering)` leaves a direction. The direction sends a business task; this contour owns everything from plan to verified code. Files here are read by coding agents (Claude Code / Codex / any), not by chat sessions.

Companion files: `PROJECT_SETUP.md` (bootstrap a product repo), `VALIDATION.md` (the gate pipeline), `TOOLING.md` (what tools are in/out and why). PROJECT_SETUP installs this contour's distilled **run contract** into each product repo's root AGENTS.md — the repo is self-sufficient at run time; this file stays the source.

## Boundary with the direction

- The direction (chat sessions) owns WHAT and the acceptance bar: outcome, business-level done_when, boundaries, budget, evidence pointers. It never prescribes architecture, design, or file layout.
- A CALL never licenses a silent downgrade, and names the ONE approach it exists to prove. The direction may mark a capability DESIRABLE-not-required, but it may NOT write a standing "ship the lesser form if the real one is costly/hangs" clause — any fallback from the named approach routes through ESCALATE (an owner decision), never a blanket in-CALL permission. When a `done_when`'s substrate/approach is load-bearing it is named as ONE token (an `approach:` / `de-risk-target:`), NOT a disjunctive "X OR a lesser Y": the coverage row echoes that token, so a substituted mechanism is a string-mismatch the gate and the writer catch (VALIDATION.md, coding-agent.md), not a silently-conforming alternative. A disjunctive or downgrade-licensed acceptance bar is a CALL-authoring defect the shape/converge session owns.
- The contour owns HOW: architecture, design, implementation, validation. Architecture is decided in PLAN — with the owner, in the product repo — and recorded there (ADRs, change specs, module docs). It never lives in direction state; business-relevant assumptions return via REPORT into the direction's review.
- Design exploration from chats (`work/` docs, research findings) arrives as CALL context pointers: input evidence, never a binding spec.
- Feasibility questions ("can this be built within budget at all?") are direction work (research/work spikes); solution design belongs to PLAN.
- **CALL budget (v35).** An engineering CALL carries at most THREE `done_when` bullets; more needs the owner's written
  over-budget token quoted in the CALL. Measured here, one bullet becomes 10-14 acceptance rows, so five is already a
  leg that has never shipped. This activates X44. The direction owns the number: it is the only place leg size is set
  before work starts.

## Roles (always separated)

**Validator write boundary (contract v24).** "Read-only" forbids the validator from authoring or editing source, tests, specs, rules, and evidence. It may invoke declared validation runners whose only writes are generated evidence artifacts/caches; it never edits those outputs.

### Contract v29-v34 roles for newly issued compiled product-code legs

Snapshot calls stay legacy; new roots pin their version.
V30-v34 retain v29 pair roles/gates.
For issued roots, Re-sync preserves feature routes; v34 adds only process-close.

For a v29 compiled leg, PLAN HOME names PAIR-CANDIDATE eligible. One fresh contract-author — the independent
test-author, never the builder or validator — owns the bounded pre-freeze job. It may revise both the smallest
compiler-green real public carrier and tests/support until the real command compiles, discovers the intended tests and
fails on behavior. Carrier edits stay inside the approved construction/observation surface and contain no behavioral
implementation. Intermediate carrier gaps stay inside this job; its handoff is only the final candidate pair or one
complete blocker after the retry cap. Binding fresh refutation then freezes the public contract+RED pair. Pair
refutation and BUILD are separate sessions from the one that authored the pair and from each other. V35: PLAN and
PAIR-CANDIDATE may share a session — the boundary that matters is between whoever authors the oracle and whoever
implements against it.

- **Builder** — autonomous session(s), default-tier model, a FRESH session reading the reviewed carrier+RED pair (never the session that authored it). Never talks to the owner mid-run.
- **Validator** — fresh-context, read-only (no Write/Edit), did not author the code; independence is established by authorship, context and authority separation, never by model identity: equal builder/reviewer model provenance is legal, and model availability cannot block review or delivery. It judges a committed ref, never a shared working tree: uncommitted bytes in a reused slot are not a finding.
- **Contract-author** — owns the whole oracle. Reads the CALL, the decision page and the existing repo, stops for the
  owner's approval of that page, then owns the spec's machine-read sections, the
  non-behavioral public carrier and the complete `behavioral-red` tests/support. It
  may correct carrier gaps and rerun RED inside that one job; it never implements behavior or weakens/omits an
  approved behavioral row. The final history records a carrier commit followed by a tests/support commit. Fresh review freezes
  the public contract and RED files; the builder makes the tests pass and may edit neither. Process, structural-review
  and final-gate obligations are
  `evidence-only`, never fake tests. Not the builder and not the validator. For a `core algorithm` change the same role
  returns for a second, POST-build pass (see cycle, PROPERTY AUDIT): once gates are green it reads the actual DIFF — the
  one artifact neither the frozen spec nor the pre-code pass could see — for new throw-paths, seams, order-dependencies,
  and derived-value ranges the implementation introduced, and appends property tests for them before REPORT.

**Mutation-review duty (contract v24).** For G2 the validator independently derives the changed mutation-eligible Core/source files from the authoritative diff and runs mutation; a builder-produced scope, report, or score is not evidence. Runner-generated output does not authorize source, test or rule edits.

**Mutation diff identity (contract v24).** Independent review evidence pins mutation-reviewed `H`; the report only echoes repo-derived `I` (declared integration-base tip), `B = merge-base(I,H)`, and `H`. Deliver recomputes and exact-matches them, rejects mutation-input changes after `H`, and handles renames/deletions per VALIDATION before it reads score.

**Extension rule.** Existing product code may already exist. Under v29-v34 the pair candidate pins its real signatures by
commit instead of copying constructors and harness facts into prose. The contract-author never invents a test-local
substitute: a missing approved construction/observation seam is added to the non-behavioral carrier; a seam outside the
approved decision page stops with one complete blocker.

**Applicability.** PAIR-CANDIDATE is the carrier only for compiled product-code legs where a repo-native compiler can
check the public surface. A markdown or other non-compiled repository must not copy the C# skeleton mechanics: it
needs its own native executable carrier, or an explicit `n/a` / separate owner decision at that repository's re-sync.

## The cycle

### Contract v29-v35 compiled route

For compiled product-code legs the operative path is:

```
PLAN -> PAIR-CANDIDATE -> binding fresh PAIR-FREEZE refutation -> BUILD -> VALIDATE
```

**V35: the frozen contract is code, not prose.** A leg freezes its spec's machine-read sections, the compiling carrier
and its RED tests. No `PLAN.md` is a frozen artifact, a gate input, or launch authority: every gate naming it reads its
path or blob hash, never a sentence.

PLAN keeps its stage and receipt and stops being a separate session: one session may close PLAN and PAIR-CANDIDATE,
writing both receipts in order. Its surviving duties — acceptance ledger, spec-silence audit, deliverable coverage,
the `behavioral-red | evidence-only` split — are recorded in the spec, which is what the gates read. The owner approves
one artifact: the decision page, at most 400 words = whitespace tokens over the whole file, the only ruler, every
fixture on it fully defined (inputs, domains, mappings) or absent.

PAIR-CANDIDATE is fresh of BUILD. Its final history is an exact carrier commit followed by an exact
tests/support commit. The carrier contains or pins the decision page and a compiling skeleton of the real public
surface. It uses real signatures; data/value construction preserves fields and trivial reachability, while behavioral
bodies remain unimplemented. Acceptance meaning may not move into `///` comments. The commit and Git manifest define
scope; prose folder lists do not. There is no production-line quota: normal formatting remains mandatory, while the
real-signature, field-preservation, trivial-reachability and no-behavior boundaries prevent source compression theater.

Within that one job the contract-author may revise the carrier as its tests expose gaps, but only inside the approved
construction/observation surface. After the last carrier edit it reruns repo-native build, hygiene and the real test
command on the final pair. Mandatory sidecars are tracked in the carrier commit; unavailable real importer/engine keeps
the existing tool-unavailable STOP. Tests must compile, be discovered and fail on behavior. An intermediate permitted
gap never creates a HOME/CALL/branch relay; a required behavioral or out-of-plan change returns one complete blocker.

Fresh refutation freezes the exact public contract+RED after inspecting their commits/manifests/diffs and evidence. BUILD pins both and changes neither.
After Re-sync 34, Direction may process-close a non-released v30+ root under its feature pin, adding no v34 feature gates. Pins/ref/receipts/manifests survive; a current-pinned replacement starts clean at the earliest affected stage.
Only exact-input evidence carries; superseded files are absent from replacement `HEAD` and gates but stay in history.
Until `RELEASED`, each v31+ root's frozen paths/blobs match its `HEAD` before exemptions; mismatch STOPs.

V29/legacy stages return HOME. V30-v34 roots advance separate fresh stages from committed progress receipts, never an
in-session substitute, and return HOME as REPORT/ESCALATE/REPLACED. Issued routes survive Re-sync.

The legacy cycle text below remains authority for every other gate and artifact; its old carrier wording does not
override the route pinned by the engineering CALL.

```
CALL (business task from a direction)
  → PLAN: the contract-author first names the change class — module
    boundaries / new module / new dependency / core algorithm (simulation,
    netcode, determinism) / data formats / perf-critical path / user-
    perceivable behavior (what the person the product is for directly
    experiences — sees, hears, feels, reads: how a mechanism looks, settles,
    or sounds; how output is paced, shaped, or phrased) touched =
    architectural: options with a recommendation, an owner conversation,
    an ADR; none touched = light: a short plan, one-message approval. For a
    user-perceivable change the OBSERVABLE behavior is an owner-signed
    acceptance PROPERTY (the implementing formula/magnitude stays HOW, the
    ADR records it) — never a builder default, surfaced beside the
    engineering decisions the owner already confirms.
    Then it interviews the owner if needed and writes the change spec:
    per-feature acceptance criteria as a machine-readable ledger (all
    entries start failing), plus the verification plan the validator
    approves BEFORE any code. Four spec-hardening checks before freeze:
    (a) when the change EXTENDS a working/frozen system, list the invariants
    that held in the old regime and, per one, whether this change can falsify
    it — falsifiable ones become failing criteria tested in the new regime;
    (b) name what the spec leaves UNCONSTRAINED (which regimes / actor-counts /
    seams / user-perceivable regimes — e.g. uniform vs gradient field, sparse
    vs dense, asymmetry) and mark each silence intentional or not — unintended silences
    become spec lines, since a test can only cover what the spec names.
    It also marks every load-bearing DERIVATION the plan ASSERTS — a stated bound, ground or
    law — `proved <where>` or `owed`; an `owed` one is discharged, proved or refuted, before
    any test, fixture or control depends on it, because a written ground is not evidence.
    This audit — the marked list — is RECORDED in the change spec, not just discussed:
    the deliver gate checks its presence (PROJECT_SETUP §Strong-check enablement), so a
    silence audit that happened only in chat is not enabled and the leg is not deliverable.
    The audit WALKS the cross-kind escape-class registry (os/engineering/ESCAPE-CLASSES.md)
    row-by-row, marking each class `addressed | n/a because <reason>` — an unmarked class is a
    deliver FAIL the same as a missing section, which turns "the author remembered the class"
    into "every class we have ever been bitten by was discharged" (the registry grows by the
    ratchet — MAINTENANCE step 6; a fresh audit authored from examples is what let end-state and
    derived-overflow escape even though §b already named "uniform vs gradient field"). The walk
    ALSO covers the repo's refuted-register (`docs/reviews/REFUTED.md`, VALIDATION
    §Refuted-register): a register row naming a module/seam this change touches is marked
    `still-holds | re-opened <why>` — an unmarked touching row fails deliver the same as an
    unmarked class. And for
    each surfaced must-hold property the audit names not only a catcher but the REGIME it must hold
    under (environment / accumulated time or inputs / the transition path, not only the settled
    instant) and confirms the catcher EXERCISES it: a catcher that can go red but only runs the
    nominal instant is green where the bug does not live — the same hole as a prose-only gate.
    (c) DELIVERABLE COVERAGE: the spec records the CALL done_when VERBATIM and maps EACH
    done_when bullet (and each owner-locked PLAN decision) to ≥1 ledger row OR an explicit
    out-of-scope line — the list is indexed by the PROMISES, not by what got built, so a
    promised artifact cannot be silently left off (a bullet with no disposition is a coverage
    FAIL). Each row RECORDS the bullet's CLASS — `headless` or `engine` — and the gate keys on it,
    so engine-vs-headless is a recorded property, NOT the builder's choice of evidence token (the
    one judgment this check exists to remove). An `engine` artifact (a scene, prefab, composer,
    adapter) disposed as built MUST close on a RECORDED existence proof — a committed path under
    the artifact root (e.g. `Assets/**`, `docs/measurements/**`) the deliver check Test-Paths, or a
    recorded MCP/batch-run artifact carrying a non-trivial measurement (node/cell count) — and may
    NEVER be discharged by a sibling headless test name, an empty/stub file, a directory, or an
    arbitrary pre-existing file (this is the exact leg-8 lie: an unbuilt composer reported done by
    citing unrelated tests). BUILD (the artifact exists) and LOOK
    (the owner likes it) are separate: an owner-acceptance / eyeball axis defers only the LOOK,
    and only AFTER the existence row is green — it never stands in for the BUILD. A
    user-perceivable / engine-side deliverable is architectural by definition (above), so the
    planner MUST give it a frozen spec; the coverage gate binds it only once it has one, so
    mis-classifying an engine deliverable as a "light" change (no frozen folder) escapes coverage
    — a classification defect the validator/owner catches, not yet a gate tripwire (FRICTION-watch).
    Cutting a promised deliverable is allowed but NEVER silent: an out-of-scope line on a
    done_when bullet needs a recorded OWNER decision (signed at plan approval, or a mid-run
    ESCALATION) — a self-authored cut of a promise is a coverage FAIL, not a disposition. This
    list is RECORDED in the spec; the deliver gate checks it (PROJECT_SETUP §Strong-check
    enablement) and the writer re-checks it on carry-back (os/adapters/coding-agent.md).
    (d) SPEC-TO-CARRIER HANDOFF: split mixed rows into atomic obligations, then classify each exactly once as
    `behavioral-red` or `evidence-only`; one row may never straddle both classes. A behavioral row names its observable
    obligation, source, negative and eventual test identity. Constructors, signatures, literals and framework calls are
    no longer copied into prose as a compile surrogate; the CALL-pinned carrier route supplies real signatures and the
    fully-defined-fixture decision page. A process-order, structural-review,
    owner-verdict or final-gate row is `evidence-only`: it names its real evidence route and
    is excluded from the RED-test count — it may not be dressed as an Arrange/Act/Assert test.
    A filled table or English skeleton is never `N/N executable` and never authorizes
    BUILD. Only actual pair-candidate evidence plus its binding fresh refutation does. A spec change invalidates every
    affected RED artifact; only unaffected exact-input evidence may cross a replacement lineage. A narrow blocker close never authorizes BUILD by itself. This is
    semantic AI review plus the real consumer artifact, not a new parser/regex/conformance tool
    (VALIDATION Executable Plan-to-RED handoff; MAINTENANCE semantic-review boundary).
    What the owner approves is the 400-word decision page: the goal in plain
    words, EACH technical decision spelled out (plain-language what + why), and
    what is cut or deferred. The machine spec / ledger / ADR ride ALONGSIDE it
    and are NOT what he reads to approve.
    Owner approval closes PLAN; v29 returns HOME and v30-v35 commits its receipt. PAIR-CANDIDATE follows and may share
    that session (v35); prose never opens BUILD, and the author of the oracle is never the builder.
  → PAIR-CANDIDATE (fresh of BUILD): the contract-author creates the non-behavioral public carrier
    and complete behavioral tests/support, fixing approved carrier gaps inside this job. It never implements behavior,
    invents test-local production substitutes or drops a planned row. The final carrier commit passes build+hygiene;
    its child RED commit compiles, discovers the intended tests and fails on behavior. Compile-RED, partial suites and
    unexplained diagnostics are ineligible. Record both commits/manifests, changed paths, commands and failure evidence.
  -> PAIR FREEZE (binding fresh refutation): the fresh read-only review inspects the carrier candidate, actual RED
    commit/diff and runner evidence, tries to refute completeness and no-behavior boundaries, and freezes the public
    contract+RED pair. It authors neither. Only this artifact-backed verdict may open BUILD.
  → BUILD (autonomous): a fresh builder starts from the reviewed pair, never changes its public contract or RED, and
    implements one feature at a time, smallest-first.


    Make-time obligations on any tests the builder writes itself too: assert
    every value-bearing/measured field EQUAL to its source (not merely
    present), and for any feature with >1 concurrent actor exercise multi-actor
    / conflicting-input-in-one-tick regimes, never a single-actor happy path.
  → VALIDATE (per feature and per change): gates in VALIDATION.md.
    The independent review (G4) and fresh-session refutation (KERNEL-G5) are
    RECORDED in `docs/reviews/review-<id>.md` (id == the openspec change folder;
    `reviewed-commit` an ancestor of the delivered HEAD with every intervening
    source commit a `fixed <commit>` disposition; every finding dispositioned,
    none `open` (in-scope only; a class-sibling the class search surfaced
    routes to the direction's backlog with a `routed` pointer, not gating this
    leg — VALIDATION §Review-evidence (iii)); every `refuted` carrying a
    G5/KERNEL-G5 verification marker
    and ALSO appended as a row to the repo's cumulative refuted-register
    `docs/reviews/REFUTED.md`, so the disagreement outlives the leg — a later
    review CITES the register (marker `register:<row-id>`) instead of
    re-litigating, and a re-raise carrying NEW evidence escalates to the
    owner, never citation-closed (VALIDATION §Refuted-register);
    `rounds` ≤3 or a resolving `escalation:<id>`), which the deliver gate checks
    for presence/freshness/structure (VALIDATION §Review-evidence, PROJECT_SETUP
    §Strong-check) — so a leg can no longer reach done before an independent
    review round is recorded; a review whose tree has since changed with
    un-accounted source commits is stale and FAILs.
    Builder may not edit the ledger or the spec; flipping a ledger entry
    to passing requires opened evidence (hook-enforced where supported).
  → RETRY policy: ≤2 retries in-context; then one fresh-context retry with a
    rewritten prompt; the same finding class recurring twice = non-convergence
    → stop early. Hard cap: 3 retries per gate.
  → A FIX IS A CHANGE, not a patch: a fix made during VALIDATE/RETRY that ADDS
    or CHANGES behavior (a new guard, a reordering, a check that can throw) re-
    triggers the spec-hardening checks (a)/(b) on the fix — explicitly on the
    NEW failure/exception paths it introduces: a guard that throws must keep the
    old-regime invariants (tick atomicity, conservation, non-negativity) intact
    ON the throw path, and each becomes a failing criterion the test-author
    writes RED before the fix (builder makes it pass, cannot edit it — #2).
    The new or changed criteria also rerun check (d) before any continuation.
    Classify a finding by the INVARIANT it violates, not its surface site:
    fixing the reported instance without its class's invariant is non-convergence
    by construction — the invariant resurfaces at the next site (per-actor →
    per-transfer → per-tick), which the non-convergence rule above must then
    catch as ONE recurring class, not three new findings.
    The classification is RECORDED, not mental: before the finding's row in
    `docs/reviews/review-<id>.md` disposes `fixed`, the fixer writes its
    `sweep:` line — the sibling sites the class predicts, each closed|n/a
    (a sibling OUTSIDE this change's diff closes `routed` to the direction's
    backlog — a class-sibling per §Review-evidence, never dragged into this leg
    as an in-diff fix), plus a seeded-miss/negative-control per class variant when the finding is
    itself a gate/scan/oracle false-green (VALIDATION §Fix-class-closure;
    writer-G10 bounces a RESULT reporting fixed findings without it). A fix
    with no recorded sweep is a patch, and a patch does not close a finding.
  → PROPERTY AUDIT (post-build, mandatory for a `core algorithm` change,
    before REPORT): once VALIDATE is green, the test-author (see Roles)
    re-reads the DIFF — not the frozen spec, which predates the code and
    cannot name a seam the implementation invented — for every NEW
    throw-path, seam, order-dependency, or derived-value range, and appends
    property tests (VALIDATION §Property-layer: CsCheck/FsCheck,
    `[Category("Property")]`, permutation-metamorphic /
    fault-injection-all-exit-paths / multi-actor-one-tick / boundary-biased)
    recorded against the spec's property table. This is the structural fix
    for the class of bug only the builder sees and only the post-DELIVERED
    reviewer previously attacked: an adversarial read positioned exactly
    when the diff exists, not before it (test-author, G0) or after it ships
    (review). A property this pass finds failing routes through the normal
    fix loop above (A FIX IS A CHANGE) — it does not bypass
    RETRY/escalation, and it does not run for a `light` change.
  → ESCALATE (the only mid-run owner contact): retry budget exhausted,
    non-convergence, a decision outside the approved plan (new dependency,
    scope change, irreversible action), or sandbox/permission boundary hit, OR a required tool/harness the plan
    depends on is UNAVAILABLE (the engine Editor not running, an MCP the leg needs
    disconnected, a headless-test license absent) — a mandatory STOP naming the tool
    to the owner («<tool> unavailable — launch it»), never a workaround/crutch/silent
    scope-narrowing around it, OR the
    specific approach/substrate the CALL or frozen plan NAMED turns out infeasible,
    blocked, or costly. A blocked named approach is ITSELF a mandatory escalation even
    if a substitute would pass every gate: the builder may PROPOSE an alternative as an
    option but may NEVER adopt one as the deliverable, and may NEVER silently widen its
    own model — a stretch/normalization "crutch" the named approach did not require is a
    substitution too. A degraded or different mechanism is an owner decision, surfaced as
    a pre-build STOP, never an end-of-run assumptions/cuts line. Any exception to a
    required STOP — proceeding on an unavailable tool, adopting a substitute, widening
    the model — stands ONLY on the owner's EXPLICIT written owner-ack (a signature or
    escalation-id he actually types in chat), never a builder default.
    Escalation = push notification + the specific question + options.
  → REPORT (the RESULT back to the direction):
    outcome; evidence (PR link, gate outputs, ledger final state, the
    `docs/reviews/review-<id>.md` reference with its finding dispositions and
    G5/KERNEL-G5 refutation markers — a done RESULT for a frozen-spec change
    carries it, or the writer bounces on carry-back, coding-agent.md G10);
    assumptions made; anything cut for budget; cost;
    a defect that reached a LATE stage (owner-eye / independent review / post-merge) names the
    INVARIANT-CLASS it violated, so the carry-back can append it to the cross-kind escape-class
    registry (MAINTENANCE step 6) — arming every future feature of any direction against it;
    the review's class-sibling findings (pre-existing defects the whole-codebase class
    search surfaced outside this diff) are handed back to the direction as a `routed`
    backlog list — none silently dropped — for it to schedule as its own CALLs, not
    fixed inside this leg (VALIDATION §Review-evidence);
    manual acceptance instructions for the owner — generated from the SAME
    verification scripts the validator ran (one source of truth, two consumers).
    Non-trivial manual steps (editor setup, device checks) may be issued as a
    guide CALL (os/plays/guide.md) instead of a flat instruction list.
    The RESULT is the leg's GATED closing artifact at a known repo path
    (PROJECT_SETUP stamps the path + fields + an executable check into the
    repo, so the agent produces it with no OS access); a prose chat summary
    does not close the leg. V29/legacy stages return HOME; v30-v34 receipts advance until REPORT/ESCALATE/REPLACED HOME.
    Direction alone issues Direction CALLs.
```

The owner returns to a finished, verified change and checks the evidence, not every line. Tier-2 actions (publish, spend, delete non-versioned data) are never auto-approved regardless of plan approval.

## Run mechanics (platform-neutral contract)

- Kill switch and steering: a stop-file halts the run; a steer-file injects owner redirection mid-run without killing it.
- Notifications: two channels wired at setup — "needs input" (escalation) and "finished: verdict" (run end). The owner is never polled; the run pushes.
- V31+ root receipts share `ACTIVE`, `PRESERVED-PAUSED`, or `RELEASED` across discovery, apply, mutation and Deliver. Only ACTIVE is eligible; paused is custody-only until re-admission; released is terminal. Machine booleans accept only JSON `true|false`; strings fail.
- V31+ retries start at the earliest affected stage: frozen PLAN/carrier/RED → replacement; implementation → BUILD/VALIDATE; process/tool → process proof; closing evidence → closing checks. Run always-safety plus stage-owned proof; PLAN publication never runs RED/full suite. Reuse exact-input evidence; rerun only changed-input dependents.
- V31+ delivery starts clean under one lease: evidence → RESULT/mirrors → gates → `RELEASED` → publish/readback. Replacement atomically commits inventoried salvage plus `replaced-by` under one lease; preserves the ref, claims no delivery, skips downstream gates and returns no draft.
- Model routing: frontier + high effort for PLAN and architecture; default tier for BUILD legs; cheap tier for evaluators/plumbing. Fallback chain configured so overnight runs survive provider errors.
- Sizing: a root may sequence dependency-ordered cohesive invariant/source-of-truth legs, each <= a focused half-day; split mixed surfaces before PAIR-CANDIDATE.
- For high-ambiguity features: best-of-N parallel attempts (where the platform supports it) judged by the validator beats in-place retries.
- Module-scoped contexts: where the platform supports it, scope builder subagents to module boundaries (module + its docs fit one context by PROJECT_SETUP design) — a recommended pattern, not a rule.

## Non-negotiables (mechanical, enforced by hooks/CI — not prose)

1. No machine-runnable check → no autonomy. Every feature ships with its check before build starts.
2. Builder cannot weaken the oracle: tests/ledger/spec edits by the builder fail the run.
3. Validator is authoring-read-only and fresh-context, always: it may run declared validators that generate evidence artifacts/caches, but never authors or edits source, tests, specs, rules, or the generated evidence.
4. All exploratory artifacts (scripts, test scenes) go to the single scratch dir; nothing from it reaches a commit.
5. Done = gates green + evidence attached. A narrative claim is not done.
6. Closing artifact is a CHECK, not prose: merge/deliver requires RESULT at its known path with required fields. Owner signals ("finish it", "merged?", "summary") trigger, never replace, the report. Only Direction issues successor Direction CALLs; a v30-v34 repo runner issues product-local fresh stages (KERNEL §4).

END_OF_FILE: os/engineering/CONTOUR.md
