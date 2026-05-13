# 06 Task Master Boundary Contract
artifact_control:
  artifact_name: "06 Task Master Boundary Contract"
  schema: codex_workflow_contract.v1
  owner_layer: codex_runtime_contract
  status: canonical
  repo_path: "workflow/codex/TASK_MASTER_BOUNDARY_CONTRACT.md"
  authority: "GitHub repository canonical after file read-back / diff verification / commit verification"
  activation_scope: workflow_runtime_reference
  freshness: refresh_when_codex_runtime_contract_changes
  last_updated: "2026-05-13"

# 06 Task Master Boundary Contract

## Purpose

This contract defines the boundary for Task Master or any equivalent task-management ledger used during Workflow vNext-R Rebuild.

Task Master may help track work. It is not canonical for workflow contracts, stage prompts, source notes, or activation state.

## Authority order

Use this authority order for Workflow vNext-R Rebuild:

1.  Explicit human instruction in the current chat or current Wave Card.
2.  Canonical GitHub repository files under `Workflow / 20 Workflow vNext-R REBUILD`.
3.  Accepted Project Files named by the current step or Wave Card.
4.  Repository files inside the allowed target scope.
5.  Task Master task records, only as a task ledger.

Task Master cannot override canonical GitHub repository content.

## Allowed Task Master uses

Task Master may be used only when the Wave Card explicitly grants access.

Allowed uses may include:

*   reading named task IDs;
*   adding a progress comment to named task IDs;
*   adding evidence links to named task IDs;
*   creating subtasks when explicitly requested;
*   updating task status when explicitly requested;
*   cross-referencing a Wave Record path or Codex Return Packet path.

## Forbidden Task Master uses

Task Master must not be used to:

*   store canonical stage prompts;
*   store canonical Workflow vNext-R contracts;
*   replace GitHub repository install logs;
*   infer activation approval;
*   mark Codex work complete without evidence;
*   mark a Wave Record validated;
*   create uncontrolled task trees;
*   import old Workflow vNext material as trusted source;
*   expand scope beyond the Wave Card.

## Access rule

Default Task Master access is:

```text
access_granted: false

```

Codex may read or update Task Master only when the Wave Card provides:

*   project identifier;
*   allowed task IDs or allowed query;
*   allowed actions;
*   forbidden actions;
*   status update rules;
*   evidence link rules.

If those fields are absent, Codex must report `Task Master access not granted` and continue only if Task Master is nonessential.

## Mismatch rule

When Task Master conflicts with GitHub repository or Project Files:

1.  Do not rewrite canonical workflow content from Task Master.
2.  Report the mismatch in the Codex Return Packet.
3.  Treat GitHub repository as canonical unless the human explicitly says otherwise.
4.  Return `NEEDS_INPUT` if the conflict blocks safe execution.

## Task Master boundary template

TASK\_MASTER\_BOUNDARY\_BEGIN

```yaml
task_master_boundary:
  access_granted: false
  project_identifier: "{{project_or_none}}"
  allowed_task_ids:
    - "{{task_id_or_none}}"
  allowed_query: "{{query_or_none}}"
  allowed_actions:
    - "read"
    - "comment"
    - "attach_evidence"
    - "status_update"
    - "create_subtask"
  forbidden_actions:
    - "mark_done_without_validation"
    - "delete_task"
    - "rewrite_scope"
    - "store_canonical_prompt"
    - "global_activation"
  canonical_for_workflow_content: false
  conflict_policy: "GitHub repository wins unless explicit human override"
  return_packet_requirements:
    - "list task IDs read"
    - "list task IDs changed"
    - "list comments/status updates made"
    - "list conflicts or state no conflicts"

```

TASK\_MASTER\_BOUNDARY\_END

## Required Codex Return Packet fields when Task Master is used

When a wave uses Task Master, the Codex Return Packet must include:

```text
## Task Master actions
- Access granted by Wave Card: yes/no
- Project identifier:
- Task IDs read:
- Task IDs updated:
- Comments added:
- Status changes:
- Evidence links added:
- Conflicts with GitHub repository:
- Canonical content changed from Task Master: must be no

```

## Acceptance anchors

This note is acceptable only if these anchors remain visible on file read-back / diff verification / commit verification:

*   `Task Master cannot override canonical GitHub repository content`
*   `access_granted: false`
*   `TASK_MASTER_BOUNDARY_BEGIN`
*   `mark_done_without_validation`
*   `canonical_for_workflow_content: false`
*   `TASK_MASTER_BOUNDARY_END`