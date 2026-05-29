# End-to-End Examples

status: candidate_draft

## Purpose

This file gives simple end-to-end examples for Workflow Runtime Rebuild Stage 4.

The examples show how the candidate runtime should feel in real use.

They are not product roadmaps.
They are not live Direction execution.
They do not activate runtime.
They do not change accepted state.

## Example 1 — Indie Game Development technical feasibility path

This example uses Indie Game Development as a realistic candidate path.

### What user writes

"Хочу понять, можно ли сделать техническое ядро игры: co-op, grid/topology, gas simulation, doors/walls/openings, и не уйти сразу в полную реализацию игры."

### What ChatGPT answers

ChatGPT does not start implementation.

It normalizes the input:

- Direction idea:
  Indie Game Development.
- Candidate Direction Spine:
  Root Result: define and validate a feasible technical nucleus for a co-op game.
  Success Conditions: technical nucleus is scoped, risks are visible, implementation package can be bounded, validation evidence is known.
  Spine Points: feasibility frame, technical nucleus spec, bounded prototype package, validation review.
  Tracks: design, technical feasibility, validation, implementation readiness.
- Candidate Active Front:
  Technical feasibility for first playable technical nucleus.
- Out of scope:
  full game roadmap, marketing, content pipeline, production implementation, monetization.

ChatGPT then opens local Work Graph:

- Node 1: define technical nucleus boundaries.
- Node 2: identify gas simulation requirements.
- Node 3: identify topology/level requirements.
- Node 4: define cross-system interactions.
- Node 5: prepare Codex Work Package only if implementation is ready.

Selected node:
  define technical nucleus boundaries.

### Work Chat

ChatGPT creates Launch Packet for Work Chat:

- target:
  Draft the technical feasibility boundary for the first playable nucleus.
- source authority:
  supplied Direction Spine and current user input only.
- in scope:
  technical boundaries, assumptions, risks, validation needs.
- out of scope:
  code implementation, full game design, roadmap.
- expected result:
  candidate technical feasibility frame.
- evidence:
  explicit assumptions, risks and blocked areas.
- return_to:
  parent/integration chat.

Work Chat returns Result Packet:

- result:
  candidate feasibility boundary.
- evidence:
  risks and validation needs identified.
- not done:
  no implementation.
- limitations:
  no engine/project repository source verified.
- candidate status:
  not accepted yet.
- Next Move:
  parent review should decide whether this frame is enough to create a Codex Work Package.

### Codex Work Package

If parent review decides repository documentation should be persisted, ChatGPT sends Codex a bounded package:

- repository:
  target game repository or workflow candidate repository, whichever is explicitly selected.
- allowed paths:
  exact documentation files only.
- forbidden paths:
  source code, build files, unrelated docs.
- required changes:
  persist the accepted candidate feasibility frame.
- validation:
  diff check, file existence, EOF marker if markdown, forbidden paths unchanged.
- return:
  branch, commit, changed files, validation results, residual risks.

Codex must not decide game direction, route, acceptance or future roadmap.

### Codex returns

Codex returns Codex Result Packet:

- branch name;
- commit SHA;
- changed files;
- validation results;
- forbidden path check;
- EOF marker check;
- residual risks.

### Codex Result verification

ChatGPT verifies:

- changed files match allowed paths;
- validation passed;
- forbidden paths unchanged;
- markdown markers preserved;
- residual risks are named.

If validation fails, result is blocked or repair-needed.

### Memory / Signals / Action Inbox

Memory candidate:
  "Technical nucleus feasibility frame exists as candidate and needs parent acceptance."

Signal:
  "Implementation repository was not verified."

Action Inbox candidate:
  "Check engine/project repository context before any Codex implementation package."

### Accepted / candidate / blocked

Accepted:
  nothing yet unless parent explicitly accepts through acceptance/update path.

Candidate:
  technical feasibility frame, Codex output, memory candidate, Action Inbox item.

Blocked:
  product implementation until repository, validation and scope are explicit.

### Next Move

Next Move:
  Paste verified Codex Result Packet into parent/integration review.
  Parent review decides whether to accept the candidate feasibility frame, request repair, or design the next bounded technical node.

## Example 2 — homelab photo storage setup

This example uses homelab photo storage as an ordinary non-workflow project.

### What user writes

"У меня mini-PC на 1 TB. Хочу понять, можно ли заменить iCloud Photos на self-hosted photo storage, чтобы iPhone automatically uploaded photos."

### What ChatGPT answers

ChatGPT does not immediately create a full shopping roadmap.

It normalizes the project:

- Direction idea:
  homelab photo storage.
