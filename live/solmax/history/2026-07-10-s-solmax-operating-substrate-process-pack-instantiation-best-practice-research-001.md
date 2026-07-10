RESULT s-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001 (call: c-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001)
direction: solmax
play: research
node/task: g-operating-substrate/c-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001
parent: s-solmax-operating-substrate-service-zone-relationship-architecture-forge-001

outcome: |
  Research status: COMPLETE.
  Architecture status: RESEARCH INPUT ONLY — this session does not approve or
  draft the Q4 process-pack instantiation architecture card.
  gap_event: none.
  hidden_prerequisite: none.
  top_level_graph_rebalance: not_required.
  q4_forge_readiness: READY.

  Proposed artifact path:
  live/solmax/work/operating-substrate-process-pack-instantiation-best-practice-research-001.md

  # Research note — process-pack instantiation and adaptation semantics

  status: research_input_not_architecture_decision
  researched_at: 2026-07-10
  call: c-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001
  parent: s-solmax-operating-substrate-service-zone-relationship-architecture-forge-001

  question: |
    How can a new domain/process instantiate the accepted universal kernel and
    reusable service semantics through a process pack without reinventing common
    mechanisms, modifying kernel semantics or freezing a configuration schema,
    implementation, carrier, topology or consumer template?

  ## 1. Scope and preserved locks

  This note preserves the accepted Q1, Q2 and Q3 answers without extending or
  revising them:

  - operating-substrate remains a stable, model-neutral and carrier-neutral
    kernel with pluggable process packs;
  - a process/domain installs or instantiates a pack and does not modify kernel
    semantics;
  - service zones remain semantic responsibility families rather than physical
    modules, agents, services, files, processes or deployment units;
  - atomic responsibility claims retain one primary normative owner;
  - Q3 retains five semantic relationship families and twelve primary kinds:
    invoke, delegate, handoff; query, observe/event, evidence/provenance;
    propose, validate, decide/authorize, apply/effect; return/result; continue;
  - every open obligation has one primary current next-action owner;
  - delegation retains parent integration/accountability and handoff transfers
    active ownership only after acceptance;
  - capability does not imply permission, authority or approval;
  - proposal, validation, authorization and apply remain semantically
    distinguishable;
  - one primary normative state owner establishes each accepted durable version
    of a mutable-state boundary;
  - portable continuation is mandatory while its exact entity, fields,
    serialization and carrier remain open;
  - durable mutation crosses a logical validated writer/apply boundary while
    its physical topology remains open;
  - no final service-zone or service-block list is accepted.

  This note does not:

  - approve or draft the Q4 architecture card;
  - define actual Health, Zaratusta, game or Direction OS process packs;
  - define a pack manifest, configuration language, entity model, packet,
    message, continuation or migration schema;
  - define field names, identifiers, version syntax or compatibility
    expressions;
  - select a repository, registry, storage engine, runtime, framework,
    resolver, provider, transport, orchestration topology or deployment;
  - freeze a final reusable-service catalogue;
  - make OSGi bundles, Terraform modules, Helm charts, OPA bundles, VS Code
    extensions, Temporal deployments or Kubernetes resources universal
    substrate entities;
  - treat current Zaratusta or Direction OS artifacts as authority;
  - promise universal transactionality or rollback for external effects;
  - implement or change Direction OS.

  ## 2. Bounded answer

  The primary-source comparison supports the following bounded Q4 orientation:

  A process pack should be evaluated as a process-owned semantic definition that
  is admitted into an unchanged kernel through a staged lifecycle.

  Instantiation is not merely:

  - copying a template;
  - filling configuration values;
  - merging overlays;
  - downloading an extension;
  - resolving a package version;
  - binding a model or tool;
  - starting a runtime object.

  At the semantic level, instantiation must establish:

  1. which kernel guarantees are inherited and cannot be weakened;
  2. which varying claims are normatively owned by the process pack;
  3. which owner-wide inputs are supplied from an owner profile rather than
     copied into the pack;
  4. which reusable semantic capabilities are required or optional;
  5. which concrete adapters currently satisfy those capabilities;
  6. whether all atomic ownership, authority, state, effect, result and
     continuation claims are coherent;
  7. whether the candidate definition is compatible with the kernel, bound
     services, adapters, existing durable state, open obligations and portable
     continuations;
  8. what would change if the candidate were activated;
  9. which activation, migration, replacement or removal effects require
     authority;
  10. whether validation and process-specific conformance evidence are
      sufficient;
  11. which definition is authoritative for each affected new or open
      obligation after activation;
  12. what recovery and continuation disposition applies if admission,
      migration, activation or removal fails.

  These are semantic obligations, not mandatory configuration fields or a fixed
  lifecycle enum.

  Recommended Q4 research synthesis:

  - use staged semantic admission and activation as the backbone;
  - compose inherited, process-owned, owner-owned and implementation-owned
    claims by normative ownership rather than generic last-write-wins
    precedence;
  - use capability requirement/resolution for reusable-service and adapter
    binding;
  - keep the currently accepted effective definition authoritative until a
    successor has passed the required admission and activation boundary;
  - treat migration, replacement and removal as governed effects over durable
    work, not as package-manager housekeeping;
  - give every open obligation and continuation an explicit compatibility
    disposition instead of forcing all work onto the newest pack;
  - preserve failed, partial and outcome-unknown distinctions rather than
    claiming universal rollback.

  This synthesis is a candidate forge direction, not accepted architecture.

  ## 3. Working terms

  These are research terms for evaluating Q4. They are not accepted entity or
  schema names.

  ### 3.1 Pack definition

  The process-owned semantic definition that states legitimate domain/process
  variation while inheriting kernel semantics.

  It may define process-specific procedures, routing, vocabulary, policy,
  capability needs, evidence expectations and conformance scenarios. This
  statement does not prescribe a manifest format or object model.

  ### 3.2 Available pack

  A pack definition that can be located or supplied to an environment.

  Availability does not establish:

  - validity;
  - compatibility;
  - capability resolution;
  - authority;
  - activation;
  - suitability for existing work.

  ### 3.3 Admission

  The semantic assessment that a candidate pack composition is sufficiently
  valid, compatible, satisfiable and policy-coherent to become eligible for
  activation in a bounded scope.

  Admission does not itself activate or mutate authoritative state.

  ### 3.4 Binding

  The association of an abstract semantic requirement with a compatible
  reusable-service or adapter implementation.

  A binding supplies capability. It does not silently grant authority or become
  the normative owner of process policy.

  ### 3.5 Effective definition

  The unambiguous accepted combination of inherited kernel semantics,
  process-owned declarations, approved owner-profile inputs and compatible
  service/adapter bindings governing a bounded process scope or obligation.

  This does not require one physical file, process, service or package.

  ### 3.6 Activation

  The governed apply/effect transition that makes an admitted effective
  definition authoritative for the stated scope or work population.

  Activation is therefore distinct from availability, validation and owner
  approval.

  ### 3.7 Degraded route

  A pack-declared legitimate mode in which an optional capability is absent or
  reduced while all kernel invariants and the pack's remaining safety and result
  obligations still hold.

  Silent omission, improvised fallback or authority expansion is not a
  legitimate degraded route.

  ### 3.8 Compatibility disposition

  An explicit conclusion for a pack, binding, durable state boundary, open
  obligation or continuation:

  - compatible as-is;
  - compatible under bounded revalidation;
  - pinned to an existing definition while draining;
  - explicitly migratable;
  - replaceable through a governed mapping/handoff;
  - incompatible and rejected;
  - unresolved and requiring a named resolution owner.

  Exact labels and representation remain downstream.

  ### 3.9 Migration

  A governed transition that preserves, transforms or rebinds accepted durable
  meaning when a process definition or binding changes.

  Migration is not merely copying data. It must preserve or explicitly settle
  identity, ownership, authority, accepted decisions, effect certainty,
  evidence, open obligations and continuation.

  ### 3.10 Drain

  Continued support for existing work under its accepted definition while new
  work is prevented from entering that definition and the remaining obligations
  are completed, migrated, handed off or explicitly closed.

  Drain is a semantic lifecycle option, not a selected deployment mechanism.

  ## 4. Primary-source architecture comparison

  ### 4.1 OSGi Core Release 8 — capability resolution and extension lifecycle

  Primary evidence:

  - OSGi models dependencies through typed requirements and capabilities.
  - A resource provides its intended functionality only when all mandatory
    requirements are satisfied.
  - Resolution creates explicit wiring between matching requirements and
    capabilities.
  - A bundle must be valid before installation.
  - installation is persistent and atomic with respect to framework state:
    either the bundle is completely installed or the framework is left as it
    was;
  - installed, resolved and active are separate lifecycle conditions;
  - a bundle can start only when it can be resolved;
  - update may make a new revision available while an old in-use revision
    remains available until refresh or restart;
  - uninstall may likewise leave in-use old wiring available until it is no
    longer in use.

  Q4 support:

  - pack availability, successful installation, requirement resolution and
    activation should not be collapsed;
  - a missing mandatory capability should prevent activation rather than cause a
    late hidden failure;
  - requirements and providers should be declared and matched without embedding
    one concrete provider in the reusable definition;
  - work already using an old definition can require an explicit drain or
    compatibility route rather than immediate forced replacement;
  - failed installation should leave the previously accepted environment
    intact where no external effects have crossed the installation boundary.

  Q4 limitation:

  - OSGi is a Java module/runtime specification;
  - its Bundle, Namespace, Requirement, Capability, Wire, RESOLVED and ACTIVE
    objects are implementation-specific;
  - atomic framework installation does not establish universal rollback of
    migrations or external effects;
  - its exact resolver and revision mechanics must not become substrate
    architecture.

  Sources:

  - https://docs.osgi.org/specification/osgi.core/8.0.0/framework.module.html
  - https://docs.osgi.org/specification/osgi.core/8.0.0/framework.lifecycle.html

  ### 4.2 Terraform — module declaration, caller binding, validation and plan/apply

  Primary evidence:

  - a module call separates module source and version from module-specific
    inputs and provider mappings;
  - reusable modules declare provider requirements while concrete provider
    configurations are established in the root configuration;
  - provider requirements identify source and acceptable versions; installation
    records the selected versions in a dependency lock;
  - associated provider configuration remains necessary for operations over
    already-created state, including destruction;
  - input validations and preconditions can block a plan before effects;
  - postconditions assess produced state after apply;
  - checks may report warnings without blocking operations;
  - a speculative plan previews proposed change without applying it;
  - final apply must account for changes that may have occurred since an earlier
    plan;
  - moved declarations preserve object identity across refactoring rather than
    treating every address change as destroy/recreate;
  - removing migration declarations can be a breaking change.

  Q4 support:

  - a pack should declare abstract requirements while the instantiating
    environment supplies concrete bindings;
  - process definition and environment/provider configuration have different
    normative owners;
  - validation occurs at several semantic times: declaration input,
    pre-activation assumptions, post-activation guarantees and ongoing checks;
  - an impact or activation plan should be inspectable before the authoritative
    apply transition;
  - a validation or plan result is neither owner authorization nor evidence
    that activation occurred;
  - definition evolution may need explicit identity-preserving migration
    declarations;
  - bindings needed by existing durable state cannot be removed solely because
    a new definition no longer declares them.

  Q4 limitation:

  - Terraform is a declarative infrastructure system with explicit schemas,
    providers, state and resource addresses;
  - its module blocks, provider blocks, lock files, moved blocks and plan files
    are not universal substrate entities;
  - a failed postcondition does not universally undo earlier applied actions;
  - the research supports semantic stages, not adoption of Terraform syntax or
    execution.

  Sources:

  - https://developer.hashicorp.com/terraform/language/block/module
  - https://developer.hashicorp.com/terraform/language/providers/requirements
  - https://developer.hashicorp.com/terraform/language/modules/develop/providers
  - https://developer.hashicorp.com/terraform/language/validate
  - https://developer.hashicorp.com/terraform/cli/commands/plan
  - https://developer.hashicorp.com/terraform/language/modules/develop/refactoring

  ### 4.3 Helm — packaged defaults, overlays, dependencies and bounded rollback

  Primary evidence:

  - a chart packages metadata, dependencies, default values, templates and
    optional validation material;
  - dependencies can carry version constraints and conditional enablement;
  - consumer-supplied values override chart defaults under documented
    precedence;
  - install and upgrade support dry-run and validation controls;
  - install can request rollback/uninstall after a failure;
  - upgrade can remove newly created resources on failure and can reuse or reset
    prior values;
  - releases retain revision history and can be rolled back to an earlier
    revision;
  - uninstall can preserve release history;
  - chart-defined tests check an installed release;
  - hook-created resources are not necessarily tracked or managed as part of the
    corresponding release and cannot be assumed to disappear on uninstall.

  Q4 support:

  - packs can combine reusable defaults with local inputs without copying an
    entire consumer;
  - dependencies, optional features and pack-specific conformance checks are
    legitimate declaration concerns;
  - admission should support preview and testing before authoritative use;
  - replacement/removal needs history and explicit cleanup disposition;
  - rollback must be bounded by what the activation mechanism actually owns.

  Q4 limitation:

  - generic override precedence can hide normative conflict;
  - last-value-wins is unsafe for kernel invariants, authority, state ownership
    and effect policy;
  - a platform rollback flag does not prove rollback of hook-created or external
    effects;
  - Chart, values files, templates, release revisions and Kubernetes resources
    are implementation-specific.

  Sources:

  - https://helm.sh/docs/topics/charts/
  - https://helm.sh/docs/helm/helm_install/
  - https://helm.sh/docs/helm/helm_upgrade/
  - https://helm.sh/docs/helm/helm_rollback/
  - https://helm.sh/docs/helm/helm_uninstall/
  - https://helm.sh/docs/topics/chart_tests/
  - https://helm.sh/docs/topics/charts_hooks/

  ### 4.4 Open Policy Agent bundles — ownership scope and last-known-good activation

  Primary evidence:

  - policy and data can be loaded and updated through bundles;
  - bundle manifests can declare owned roots;
  - OPA validates that roots within a bundle do not overlap and that included
    policy/data remains inside the declared roots;
  - bundle validation failures are reported rather than accepted;
  - signed bundles are activated only after verification succeeds;
  - if verification fails, OPA continues using the existing bundle and reports
    activation failure;
  - activated bundles can optionally be persisted for best-effort recovery;
  - multiple independent bundle sources have no guaranteed load order;
  - conflicting bundles can place OPA into an error state;
  - bundle revision and language-version metadata support evolution.

  Q4 support:

  - composition should be scoped by normative ownership rather than unrestricted
    overlay;
  - a candidate definition should not replace the currently accepted definition
    until verification and admission succeed;
  - conflicting ownership claims should be rejected rather than resolved by
    arrival order;
  - last-known-good activation is safer than destructive replacement;
  - integrity/provenance validation is separate from semantic compatibility.

  Q4 limitation:

  - OPA manages policy and data, not complete process obligations, owner
    authority or continuation;
  - its roots, Rego versions, signatures, ETags and bundle file format are not
    universal substrate entities;
  - best-effort persisted recovery is weaker than the accepted portable
    continuation requirement;
  - OPA itself demonstrates that multi-source overlay without a deterministic
    ownership model is unsafe.

  Source:

  - https://www.openpolicyagent.org/docs/management-bundles

  ### 4.5 Visual Studio Code extensions — dependency versus convenience pack and host compatibility

  Primary evidence:

  - an extension manifest declares host compatibility, dependencies, activation
    conditions, execution placement and bounded capabilities;
  - an extension pack groups extensions for installation convenience;
  - an extension pack should not be confused with a functional dependency;
  - actual dependencies are declared separately;
  - compatibility with the host API is checked through the supported engine
    range;
  - uninstall hooks occur only after complete uninstall and restart;
  - deprecating an extension does not automatically migrate or uninstall
    already-installed copies;
  - a replacement can be offered explicitly through a migration route;
  - removing a published version has irreversible consequences.

  Q4 support:

  - a reusable service collection or suggested pack is not equivalent to a
    mandatory semantic dependency;
  - host/kernel compatibility should be checked before activation;
  - activation conditions can differ from installation availability;
  - deprecation, replacement and removal require explicit lifecycle treatment;
  - source disappearance or deprecation does not establish that existing
    instances and open work are safely migrated.

  Q4 limitation:

  - VS Code concerns an interactive application extension host;
  - it does not define durable process state, Q3 obligation ownership or
    carrier-neutral continuation;
  - extension manifest fields, activation events and host-process placement are
    implementation details.

  Sources:

  - https://code.visualstudio.com/api/references/extension-manifest
  - https://code.visualstudio.com/api/working-with-extensions/publishing-extension

  ### 4.6 Temporal — long-lived definition evolution, pinning and draining

  Primary evidence:

  - workflow definition and workflow execution are distinct;
  - running workflow histories must remain compatible with the code that
    interprets them;
  - incompatible definition changes can fail replay;
  - workflow types can use pinned or auto-upgrade versioning behavior;
  - pinned work stays on one deployment version unless explicitly moved;
  - auto-upgrade work must remain replay-compatible through governed patching;
  - new versions can be staged, ramped and rolled back;
  - old versions may remain active for pinned work and transition through
    draining and drained conditions;
  - child, retry and continue-as-new behavior across versions is explicit rather
    than assumed.

  Q4 support:

  - compatibility belongs to each open obligation or continuation, not only to
    the latest global pack version;
  - pack upgrade can assign new work to a successor while old work remains
    pinned and drains;
  - forced latest-version execution is not a safe universal rule;
  - definition identity and compatibility disposition belong in portable
    continuation semantics;
  - rollout and rollback should be staged and observable;
  - explicit migration or patching is needed when semantics change.

  Q4 limitation:

  - deterministic replay, Worker Deployments, Build IDs and specific versioning
    behaviors are Temporal implementation concepts;
  - arbitrary LLM reasoning cannot be assumed to replay deterministically;
  - the substrate needs compatible continuation and recoverability, not
    Temporal's runtime topology.

  Sources:

  - https://docs.temporal.io/worker-versioning
  - https://docs.temporal.io/workflow-definition
  - https://docs.temporal.io/production-deployment/worker-deployments/worker-versioning

  ### 4.7 Kubernetes CustomResourceDefinition versioning — coexistence, conversion and safe removal

  Primary evidence:

  - several API versions can be served while one version is used for storage;
  - old and new clients can coexist during incremental migration;
  - representations that differ require explicit conversion;
  - stored objects must be migrated to the new storage version;
  - an old served version should not be removed until clients have migrated and
    stored objects no longer depend on it;
  - failed conversion causes the affected operation to fail rather than silently
    reinterpret state;
  - stored-version evidence tracks whether an old representation remains in use.

  Q4 support:

  - compatibility is not one version-number comparison;
  - accepted durable state, active consumers and representation/definition
    interpretation can evolve on different schedules;
  - old support should remain while open users or stored state still require it;
  - removal needs evidence that consumers and durable state have migrated;
  - conversion/migration failure must be explicit and must not silently alter
    meaning.

  Q4 limitation:

  - Kubernetes defines API and stored-object versioning, not AI-process packs;
  - served/storage flags, CRDs and conversion webhooks are implementation
    mechanisms;
  - the source supports coexistence and migration principles, not a substrate
    schema.

  Source:

  - https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/

  ## 5. Comparative findings

  ### 5.1 Definition is not instance or execution

  All compared systems separate, in some form:

  - an extension/module/policy/workflow definition;
  - the environment in which it is admitted;
  - concrete dependencies or providers;
  - an installed or available revision;
  - an activated instance or running execution;
  - durable state created under that definition.

  Q4 implication:

  A process pack should not become identical to one current runtime object,
  session, repository checkout or configuration document.

  ### 5.2 Inherited host guarantees and local declarations are different

  Extension systems rely on host semantics that extensions may use but not
  redefine. Modules and policies then declare legitimate local variation.

  Q4 implication:

  Kernel semantics are inherited and non-overridable. A pack may declare domain
  behavior only at accepted extension points. A declaration attempting to make
  event equal command, capability equal authority, proposal equal apply, or
  transcript equal continuation is invalid rather than an alternative policy.

  ### 5.3 Requirements and concrete providers should be separate

  OSGi requirements/capabilities and Terraform provider requirements/configuration
  both separate what is needed from which concrete implementation supplies it.

  Q4 implication:

  A pack declares required semantic capabilities. Reusable services or adapters
  supply compatible implementations. The pack must not embed one provider as
  the meaning of the capability.

  ### 5.4 Installation, resolution, validation and activation are non-equivalent

  Sources repeatedly distinguish package availability, dependency resolution,
  validation, preview, application and runtime activation.

  Q4 implication:

  Successful download or parsing is not evidence that a pack is valid,
  compatible, authorized or active.

  ### 5.5 Mandatory absence and optional absence need different dispositions

  OSGi blocks resolution when mandatory requirements are unsatisfied. Other
  systems allow conditional or optional features.

  Q4 implication:

  - missing mandatory capability: no activation;
  - missing optional capability: only an explicit pack-declared degraded route;
  - if absence breaks a kernel invariant, declared safety obligation or result
    contract, the capability is not semantically optional.

  ### 5.6 Ownership-scoped composition is safer than generic precedence

  Helm demonstrates useful defaults and overlays. OPA demonstrates the failure
  risk of unordered or overlapping ownership.

  Q4 implication:

  Composition should not use a universal "last value wins" rule. Each atomic
  claim should be accepted from its primary normative owner:

  - kernel owns universal semantics;
  - pack owns domain/process variation;
  - owner profile owns approved owner-wide preferences and context;
  - reusable services own their abstract service outcome contract;
  - adapters own concrete implementation capability facts and receipts.

  A conflicting claim from a non-owner is rejected or routed to explicit
  resolution.

  ### 5.7 Last-known-good should survive a failed candidate

  OPA retains the existing bundle when a new signed bundle fails verification.
  OSGi installation is atomic within framework state.

  Q4 implication:

  A candidate pack should not become authoritative merely because installation
  began. Failed admission should normally leave the current accepted definition
  in force.

  If migration or an external effect has already crossed the apply boundary,
  however, the outcome may be partial or unknown and requires reconciliation;
  it cannot be described as unchanged without evidence.

  ### 5.8 Compatibility is multi-dimensional

  A version identity is necessary for provenance but insufficient for safe
  continuation.

  Compatibility can concern:

  - kernel semantic contract;
  - process-pack definition lineage;
  - local procedure and policy meaning;
  - reusable-service contract;
  - adapter capability;
  - durable state interpretation;
  - open obligation lifecycle;
  - pending authority decisions;
  - external effect certainty;
  - continuation import/resume;
  - migration/removal behavior.

  Exact representation and version rules remain Q11/Q12 work.

  ### 5.9 Long-lived work needs per-obligation disposition

  OSGi retains old in-use wiring, Temporal pins or drains work, and Kubernetes
  supports old and new consumers during migration.

  Q4 implication:

  An upgrade need not choose between "everything remains old" and "everything
  instantly becomes latest." Each affected open obligation can:

  - continue under a compatible new definition;
  - be explicitly revalidated and migrated;
  - remain pinned while draining;
  - be handed off or closed;
  - be rejected as incompatible with a named resolution owner.

  ### 5.10 Removal is governed closure, not file deletion

  Existing durable state, provider dependencies, installed consumers and open
  workflows can outlive source or package removal.

  Q4 implication:

  Removal/replacement must settle:

  - open obligations and their owners;
  - accepted state interpretation;
  - pending owner decisions and authority;
  - applied, partial or unknown effects;
  - evidence and history retention;
  - continuation compatibility;
  - any surviving dependency on the old binding.

  ### 5.11 Rollback has an ownership boundary

  OSGi can restore framework state after failed installation; Helm can roll back
  managed release resources; Terraform can preview before apply. Helm hooks and
  post-apply conditions demonstrate that some effects can escape a nominal
  release rollback.

  Q4 implication:

  The kernel should require truthful effect certainty and recovery semantics,
  not promise that every pack lifecycle action is transactionally reversible.

  ### 5.12 Pack-specific conformance scenarios are part of admissibility

  Helm chart tests, Terraform validations and OPA bundle validation demonstrate
  that packaged behavior can carry checks explaining what correct use means.

  Q4 implication:

  A pack should contribute domain/process-specific conformance scenarios and
  evidence expectations, while kernel conformance remains inherited and cannot
  be replaced by pack tests.

  ## 6. Five responsibility and binding layers

  ### A. Kernel-inherited semantics

  Normative owner:

  - universal kernel.

  Instantiation behavior:

  - inherited automatically;
  - not copied into every pack as if locally authored;
  - not disabled, weakened or redefined by pack, owner profile, service or
    adapter;
  - checked for conformance at admission and activation.

  Includes the accepted semantics for:

  - bounded work and run lifecycle;
  - invoke, delegate, handoff, query, observe/event, evidence, propose,
    validate, decide/authorize, apply/effect, return/result and continue;
  - one current owner per open obligation;
  - retained parent accountability under delegation;
  - accepted ownership transfer under handoff;
  - one normative state owner per mutable boundary;
  - capability/permission/authority separation;
  - controlled durable mutation;
  - effect certainty, recovery and evidence;
  - portable continuation;
  - governed definition evolution.

  This is not a final physical service list.

  ### B. Reusable-service bindings

  Normative owner:

  - the service contract owns the reusable semantic outcome;
  - the pack owns whether and under what conditions that outcome is needed;
  - the environment owns the selected compatible implementation binding.

  Candidate examples for evaluation only, not a frozen list:

  - continuation materialization or validation;
  - provenance/evidence processing;
  - policy evaluation or approval coordination;
  - durable-state/checkpoint support;
  - retrieval or source discovery;
  - routing assistance;
  - compatibility/migration validation;
  - trace or evaluation export.

  Instantiation must determine:

  - the required semantic capability;
  - whether it is mandatory or optional for this pack;
  - compatible provider/binding availability;
  - bounded authority and data access;
  - failure and recovery meaning;
  - legitimate degraded behavior;
  - replacement/rebinding compatibility.

  A service binding must not become process-policy authority merely because it
  supplies capability.

  ### C. Required process-pack declarations

  Normative owner:

  - the process/domain pack.

  Likely semantic declaration concerns:

  - process objective and applicability;
  - procedures and routing policy;
  - domain vocabulary and local role meanings;
  - process-local state, memory, source and evidence distinctions;
  - result and evidence sufficiency;
  - domain-specific effect and safety policy;
  - local delegation and escalation policy;
  - budget, stop and failure criteria;
  - required and optional semantic capabilities;
  - legitimate degraded routes;
  - process-definition compatibility and migration obligations;
  - replacement/removal obligations;
  - process-specific conformance scenarios.

  These are concern categories, not required manifest sections or fields.

  A pack must not:

  - redefine kernel relationship semantics;
  - claim owner-wide facts as process truth without provenance;
  - bind itself irreversibly to one provider as its semantic meaning;
  - grant authority merely by declaring capability;
  - treat a local artifact or configuration as proof of live usefulness.

  ### D. Owner-profile inputs

  Normative owner:

  - the owner or owner-authorized profile responsibility.

  Candidate concerns:

  - language and presentation preferences;
  - initiative/ask/proceed preferences;
  - privacy and sharing defaults;
  - owner-wide approval preferences;
  - approved shared constraints and context;
  - explanation and decision style.

  Instantiation must:

  - import only approved and relevant owner-wide inputs;
  - retain provenance and sharing boundaries;
  - distinguish owner preference from process policy;
  - detect conflict with mandatory domain safety or effect policy;
  - avoid promoting one process's local assumption into the owner profile;
  - avoid using a preference to weaken a kernel invariant.

  Exact owner-profile content and schema remain Q5/Q10 work.

  ### E. Adapter and implementation bindings

  Normative owner:

  - the implementation environment for capability facts;
  - the relevant pack/kernel owner for allowed use and authority.

  Candidate implementation categories:

  - model or agent runtime;
  - tool or external service;
  - store or repository;
  - transport or communication binding;
  - user interface;
  - validator, evaluator or telemetry backend;
  - scheduler or orchestration runtime;
  - credential and authentication mechanism.

  Instantiation must establish:

  - what capability is actually supplied;
  - compatibility with the required semantic contract;
  - current availability and limits;
  - authority and credential scope;
  - retry/effect behavior;
  - evidence and receipts;
  - substitution or recovery route.

  Concrete runtime identifiers and implementation objects may appear as
  references but do not define process identity or portable continuation.

  ## 7. What one instantiation must establish semantically

  Without specifying configuration fields, a conforming instantiation should
  make the following questions answerable.

  ### 7.1 Identity and scope

  - Which process-pack definition and lineage are being considered?
  - Is this a new instantiation, upgrade, rebind, recovery, replacement or
    removal?
  - Which process scope, new obligations, open obligations and durable state
    boundaries are affected?
  - Which currently accepted definition remains authoritative before
    activation?

  ### 7.2 Inheritance

  - Which kernel contract is inherited?
  - Does any candidate claim attempt to override a kernel invariant?
  - Are all Q3 relationship, ownership, authority, result and continuation
    meanings preserved?

  ### 7.3 Local declaration ownership

  - Which varying claims are process-owned?
  - Are state, evidence, effect, safety and result responsibilities assigned to
    unambiguous normative owners?
  - Does the pack remain within the process/domain boundary rather than
    redefining owner-wide or implementation concerns?

  ### 7.4 Owner-profile projection

  - Which approved owner-wide inputs are relevant?
  - What may be shared into this process?
  - Which owner preferences are subordinate to mandatory process safety or
    authority requirements?
  - Has any local fact been incorrectly promoted to owner-wide authority?

  ### 7.5 Capability requirements

  - What semantic capabilities are mandatory?
  - What capabilities are optional?
  - For every optional capability, what legitimate degraded route exists?
  - Would absence break a kernel invariant, safety rule or result contract?

  ### 7.6 Binding resolution

  - Which reusable service or adapter supplies each capability?
  - Is the binding semantically and version compatible?
  - Does it have sufficient but not excessive authority and context?
  - Can it return evidence, failure and recovery dispositions required by the
    contract?
  - Is substitution possible without changing process meaning?

  ### 7.7 Composition and conflict

  - Which normative owner supplies each atomic effective claim?
  - Are two layers attempting to own the same claim incompatibly?
  - Are ambiguous precedence, duplicate state ownership or authority expansion
    rejected?
  - Can the effective composition be explained without relying on merge order?

  ### 7.8 Validation and proof

  - Is the candidate complete and internally coherent?
  - Are mandatory capabilities resolvable?
  - Are ownership and authority chains closed?
  - Are state mutation and external effect paths governed?
  - Can result and portable continuation obligations be fulfilled?
  - Is existing state/open work compatible or explicitly migratable?
  - Do pack-specific conformance scenarios pass?
  - What evidence supports the verdict and what remains uncertain?

  ### 7.9 Impact and authority

  - What authoritative definition, durable state, open work, privacy scope,
    external effect or approval policy would change?
  - Is owner/human authorization required for that bounded change?
  - Is any prior authorization stale because target, evidence, policy or state
    changed?
  - Does authorization bind to the exact proposed lifecycle action?

  Exact authorization thresholds remain Q10.

  ### 7.10 Activation and closure

  - What admitted candidate is being made authoritative?
  - Which obligations use the new definition and which remain pinned or
    unresolved?
  - Did activation apply, fail-known-not-done, become partial or remain
    outcome-unknown?
  - What definition is authoritative after the attempt?
  - Who owns recovery, migration or remaining work?
  - What result and portable continuation are returned?

  ## 8. Candidate scenario grammar for Q4 forge

  This sequence is a scenario grammar, not a mandatory state enum, message
  sequence or physical topology. One implementation may combine phases, but
  conformance must preserve their semantic distinctions.

  ### Phase 1 — Propose a bounded lifecycle action

  The current work owner proposes:

  - new instantiation;
  - upgrade;
  - service/adapter rebind;
  - recovery;
  - replacement;
  - or removal.

  The proposal identifies the affected scope and intended outcome.

  No pack becomes authoritative at this phase.

  ### Phase 2 — Establish the current accepted basis

  Determine:

  - the current effective definition;
  - open obligations and current owners;
  - accepted durable state and evidence;
  - pending decisions and authority bounds;
  - applied, partial or unknown effect status;
  - relevant continuations and compatibility claims.

  Absence of an old source repository does not erase this accepted basis.

  ### Phase 3 — Inherit kernel semantics

  Attach the unchanged kernel contract.

  Reject any candidate declaration that attempts to redefine or disable the
  inherited semantics.

  ### Phase 4 — Interpret process-owned declarations

  Establish the candidate process-specific meaning:

  - procedures and routing;
  - domain policy;
  - required outcomes and evidence;
  - capability requirements;
  - degraded routes;
  - compatibility, migration and removal obligations;
  - process-specific conformance scenarios.

  Exact declaration representation remains open.

  ### Phase 5 — Project approved owner-profile inputs

  Supply relevant owner-wide preferences, policy and approved shared context
  under provenance and sharing limits.

  Do not copy unrelated owner information or let an owner preference silently
  override mandatory domain policy.

  ### Phase 6 — Resolve reusable-service and adapter bindings

  Match declared semantic requirements to compatible providers.

  Results can include:

  - resolved;
  - missing mandatory capability;
  - missing optional capability with legitimate degraded route;
  - incompatible provider;
  - unresolved conflict;
  - authority or credential insufficiency.

  Capability resolution does not grant new human authority.

  ### Phase 7 — Compose by normative ownership

  Form the candidate effective definition from:

  - inherited kernel semantics;
  - pack-owned declarations;
  - owner-profile inputs;
  - reusable-service bindings;
  - adapter capability facts.

  Reject:

  - kernel override;
  - duplicate primary normative owner;
  - ambiguous state ownership;
  - hidden authority expansion;
  - unsafe last-write-wins conflict;
  - provider-specific semantics masquerading as process meaning.

  ### Phase 8 — Validate and produce an impact disposition

  Validate:

  - integrity and provenance;
  - kernel conformance;
  - declaration coherence;
  - capability satisfiability;
  - ownership and authority closure;
  - effect/recovery behavior;
  - current-state preconditions;
  - open-work and continuation compatibility;
  - migration/removal feasibility;
  - pack-specific conformance scenarios.

  Produce a bounded impact disposition:

  - what would become authoritative;
  - what work would migrate, pin, drain, hand off or reject;
  - what durable state or effects may change;
  - what evidence and uncertainty remain.

  Validation is not authorization or activation.

  ### Phase 9 — Decide or authorize where required

  Route only the bounded authority questions that truly require owner/human
  decision.

  Potential examples:

  - broader external-effect authority;
  - changed privacy or sharing boundary;
  - irreversible migration/removal;
  - changed approval threshold;
  - acceptance of a material compatibility gap.

  Exact gate categories and thresholds remain Q10.

  ### Phase 10 — Stage and test without displacing the accepted definition

  Prepare candidate bindings, migration and conformance checks while the current
  accepted definition remains authoritative.

  Staging may discover:

  - missing capability;
  - invalid data interpretation;
  - incompatible continuation;
  - failed test;
  - external dependency failure;
  - partial preparatory effect.

  Any preparatory effect must retain Q3 effect-certainty semantics.

  ### Phase 11 — Activate through the governed apply boundary

  Apply the admitted and, where required, authorized effective definition to the
  stated scope.

  After activation, every affected open or new obligation must have an
  unambiguous definition and current owner.

  Permitted dispositions include:

  - new definition active for the scope;
  - new work on the successor while old work drains;
  - selected obligations migrated;
  - selected obligations pinned;
  - rejected or unresolved obligations with named resolution owners.

  This does not require a single physical orchestrator or store.

  ### Phase 12 — Verify, return and continue

  Return an authoritative lifecycle result stating:

  - whether admission and activation succeeded;
  - which definition is authoritative;
  - which capabilities and bindings are effective;
  - what was migrated, pinned, drained or rejected;
  - effect certainty;
  - evidence and limitations;
  - open obligations and current owners;
  - next legitimate action;
  - continuation disposition.

  Exact result or continuation fields remain Q9/Q12.

  ### Phase 13 — Operate and observe

  During operation, detect:

  - binding disappearance;
  - compatibility drift;
  - deprecated pack or adapter;
  - stale authority;
  - failed conformance check;
  - new evidence requiring evolution.

  Observation alone does not silently mutate the effective definition.

  ### Phase 14 — Upgrade, rebind, replace or remove through the same grammar

  Every lifecycle change re-enters proposal, validation, authority and apply
  semantics.

  No hidden hot-swap may alter process meaning for open work without a
  compatibility disposition and updated continuation.

  ## 9. Failure, compatibility and removal behavior

  ### 9.1 Missing mandatory capability

  Required disposition:

  - candidate remains unresolved/inactive;
  - current accepted definition remains authoritative if no effect crossed the
    apply boundary;
  - missing semantic requirement is identified;
  - a current resolution owner and permitted routes are named;
  - no provider is silently substituted with broader authority or different
    semantics.

  ### 9.2 Missing optional capability

  Required disposition:

  - use only a pack-declared legitimate degraded route;
  - preserve kernel guarantees and remaining pack obligations;
  - expose changed result quality, evidence limits or unavailable behavior;
  - do not silently reinterpret the capability as unnecessary.

  If no legitimate degraded route exists, treat the capability as mandatory for
  that instantiation.

  ### 9.3 Invalid pack or attempted kernel override

  Required disposition:

  - reject before activation;
  - report the invalid claim and evidence;
  - retain the current accepted definition;
  - do not "best effort" around altered ownership, authority, mutation, result
    or continuation semantics.

  ### 9.4 Conflicting declarations or overlays

  Required disposition:

  - identify the atomic conflicting claims and their asserted normative owners;
  - resolve by accepted ownership or explicit authority decision where
    legitimately allowed;
  - otherwise reject the composition;
  - never use arrival order or generic last-write-wins for safety, authority,
    state ownership or effect claims.

  ### 9.5 Incompatible kernel, pack, service or adapter versions

  Permitted routes:

  - select a compatible binding;
  - keep existing work pinned;
  - explicitly patch or migrate;
  - stage a replacement;
  - reject the candidate.

  Prohibited route:

  - force activation and hope runtime failure reveals incompatibility.

  ### 9.6 Existing open obligations are incompatible

  Each obligation requires one of:

  - compatible resume under the successor;
  - bounded revalidation and migration;
  - continued operation under the old definition while draining;
  - accepted handoff to another compatible process;
  - explicit unresolved closure with a named owner.

  Silent abandonment or ownerless waiting is invalid.

  ### 9.7 Failed validation

  Required disposition:

  - no authorization or activation follows from the failed verdict;
  - return reasons, evidence and possible correction route;
  - current accepted definition remains in force if no earlier effect changed
    it;
  - preserve the candidate as rejected evidence only if retention is justified.

  ### 9.8 Partial installation or staging failure

  Required disposition:

  - distinguish failed-known-not-done, partial effect and outcome-unknown;
  - clean up only effects whose ownership and reversibility are established;
  - reconcile any uncertain external effect before retry;
  - retain causal evidence;
  - name the current recovery owner.

  "Atomic install" must not be reported if the system cannot prove that all
  relevant effects are inside the atomic boundary.

  ### 9.9 Activation failure

  If activation is known not to have applied:

  - retain or restore the previously accepted definition;
  - return rejected/failed-known-not-done.

  If activation may have partially applied:

  - do not report automatic rollback;
  - reconcile authoritative state;
  - identify which obligations and boundaries use which definition;
  - suspend unsafe new work if necessary;
  - return partial or outcome-unknown with a recovery owner and continuation.

  ### 9.10 Migration failure

  Migration is itself a governed mutation.

  Required preservation or settlement concerns:

  - durable identity;
  - current and parent/child ownership;
  - accepted state;
  - decisions and authority;
  - external effect certainty;
  - evidence and provenance;
  - open obligations;
  - next legitimate action;
  - continuation compatibility.

  Recovery may be:

  - resume migration;
  - reconcile state;
  - return to an old compatible definition;
  - compensate an applied effect;
  - pin and drain;
  - escalate a bounded owner decision;
  - close unresolved with a named owner.

  Rollback is only one possible recovery route.

  ### 9.11 Failed rollback or recovery

  Required disposition:

  - preserve the original activation/migration evidence;
  - report the recovery attempt separately;
  - mark remaining state partial or outcome-unknown;
  - prohibit blind repeated rollback;
  - name the next-action owner and continuation.

  ### 9.12 Pack deprecation or source disappearance

  Required disposition:

  - deprecation is observation, not automatic removal;
  - source disappearance does not invalidate accepted durable state by itself;
  - identify open obligations and continuations still depending on the pack;
  - route migration, replacement, pin/drain or explicit risk acceptance;
  - preserve pack identity and provenance sufficient to interpret existing
    work.

  ### 9.13 Pack replacement

  Replacement can cross process-definition lineage and is not assumed to be a
  compatible update.

  It requires:

  - declared mapping of still-legitimate responsibilities;
  - compatibility assessment for durable state and continuation;
  - accepted handoff or migration of open ownership;
  - explicit treatment of changed policy and authority;
  - preservation of history/evidence;
  - governed activation and retirement of the predecessor.

  ### 9.14 Pack removal

  Removal should be blocked while any of these remain unresolved:

  - open obligation without a continuation or successor owner;
  - durable state that cannot be interpreted after removal;
  - pending authorization or effect whose status is not settled;
  - current dependency on an old service/adapter binding;
  - required evidence or audit that would be lost;
  - continuation that names no compatible resume route.

  Safe removal may require:

  - drain;
  - migration;
  - accepted handoff;
  - revocation of pack-specific authority;
  - preservation of evidence and compatibility information;
  - explicit final result and continuation.

  The mechanism is downstream.

  ## 10. Material disagreements and unresolved choices

  ### 10.1 Static versus dynamic binding

  OSGi and Terraform emphasize declared resolution. Agent/tool environments may
  discover capabilities dynamically.

  Q4 implication:

  Dynamic discovery can be allowed, but a binding that changes process meaning,
  authority, effect behavior or continuation compatibility must pass the same
  semantic admission boundary. Runtime fallback must not become hidden policy.

  ### 10.2 Global upgrade versus per-work compatibility

  Some extension hosts emphasize one active host state. Durable workflow and API
  evolution systems preserve old work or clients during migration.

  Q4 implication:

  Q4 should prefer per-obligation compatibility disposition over a universal
  immediate global upgrade rule.

  ### 10.3 Generic overlays versus ownership-scoped composition

  Helm-style overlay precedence is flexible. OPA conflict behavior demonstrates
  that unordered multi-source composition can be unsafe.

  Q4 implication:

  Q4 must choose whether atomic normative ownership is sufficient as the
  composition rule or whether a further bounded precedence model is required.
  It should not freeze an arbitrary merge algorithm.

  ### 10.4 Fail-closed versus degraded operation

  Safety-critical processes may need fail-closed behavior. Creative or
  exploratory processes can remain useful without some optional capabilities.

  Q4 implication:

  Required/optional status and legitimate degraded behavior belong to the
  process pack, constrained by kernel invariants and domain policy.

  ### 10.5 Rollback versus forward recovery

  Package managers often expose rollback. External effects, partial migrations
  and nondeterministic work may make forward reconciliation safer or the only
  truthful route.

  Q4 implication:

  Q4 should require recovery disposition and effect certainty rather than
  universal rollback.

  ### 10.6 One pack versus composed packs

  Sources support extension aggregation, dependencies and bundles, but they do
  not settle whether one substrate process instance can compose several process
  packs as peer definitions.

  Q4 implication:

  Do not freeze pack composition cardinality. Require only that the effective
  definition has unambiguous normative ownership and compatibility.

  This is a downstream Q4/Q11 child question, not a hidden prerequisite.

  ## 11. Process-pressure stress test

  ### 11.1 Health-like safety-critical process

  Pressure characteristics:

  - high consequence of unsupported claims or effects;
  - domain-specific safety/evidence policy;
  - strict provenance and source handling;
  - owner decisions for bounded high-impact effects;
  - long-lived work with potentially stale evidence and approvals;
  - privacy and controlled data sharing.

  Candidate instantiation:

  Kernel-inherited:

  - bounded work and explicit current owner;
  - query/evidence/propose/validate/decide/apply/result/continue distinctions;
  - one normative state owner per mutable boundary;
  - controlled mutation;
  - effect-certainty and recovery;
  - portable continuation.

  Pack-owned:

  - domain vocabulary and applicability;
  - domain procedures and routing;
  - evidence thresholds and source-quality rules;
  - safety and escalation policy;
  - domain effect classes;
  - success, stop and unresolved-result criteria;
  - required capabilities and process-specific proof scenarios.

  Owner-profile input:

  - language and explanation preference;
  - approved privacy/sharing defaults;
  - owner-wide approval preference within applicable domain constraints;
  - approved shared context.

  Reusable-service bindings:

  - only those semantically required by the pack;
  - missing mandatory provenance, validation, controlled-effect or continuation
    capability fails admission;
  - optional capability absence is allowed only under a pack-declared safe
    degraded route.

  Adapter bindings:

  - concrete models, source connectors, stores, interfaces and effect tools;
  - capability and credentials do not create medical or owner authority.

  Upgrade/removal behavior:

  - pending approvals remain bound to their exact proposal and are revalidated
    when stale;
  - open obligations preserve accepted evidence, current owners and effect
    status;
  - incompatible work can remain pinned and drain or undergo explicit
    migration;
  - removal is blocked if care/research obligations or state cannot continue
    legitimately.

  Verdict:

  PASS at the semantic boundary.

  The process requires strict local policy and mandatory capabilities without
  modifying kernel semantics or making Health policy universal.

  ### 11.2 Game/productive-play creative process

  Pressure characteristics:

  - exploratory and branching work;
  - rapid iteration;
  - reversible local changes are common;
  - creative quality is partly subjective;
  - visualization, retrieval or evaluation services may be optional;
  - owner steering may be frequent but high-impact approval gates are rarer.

  Candidate instantiation:

  Kernel-inherited:

  - bounded obligations and explicit ownership;
  - delegation/handoff/result semantics;
  - proposal versus applied durable canon/state change;
  - evidence/provenance where claims or assets depend on sources;
  - portable continuation across carriers.

  Pack-owned:

  - game/productive-play vocabulary;
  - creative procedures and iteration rhythm;
  - local canon, rule and artifact distinctions;
  - playtest/evaluation criteria;
  - routing between exploration, convergence and production;
  - local budgets and stop criteria;
  - optional capability and degraded-mode policy.

  Owner-profile input:

  - preferred explanation and decision style;
  - initiative level;
  - owner-wide privacy and presentation preferences.

  Reusable-service bindings:

  - optional retrieval, visualization or evaluator support may be absent when
    the pack declares a useful degraded route;
  - absence does not authorize fabricated visual evidence or false completion.

  Adapter bindings:

  - concrete creative model, game tool, artifact store or visual interface;
  - no Health-specific evidence gate or medical policy is copied.

  Upgrade/removal behavior:

  - active branches or canon decisions retain ownership and continuation;
  - pack evolution may migrate compatible work or let an old branch drain;
  - irreversible artifact publication or external effect still uses Q3
    authority/apply semantics.

  Verdict:

  PASS at the semantic boundary.

  The same kernel and admission grammar support a lower-stakes, highly
  exploratory process without importing Health policy or modifying kernel
  semantics.

  ### 11.3 Direction-OS-like durable authoring/governance process

  Pressure characteristics:

  - long-lived tasks and accepted architecture decisions;
  - strict writer/apply separation;
  - owner-approved freezes;
  - durable history and continuation;
  - definitions evolve while work remains open.

  Candidate boundary observation:

  - the process pack may own local plays, graph policy and evidence gates;
  - repository and Markdown remain carrier/adapter choices;
  - open owner decisions and pending state changes must survive pack upgrade;
  - removal/replacement is blocked until open obligations and continuation are
    settled;
  - current Direction OS CALL/RESULT names are evidence only and do not become
    universal entities.

  Verdict:

  PASS as an additional pressure probe.

  ### 11.4 Stress-test conclusion

  The candidate boundary supports at least two materially different pressures:

  - strict safety/evidence/effect control;
  - exploratory creative iteration with legitimate optional capabilities.

  It does so without:

  - copying one consumer into another;
  - modifying kernel semantics;
  - requiring one service-block list;
  - selecting a schema, carrier, runtime or topology.

  Therefore the cartography return condition is not triggered.

  ## 12. Candidate Q4 architecture directions

  These are research directions for architecture-forge, not owner-approved
  answers.

  ### Direction A — staged semantic admission and activation

  Core idea:

  Treat process-pack instantiation as a governed sequence:

  - establish current accepted basis;
  - inherit kernel;
  - interpret local declarations;
  - project approved owner inputs;
  - resolve capabilities;
  - compose;
  - validate and assess impact;
  - authorize where required;
  - stage/test;
  - activate;
  - verify/return/continue;
  - evolve or remove through the same boundary.

  Useful because:

  - preserves proposal/validation/authorization/apply distinctions;
  - protects the last accepted definition from invalid candidates;
  - supports failure, partial effects and recovery;
  - gives upgrade/removal explicit treatment;
  - fits Q4's scenario_grammar answer shape;
  - remains implementation-neutral.

  Bad, because:

  - it introduces lifecycle ceremony;
  - if over-specified, it can become a hidden state machine or setup wizard;
  - it must avoid pretending that every external effect is rollbackable.

  ### Direction B — ownership-scoped layered composition

  Core idea:

  Define Q4 primarily as composition of five ownership layers:

  - kernel;
  - reusable services;
  - process pack;
  - owner profile;
  - adapters.

  Resolve every atomic effective claim through its normative owner and reject
  conflicting non-owner overrides.

  Useful because:

  - makes local versus inherited responsibility explicit;
  - avoids duplicating common layers;
  - prevents generic configuration precedence from silently changing authority
    or state ownership;
  - remains flexible across domains.

  Bad, because:

  - composition alone does not establish install, validation, activation,
    migration or removal lifecycle;
  - an insufficiently precise ownership rule could become abstract and hard to
    test;
  - pack composition and cross-layer conflict still need scenarios.

  ### Direction C — capability requirement and negotiated binding graph

  Core idea:

  Define packs through mandatory and optional semantic requirements, then bind
  them to compatible reusable services and adapters.

  Useful because:

  - supports portability and implementation substitution;
  - gives clear missing-capability behavior;
  - separates process meaning from concrete provider;
  - allows materially different processes to reuse the same service semantics.

  Bad, because:

  - a resolver cannot decide domain policy, owner authority, migration or
    effect safety;
  - dynamic rebinding can become hidden runtime magic;
  - capability matching alone does not create a coherent effective process
    definition.

  ## 13. Research recommendation

  Recommend that Q4 architecture-forge evaluate:

  1. Direction A as the primary answer backbone.
  2. Direction B as the composition and conflict rule inside Direction A.
  3. Direction C only as the subordinate service/adapter resolution mechanism.

  In compact form:

  A process pack becomes effective through staged semantic admission and
  activation. The candidate effective definition inherits non-overridable kernel
  semantics, accepts process-, owner- and implementation-owned claims only from
  their normative owners, resolves declared semantic capabilities to compatible
  bindings, validates compatibility and open-work disposition, obtains bounded
  authority where required, and crosses a governed activation boundary. Failed
  candidates do not displace the accepted definition unless an effect has
  already become partial or uncertain; upgrades, replacement and removal
  preserve or explicitly settle open ownership, authority, effects, evidence
  and continuation.

  This recommendation does not freeze:

  - lifecycle status names;
  - a manifest or configuration format;
  - an exact versioning rule;
  - a resolver implementation;
  - physical activation topology;
  - one active-pack cardinality;
  - a reusable-service list;
  - a migration representation;
  - owner-profile fields;
  - any consumer template.

  ## 14. Premature-freeze and failure risks

  Q4 forge should explicitly reject:

  1. Treating a process pack as a copyable consumer template.
  2. Treating configuration merge as the whole instantiation model.
  3. Allowing packs to override kernel semantics.
  4. Making service-zone names into mandatory package/module names.
  5. Making every reusable service mandatory for every process.
  6. Treating every missing optional capability as silent best-effort mode.
  7. Binding process meaning to one current model, runtime, store or tool.
  8. Using generic last-write-wins precedence for authority or state ownership.
  9. Treating successful download or parsing as activation.
  10. Treating validation as authorization.
  11. Treating owner approval as proof that activation succeeded.
  12. Activating an invalid successor after partially displacing the current
      accepted definition.
  13. Forcing all open work onto the newest pack version.
  14. Treating version equality as complete semantic compatibility.
  15. Removing an old pack while open obligations or state still depend on it.
  16. Treating deprecation or source disappearance as automatic uninstall.
  17. Assuming rollback covers external hooks, migrations or effects.
  18. Retrying outcome-unknown activation or migration blindly.
  19. Omitting current owners and pending authority from migration/continuation.
  20. Letting a capability resolver grant broader authority.
  21. Promoting process-local policy or facts into the owner profile.
  22. Treating adapter configuration as process policy.
  23. Freezing OSGi, Terraform, Helm, OPA, VS Code, Temporal or Kubernetes
      object names as substrate entities.
  24. Claiming live process readiness from a valid pack and complete artifacts
      without owner-facing scenario evidence.
  25. Selecting a repository, storage system, runtime, provider or deployment
      while answering Q4.

  ## 15. Evidence confidence and limits

  ### High confidence

  Cross-source support is strong for:

  - separating definition, availability, resolution, validation and activation;
  - separating abstract requirements from concrete provider bindings;
  - blocking activation when mandatory requirements are unsatisfied;
  - distinguishing required dependencies from convenience groupings;
  - validating candidates before they displace the accepted definition;
  - retaining a last-known-good definition on failed admission where no later
    effect has occurred;
  - treating version identity and compatibility as explicit concerns;
  - preserving old support while active consumers/work still depend on it;
  - requiring explicit migration/removal treatment for durable state;
  - separating preview/plan from authoritative apply;
  - limiting rollback claims to the effects actually owned by the mechanism.

  ### Medium-high confidence

  The following are strong architecture synthesis rather than one direct
  standard:

  - staged semantic admission/activation as the Q4 backbone;
  - ownership-scoped composition instead of generic overlay precedence;
  - mandatory/optional semantic capability declarations;
  - explicit pack-declared degraded routes;
  - per-obligation compatibility disposition;
  - keeping the current accepted definition authoritative until successor
    activation;
  - treating pack activation and migration as governed apply/effect relations.

  ### Medium confidence

  The following remain forge/downstream choices:

  - the exact candidate phase granularity;
  - whether one process scope always has one effective pack or can compose peer
    packs;
  - which lifecycle changes require owner authorization;
  - the minimum compatibility evidence for automatic resume under a successor;
  - the exact boundary between reusable-service contracts and adapter
    contracts;
  - whether pack-specific tests are mandatory for all packs or only defined
    classes;
  - how much migration material must be portable rather than referenced.

  ### Evidence limits

  1. No reviewed source defines the whole desired operating-substrate.
  2. OSGi and VS Code are code-extension hosts, not owner-led durable
     AI-process substrates.
  3. Terraform and Helm are declarative infrastructure/package systems with
     explicit schemas and platform-specific apply behavior.
  4. OPA bundles address policy/data distribution, not complete process
     ownership or continuation.
  5. Temporal provides strong long-lived compatibility evidence but assumes a
     durable workflow runtime and replay constraints.
  6. Kubernetes versioning concerns APIs and stored resources, not process packs.
  7. None of the sources defines the accepted Q3 relationship algebra.
  8. None provides a universal owner-profile layer.
  9. None provides full carrier-neutral continuation across models, providers
     and runtimes.
  10. No source proves owner-facing live usefulness from package validity or
      protocol completeness.
  11. "Atomic" and "rollback" are scoped terms; they do not universally cover
      external effects.
  12. The recommendation is cross-source architecture synthesis, not adoption
      of an existing standard.
  13. Current vendor/project documentation can evolve after the 2026-07-10
      observation date.
  14. No actual process pack was implemented or live-tested in this research.

  Evidence that would materially change the recommendation includes:

  - two materially different process pressures that cannot share the proposed
    inherited/declaration/binding/admission boundary;
  - a broadly adopted standard providing portable process definition,
    authority, evidence, state migration and continuation across runtimes;
  - proof that safe dynamic rebinding needs no compatibility or authority
    validation;
  - proof that an invalid successor can safely displace the current accepted
    definition before admission completes;
  - owner-facing trials showing the proposed admission grammar creates more
    reconstruction bureaucracy than it prevents;
  - an accepted Q1/Q2/Q3 revision changing the kernel/pack boundary.

  ## 16. Downstream and child questions

  These questions do not block Q4 forge.

  ### Q4 forge must decide

  - the accepted definition of process-pack instantiation at the semantic level;
  - what is inherited, declared, supplied, bound, validated, authorized and
    activated;
  - the bounded scenario grammar;
  - conflict behavior among kernel, pack, owner-profile and adapter claims;
  - mandatory versus optional capability behavior;
  - failed-candidate and current-accepted-definition behavior;
  - minimum upgrade, migration, replacement and removal obligations;
  - the relationship between activation and Q3 apply/effect semantics.

  ### Existing downstream routes

  - Q5 shared owner context:
    exact owner-profile projection, sharing and promotion/retirement rules.
  - Q6 persistence/history:
    which accepted definitions, migrations and compatibility evidence become
    durable.
  - Q7 routing/procedure:
    exact reusable procedure structure versus pack-owned procedures.
  - Q8 live interface:
    how admission, degraded state, migration and owner decisions are presented
    without bureaucracy.
  - Q9 result/continuation:
    exact semantic minimum for lifecycle result and compatible continuation.
  - Q10 authority/gates:
    which pack lifecycle actions require owner authorization.
  - Q11 evidence/evolution:
    version identity, compatibility, migration, pin/drain, replacement and
    evidence-to-change rules.
  - Q12 communication/entities:
    representation, identity, correlation and binding protocol.
  - Q13 proof:
    conformance scenarios for instantiation and lifecycle failure.
  - Q14 carrier:
    mappings to Markdown, chat, applications, registries and automated
    transports.

  ### Candidate child questions

  1. Can one effective process compose several peer process packs, and if so,
     how is normative ownership kept unambiguous?
  2. What semantic compatibility relation is sufficient for automatic resume
     under a successor pack?
  3. Which capability changes are equivalent rebinding and which require full
     readmission?
  4. What evidence establishes that all old obligations and durable state have
     drained before pack removal?
  5. How are pack lineage, replacement and cross-lineage handoff distinguished?
  6. What is the minimum process-pack conformance evidence required before
     activation?
  7. How are owner-profile changes revalidated against an already active pack?
  8. What is the authoritative current definition when activation outcome is
     unknown?
  9. Which activation/migration effects can be compensated rather than rolled
     back?
  10. How is source disappearance handled when an accepted instance remains
      required for continuation?

  Classification:

  - these are Q4 children or existing Q5/Q9/Q10/Q11/Q12/Q13 downstream
    elaborations;
  - none is a hidden prerequisite for the bounded Q4 architecture decision;
  - no new top-level graph node is required.

  ## 17. Q4 forge handoff

  plain_question: |
    Как новый domain/process instantiates the universal structure without
    reinventing common service layers?

  why_it_matters: |
    If every process reconstructs lifecycle, capability, authority, evidence,
    compatibility and recovery semantics, the substrate fails to provide reuse.
    If the kernel dictates domain policy or one consumer template, it
    overreaches.

  expected_answer_shape: scenario_grammar

  must_decide: |

    - what is inherited and non-overridable;
    - what the pack must declare semantically;
    - what remains owner-profile input;
    - how reusable-service and adapter bindings are resolved;
    - how atomic ownership and conflicts are handled;
    - what validation and impact assessment precede activation;
    - how authorization and activation remain distinct;
    - how missing capabilities and degraded routes behave;
    - how versions, open obligations and continuations are checked;
    - how upgrade, migration, recovery, replacement and removal behave;
    - what result/continuation an instantiation lifecycle action owes.

  must_not_decide: |

    - actual Health, Zaratusta, game or Direction OS pack;
    - manifest/config/entity/message/continuation schema;
    - field names, identifiers or version syntax;
    - final service-zone or service-block list;
    - repository, registry, storage, runtime, provider or framework;
    - resolver algorithm;
    - API, transport, orchestration or deployment topology;
    - owner-profile content;
    - implementation or proof harness.

  candidate_directions: |

    A. Staged semantic admission/activation.
       Bad, because it can become lifecycle bureaucracy or a hidden state
       machine if forge over-specifies it.

    B. Ownership-scoped layered composition.
       Bad, because composition alone does not settle activation, migration,
       failure or removal.

    C. Capability requirement/resolution.
       Bad, because a resolver alone cannot decide policy, authority, open-work
       compatibility or safe activation.

  research_recommendation: |

    Use A as the backbone, B as its normative composition/conflict rule and C
    as its subordinate service/adapter binding mechanism.

  proof_pressure: |

    - Health-like process with mandatory safety/evidence capabilities and stale
      approval risk;
    - game/productive-play process with exploratory branching and legitimate
      optional/degraded capabilities;
    - invalid pack attempting kernel override;
    - missing mandatory capability;
    - conflicting owner-profile/pack claim;
    - failed validation retaining current accepted definition;
    - partial activation or migration;
    - old work pinned/draining during upgrade;
    - incompatible continuation;
    - removal blocked by unresolved obligations or state;
    - owner-facing use that avoids exposing internal setup bureaucracy.

  return_to_graph_if: |

    - the boundary cannot support both strict safety-critical and exploratory
      creative pressures without copying one process into another;
    - pack semantics require modifying the kernel;
    - a final service-block list or implementation must be selected before the
      instantiation rule can be stated;
    - a newly discovered entity is a hard prerequisite rather than a
      downstream identity/schema question.

  ## 18. Graph, gap and route verdict

  hidden_prerequisite: none

  gap_event: none

  top_level_rebalance: not_needed

  return_to_cartography: not_required

  implementation_activation: prohibited

  Why Q4 is ready:

  - Q1 fixes the unchanged kernel and pluggable-pack boundary;
  - Q2 fixes atomic responsibility classification and separates kernel,
    reusable service, pack, owner-profile and adapter concerns;
  - Q3 fixes relationship, ownership, authority, lifecycle, result and
    continuation semantics that instantiation must preserve;
  - primary sources provide convergent evidence for declaration/binding
    separation, staged admission, last-known-good activation, compatibility,
    migration and drain/removal behavior;
  - the candidate boundary passes Health-like and game/productive-play pressure
    tests without kernel modification or consumer copying;
  - unresolved identity, schema, compatibility and gate details fit existing
    downstream nodes.

  Next graph route:

  - one bounded Q4 process-pack instantiation/adaptation architecture-forge;
  - no implementation, repo/carrier selection or final service-block work.

  ## 19. Primary-source register

  1. OSGi Core Release 8 — Module Layer.
     https://docs.osgi.org/specification/osgi.core/8.0.0/framework.module.html

     OSGi Core Release 8 — Life Cycle Layer.
     https://docs.osgi.org/specification/osgi.core/8.0.0/framework.lifecycle.html

  2. HashiCorp Terraform documentation, v1.15.x observed 2026-07-10.

     Module block reference.
     https://developer.hashicorp.com/terraform/language/block/module

     Provider requirements.
     https://developer.hashicorp.com/terraform/language/providers/requirements

     Providers within modules.
     https://developer.hashicorp.com/terraform/language/modules/develop/providers

     Validate configuration.
     https://developer.hashicorp.com/terraform/language/validate

     Terraform plan command.
     https://developer.hashicorp.com/terraform/cli/commands/plan

     Refactor modules.
     https://developer.hashicorp.com/terraform/language/modules/develop/refactoring

  3. Helm documentation, version 4.2.2 observed 2026-07-10.

     Charts.
     https://helm.sh/docs/topics/charts/

     Install.
     https://helm.sh/docs/helm/helm_install/

     Upgrade.
     https://helm.sh/docs/helm/helm_upgrade/

     Rollback.
     https://helm.sh/docs/helm/helm_rollback/

     Uninstall.
     https://helm.sh/docs/helm/helm_uninstall/

     Chart tests.
     https://helm.sh/docs/topics/chart_tests/

     Chart hooks.
     https://helm.sh/docs/topics/charts_hooks/

  4. Open Policy Agent — Bundles, observed 2026-07-10.
     https://www.openpolicyagent.org/docs/management-bundles

  5. Visual Studio Code Extension API, observed 2026-07-10.

     Extension manifest.
     https://code.visualstudio.com/api/references/extension-manifest

     Publishing, compatibility, deprecation and removal.
     https://code.visualstudio.com/api/working-with-extensions/publishing-extension

  6. Temporal Platform documentation, observed 2026-07-10.

     Worker Versioning.
     https://docs.temporal.io/worker-versioning

     Workflow Definition and versioning.
     https://docs.temporal.io/workflow-definition

     Worker Versioning in production.
     https://docs.temporal.io/production-deployment/worker-deployments/worker-versioning

  7. Kubernetes documentation — Versions in CustomResourceDefinitions,
     observed 2026-07-10.
     https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/

  END_OF_FILE: live/solmax/work/operating-substrate-process-pack-instantiation-best-practice-research-001.md

