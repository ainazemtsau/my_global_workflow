# Implementation Next Steps

status: candidate_draft

## Purpose

This file explains what can happen after Stage 4.

Stage 4 does not activate runtime.
Stage 4 does not replace the current Workflow OS.
Stage 4 does not migrate active Directions.
Stage 4 does not update Project Instructions.

After Stage 4, only candidate next steps are allowed unless a later explicit activation plan is designed, reviewed and accepted.

## What Stage 4 means

Stage 4 means the candidate runtime has pilot scenarios, end-to-end examples and concept acceptance checks.

It can support a parent/integration review.

It does not mean production rollout.

It does not mean active state migration.

It does not mean ChatGPT Projects should be changed.

## Possible next paths

### 1. accept candidate concept for integration planning

Use this path when Stage 4 checklist passes.

Result:
  Candidate concept becomes ready for integration planning.

Still not allowed:
  activation, migration, Project Instructions rollout or current Workflow OS replacement.

### 2. revise specific weak area

Use this path when the concept mostly works but one area is weak.

Possible weak areas:
  Direction Spine wording, Active Front selection, Work Graph scope, Action Inbox hygiene, Runtime Console boundary, Codex verification, child/parent return, failure recovery.

Result:
  Open a bounded revision work package for that area only.

### 3. reject / restart concept

Use this path when Stage 4 shows blocker gaps.

Result:
  Record why the candidate failed and restart concept design from the smallest useful baseline.

Do not patch around a broken core model.

### 4. design storage layout

Use this path only after the concept is coherent enough.

Goal:
  Design where Direction Spine, Active Front, Work Graph, Work Contracts, Evidence, Acceptance Decisions, Memory, Signals and Action Inbox would live.

Boundary:
  storage layout design is still candidate documentation.
  It does not create production storage.

### 5. design Project setup integration

Use this path only after parent review agrees the candidate should move toward integration.

Goal:
  Design how ChatGPT Project Instructions UI, Project Files/Sources, request-only packs and source authority should support the candidate runtime.

Boundary:
  Project setup integration design does not update any Project Instructions by itself.

### 6. design first real direction pilot separately

Use this path when the team wants to test the candidate on one real Direction.

Goal:
  Pick one safe Direction pilot with bounded scope, no migration of all Directions and explicit rollback/non-adoption boundary.

Boundary:
  The pilot must not silently replace the current Workflow OS.

### 7. design migration/non-migration policy

Use this path before any active Direction migration.

Goal:
  Decide whether active Directions are migrated, partially mapped, left under current Workflow OS, or connected through a bridge.

Boundary:
  No active Direction migration happens without separate explicit approval and evidence.

### 8. design activation and replacement boundary

Use this path before any future Workflow v3 activation package.

Goal:
  Define the candidate-only activation boundary, replacement boundary, future production namespace, pilot boundary, migration vs non-migration options, Project setup gates, validation gates, coexistence and rollback model.

Boundary:
  Activation and replacement boundary design is still candidate documentation. It does not activate runtime, replace the current Workflow OS, migrate active Directions, update Project Instructions UI or create production runtime files.

## What still cannot be done automatically

The candidate cannot automatically:

- activate itself;
- replace the current Workflow OS;
- update ChatGPT Project Instructions;
- refresh Project Files/Sources;
- migrate active Directions;
- import legacy state;
- accept Codex output;
- promote Memory;
- execute Action Inbox items;
- run Codex without bounded package;
- decide product strategy;
- delete current workflow files.

## Evidence needed before activation

Before any future activation, at minimum, evidence is needed that:

- storage layout exists and is understandable;
- Project setup integration is designed;
- exact source authority rules are defined;
- acceptance/update path is concrete;
- real pilot Direction has been tested safely;
- failure recovery worked in realistic cases;
- Codex bounded package flow worked end to end;
- Runtime Console stayed read-only;
- Action Inbox did not become a trash bin;
- users were not forced into YAML;
- current Workflow OS rollback or coexistence path is clear.

## What a future activation plan would need

A future activation plan would need:

- activation scope;
- non-activation surfaces;
- migration/non-migration decision;
- storage layout;
- Project Instructions update plan;
- Project Files/Sources refresh plan;
- validation checklist;
- rollback plan;
- first pilot Direction;
- explicit acceptance authority;
- evidence required before broader rollout;
- clear statement that current Workflow OS remains active until activation is accepted.

## How to avoid changing current Workflow OS prematurely

Use these rules:

1. Keep all candidate docs under workflow/candidates/workflow_runtime_rebuild/.
2. Do not edit workflow/core, workflow/policies, workflow/transport, workflow/project_packs, workflow/project_setup or directions during candidate design.
3. Do not update Project Instructions UI from candidate docs.
4. Do not upload candidate docs as Project Files/Sources for active runtime use.
5. Do not treat Stage 4 checklist pass as activation.
6. Keep integration planning separate from activation planning.
7. Keep first real pilot design separate from migration.
8. Require explicit parent/integration review before any next path.

## Recommended immediate Next Move

Run parent/integration review on Stage 4 candidate package.

The review should decide one of:

- accept candidate concept for integration planning;
- revise a specific weak area;
- reject / restart concept;
- design storage layout;
- design Project setup integration;
- design first real direction pilot separately;
- design migration/non-migration policy.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/IMPLEMENTATION_NEXT_STEPS.md
