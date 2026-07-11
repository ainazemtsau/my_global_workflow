# Operating-substrate architecture card — process-pack instantiation

status: accepted
accepted_at: 2026-07-10
session: s-solmax-operating-substrate-process-pack-instantiation-architecture-forge-001
call: c-solmax-operating-substrate-process-pack-instantiation-architecture-forge-001
card_id: operating-substrate-process-pack-instantiation-001
graph_nodes:
  - q04_process_pack_instantiation

## Owner approval

diverge_choice_words: |
  "принимаю твою рекомендацию"

selected_direction: |
  Direction A — staged semantic admission and activation — is the
  architecture backbone.

  Direction B — ownership-scoped layered composition — is retained as
  the mandatory composition and conflict rule inside that lifecycle.

  Direction C — capability requirement and resolution — is retained
  as the subordinate reusable-service and adapter binding mechanism.

freeze_words: |
  "Approve v1"

## Question

Как новый domain/process instantiates universal kernel и reusable
service semantics через process pack, не изобретая заново общие
механизмы, не изменяя kernel и не превращая substrate в жёсткий
consumer template?

## Preserved parent locks

This card does not revise Q1, Q2 or Q3.

The following accepted positions remain unchanged:

1. Operating-substrate is a stable, model-neutral and carrier-neutral
   kernel with pluggable process packs.

2. A concrete domain/process is created through a process pack and
   does not modify kernel semantics.

3. Service zones are semantic responsibility families rather than
   mandatory modules, services, agents, files, processes or
   deployments.

4. Each atomic responsibility claim has one primary normative owner.

5. Kernel, reusable-service, process-pack, owner-profile and
   adapter/implementation concerns remain distinct architecture
   classes.

6. Q3 retains five relationship families and twelve primary semantic
   kinds:

   - invoke, delegate, handoff;
   - query, observe/event, evidence/provenance;
   - propose, validate, decide/authorize, apply/effect;
   - return/result;
   - continue.

7. Every open obligation has one primary current next-action owner.

8. Capability, permission, authorization and approval are
   non-equivalent.

9. Validation, authorization and apply remain semantically
   distinguishable.

10. One primary normative state owner establishes each accepted
    durable version inside one bounded mutable-state boundary.

11. Portable continuation is mandatory while its exact entity model,
    schema and serialization remain open.

12. Durable mutation crosses a logical validated writer/apply
    boundary while physical topology remains open.

13. Universal rollback and universal transactionality are not
    assumed.

14. No final service-zone, service-block list or physical topology is
    accepted.

## Frozen answer

### Process-pack instantiation

Process-pack instantiation is the governed establishment of an
effective process definition for an explicitly bounded process scope.

It occurs through staged semantic admission and activation in which:

1. unchanged kernel semantics are inherited;

2. process-owned declarations are interpreted as legitimate local
   policy and behavior;

3. relevant owner-profile inputs are supplied under provenance,
   privacy and sharing boundaries;

4. reusable-service requirements and adapter capabilities are
   resolved into compatible bindings;

5. atomic effective claims are composed according to their primary
   normative owners;

6. the candidate is checked for semantic validity, compatibility,
   capability sufficiency, ownership, authority, state/effect safety,
   result obligations and continuation obligations;

7. impact on accepted state, open work, pending authority and external
   effects is assessed separately from validation;

8. bounded authorization is obtained where the lifecycle action
   requires it;

9. staging and conformance checking occur without prematurely
   displacing the current accepted definition;

10. the admitted candidate crosses a governed apply/activation
    boundary;

11. an authoritative lifecycle result establishes which definition
    governs each affected scope and obligation;

12. portable continuation preserves compatibility, ownership,
    authority, effect certainty and the next legitimate action.

Instantiation is not merely:

- copying a consumer template;
- filling configuration values;
- merging overlays;
- downloading or installing a package;
- resolving a dependency version;
- binding a model or tool;
- creating a runtime object;
- starting one execution;
- successfully parsing or validating a definition;
- obtaining owner approval without authoritative activation.

### Effective definition

An effective definition is the unambiguous accepted composition of:

- inherited kernel semantics;
- process-pack-owned declarations;
- approved owner-profile inputs;
- reusable-service semantic bindings;
- adapter capability facts and implementation bindings;

that authoritatively governs one bounded process scope or obligation.

An effective definition does not have to exist as one file, object,
package, service, process or runtime instance.

### Core Q4 invariant

For each atomic effective claim it must be possible to determine:

1. its primary normative owner;
2. its origin and provenance;
3. why it applies to the bounded scope;
4. whether it preserves kernel semantics;
5. which capabilities and authority it requires;
6. what accepted state, open work or external effects it may change;
7. which definition was and became authoritative;
8. what evidence supports the lifecycle result;
9. who owns unresolved work;
10. how legitimate continuation can proceed.

Merge order, source order, installation order, discovery order or
physical component order cannot substitute for these answers.

## Semantic terms

The terms below freeze semantic distinctions. They are not mandatory
entity names, lifecycle enum values, packet fields or implementation
stages.

