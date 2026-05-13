# 07 Codex Project Setup Procedure
artifact_control:
  artifact_name: "07 Codex Project Setup Procedure"
  schema: codex_workflow_contract.v1
  owner_layer: codex_runtime_contract
  status: canonical
  repo_path: "workflow/codex/CODEX_PROJECT_SETUP_PROCEDURE.md"
  authority: "GitHub repository canonical after file read-back / diff verification / commit verification"
  activation_scope: workflow_runtime_reference
  freshness: refresh_when_codex_runtime_contract_changes
  last_updated: "2026-05-13"

# 07 Codex Project Setup Procedure

## 1\. Purpose

This note defines the required setup procedure that must run before Codex execution starts when the target project is not yet execution-ready.

The procedure creates or verifies the minimum project-local setup layer needed for safe Codex work:

*   Project Execution Profile;
*   Validation Profile;
*   Memory Policy;
*   repo-local `AGENTS.md`;
*   optional project-scoped `.codex/config.toml`;
*   tool binding profile;
*   basic execution setup required to run, inspect, patch, and validate the project.

This procedure is a Codex Bridge contract. It is not a stage prompt. It does not modify accepted stage prompts, Direction Project Files, the Step 7 stage-development order, or old active Workflow vNext.

## 2\. Required trigger rule

Codex project setup MUST run before Codex execution begins when any of the following are missing, incomplete, stale, contradictory, or inaccessible:

*   Project Execution Profile;
*   Validation Profile;
*   Memory Policy;
*   repo-local `AGENTS.md`;
*   tool binding information;
*   basic execution setup;
*   repo root;
*   module boundary;
*   default autonomy setting;
*   default validation setting;
*   project-specific validation commands;
*   project/module technical memory rules;
*   required Codex or MCP configuration.

This setup may run in discovery-only mode before any write action. It must not proceed to repository mutation until the minimum safe execution context is known.

## 3\. Non-goals and boundaries

This procedure MUST NOT:

*   write C1 or C2 final runtime prompts;
*   modify accepted stage prompts;
*   modify the current Step 7 stage-development order;
*   modify Direction Project Files;
*   overwrite old active Workflow vNext;
*   treat memory as GitHub repository canon;
*   treat raw chat logs as project memory;
*   mirror GitHub repository into repo memory;
*   overwrite project-owned customization;
*   infer technology-specific validation globally across all projects.

This procedure MAY create missing project setup artifacts when explicitly routed through Codex setup and when the target path is inside the project/repo scope authorized for Codex work.

## 4\. Setup readiness states

Codex must classify project setup into one of these states before execution:

### NOT\_CONFIGURED

Required setup artifacts are missing or the repo root cannot be resolved.

Allowed action:

*   inspect;
*   ask for missing context;
*   propose setup patch;
*   create missing setup artifacts only after explicit route allows setup writes.

Disallowed action:

*   code mutation unrelated to setup;
*   claiming execution readiness.

### PARTIAL

Some setup artifacts exist but required fields or links are missing.

Allowed action:

*   inspect;
*   patch missing managed setup fields;
*   preserve project-owned customization;
*   return a setup result packet.

Disallowed action:

*   overwriting custom project instructions;
*   using guessed validation commands as mandatory project checks.

### READY

The project has a usable Project Execution Profile, Validation Profile, Memory Policy, AGENTS.md, tool binding, and basic execution setup.

Allowed action:

*   continue to Codex planning or execution route;
*   run validation at the default or requested validation level;
*   use memory according to the Memory Policy.

### BLOCKED

Critical setup information is unavailable and cannot be safely inferred.

Required action:

*   return a Context Request or Human Decision Card;
*   do not mutate code;
*   do not create speculative durable project instructions.

## 5\. Minimum discovery pass

Before creating or modifying setup artifacts, Codex must inspect the target scope and record evidence for:

*   repo root;
*   project type;
*   module layout;
*   technology stack;
*   package/build/test configuration;
*   existing `AGENTS.md` files;
*   existing `.codex/config.toml`;
*   existing validation scripts;
*   existing memory or documentation conventions;
*   tool access and unavailable tools;
*   protected paths;
*   existing project-owned customization.

Codex must distinguish between observed evidence and inference.

## 6\. Required setup artifacts

### 6.1 Project Execution Profile

Defines:

*   project type;
*   repo root;
*   technology stack;
*   default autonomy;
*   default validation;
*   links to validation, memory, module, and tool profiles.

The contract is defined in:

`04 Codex Bridge / 08 Project Execution Profile Contract`

### 6.2 Validation Profile

Defines validation levels and project-specific checks.

The contract is defined in:

`04 Codex Bridge / 09 Validation Profile Contract`

The Validation Profile must not hardcode one technology globally. It must bind checks to the project’s actual stack, scripts, tools, and risk profile.

### 6.3 Memory Policy

Defines what Codex may store as durable technical memory for the project or module.

The contract is defined in:

`04 Codex Bridge / 10 Memory Policy Contract`

Memory is never GitHub repository canon.

### 6.4 AGENTS.md

`AGENTS.md` is the repo-local durable instruction layer for Codex and other coding agents.

It may contain:

