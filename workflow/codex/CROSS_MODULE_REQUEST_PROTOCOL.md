# 13 Cross-Module Request Protocol
Status: draft Workflow version: vNext-R REBUILD Installed from roadmap step: Side Amendment SA-01B — Module Governance Installed at: 2026-05-10T04:39:15.4794821+03:00 Source input: ChatGPT SA-01B installable package generated from user request on 2026-05-10 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 13 Cross-Module Request Protocol

## 1\. Purpose

This protocol defines how Codex must request capability, interface, documentation, or scope changes in another module.

It prevents silent cross-module edits.

A Cross-Module Request must include requesting module, target module, needed capability, proposed interface, alternatives, risk, and recommended next route.

## 2\. Trigger conditions

Codex must create a Cross-Module Request when any of the following occurs:

*   the editable module needs a capability from a read-only dependency module;
*   the public interface of a dependency module is missing, stale, ambiguous, or insufficient;
*   the task appears to require editing a module outside the Wave's editable scope;
*   Codex needs internal docs of a read-only dependency;
*   Codex needs to update AGENTS.md outside editable scope;
*   Codex needs a new dependency direction;
*   Codex needs to remove or alter a forbidden dependency;
*   Codex needs to change shared infrastructure while scoped to a module;
*   Codex discovers a boundary conflict in the Module Map;
*   Codex would otherwise create duplicate companion functionality in the requesting module;
*   a test failure appears rooted in a read-only dependency;
*   the safest fix belongs in another module.

## 3\. Required non-action before request

Before creating the request, Codex must not:

*   edit the target module;
*   load target module internal docs;
*   patch target module Public Interface Docs;
*   patch target module AGENTS.md;
*   add private imports;
*   create hidden coupling;
*   bypass the target public interface;
*   move files across module boundaries;
*   modify generated artifacts as a substitute for source changes;
*   mark the task DONE if the needed capability remains unresolved.

## 4\. Cross-Module Request required fields

Every Cross-Module Request must include:

*   request\_id: stable local identifier.
*   status: proposed, blocked, human\_decision\_needed, approved\_for\_scope\_expansion, routed\_to\_new\_wave, rejected, or resolved.
*   requesting\_module: module that needs the capability.
*   target\_module: module expected to provide the capability or change.
*   requested\_by: Codex Wave, stage, Direction, task, or human source.
*   current\_edit\_scope: modules and paths currently editable.
*   needed\_capability: the missing behavior, interface, data, validation, or documentation.
*   proposed\_interface: the smallest public interface or contract that would satisfy the need.
*   alternatives: options considered, including use of existing public interface, local workaround, deferral, or scope cut.
*   why\_alternatives\_are\_insufficient: concise explanation.
*   risk: coupling, regression, security, stale docs, dependency direction, validation, ownership, migration, or scope risk.
*   expected\_files\_or\_paths: likely target docs, APIs, schemas, tests, or configs, if known from public docs.
*   validation\_needed: target-module and integration validation expected.
*   documentation\_impact: Public Interface Docs, Internal Module Knowledge, AGENTS.md, Module Map, or Project File changes expected.
*   module\_map\_impact: whether dependencies, forbidden dependencies, ownership, or validation rules need updates.
*   blocking\_status: blocking, nonblocking, optional, or defer.
*   recommended\_next\_route: Human Decision Card, scope expansion, new Codex Wave for target module, documentation repair, use existing interface, defer, reject, or split work.
*   owner\_decision\_needed: yes/no and owner if known.
*   notes: short supporting evidence.

## 5\. Minimal request template

Use this shape when emitting a Cross-Module Request:

Cross-Module Request:

*   request\_id:
*   status:
*   requesting\_module:
*   target\_module:
*   requested\_by:
*   current\_edit\_scope:
*   needed\_capability:
*   proposed\_interface:
*   alternatives:
*   why\_alternatives\_are\_insufficient:
*   risk:
*   expected\_files\_or\_paths:
*   validation\_needed:
*   documentation\_impact:
*   module\_map\_impact:
*   blocking\_status:
*   recommended\_next\_route:
*   owner\_decision\_needed:
*   notes:

## 6\. Recommended next routes

Codex must recommend one route.

Allowed routes:

*   Human Decision Card: use when ownership, priority, risk, or dependency direction requires human choice.
*   Scope expansion: use when the same Wave should continue only after explicit approval expands editable modules and internal-doc access.
*   New Codex Wave for target module: use when the target module owner should implement or expose the capability.
*   Documentation repair: use when Public Interface Docs are stale, incomplete, or conflicting.
*   Use existing public interface: use when a safe public route exists.
*   Defer: use when the missing capability is not needed for the smallest safe version.
*   Reject: use when the request would create harmful coupling or overbuild.
*   Split work: use when part of the current module work can finish while target-module work is separately routed.

## 7\. Output placement

A Cross-Module Request must appear in the Codex Return Packet under a clearly labeled cross\_module\_requests section.

If the active Direction has a designated GitHub repository path for cross-module requests, Codex may propose a Repository Patch to create or update that note.

If no designated path exists, Codex must not invent a random durable location. It must include the request in the Codex Return Packet and recommend a target path for human approval.

A Cross-Module Request is not proof that the target module changed. It is a routing artifact.

## 8\. Interaction with Repository Patch

A Repository Patch may create or update a Cross-Module Request note only when the target path is explicitly named by the Wave Card, Direction context, or human instruction.

The patch must not modify:

*   target module source;
*   target module tests;
*   target module internal docs;
*   target module AGENTS.md;
*   accepted stage prompts;
*   Direction Project Files;
*   old active Workflow vNext;
*   unrelated workflow notes.

## 9\. Continue-or-stop rule

After creating a Cross-Module Request, Codex may continue only if all remaining work is inside authorized editable scope and does not depend on the unresolved target capability.

Codex must stop and return a blocker when:

*   the current task cannot be completed without the target module change;
*   continuing would create duplicate functionality;
*   continuing would make a public interface assumption;
*   validation would be misleading without the target change;
*   ownership is ambiguous;
*   scope expansion is required.

## 10\. Resolution states

A Cross-Module Request may be resolved by:

*   approved scope expansion;
*   target module implementation;
*   target module public docs update;
*   using an existing interface;
*   deferring the capability;
*   rejecting the capability;
*   splitting work into a separate Wave;
*   updating the Module Map.

Resolution must include:

*   who/what resolved it;
*   changed files or docs, if any;
*   validation evidence;
*   remaining risks;
*   whether the requesting module must be revisited.

## 11\. Evidence expectations

Codex must provide evidence that it respected module boundaries:

*   changed files grouped by module;
*   target module untouched unless scope was approved;
*   internal docs not loaded for read-only dependencies;
*   public docs used for dependencies;
*   Cross-Module Requests emitted for missing capabilities;
*   validation run or explicitly not runnable;
*   unresolved blockers stated.

## 12\. Acceptance anchors

This note is valid only if these rules remain visible:

*   A Cross-Module Request must include requesting module, target module, needed capability, proposed interface, alternatives, risk, and recommended next route.
*   Cross-module missing capabilities must create a Cross-Module Request, not a silent edit.
*   Target module edits require explicit editable scope or approved scope expansion.
*   Read-only dependency internal docs cannot be loaded merely to avoid a request.
*   The request must be emitted in the Codex Return Packet and routed, not buried in prose.