### Available pack

A pack definition can be located or supplied to an environment.

Availability does not establish:

- validity;
- compatibility;
- capability resolution;
- authority;
- admission;
- activation;
- suitability for existing work.

### Installed pack

An environment may consider a pack physically imported, placed or
registered.

Installation is an implementation/environment fact. It does not make
the pack authoritative.

### Candidate definition

A proposed but not yet activated composition of kernel, pack,
approved owner inputs and bindings.

### Admission

The semantic conclusion that a candidate is sufficiently valid,
compatible, satisfiable and policy-coherent to become eligible for
activation in a bounded scope.

Admission does not itself change authoritative process state.

### Binding

The association of an abstract semantic capability requirement with a
compatible reusable service or concrete adapter.

A binding supplies capability. It does not silently receive
process-policy ownership or human authority.

### Activation

The governed apply/effect transition through which an admitted
effective definition becomes authoritative for its stated scope or
work population.

### Degraded route

A pack-declared legitimate mode in which an optional capability is
absent or reduced while all kernel invariants and the pack's
remaining safety, authority, result and continuation obligations
continue to hold.

Silent omission, improvised fallback and authority expansion are not
legitimate degraded routes.

### Compatibility disposition

An explicit conclusion for a pack, binding, durable-state boundary,
open obligation or continuation stating whether it is:

- compatible as-is;
- compatible after bounded revalidation;
- explicitly migratable;
- pinned to the existing definition while draining;
- transferable through an accepted handoff;
- incompatible and rejected;
- unresolved with a named resolution owner.

These are semantic alternatives, not a fixed lifecycle enum.

### Migration

A governed mutation that preserves, transforms or rebinds accepted
durable meaning when a process definition or binding changes.

Migration is not merely data copying. It preserves or explicitly
settles identity, ownership, authority, accepted decisions, effect
certainty, evidence, open obligations and continuation.

### Drain

Continued support for existing work under its accepted definition
while new work is prevented from entering that definition and
remaining obligations are completed, migrated, handed off, rejected
or explicitly closed.

Drain is a semantic lifecycle option, not a selected deployment
mechanism.

## Five normative layers

### Kernel-inherited semantics

Normative owner:

- universal kernel.

Kernel semantics:

- are inherited automatically;
- are not copied into every pack as locally authored policy;
- cannot be disabled, weakened or redefined by a process pack, owner
  profile, reusable service or adapter;
- are checked for conformance during admission and activation.

Kernel-inherited semantics preserve accepted Q1-Q3 guarantees,
including:

- bounded work and execution lifecycle;
- invoke, delegate and handoff;
- query, observe/event and evidence/provenance;
- propose, validate, decide/authorize and apply/effect;
- return/result and continue;
- one current owner for every open obligation;
- retained parent integration and accountability under delegation;
- accepted transfer before handoff changes active ownership;
- one normative state owner per mutable-state boundary;
- capability, permission and authority separation;
- controlled durable mutation;
- effect certainty, evidence and recovery;
- portable continuation;
- governed definition evolution.

An attempted kernel override makes the candidate invalid. It is not a
legitimate process variation.

### Reusable-service semantics and bindings

Three responsibilities remain distinct:

1. The reusable-service contract owns the abstract semantic outcome,
   including its failure and recovery meaning.

2. The process pack owns whether that semantic outcome is needed,
   whether it is mandatory or optional, and under which process
   conditions it applies.

3. The instantiation environment owns selection of a compatible
   concrete implementation binding.

Instantiation must establish:

- the required semantic capability;
- whether it is mandatory or optional for this pack;
- which compatible provider or binding supplies it;
- applicable authority and data-access bounds;
- failure and recovery meaning;
- legitimate degraded behavior;
- replacement and rebinding compatibility.

A reusable-service binding does not become process-policy authority
merely because it supplies capability.

This card does not freeze a reusable-service catalogue.

### Required process-pack declarations

Normative owner:

- process/domain pack.

A process pack must semantically define all required process-local
variation. Declaration concern categories may include:

- process objective and applicability;
- domain procedures and routing policy;
- domain vocabulary and local role meanings;
- process-local state, memory, source and evidence distinctions;
- result and evidence sufficiency;
- domain-specific safety and effect policy;
- local delegation and escalation policy;
- budgets, stop conditions and failure meaning;
- required and optional semantic capabilities;
- legitimate degraded routes;
- compatibility and migration obligations;
- replacement and removal obligations;
- process-specific conformance scenarios.

These are semantic concern categories, not mandatory manifest
sections, fields or objects.

A pack must not:

- redefine kernel relationship semantics;
- claim owner-wide facts as process truth without provenance;
- bind itself irreversibly to one provider as the semantic meaning of
  a capability;
- grant authority merely by declaring capability;
- treat a local artifact or configuration as proof of live
  usefulness.

### Owner-profile inputs

Normative owner:

- owner or owner-authorized profile responsibility.

Owner-profile inputs may supply genuinely cross-process concerns such
as:

