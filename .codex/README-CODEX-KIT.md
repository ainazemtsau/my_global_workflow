# Codex kit — make Codex work the Direction OS by default

This kit configures the **OpenAI Codex** desktop app / CLI to run this repo's Direction OS exactly like any other coding agent: same job-recognition table, same plays, same gates — with play-mandated parallel fan-out realized as Codex **subagents**, and the binding **G5** refutation routed cross-family to **Claude**.

The OS stays the orchestrator. Codex is a strong per-leg **executor/session** that fans out **only when a play calls for it** — not a self-orchestrating swarm.

> All paths/fields below were web-verified against `developers.openai.com/codex` (mid-2026). A few details drifted across versions and one mechanism has a known limitation — see **Version caveats**, **the spawn limitation**, and **run the smoke tests** to confirm on YOUR installed build.

---

## The one thing to know first: by-name subagent spawn is NOT guaranteed on your surface

The kit's headline move is "spawn the matching role worker." There is a verified limitation (openai/codex issues #15250, #26828, #19399): **in tool-backed sessions — including the Codex desktop app, especially on Windows — a session often cannot spawn a custom `.codex/agents/*` agent BY NAME.** The `spawn_agent` interface exposes only a generic `agent_type` (`explorer` / `worker` / `default`) plus `prompt` / `model` overrides.

So the kit works in two modes, and you confirm which you have with the **first smoke test**:

- **By-name (Codex CLI/TUI):** spawn `explorer` / `validator` / `researcher` / `builder` directly.
- **Generic-spawn-plus-inject (desktop / tool-backed / Windows fallback):** spawn the generic `explorer` (read-only roles) or `worker` (the build leg) and **paste the matching `.codex/agents/<role>.toml` `developer_instructions` as the child's prompt.** The TOML files stay the single source of truth for that text either way.

Everything below is written so the kit functions in EITHER mode.

---

## What each file is

| File | Scope | Purpose |
|---|---|---|
| `AGENTS.md` (repo root) | project | Auto-read by Codex. Holds the job-recognition table + hard rules + the spliced **"Codex: how to work this OS"** section. |
| `.agents/skills/direction-os/SKILL.md` | project | The full "how to run the OS" procedure (progressive disclosure: AGENTS.md stays terse, detail lives here). |
| `.agents/skills/parallel-verify/SKILL.md` | project | The fan-out + verification procedure (incl. the spawn limitation + the cross-family G5 routing). |
| `.codex/agents/explorer.toml` | project | Role: read-only research/converge miner + nominal-group child. |
| `.codex/agents/researcher.toml` | project | Role: read-only strategic_search child. |
| `.codex/agents/validator.toml` | project | Role: read-only intra-family refutation child (NON-binding; the binding G5 is Claude). |
| `.codex/agents/builder.toml` | product repos | Role: workspace-write BUILD leg — belongs in a PRODUCT repo, not here. |
| `.codex/config.toml` | project | `[agents]` fan-out limits (`max_threads`, `max_depth`, `job_max_runtime_seconds`). |
| `.codex/hooks.json` + `.codex/guard/` | project | Repo-scoped Codex hook guard. It blocks known-bad close claims and product-repo write hazards while allowing read-only inspection and checkpoint/pending text. |

**The load-bearing pieces** — `.codex/agents/*`, `.agents/skills/`, and the AGENTS.md section — together make Codex work the OS by default: AGENTS.md tells it *what job it's in and when to fan out*, the skills tell it *the procedure*, the agent TOMLs are *the role text* a play's children run (spawned by name, or injected into a generic child).

---

## Repo-scope vs global — use **repo scope** (recommended)

Keep **everything in this repo** (`.codex/`, `.agents/skills/`, root `AGENTS.md`). Do **not** put OS instructions in the global `~/.codex/AGENTS.md` or `~/.codex/agents/`.

