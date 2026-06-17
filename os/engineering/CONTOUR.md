# Engineering contour — how product code gets built

The second loop of the OS: what happens after a `call:executor (kind: engineering)` leaves a direction. The direction sends a business task; this contour owns everything from plan to verified code. Files here are read by coding agents (Claude Code / Codex / any), not by chat sessions.

Companion files: `PROJECT_SETUP.md` (bootstrap a product repo), `VALIDATION.md` (the gate pipeline), `TOOLING.md` (what tools are in/out and why). PROJECT_SETUP installs this contour's distilled **run contract** into each product repo's root AGENTS.md — the repo is self-sufficient at run time; this file stays the source.

## Boundary with the direction

- The direction (chat sessions) owns WHAT and the acceptance bar: outcome, business-level done_when, boundaries, budget, evidence pointers. It never prescribes architecture, design, or file layout.
- The contour owns HOW: architecture, design, implementation, validation. Architecture is decided in PLAN — with the owner, in the product repo — and recorded there (ADRs, change specs, module docs). It never lives in direction state; business-relevant assumptions return via REPORT into the direction's review.
- Design exploration from chats (`work/` docs, research findings) arrives as CALL context pointers: input evidence for the planner, never a binding spec.
- Feasibility questions ("can this be built within budget at all?") are direction work (research/work spikes); solution design belongs to PLAN.

## Roles (always separated)

- **Planner** — interactive session, frontier model, plan mode. Talks to the owner.
- **Builder** — autonomous session(s), default-tier model. Never talks to the owner mid-run.
- **Validator** — fresh-context, read-only (no Write/Edit), did not author the code; for at least one pass per feature — a different model family than the builder. Agents consistently overrate their own output; same-model self-review is a mirror, not a check.
- **Test-author** — a separate subagent that, after the spec freezes and before BUILD, reads ONLY the frozen spec (never the code — it does not exist yet) and writes the per-criterion acceptance tests as failing (red). The builder makes them pass and may not edit them. Not the builder (self-review is a mirror), not the validator (a pre-code oracle and a post-code review are different artifacts); a cheap-tier model is fine — its independence is from the SPEC, not from a verdict. This is what stops the builder's own tests from inheriting the builder's misreading of the spec.

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
    approves BEFORE any code. Two spec-hardening checks before freeze:
    (a) when the change EXTENDS a working/frozen system, list the invariants
    that held in the old regime and, per one, whether this change can falsify
    it — falsifiable ones become failing criteria tested in the new regime;
    (b) name what the spec leaves UNCONSTRAINED (which regimes / actor-counts /
    seams / user-perceivable regimes — e.g. uniform vs gradient field, sparse
    vs dense, asymmetry) and mark each silence intentional or not — unintended silences
    become spec lines, since a test can only cover what the spec names.
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
    Builder may not edit the ledger or the spec; flipping a ledger entry
    to passing requires opened evidence (hook-enforced where supported).
  → RETRY policy: a failed gate returns its findings verbatim into the next
    attempt. ≤2 retries in-context; then one fresh-context retry with a
    rewritten prompt; the same finding class recurring twice = non-convergence
    → stop early. Hard cap: 3 retries per gate.
  → ESCALATE (the only mid-run owner contact): retry budget exhausted,
    non-convergence, a decision outside the approved plan (new dependency,
    scope change, irreversible action), or sandbox/permission boundary hit.
    Escalation = push notification + the specific question + options.
  → REPORT (the RESULT back to the direction):
    outcome; evidence (PR link, gate outputs, ledger final state);
    assumptions made; anything cut for budget; cost;
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