- language and presentation preferences;
- initiative, ask and proceed preferences;
- privacy and sharing defaults;
- owner-wide approval preferences;
- approved shared constraints and context;
- explanation and decision style.

Instantiation must:

- project only relevant, approved owner-wide inputs;
- retain provenance;
- preserve privacy and sharing boundaries;
- distinguish owner preference from process policy;
- detect conflict with mandatory domain safety or effect policy;
- avoid promoting one process's local assumption into the owner
  profile;
- prevent owner preference from weakening a kernel invariant.

Exact owner-profile content and schema remain downstream Q5/Q10 work.

### Adapter and implementation bindings

Normative owner for concrete capability facts:

- implementation environment.

Normative owner for allowed use and authority:

- the applicable kernel, pack or authority responsibility.

Adapter binding establishes:

- which capability is actually supplied;
- compatibility with the required semantic contract;
- current availability and limits;
- credential and authority scope;
- retry and effect behavior;
- evidence and receipts;
- substitution and recovery route.

A model, runtime, tool, store, repository, transport, UI, validator,
scheduler or orchestration system does not become architectural
authority.

Concrete runtime identifiers may be retained as references but do not
define process identity or portable continuation by themselves.

## Ownership-scoped composition

### Primary composition rule

Each atomic effective claim is accepted from exactly one primary
normative owner.

Other layers may:

- supply evidence;
- implement capability;
- propose change;
- validate;
- authorize bounded use;
- constrain access;
- reference the claim;

but cannot silently become a second normative owner.

### Composition is not overlay precedence

The effective definition is not formed by generic
last-write-wins precedence.

Merge order, source order, installation order and runtime discovery
order do not determine authority.

The following conflicts must be rejected or explicitly resolved:

1. A process pack attempts to change a kernel semantic.

2. An owner preference attempts to weaken mandatory domain safety.

3. An adapter capability fact is interpreted as permission or
   authority.

4. A reusable service attempts to define process-local policy.

5. Two layers claim primary ownership of one mutable-state boundary.

6. A binding expands authority or access beyond the approved scope.

7. Provider-specific behavior masquerades as universal process
   meaning.

8. A conflict is hidden through generic override precedence.

9. A process-local fact becomes owner-wide context without provenance
   and promotion.

10. A candidate changes result or continuation meaning without a
    separate accepted architecture decision.

### Conflict disposition

If a conflict cannot be removed by correctly decomposing the atomic
claims, the candidate is:

- rejected;
- retained as unresolved with a named resolution owner;
- or routed to an authority owner only where the disputed decision
  legitimately falls inside that authority.

An authority decision cannot legalize a kernel override.

## Availability, admission, authorization and activation

These are semantically non-equivalent.

### Availability or installation

The pack or binding is present in the environment.

This does not establish:

- validity;
- compatibility;
- semantic completeness;
- conformance;
- authority;
- admission;
- activation.

### Validation and admission

The candidate is assessed against:

- kernel semantics;
- process-pack declaration coherence;
- capability sufficiency;
- ownership closure;
- authority closure;
- current-state preconditions;
- effect and recovery obligations;
- open-work compatibility;
- result and continuation obligations;
- process-specific conformance scenarios.

Validation produces a bounded conclusion.

Admission establishes eligibility for activation. It does not make the
candidate authoritative.

### Authorization

An authority holder approves, denies, conditions or revokes a
specific bounded lifecycle action.

Authorization must remain bound to the proposal and may become stale
when any of these change:

- target;
- candidate definition;
- evidence;
- policy;
- current state;
- affected work population.

Authorization does not prove that activation occurred.

### Activation

Activation occurs as a Q3 apply/effect transition.

Only an authoritative activation result establishes that a candidate
became the effective definition for the stated scope.

## Bounded scenario grammar

This is a scenario grammar, not a mandatory state machine, message
sequence, lifecycle enum or physical topology.

One implementation may physically combine several phases. Conformance
must nevertheless preserve their semantic distinctions and evidence.

### 1. Propose a bounded lifecycle action

The current work owner proposes one bounded action:

- new instantiation;
- upgrade;
- service or adapter rebind;
- recovery;
- migration;
- replacement;
- removal.

The proposal identifies its intended outcome and affected scope.

No candidate becomes authoritative during proposal.

### 2. Establish the current accepted basis

Before evaluating a candidate, establish:

- current effective definition;
- accepted durable state;
- open obligations and their current owners;
- parent/child ownership;
- pending decisions and authority bounds;
- applied, partial or outcome-unknown effects;
- relevant evidence and provenance;
- continuations and compatibility claims.

Absence of the original repository, registry or package source does
not erase the accepted basis.

### 3. Inherit kernel semantics

Attach the unchanged kernel contract.

Reject every candidate declaration that attempts to redefine,
disable or weaken inherited semantics.

### 4. Interpret process-pack declarations

Establish the candidate process-owned meaning, including as
applicable:

