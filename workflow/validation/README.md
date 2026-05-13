# Workflow Runtime Static Validation

Status: baseline guardrail
Owner layer: workflow validation
Scope: shared Workflow vNext-R runtime consistency checks

## Purpose

This directory contains read-only static checks for Workflow vNext-R runtime cleanup.

The validation suite exists to catch workflow drift before cleanup patches create blockers across:

- runtime core;
- stage registry;
- stage prompts;
- transport templates;
- Direction Project Files cache;
- ChatGPT Project setup surfaces.

## Source of truth

GitHub repository markdown remains the source of truth.

Project Files are runtime cache only.

This validation suite does not replace `WORKFLOW_SOURCE_OF_TRUTH.md`, `WF_VNEXT_R_RUNTIME_CORE.md`, `WORKFLOW_RUNTIME_CACHE_MANIFEST.md`, or `STAGE_REGISTRY.md`.

## Run

From repository root:

```bash
python workflow/validation/runtime_static_checks.py --root . --mode baseline
```

Optional JSON output:

```bash
python workflow/validation/runtime_static_checks.py --root . --mode baseline --format json
```

Future strict mode:

```bash
python workflow/validation/runtime_static_checks.py --root . --mode strict
```

## Modes

### baseline

Baseline mode is for the current cleanup period.

Known cleanup debt is reported as `WARN`, not as a blocking failure.

Expected first useful result:

```text
PASS_WITH_CLEANUP
```

### strict

Strict mode is for later hardening after cleanup patches are complete.

In strict mode, selected baseline warnings become failures.

## Result semantics

```text
PASS
  No failures and no warnings.

PASS_WITH_CLEANUP
  No blocking failures, but known cleanup debt remains.

BLOCKED
  One or more hard runtime invariants failed.

ERROR
  The validator could not run correctly.
```

## Exit codes

```text
0 = PASS or PASS_WITH_CLEANUP
1 = BLOCKED
2 = ERROR / invalid invocation
```

## Read-only rule

The validator is read-only.

It must not modify repository files, emit repository patches, update Project Files, or change workflow state.

## Current known cleanup debt

The first baseline run may warn about:

- legacy transport card shapes;
- missing stage prompt EOF markers;
- missing dedicated `codex_repository_maintenance_apply.v1` transport template;
- stale rebuild/test-active metadata;
- prompt schema duplication / route examples;
- stale `docs/CHATGPT_PROJECT_SETUP.md` setup blocks.

These warnings are expected until the corresponding cleanup patches are approved and applied.
