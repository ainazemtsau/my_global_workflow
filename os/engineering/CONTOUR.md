# Engineering contour — how product code gets built

The second loop of the OS: what happens after a `call:executor (kind: engineering)` leaves a direction. The direction sends a business task; this contour owns everything from plan to verified code. Files here are read by coding agents (Claude Code / Codex / any), not by chat sessions.

Companion files: `PROJECT_SETUP.md` (bootstrap a product repo), `VALIDATION.md` (the gate pipeline), `TOOLING.md` (what tools are in/out and why). PROJECT_SETUP installs this contour's distilled **run contract** into each product repo's root AGENTS.md — the repo is self-sufficient at run time; this file stays the source.

## Boundary with the direction

- The direction (chat sessions) owns WHAT and the acceptance bar: outcome, business-level done_when, boundaries, budget, evidence pointers. It never prescribes architecture, design, or file layout.
- A CALL never licenses a silent downgrade, and names the ONE approach it exists to prove. The direction may mark a capability DESIRABLE-not-required, but it may NOT write a standing "ship the lesser form if the real one is costly/hangs" clause — any fallback from the named approach routes through ESCALATE (an owner decision), never a blanket in-CALL permission. When a `done_when`'s substrate/approach is load-bearing it is named as ONE token (an `approach:` / `de-risk-target:`), NOT a disjunctive "X OR a lesser Y": the coverage row echoes that token, so a substituted mechanism is a string-mismatch the gate and the writer catch (VALIDATION.md, coding-agent.md), not a silently-conforming alternative. A disjunctive or downgrade-licensed acceptance bar is a CALL-authoring defect the shape/converge session owns.
- The contour owns HOW: architecture, design, implementation, validation. Architecture is decided in PLAN — with the owner, in the product repo — and recorded there (ADRs, change specs, module docs). It never lives in direction state; business-relevant assumptions return via REPORT into the direction's review.
- Design exploration from chats (`work/` docs, research findings) arrives as CALL context pointers: input evidence for the planner, never a binding spec.
- Feasibility questions ("can this be built within budget at all?") are direction work (research/work spikes); solution design belongs to PLAN.

## Roles (always separated)

- **Planner** — interactive session, frontier model, plan mode. Talks to the owner.
- **Builder** — autonomous session(s), default-tier model. Never talks to the owner mid-run.
- **Validator** — fresh-context, read-only (no Write/Edit), did not author the code; for at least one pass per feature — a different model family than the builder. Agents consistently overrate their own output; same-model self-review is a mirror, not a check.
- **Test-author** — a separate subagent that, after the spec freezes and before BUILD, reads ONLY the frozen spec (never the code — it does not exist yet) and writes the per-criterion acceptance tests as failing (red). The builder makes them pass and may not edit them. Not the builder (self-review is a mirror), not the validator (a pre-code oracle and a post-code review are different artifacts); a cheap-tier model is fine — its independence is from the SPEC, not from a verdict. This is what stops the builder's own tests from inheriting the builder's misreading of the spec. For a `core algorithm` change the same role returns for a second, POST-build pass (see cycle, PROPERTY AUDIT): once gates are green it reads the actual DIFF — the one artifact neither the frozen spec nor the pre-code pass could see — for new throw-paths, seams, order-dependencies, and derived-value ranges the implementation introduced, and appends property tests for them before REPORT. Still not the builder (same self-review mirror) and not the validator (adversarial test-authoring, not review) — it is the only step positioned at the moment the seam becomes visible, between a test-author blind to the code and a reviewer who only reads it after DELIVERED.

## The cycle