- procedures and routing;
- domain policy;
- state, evidence and result expectations;
- capability requirements;
- degraded routes;
- compatibility and migration obligations;
- replacement and removal behavior;
- process-specific conformance scenarios.

Exact declaration representation remains open.

### 5. Project approved owner-profile inputs

Supply only relevant and approved owner-wide preferences, policy and
shared context.

Projection preserves provenance, privacy and sharing boundaries.

Owner preference cannot silently override kernel semantics or
mandatory process policy.

### 6. Resolve reusable-service and adapter bindings

Match each declared semantic requirement to a compatible provider.

Semantic outcomes may include:

- resolved;
- missing mandatory capability;
- missing optional capability with a legitimate degraded route;
- incompatible provider;
- unresolved conflict;
- insufficient authority or credentials.

Capability resolution does not grant new human authority.

### 7. Compose by normative ownership

Form the candidate effective definition from:

- inherited kernel semantics;
- process-owned declarations;
- owner-profile inputs;
- reusable-service contracts and bindings;
- adapter capability facts.

Reject:

- kernel override;
- duplicate primary normative ownership;
- ambiguous state ownership;
- hidden authority expansion;
- unsafe generic precedence;
- provider-specific semantics masquerading as process meaning.

### 8. Validate the candidate

Validate:

- integrity and provenance;
- kernel conformance;
- declaration coherence;
- mandatory capability satisfiability;
- ownership and authority closure;
- mutation and external-effect paths;
- result obligations;
- portable continuation obligations;
- current-state preconditions;
- open-work compatibility;
- migration and removal feasibility;
- pack-specific conformance evidence.

Validation is not authorization or activation.

### 9. Assess impact and issue an admission disposition

Determine separately:

- which definition would become authoritative;
- which process scope would change;
- which open obligations are affected;
- which work is compatible without change;
- which work requires bounded revalidation or migration;
- which work must remain pinned;
- which work can drain;
- which work requires handoff;
- which work is incompatible;
- which durable state or external effects may change;
- what evidence and uncertainty remain;
- which bounded authority decisions are required.

Admission is permitted only after acceptable validation and an
explicit impact disposition.

### 10. Decide or authorize where required

Route only genuinely required bounded decisions to the applicable
authority owner.

Potential authority pressures include:

- broader external-effect authority;
- changed privacy or sharing boundary;
- irreversible migration;
- removal that destroys required state availability;
- changed approval policy;
- acceptance of a material compatibility gap.

Exact gate categories and thresholds remain downstream Q10 work.

### 11. Stage and check without displacement

Candidate bindings, migration work and conformance scenarios may be
prepared and tested while the current accepted definition remains
authoritative.

Staging does not automatically route live work to the candidate.

Every preparatory effect retains Q3 effect-certainty semantics.

### 12. Activate through the governed apply boundary

Apply the admitted and, where required, authorized candidate to the
stated scope.

After successful activation:

- affected obligations have an unambiguous effective definition;
- each open obligation retains a current next-action owner;
- migrated, pinned, draining, handed-off, rejected and unresolved work
  are distinguishable;
- authoritative state boundaries remain explicit;
- effective bindings and authority scopes are known;
- continuation is updated.

Activation does not require one physical orchestrator, service, store
or writer.

### 13. Verify, return and continue

The lifecycle result must semantically state:

- whether admission succeeded;
- whether activation was attempted;
- the authoritative activation outcome;
- which definition is authoritative after the attempt;
- which bindings are effective;
- what was migrated, pinned, draining, handed off or rejected;
- effect certainty;
- evidence and limitations;
- open obligations and their current owners;
- next legitimate action;
- continuation disposition.

Exact result and continuation fields remain downstream Q9/Q12 work.

### 14. Operate, observe and re-enter the grammar

During operation the process may detect:

- binding disappearance;
- compatibility drift;
- stale authority;
- pack or adapter deprecation;
- failed conformance checks;
- new evidence;
- changed owner-profile inputs;
- source disappearance.

Observation does not silently mutate the effective definition.

Upgrade, rebind, recovery, replacement and removal re-enter proposal,
validation, impact, authority and apply semantics.

Hidden hot-swap that changes process meaning for open work without
compatibility disposition and updated continuation is prohibited.

## Capability behavior

### Missing mandatory capability

If a mandatory semantic capability cannot be resolved:

- the candidate does not activate for the affected scope;
- the missing semantic requirement is identified;
- a current resolution owner is named;
- permitted correction routes remain explicit;
- the current accepted definition remains authoritative when no
  effect crossed the apply boundary;
- no broader or semantically different provider is silently
  substituted.

### Missing optional capability

An optional capability may be absent only under an explicit
pack-declared legitimate degraded route.

The degraded route must:

- preserve kernel guarantees;
- preserve mandatory safety and authority policy;
- preserve remaining process obligations;
- disclose changed result quality or unavailable behavior;
- retain evidence limitations;
- avoid authority expansion;
- avoid reporting absent capability as successful completion.

If no legitimate degraded route exists, the capability is mandatory
for that instantiation.

If absence breaks a kernel invariant, safety obligation or result
contract, the capability is not semantically optional.

