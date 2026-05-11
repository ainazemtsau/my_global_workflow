# 12 Module Knowledge Contract
Status: draft Workflow version: vNext-R REBUILD Installed from roadmap step: Side Amendment SA-01B — Module Governance Installed at: 2026-05-10T04:39:15.4794821+03:00 Source input: ChatGPT SA-01B installable package generated from user request on 2026-05-10 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 12 Module Knowledge Contract

## 1\. Purpose

This contract separates public interface documentation from internal module knowledge.

It prevents Codex from treating all project knowledge as globally loadable, especially when a module is a read-only dependency.

The governing rule is:

Editable modules may load internal docs. Read-only dependency modules expose public interface docs only. Internal docs of read-only dependency modules require scope expansion.

## 2\. Knowledge classes

Module knowledge is divided into these classes.

### 2.1 Public Interface Docs

Public Interface Docs are safe for dependency modules to read.

They describe what another module may rely on without exposing private implementation details.

Public Interface Docs may include:

*   interface summary;
*   exported API signatures;
*   route contracts;
*   CLI contracts;
*   event schemas;
*   data contracts;
*   extension points;
*   public configuration options;
*   supported behaviors;
*   documented side effects;
*   error contracts;
*   version/freshness information;
*   examples for consumers;
*   validation expectations;
*   owner and change policy.

### 2.2 Internal Module Knowledge

Internal Module Knowledge is private to the module unless the module is explicitly editable.

It may include:

*   architecture notes;
*   implementation strategy;
*   private algorithms;
*   private classes and helpers;
*   internal invariants;
*   internal data flow;
*   private tests and fixtures;
*   migration notes;
*   refactor notes;
*   failure analysis;
*   local debugging notes;
*   local AGENTS.md rules;
*   module-private runbooks;
*   partially accepted implementation ideas;
*   stale or experimental design notes.

Internal Module Knowledge must not be loaded for read-only dependency modules without scope expansion.

### 2.3 Operational Evidence

Operational Evidence includes test output, logs, build output, validator output, file read-back / diff verification / commit verification, or diff evidence.

Operational Evidence may be used to validate an editable module. For read-only dependencies, Codex may use public validation outputs only unless scope is expanded.

## 3\. Access matrix

Editable module:

*   may load Public Interface Docs;
*   may load Internal Module Knowledge;
*   may inspect source and tests inside editable paths;
*   may update internal docs when implementation changes;
*   may update Public Interface Docs when public behavior changes;
*   must validate documentation freshness after edits.

Read-only dependency module:

*   may expose Public Interface Docs only;
*   must not expose Internal Module Knowledge;
*   must not have source, tests, private docs, AGENTS.md, or configs edited;
*   must not be reverse-engineered from private internals;
*   must create a Cross-Module Request when the public interface is insufficient.

Forbidden module:

*   may not be edited;
*   may not be used as a new dependency;
*   may be referenced only to explain the boundary or request an owner decision.

Unknown module:

*   is treated as read-only until a Module Map, owner, or approved scope expansion says otherwise.

## 4\. Public Interface Docs minimum content

A module's Public Interface Docs should be sufficient for another module to consume the module without loading internal docs.

Minimum useful Public Interface Docs:

*   module\_id and module\_name;
*   owner or owning role;
*   lifecycle status;
*   public purpose;
*   supported consumers;
*   exported interfaces;
*   input/output contracts;
*   error behavior;
*   side effects;
*   stability level;
*   version or freshness marker;
*   allowed dependency direction;
*   unsupported usage;
*   validation commands or contract tests;
*   change request process;
*   examples of correct use.

If Public Interface Docs are missing or insufficient, Codex must not compensate by reading internal docs of a read-only dependency. It must create a Cross-Module Request or Context Request.

## 5\. Internal Module Knowledge minimum content

Internal Module Knowledge may include:

*   implementation model;
*   private architecture;
*   private invariants;
*   module-specific conventions;
*   known pitfalls;
*   internal validation notes;
*   internal diagrams;
*   local maintenance instructions;
*   active refactor state;
*   stale areas requiring caution.

Internal docs should be useful for the module owner and for Codex only when the module is in editable scope.

Internal docs should not be required by consumers of the module.

## 6\. Freshness rules

Public Interface Docs are authoritative only when marked fresh or confirmed by validation.

If Public Interface Docs are stale, unknown, or conflicting:

*   Codex may not silently use internal docs of a read-only dependency as a substitute;
*   Codex must report the freshness problem;
*   Codex must create a Cross-Module Request when a missing or stale interface blocks work;
*   Codex may continue only with safe work inside the editable module.

If Internal Module Knowledge is stale inside an editable module:

*   Codex may load it with caution;
*   Codex must verify against current files, tests, and validation output;
*   Codex must update or flag stale internal docs when the edit materially depends on them.

## 7\. Documentation update rules

When Codex edits an editable module:

*   update Internal Module Knowledge if implementation details changed materially;
*   update Public Interface Docs if public behavior, API, schema, command contract, or integration behavior changed;
*   update validation notes if tests/checks changed;
*   report any documentation update that was required but not performed.

When Codex works against a read-only dependency:

*   do not update dependency docs directly;
*   do not patch dependency AGENTS.md;
*   do not alter dependency examples;
*   create a Cross-Module Request if the dependency docs need correction.

## 8\. Scope expansion

Scope expansion is required before Codex may:

*   load Internal Module Knowledge for a read-only dependency;
*   inspect private source of a read-only dependency to design a workaround;
*   edit a dependency module;
*   update a dependency module's Public Interface Docs;
*   update a dependency module's AGENTS.md;
*   add a new public interface to a dependency module;
*   change dependency direction;
*   bypass a public interface.

Scope expansion must name:

*   requesting module;
*   target module;
*   reason;
*   newly editable paths;
*   internal docs permitted to load;
*   validation required;
*   owner or human approval source;
*   expected impact on Module Map and Public Interface Docs.

## 9\. Context loading rule for Codex

Codex context loading must follow module scope.

Load by default:

*   Wave Card;
*   Module Map;
*   root AGENTS.md;
*   editable module public docs;
*   editable module internal docs;
*   editable module guidance paths;
*   read-only dependency public docs;
*   validation instructions.

Do not load by default:

*   read-only dependency internal docs;
*   unrelated module internals;
*   old active workflow sources;
*   stale archives;
*   generated files as authority;
*   private implementation notes for forbidden modules.

## 10\. Missing capability rule

When an editable module needs a capability that only a read-only dependency can provide, Codex must not edit the dependency silently.

Required behavior:

1.  check the dependency Public Interface Docs;
2.  use an existing public interface if suitable;
3.  if unsuitable, create a Cross-Module Request;
4.  recommend the smallest safe next route;
5.  avoid companion functionality in unrelated modules unless explicitly approved.

## 11\. Acceptance anchors

This note is valid only if these rules remain visible:

*   Editable modules may load internal docs.
*   Read-only dependency modules expose public interface docs only.
*   Internal docs of read-only dependency modules require scope expansion.
*   Public Interface Docs must be sufficient for dependency consumers.
*   Missing public capability must create a Cross-Module Request or Context Request, not silent private-doc loading.