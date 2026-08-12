---
id: g-zara-extensible-areas-workflows
_kind: node
_parent: g-zara
status: parked
label: Расширение без переделки ядра
hook: Новые Areas и Workflows регистрируются без изменения центральных semantics.
_pos: 3
---

## goal
New Areas, Capabilities, Operations and Workflows can be developed, tested,
owner-approved and registered without changing central routing, authority,
trace or web-navigation semantics.
## done_when
1. Stable registration contracts exist for Area manifests, capabilities,
   operations, workflows, state/projection providers, effects, evals and UI
   sections.
2. A new Capability inside Health and one materially different second Area or
   equivalent cross-Area scenario are added through their own handlers and
   contracts without editing central router semantics.
3. Registered additions automatically appear in navigation, owner overview,
   workflow/run history and eval views through fixed projection/component
   types; central pages contain no Area-specific branches.
4. Pre-activation checks cover identity/reference integrity, schemas,
   context/authority/effects, transition compatibility, eval coverage and
   replay/idempotency.
5. Semantic instructions are reviewed by owner or model returning typed
   verdict; deterministic code never grades prose.
6. Lifecycle is explicit (`draft -> tested -> owner-approved -> active`, with
   revise/reject), versioned, rollback-capable and unable to self-activate.
7. No general process language, universal dashboard DSL or renewed universal
   Process Creator is introduced.
## why
This is the mechanical proof behind the root extensibility criterion: the Nth
capability is registration plus handler and tests, not another kernel rewrite.
## edge
The owner already has several materially different domains and Workflow 2 as
requirements/negative evidence, so extensibility can be tested against real
differences rather than toy plugins.
## risk
A universal factory may reappear before useful Areas exist. If onboarding one
addition needs more platform code than domain work, keep a manual explicit
package template and return to dogfood.
## журнал
2026-08-13 · map Zaratustra finalized: owner-approved six-node 1→6 roadmap recorded with four evidence-backed boundaries, old unfinished operating-manager branch dropped, and Health converge opened as the sole frontier · history/2026-08-13-s-solmax-zaratustra-map-finalize-026.md
END_OF_FILE: live/solmax/cards/g-zara-extensible-areas-workflows.md
