# Concept Acceptance Checklist

status: candidate_draft

## Purpose

This checklist is used to review whether the Workflow Runtime Rebuild candidate concept is coherent enough for integration planning.

Passing this checklist does not activate runtime.
Passing this checklist does not replace the current Workflow OS.
Passing this checklist does not migrate active Directions.
Passing this checklist does not make candidate docs accepted production authority.

## Verdict options

pass:
  Concept is coherent enough for integration planning.

warn:
  Concept is promising, but specific weak areas must be revised first.

fail:
  Concept has blocker gaps and should be rejected or restarted.

## Checklist

### 1. Simple top-level model preserved

Pass when:
  The model is still understandable as:
  Direction Spine → Active Front → Work Graph → Work Contract / Run / Evidence / Acceptance → Memory → Signals / Handlers / Action Inbox → Next Move.

Fail when:
  The model requires the user to understand a large architecture before using it.

### 2. no 15-module regression

Pass when:
  Stage 4 does not recreate the old large module map.
  Pilot scenarios are practical checks, not a new module architecture.

Fail when:
  The candidate becomes a 15-module regression or splits simple work into artificial architecture layers.

### 3. Direction Spine visible

Pass when:
  Direction Spine has Root Result, Success Conditions, Spine Points and Tracks.
  It remains a simple axis.

Fail when:
  Direction Spine becomes a full roadmap, backlog or task database.

### 4. Active Front bounded

Pass when:
  Active Front shows the currently moving part of Direction Spine.
  It explains why this work is active and what is out of scope.

Fail when:
  Active Front becomes the whole project.

### 5. Work Graph local

Pass when:
  Work Graph is local to Active Front.
  It shows nearby nodes, dependencies and selected next node.

Fail when:
  Work Graph becomes a global graph of the entire project.

### 6. Every material chat has Launch Packet and Result Packet

Pass when:
  Material work starts from Launch Packet and ends with Result Packet.

Fail when:
  Chat starts from vague memory or closes with only explanation.

### 7. exact Next Move always present

Pass when:
  Every material closure tells the user exactly what to open, paste, verify, accept, decide or stop.

Fail when:
  The user must infer the next step.

### 8. Adapters do not become core

Pass when:
  ChatGPT, Codex, Claude Code, Deep Research, GitHub, future providers and human actions remain adapters / role implementations.

Fail when:
  A provider becomes the runtime model or acceptance authority.

### 9. Codex bounded

Pass when:
  Codex receives repository, base ref, branch policy, allowed paths, forbidden paths, required changes, validation and return fields.

Fail when:
  Codex is asked to "fix everything", decide route, decide acceptance or implement vague goals.

### 10. no hidden accepted-state mutation

Pass when:
  Chat output, Codex output, document existence, Project Files, Signal, Handler result, Action Inbox item and Check Job result do not mutate Accepted State by themselves.

Fail when:
  Any candidate output is treated as accepted without explicit acceptance/update path.

### 11. Memory requires promotion

Pass when:
  Useful information becomes Memory only through explicit promotion.

Fail when:
  Raw chat notes, Signals or Result Packets become Memory automatically.

### 12. Signals facts only

Pass when:
  Signal records what happened or was observed.

Fail when:
  Signal becomes command, task, route decision or state mutation.

### 13. Handlers candidates only

Pass when:
  Handler creates candidate actions only.

Fail when:
  Handler executes material work, launches Codex, accepts evidence or changes state.

### 14. Action Inbox not trash bin

Pass when:
  Every Action Inbox item has reason, relation, priority, when_to_run or stale_condition and close condition.

Fail when:
  Action Inbox stores vague "think later" items, duplicates, stale noise or a hidden roadmap.

### 15. Runtime Console read-only

Pass when:
  Runtime Console summarizes state, uncertainty, blockers, Action Inbox and candidate Next Move without material work.

Fail when:
  Console accepts results, mutates state, launches Codex directly or becomes hidden controller.

### 16. Quality gates cover false done

Pass when:
  Quality gates block false done, missing evidence, failed validation, unclear acceptance, stale sources and forbidden path changes.

Fail when:
  "Done" is allowed without evidence or validation.

### 17. failure recovery covers common cases

Pass when:
  GitHub unavailable, stale Project Files, missing source, Codex validation failed, missing child result, conflicting evidence and handler flood have recovery outputs.

Fail when:
  Failures leave the user with no safe next step.

### 18. Project Files not truth

Pass when:
  Project Files are cache/context unless verified against canonical source.

Fail when:
  Uploaded files are treated as latest repository or accepted state.

### 19. GitHub/source limitations explicit

Pass when:
  Read limitations are recorded and missing exact path/ref is requested.

Fail when:
  Chat guesses repository state.

### 20. User not forced into YAML

Pass when:
  User can write normal text and ChatGPT normalizes it when intent is clear.

Fail when:
  Workflow requires user to manually fill schemas for ordinary input.

### 21. No micro-step workflow

Pass when:
  One material chat produces one meaningful result and one Codex run produces one bounded implementation package.

Fail when:
  Work is split into tiny artificial steps that make the user orchestrate everything manually.

## Integration readiness question

After this checklist, parent review should answer:

1. Is the candidate concept coherent enough for integration planning?
2. Which weak area, if any, must be revised?
3. Is a storage layout design now justified?
4. Is Project setup integration now justified?
5. Is a first real Direction pilot safe to design separately?
6. Is activation still blocked until a separate activation plan exists?

## Final acceptance boundary

A Stage 4 pass means:
  ready for candidate integration planning.

A Stage 4 pass does not mean:
  runtime active, current Workflow OS replaced, active Directions migrated, Project Instructions updated or accepted state changed.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/CONCEPT_ACCEPTANCE_CHECKLIST.md