### Dynamic discovery and rebinding

Dynamic discovery is permitted as an implementation technique.

A binding may use a bounded reduced readmission path only when evidence
establishes preservation of:

- abstract service outcome;
- authority and data-access scope;
- failure and recovery semantics;
- retry and effect behavior;
- evidence contract;
- continuation compatibility;
- process meaning.

If any of these changes, full semantic admission and impact assessment
are required.

## Versioning and compatibility

### Version identity

Every accepted effective definition must retain enough identity,
lineage and compatibility evidence to determine:

- which semantics governed the work;
- which definition replaced it;
- whether a continuation can resume;
- which bindings were effective;
- which migrations were applied.

Exact identifiers and version syntax remain open.

### Compatibility is multidimensional

Equal version identity does not prove compatibility.

Compatibility may independently concern:

- kernel semantic contract;
- process-pack definition lineage;
- procedure and policy meaning;
- reusable-service contract;
- adapter capability;
- durable-state interpretation;
- open-obligation lifecycle;
- pending authorization;
- external-effect certainty;
- result semantics;
- continuation import and resume;
- migration and removal behavior.

### Per-obligation disposition

An upgrade does not have to move all work immediately to the newest
definition.

Each affected open obligation must receive one explicit disposition:

1. compatible resume under the successor;

2. bounded revalidation and migration;

3. pin to the old definition while draining;

4. accepted handoff to another compatible process;

5. explicit rejection or unresolved closure with a named owner.

Silent abandonment and ownerless waiting are invalid.

### Continuation compatibility

Portable continuation must preserve enough accepted semantics to
determine:

- effective definition;
- relevant compatibility claim;
- work identity;
- current owners;
- decisions and authority;
- state and effect status;
- pending obligations;
- next legitimate action.

A new runtime or carrier cannot claim compatibility merely because it
can parse or display the continuation.

## Current accepted definition and failure behavior

### Invalid, incompatible or failed-validation candidate

The candidate is rejected before activation.

If the apply boundary was not crossed:

- the current accepted definition remains authoritative;
- no live work is silently assigned to the candidate;
- reasons and evidence are preserved;
- correction, replacement or unresolved routes remain explicit.

Best-effort bypass of kernel, authority, state, effect, result or
continuation conflicts is prohibited.

### Failed-known-not-done staging or activation

If authoritative evidence establishes that activation did not occur:

- the previous accepted definition remains authoritative;
- the result records failed-known-not-done;
- retry is allowed only under a bounded safe policy;
- preparatory effects are cleaned up only where ownership and
  reversibility are established.

### Partial effect

If activation or migration partially applied:

- universal rollback is not claimed;
- boundaries using old and new definitions are identified;
- unsafe new work may be suspended;
- every affected obligation receives a current owner;
- authoritative state is reconciled;
- recovery may include forward repair, continued migration,
  compensation, pin/drain or accepted handoff;
- the lifecycle result reports partial effect.

### Outcome unknown

If it is unknown whether activation crossed the apply boundary:

- the candidate is not declared active by assumption;
- the previous definition is not declared globally unchanged without
  evidence;
- unaffected scopes retain the previous accepted definition;
- the affected scope receives an unresolved
  authoritative-definition disposition;
- unsafe retry is blocked;
- a current recovery owner reconciles authoritative state;
- continuation preserves uncertainty, owners and permitted next
  actions.

### Recovery

Recovery may mean:

- resume;
- authoritative query and reconciliation;
- known-safe retry;
- rebinding;
- completion of migration;
- pin and drain;
- repair;
- accepted handoff;
- bounded owner decision;
- compensating effect;
- explicit unresolved closure.

Compensation is a new governed effect. It does not erase history and
requires its own validation, authority and apply semantics.

Rollback is one possible recovery route, not a universal guarantee.

## Lifecycle evolution

### Upgrade

A successor pack enters the same scenario grammar.

New work may be assigned to the successor while old work remains
pinned and drains.

Forced latest-version execution is not a universal rule.

### Rebinding

Rebinding changes a concrete reusable-service or adapter binding.

It must not silently change process meaning, authority, state
ownership, effect behavior or continuation compatibility.

A semantic change makes the rebind a full readmission action.

### Migration

Migration must preserve or explicitly settle:

- durable identity;
- current ownership;
- parent/child ownership;
- accepted state;
- decisions;
- authority and approvals;
- external-effect certainty;
- evidence and provenance;
- open obligations;
- result expectations;
- next legitimate action;
- continuation compatibility.

### Pin and drain

An old definition may continue serving existing work while new
obligations no longer enter it.

Drain completes only when remaining obligations are:

- completed;
- migrated;
- handed off;
- rejected;
- or explicitly closed with a named owner.

### Replacement

Replacement may cross process-pack lineage and is not assumed to be a
compatible upgrade.

It requires:

- mapping of still-legitimate responsibilities;
- state and continuation compatibility assessment;
- migration or accepted ownership handoff;
- explicit treatment of changed policy and authority;
- preservation of history and evidence;
- governed activation of the successor;
- governed retirement of the predecessor.

