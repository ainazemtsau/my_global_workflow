# Context and Source Interface

status: active_interface_layer

## Purpose

This file defines how context enters Workflow v3 and how source authority is classified, verified, and stopped when incomplete.

## Owner/surface

Owner/surface: context loading, source authority, Project source classification, and Context Request boundaries.

## Persistence target

Persistence target: `workflow_v3/interfaces/01_CONTEXT_AND_SOURCE_INTERFACE.md`.

## Source authority rule

Exact repository files at a named repo/path/ref are source authority when repository state matters.

Project Files/Sources are cache/context only. Uploaded files, pasted excerpts, prior chat summaries, and candidate docs are candidate context or verified excerpts only after their source, completeness, and ref are stated.

No source may be silently promoted from cache/context to authority.

## Context classes

- canonical repository source - exact repo/path/ref read with completeness known.
- accepted record - a committed accepted-state record created through an explicit acceptance/update path.
- current human input - the user's current instruction or decision in the active run.
- verified excerpt - a bounded excerpt verified against an exact source, with limitations stated.
- Project Files cache/context - uploaded or connected project context that may be stale.
- candidate context - design evidence, draft output, child result, or unaccepted proposal.
- legacy_evidence - old Workflow OS or old Direction material used only through explicit bridge/import/adoption policy.
- unknown/unverified - any source whose origin, ref, completeness, or authority is not known.

## Source-loading input contract

A source-loading request must identify:

- repository or source origin;
- path;
- ref, branch, commit, or supplied excerpt origin;
- reason the source is needed;
- required completeness level;
- whether Project Files/Sources or request-only sources are allowed;
- forbidden sources or paths;
- return destination;
- blocker behavior if unavailable.

## Source-loading output contract

A source-loading result must return:

- source class;
- repo/path/ref or excerpt origin;
- read completeness;
- EOF marker status when relevant;
- freshness/recency limitations;
- conflicts with other sources if observed;
- whether the source is sufficient for the material interface decision;
- Context Request if insufficient.

## Read completeness

A truncated, omitted, or tail-unverified read is not sufficient authority for material workflow work.

When an interface decision depends on a required file, the full file must be readable or the work must stop with a Context Request.

## Stale context handling

If Project Files/Sources, uploaded files, pasted excerpts, prior chats, or memory conflict with exact repository state, the exact repository read wins.

If exact repository state is unavailable, stale context may be used only as candidate context with limitations, and no accepted-state or interface decision may depend on it without verification.

## Request-only source rules

Request-only sources are loaded only when a Launch Packet, Check Job, Codex package, review, or human decision needs them.

Examples include exact node workspaces, Work Contracts, Run records, Result Packets, Evidence records, Acceptance Decisions, Memory Artifacts beyond indexes, raw run logs, archives, old Direction files used as `legacy_evidence`, and candidate docs used for maintenance review.

Request-only loading does not refresh actual Project Files/Sources and does not promote the loaded source to default Project context.

## Relation to Project setup

Project setup must report source surfaces separately:

- Project Instructions UI;
- Project Files/Sources;
- repository Project Instruction Sources;
- request-only sources;
- `do_not_upload_as_project_file`.

Repository commits do not update actual ChatGPT Projects or refresh Project Files/Sources.

## Inputs

Inputs are current human instructions, Launch Packets, Check Job requests, Codex packages, exact repo/path/ref reads, Project Files/Sources cache, verified excerpts, and request-only source requests.

## Outputs

Outputs are source classifications, verified source summaries, limitations, Context Requests, and evidence that a material decision has adequate source authority.

## State mutation rights

This interface does not mutate accepted state.

Source loading may produce candidate evidence. It may not update Project UI, refresh Project Files/Sources, import legacy evidence, or create accepted Direction records by itself.

## Allowed producers

Allowed producers are ChatGPT parent chats, child chats, Check Jobs, Codex packages, research agents, GitHub/exact-repo access, and human-provided source excerpts.

## Allowed consumers

Allowed consumers are Work Contracts, Runs, Evidence review, Acceptance review, Event Loop Closure, Progression Router, Project setup packages, and quality gates.

## Validation/evidence requirement

Validation must state source class, exact path/ref or excerpt origin, completeness, limitations, and whether the evidence is sufficient for the claimed decision.

## Forbidden behaviors

- Guessing repository state.
- Treating Project Files/Sources as latest source authority.
- Treating pasted text or prior chat as accepted state without verification.
- Silently loading or promoting request-only sources.
- Using legacy files as `accepted_v3_state` by implication.
- Continuing material work when a required source read is unavailable, contradictory, or incomplete.

## Failure/recovery path

Stop with a Context Request when required source is missing, truncated, contradictory, or insufficient for a material interface decision.

Use a Check Job when verification is bounded and source access exists but confidence is not yet adequate.

Use same-package repair only when missing evidence can be obtained inside allowed paths and scope.

## Dependencies

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow_v3/PROJECT_SETUP_MODEL.md`
- `workflow_v3/project_setup/PROJECT_FILES_MANIFEST_TEMPLATE.md`
- `workflow_v3/QUALITY_AND_RECOVERY.md`

END_OF_FILE: workflow_v3/interfaces/01_CONTEXT_AND_SOURCE_INTERFACE.md
