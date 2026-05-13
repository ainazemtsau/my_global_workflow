# 14 Codex Tool Binding Matrix

artifact_control:
  artifact_name: "14 Codex Tool Binding Matrix"
  schema: codex_workflow_contract.v1
  owner_layer: codex_runtime_contract
  status: canonical
  repo_path: "workflow/codex/CODEX_TOOL_BINDING_MATRIX.md"
  authority: "GitHub repository canonical after file read-back / diff verification / commit verification"
  activation_scope: workflow_runtime_reference
  freshness: refresh_when_codex_runtime_contract_changes
  last_updated: "2026-05-13"

## 1\. Purpose

This note defines governance for when Codex-facing tools, project files, validators, memory systems, and review helpers are required, optional, or forbidden.

SA-01A/B/C install governance/contracts only. They do not configure any concrete repo/project.

Concrete project setup happens later per project through CODEX\_PROJECT\_SETUP.

CODEX\_PROJECT\_SETUP is responsible for actual project/repo configuration, including:

*   AGENTS.md
*   .codex/config.toml
*   Task Master AI project/tag/ledger
*   Serena project binding/indexing
*   Basic Memory project namespace/policy
*   MCP/tool bindings
*   validation commands
*   module map
*   module knowledge
*   tool binding status

This matrix is not a substitute for concrete setup. It tells the workflow when setup is needed and what evidence Codex must return.

## 2\. Binding state definitions

| State | Meaning |
| --- | --- |
| REQUIRED | The tool/artifact must exist or Codex must return NEEDS\_INPUT before performing the affected work. |
| CONDITIONALLY REQUIRED | Required only when the trigger condition is present. |
| OPTIONAL | Useful but not mandatory; Codex may proceed without it if the acceptance target is still safely testable. |
| FORBIDDEN | Codex must not use, create, infer, or claim the tool/artifact in that circumstance. |
| DEFER\_TO\_CODEX\_PROJECT\_SETUP | Governance requires the item to be configured later in a concrete project setup packet, not in SA-01A/B/C. |

## 3\. Tool binding matrix