### Deprecation and source disappearance

Deprecation or source disappearance is an observation, not automatic
removal.

Accepted durable work does not become invalid merely because the
original package or repository is unavailable.

The process must preserve:

- definition identity and provenance;
- ability to interpret accepted state;
- open obligations and current owners;
- migration or replacement route;
- continuation compatibility.

### Removal

Removal is blocked while any of these remains unresolved:

- an open obligation without a successor owner or continuation;
- durable state whose meaning cannot be interpreted after removal;
- pending authorization;
- partial or outcome-unknown effect;
- a binding still required by existing work;
- evidence or audit material that would be lost;
- a continuation with no compatible resume route.

Safe removal may require:

- drain;
- migration;
- accepted handoff;
- revocation of pack-specific authority;
- preservation of evidence and compatibility information;
- final result;
- portable continuation.

Removal is governed closure, not file or package deletion.

## Preservation of Q3 semantics

Each process-pack lifecycle action preserves Q3 relationship
distinctions:

| Q4 responsibility | Q3 semantic meaning |
|---|---|
| Propose instantiation, upgrade, migration or removal | propose |
| Assess validity and compatibility | validate |
| Obtain bounded permission | decide/authorize |
| Make a definition authoritative or mutate durable meaning | apply/effect |
| Report authoritative lifecycle outcome | return/result |
| Preserve open work through change or interruption | continue |

This is a semantic mapping, not a mandatory message sequence.

All lifecycle actions preserve these invariants:

1. Every open obligation has one current next-action owner.

2. Delegation retains parent integration and accountability.

3. Handoff changes ownership only after accepted transfer.

4. Each mutable-state boundary has one primary normative state owner.

5. Capability does not create permission or authority.

6. Validation is not authorization.

7. Authorization is not apply.

8. Apply result distinguishes applied, failed-known-not-done, partial
   and outcome-unknown.

9. Result is not equivalent to an artifact or final runtime output.

10. Continuation preserves unresolved ownership, authority and effect
    certainty.

11. Cancellation or timeout does not prove absence of effect.

12. Unknown effect blocks blind retry.

13. Migration and removal do not silently close obligations.

14. Owner-facing result does not require the owner to operate or read
    internal admission machinery.

## Process-pressure stress test

### Health-like safety-critical pressure

Pressure characteristics:

- high consequence of unsupported claims or effects;
- strict provenance and source handling;
- domain-specific safety and escalation policy;
- privacy constraints;
- long-lived evidence;
- stale approval risk;
- controlled external effects.

Kernel-inherited semantics include:

- bounded work and explicit current owner;
- query, evidence, propose, validate, authorize, apply, result and
  continue distinctions;
- authoritative state ownership;
- controlled durable mutation;
- effect certainty and recovery;
- portable continuation.

Pack-owned semantics include:

- health-domain vocabulary and applicability;
- domain procedures and routing;
- evidence thresholds and source-quality rules;
- safety and escalation policy;
- domain effect classes;
- success, stop and unresolved-result criteria;
- required capabilities;
- process-specific conformance scenarios.

Owner-profile inputs may include:

- language and explanation preference;
- approved privacy and sharing defaults;
- owner-wide approval preference inside applicable domain constraints;
- approved shared context.

Reusable-service and adapter bindings supply only the capabilities
required by the pack.

Missing mandatory provenance, validation, controlled-effect or
continuation capability blocks admission.

An optional capability may be absent only through a pack-declared safe
degraded route.

Pending approvals remain bound to the exact proposal and are
revalidated when evidence, policy or state becomes stale.

Incompatible open obligations may remain pinned and drain or undergo
explicit migration.

Removal is blocked while open obligations, accepted state or
continuation cannot proceed legitimately.

Verdict:

PASS.

Health-specific policy remains process-pack-owned. It does not modify
kernel semantics and does not become universal policy.

### Game/productive-play creative pressure

Pressure characteristics:

- exploratory and branching work;
- rapid iteration;
- frequently reversible local changes;
- partly subjective creative quality;
- optional visualization, retrieval or evaluation capabilities;
- frequent owner steering;
- fewer high-impact approval gates.

Kernel-inherited semantics include:

- bounded obligations and explicit ownership;
- delegation, handoff and result;
- proposal versus applied durable canon/state change;
- evidence and provenance where relevant;
- portable continuation across carriers.

Pack-owned semantics include:

- game or productive-play vocabulary;
- creative procedures and iteration rhythm;
- local canon, rule and artifact distinctions;
- playtest and evaluation criteria;
- routing between exploration, convergence and production;
- local budgets and stop criteria;
- optional capabilities and degraded-route policy.

Owner-profile inputs may include:

- explanation and decision style;
- initiative preference;
- privacy and presentation preferences.

Optional retrieval, visualization or evaluation capability may be
absent when the pack defines a legitimate useful degraded route.

Absence cannot authorize fabricated visual evidence or false
completion.

