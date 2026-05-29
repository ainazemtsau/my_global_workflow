# Packet Formats

status: candidate_draft

## Purpose

Этот файл задает минимальные packet boundaries для Stage 2.

Packet is a copy-pasteable work boundary. Он не является Accepted State и не обязан быть тяжелой machine schema.

Пользователь не обязан писать YAML. Чат может нормализовать обычный человеческий ввод в packet form, если intent ясен.

## Packet principles

1. Human-readable first.
2. Minimal structured fields only where useful.
3. No hidden state.
4. No acceptance by document existence.
5. Every material start has Launch Packet.
6. Every material close has Result Packet + exact Next Move.
7. Missing source state must be explicit.
8. Project Files are cache/context, not truth.
9. Adapter output is candidate until accepted.

## Packet types

Stage 2 uses only these packet boundaries:

- Launch Packet;
- Result Packet;
- Parent Recovery Block;
- Codex Work Package;
- Codex Result Packet.

Context Request is not a separate packet type in Stage 2. It can be a blocked Result Packet.

Human Decision is not a separate packet type in Stage 2. It can be recorded inside Result Packet or acceptance/update path later.

## 1. Launch Packet

### Purpose

Start a material chat or adapter run with enough context to produce one meaningful result.

### Required human-readable fields

- Task: what work is being launched.
- Why now: why this work is the current target.
- Expected result: what should be produced.
- Source authority: where accepted/canonical context comes from.
- Context included: what excerpts/files are supplied.
- Scope: what is in scope.
- Boundaries: what is out of scope / forbidden.
- Evidence needed: what proof/check/output is required.
- Return destination: where result must be pasted or stored.
- If blocked: what to do if source/access is missing.

### Minimal structured fields

```text
packet_type: Launch Packet
target:
source_refs:
context_included:
in_scope:
out_of_scope:
expected_result:
evidence_required:
return_to:
blocked_if:
```

### Forbidden omissions

A Launch Packet must not omit:

- target;
- source authority or limitation;
- in-scope boundary;
- out-of-scope boundary;
- expected result;
- return destination.

### Example

```text
LAUNCH PACKET

target:
  Design Stage 2 Transport + Adapter Setup for Workflow Runtime Rebuild.

source_refs:
  repo: ainazemtsau/my_global_workflow
  ref: wg/workflow-runtime-rebuild-stage-1-candidate-2026-05-29
  path: workflow/candidates/workflow_runtime_rebuild/

context_included:
  Stage 1 candidate package files are listed.
  Concept Snapshot is included as fallback only.

in_scope:
  Transport/interaction protocol.
  Chat types.
  Minimal packet boundaries.
  Codex workflow.
  Adapter setup and context access.

out_of_scope:
  Runtime activation.
  Project Instructions rollout.
  Direction migration.
  Full storage layout.
  Full machine schema.
  Runtime Console details.

expected_result:
  Draft content for five standalone markdown files.

evidence_required:
  State whether GitHub read was verified.
  List files read.
  State limitations.

return_to:
  Parent/integration review.

blocked_if:
  Required GitHub files cannot be read and fallback snapshot is insufficient.
```

## 2. Result Packet

### Purpose

Close a material chat with candidate result, evidence, limitations and exact Next Move.

### Required human-readable fields

- Result summary.
- What was produced.
- What was not produced.
- Evidence.
- Source/read limitations.
- Assumptions.
- Unresolved decisions.
- Risks.
- Candidate status.
- Exact Next Move.

### Minimal structured fields

```text
packet_type: Result Packet
target:
status:
result:
evidence:
not_done:
limitations:
assumptions:
unresolved_decisions:
risks:
candidate_state_notice:
next_move:
```

### Forbidden omissions

A Result Packet must not omit:

- status;
- result;
- evidence or explicit no-evidence reason;
- limitations;
- candidate state notice;
- exact Next Move.

### Example

```text
RESULT PACKET

target:
  Stage 2 Transport + Adapter Setup draft.

status:
  draft_ready_for_parent_review

result:
  Five draft files prepared.

evidence:
  Required Stage 1 GitHub files were read from specified ref.
  Drafts include transport lifecycle, chat types, packet formats, Codex workflow and adapter setup.

not_done:
  Repository was not mutated.
  Runtime was not activated.
  Project Instructions were not changed.

limitations:
  Exact storage layout intentionally not defined in Stage 2.

candidate_state_notice:
  This draft is not accepted runtime state until parent review and explicit acceptance/update path.

next_move:
  Parent/integration review should check whether Stage 2 is complete enough for Codex persistence.
```

## 3. Parent Recovery Block

### Purpose

Allow the user to recover a parent/integration chat when child chats are launched.

Use only when child coordination creates recovery risk.

### Required human-readable fields

- Parent target.
- Why child chats were launched.
- Child list.
- Expected result from each child.
- Returned results.
- Missing results.
- Current parent synthesis state.
- Resume instruction.
- What child chats must not decide.

### Minimal structured fields

```text
packet_type: Parent Recovery Block
parent_target:
children_launched:
expected_child_returns:
received_child_returns:
missing_child_returns:
current_parent_state:
resume_from:
child_forbidden_decisions:
```

### Forbidden omissions

A Parent Recovery Block must not omit:

- parent target;
- children launched;
- missing/received status;
- resume instruction.

### Example

```text
PARENT RECOVERY BLOCK

parent_target:
  Complete Stage 2 design review.

children_launched:
  - Child A: audit packet boundaries.
  - Child B: audit Codex workflow.
  - Child C: audit adapter setup.

expected_child_returns:
  Each child returns PASS/WARN/FAIL, findings, risks and suggested minimal changes.

received_child_returns:
  Child A returned.
  Child B not returned.
  Child C not returned.

current_parent_state:
  Parent synthesis is paused until remaining child results return.

resume_from:
  Paste missing child results here, then synthesize all findings into one parent review.

child_forbidden_decisions:
  Children must not accept Stage 2 or authorize Codex persistence.
```