evidence:
  internal_sources_read:
    - os/KERNEL.md
    - os/plays/research.md
    - os/schema/packets.md
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md through END_OF_FILE
    - live/solmax/plays/architecture-forge.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-core-invariant-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-relationship-001.md
    - live/solmax/work/operating-substrate-universal-structure-cartography-001.md
    - live/solmax/work/operating-substrate-kernel-service-zone-best-practice-research-001.md
    - live/solmax/work/operating-substrate-service-zone-relationship-best-practice-research-001.md
    - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md
    - user-provided CALL c-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001

  primary_source_families_compared:
    - OSGi capability resolution and bundle lifecycle
    - Terraform modules, provider binding, validation, plan/apply and refactoring
    - Helm packaged defaults, overlays, dependencies, tests and rollback/removal
    - Open Policy Agent bundle ownership, validation and activation
    - Visual Studio Code extension dependencies, compatibility and deprecation
    - Temporal long-lived workflow definition versioning, pinning and draining
    - Kubernetes multi-version coexistence, conversion and stored-state migration

  load_bearing_findings:
    - availability, installation, resolution, validation and activation are
      non-equivalent;
    - mandatory semantic requirements must resolve before activation;
    - process definitions should declare requirements while concrete
      environments supply compatible bindings;
    - current accepted definitions should survive failed candidate admission;
    - generic overlay precedence is unsafe for normative ownership, authority
      and state/effect claims;
    - version identity is necessary but insufficient for compatibility;
    - existing open work needs pin, drain, migrate, handoff, compatible resume
      or explicit rejection;
    - pack replacement/removal must settle open obligations, durable state,
      authority, effects, evidence and continuation;
    - rollback is bounded by owned effects and cannot be promised universally;
    - pack validity does not prove live owner-facing usefulness.

  done_when_checks:
    1_primary_source_comparison: PASS
    2_five_layer_distinction: PASS
    3_semantic_instantiation_without_schema: PASS
    4_failure_compatibility_migration_removal: PASS
    5_two_materially_different_pressures: PASS
    6_three_directions_tradeoffs_recommendation: PASS
    7_limits_downstream_hidden_prereq_graph_gap: PASS
    8_no_implementation_schema_carrier_topology_or_final_list: PASS

  confidence:
    high:
      - declaration versus concrete binding separation;
      - mandatory resolution before activation;
      - staged validation/admission;
      - last-known-good behavior;
      - explicit compatibility and migration/removal obligations;
      - per-open-work drain/pin pressure;
      - bounded rollback claims.
    medium_high:
      - staged semantic admission/activation as Q4 backbone;
      - ownership-scoped composition;
      - explicit degraded routes;
      - activation as governed apply/effect.
    open:
      - exact phase and entity model;
      - exact compatibility relation;
      - pack-composition cardinality;
      - exact owner authorization thresholds;
      - exact continuation and migration representation;
      - final service-zone list and all implementation choices.