Why: Codex reads the **global `~/.codex/AGENTS.md` for ALL Codex work, in every repo**. A heavy Direction-OS prompt there would hijack unrelated projects (every session would think it's a Direction-OS writer). Global also competes for the same byte budget. Repo-scoped config only activates when Codex is launched inside this repo — which is exactly what we want. (Repo-scoped `.codex/` layers also require the project to be **trusted**; approve the trust prompt once.)

The only thing reasonable to keep global is a personal, repo-agnostic skill (e.g. a generic commit-message helper) — not this kit.

---

## Replicating the kit into a product repo (health-ai, etc.)

Product repos (e.g. `github.com/ainazemtsau/health-ai`, `C:\projects\health-ai`) are **executor** repos: Codex builds/validates there. Give them the same fan-out + cross-family-gate behavior, tuned to engineering plays:

1. Copy `.codex/agents/` (including `builder.toml`, which belongs in product repos), `.codex/config.toml`, and the relevant skill(s) into the product repo.
2. Add (or splice into) the product repo's root `AGENTS.md` the **same 3 rules** from the Codex section, adapted: follow the repo's skill; realize play-mandated children (planner/builder/validator fan-out) as subagents only when the play calls for it; route the **binding validation/G5 gate cross-family to Claude** (a Codex `validator` = same-family pre-pass only).
3. Keep it **repo-scoped** there too — never global.
4. Re-run the smoke tests below inside the product repo (start with the by-name-spawn check).

This keeps one consistent mechanism across the Direction OS repo and every product repo, without a global footprint.

---

## Install (this repo)

1. **Splice the section** from the repo's `AGENTS.md` Codex block (source: the `agents_md_section` shipped with this kit) into the root `AGENTS.md` between its `BEGIN/END` markers. Keep root `AGENTS.md` well under the **32 KiB** cap — push any new detail into the skill, not AGENTS.md.
2. Ensure `.codex/agents/*.toml`, `.codex/config.toml`, and `.agents/skills/*/SKILL.md` exist.
3. Ensure `.codex/hooks.json` and `.codex/guard/` exist if you want the repo-scoped guard enabled.
4. **Trust the project** when Codex prompts (repo-scoped `.codex/` only loads for trusted projects), then **restart Codex** so it re-scans agents, skills, and hooks. Review the hook trust prompt before enabling; the hook runs local Python from this repo.
5. Run the **smoke tests** — the by-name-spawn check FIRST.

---

## Smoke tests — confirm on YOUR installed Codex version

Run these **inside this repo**. (`/...` = type in the Codex composer.)

| Check | Command | Pass = |
|---|---|---|
| **By-name spawn works on your surface (RUN FIRST)** | *"Spawn the `explorer` agent by name on `<a tiny read-only prompt>` and report back."* | A child runs **as `explorer`**. If Codex says it can't select a custom agent by name (known on desktop/Windows — issues #15250/#26828), you are in **generic-spawn-plus-inject** mode: spawn the generic `explorer`/`worker` and paste the role TOML's `developer_instructions` as the prompt. Decide which mode you're in before trusting the rest. |
| AGENTS.md loaded (not truncated) | start a session here; ask: *"Quote the first hard rule from this repo's AGENTS.md and the title of the Codex section."* | It quotes "One session = one job…" **and** "Codex: how to work this OS". If the section is missing, AGENTS.md likely exceeded the byte cap → trim it. |
| Skill discovered | `/skills` | `direction-os` and `parallel-verify` appear with their source paths. |
| Subagents available | `/agent` (CLI) | The agent threads UI is present / switchable. **Note `/agent` is documented for the CLI; the desktop app may surface subagents differently — if `/agent` is absent there, that does not mean subagents are off, only that the command lives elsewhere.** |
| Explicit fan-out works | *"Spawn three read-only children in parallel on `<a tiny prompt>`, wait for all, summarize each."* | Three child threads run and report back (Codex spawns subagents **only when explicitly asked** — matches the play-triggered design). |
| Cross-family gate is honored | ask Codex to close a node on evidence | Its RESULT says the **binding G5/validation pass routes to a Claude session**, and labels any Codex check as intra-family (SURVIVED-INTRA-FAMILY), not "verified." |
| Hook guard unit tests | `python -m unittest discover -s .codex/guard/tests` | The guard blocks bad close claims, product-repo writes, unauthorized side repair, and malformed JSON; it allows checkpoints, G5-backed closes, product read-only git, and owner-acked side repair. |
| Hook guard stdin smoke | `'{\"last_assistant_message\":\"Checkpoint RESULT for c-visual-006; close remains pending\"}' | python .codex/guard/codex_guard.py --event Stop` | Prints `{"continue": true}`. A malformed JSON payload prints `{"decision":"block",...}` because the guard fails closed. |
| Scaffold helper (optional) | `/init` | Generates/refreshes an `AGENTS.md` scaffold — handy to confirm Codex is reading this dir. |

---

## Version caveats (verify, don't trust memory)

- **By-name subagent spawn limitation** — see the top section. Verified via openai/codex issues #15250, #26828, #19399. Use generic-spawn-plus-inject if by-name fails on your surface; the `.codex/agents/*.toml` files are the source of truth for the injected text.
- **AGENTS.md size cap.** Official default `project_doc_max_bytes` = **32 KiB**. On overflow Codex **skips whole files once the combined size reaches the cap** (it does not truncate mid-file, and the docs do not mention a warning). Keep root `AGENTS.md` lean; detail belongs in the skill. To raise it: `project_doc_max_bytes = 65536` in `~/.codex/config.toml`. (A larger "current" default is sometimes reported but is NOT in official docs — don't size against an unverified cap; verify on your build.)
- **Skills discovery path drifted.** Current: `.agents/skills` (walked **cwd → repo root**), then `$HOME/.agents/skills`, then `/etc/codex/skills`, then built-ins. It is **`.agents/skills`, NOT `~/.codex/skills`.** Confirm with `/skills` after a restart.
- **Subagents.** `.codex/agents/*.toml`. Required fields: `name`, `description`, `developer_instructions`. Optional (`model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers`, `skills.config`, `nickname_candidates`) **inherit from the parent session** when omitted. Spawn **only on explicit request**. `[agents]` knobs (`max_threads`=6, `max_depth`=1, `job_max_runtime_seconds`=1800) go in the **project `.codex/config.toml`**. **Precedence (highest wins): CLI flags / --config > project config (`.codex/config.toml`) > profile files (--profile) > user config (`~/.codex/config.toml`) > system > defaults.** A handful of keys are never honored from project-scoped config even when trusted (`model_provider`, `model_providers`, `profile`, `profiles`, `notify`, `otel`, `*_base_url`) — `[agents]` is NOT one of them.
- **Custom prompts → use Skills.** Author reusable workflows as `SKILL.md` rather than `~/.codex/prompts`; the official guidance frames Skills as the authoring format for reusable workflows.
- **Known-wrong, do NOT use:** `[profiles.<name>]` tables + top-level `profile=` were removed (CLI 0.134.0) — use a separate `$CODEX_HOME/<name>.config.toml` via `--profile`; there is no `CODEX_PROFILE` env var; no on-disk `PLANS.md` plan convention; hook `PreToolUse`-deny is a guardrail, **not** an authoritative gate. `sandbox_mode` values: `read-only`, `workspace-write`, `danger-full-access` (note: `danger-full-access` can be rejected by parse_policy on some Windows automations → forced read-only).

---

**Bottom line:** install repo-scoped, trust the project, splice the AGENTS.md section, restart, run the smoke tests — **the by-name-spawn check first**. Codex then recognizes the OS job, fans out into the role workers (by name on the CLI, or generic-spawn-plus-inject on desktop/Windows) exactly where a play calls for it, and defers the binding G5 refutation to Claude.
