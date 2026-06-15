---
name: parallel-verify
description: >-
  Fan-out and verification procedure for Direction OS plays run from Codex. Use
  when a play step calls for parallel children — research nominal-group
  (multiple independent generators), converge / converge-arch (miner +
  strategic_search children), or review / converge-verify G5 refutation. Spawn
  the matching role workers in parallel, merge and dedupe, then run validator
  workers; for adversarial verification use multiple validators and
  majority-refute; for loop-until-dry keep going until K empty rounds. Also
  covers the honest limits of Codex's model-driven loop, the named-subagent
  spawn limitation, and the distinction between in-session validator pre-passes
  and binding fresh G5 review sessions.
---

# parallel-verify — fan-out + verification (Codex)

Triggered from a play step that asks for parallel children. Codex spawns
subagents **only when explicitly asked** — never spontaneously. So your prompt
must name the workers and say "in parallel," and the controlling play/CALL text
must call for the fan-out. If neither does, do NOT invent a swarm: run the leg
as a single agent.

## 0. Where the agents and config live — and the by-name spawn limitation (verified)

- Role instructions are TOML files in `.codex/agents/` (project, this repo) or
  `~/.codex/agents/` (global). Required fields: `name`, `description`,
  `developer_instructions`. Optional (inherit from the parent when omitted):
  `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers`,
  `skills.config`, `nickname_candidates`.
