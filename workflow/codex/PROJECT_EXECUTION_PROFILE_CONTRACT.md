# 08 Project Execution Profile Contract
artifact_control:
  artifact_name: "08 Project Execution Profile Contract"
  schema: codex_workflow_contract.v1
  owner_layer: codex_runtime_contract
  status: canonical
  repo_path: "workflow/codex/PROJECT_EXECUTION_PROFILE_CONTRACT.md"
  authority: "GitHub repository canonical after file read-back / diff verification / commit verification"
  activation_scope: workflow_runtime_reference
  freshness: refresh_when_codex_runtime_contract_changes
  last_updated: "2026-05-13"

# 08 Project Execution Profile Contract

## 1\. Purpose

The Project Execution Profile defines the minimum project-local execution context Codex needs before planning or changing a repository.

It answers:

*   what project Codex is working in;
*   where the repo root is;
*   what technology stack is present;
*   what level of autonomy Codex may use by default;
*   what validation level Codex must use by default;
*   which validation, memory, module, and tool profiles apply.

This contract is generic across project types. It must not assume one global technology stack.

## 2\. Canonicality and scope

The Project Execution Profile is an execution setup artifact.

It is not a replacement for GitHub repository Direction canon, Goal state, Phase state, or Workflow stage prompts.

It may be represented in a repo-local setup file, an AGENTS.md managed section, a Codex setup profile, or another explicit project-local artifact selected by the project. The selected location must be recorded.

When GitHub repository stores a pointer or summary for this profile, GitHub repository remains canonical only for the Workflow rebuild documentation and any explicitly accepted GitHub repository Direction state. The repo-local project profile remains the operative project-owned execution setup for Codex.

## 3\. Required fields

A valid Project Execution Profile must define these fields.

### 3.1 Identity

*   `profile_id`
*   `profile_version`
*   `project_name`
*   `project_type`
*   `profile_status`
*   `created_at`
*   `updated_at`
*   `owner_or_source`
*   `profile_location`

### 3.2 Scope

*   `repo_root`
*   `module_scope`
*   `monorepo_layout`
*   `write_scope`
*   `protected_paths`
*   `read_only_paths`
*   `generated_paths`
*   `external_dependency_boundaries`

### 3.3 Technology stack

*   `languages`
*   `frameworks`
*   `package_managers`
*   `build_systems`
*   `test_frameworks`
*   `linters`
*   `formatters`
*   `runtime_targets`
*   `deployment_targets`
*   `database_or_schema_tools`
*   `documentation_tools`

Technology stack fields must be evidence-based. Unknown fields must be marked `unknown`, not guessed.

### 3.4 Default autonomy

The profile must define a default autonomy level.

Recommended autonomy levels:

*   `A0_READ_ONLY`: inspect and report only.
*   `A1_SETUP_ONLY`: create or patch setup artifacts only.
*   `A2_PATCH_WITH_PREVIEW`: propose patches and wait for approval.
*   `A3_PATCH_WITH_VALIDATION`: apply bounded patches and run required validation.
*   `A4_MULTI_FILE_EXECUTION`: execute approved multi-file work with evidence and validation.
*   `A5_HIGH_RISK_REQUIRES_HUMAN`: stop for human approval before risky, destructive, external, credentialed, or deployment-related actions.

The profile must state which autonomy level is default and which actions require escalation.

### 3.5 Default validation

The profile must define:

*   default validation profile link;
*   default validation level;
*   minimum validation for setup-only work;
*   minimum validation for code changes;
*   minimum validation for high-risk changes;
*   allowed validation fallbacks;
*   required evidence for skipped checks.

### 3.6 Linked profiles

The profile must link to:

*   Validation Profile;
*   Memory Policy;
*   module profiles, if any;
*   tool binding profile;
*   AGENTS.md path;
*   `.codex/config.toml` path, if used;
*   Wave Record or Codex execution record location, if used.

### 3.7 Human approval gates

The profile must define when Codex must stop for human approval.

At minimum, human approval is required for:

*   destructive filesystem operations;
*   production deployment;
*   secret or credential handling;
*   database migration execution;
*   broad dependency upgrades;
*   license-sensitive changes;
*   replacing project-owned customization;
*   changing the default autonomy or validation profile;
*   writing memory that could be mistaken for canon.