## 4. Codex Work Package

### Purpose

Launch Codex with a bounded implementation package.

Codex Work Package is a specialized Launch Packet for repository work.

### Required human-readable fields

- Repository.
- Base ref.
- Branch policy.
- Goal.
- Problem statement.
- Allowed paths.
- Forbidden paths.
- Required changes.
- Validation checks.
- Stop conditions.
- Commit/push instructions.
- Requested return fields.
- Project refresh requirements if relevant.

### Minimal structured fields

```text
packet_type: Codex Work Package
repository:
base_ref:
target_branch:
branch_policy:
mode:
goal:
problem_statement:
allowed_paths:
forbidden_paths:
required_changes:
validation:
stop_and_ask_if:
commit_instructions:
push_instructions:
requested_return_fields:
project_refresh_requirements:
```

### Forbidden omissions

A Codex Work Package must not omit:

- repository;
- base ref;
- branch policy;
- allowed paths;
- forbidden paths;
- required changes;
- validation;
- stop conditions;
- requested return fields.

### Example

```text
CODEX WORK PACKAGE

repository:
  ainazemtsau/my_global_workflow

base_ref:
  wg/workflow-runtime-rebuild-stage-1-candidate-2026-05-29

target_branch:
  wg/workflow-runtime-rebuild-stage-2-transport-adapter-2026-05-29

branch_policy:
  review_branch_required

mode:
  documentation persistence only

goal:
  Add Stage 2 draft files under workflow/candidates/workflow_runtime_rebuild/.

allowed_paths:
  - workflow/candidates/workflow_runtime_rebuild/TRANSPORT_AND_INTERACTION_PROTOCOL.md
  - workflow/candidates/workflow_runtime_rebuild/CHAT_TYPES.md
  - workflow/candidates/workflow_runtime_rebuild/PACKET_FORMATS.md
  - workflow/candidates/workflow_runtime_rebuild/CODEX_WORKFLOW.md
  - workflow/candidates/workflow_runtime_rebuild/ADAPTER_SETUP_AND_CONTEXT_ACCESS.md

forbidden_paths:
  - workflow/candidates/clean_runtime/**
  - workflow/core/**
  - workflow/policies/**
  - workflow/project_setup/**
  - directions/**
  - docs/**
  - Project Instructions sources

required_changes:
  Create the five Stage 2 markdown files exactly from accepted draft content.
  Preserve END_OF_FILE markers.

validation:
  - git diff --check
  - verify each new file exists
  - verify each new file has END_OF_FILE marker
  - verify no forbidden paths changed

stop_and_ask_if:
  - base branch is unavailable
  - any required file already exists with conflicting content
  - validation fails and cannot be repaired within allowed paths

requested_return_fields:
  - branch_name
  - commit_sha
  - changed_files
  - validation_results
  - forbidden_paths_check
  - eof_marker_check
  - residual_risks
```

## 5. Codex Result Packet

### Purpose

Return Codex output to ChatGPT for verification.

### Required human-readable fields

- Status.
- Branch name.
- Commit SHA if committed.
- Changed files.
- Summary of changes.
- Validation results.
- Forbidden paths check.
- EOF marker check for markdown.
- Push/remote status if applicable.
- Residual risks.
- Project refresh requirements if applicable.

### Minimal structured fields

```text
packet_type: Codex Result Packet
status:
branch_name:
commit_sha:
changed_files:
summary:
validation_results:
forbidden_paths_check:
eof_marker_check:
push_status:
project_refresh_requirements:
residual_risks:
```

### Forbidden omissions

A Codex Result Packet must not omit:

- changed files;
- validation results;
- forbidden paths check;
- residual risks;
- commit SHA if commit was requested;
- EOF marker check for edited markdown files.

### Example

```text
CODEX RESULT PACKET

status:
  done

branch_name:
  wg/workflow-runtime-rebuild-stage-2-transport-adapter-2026-05-29

commit_sha:
  abc123...

changed_files:
  - workflow/candidates/workflow_runtime_rebuild/TRANSPORT_AND_INTERACTION_PROTOCOL.md
  - workflow/candidates/workflow_runtime_rebuild/CHAT_TYPES.md
  - workflow/candidates/workflow_runtime_rebuild/PACKET_FORMATS.md
  - workflow/candidates/workflow_runtime_rebuild/CODEX_WORKFLOW.md
  - workflow/candidates/workflow_runtime_rebuild/ADAPTER_SETUP_AND_CONTEXT_ACCESS.md

summary:
  Created Stage 2 transport and adapter setup draft files.

validation_results:
  git diff --check: PASS
  file existence check: PASS
  EOF marker check: PASS
  forbidden paths check: PASS

push_status:
  pushed to origin branch

project_refresh_requirements:
  project_instruction_ui_update_required: no
  project_sources_files_refresh_required: no
  request_only_sources_refresh_required: no
  do_not_upload_as_project_file: none

residual_risks:
  Parent review still required before accepting Stage 2.
```

## Blocked result instead of separate Context Request

If work cannot continue, use Result Packet:

```text
RESULT PACKET

status:
  blocked_missing_context

result:
  No material draft produced.

limitations:
  Required source file could not be read.

missing_context:
  workflow/candidates/workflow_runtime_rebuild/ROOT_RUNTIME_MODEL.md at required ref.

next_move:
  Provide verified file content or restore GitHub read access, then rerun the Launch Packet.
```

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/PACKET_FORMATS.md
