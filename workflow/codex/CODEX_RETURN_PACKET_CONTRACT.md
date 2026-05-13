# 03 Codex Return Packet Contract
artifact_control:
  artifact_name: "03 Codex Return Packet Contract"
  schema: codex_workflow_contract.v1
  owner_layer: codex_runtime_contract
  status: canonical
  repo_path: "workflow/codex/CODEX_RETURN_PACKET_CONTRACT.md"
  authority: "GitHub repository canonical after file read-back / diff verification / commit verification"
  activation_scope: workflow_runtime_reference
  freshness: refresh_when_codex_runtime_contract_changes
  last_updated: "2026-05-13"

# 03 Codex Return Packet Contract

## Purpose

A Codex Return Packet is the required response from Codex after executing, previewing, blocking, or failing a Codex Wave Card.

It is the evidence-bearing bridge back to ChatGPT or a human validator. It must be complete enough for validation without relying on private Codex memory.

## Final states

Allowed final states:

```text
DONE
NEEDS_INPUT
PARTIAL
STUCK
FAILED

```

State meanings:

*   `DONE`: all requested work within scope is complete, required validators and file read-back / diff verification / commit verification are satisfied, evidence is present, and forbidden targets were not touched.
*   `NEEDS_INPUT`: Codex did not proceed because required context, access, permission, or human decision was missing.
*   `PARTIAL`: Codex completed some work but not all required work; remaining work is explicitly listed.
*   `STUCK`: Codex cannot safely continue and the next action is not obvious.
*   `FAILED`: Codex attempted work and a validator, write, file read-back / diff verification / commit verification, or safety check failed.

## DONE claim rule

Codex may use `DONE` only when all of the following are true:

1.  The requested objective was completed within the allowed scope.
2.  Every changed file or note is listed.
3.  Required validators were run and their outcomes are reported, or an explicit waiver was present in the Wave Card.
4.  Required file read-back / diff verification / commit verification was performed and passed.
5.  Forbidden targets were checked and not changed.
6.  Any remaining issues are explicitly nonblocking.
7.  The return packet includes an exact next route.

Codex must not claim DONE based only on intention, partial inspection, or an unstated assumption.

## Required Codex Return Packet template

CODEX\_RETURN\_PACKET\_BEGIN

```text
# CODEX RETURN PACKET

Final state: DONE / NEEDS_INPUT / PARTIAL / STUCK / FAILED

## Wave executed
- Wave ID:
- Wave name:
- Wave Card source:
- Wave Record path:
- Codex mode:
- Apply command received: yes/no/not-required

## Objective
- Requested objective:
- Completed objective:
- Non-goals respected:

## Source and authority check
- Canonical sources read:
- Required sources missing:
- Stale or untrusted sources ignored:
- Authority conflicts detected:

## Work performed
- Summary:
- Files changed:
  - path:
    action: create | modify | delete | move | no-change
    summary:
- GitHub repository files changed:
  - path:
    action: create | replace_note | replace_section | append_section | update_header | mark_stale | no-change
    summary:
- Commands run:
  - command:
    result:
    evidence excerpt:
- Task Master actions:
  - task_id:
    action:
    summary:

## Evidence
- Diff summary:
- Read-back results:
- Validator results:
- Logs or artifacts:
- Screenshots or visual checks, if applicable:
- Evidence not available:
- Reason evidence is unavailable:

## Safety checks
- Allowed targets only: pass/fail
- Forbidden targets untouched: pass/fail
- Secrets or credentials exposed: yes/no
- Active Workflow vNext overwritten: yes/no
- Global activation performed: yes/no
- Unexpected side effects:

## Result classification
- Final state:
- Why this state is valid:
- Blocking issues:
- Nonblocking notes:

## Next route
- Return to:
- Exact next instruction:

```

CODEX\_RETURN\_PACKET\_END

## Required GitHub repository install return compatibility

When the wave is specifically a GitHub repository install operation, Codex must use the more specific `CODEX GITHUB CHANGE RESULT` format required by the universal installer.

That install result is considered a specialized Codex Return Packet. It must still satisfy the DONE claim rule above.

## Invalid evidence patterns

These are not sufficient evidence for DONE:

*   “Looks good.”
*   “Should be installed.”
*   “I updated the relevant note.”
*   “Tests should pass.”
*   “No issues found” without naming the check performed.
*   A write claim without file read-back / diff verification / commit verification when file read-back / diff verification / commit verification is required.
*   A validator claim without command, output summary, or explicit unavailable reason.

## Acceptance anchors

This note is acceptable only if these anchors remain visible on file read-back / diff verification / commit verification:

*   `CODEX_RETURN_PACKET_BEGIN`
*   `DONE claim rule`
*   `Required validators were run`
*   `Required file read-back / diff verification / commit verification was performed and passed`
*   `Forbidden targets were checked and not changed`
*   `CODEX_RETURN_PACKET_END`