state_changes: |
  No repository files were created or modified by this session.

  Mechanical writer should apply exactly:

  1. Create the Q4 research work artifact.

     Path:
     live/solmax/work/operating-substrate-process-pack-instantiation-best-practice-research-001.md

     Content:
     Copy the complete research note from RESULT.outcome beginning with:

     "# Research note — process-pack instantiation and adaptation semantics"

     and ending with:

     "END_OF_FILE: live/solmax/work/operating-substrate-process-pack-instantiation-best-practice-research-001.md"

  2. Create the ready Q4 architecture-forge CALL.

     Path:
     live/solmax/work/calls/c-solmax-operating-substrate-process-pack-instantiation-architecture-forge-001.md

     Content:
     Copy the complete CALL from RESULT.next beginning with:

     "CALL c-solmax-operating-substrate-process-pack-instantiation-architecture-forge-001"

     and ending with its matching END_OF_FILE marker.

  3. Update live/solmax/NOW.md.

     Change:

     route_status: operating_substrate_q3_relationship_card_accepted_q4_instantiation_research_ready

     To:

     route_status: operating_substrate_q4_instantiation_research_ready_for_forge

     In owner_directive, append this exact checkpoint:

     Q4 process-pack instantiation research checkpoint:
     - Primary-source comparison across OSGi, Terraform, Helm, OPA, VS Code,
       Temporal and Kubernetes is complete.
     - This is research input, not an approved Q4 architecture answer.
     - Research supports staged semantic admission/activation rather than
       treating process-pack instantiation as configuration merge or package
       download.
     - Kernel semantics remain inherited and non-overridable. Pack declarations,
       owner-profile inputs, reusable-service bindings and adapter bindings
       retain separate normative owners.
     - Mandatory semantic capabilities must resolve before activation. Optional
       capabilities may be absent only under an explicit pack-declared degraded
       route that preserves kernel and remaining process obligations.
     - Composition must follow atomic normative ownership and reject ambiguous
       authority/state/effect conflicts rather than generic last-write-wins
       precedence.
     - Validation and impact assessment precede authorization and activation.
       Failed candidates normally leave the current accepted definition in
       force.
     - Open work and continuation require explicit compatible-resume, migration,
       pin/drain, handoff, rejection or unresolved-owner disposition; they must
       not be forced silently onto the newest pack.
     - Pack migration, replacement and removal must preserve or explicitly
       settle ownership, authority, effect certainty, evidence and continuation.
       Universal rollback is not assumed.
     - The candidate boundary passed materially different Health-like and
       game/productive-play pressures without modifying kernel semantics or
       copying one consumer into another.
     - Research recommendation: staged semantic admission/activation as Q4
       backbone, ownership-scoped composition as its conflict rule, and
       capability resolution as its service/adapter submechanism.
     - gap_event: none. Exact schema, identity, compatibility representation,
       carrier, topology, implementation and final service-block list remain
       downstream.
     - Next route is the Q4 process-pack instantiation architecture-forge.

     Keep:

     open_calls: []

     Do not add the ready architecture-forge CALL to open_calls until that
     session actually starts.

     Replace NOW.next with:

     work/calls/c-solmax-operating-substrate-process-pack-instantiation-architecture-forge-001.md

     Append to preserved_evidence:

     - live/solmax/work/operating-substrate-process-pack-instantiation-best-practice-research-001.md
     - live/solmax/history/2026-07-10-s-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001.md
     - live/solmax/work/calls/c-solmax-operating-substrate-process-pack-instantiation-architecture-forge-001.md

     Keep tasks, recurring, decisions and active_bet unchanged.

  4. Append live/solmax/LOG.md:

     2026-07-10 — solmax/g-operating-substrate research: Q4 process-pack
     instantiation primary-source note completed across OSGi, Terraform, Helm,
     OPA, VS Code, Temporal and Kubernetes; staged semantic
     admission/activation, ownership-scoped composition, capability binding,
     compatibility, failure, migration, drain and removal findings derived;
     Health-like and game/productive-play pressure tests pass; gap_event none;
     next Q4 architecture-forge. →
     history/2026-07-10-s-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001.md

  5. Create the history record.

     Path:
     live/solmax/history/2026-07-10-s-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001.md

     Content:
     This complete RESULT, including its final history END_OF_FILE marker.

  6. Do not modify:

     - live/solmax/CHARTER.md
     - live/solmax/TREE.md
     - any accepted Q1, Q2 or Q3 architecture card
     - the accepted cartography graph
     - any Direction OS kernel, play or schema
     - any implementation or product repository
     - any actual Health, Zaratusta, game or Direction OS process pack

