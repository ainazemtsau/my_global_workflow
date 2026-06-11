# Codex Workflow

status: candidate_draft

## Purpose

Этот файл описывает, как ChatGPT и Codex взаимодействуют в Workflow Runtime Rebuild.

Codex is an adapter / role implementation.

Codex is not the execution system. Codex does not create Accepted State. Codex performs bounded repository work and returns evidence.

## When Codex is allowed

Codex is allowed when all conditions are true:

1. There is a bounded implementation or repository inspection package.
2. The expected result is concrete.
3. Allowed paths are known.
4. Forbidden paths are known.
5. Validation checks are known.
6. Stop conditions are known.
7. ChatGPT can verify the result after Codex returns.
8. The user can paste one self-contained package into Codex.

Codex is not allowed when:

- the goal is vague;
- the scope is "fix everything";
- route/product meaning is undecided;
- acceptance criteria are unknown;
- required source state is missing;
- allowed/forbidden paths are unclear;
- validation cannot be stated;
- the work should be a human decision;
- the work is only research without repository mutation need.

## What Codex may do

Codex may:

- read repository files;
- compare source state;
- create or edit files within allowed paths;
- run validation;
- commit if authorized;
- push if authorized;
- return evidence;
- stop and ask when conditions are unsafe.

## What Codex must not decide

Codex must not decide:

- whether Stage 2 is accepted;
- whether runtime is active;
- whether a Direction is migrated;
- whether Project Instructions are rolled out;
- product strategy;
- future roadmap;
- parent-level route;
- acceptance;
- scope expansion;
- forbidden path exceptions.

If Codex finds a problem outside scope, it reports it as residual risk. It does not fix it unless the Work Package allowed it.

## How ChatGPT creates Codex Work Package

ChatGPT creates Codex Work Package after it has enough information to make the package self-contained.

The package must include:

- repository;
- base ref;
- branch name or branch naming rule;
- branch policy;
- mode/purpose;
- goal;
- problem statement;
- allowed paths;
- forbidden paths;
- required changes;
- validation checks;
- stop and ask conditions;
- commit/push behavior;
- requested return fields.

The user should not have to build the Codex task manually from scattered chat messages.

## Codex Work Package quality test

Before giving the package to the user, ChatGPT asks:

1. Could Codex run this without asking what repository to use?
2. Could Codex know exactly which files may change?
3. Could Codex know exactly which files must not change?
4. Could Codex know what done means?
5. Could Codex validate the result?
6. Could ChatGPT verify the returned result?
7. Would this avoid micro-step work?
8. Does it avoid hidden acceptance?

If any answer is no, the package is not ready.

## How Codex returns result

Codex returns Codex Result Packet.

It must include:

- status;
- branch name;
- commit SHA if committed;
- changed files;
- summary of behavior/content changes;
- validation results;
- forbidden paths check;
- EOF marker check for markdown when relevant;
- push status if relevant;
- project refresh requirements if relevant;
- residual risks.

Codex should not return only prose like "done". That is not enough evidence.

## How ChatGPT verifies Codex result

ChatGPT verifies:

1. Branch and commit.
2. Changed files are within allowed paths.
3. Forbidden paths were not changed.
4. Required changes were actually made.
5. Validation evidence is credible.
6. Markdown EOF markers are present where required.
7. Project refresh requirements are separated.
8. Residual risks are named.
9. No hidden acceptance or scope expansion happened.

Verification outcomes:

```text
verified_ready_for_acceptance_review
needs_codex_repair_same_package
blocked_missing_codex_evidence
rejected_scope_violation
rejected_validation_failed
```

If verification cannot be completed from the pasted result, ChatGPT asks for exact missing evidence.

## When Codex must stop and ask

Codex must stop and ask when:

- base ref is missing/unavailable;
- working tree is dirty in a way not caused by the run;
- required source file is missing;
- existing file conflicts with requested change;
- allowed path needs are insufficient;
- a forbidden path appears necessary;
- validation command is unavailable and no fallback was authorized;
- tests fail and repair requires scope expansion;
- instructions conflict;
- repository state differs materially from package assumptions.

Codex should return a stopped/blocked result, not improvise.

## Anti-micro-step Codex rule

One Codex run should create one bounded implementation package.

Bad Codex package:

```text
Open README and tell me what headings exist.
```

This may be useful as a check job, but it is not a meaningful implementation package.

Bad Codex package:

```text
Create one empty file.
Then we will decide content later.
```

This creates process overhead without meaningful result.

Good Codex package:

```text
Create the five accepted Stage 2 markdown files under workflow/candidates/workflow_runtime_rebuild/.
Use the exact accepted draft content.
Preserve EOF markers.
Run git diff --check and verify no forbidden paths changed.
Commit to review branch and return Codex Result Packet.
```

Good Codex package:

```text
Inspect the candidate package and verify that all Stage 2 files exist,
have END_OF_FILE markers, and do not modify active runtime surfaces.
Do not edit files.
Return verification evidence.
```

A Codex run can be small if the risk is high, but it should still produce a meaningful evidence-bearing result.

## Good vs bad examples

### Good: documentation persistence

```text
Goal:
  Persist reviewed Stage 2 docs.

Allowed:
  workflow/candidates/workflow_runtime_rebuild/*.md for the five Stage 2 files only.

Forbidden:
  active workflow runtime, directions, Project Instructions, old clean_runtime.

Validation:
  git diff --check
  EOF marker check
  forbidden paths check

Return:
  branch, commit, changed files, validation.
```

Why good:

- bounded;
- verifiable;
- no acceptance hidden inside Codex;
- no active runtime mutation.

### Bad: vague workflow implementation

```text
Make the new workflow runtime work.
```

Why bad:

- no scope;
- no allowed paths;
- no validation;
- unclear acceptance;
- invites Codex to make architecture decisions.

### Good: targeted repair

```text
Repair only broken links in the five Stage 2 candidate docs.
Do not change semantics.
Return before/after diff summary and validation.
```

Why good:

- clear defect;
- narrow path;
- validation possible;
- no hidden redesign.

### Bad: micro-step

```text
Add the first heading to PACKET_FORMATS.md.
```

Why bad:

- too small to be a meaningful package;
- likely creates many unnecessary runs;
- user must orchestrate details manually.

## ChatGPT closure after Codex verification

After Codex verification, ChatGPT must end with exact Next Move.

Possible Next Moves:

- accept/review the candidate result;
- ask Codex to repair same package;
- request missing evidence;
- reject due to scope violation;
- open next material chat with a new Launch Packet;
- stop because the target is complete.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/CODEX_WORKFLOW.md
