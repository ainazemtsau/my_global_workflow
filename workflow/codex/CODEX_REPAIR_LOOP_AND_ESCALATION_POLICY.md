# 15 Codex Repair Loop and Escalation Policy

Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Side Amendment SA-01C — Validation, Review, Repair, and Concrete Project Setup Boundary Installed at: 2026-05-10T04:56:01.1979556+03:00 Source input: ChatGPT SA-01C installable source output, 2026-05-10 Authority: Trilium canonical after read-back Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

## 1\. Purpose

This note defines the finite repair loop Codex must follow when implementation, validation, read-back, or review fails.

Repair attempts are finite. Codex must not loop indefinitely, patch randomly, suppress validators, or mark work complete without evidence.

SA-01A/B/C install governance/contracts only. They do not configure any concrete repo/project.

Concrete project setup happens later per project through CODEX\_PROJECT\_SETUP.

## 2\. Scope

This policy applies to Codex work involving:

*   repo/project setup
*   code edits
*   module map or module knowledge updates
*   validator failures
*   test failures
*   read-back failures
*   install mismatch
*   independent review findings
*   repeated acceptance mismatch
*   cross-module defects
*   security/privacy-sensitive corrections

For Trilium rebuild installs, the same principle applies: preview first, apply only approved changes, read back, validate anchors, and escalate if the install does not match the accepted install card.

## 3\. Failure classification

| Class | Meaning | Default action |
| --- | --- | --- |
| MINOR | Formatting, wording, small missing noncritical evidence, or clearly local defect. | One targeted repair may proceed if acceptance remains unchanged. |
| MAJOR | Acceptance mismatch, validator failure, module boundary issue, broken test, missing required evidence, or incomplete implementation. | Repair attempt required, then rerun relevant validators and update evidence. |
| BLOCKER | Missing required context/tool, unsafe instruction conflict, unclear authority, repeated failure, security/privacy issue, concrete setup absent, or risk of destructive write. | Stop and return NEEDS\_INPUT, STUCK, Human Decision Card, or CODEX\_PROJECT\_SETUP request. |

## 4\. Maximum repair attempts

Codex may perform at most two repair attempts after the initial failed execution.

| Pass | Name | Allowed scope |
| --- | --- | --- |
| Attempt 0 | Initial execution | Perform approved work and run required validation. |
| Repair 1 | Targeted repair | Minimal fix for the observed failure; rerun failed validators and directly affected regression checks. |
| Repair 2 | Root-cause repair | Deeper correction only if root cause is understood; rerun full relevant validators and request independent review when triggered. |
| Escalation | Stop | No further autonomous repair. Return escalation packet with evidence and requested decision/input. |

High-risk, security/privacy-sensitive, broad cross-module, or architecture-sensitive work may have a stricter limit of one repair attempt before independent review or escalation.

## 5\. Required repair loop

For every failed validator, review finding, read-back mismatch, or acceptance mismatch, Codex must:

1.  Identify the failed acceptance criterion, validator, review item, or read-back anchor.
2.  Classify the failure as MINOR, MAJOR, or BLOCKER.
3.  State the suspected root cause.
4.  Propose the smallest safe repair.
5.  Apply only the repair needed for the accepted scope.
6.  Rerun the failed validator/check.
7.  Rerun relevant regression or module-boundary checks.
8.  Update the Codex Return Packet with evidence.
9.  Stop if the maximum attempt count is reached or escalation criteria are triggered.

## 6\. Escalation triggers

Codex must stop and escalate when any of these occur:

*   maximum repair attempts are exhausted
*   required tool binding is missing
*   CODEX\_PROJECT\_SETUP is required but has not been completed
*   acceptance criteria are unclear or conflict with repo/project constraints
*   repair would expand scope materially
*   repair would modify unrelated modules without approval
*   repair would weaken, remove, or bypass tests/validators
*   repair would alter AGENTS.md, .codex/config.toml, module map, module knowledge, Task Master ledger, or Basic Memory policy outside approved setup/update scope
*   same failure class repeats after repair
*   independent review is required but unavailable
*   security/privacy risk is detected
*   destructive or irreversible write risk exists
*   Trilium install preview/apply/read-back does not match the install card
*   old active Workflow vNext would be touched

Escalation output must be one of:

*   NEEDS\_INPUT
*   STUCK
*   Human Decision Card
*   CODEX\_PROJECT\_SETUP request
*   Repair-only Codex Wave Card
*   Recovery Close route when install/work state is confused

## 7\. Prohibited repair behavior

Codex must not:

*   delete or weaken tests to make validation pass
*   lower acceptance criteria without explicit human approval
*   treat Task Master DONE as implementation DONE
*   use Basic Memory as canonical authority
*   claim Serena found proof of correctness without validator/review evidence
*   ignore module boundaries to force a local pass
*   hide failed commands
*   omit failed repair attempts from the Codex Return Packet
*   create concrete project setup files from SA-01 governance notes alone
*   continue repairing after escalation criteria are met

Task Master AI is graph substrate, not DONE authority.

Basic Memory is project/module technical recall only, not Trilium canon.

Serena is trigger-based semantic code/navigation/refactor support.

## 8\. Codex Return Packet repair evidence

When repair occurs, Codex must include:

*   original acceptance target
*   failed check or review item
*   failure class
*   root-cause analysis
*   repair attempt number
*   files/notes changed
*   tests/validators/checks rerun
*   output summary
*   regression/module-boundary checks
*   independent review result if triggered
*   remaining risks
*   whether another repair attempt remains
*   escalation decision if blocked

Codex cannot claim DONE unless the final packet includes acceptance evidence, validator/read-back evidence, and review evidence where required.