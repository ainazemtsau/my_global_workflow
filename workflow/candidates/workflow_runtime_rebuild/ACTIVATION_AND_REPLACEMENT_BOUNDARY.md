# Activation and Replacement Boundary

status: candidate_draft

## Purpose

This file defines the candidate-only boundary for how Workflow Runtime Rebuild could later become a safe Workflow v3 replacement.

It does not activate runtime.
It does not replace current Workflow OS.
It does not migrate active Directions.

The goal is to make future activation safer by separating design, pilot evidence, Project setup changes, migration decisions and old Workflow OS decommission decisions.

## Candidate-only boundary

This document is candidate documentation only.

It records a possible future activation and replacement design, but it does not create active authority, accepted state, runtime state, Project setup payloads, Direction migration permission or decommission permission.

All decisions in this document remain proposals until a later explicit Activation Decision is accepted, committed and validated.

## Exact "not active yet" rule

Until a future explicit Activation Decision is accepted, committed, and validated, everything under workflow/candidates/workflow_runtime_rebuild/** is candidate documentation only. It must not be used as active runtime authority, active Project Instructions source, active Project Files/Sources payload, Direction accepted state storage, migration authority, decommission authority, or permission to delete/replace the current Workflow OS.

This rule also means candidate docs, examples, pilot designs, Result Packets and Project setup drafts do not become active by being reviewed, committed or referenced.

## Activation boundary

Activation is a future acceptance event, not a property of this candidate folder.

A future activation boundary must define:

- the accepted Workflow v3 source authority;
- the exact production namespace to create or update;
- the first active pilot Direction, if any;
- the Project setup update package;
- the validation evidence required before and after activation;
- the coexistence and rollback path;
- the non-migration boundary for all Directions not explicitly selected;
- the acceptance authority and commit evidence.

The default future strategy should be a clean Workflow v3 replacement, not patching the old runtime in place as the default path.

Activation may only use a future production namespace after activation acceptance. Until then, no production runtime files are created from this candidate.

Deleting or renaming current Workflow OS files is not part of activation boundary design.

## Replacement boundary

Replacement means future functional replacement after activation acceptance, not immediate file replacement.

The replacement boundary should:

- keep the current Workflow OS active until a future Activation Decision passes;
- introduce Workflow v3 through a clean production namespace instead of mutating old runtime surfaces in place;
- prefer clean Direction runtime state under directions/<direction-id>/runtime/;
- allow selective bridge or import from the old Workflow OS only through explicit decision and evidence;
- disfavor bulk migration until a separate migration policy exists;
- require each replaced behavior to have validation evidence and rollback coverage.

This candidate does not authorize any edit, delete, rename or move of current Workflow OS files.

## Future production namespace

The future production namespace is a proposal only.

No path in this section is active now, and no path in this section should be created before a future Activation Decision accepts it.

Proposed Workflow v3 production namespace:

- workflow/runtime/
- workflow/runtime/project_setup/
- workflow/runtime/project_packs/
- directions/<direction-id>/runtime/

The preferred Direction state model is clean runtime state under directions/<direction-id>/runtime/ after explicit activation or pilot acceptance.

## What remains candidate-only

The following remain candidate-only until explicitly accepted through a future activation or pilot decision:

- workflow/candidates/workflow_runtime_rebuild/**
- candidate docs;
- candidate examples;
- pilot designs before accepted pilot start;
- any Result Packet before acceptance;
- any Project setup integration draft before activation.

Candidate-only material may be supplied as request-specific evidence for maintenance or integration review, but it must not be uploaded or treated as active Direction Project Files/Sources.

## Current Workflow OS surfaces that might later be replaced

The following current Workflow OS surfaces might later be functionally replaced by Workflow v3, but they are not allowed edit surfaces for this task:

- workflow/core/**
- workflow/policies/**
- workflow/project_setup/**
- workflow/project_packs/**
- workflow/transport/**
- workflow/execution/**
- current Direction payload model: Ledger, Obligations, Receipts index, Commit scopes, Dashboard, Migration receipt.

These are possible future replacement surfaces only. They are not active migration targets, not allowed edits in this package and not decommission candidates before a later decommission decision.

## Coexistence model

Before activation, coexistence is simple: the current Workflow OS remains active and this candidate remains documentation.

After a future activation acceptance, coexistence should still be explicit:

- Workflow v3 starts in the accepted production namespace only;
- one pilot Direction may use isolated Workflow v3 runtime state only after explicit pilot decision;
- all other Directions remain under the current Workflow OS unless separately accepted;
- Project setup must clearly identify active sources and candidate-only sources;
- old Workflow OS files remain available as the rollback path;
- no silent replacement or implicit routing change is allowed.

Coexistence ends only for a specific surface or Direction after acceptance evidence shows that Workflow v3 covers the required behavior and rollback remains possible.

## Rollback model

Before activation, rollback means leaving the candidate unused.

For a future pilot or production activation, rollback must be designed before activation and must include:

- old Workflow OS files still present and unrenamed;
- no overwritten Direction accepted state;
- clear branch or tag archive for the pre-activation state;
- a way to stop using directions/<direction-id>/runtime/ for the pilot Direction;
- Project setup rollback instructions if Project Instructions UI or Project Files/Sources were updated;
- evidence that active Directions not in the pilot were not migrated.

Rollback is not credible if activation depends on deleting, renaming or destructively rewriting current Workflow OS files.

## First pilot Direction boundary

The first pilot Direction must be one safe pilot Direction only.

Pilot boundary rules:

- no all-Direction migration;
- no silent replacement;
- no Project setup change without separate accepted update instructions;
- isolated runtime root only after explicit pilot decision;
- old Workflow OS remains rollback path;
- pilot output remains evidence until accepted;
- non-pilot Directions continue under the current Workflow OS;
- pilot scope, acceptance criteria and rollback criteria must be committed before material pilot execution.

The pilot Direction is a test of the Workflow v3 runtime boundary, not permission to migrate the repository.

## Migration vs non-migration decision points

Future adoption must choose migration vs non-migration per Direction or per surface.

Allowed future options:

- clean start: a Direction starts fresh under Workflow v3 without importing old accepted state;
- bridge only: Workflow v3 reads or references old Workflow OS state through an explicit bridge without claiming migration;
- selective import: specific accepted artifacts are imported with evidence and acceptance;
- full migration only after separate policy: bulk or complete migration waits for a dedicated migration policy, validation evidence and rollback design;
- no adoption for a Direction: the Direction remains under the current Workflow OS.

Decision points should include Direction criticality, evidence quality, current accepted state shape, rollback cost, Project setup impact and whether the old Direction payload model can be mapped without inventing proof state.

Bulk migration is disfavored until a separate migration policy exists.

## Project setup update gates

Candidate docs do not update Project setup.

Project setup gates:

- no Project Instructions UI update from candidate docs;
- no Project Files/Sources refresh from candidate docs;
- no request-only source refresh from candidate docs unless explicitly requested as evidence for a maintenance or integration review;
- no candidate doc becomes an active Project Instructions source;
- no candidate doc becomes an active Project Files/Sources payload;
- future Project setup changes require an accepted Activation Decision;
- future Project setup changes require payload character counts;
- future Project setup changes require a manifest;
- future Project setup changes require refresh categories;
- future Project setup changes require separate explicit update instructions.

Project setup integration drafts remain candidate-only until activation acceptance and a separate update package.

## Validation gates before activation

Before any future activation, these gates must pass:

- candidate concept review passes;
- storage layout accepted;
- Project setup integration accepted;
- source authority rules accepted;
- acceptance/update path concrete;
- first pilot Direction tested;
- Codex bounded package flow tested;
- Runtime Console stayed read-only;
- Action Inbox stayed hygienic;
- rollback/coexistence path verified;
- no active Direction migration happened silently;
- no current Workflow OS files were deleted or renamed.

Activation must fail closed if any gate is missing, ambiguous or contradicted by repository evidence.

## Archive / decommission boundary for the old Workflow OS

Old Workflow OS archive, deletion, rename or decommission is not part of this activation boundary design.

Archive or decommission can only be a later decision after:

- production activation is accepted;
- pilot evidence is accepted;
- rollback safety is confirmed;
- branch or tag archive is confirmed;
- Project setup rollback is understood;
- active Directions have explicit adoption or non-adoption decisions.

This candidate gives no permission to delete, rename, move or replace current Workflow OS files.

## Risks

Main risks:

- candidate docs being mistaken for active authority;
- Project Instructions UI or Project Files/Sources being updated too early;
- silent migration of active Directions;
- mixed old/new source authority;
- rollback path lost by deleting or renaming old files;
- bulk migration without a policy;
- pilot evidence being treated as accepted production state before acceptance.

## Open decisions

Open decisions for future packages:

- who can accept the Activation Decision;
- whether Workflow v3 is the final production name;
- exact production namespace ownership and file inventory;
- first pilot Direction selection;
- pilot acceptance criteria;
- bridge/import policy from old Workflow OS;
- Project setup payload budgets and manifests;
- branch/tag archive convention before activation;
- decommission criteria for old Workflow OS surfaces.

## Validation expectations

Validation for this candidate document should prove that:

- the file remains under workflow/candidates/workflow_runtime_rebuild/;
- it does not modify production runtime files;
- it does not modify Project setup files;
- it names activation and replacement boundaries without activating them;
- it preserves the rule that the candidate does not activate runtime, does not replace current Workflow OS and does not migrate active Directions;
- it includes workflow/runtime/ and directions/<direction-id>/runtime/ as future proposal paths only;
- it keeps rollback, pilot Direction and migration vs non-migration decisions explicit.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/ACTIVATION_AND_REPLACEMENT_BOUNDARY.md