```
CALL (business task from a direction)
  → PLAN (interactive): the planner first names the change class — module
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
    approves BEFORE any code. Three spec-hardening checks before freeze:
    (a) when the change EXTENDS a working/frozen system, list the invariants
    that held in the old regime and, per one, whether this change can falsify
    it — falsifiable ones become failing criteria tested in the new regime;
    (b) name what the spec leaves UNCONSTRAINED (which regimes / actor-counts /
    seams / user-perceivable regimes — e.g. uniform vs gradient field, sparse
    vs dense, asymmetry) and mark each silence intentional or not — unintended silences
    become spec lines, since a test can only cover what the spec names.
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
    Owner approves the plan. This is the
    owner's last mandatory appearance until the final report.
  → RED TESTS (before build): the test-author (see Roles) writes the failing
    acceptance tests from the frozen spec — the builder cannot author or edit
    the tests it must satisfy, so a misreading of the spec cannot hide in
    self-agreeing tests.
  → BUILD (autonomous): one feature at a time, smallest-first.
    Reuse-first rule: before writing anything, search for an existing
    implementation; the duplicate you would have written becomes a call.
    Make-time obligations on any tests the builder writes itself too: assert
    every value-bearing/measured field EQUAL to its source (not merely
    present), and for any feature with >1 concurrent actor exercise multi-actor
    / conflicting-input-in-one-tick regimes, never a single-actor happy path.
  → VALIDATE (per feature and per change): gates in VALIDATION.md.
    The independent review (G4) and fresh-session refutation (KERNEL-G5) are
    RECORDED in `docs/reviews/review-<id>.md` (id == the openspec change folder;
    `reviewed-commit` an ancestor of the delivered HEAD with every intervening
    source commit a `fixed <commit>` disposition; every finding dispositioned,
    none `open`; every `refuted` carrying a G5/KERNEL-G5 verification marker
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
  → RETRY policy: a failed gate returns its findings verbatim into the next
    attempt. ≤2 retries in-context; then one fresh-context retry with a
    rewritten prompt; the same finding class recurring twice = non-convergence
    → stop early. Hard cap: 3 retries per gate.
  → A FIX IS A CHANGE, not a patch: a fix made during VALIDATE/RETRY that ADDS
    or CHANGES behavior (a new guard, a reordering, a check that can throw) re-
    triggers the spec-hardening checks (a)/(b) on the fix — explicitly on the
    NEW failure/exception paths it introduces: a guard that throws must keep the
    old-regime invariants (tick atomicity, conservation, non-negativity) intact
    ON the throw path, and each becomes a failing criterion the test-author
    writes RED before the fix (builder makes it pass, cannot edit it — #2).
    Classify a finding by the INVARIANT it violates, not its surface site:
    fixing the reported instance without its class's invariant is non-convergence
    by construction — the invariant resurfaces at the next site (per-actor →
    per-transfer → per-tick), which the non-convergence rule above must then
    catch as ONE recurring class, not three new findings.
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
    scope change, irreversible action), or sandbox/permission boundary hit, OR the
    specific approach/substrate the CALL or frozen plan NAMED turns out infeasible,
    blocked, or costly. A blocked named approach is ITSELF a mandatory escalation even
    if a substitute would pass every gate: the builder may PROPOSE an alternative as an
    option but may NEVER adopt one as the deliverable, and may NEVER silently widen its
    own model — a stretch/normalization "crutch" the named approach did not require is a
    substitution too. A degraded or different mechanism is an owner decision, surfaced as
    a pre-build STOP, never an end-of-run assumptions/cuts line.
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
    manual acceptance instructions for the owner — generated from the SAME
    verification scripts the validator ran (one source of truth, two consumers).
    Non-trivial manual steps (editor setup, device checks) may be issued as a
    guide CALL (os/plays/guide.md) instead of a flat instruction list.
    The RESULT is the leg's GATED closing artifact at a known repo path
    (PROJECT_SETUP stamps the path + fields + an executable check into the
    repo, so the agent produces it with no OS access); a prose chat summary
    does not close the leg. It ends with `next:` naming the direction as the
    carry-back target — the builder NEVER authors the next task CALL (#6).
```

The owner returns to a finished, verified change and checks the evidence, not every line. Tier-2 actions (publish, spend, delete non-versioned data) are never auto-approved regardless of plan approval.

## Run mechanics (platform-neutral contract)

- State on disk, never in conversation: approved spec + ledger + progress log live in the product repo; any fresh session resumes from them in under a minute. Assume interruption.
- Kill switch and steering: a stop-file halts the run; a steer-file injects owner redirection mid-run without killing it.
- Notifications: two channels wired at setup — "needs input" (escalation) and "finished: verdict" (run end). The owner is never polled; the run pushes.
- Model routing: frontier + high effort for PLAN and architecture; default tier for BUILD legs; cheap tier for evaluators/plumbing. Fallback chain configured so overnight runs survive provider errors.
- Sizing: one autonomous run ≤ the approved change; one feature leg ≤ a focused half-day equivalent. Bigger means the plan needed smaller features.
- For high-ambiguity features: best-of-N parallel attempts (where the platform supports it) judged by the validator beats in-place retries.
- Module-scoped contexts: where the platform supports it, scope builder subagents to module boundaries (module + its docs fit one context by PROJECT_SETUP design) — a recommended pattern, not a rule.

## Non-negotiables (mechanical, enforced by hooks/CI — not prose)

1. No machine-runnable check → no autonomy. Every feature ships with its check before build starts.
2. Builder cannot weaken the oracle: tests/ledger/spec edits by the builder fail the run.
3. Validator is read-only and fresh-context, always.
4. All exploratory artifacts (scripts, test scenes) go to the single scratch dir; nothing from it reaches a commit.
5. Done = gates green + evidence attached. A narrative claim is not done.
6. Closing artifact is a CHECK, not prose: a leg cannot merge/deliver unless its RESULT exists at the known repo path with its required fields (a prose summary fails the check). Owner signals ("finish it", "merged?", "summary") TRIGGER the report, never replace it; the builder never authors the next CALL (continuation is the direction's, KERNEL §4).

Key sources: Anthropic long-running harness & three-agent harness (planner/generator/evaluator, default-FAIL ledger, evidence gate), Claude Code best practices (/goal, hooks, fresh-context review), OpenAI Codex long-horizon guidance (plans on disk, compaction), retry research (gains plateau at ~3, non-convergence = same error repeating). Full links: os/docs/RESEARCH_BASIS.md and the engineering research session history.

END_OF_FILE: os/engineering/CONTOUR.md