### 3.8 Evidence requirements

The profile must define what Codex must report after execution:

*   changed files;
*   commands run;
*   validation results;
*   skipped validation and reason;
*   file read-back / diff verification / commit verification results for setup artifacts;
*   known risks;
*   next recommended route.

## 4\. Minimal profile shape

A Project Execution Profile should be serializable in a simple structured form.

Recommended shape:

```text
project_execution_profile.v1

identity:
  profile_id:
  profile_version:
  project_name:
  project_type:
  profile_status:
  created_at:
  updated_at:
  owner_or_source:
  profile_location:

scope:
  repo_root:
  module_scope:
  monorepo_layout:
  write_scope:
  protected_paths:
  read_only_paths:
  generated_paths:
  external_dependency_boundaries:

technology_stack:
  languages:
  frameworks:
  package_managers:
  build_systems:
  test_frameworks:
  linters:
  formatters:
  runtime_targets:
  deployment_targets:
  database_or_schema_tools:
  documentation_tools:
  evidence:

defaults:
  autonomy_level:
  validation_profile:
  validation_level:
  setup_validation_level:
  code_change_validation_level:
  high_risk_validation_level:

linked_profiles:
  validation_profile_path:
  memory_policy_path:
  module_profiles:
  tool_binding_profile_path:
  agents_md_path:
  codex_config_path:
  wave_record_location:

human_approval_gates:
  required_for:
  escalation_rule:

evidence_requirements:
  changed_files_required: true
  commands_required: true
  validation_summary_required: true
  skipped_validation_reason_required: true
  setup_readback_required: true

customization_policy:
  preserve_project_owned_customization: true
  managed_sections:
  custom_sections:

```

## 5\. Project type classification

`project_type` should use the smallest accurate label.

Examples:

*   `software_repo`
*   `monorepo`
*   `documentation_repo`
*   `data_project`
*   `workflow_project`
*   `content_project`
*   `automation_project`
*   `mixed_project`
*   `unknown`

A project may have multiple tags, but Codex must still identify the primary execution mode.

## 6\. Validation binding rule

The Project Execution Profile does not define every validation command itself. It links to the Validation Profile.

The Project Execution Profile must state:

*   default validation level;
*   when to escalate validation;
*   where validation commands are defined;
*   how to report skipped validation.

## 7\. Memory binding rule

The Project Execution Profile does not define all memory rules itself. It links to the Memory Policy.

The Project Execution Profile must state:

*   memory policy path;
*   whether technical memory may be written;
*   who owns memory;
*   where memory is stored;
*   which memory writes require human approval.

Memory must not be used as GitHub repository canon.

## 8\. Tool binding rule

The Project Execution Profile must identify tool bindings needed for execution.

Tool binding may include:

*   shell access;
*   git access;
*   package manager;
*   test runner;
*   build runner;
*   language server;
*   MCP servers;
*   repository hosting integration;
*   GitHub repository integration, if explicitly available;
*   task management integration, if explicitly available.

Missing tools must be explicit. Codex must not pretend validation was run when the tool was unavailable.

## 9\. Update rules

Codex may update the Project Execution Profile only under an allowed setup or maintenance route.

Updates must:

*   preserve project-owned customization;
*   patch managed sections only;
*   keep unknown fields explicit;
*   record evidence for changed stack assumptions;
*   update timestamps;
*   avoid changing default autonomy silently;
*   avoid changing default validation silently;
*   return a file read-back / diff verification / commit verification result.

## 10\. Invalid profiles

A Project Execution Profile is invalid if it:

*   lacks repo root;
*   lacks project type;
*   lacks default autonomy;
*   lacks default validation;
*   lacks a Validation Profile link;
*   lacks a Memory Policy link;
*   stores Direction State as project setup;
*   stores Active Goal as canon;
*   stores Wave Card as canon;
*   treats raw chat as durable setup;
*   overwrites project-owned customization without approval;
*   hardcodes one technology stack globally.

## 11\. Acceptance anchors

A valid install of this note must preserve these anchors:

*   “project type”
*   “repo root”
*   “technology stack”
*   “default autonomy”
*   “default validation”
*   “links to validation, memory, module, and tool profiles”
*   “preserve project-owned customization”
*   “must not assume one global technology stack”