Irreversible artifact publication or another external effect still
crosses Q3 validation, authority and apply semantics.

Verdict:

PASS.

The same kernel and admission grammar support a lower-stakes,
exploratory process without importing Health policy or changing
kernel semantics.

### Cross-pressure verdict

The Q4 boundary supports:

- fail-closed behavior for mandatory safety capabilities;
- legitimate degraded operation for optional creative capabilities;
- materially different domain policies;
- different evidence thresholds;
- different interaction rhythms;

without:

- copying one consumer into another;
- modifying kernel semantics;
- requiring one final service-block list;
- selecting a schema;
- selecting a carrier, runtime or topology.

The cartography return condition is not triggered.

## Rejected alternatives

1. Process pack as a copyable consumer template.

   Rejected because a new process would become a copy of Health,
   Zaratusta, Direction OS, game or another current consumer.

2. Configuration merge as the whole instantiation model.

   Rejected because merge order does not establish normative
   ownership, authority, effect safety, admission or activation.

3. Generic last-write-wins precedence.

   Rejected because it can silently change kernel semantics, state
   ownership, authority or domain safety.

4. Ownership-layer composition as the complete primary answer.

   Rejected because composition alone does not define admission,
   activation, migration, failure, recovery or removal.

   Its useful part is retained as the mandatory composition and
   conflict rule.

5. Capability resolver as the complete primary answer.

   Rejected because a resolver cannot determine process policy, human
   authority, open-work compatibility or safe activation.

   Its useful part is retained as the reusable-service and adapter
   binding mechanism.

6. Availability or installation equals activation.

   Rejected because presence does not establish validity,
   compatibility, authority or authoritative apply.

7. Every reusable service is mandatory for every process.

   Rejected because materially different processes have different
   capability needs.

8. Silent optional fallback.

   Rejected because it hides changed result meaning and may violate
   safety or evidence obligations.

9. Force all work onto the newest version.

   Rejected because open obligations, accepted state, continuations
   and pending authority may be incompatible.

10. Version equality equals compatibility.

    Rejected because compatibility is a multidimensional semantic
    relation.

11. Universal rollback.

    Rejected because external effects, migrations and partial
    activation may be outside the rollback mechanism's ownership.

12. Hidden hot-swap without readmission.

    Rejected when rebinding changes process meaning, authority,
    state/effect behavior or continuation compatibility.

13. Removal as package or file deletion.

    Rejected because durable state, evidence, bindings and open
    obligations may continue to depend on the definition.

14. Framework entities as substrate entities.

    OSGi bundles, Terraform modules, Helm charts, OPA bundles,
    VS Code extensions, Temporal deployments and Kubernetes resources
    remain source-system concepts rather than universal substrate
    entities.

15. Valid pack equals useful live process.

    Rejected because package validity and artifact completeness do not
    prove owner-facing usefulness. The Zaratusta live trial showed
    that complete state/intake/handback surfaces can still produce
    bureaucratic and ineffective live operation.

## Evidence anchors and limits

### Evidence anchors

Parent architecture:

- live/solmax/work/operating-substrate/cards/operating-substrate-core-invariant-001.md
- live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md
- live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-relationship-001.md

Main research input:

- live/solmax/work/operating-substrate-process-pack-instantiation-best-practice-research-001.md

Live-use failure evidence:

- live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md

Research compared:

- OSGi;
- Terraform;
- Helm;
- Open Policy Agent;
- Visual Studio Code extensions;
- Temporal;
- Kubernetes API versioning.

Cross-source evidence strongly supports:

- definition, availability, resolution, validation and activation are
  distinct;
- abstract requirements and concrete bindings are distinct;
- missing mandatory requirements block activation;
- invalid candidates should not displace the last-known-good
  definition before authoritative activation;
- old work may require pin/drain or explicit migration;
- version identity alone is insufficient for compatibility;
- removal requires treatment of state and open work;
- rollback claims are bounded by the effects actually controlled by
  the mechanism.

### Evidence limits

1. No reviewed source defines the complete desired
   operating-substrate.

2. Extension hosts are not owner-led durable AI-process substrates.

3. Infrastructure tools use explicit schemas and platform-specific
   apply behavior that are not universal substrate semantics.

4. Temporal provides strong durability and compatibility evidence but
   assumes a durable workflow runtime and replay constraints.

5. No reviewed source contains the accepted Q3 semantic relationship
   model.

6. No reviewed source defines a universal owner-profile layer.

7. No reviewed source provides full carrier-neutral continuation
   across models, providers and runtimes.

8. Exact scenario-phase granularity is architecture synthesis.

9. Per-obligation compatibility disposition is architecture
   synthesis.

10. Pack-declared degraded routes are architecture synthesis.

11. It remains open whether one effective process can compose several
    peer packs.

12. Minimum evidence for automatic successor resume remains open.

13. Exact lifecycle actions requiring owner authorization remain open.

14. No actual process pack was implemented or live-tested by the
    research.

15. Valid admission does not prove useful owner-facing operation.