captures:
  - Q13 proof should include an invalid pack that attempts to weaken a kernel
    invariant and must be rejected before activation.
  - Q13 proof should include a missing mandatory capability and an optional
    capability with both valid and invalid degraded routes.
  - Q13 proof should include conflicting pack/owner-profile claims where generic
    last-write-wins would expand authority.
  - Q13 proof should include failed successor admission while the current
    accepted definition continues operating.
  - Q13 proof should include partial activation or migration with
    outcome-unknown and reconciliation before retry.
  - Q13 proof should include old work pinned and draining while new work uses a
    successor definition.
  - Q13 proof should include pack removal blocked by an open obligation,
    pending approval or uninterpretable durable state.
  - Q10 should decide which pack activation, migration, privacy, effect-policy
    and removal changes require owner authorization.
  - Q11 should define pack lineage, compatibility disposition, migration,
    pin/drain and replacement semantics.
  - Q9/Q11 should define the minimum continuation information needed to detect
    definition incompatibility after interruption.
  - Q12 should represent requirements, bindings and effective-definition
    provenance without copying one package-manager manifest.
  - Q8/Q13 should reject a valid but owner-hostile instantiation flow that turns
    setup, state and handback mechanics into owner-facing bureaucracy.
  - Peer process-pack composition may require a Q4 child question, but it does
    not currently require a top-level graph node.
  - A formal compatibility algebra may become useful downstream; defining it in
    Q4 would prematurely freeze identity and representation.