- Candidate Direction Spine:
  Root Result: reliable self-hosted photo library with automatic phone upload and safe backup.
  Success Conditions: photos import automatically, storage sizing is understood, backup exists, restore path exists, user can maintain it.
  Spine Points: requirements, tool choice, storage/backup plan, install plan, test restore.
  Tracks: app choice, storage hardware, backup, mobile sync, maintenance.
- Candidate Active Front:
  feasibility and setup requirements.
- Out of scope:
  buying hardware immediately, production migration, deleting iCloud, complex Kubernetes setup.

Local Work Graph:

- Node 1: requirements and constraints.
- Node 2: compare candidate tools.
- Node 3: storage and backup sizing.
- Node 4: install/runbook.
- Node 5: migration test.

Selected node:
  requirements and storage/backup sizing.

### Work Chat

ChatGPT creates a Work Chat result:

- candidate requirements:
  automatic iPhone upload, original photo retention, local network access, remote access if needed, backup, restore test.
- candidate risk:
  1 TB may be small depending on library size and backup retention.
- blocked item:
  exact current prices and hardware availability need current market research.
- Action Inbox:
  "Run price/current availability Check Job before purchase."

### Codex

Codex is not needed unless the user has a homelab repository and wants to persist a runbook.

If needed, Codex receives only a bounded documentation package:

- allowed paths:
  homelab docs/runbook path selected by user.
- forbidden paths:
  production config, secrets, unrelated services.
- required change:
  add candidate photo storage runbook.
- validation:
  markdown check and forbidden path check.

### Codex returns

Codex returns changed docs, validation and residual risks.

### Accepted / candidate / blocked

Accepted:
  nothing unless user accepts the requirements or setup plan.

Candidate:
  requirements, tool shortlist, runbook, Action Inbox price check.

Blocked:
  purchase decision until current prices and backup strategy are checked.
  production migration until dry-run import/restore evidence exists.

### Next Move

Next Move:
  Run a bounded Check Job for current storage/NAS cost and tool choice, or accept the requirements and design a safe install plan.
  Do not delete or migrate iCloud Photos until backup and restore evidence exist.

## Example 3 — workflow governance maintenance task

This example uses workflow governance as a maintenance-console style task.

### What user writes

"Проверь чат. Кажется, там ассистент начал делать несколько независимых задач в одном чате."

### What ChatGPT answers

ChatGPT does not start Direction runtime.

It classifies the request:

- task:
  audit a completed transcript.
- source:
  pasted transcript is evidence, not accepted truth.
- in scope:
  single responsibility, project mode, source authority, Codex handoff/result verification if present, terminal outcome.
- out of scope:
  continuing the transcript task, mutating repository, creating runtime artifacts.

Local Work Graph:

- Node 1: identify bounded work.
- Node 2: run P0 Single Responsibility / Atomic Run.
- Node 3: apply relevant gates only.
- Node 4: produce verdict and minimal fix.
- Node 5: prepare Codex handoff only if repository persistence is needed.

### Work Chat

ChatGPT returns:

- Verdict:
  WARN or FAIL depending on evidence.
- Findings:
  one chat handled multiple independent material jobs.
- Defect class:
  multi_work_in_one_chat or no_scope_triage_on_compound_input if supported.
- Recommended fix:
  clarify chat boundary or handoff rule.
- Next Move:
  if persistence is needed, launch Codex with a bounded documentation repair package.

### Codex Work Package

If persistence is needed, Codex receives:

- repository:
  ainazemtsau/my_global_workflow.
- base branch:
  exact branch from user or main if explicitly authorized.
- allowed paths:
  only the policy/docs files selected by the audit.
- forbidden paths:
  directions, product files, Project Instructions unless explicitly in scope.
- required changes:
  repair the specific rule gap.
- validation:
  git diff --check, required marker checks, forbidden paths unchanged.
- return:
  branch, commit, changed files, validation, residual risks, project refresh requirements.

### Codex returns

Codex returns branch, commit, changed files and validation.

### Accepted / candidate / blocked

Accepted:
  repository change only after Codex result verification and explicit acceptance/update path.

Candidate:
  audit finding, proposed fix, Codex output.

Blocked:
  acceptance if Codex changed forbidden paths, validation failed, or evidence is missing.

### Next Move

Next Move:
  Paste Codex Result Packet back into the verification chat.
  ChatGPT verifies the result and then tells the user whether to accept, repair, reject or stop.

## Pattern shown by the examples

The same candidate runtime path works across different kinds of long work:

1. ordinary user input;
2. Direction Spine;
3. Active Front;
4. local Work Graph;
5. Work Contract / Work Chat;
6. Result Packet;
7. Codex Work Package when repository persistence is needed;
8. Codex Result verification;
9. Memory / Signals / Action Inbox as candidates only;
10. exact Next Move.

The examples stay candidate.
They do not activate runtime.
They do not replace current Workflow OS.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/END_TO_END_EXAMPLES.md
