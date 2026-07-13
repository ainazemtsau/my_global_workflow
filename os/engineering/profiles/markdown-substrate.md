# Stack profile: markdown-substrate

First created 2026-07-12 (solmax/g-operating-substrate-first-process-creator/t-2,
repo `ainazemtsau/solmax-operating-substrate`). Format: `profiles/README.md`.

For a repo whose ARTIFACTS are markdown/YAML specifications and procedures
interpreted by an AI (no compiled runtime). The correctness teeth are the AI
author + an independent fresh-session refutation review (KERNEL G5) + the owner
— NOT a script. Owner directive (2026-07-12): Python only for concrete,
non-semantic functions; never a compiler, string/semantic parser or conformance
scanner (aligns with contract v17 source-scan ban).

## 1. Module conventions

- Substrate zones are DIRECTORIES with nearest-wins `AGENTS.md`:
  `kernel/` (inherited invariant semantics, never overridden),
  `services/` (reusable-service contracts = capability, not authority),
  `packs/` (process packs — the only way processes are created),
  `adapters/` (replaceable carriers/providers; implement semantics, never define).
- "Boundary enforcement" is LAYOUT + review, not a graph lint (no import graph):
  a wiring-smoke asserts required zone files exist; kernel/pack/adapter SEMANTIC
  separation (Q2) is judged by the reviewer, never scripted.
- Truncation guard: substrate spec files carry an `END_OF_FILE: <own-path>`
  trailer, checked as the last non-empty line.

## 2. Default validation.config thresholds

- `synced_contract_version`: stamp current `os/engineering/CONTRACT_VERSION`.
- `retry_budget`: 3 per gate, then stop and report.
- `mutation_kill_floor`: `n/a-markdown-substrate` — REQUIRED key kept present and
  honest (no compiled code → G2 has no subject matter). Do NOT fake a score.
- `gate_translation`: record every code-oriented gate as
  wired_executable / wired_by_review_discipline / not_applicable_no_compiled_code.
  N/A here: G2 mutation, negative-control (v11), property-layer (v12),
  dependency-boundary lint, unit-test hygiene. If compiled code is later added,
  these stop being N/A — re-sync via `docs/FRICTION.md`.

## 3. Test layout

- No unit tests (no code). The "tests" are: `tools/check.py` (concrete
  wiring-smoke gate) proven RED by `tools/selfcheck.py` (its negative control),
  and the recorded review artifacts under `docs/reviews/`.
- Review evidence: `docs/reviews/review-<id>.md` + cumulative
  `docs/reviews/REFUTED.md`; closing reports under `docs/results/` (or root
  `RESULT.md`); change proposals under `openspec/changes/<id>/`.

## 4. Known landmines + mechanical fixes

- **The scanner trap.** The tempting failure is to grow a Python validator that
  judges whether a pack is well-composed. BANNED (owner + v17): it becomes a
  compiler and an arms race. Keep Python to file/section presence, YAML parse
  (via PyYAML, not a hand parser), cited-path existence, report-field presence,
  scratch/secret hygiene. Semantics → the reviewer.
- **The reflexive-CI trap.** PROJECT_SETUP says "CI on every PR" — a code-project
  assumption. For a markdown substrate the owner does NOT watch, driven by AI
  executors, a post-push badge nobody reads enforces nothing. The forcing
  function is the local gate the agent runs BEFORE it pushes
  (`check.py --deliver`). Default to NO CI (owner decision 2026-07-12); it is
  the same N/A logic as the code-gates. If a hard backstop is wanted, a local
  git pre-push hook fits — not a cloud pipeline. CI re-enters only via friction
  if compiled code lands.
- **Second source of truth.** Do not copy the accepted Q1-Q7 architecture cards
  into the repo without a materialization CALL — the direction state stays
  authoritative until then; a premature copy drifts.
- **Line endings.** Windows dev + Linux CI: add `.gitattributes` (`* text=auto
  eol=lf`) so the Python gate and CI agree.

## 5. Setup notes

- One dependency: `PyYAML` (config parsing only), pinned in `tools/requirements.txt`.
- **No CI by default** (see §4 reflexive-CI trap): the gate is run by the agent
  before deliver (`python tools/check.py --deliver` + `python tools/selfcheck.py`),
  not by a post-push pipeline.
- Deliver gate: `--deliver` adds the `RESULT.md` field-presence check to the
  always-run inner-loop gate; cited-artifact existence (v18) runs always.
- The code-only strong-check deliver dependencies (mutation/negative-control/
  property-layer/review-evidence freshness) are N/A-by-absence until a frozen
  compiled-code change exists; the review discipline (G4/G5) still applies to
  any substrate-content change and is recorded under `docs/reviews/`.

END_OF_FILE: os/engineering/profiles/markdown-substrate.md