*   repo-specific operating rules;
*   module conventions;
*   validation commands;
*   protected paths;
*   coding standards;
*   evidence requirements;
*   links or pointers to project profiles.

It must not contain:

*   canonical Direction State;
*   Active Goal as canon;
*   Wave Card as canon;
*   raw chats;
*   GitHub repository mirrors;
*   secrets;
*   stale workflow exports.

### 6.5 .codex/config.toml

`.codex/config.toml` may define project-scoped Codex or MCP configuration when needed.

It is optional. Codex must not create it just because it is interesting. It should be created only when project-scoped tool configuration materially improves safe execution.

## 7\. Project-owned customization protection

Workflow updates must not overwrite project-owned customization.

When setup artifacts already exist, Codex must:

*   read existing content first;
*   identify managed sections, if any;
*   preserve unrecognized custom sections;
*   prefer additive or section-scoped patches;
*   avoid replacing the whole file unless the install card explicitly permits replace\_note or replace\_file;
*   report any ambiguity before writing.

If an artifact contains both workflow-managed and project-owned content, Codex must patch only the workflow-managed section or return NEEDS\_INPUT.

## 8\. Setup procedure

### Step 1 — Resolve scope

Codex resolves:

*   target project;
*   repo root;
*   module scope, if any;
*   requested execution route;
*   allowed write scope;
*   protected paths.

If repo root is missing, Codex must stop and request it.

### Step 2 — Inspect existing setup

Codex reads:

*   Project Execution Profile, if present;
*   Validation Profile, if present;
*   Memory Policy, if present;
*   `AGENTS.md`, including nested module-level versions;
*   `.codex/config.toml`, if present;
*   build/test/lint configuration;
*   package manager files;
*   task runner files;
*   existing project documentation relevant to execution.

### Step 3 — Classify readiness

Codex returns one of:

*   NOT\_CONFIGURED;
*   PARTIAL;
*   READY;
*   BLOCKED.

The classification must include evidence.

### Step 4 — Generate missing setup draft

When setup is NOT\_CONFIGURED or PARTIAL, Codex prepares exact patch content for missing artifacts.

The generated setup must:

*   use project-specific evidence;
*   avoid global technology assumptions;
*   define default autonomy;
*   define default validation;
*   define memory rules;
*   link setup artifacts together;
*   preserve customization;
*   identify unknowns explicitly.

### Step 5 — Apply setup only when allowed

Codex may apply setup changes only when the active route allows setup writes.

For preview routes, Codex must show exact proposed writes and stop.

For apply routes, Codex must write only previewed setup changes.

### Step 6 — Validate setup

After setup writes, Codex must read repository files / verify diff or commit every created or updated setup artifact and verify:

*   required fields exist;
*   cross-links resolve;
*   no forbidden memory content was added;
*   project-owned customization was preserved;
*   default validation level is defined;
*   default autonomy level is defined;
*   AGENTS.md exists or its absence is explicitly justified;
*   `.codex/config.toml` exists only when needed.

### Step 7 — Return setup result

Codex returns a setup result packet before continuing to graph planning, wave planning, or execution.

## 9\. Codex project setup result packet

Codex must return:

```text
codex_project_setup_result.v1

setup_id:
project:
repo_root:
module_scope:
setup_state: NOT_CONFIGURED | PARTIAL | READY | BLOCKED
artifacts_checked:
  - path:
    found: true | false
    status:
artifacts_created:
  - path:
    reason:
artifacts_updated:
  - path:
    action:
    customization_preserved: true | false
artifacts_not_touched:
  - path:
    reason:
project_execution_profile:
  path:
  status:
validation_profile:
  path:
  status:
memory_policy:
  path:
  status:
agents_md:
  path:
  status:
codex_config:
  path:
  status:
tool_bindings:
  status:
  missing:
default_autonomy:
default_validation:
forbidden_content_check:
  memory_contains_repository_canon: true | false
  memory_contains_raw_chats: true | false
  memory_contains_direction_state_as_canon: true | false
readback_validation:
  result: pass | fail
  issues:
next_route:
  allowed:
  route:
  reason:
context_request:
  required: true | false
  missing:

```

## 10\. Blocking conditions

Codex must return NEEDS\_INPUT or a Context Request when:

*   repo root cannot be identified;
*   project type cannot be determined enough to define validation;
*   setup artifacts exist but ownership boundaries are unclear;
*   write scope is not authorized;
*   validation commands require unavailable tools and no fallback is known;
*   memory policy would require storing forbidden canonical workflow data;
*   project-owned customization would be overwritten by the proposed patch.

## 11\. Acceptance anchors

A valid install of this note must preserve these anchors:

*   “Project setup MUST run before Codex execution begins”
*   “Memory is never GitHub repository canon”
*   “Workflow updates must not overwrite project-owned customization”
*   “AGENTS.md is the repo-local durable instruction layer”
*   “This procedure MUST NOT modify the current Step 7 stage-development order”

## Validation anchor note

Project setup MUST run before Codex execution begins

Memory is never GitHub repository canon

Workflow updates must not overwrite project-owned customization

AGENTS.md is the repo-local durable instruction layer

This procedure MUST NOT modify the current Step 7 stage-development order