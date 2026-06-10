# Engineering contour — how product code gets built

The second loop of the OS: what happens after a `call:executor (kind: engineering)` leaves a direction. The direction sends a business task; this contour owns everything from plan to verified code. Files here are read by coding agents (Claude Code / Codex / any), not by chat sessions.

Companion files: `PROJECT_SETUP.md` (bootstrap a product repo), `VALIDATION.md` (the gate pipeline), `TOOLING.md` (what tools are in/out and why).

## Roles (always separated)

- **Planner** — interactive session, frontier model, plan mode. Talks to the owner.
- **Builder** — autonomous session(s), default-tier model. Never talks to the owner mid-run.
- **Validator** — fresh-context, read-only (no Write/Edit), did not author the code; for at least one pass per feature — a different model family than the builder. Agents consistently overrate their own output; same-model self-review is a mirror, not a check.

## The cycle

```
CALL (business task from a direction)
  → PLAN (interactive): planner interviews the owner if needed, writes the
    change spec: per-feature acceptance criteria as a machine-readable
    ledger (all entries start failing), plus the verification plan the
    validator approves BEFORE any code. Owner approves the plan. This is
    the owner's last mandatory appearance until the final report.
  → BUILD (autonomous): one feature at a time, smallest-first.
    Reuse-first rule: before writing anything, search for an existing
    implementation; the duplicate you would have written becomes a call.
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
```

The owner returns to a finished, verified change and checks the evidence, not every line. Tier-2 actions (publish, spend, delete non-versioned data) are never auto-approved regardless of plan approval.

## Run mechanics (platform-neutral contract)

- State on disk, never in conversation: approved spec + ledger + progress log live in the product repo; any fresh session resumes from them in under a minute. Assume interruption.
- Kill switch and steering: a stop-file halts the run; a steer-file injects owner redirection mid-run without killing it.
- Notifications: two channels wired at setup — "needs input" (escalation) and "finished: verdict" (run end). The owner is never polled; the run pushes.
- Model routing: frontier + high effort for PLAN and architecture; default tier for BUILD legs; cheap tier for evaluators/plumbing. Fallback chain configured so overnight runs survive provider errors.
- Sizing: one autonomous run ≤ the approved change; one feature leg ≤ a focused half-day equivalent. Bigger means the plan needed smaller features.
- For high-ambiguity features: best-of-N parallel attempts (where the platform supports it) judged by the validator beats in-place retries.

## Non-negotiables (mechanical, enforced by hooks/CI — not prose)

1. No machine-runnable check → no autonomy. Every feature ships with its check before build starts.
2. Builder cannot weaken the oracle: tests/ledger/spec edits by the builder fail the run.
3. Validator is read-only and fresh-context, always.
4. All exploratory artifacts (scripts, test scenes) go to the single scratch dir; nothing from it reaches a commit.
5. Done = gates green + evidence attached. A narrative claim is not done.

Key sources: Anthropic long-running harness & three-agent harness (planner/generator/evaluator, default-FAIL ledger, evidence gate), Claude Code best practices (/goal, hooks, fresh-context review), OpenAI Codex long-horizon guidance (plans on disk, compaction), retry research (gains plateau at ~3, non-convergence = same error repeating). Full links: os/docs/RESEARCH_BASIS.md and the engineering research session history.

END_OF_FILE: os/engineering/CONTOUR.md
