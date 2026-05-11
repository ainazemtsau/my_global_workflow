# 11 Module Map and Boundary Contract
Status: draft Workflow version: vNext-R REBUILD Installed from roadmap step: Side Amendment SA-01B — Module Governance Installed at: 2026-05-10T04:39:15.4794821+03:00 Source input: ChatGPT SA-01B installable package generated from user request on 2026-05-10 Authority: Trilium canonical after read-back Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 11 Module Map and Boundary Contract

## 1\. Purpose

This contract defines how Codex must identify, respect, and validate module boundaries in modular projects.

The governing safety rule is:

Cross-module missing capabilities must create a Cross-Module Request, not a silent edit.

Codex must never silently edit unrelated modules, dependency modules, shared infrastructure, generated outputs, or old active workflow sources merely because a requested task appears easier if boundaries are ignored.

## 2\. Scope

This contract applies to Codex work that touches a repository, app, package, service, plugin, workflow component, Trilium-backed module, or any project divided into separately owned functional areas.

It applies before future C1/C2 runtime prompts are finalized, but it is not a C1 or C2 prompt.

It governs:

*   module ownership;
*   module paths;
*   public interfaces;
*   dependencies;
*   forbidden dependencies;
*   read/edit rules;
*   validation rules;
*   AGENTS.md and module guidance paths;
*   cross-module escalation.

## 3\. Module Map requirement

Before Codex edits a modular project, the active Codex Wave must identify its module scope.

A Module Map is the authoritative project artifact that records module boundaries. It may live in Trilium, the repository, or both, but the Codex Wave Card must name the exact Module Map path or state that the Module Map is missing.

If the Module Map is missing and the project is clearly modular, Codex must not infer broad edit permission. It must either:

*   operate only inside the explicitly named path/module from the Wave Card; or
*   return a Context Request asking for module scope; or
*   create a proposed Module Map draft if the Wave explicitly authorizes documentation work.

## 4\. Required Module Map fields

Each module entry must define:

*   module\_id: stable identifier used in Wave Cards and Cross-Module Requests.
*   module\_name: human-readable name.
*   owner: responsible human, team, Direction, stage, or maintainer role.
*   lifecycle\_status: active, draft, deprecated, read-only, generated, archived, or unknown.
*   root\_paths: source roots owned by the module.
*   test\_paths: tests owned by the module.
*   doc\_paths: documentation owned by the module.
*   config\_paths: configuration owned by the module.
*   generated\_paths: generated or build-output paths that Codex must not hand-edit unless explicitly authorized.
*   public\_interface\_docs: paths to docs that dependency modules may read.
*   internal\_module\_docs: paths to implementation knowledge that only editable modules may load.
*   module\_guidance\_paths: module-specific AGENTS.md, README, runbook, lint/test instructions, and local coding rules.
*   public\_interfaces: exported APIs, CLIs, schemas, routes, events, commands, data contracts, or integration points.
*   allowed\_dependencies: modules this module may use through public interfaces.
*   forbidden\_dependencies: modules, paths, APIs, private internals, or dependency directions this module must not use.
*   editable\_paths: exact paths Codex may edit when this module is in editable scope.
*   read\_only\_dependency\_paths: paths Codex may read when this module is only a dependency.
*   validation\_rules: tests, checks, commands, read-back requirements, or manual checks needed after edits.
*   boundary\_change\_policy: what requires owner approval, scope expansion, or a Cross-Module Request.
*   freshness: fresh, stale, unknown, or conflicting.
*   last\_verified\_source: source of the latest boundary confirmation.

## 5\. Module ownership rules

A module owner controls:

*   the module public interface;
*   the module internal knowledge;
*   dependency policy;
*   module-local AGENTS.md guidance;
*   module validation rules;
*   acceptance criteria for edits to the module.

Codex must not infer ownership solely from filesystem proximity, import paths, naming similarity, or convenience.

When ownership is unknown, Codex must treat the module as read-only until scope is clarified.

## 6\. AGENTS.md and module guidance paths

The Module Map must name all known guidance paths relevant to module work, including:

*   repository root AGENTS.md;
*   nested AGENTS.md files;
*   module-specific AGENTS.md;
*   module README or runbook;
*   module test/lint/build instructions;
*   generated-code instructions;
*   documentation maintenance instructions.

AGENTS.md hierarchy applies as follows:

*   root guidance applies globally unless overridden by narrower guidance;
*   module guidance applies inside the module boundary;
*   narrower guidance may constrain local work;
*   narrower guidance cannot expand the Wave edit scope beyond the Module Map or Wave Card;
*   conflicting guidance must trigger a Context Request or Human Decision Card before edits continue.

## 7\. Public interfaces

A public interface is the stable surface other modules may rely on.

