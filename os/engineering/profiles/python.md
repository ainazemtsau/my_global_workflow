# Stack profile: python-uv

First created 2026-08-28 (solmax/g-zara-health-vertical/t-health-repo, repo
`ainazemtsau/zaratusta`). Format: `profiles/README.md`.

For a Python runtime whose owner works on **Windows AND macOS**. The whole
toolchain is pure Python, so there is exactly one runtime to keep alive: `uv`
(interpreter + dependencies), `ruff` (format + lint), `mypy` (types), `pytest`
(tests), `import-linter` (module boundaries). No Node, no shell script, no
Makefile anywhere — `pyright` and `dprint` are rejected for that reason alone.

## 1. Module conventions

- Modules at `src/<module>/`; `__init__.py` IS the public surface, and
  cross-module access goes through it (`from foundation import slug`, never
  `from foundation.ids import slug`). Each module carries its own `AGENTS.md`.
- **Boundary enforcement is `import-linter`** (`[tool.importlinter]` in
  `pyproject.toml`, CLI `lint-imports`): a `layers` contract for direction plus
  a `forbidden` contract per leaf. The graph is OPT-IN — a new module that is
  not added to a contract is unguarded, so "new module ⇒ new layer entry" is a
  checklist item, not a habit.
- `[tool.uv] package = false`, with the check runner injecting
  `PYTHONPATH=<root>/src`. Avoids a build backend and the wheel-packages array
  that silently drops a module nobody remembered to list.

## 2. Default validation.config thresholds

- `synced_contract_version`: stamp the current `os/engineering/CONTRACT_VERSION`.
- `retry_budget`: 3 per gate, then escalate; same finding class twice = stop.
- `mutation_kill_floor`: REQUIRED key. Python runners exist (`mutmut`,
  `cosmic-ray`) and are slow; under CONTOUR v36 a PROBA leg owes no G2, so set
  the floor AND `mutation_runner = "none"` beside it. Never fake a score.
- `gate_translation`: every code-oriented gate recorded as `wired_executable`
  / `wired_by_review_discipline` / `not_applicable_until_first_opora_leg`.
- `[result_report]` carries the closing-report path and field list, and the
  check READS them — so the file is machine state, not documentation. Parse it
  with stdlib `tomllib`; the config costs no dependency.

## 3. Test layout

- `tests/<module>/` mirrors `src/<module>/`; `[tool.pytest.ini_options]
  pythonpath = ["src"]` makes that work without installing the project.
- Hygiene is mechanical in the check runner, over `ast` plus the git-tracked
  file list: a test file outside `tests/`, a `tests/<x>/` with no `src/<x>/`,
  any `pytest.mark.skip`/`xfail`, and a test function with no `assert` and no
  `pytest.raises`.
- **Every gate owes a negative control.** `tools/selfcheck.py` seeds a
  violation of each gate into a `tempfile` tree and fails if the gate stays
  green — and, where a false red would be equally bad, feeds it a clean tree
  and fails if it reds anyway. The dependency-graph control runs against the
  real tree and removes its seed in a `finally`.

## 4. Known landmines + mechanical fixes

- **uv silently uses the SYSTEM interpreter.** `uv lock` picks whatever CPython
  is on PATH, which quietly destroys the cross-platform claim: two machines,
  two Pythons, one lockfile. Fix: `[tool.uv] python-preference = "only-managed"`
  — uv then downloads and pins its OWN build, so both platforms resolve the
  same interpreter from `uv.lock`. Verify by re-locking and reading the line.
- **`python -m importlinter` exits 0 without checking anything** — a silent
  false-green. Fix: resolve the `lint-imports` console script through
  `shutil.which` and STOP by name if absent. Confirm every `python -m <tool>`
  form actually runs the tool (`ruff`, `mypy`, `pytest` do).
- **Floored dev dependencies drift.** A `uv lock` for an unrelated package
  moves ruff/mypy and reds a gate for a reason the leg never caused. Fix: pin
  the gate toolchain with `==`; a bump becomes a deliberate edit.
- **A backslash inside a string literal is THE Windows-only trap.** Fix: a
  check over `ast.Constant` string values that fails on any backslash or on
  `^[A-Za-z]:/`, with a `# check: allow-backslash` hatch that owes a FRICTION
  entry. The checker builds the character as `chr(92)` so it obeys its own
  rule, and writes its regexes as `[.]` / `[ <tab>]` instead of the escapes.
- **Two documented launch lines drift apart.** Fix: put them in a README table
  and have the check COMPARE them rather than trust them.
- **Line endings.** Windows dev + Linux CI: `.gitattributes` with
  `* text=auto eol=lf`.

## 5. Setup notes

- `.python-version` pinned; `requires-python = ">=3.13,<3.14"`; dev tools in
  `[dependency-groups] dev` (PEP 735), which uv syncs by default.
- ONE entry point (`tools/check.py`) and no separate lint/format/test command,
  so an agent cannot run a subset and call it green. `--files` narrows the slow
  tools; the dependency graph stays whole-repo by nature. `--deliver` adds the
  `RESULT.md` field-presence check plus contract-v18 cited-artifact existence.
- CI is not the forcing function (the local gate is — `profiles/markdown-substrate.md`
  §4). Where the owner has two target platforms and one machine, a
  `windows-latest` + `macos-latest` matrix running the identical command is
  still the cheapest way to turn a mechanical cross-platform argument into an
  observation — but it is a SPEND (macOS runners bill at 10x) and therefore an
  owner decision, offered by the setup leg, never installed by it.

END_OF_FILE: os/engineering/profiles/python.md