- **KNOWN LIMITATION (verified mid-2026 — openai/codex issues #15250, #26828,
  #19399):** in tool-backed sessions, INCLUDING the Codex desktop app on
  Windows, a session often CANNOT spawn a custom `.codex/agents/*` agent BY
  NAME. The exposed `spawn_agent` interface accepts only a generic `agent_type`
  (`explorer` / `worker` / `default`) plus `prompt` / `model` overrides — there
  is no parameter to select a custom agent by name, and on Windows a custom
  agent may silently spawn with default config. **Documented-working pattern:**
  spawn the GENERIC agent (`explorer` for read-only research/verification,
  `worker` for a writing build leg) and INJECT the matching role TOML's
  `developer_instructions` text as the child's prompt. The `.codex/agents/*.toml`
  files stay the single source of truth for that text. By-name spawn DOES work
  on the Codex CLI/TUI — confirm on YOUR surface with the first smoke test
  before relying on it; if it fails, use the generic-spawn-plus-inject fallback.
- Concurrency limits live in the `[agents]` table of `config.toml`
  (`~/.codex/config.toml`, or the project `.codex/config.toml`):
  `max_threads` (default 6), `max_depth` (default 1; root = 0),
  `job_max_runtime_seconds`. Wide fan-out beyond `max_threads` queues — raise it
  if a leg needs more concurrent generators. Recursive children need
  `max_depth` raised.
- `sandbox_mode` for generator/validator children: `read-only` is the right
  default for research and verification (they inform, they do not write state);
  use `workspace-write` only for a child that must touch the worktree.
- Tokens are not the constraint here — bias toward thoroughness: more
  generators, more validator votes, an extra refutation round.

## 1. Generator fan-out (divergence)

For a play step that wants independent ideas or evidence, spawn the matching
role (by name on the CLI; or generic `explorer` + injected
`developer_instructions` on a tool-backed/desktop surface):

- **research nominal-group** — N independent `explorer` children on the same
  question. They run **independently in parallel**, NOT a shared brainstorm
  thread (a shared thread collapses to one voice — the whole point of nominal
  group is independence).
- **research miner** — one `explorer` child per brief: fetch one rare case, one
  far analogy, or the single strongest argument against the default path. Raw
  material, not advice.
- **research strategic_search** — one `researcher` child, ONE operator per brief
  (baseline-deletion / constraint-inversion / far-analogy /
  small-team-asymmetry / AI-leverage-with-named-evaluator / failure-inversion);
  ask for a distribution of structurally different variants including
  low-probability ones.
- **converge / converge-arch** — `explorer` (miner) + `researcher`
  (strategic_search) children supply precedent sets and decision-class material
  to the deciding session.

Spawn them in ONE request, explicitly ("spawn N children in parallel"). Codex
waits until all requested children return, then hands you a consolidated set of
results. Each child returns a plain report; a child never decides for the parent
and never writes state — it informs.

## 2. Merge and dedupe (convergence)

When the children return:

- Collapse synonyms and near-duplicates with a short log of what merged.
- Keep survivors that are genuinely distinct on target, mechanism,
  proof-channel, or main assumption (converge/strategic_search rule of thumb:
  3–5 survivors, each refuted once).
- Carry the merged set into the parent session's reasoning. The PARENT digests
  it into its own RESULT — the children's outputs are inputs, not the answer.

## 3. Validator pass (verification)

After merge, verify with `validator` children (separate from the generators):

- **Single-claim check** — one validator re-derives the claim and reports
  survive / refute with the specific hole.
- **Adversarial verify (majority-refute)** — spawn MULTIPLE validators (odd
  count, e.g. 3 or 5) whose job is to try to BREAK the claim, not confirm it.
  A claim survives only if a majority fail to refute it. Any successful
  refutation names the hole and bounces it back for another generation/converge
  round.
- **Loop-until-dry** — for "find everything wrong" sweeps, keep running
  refutation rounds until **K consecutive rounds come back empty** (K = 2 is a
  reasonable default; raise it for a high-stakes node). Each round may use fresh
  validator children so a new round is not anchored on the last.

Note: a `validator` child returns a NON-BINDING in-session verdict
(`SURVIVED-PREPASS` / `REFUTED` / `INCONCLUSIVE`) — never the word
"verified." Surviving the in-session pass is NOT a closed G5 (see §5).

## 4. HONEST LIMIT — the model-driven loop does not guarantee termination

Codex's subagent orchestration is **model-driven**: the parent model decides
when it has "enough" results and stops. It does NOT mechanically count votes,
nor guarantee it ran exactly K empty rounds, nor that it tallied a true
majority. Treat §3's vote-counting and loop-until-dry as a DISCIPLINE you impose
in the prompt and verify by reading the children's outputs yourself — not as an
engine guarantee.

For guaranteed determinism (real vote tallies, a fixed number of rounds, a hard
stop) an external driver — e.g. a wrapper that spawns each child as its own
`codex exec --json` run (JSONL event stream, one JSON object per line), parses
it, counts refutations in code, and decides termination — is possible. But that
wrapper IS a small orchestrator outside the OS plays, and the owner's standing
stance is **the OS is the orchestrator** (TOOLING.md SKIPs external
orchestrators). So this driver is a **maintenance/tooling-level aid the OWNER
opts into for a specific high-stakes node — never something a session spins up
on its own mid-leg.** The default in-session mechanism stays: local subagents +
the session reading the children's outputs itself, no cloud-only feature
required. Surface the option to the owner whenever a leg's correctness depends
on an exact count or an exact number of rounds; do not normalize it for routine
legs.

## 5. Authoritative G5 is a fresh session, not an in-session subagent

Gate G5 ("a claim is verified in a DIFFERENT session by trying to REFUTE it")
is not satisfied by a child validator inside the same parent session. Codex
validators, however many, give you a useful pre-pass but NOT the binding G5
review, because they are part of the same leg. The authoritative final
refutation must be a **fresh session** (`converge-verify` as its own session, or
`review`'s G5 pass run separately from the executor/work session). A different
model family can be requested by a CALL or direction state for extra rigor, but
it is not the default hard gate. State this in the parent's RESULT: which checks
were in-session pre-passes and which fresh session provides the binding review.

## 6. What never fans out

Mechanical legs run as a single agent, no children: writer apply, a single
`work` task, `digest`, `audit`. Fan-out there is wasted motion and risks
diverging state.

## Format / path note (verified, with version drift flagged)

- This skill is a `SKILL.md` with YAML frontmatter; only `name` and
  `description` are required fields.
- Repo-scoped discovery path is `.agents/skills/<skill>/SKILL.md`: Codex scans
  `.agents/skills` in every directory from the current working directory up to
  the repository root, so this file under the repo root is found. User-scope is
  `$HOME/.agents/skills` and admin-scope `/etc/codex/skills` — note these are
  NOT `~/.codex/skills`; that path drifted across versions. Confirm on the
  installed build with `codex --version` and the `/skills` command (it lists
  discovered skills and their source paths). Invocation is implicit (Codex picks
  by `description`) or explicit via `$` mention / `/skills`.
