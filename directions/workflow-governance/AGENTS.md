# Workflow Governance Direction Instructions

Status: active

Direction path: `directions/workflow-governance`

Source of truth: GitHub repository markdown in `ainazemtsau/my_global_workflow`.

## Purpose

This Direction maintains and improves Workflow vNext-R. It is separate from Solo Max Productive and real product/game Directions.

## Scope

Allowed by default:
- `directions/workflow-governance/**`
- shared workflow files under `workflow/` only when auditing workflow runtime, stage prompts, transport, registry, or Codex protocol behavior.

Allowed only when the audit explicitly targets real Direction behavior:
- `directions/*/project_files/`

Forbidden unless explicitly requested:
- product/project execution
- modifying sibling Directions
- bulk-loading all stage prompts
- changing runtime behavior without approved repository patch

## Runtime Rules

- Stage prompts are request-only by exact stage ID.
- Do not invent workflow findings, source facts, runtime defects, or evaluation results.
- Separate source-backed facts vs inference.
- No repository patch until approval.
- Return Context Request if a required GitHub path is missing.

## Change Rules

- Use small diffs.
- Do not delete files without explicit approval.
- Do not modify runtime core, stage prompts, stage registry, or sibling Directions unless the task explicitly approves those paths.
- Report changed files and validation evidence after edits.
