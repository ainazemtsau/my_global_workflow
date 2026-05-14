# 04 AGENTS.md Base Contract
artifact_control:
  artifact_name: "04 AGENTS.md Base Contract"
  schema: codex_workflow_contract.v1
  owner_layer: codex_runtime_contract
  status: canonical
  repo_path: "workflow/codex/AGENTS_BASE_CONTRACT.md"
  authority: "GitHub repository canonical after file read-back / diff verification / commit verification"
  activation_scope: workflow_runtime_reference
  freshness: refresh_when_codex_runtime_contract_changes
  last_updated: "2026-05-13"

# 04 AGENTS.md Base Contract

## Purpose

This note defines the base repository-side `AGENTS.md` contract for future Codex work.

This step does not install an `AGENTS.md` file into a repository. It installs the canonical base contract under the GitHub repository rebuild root so future Codex waves can copy or adapt it when a repository-specific Wave Card explicitly authorizes that action.

This is not a C1 or C2 final prompt.

## Base AGENTS.md content

AGENTS\_MD\_BASE\_CONTRACT\_BEGIN

```markdown
# AGENTS.md — Workflow vNext-R Codex Base Contract

## Scope

This repository participates in Workflow vNext-R Rebuild work only when a valid Codex Wave Card authorizes work.

The Wave Card controls the task, allowed targets, forbidden targets, validators, evidence requirements, and return format.

## Source of truth

Use this authority order:

1. The current Codex Wave Card.
2. Canonical GitHub repository files under `ainazemtsau/my_global_workflow`.
3. Current rebuild project files explicitly named by the Wave Card.
4. Repository files in the allowed target scope.
5. Task Master or other task ledgers, only when explicitly authorized.

Do not treat old Workflow vNext outputs, old roadmap files, or unvalidated partial installs as canonical unless the Wave Card explicitly reintroduces them.

## Required operating loop

1. Read the Wave Card.
2. Confirm allowed and forbidden targets.
3. Read required canonical sources.
4. Stop with `NEEDS_INPUT` if required sources or permissions are missing.
5. Produce a preview first when the Wave Card requires preview.
6. Apply changes only after the exact apply command when required.
7. Keep the change set minimal and scoped.
8. Run required validators when available.
9. Read back changed GitHub repository files or inspect changed repository files as required.
10. Return a Codex Return Packet.

## Write discipline

Allowed write actions must be explicitly named by the Wave Card.

Do not:

- write outside allowed targets;
- delete files or notes unless explicitly authorized;
- overwrite active Workflow vNext;
- perform global activation;
- create final stage prompts before Step 7+;
- expose secrets or credentials;
- mark Task Master work done without wave validation when the Task Master Boundary Contract applies;
- substitute undocumented assumptions for missing context.

## Evidence discipline

Every completion claim must be supported by evidence.

Expected evidence may include:

- changed file list;
- diff summary;
- GitHub repository file read-back / diff verification / commit verification;
- target tree verification;
- command output;
- validator results;
- forbidden path check;
- unresolved issue list.

When a validator cannot run, state that it was not run and explain why. Do not report a skipped validator as passed.

## Return format

Always return the Codex Return Packet required by the Wave Card.

For GitHub repository install work, return the required CODEX GITHUB CHANGE RESULT.

## Failure and recovery

Return `NEEDS_INPUT`, `PARTIAL`, `STUCK`, or `FAILED` instead of `DONE` when:

- required context is missing;
- target scope is ambiguous;
- a required validator fails;
- file read-back / diff verification / commit verification fails;
- forbidden paths must be touched to proceed;
- partial writes occurred and safe correction is unclear.

Do not patch forward from a confused install. Use the recovery route specified by the Wave Card or return to ChatGPT validation.

```

AGENTS\_MD\_BASE\_CONTRACT\_END

## Required repository adaptation fields

When a future wave creates an actual repository `AGENTS.md`, it must add repository-specific fields for:

*   repository name;
*   path scope;
*   build/test commands;
*   dependency installation rules;
*   branch/worktree policy;
*   generated-file policy;
*   local secrets policy;
*   project-specific forbidden paths;
*   validator commands.

## Acceptance anchors

This note is acceptable only if these anchors remain visible on file read-back / diff verification / commit verification:

*   `AGENTS_MD_BASE_CONTRACT_BEGIN`
*   `Source of truth`
*   `Required operating loop`
*   `Evidence discipline`
*   `For GitHub repository install work, return the required CODEX GITHUB CHANGE RESULT`
*   `AGENTS_MD_BASE_CONTRACT_END`