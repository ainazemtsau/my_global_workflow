# 09 Validation Profile Contract
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Side Amendment SA-01A — Codex Project Setup Core Installed at: 2026-05-10T04:16:01.8896091+03:00 Source input: ChatGPT SA-01A side amendment output Authority: Trilium canonical after read-back Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 09 Validation Profile Contract

## 1\. Purpose

The Validation Profile defines how Codex validates work for a specific project or module.

It must define:

*   validation levels;
*   project-specific checks;
*   command evidence requirements;
*   fallback rules;
*   skip rules;
*   failure handling.

The Validation Profile must not hardcode one technology globally. It binds validation to the actual project stack, available tools, risk level, and execution route.

## 2\. Scope

A Validation Profile may apply to:

*   entire repo;
*   module;
*   package;
*   service;
*   documentation project;
*   workflow project;
*   data project;
*   mixed project.

The scope must be explicit.

## 3\. Core rule

Codex must not claim work is DONE without validation evidence or an explicit, truthful skipped-validation explanation.

When validation cannot be run, Codex must state:

*   which checks were expected;
*   why they could not run;
*   what evidence was gathered instead;
*   whether the result is blocked, partial, or ready for human validation.

## 4\. Validation level model

Each project may adapt validation levels, but every Validation Profile must define the levels it uses.

Recommended generic levels:

### V0\_READINESS

Purpose:

*   verify setup, scope, tools, and project profile.

Typical checks:

*   repo root exists;
*   required setup files exist;
*   tool access is known;
*   project-specific validation commands are identified;
*   no code mutation has occurred.

Used for:

*   setup-only work;
*   project discovery;
*   blocked execution triage.

### V1\_PATCH\_SANITY

Purpose:

*   confirm a small patch is structurally sane.

Typical checks, depending on stack:

*   formatting check;
*   syntax check;
*   type check;
*   lint check;
*   schema check;
*   documentation link check;
*   configuration parse check.

Used for:

*   small bounded changes;
*   setup file patches;
*   low-risk code edits.

### V2\_TARGETED\_BEHAVIOR

Purpose:

*   confirm changed behavior in the smallest relevant scope.

Typical checks, depending on stack:

*   targeted unit tests;
*   targeted integration tests;
*   focused documentation render;
*   focused schema migration dry-run;
*   focused workflow scenario test;
*   local smoke test.

Used for:

*   normal feature patches;
*   bug fixes;
*   module changes.

### V3\_INTEGRATION\_BUILD

Purpose:

*   confirm the changed work integrates with the broader project.

Typical checks, depending on stack:

*   full package test;
*   build;
*   integration suite;
*   end-to-end test;
*   dependency consistency check;
*   cross-module compile or render.

Used for:

*   multi-file changes;
*   cross-module changes;
*   changes affecting public interfaces.

### V4\_RELEASE\_CONFIDENCE

Purpose:

*   confirm readiness for high-risk merge, release, deployment, or durable workflow activation.

Typical checks, depending on stack:

*   full test suite;
*   production-equivalent build;
*   migration dry-run;
*   security or policy check;
*   human acceptance checklist;
*   rollback or recovery verification.

Used for:

*   deployment;
*   data migration;
*   workflow activation;
*   high-risk changes.

## 5\. Required profile fields

A valid Validation Profile must define:

```text
validation_profile.v1

identity:
  profile_id:
  profile_version:
  project_name:
  module_scope:
  profile_status:
  created_at:
  updated_at:
  owner_or_source:

scope:
  repo_root:
  applies_to:
  excluded_paths:
  protected_paths:

levels:
  - level_id:
    name:
    purpose:
    required_for:
    checks:
    evidence_required:
    allowed_fallbacks:
    skip_requires_reason: true

checks:
  - check_id:
    level:
    name:
    command:
    working_directory:
    applies_when:
    requires_network:
    requires_external_service:
    timeout_policy:
    pass_condition:
    fail_condition:
    artifacts:
    evidence_summary_required: true

fallbacks:
  - from_check:
    fallback_check:
    allowed_when:
    evidence_required:

failure_policy:
  on_check_failure:
  on_tool_unavailable:
  on_timeout:
  on_flaky_result:
  on_unknown_command:

reporting:
  commands_run_required: true
  outputs_summarized_required: true
  skipped_checks_list_required: true
  residual_risk_required: true

```

## 6\. Project-specific check rule

Validation checks must be project-specific.

Codex may infer candidate checks from discovered evidence, such as:

*   package manager files;
*   build files;
*   test configuration;
*   scripts;
*   documentation tooling;
*   framework configuration;
*   CI configuration;
*   existing AGENTS.md instructions.

However, Codex must mark inferred checks as candidates until confirmed by evidence or human approval.

## 7\. No global technology hardcoding

This contract must not require one universal command such as a specific package manager, test runner, language compiler, or framework.

Examples of invalid global hardcoding:

*   all projects must run `npm test`;
*   all projects must run `pytest`;
*   all projects must run a specific build command;
*   all projects must use one linter;
*   all projects must have the same validation level names without local mapping.

A project may define those commands in its own Validation Profile when evidence supports them.

## 8\. Validation selection rules

Codex must select validation level based on:

*   requested route;
*   autonomy level;
*   risk level;
*   files changed;
*   module scope;
*   public interface impact;
*   dependency impact;
*   human instruction;
*   project default validation;
*   available tools.

Minimum expected defaults:

*   setup-only change: V0 or V1;
*   small local patch: V1 plus targeted relevant check;
*   behavior change: V2;
*   public interface or cross-module change: V3;
*   deployment, migration, or activation: V4.

## 9\. Skipped validation rules

Skipped validation is allowed only when truthful and explicit.

Each skipped check must report:

*   check ID;
*   reason skipped;
*   whether tool was unavailable;
*   whether command was unknown;
*   whether scope was unsafe;
*   fallback performed;
*   residual risk;
*   whether human validation is required.

Codex must not hide skipped validation in a generic summary.

## 10\. Failure handling

When validation fails, Codex must classify the failure:

*   expected failing test unrelated to patch;
*   patch-caused failure;
*   command unavailable;
*   environment unavailable;
*   flaky result;
*   timeout;
*   unknown cause.

Codex must not proceed as DONE when the validation state is failing unless the route explicitly allows a partial result and the failure is documented.

## 11\. Evidence requirements

A validation report must include:

*   commands run;
*   working directory;
*   validation level;
*   pass/fail result;
*   concise output summary;
*   artifacts, if any;
*   skipped checks;
*   fallback checks;
*   residual risk;
*   recommendation.

## 12\. Relationship to Project Execution Profile

The Project Execution Profile links to the Validation Profile and states the default validation level.

The Validation Profile defines the actual project-specific checks and evidence rules.

## 13\. Relationship to Memory Policy

Validation results may inform technical memory only if the Memory Policy permits it.

Validation output must not be stored as raw logs in memory unless explicitly permitted. Stable technical lessons may be summarized with evidence and scope.

## 14\. Acceptance anchors

A valid install of this note must preserve these anchors:

*   “validation levels”
*   “project-specific checks”
*   “must not hardcode one technology globally”
*   “Codex must not claim work is DONE without validation evidence”
*   “Skipped validation is allowed only when truthful and explicit”
*   “The Project Execution Profile links to the Validation Profile”