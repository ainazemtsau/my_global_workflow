# 05 Evidence and Validator Expectations
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 4 — Codex Bridge Contracts Installed at: 2026-05-07T15:53:47.6656515+03:00 Source input: ChatGPT Step 4 output using Project Files 01/02/03 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: none Superseded by: none

# 05 Evidence and Validator Expectations

## Purpose

This contract defines what counts as evidence for Codex work and how validators must be reported.

It exists so ChatGPT and human reviewers can distinguish completed work from unverified claims.

## Evidence classes

Codex evidence must be classified using these terms:

| Evidence class | Meaning | Examples |
| --- | --- | --- |
| Source evidence | What Codex read before acting. | GitHub repository file paths, project file names, Wave Card path. |
| Change evidence | What Codex changed. | File list, note list, action type, diff summary. |
| Runtime evidence | What Codex executed. | Test command output, lint output, build output. |
| Read-back evidence | What Codex re-read after writing. | GitHub repository file read-back / diff verification / commit verification, target tree verification, file content check. |
| Negative evidence | What Codex confirmed did not happen. | Forbidden path untouched, active vNext not overwritten. |
| Residual-risk evidence | What remains uncertain. | Validator unavailable, environment mismatch, nonblocking notes. |

## Claim vocabulary

Codex must use these claim terms:

*   `observed`: directly read, executed, or inspected.
*   `validated`: checked by a named validator or explicit file read-back / diff verification / commit verification.
*   `inferred`: reasoned from available evidence but not directly checked.
*   `not checked`: not inspected or not run.
*   `unavailable`: could not be checked because access or tooling was missing.
*   `failed`: checked and did not pass.

Codex must not use passed for a validator that was not run.

## Minimum evidence required for DONE

A Codex Return Packet may claim DONE only when it includes all applicable evidence below:

1.  Source evidence naming the required canonical sources read.
2.  Change evidence naming every file or GitHub repository file changed.
3.  Runtime evidence for every required command or validator that was run.
4.  Read-back evidence for every changed GitHub repository file when GitHub repository was changed.
5.  Negative evidence confirming forbidden targets were not touched.
6.  A clear list of unresolved issues, even if the list is `none`.
7.  A next route that tells the user exactly where to send the result.

## Validator expectation matrix

| Work type | Expected validators | Required evidence |
| --- | --- | --- |
| GitHub repository install | Tree file read-back / diff verification / commit verification, note file read-back / diff verification / commit verification, header check, content anchor check, active workflow safety check. | Install Result Packet with pass/fail per note. |
| Markdown/documentation change | File or note file read-back / diff verification / commit verification, anchor check, link/path check where applicable. | Changed path list and file read-back / diff verification / commit verification excerpts. |
| Repository code patch | Tests named by Wave Card, lint/typecheck if available, diff summary, working tree status. | Command output summaries and changed file list. |
| Planning-only wave | No write validators unless specified; source-read evidence and plan completeness checks required. | Plan packet and non-goal compliance. |
| Recovery wave | Failed artifact identification, stale/superseded marking, repair file read-back / diff verification / commit verification. | Before/after paths and recovery close packet. |

## Validator unavailable rule

When a required validator cannot run, Codex must report:

```text
Validator:
Expected command/check:
Run status: not run
Reason:
Impact on final state:
Waiver present: yes/no

```

If no waiver is present and the validator is required for DONE, Codex must not return DONE.

## Read-back rule

Read-back is mandatory when Codex changes GitHub repository.

Read-back must identify:

*   exact GitHub repository path;
*   file read-back / diff verification / commit verification pass/fail;
*   required headers present or missing;
*   required anchors present or missing;
*   unexpected content differences;
*   whether any old active Workflow vNext material was overwritten.

## Evidence bundle template

EVIDENCE\_BUNDLE\_TEMPLATE\_BEGIN

```yaml
evidence_bundle:
  source_evidence:
    - source:
      status: observed | unavailable
      notes:
  change_evidence:
    - path:
      system: GitHub repository | repository | local_file | task_master
      action:
      status: observed
      summary:
  runtime_evidence:
    - validator:
      command_or_check:
      result: passed | failed | not checked | unavailable
      output_summary:
  readback_evidence:
    - path:
      result: passed | failed | not checked | unavailable
      anchors_checked:
      missing_anchors:
  negative_evidence:
    - protected_target:
      result: untouched | changed | not checked
      notes:
  residual_risks:
    - risk:
      severity: blocking | nonblocking
      mitigation:

```

EVIDENCE\_BUNDLE\_TEMPLATE\_END

## Acceptance anchors

This note is acceptable only if these anchors remain visible on file read-back / diff verification / commit verification:

*   `Minimum evidence required for DONE`
*   `Codex must not use passed for a validator that was not run`
*   `Read-back is mandatory when Codex changes GitHub repository`
*   `EVIDENCE_BUNDLE_TEMPLATE_BEGIN`
*   `EVIDENCE_BUNDLE_TEMPLATE_END`