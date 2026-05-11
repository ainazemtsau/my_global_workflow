# 10 Memory Policy Contract
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Side Amendment SA-01A — Codex Project Setup Core Installed at: 2026-05-10T04:16:01.8896091+03:00 Source input: ChatGPT SA-01A side amendment output Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 10 Memory Policy Contract

## 1\. Purpose

The Memory Policy defines what Codex may store as durable project or module technical memory.

It governs:

*   what memory may contain;
*   what memory must never contain;
*   where memory may live;
*   how memory is scoped;
*   when memory may be updated;
*   how stale memory is handled;
*   how memory relates to AGENTS.md, Project Execution Profile, Validation Profile, and GitHub repository.

## 2\. Core rule

Memory is never GitHub repository canon.

Memory may help Codex remember stable technical facts about a repo or module. It must not become the canonical source for Direction state, Workflow state, Goal state, Phase state, Wave state, or GitHub repository content.

GitHub repository canon must not be mirrored into memory.

## 3\. Allowed memory content

Memory may store stable technical information such as:

*   repo layout facts;
*   module boundaries;
*   build or validation quirks;
*   command usage notes;
*   environment constraints;
*   framework-specific conventions;
*   generated-file rules;
*   protected path rules;
*   common failure modes;
*   stable dependency constraints;
*   code style conventions;
*   known test flakiness with evidence;
*   setup lessons learned after validation.

Allowed memory must be:

*   scoped to project, repo, module, or package;
*   evidence-backed;
*   concise;
*   dated;
*   reviewable;
*   safe to become stale without corrupting workflow canon.

## 4\. Forbidden memory content

Memory must not store any of the following as canon:

*   Direction State;
*   Active Goal;
*   Wave Card;
*   Phase state;
*   Stage Result Packet;
*   raw chats;
*   GitHub repository mirrors;
*   GitHub repository file bodies copied wholesale;
*   old workflow exports;
*   raw Wave JSON as authoritative state;
*   secrets;
*   credentials;
*   private tokens;
*   production passwords;
*   sensitive personal data;
*   unvalidated speculation;
*   stale project status;
*   user intent snapshots that should remain in Direction state;
*   unresolved human decisions as if decided.

Memory may include a pointer to a canonical GitHub repository file or Direction artifact only when the pointer is clearly non-canonical and does not copy the canonical content.

## 5\. AGENTS.md relationship

`AGENTS.md` is the repo-local durable instruction layer.

It may contain:

*   coding-agent operating rules;
*   repo conventions;
*   module-specific instructions;
*   validation commands;
*   protected paths;
*   memory policy pointer;
*   project execution profile pointer;
*   validation profile pointer.

`AGENTS.md` must not become a GitHub repository mirror.

`AGENTS.md` must not store Direction State, Active Goal, or Wave Card as canon.

## 6\. .codex/config.toml relationship

`.codex/config.toml` may define project-scoped Codex or MCP configuration when needed.

It may contain:

*   project-scoped tool bindings;
*   MCP server configuration references;
*   Codex execution preferences;
*   safe defaults.

It must not contain:

*   secrets unless the project’s secure configuration policy explicitly allows and protects them;
*   canonical Direction State;
*   raw chats;
*   GitHub repository mirrors.

`.codex/config.toml` is optional and must not be created without a clear execution need.

## 7\. Recommended memory locations

Project memory location must be explicit.

Allowed examples:

*   `AGENTS.md` managed memory section;
*   `.codex/memory/project.md`;
*   `.codex/memory/modules/<module>.md`;
*   module-local `AGENTS.md`;
*   project-approved documentation path.

The selected path must be recorded in the Project Execution Profile.

## 8\. Memory scope levels

Memory must declare scope.

Recommended scope levels:

*   `project`;
*   `repo`;
*   `module`;
*   `package`;
*   `tool`;
*   `validation`;
*   `environment`.

Memory must not use vague scope such as “current workflow” unless the scope is defined.

## 9\. Required memory entry shape

A memory entry should use this structure:

```text
technical_memory_entry.v1

entry_id:
scope:
applies_to:
status: active | stale | superseded | rejected
created_at:
updated_at:
source_evidence:
summary:
details:
validation_link:
risk_if_stale:
staleness_triggers:
owner:
supersedes:
superseded_by:
canonicality_notice: This is technical memory only. It is not GitHub repository canon.

```

## 10\. Memory update rules

Codex may propose or write memory only when:

*   the active route permits memory updates;
*   the Memory Policy permits the memory type;
*   the memory is technical and scoped;
*   the memory is evidence-backed;
*   the memory does not duplicate GitHub repository canon;
*   project-owned customization is preserved;
*   stale or superseded memory is marked rather than silently overwritten.

Codex must not write memory from raw chat without distilling it into a technical, evidence-backed entry.

## 11\. Staleness rules

Memory must be marked stale or superseded when:

*   validation commands change;
*   repo layout changes;
*   module ownership changes;
*   AGENTS.md contradicts it;
*   Project Execution Profile contradicts it;
*   Validation Profile contradicts it;
*   Codex observes contrary evidence;
*   human instruction overrides it.

Stale memory must not be silently used as current fact.

## 12\. Customization protection

Workflow updates must not overwrite project-owned customization.

When memory files already exist, Codex must:

*   read existing content;
*   identify managed sections;
*   preserve project-authored sections;
*   patch only allowed sections;
*   report conflicts;
*   request input when ownership is unclear.

## 13\. Memory and execution evidence

Validation results may produce memory only when they reveal stable technical facts.

Allowed example:

*   “Module X requires command Y from repo root because command Z fails when run inside the module directory.”

Forbidden example:

*   copying the full validation log into memory;
*   storing a one-time failure as permanent truth without evidence;
*   storing the current Wave Card as project memory.

## 14\. Memory and GitHub repository

Memory may point to GitHub repository only as a non-canonical reference.

Allowed:

*   “Canonical Direction state lives in GitHub repository; this memory does not reproduce it.”

Forbidden:

*   copying GitHub repository file bodies into memory;
*   using memory as the canonical location for Direction State;
*   using memory as the canonical location for Active Goal;
*   using memory as the canonical location for Wave Card.

## 15\. Invalid memory policy

A Memory Policy is invalid if it:

*   treats memory as GitHub repository canon;
*   allows raw chats as durable memory;
*   allows GitHub repository mirrors;
*   allows Direction State as repo memory canon;
*   allows Active Goal as repo memory canon;
*   allows Wave Card as repo memory canon;
*   lacks scope rules;
*   lacks staleness rules;
*   lacks customization protection;
*   allows secrets to be stored unsafely.

## 16\. Acceptance anchors

A valid install of this note must preserve these anchors:

*   “Memory is never GitHub repository canon”
*   “Memory must not store Direction State, Active Goal, Wave Card as canon”
*   “raw chats”
*   “GitHub repository mirrors”
*   “AGENTS.md is the repo-local durable instruction layer”
*   “Workflow updates must not overwrite project-owned customization”
*   “stale memory must not be silently used as current fact”

## Validation anchor note

Memory is never GitHub repository canon

Memory must not store Direction State, Active Goal, Wave Card as canon

raw chats

GitHub repository mirrors

AGENTS.md is the repo-local durable instruction layer

Workflow updates must not overwrite project-owned customization

stale memory must not be silently used as current fact