16. Vendor and project documentation may change after the research
    observation date.

## Child and downstream questions

### Q4 child questions

The following do not block Q4:

1. Can one effective definition compose several peer process packs
   while retaining unambiguous normative ownership?

2. What semantic compatibility relation is sufficient for automatic
   resume under a successor pack?

3. Which capability changes are simple rebinding and which require
   full readmission?

4. What evidence establishes that old obligations and durable state
   have fully drained before removal?

5. How are lineage-preserving upgrade and cross-lineage replacement
   distinguished?

6. What minimum process-pack-specific conformance evidence is required
   before activation?

7. How are owner-profile changes revalidated against an already active
   pack?

8. How is the authoritative current definition reconciled when
   activation outcome is unknown?

9. Which lifecycle effects permit compensation, genuine reversal or
   only forward repair?

10. How is continuation preserved when the original pack source
    disappears?

### Existing downstream routes

- Q5: shared owner context, projection, provenance, sharing and
  local-versus-owner-wide boundary.

- Q6: durable state, history and accepted-definition persistence.

- Q7: reusable routing/procedure semantics versus pack-owned
  procedures.

- Q8: owner-facing admission, degraded operation and migration without
  exposing internal bureaucracy.

- Q9: exact semantic minimum for lifecycle result and portable
  continuation.

- Q10: lifecycle authority and approval gates.

- Q11: version identity, compatibility, migration, replacement,
  removal and evidence-driven evolution.

- Q12: entities, representation, identity, correlation and binding
  protocol.

- Q13: conformance and live-use proof scenarios.

- Q14: mapping to Markdown, chat, applications, registries and
  transports.

None is a hidden prerequisite for the bounded Q4 answer.

## Not frozen

This card does not freeze:

- actual Health, Zaratusta, game or Direction OS process packs;
- final service-zone list;
- final reusable-service list;
- manifest;
- configuration schema;
- entity schema;
- message schema;
- continuation schema;
- migration schema;
- field names;
- identifiers;
- version syntax;
- compatibility expression language;
- exact lifecycle enum;
- exact physical phase implementation;
- one-pack or multi-pack cardinality;
- repository;
- registry;
- storage;
- runtime;
- framework;
- model;
- provider;
- resolver algorithm;
- transport;
- API;
- orchestration topology;
- deployment topology;
- physical writer;
- application architecture;
- UI;
- setup workflow;
- owner-profile schema or concrete content;
- proof harness;
- universal transactionality;
- universal rollback;
- consumer template;
- Direction OS changes.

## Graph verdict

hidden_prerequisite: none
gap_event: none
top_level_rebalance: not_needed
return_to_cartography: not_required
implementation_activation: prohibited

Q4 is ready to remain frozen because:

1. Q1-Q3 supply all required parent semantics.

2. The scenario grammar can be defined without a schema or
   implementation.

3. Atomic normative ownership permits composition without generic
   precedence.

4. Mandatory and optional capability behavior are distinguishable.

5. Last-known-good, partial and outcome-unknown behavior can be
   specified without universal rollback.

6. Health-like and game/productive-play pressures pass without
   consumer copying.

7. Open identity, representation, gate and proof questions fit
   existing Q5-Q14 routes.

Next graph route:

- bounded best-practice and failure-case research for Q5 shared owner
  context;
- then one separate Q5 architecture-forge;
- no implementation, carrier, repository or final service-block work.

## Gate

status: PASS

Checks:

- Q1 remains unchanged.
- Q2 remains unchanged.
- Q3 remains unchanged.
- The card answers only Q4 process-pack instantiation.
- Process-pack instantiation is defined semantically.
- Kernel, reusable-service, process-pack, owner-profile and adapter
  concerns remain distinct.
- Atomic claims retain one primary normative owner.
- Ambiguous kernel, authority, state and effect overrides are rejected.
- The scenario grammar is bounded without becoming a state enum,
  manifest or topology.
- Availability, installation, admission, authorization and activation
  remain distinct.
- Missing mandatory capability blocks activation.
- Optional absence requires an explicit legitimate degraded route.
- Capability, permission, authorization and approval remain distinct.
- Validation, authorization and apply remain distinct.
- Invalid candidates do not displace the current accepted definition
  before authoritative activation.
- Incompatible versions and open work receive explicit compatibility
  dispositions.
- Migration, recovery, pin/drain, rebinding, replacement and removal
  are covered.
- Failed-known-not-done, partial and outcome-unknown effects are
  covered without universal rollback.
- Q3 ownership, authority, effect-certainty, result and continuation
  semantics are preserved through every lifecycle action.
- Health-like and game/productive-play pressures pass without
  modifying kernel semantics or copying one consumer into another.
- Rejected alternatives, evidence limits, downstream questions and
  graph verdict are recorded.
- No implementation, schema, carrier, provider, topology, consumer
  template or final service-block list is selected.
- Owner choice and approval words are recorded.

END_OF_FILE: live/solmax/work/operating-substrate/cards/operating-substrate-process-pack-instantiation-001.md
