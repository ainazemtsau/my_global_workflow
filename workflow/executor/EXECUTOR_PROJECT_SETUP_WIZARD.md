# Executor Project Setup Wizard

## Purpose

The Executor Project Setup Wizard defines how a Direction prepares a product/project workspace for future executor-based implementation. The wizard is a workflow capability, not a registered stage in this pass.

Core-only setup is valid complete setup.

## Launch Model

The wizard launches through a Project Setup Request that identifies the Direction, project, workspace pointer, expected repository or workspace, requested executor adapter, and authorization boundary.

For the Codex adapter, `/executor:init-project` is the command concept for starting setup. This document records the concept only and does not implement a command.

## Setup Layers

Executor Project Setup has two layers:

- Required Core Bootstrap
- Optional Stack-Specific Setup Tuning Pass

The Required Core Bootstrap is enough to complete setup. Stack-specific tuning may be useful, but it must not become a blind install ceremony.

## Core Bootstrap

Core Bootstrap creates or verifies the baseline project-local execution layer:

- `AGENTS.md`
- `PROJECT_PROFILE.md`
- `EXECUTOR_PROFILE.md`
- `VALIDATION_PROFILE.md`
- `MODULE_MAP.md`
- optional `.codex/*`
- project-local change/evidence folder convention such as `changes/<change-id>/`
- required executor tools for the selected adapter
- target binding fields

For the Codex adapter, Core Bootstrap must install, configure, and verify:

- Task Master
- subagents and reviewer roles
- validation profile
- module map
- `AGENTS.md`
- project and executor profiles
- doctor checks

Task Master is required and verified during setup. Subagents and reviewer roles are setup-time requirements.

## Core Doctor

Core Doctor verifies that setup artifacts and tools are usable before execution is marked complete.

Core Doctor checks:

- target binding exists and matches the workspace
- core-required project-local files exist; approved absence is allowed only for optional artifacts or for a named `complete_with_approved_fallback` result that does not block the requested execution modes
- Task Master is installed, configured, and project-bound for Codex
- subagents and reviewer roles are configured and verified for Codex
- validation profile contains executable or explicitly unavailable checks
- module map identifies ownership and boundaries
- `AGENTS.md` contains project-local operating rules
- no Direction state, raw chats, secrets, or full workflow state mirror was added
- doctor output is recorded in the Executor Setup Result

If true subagents cannot be configured, setup must stop and ask for a setup-time fallback decision. Normal execution assumes setup is complete and does not renegotiate fallback.

## Stack-Specific Setup Tuning Pass

The optional tuning pass evaluates stack-specific support for the concrete project. Examples can include game engine, web, mobile, backend, data, infrastructure, or Unity-specific validation and tooling.

The tuning pass may inspect local project evidence and recommend:

- validators
- MCP servers
- skills
- test harnesses
- build commands
- module documentation conventions
- public interface documentation
- performance or stability checks

Optional stack-specific tools are not installed blindly. Each recommendation receives a setup decision.

## Setup Recommendation Brief

The tuning pass may produce a Setup Recommendation Brief containing:

- observed stack and evidence
- recommended tools or validators
- rationale
- risk and maintenance cost
- setup decision
- required user action, if any
- whether research or guided execution is needed

Setup decisions:

- enable now
- core-only
- park
- research more
- reject

## Research and Guided Branches

If current external facts or current tool behavior materially affect setup, the wizard may request `D1_DEEP_RESEARCH` or return a research-needed note.

If external UI operation, credential action, local installer action, or guided tool configuration is required, the wizard may route to `U1_USER_GUIDED_EXECUTION`.

No new stage IDs are created by this document.

## Final Doctor

Final Doctor reruns after Core Bootstrap and any approved tuning. It verifies:

- setup status
- customization mode
- target binding
- generated or updated files
- required tools
- subagent/reviewer availability
- validation commands
- module map
- forbidden content checks
- approved fallback, if any

The final doctor result is included in the Executor Setup Result.

## Executor Setup Result

The wizard returns an Executor Setup Result with:

- project identity
- target binding fields
- executor adapter
- setup status
- customization mode
- generated files
- verified tools
- subagent/reviewer validation
- validation profile status
- module map status
- doctor result
- recommendations
- approved fallback, if any
- blockers or missing inputs

Setup statuses:

- `complete`
- `incomplete`
- `blocked`
- `complete_with_approved_fallback`

Customization modes:

- `core_only`
- `tuned`
- `deferred`

`complete_with_approved_fallback` is allowed only when the fallback was decided during setup and recorded in the result. It is not negotiated during normal execution.

## Project-Local Generated Files

Setup may create or update project-local artifacts only inside the authorized target project workspace:

- `AGENTS.md`
- `PROJECT_PROFILE.md`
- `EXECUTOR_PROFILE.md`
- `VALIDATION_PROFILE.md`
- `MODULE_MAP.md`
- `docs/architecture/ADR-*.md`
- `docs/modules/*.md`
- `docs/public-interfaces/*.md`
- `changes/<change-id>/*`
- optional `.codex/*`

Generated files must be compact, project-specific, and pointer-oriented. They must not mirror full Direction state or raw chats.

## Tool and Subagent Validation Requirements

For Codex setup, Task Master and subagents/reviewer roles are required and verified during setup. Validation failure blocks setup unless an approved setup-time fallback is recorded.

Normal execution assumes setup is complete. It does not reopen fallback negotiation for missing baseline tools.

END_OF_FILE: workflow/executor/EXECUTOR_PROJECT_SETUP_WIZARD.md
