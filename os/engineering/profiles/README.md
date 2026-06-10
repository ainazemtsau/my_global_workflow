# Stack profiles

One file per technology stack: `os/engineering/profiles/<stack>.md` (e.g. `unity.md`, `web-app.md`, `python-service.md`). A profile makes setup lessons portable across projects instead of being rediscovered per repo.

## Format (≤100 lines per profile)

1. **Module conventions** — how modules are laid out in this stack, and the boundary-enforcement tool (Unity: Assembly Definitions; TS: dep-cruiser; Python: import-linter).
2. **Default validation.config thresholds** — starting points for the gate pipeline in this stack.
3. **Test layout** — where tests/test scenes live, which runner (engines: the single registered test-scene root).
4. **Known landmines + mechanical fixes** — stack-specific failure patterns and the hook/CI rule that closes each.
5. **Setup notes** — anything PROJECT_SETUP needs that is stack-specific (license activation steps, CI runner choice).

## Lifecycle

- Profiles are NOT written speculatively. The first PROJECT_SETUP run for a stack creates the profile as a byproduct and returns it in its RESULT's `state_changes`, so the writer commits it here (the executor works in the product repo and does not write to the workflow repo directly).
- Updates flow from product-repo friction: a landmine logged in ≥2 repos of the same stack (their `docs/FRICTION.md`) moves into the profile via a maintenance session.
- PROJECT_SETUP step 1 checks this folder first: an existing profile is the entry point; absence of one is the instruction to create it.

END_OF_FILE: os/engineering/profiles/README.md