decisions_needed: []

play_check:
  - 1 Recite: done — the bounded Q4 question, accepted Q1/Q2/Q3 locks,
    prohibited implementation/schema/carrier choices, requested RESULT shape and
    focused session budget were restated.
  - 2 Investigate: done — every named internal artifact was read through its
    END_OF_FILE marker; seven materially different primary-source architecture
    families were compared across extension lifecycle, modules, overlays,
    capability declarations, validation and long-lived compatibility.
  - 3 Confidence: done — direct cross-source convergence was separated from
    architecture synthesis; counterexamples, rollback limits, material
    disagreements, confidence levels, answer-change conditions and
    premature-freeze risks were recorded.
  - 4 Close: done — the bounded research note, source register, comparative
    findings, five-layer distinction, scenario grammar, failure/compatibility
    matrix, three candidate directions, recommendation, process-pressure tests,
    evidence limits, forge handoff, graph/gap verdict, exact writer
    state_changes and ready Q4 forge CALL are returned.

log: |
  solmax research
  c-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001:
  Q4 primary-source instantiation semantics complete; staged semantic
  admission/activation recommended with ownership-scoped composition and
  capability binding; compatibility, migration, drain/removal and failure
  semantics covered; Health-like and game pressure tests pass; gap_event none;
  return to parent with ready Q4 architecture-forge CALL.