| Tool / artifact | Governance role | Required when | Optional when | Forbidden when | Concrete setup owner | Required Codex evidence |
| --- | --- | --- | --- | --- | --- | --- |
| AGENTS.md | Repo-local operating contract for Codex and coding agents. | Required before nontrivial code execution in a concrete repo, especially multi-file, multi-module, validator-sensitive, or convention-sensitive work. | Optional for non-code workflow design, pure GitHub repository governance, or one-off analysis with no repo changes. | Forbidden to invent as a generic global contract, write outside the concrete repo, or treat as installed when CODEX\_PROJECT\_SETUP has not created/read it. | CODEX\_PROJECT\_SETUP. | Path, existence/file read-back / diff verification / commit verification status, relevant instruction summary, and whether Codex followed it. |
| .codex/config.toml | Concrete Codex runtime/tool configuration. | Required when the project needs explicit sandbox, approval, MCP, model, validator, or tool settings. | Optional when default Codex configuration is sufficient and low-risk. | Forbidden to define inside SA-01 governance notes as if it were a real project config. | CODEX\_PROJECT\_SETUP. | Path, active profile summary, enabled MCP/tools, restrictions, and validation that config was read. |
| Task Master AI project/tag/ledger | Task graph substrate for decomposition, dependencies, and work tracking. | Required for multi-task, multi-wave, cross-module, repeated-repair, or long-running Codex work. | Optional for a small isolated fix with clear acceptance and no dependency graph. | Forbidden as DONE authority. Task Master AI is graph substrate, not DONE authority. A task state cannot replace acceptance evidence, validator output, or review. | CODEX\_PROJECT\_SETUP, then per-wave Codex updates. | Project/tag, task IDs, dependency edges, status changes, and explicit statement that DONE is determined by acceptance evidence, not Task Master status. |
| Serena project binding/indexing | Semantic code navigation, symbol search, dependency understanding, and refactor support. | Required for unfamiliar repos, cross-file edits, module-boundary work, semantic refactors, or architecture-sensitive changes where text search is insufficient. | Optional for small edits in known files with low coupling. | Forbidden as canonical documentation, storage, or proof of correctness. Forbidden to claim Serena analysis if project binding/indexing was unavailable. | CODEX\_PROJECT\_SETUP. | Project binding name/path, indexing status, key symbols/files inspected, and findings used. |
| Basic Memory project namespace/policy | Durable technical recall for project/module implementation facts across waves. | Required when repeated Codex waves need recall of module decisions, prior defects, validator quirks, or repo-specific implementation facts. | Optional for one-off work where no durable technical recall is needed. | Forbidden as GitHub repository canon, project authority, acceptance proof, or replacement for module map/module knowledge. Basic Memory is project/module technical recall only, not GitHub repository canon. | CODEX\_PROJECT\_SETUP. | Namespace, memory policy, entries read/written, and confirmation no sensitive/private data was stored outside policy. |
| MCP/tool bindings | Concrete bindings for external tools such as repository access, validators, Task Master, Serena, Basic Memory, filesystem, or other project tools. | Required when a workflow step depends on those tools for execution, validation, memory, graph updates, or review. | Optional for pure design work that can be completed without external execution. | Forbidden to assume available. If a required MCP/tool binding is missing, Codex must return NEEDS\_INPUT or use an explicitly approved fallback. | CODEX\_PROJECT\_SETUP. | Tool list, enabled/disabled status, failure modes, and which tools were actually used. |
| Validators / validation commands | Evidence-producing commands for tests, lint, typecheck, build, smoke tests, scripts, or project-specific checks. | Required before Codex claims implementation work is complete, unless the work is explicitly non-code or no validator exists and the gap is disclosed. | Optional for pure documentation/governance work if file read-back / diff verification / commit verification anchors are sufficient. | Forbidden to skip silently, weaken, delete, or replace with unrelated checks. Forbidden to claim DONE when validators were not run and no valid reason is given. | CODEX\_PROJECT\_SETUP defines commands; Codex runs them per wave. | Exact command, working directory, result, relevant output summary, failures, reruns after repair, and untested risk. |
| Skills | Specialized execution protocols for artifact types, repo operations, or workflow-specific handling. | Required when the environment provides a relevant mandatory skill/protocol for the task type. | Optional when no specific skill applies. | Forbidden to use the wrong skill path when a task-specific protocol is mandatory; forbidden to ignore mandatory artifact/tool instructions. | Environment/project setup plus Codex execution. | Skill/protocol name, when used, and any required output artifact/file read-back / diff verification / commit verification. |
| Subagents / independent reviewers | Separate review or specialized pass for high-risk, complex, cross-module, security/privacy-sensitive, or repeated-failure work. | Required when the Independent Validation / Review Protocol triggers review and a separate reviewer/subagent is available. | Optional for routine low-risk work. | Forbidden to claim independent review when the same implementer performed only ordinary self-review. If required independence is unavailable, Codex must disclose the limitation and escalate according to policy. | CODEX\_PROJECT\_SETUP may bind available reviewers; Codex requests/uses them per wave. | Reviewer identity/type, scope, checklist results, issues found, and disposition. |

Validation anchor: Serena is trigger-based semantic code/navigation/refactor support.

## 4\. Default decision rules

1.  Governance notes may require that a tool be present for a class of work, but they do not configure the concrete tool.
2.  When a required binding is missing in a concrete project, Codex must return NEEDS\_INPUT or an explicit CODEX\_PROJECT\_SETUP request.
3.  Codex may not silently downgrade required tools to optional tools.
4.  Codex may proceed without optional tools only if acceptance remains testable and the Codex Return Packet discloses the omission.
5.  Task Master state, Basic Memory entries, Serena findings, and MCP availability are supporting evidence only. They do not replace acceptance criteria, validator results, file read-back / diff verification / commit verification, or human-required review.
6.  Concrete tool binding status must be recorded by CODEX\_PROJECT\_SETUP before project execution waves depend on those tools.

## 5\. CODEX\_PROJECT\_SETUP minimum tool-binding status

For each concrete project, CODEX\_PROJECT\_SETUP must produce a tool-binding status section with at least:

*   project name
*   repo path or project root
*   branch or workspace status if applicable
*   AGENTS.md status
*   .codex/config.toml status
*   Task Master AI project/tag/ledger status
*   Serena binding/indexing status
*   Basic Memory namespace/policy status
*   MCP/tool binding status
*   validation commands and working directories
*   module map status
*   module knowledge status
*   unavailable tools and fallback policy
*   high-risk work review mechanism

## 6\. Codex Return Packet evidence requirements

When any tool in this matrix is required or used, Codex must return evidence in the Codex Return Packet.

Minimum evidence:

*   tool/artifact name
*   required/optional/forbidden classification for the work
*   whether it was available
*   whether it was used
*   what it changed, if anything
*   what it proved, if anything
*   what it did not prove
*   validator/review/file read-back / diff verification / commit verification output when relevant
*   unresolved setup gaps

Codex cannot claim DONE from tool presence alone. DONE requires acceptance fit, evidence, validation, and required review outcome.