Public interfaces may include:

*   exported functions, classes, components, packages, or modules;
*   API routes;
*   CLIs and command contracts;
*   event schemas;
*   database contracts explicitly declared public;
*   message formats;
*   configuration contracts;
*   extension points;
*   public docs and examples.

Dependency modules may use public interfaces only. They may not rely on private implementation details, private tests, internal docs, or accidental filesystem structure.

## 8\. Dependency rules

Allowed dependencies must be declared in the Module Map.

A dependency is allowed only when:

*   the requesting module uses the target module through a public interface;
*   the dependency direction is permitted;
*   validation exists for the integration or the lack of validation is explicitly reported;
*   no forbidden dependency rule is violated.

Forbidden dependencies include:

*   importing private internals of another module;
*   editing another module to make the current task easier without scope expansion;
*   creating cyclic dependencies not allowed by the Module Map;
*   reaching into another module's tests, fixtures, internals, or generated files;
*   bypassing public interfaces;
*   creating companion functionality in unrelated modules without approval;
*   changing shared infrastructure when the Wave is scoped to a leaf module;
*   using stale or unknown internal docs as authority.

## 9\. Read/edit scope matrix

Editable module:

*   Codex may read public interface docs.
*   Codex may load internal module knowledge.
*   Codex may read module source, tests, docs, configs, and guidance paths.
*   Codex may edit declared editable paths.
*   Codex may update module docs and validation artifacts when required by the edit.
*   Codex must run or report module validation.

Read-only dependency module:

*   Codex may read public interface docs only.
*   Codex may not load internal module knowledge.
*   Codex may not edit source, tests, docs, AGENTS.md, configs, or generated paths.
*   Codex may not inspect private internals to design around the public interface.
*   Codex must create a Cross-Module Request when the public interface is insufficient.

Forbidden module:

*   Codex must not edit.
*   Codex must not depend on it.
*   Codex may read only the minimal public information needed to identify the boundary, unless the Wave Card explicitly authorizes more.
*   Any needed capability must become a Cross-Module Request.

Unknown module:

*   Codex must treat as read-only.
*   Codex may inspect only enough public structure to identify the owner or request missing scope.
*   Ambiguity must trigger a Context Request.

## 10\. Internal docs access rule

Editable modules may load public interface docs and internal module knowledge for that module.

Read-only dependency modules expose public interface docs only.

Internal docs of read-only dependency modules require scope expansion.

Scope expansion must be explicit in the Wave Card, a Human Decision Card, an approved Cross-Module Request, or another accepted routing artifact.

## 11\. Validation rules

Every module edit must produce evidence.

Required validation evidence:

*   files changed, grouped by module;
*   whether each changed module was editable;
*   validation commands run;
*   validation results;
*   validation commands not run and why;
*   public interface changes, if any;
*   Module Map changes, if any;
*   Cross-Module Requests created, if any;
*   boundary violations avoided.

When a public interface changes, Codex must validate:

*   the edited module;
*   dependent contract tests, when available;
*   public docs freshness;
*   Module Map dependency entries;
*   downstream integration risk.

When validation is unavailable, Codex must explicitly say so and provide the smallest useful substitute evidence.

## 12\. Boundary violation handling

Codex must stop or reroute when it detects:

*   a needed edit outside editable module scope;
*   missing capability in a read-only dependency module;
*   stale public interface docs;
*   conflict between Module Map and repository reality;
*   need to load internal docs for a read-only dependency;
*   need to change AGENTS.md outside editable scope;
*   need to alter forbidden dependencies;
*   ambiguous ownership;
*   generated output that appears to require source regeneration.

The default handling is:

1.  preserve current edits inside authorized scope if safe;
2.  do not edit the target module;
3.  create a Cross-Module Request;
4.  recommend the next route.

## 13\. Minimum Codex Wave Card module fields

A Codex Wave Card for modular work should include:

*   editable\_modules;
*   read\_only\_dependency\_modules;
*   forbidden\_modules;
*   Module Map path;
*   public interface docs to load;
*   internal docs allowed to load;
*   module AGENTS.md paths;
*   validation commands by module;
*   expected changed modules;
*   explicit out-of-scope modules;
*   cross-module request handling rule.

If these fields are absent and the work is modular, Codex must operate under the narrowest safe interpretation of the user request.

## 14\. Acceptance anchors

This note is valid only if these rules remain visible:

*   Cross-module missing capabilities must create a Cross-Module Request, not a silent edit.
*   Editable modules may load public interface docs and internal module knowledge for that module.
*   Read-only dependency modules expose public interface docs only.
*   Internal docs of read-only dependency modules require scope expansion.
*   AGENTS.md/module guidance paths must be named in the Module Map or treated as missing context.