next: |
  return-to-parent s-solmax-operating-substrate-service-zone-relationship-architecture-forge-001

  CALL c-solmax-operating-substrate-process-pack-instantiation-architecture-forge-001
  to: session
  direction: solmax
  play: local/architecture-forge
  node: g-operating-substrate
  goal: |
    One owner-approved Q4 architecture card exists for how a new domain/process
    instantiates the accepted universal kernel and reusable service semantics
    through a process pack, deciding what is inherited, declared, locally
    owned, supplied, bound, validated, versioned, activated and checked without
    freezing a configuration schema, implementation, carrier, topology,
    consumer template or final service-block list.
  context: |
    Read:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - live/solmax/plays/architecture-forge.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-core-invariant-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-relationship-001.md
    - live/solmax/work/operating-substrate-universal-structure-cartography-001.md
    - live/solmax/work/operating-substrate-kernel-service-zone-best-practice-research-001.md
    - live/solmax/work/operating-substrate-service-zone-relationship-best-practice-research-001.md
    - live/solmax/work/operating-substrate-process-pack-instantiation-best-practice-research-001.md
    - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md

    Accepted parent locks:
    - operating-substrate is a stable, model-neutral and carrier-neutral kernel
      with pluggable process packs;
    - a process/domain does not modify kernel semantics;
    - service zones are semantic responsibility families, not physical
      deployment blocks;
    - atomic responsibility claims have one primary normative owner;
    - Q3 freezes five semantic relationship families and twelve primary kinds
      plus shared lifecycle and ownership invariants;
    - every open obligation has one primary current next-action owner;
    - capability does not imply authority;
    - validation, authorization and apply remain distinguishable;
    - portable continuation is mandatory while exact schema remains open;
    - durable mutation crosses a logical validated writer/apply boundary;
    - no final service-block list, implementation or physical topology is
      accepted;
    - Q1, Q2 and Q3 must not be revised by Q4.

    Q4 cartography handoff:
    - plain_question: "Как новый domain/process instantiates the universal
      structure without reinventing common service layers?"
    - why_it_matters: "If every process rewrites the structure, substrate
      fails; if substrate dictates local policy, it overreaches."
    - answer_shape: scenario_grammar
    - must_decide: "What is inherited, declared, locally owned, bound,
      validated, versioned and checked at process-pack instantiation."
    - must_not_decide: "Actual Health/Zaratusta/game configurations,
      config/entity schema, UI, repository, storage, runtime, framework,
      provider or deployment."
    - return_to_graph_if: "A process-pack boundary cannot support at least two
      materially different process pressures without copying one consumer into
      another or modifying kernel semantics."

    Research findings:
    - Instantiation is best evaluated as staged semantic admission and
      activation, not configuration merge or package download.
    - Kernel semantics are inherited and non-overridable.
    - Process-pack declarations, owner-profile inputs, reusable-service
      bindings and adapter bindings have different normative owners.
    - Mandatory semantic capabilities must resolve before activation.
    - Optional capability absence is legitimate only under an explicit
      pack-declared degraded route that preserves kernel and remaining process
      obligations.
    - Composition should follow atomic normative ownership and reject ambiguous
      conflicts rather than generic last-write-wins precedence.
    - Validation and impact assessment are distinct from authorization and
      activation.
    - Failed candidates normally leave the current accepted definition in
      force; partial or unknown effects require reconciliation.
    - Open obligations and continuations require compatible-resume, migration,
      pin/drain, handoff, rejection or named unresolved-owner disposition.
    - Migration, replacement and removal must preserve or settle ownership,
      authority, effect certainty, evidence and continuation.
    - Universal rollback is not supported by the evidence.
    - Health-like and game/productive-play pressures pass without kernel
      modification or consumer copying.
    - Research directions:
      A. staged semantic admission/activation;
      B. ownership-scoped layered composition;
      C. capability requirement/resolution.
    - Research recommendation: A as backbone, B as its composition/conflict
      rule, C as its service/adapter binding submechanism.
    - gap_event from research: none.
  boundaries: |
    Do not revise or reopen Q1, Q2 or Q3.
    Do not define actual Health, Zaratusta, game or Direction OS process packs.
    Do not freeze a final service-zone or service-block list.
    Do not define a manifest, configuration, entity, message, migration or
    continuation schema.
    Do not define field names, identifiers, version syntax or exact lifecycle
    enum.
    Do not select a repository, registry, storage system, runtime, framework,
    provider, transport, resolver, orchestration topology or deployment.
    Do not turn current OSGi, Terraform, Helm, OPA, VS Code, Temporal,
    Kubernetes, Zaratusta or Direction OS names into universal substrate
    entities.
    Do not promise universal transactionality or rollback.
    Do not implement.
    Do not change Direction OS.
    Keep Q5-Q14 questions downstream unless a genuine hidden prerequisite is
    found.
  done_when: |
    One atomic Q4 architecture card is explicitly owner-approved and:

    1. defines process-pack instantiation semantically without defining a
       configuration or packet schema;
    2. distinguishes non-overridable kernel-inherited semantics,
       reusable-service bindings, required process-pack declarations,
       owner-profile inputs and adapter/implementation bindings;
    3. states which varying claims each layer normatively owns and rejects
       ambiguous kernel, authority, state or effect overrides;
    4. freezes a bounded scenario grammar for declaration, resolution,
       composition, validation, impact assessment, authorization where
       required, staging, activation, result and continuation;
    5. distinguishes availability/install, admission/validation and
       authoritative activation;
    6. defines missing mandatory-capability behavior and legitimate optional
       degraded behavior;
    7. preserves capability/permission/authority and
       validation/authorization/apply distinctions;
    8. states how current accepted definitions behave when a candidate is
       invalid, incompatible or fails activation;
    9. covers incompatible versions, open-work compatibility, migration,
       recovery, pin/drain, rebinding, replacement and pack removal;
    10. covers failed-known-not-done, partial and outcome-unknown lifecycle
        effects without claiming universal rollback;
    11. preserves Q3 ownership, authority, effect-certainty, result and
        continuation semantics during every lifecycle action;
    12. demonstrates the boundary against at least one Health-like
        safety-critical pressure and one game/productive-play creative pressure
        without copying one pack into the other or modifying kernel semantics;
    13. records rejected alternatives, evidence limits, child/downstream
        questions, hidden prerequisites, graph verdict and gap_event;
    14. selects no implementation, schema, carrier, provider, topology,
        consumer template or final service-block list.
  return: |
    RESULT with the owner-approved Q4 architecture card, owner choice and
    approval words, rejected alternatives, scenario grammar, process-pressure
    stress test, evidence limits, child/downstream questions, graph/gap verdict,
    exact state_changes and next graph route.
  budget: one focused session
  parent: s-solmax-operating-substrate-service-zone-relationship-architecture-forge-001
  surface: chatgpt

  END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-process-pack-instantiation-architecture-forge-001.md

END_OF_FILE: live/solmax/history/2026-07-10-s-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001.md
