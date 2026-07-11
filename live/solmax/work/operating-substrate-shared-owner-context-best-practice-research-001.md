# Research note — shared owner context across process packs

status: research_input_not_architecture_decision
researched_at: 2026-07-11
call: c-solmax-operating-substrate-shared-owner-context-best-practice-research-001
parent: s-solmax-operating-substrate-process-pack-instantiation-architecture-forge-001

## 1. Question

What may legitimately be supplied as shared owner context across process
packs, what must remain process-local, and what provenance, sharing,
authority, conflict, staleness, promotion, retirement and continuation
semantics are required before one owner-profile boundary can be forged
without defining a schema, repository or actual owner profile?

## 2. Scope and preserved locks

This research preserves Q1-Q4 without revising them:

- operating-substrate remains a stable, model-neutral and carrier-neutral
  kernel with pluggable process packs;
- process packs do not modify kernel semantics;
- atomic responsibility claims have one primary normative owner;
- owner-profile concerns are genuinely owner-wide preferences, policy or
  approved shared context, not every fact concerning the same owner;
- one process's local fact, memory or assumption does not become owner-wide
  truth without an explicit legitimate transition;
- capability, permission, authorization, approval and applied effect remain
  non-equivalent;
- validation, authorization and apply remain distinguishable;
- portable continuation is mandatory while its exact entity model, fields,
  serialization and carrier remain open;
- durable mutation crosses a logical validated writer/apply boundary;
- Q4 staged semantic admission and activation remains frozen;
- Q4 projects only relevant approved owner-profile inputs under provenance,
  privacy and sharing boundaries;
- owner preferences cannot weaken kernel semantics or mandatory domain
  safety/effect policy;
- changed owner-profile input during operation is an observation, not a
  hidden mutation of the effective process definition;
- open work receives explicit compatibility, revalidation, migration,
  pin/drain, handoff, rejection or named-unresolved-owner treatment;
- no final service-block list, implementation, carrier, provider, repository,
  storage system or topology is accepted.

This note does not:

- approve a Q5 architecture answer;
- define an actual owner profile or import any actual owner facts;
- define actual Health, Zaratusta, game or Direction OS policy;
- define profile, claim, consent, message, continuation or storage schemas;
- define field names, identifiers, exact status names, version syntax or
  lifecycle enums;
- select a repository, database, vector store, knowledge graph, identity
  provider, policy engine, privacy technology, runtime, framework, transport,
  model, provider, application or deployment;
- make current vendor, Direction OS or Zaratusta objects universal entities;
- freeze a final owner-context category list;
- implement or change Direction OS.

## 3. Bounded research answer

The primary-source comparison supports the following bounded orientation:

Shared owner context should not be treated as one global data object, one
inherited configuration layer, one universal transcript, or one owner-wide
truth store.

It is better treated semantically as a governed boundary through which:

1. genuinely owner-wide preferences or policies can be established by the
   owner or an explicitly owner-authorized responsibility;

2. source-backed contextual claims can become eligible for bounded
   cross-process projection without changing who asserted the claim or
   pretending that approval proves truth;

3. a process receives only the relevant and currently permitted projection
   needed for its stated purpose;

4. the receiving process separately determines whether the projected
   material is sufficiently current, reliable and applicable to become
   accepted process truth for its obligation;

5. permission to disclose or use context remains distinct from authority to
   perform an action;

6. promotion, correction, dispute, revocation and retirement cross a
   governed mutation boundary rather than occurring through transcript
   accumulation, repeated inference or hidden profile edits;

7. changed context does not silently rewrite active obligations or portable
   continuations.

Compact candidate invariant for Q5 forge:

An owner-wide boundary may make an atomic preference, policy or contextual
claim available for relevant cross-process projection only under explicit
normative ownership, provenance, purpose, privacy/sharing limits, current
status and governed change. Projection does not itself establish truth,
authority, consent for a different purpose or compatibility with active
work.

This is architecture synthesis for Q5 forge, not an accepted card.

## 4. Working semantic distinctions

These distinctions are research terms. They are not mandatory entities,
field names, object types or a final category catalogue.

### 4.1 Owner-wide preference or policy

Meaning:

- a preference, constraint or policy intentionally declared or explicitly
  approved as applicable across more than one process context;
- normatively owned by the owner or an explicitly owner-authorized profile
  responsibility.

It may guide:

- interaction, presentation or explanation behavior;
- general initiative/ask/proceed behavior;
- privacy and sharing defaults;
- owner-wide decision-routing preferences;
- other genuinely cross-process constraints.

It does not:

- create authority for a specific external effect;
- override a kernel invariant;
- weaken mandatory process-pack safety, evidence or effect policy;
- become owner-wide merely because the same pattern was observed repeatedly.

Repeated behavior is evidence for proposing a preference. It is not itself
an owner declaration.

### 4.2 Approved shared context

Meaning:

- a contextual claim, constraint, resource or relationship that has been
  admitted for bounded cross-process availability and projection;
- admission includes a legitimate purpose and sharing boundary.

Normative ownership remains decomposed:

- the original source remains responsible for what it asserted;
- the owner/profile responsibility owns the decision that the claim may be
  made available for defined owner-wide purposes;
- each process pack owns its local applicability, evidence and safety rules;
- the receiving process's accepted-state responsibility determines whether
  the claim is accepted for the current obligation.

Approval therefore changes eligibility for sharing. It does not convert a
third-party or process-originated claim into owner-authored truth.

### 4.3 Process-local state or assumption

Meaning:

- accepted, provisional, disputed or working material scoped to one process,
  obligation, branch or execution context;
- normatively owned by that process's accepted-state boundary.

Examples of concern classes, not personal content:

- process progress and commitments;
- local canon or project facts;
- domain-local observations and evidence conclusions;
- temporary routing assumptions;
- one process's interpretation of owner intent;
- one obligation's pending decision or approval.

Default:

- remains local;
- is not exported merely because it concerns the same owner;
- may only become cross-process material through a separate governed
  promotion transition.

### 4.4 Source claim

Meaning:

- a proposition asserted or observed by a source;
- retains attribution, collection context, time, revision and status
  provenance.

Source integrity or signature verification can establish origin,
tamper-evidence and currency. It does not prove the proposition is true or
sufficient for a receiving process's purpose.

Source claims can be:

- consulted locally;
- admitted for bounded cross-process projection;
- rejected;
- superseded;
- disputed;
- invalidated or retired.

The exact representation remains downstream.

### 4.5 Derived memory

Meaning:

- a summary, inference, preference hypothesis, compression, prediction or
  other material derived from source claims, process state, history or prior
  interaction.

Required discipline:

- retain derivation and upstream dependencies;
- retain uncertainty appropriate to the derivation;
- do not relabel it as a source assertion;
- reassess it when supporting claims change, become stale or are revoked;
- make its inferred status visible to receiving processes.

Derived memory may itself be approved for bounded sharing, but it remains a
derived claim. Promotion must not launder inference into fact.

### 4.6 Authority or consent

Meaning:

- a bounded conclusion permitting disclosure, use, request or action under
  stated purpose, target, scope and conditions.

Authority or consent is not ordinary descriptive context.

Distinctions:

- consent to disclose information is not authority to perform an effect;
- standing process permission is not approval of a specific action;
- authorization for one target or payload does not cover a changed target
  or payload;
- one process's consent does not become owner-wide consent;
- withdrawal or revocation constrains future use but does not retroactively
  assert that earlier processing or an already-applied effect never occurred.

A general owner-wide approval preference may be profile input. A specific
authorization remains bound to its concrete proposal and applicable policy.

### 4.7 Credential or secret

Meaning for this note:

- protected authentication or capability material such as an access token,
  signing key, password, recovery material or other secret-bearing
  credential.

Boundary:

- raw secret material does not belong in ordinary owner context, memory,
  trace, result or portable continuation;
- a process may receive only the capability or minimally necessary
  non-secret facts about availability, scope and current status;
- possession or technical access does not create human authority.

Terminology warning:

W3C "verifiable credential" means a secured bundle of issuer claims and is
not necessarily secret capability material. Q5 must not collapse that
meaning with an account credential or secret.

### 4.8 Accepted process truth

Meaning:

- a receiving process's bounded conclusion that a claim is sufficiently
  supported, current and applicable for a stated process purpose.

It is distinct from:

- availability in owner context;
- permission to disclose;
- source authenticity;
- owner approval to share;
- authority to act.

A claim accepted in one process does not automatically become accepted in
another process with different evidence, safety or freshness requirements.

## 5. Four independent conclusions

A conforming Q5 boundary should preserve four independent questions for each
relevant atomic concern.

### A. Context availability

Question:

- may this concern be located or referenced for potential use by the
  receiving process?

Availability does not establish disclosure permission, truth, relevance or
authority.

### B. Permission to disclose or use

Question:

- may this receiving process obtain or use this concern for this stated
  purpose and under these sharing conditions?

Permission may allow only a subset, abstraction or reference rather than the
full underlying material.

### C. Authority to act

Question:

- may the current identity perform or approve this concrete action against
  this target under current policy?

Descriptive context, technical capability, a credential, owner preference or
prior consent does not answer this question automatically.

### D. Accepted process truth

Question:

- does this process accept the claim as sufficiently reliable, current and
  applicable for the present obligation?

Source verification and owner-wide admission are inputs to this conclusion,
not substitutes for it.

Cross-cutting qualifiers include:

- provenance and derivation;
- relevance and purpose;
- currentness and status;
- sensitivity and sharing limits;
- conflicts and uncertainty;
- dependency by active work.

These are separate semantic conclusions, not four required fields or an
exact state machine.

Consequence examples:

- material can be available but not permitted for this process;
- permitted material can remain unaccepted or disputed;
- accepted context can inform reasoning without authorizing an effect;
- a credential can enable technical access while the requested action
  remains unauthorized;
- revocation of action authority need not make an underlying factual claim
  false;
- correction of a factual claim need not by itself revoke every unrelated
  permission.

## 6. Primary-source architecture comparison

### 6.1 W3C Verifiable Credentials Data Model v2.0 — claims, roles,
verification and selective disclosure [S1]

Primary evidence:

- separates issuer, holder, verifier, subject and claim;
- explicitly states that verifiability does not imply truth of encoded
  claims;
- the verifier applies its own policy before relying on claims;
- supports selective disclosure and claim status/validity;
- warns about correlation, dynamic information and inappropriate use;
- authorization is not supplied merely by carrying a credential.

Q5 support:

- source claim, holder availability and receiving-process acceptance must
  remain distinct;
- integrity/provenance does not create accepted truth;
- shared context should support selective projection rather than disclosure
  of a complete profile;
- highly dynamic claims require use-time currentness evaluation;
- a claim-bearing credential does not itself establish action authority.

Limitation:

- W3C VC defines a credential data model, not an owner-profile boundary,
  process-pack model or carrier-neutral continuation contract.

### 6.2 W3C PROV-DM — attribution, derivation, revision, delegation and
invalidation [S2]

Primary evidence:

- represents attribution of an entity to an agent;
- represents responsibility and delegated activity;
- distinguishes generation, derivation, revision and invalidation;
- permits provenance at different granularities;
- preserves relations between original and derived entities.

Q5 support:

- source and derived memory should preserve lineage;
- correction or retirement should not erase the relation to prior material;
- provenance must identify transformations rather than only the last stored
  value;
- invalidation can be represented without pretending an entity never
  existed.

Limitation:

- PROV-DM describes provenance relations; it does not decide privacy,
  consent, process truth or owner-wide promotion policy.

### 6.3 W3C Bitstring Status List v1.0 — status change and privacy [S3]

Primary evidence:

- distinguishes refresh, revocation, suspension and message-like status
  purposes;
- treats revocation and suspension differently;
- warns that status checking can reveal holder, verifier, time and usage
  relationships;
- promotes privacy-preserving group status mechanisms.

Q5 support:

- "changed", "stale", "suspended", "revoked" and "retired" must not be
  collapsed into one generic absent flag;
- status verification itself crosses a privacy boundary;
- future-use invalidation does not require destruction of provenance.

Limitation:

- the exact status purposes and list representation are credential-specific
  and must not become a substrate lifecycle enum.

### 6.4 GDPR — purpose limitation, minimization, accuracy, storage,
correction and withdrawal [S4]

Primary evidence used as privacy and governance pressure:

- personal data should be collected for specified legitimate purposes;
- processing should be relevant and limited to what is necessary;
- data should be accurate and kept current where needed;
- retention should be bounded by purpose and reviewed;
- inaccurate material can require rectification or restricted use;
- consent can be withdrawn, without retroactively invalidating processing
  that was lawful before withdrawal;
- downstream recipients can need notification of correction, erasure or
  restriction.

Q5 support:

- "same owner" is not a sufficient sharing purpose;
- profile projection should be purpose-bound and minimized;
- correction, restriction and retirement affect dependent consumers;
- consent withdrawal and factual invalidity are different semantics;
- indefinite global accumulation is unsafe.

Limitation:

- GDPR is a jurisdiction-specific legal regime, not a universal substrate
  specification. Q5 should derive general privacy pressures without
  pretending to define legal compliance for every jurisdiction or process.

### 6.5 RFC 9396 — fine-grained authorization [S5]

Primary evidence:

- represents authorization details more precisely than one coarse scope;
- allows a user to grant only a subset of requested access;
- binds authorization requirements to actions, resources and other
  concrete details.

Q5 support:

- owner consent or authority should remain bounded to purpose, action and
  target;
- one broad "owner approved" flag is insufficient;
- disclosure authorization and effect authorization require separate
  interpretation.

Limitation:

- RFC 9396 is an OAuth authorization protocol extension, not a context,
  provenance or memory model.

### 6.6 RFC 7009 — authorization revocation and propagation [S6]

Primary evidence:

- authorization grants or tokens can be invalidated unexpectedly;
- revocation prevents future token use;
- propagation can be temporarily non-instant across components;
- clients must handle revocation rather than assume permanent access.

Q5 support:

- continuations and active work must tolerate lost authority;
- cached access does not remain legitimate after revocation;
- revocation propagation and effect reconciliation can be distinct;
- capability availability cannot be assumed permanently.

Limitation:

- token revocation concerns technical authorization material, not truth,
  consent law, profile retirement or all prior effects.

### 6.7 Model Context Protocol — host authority, isolation and minimum
context [S7]

Primary evidence:

- the host controls connection permissions, security policy, consent,
  authorization and context aggregation;
- clients maintain isolated one-to-one server sessions;
- servers receive only necessary context;
- full conversation history remains with the host;
- focused servers do not automatically see other servers or all context;
- capabilities are explicitly negotiated.

Q5 support:

- context aggregation should remain under an owner/host-side boundary;
- process or tool capability does not justify full-profile access;
- each process receives a scoped projection rather than global context;
- context isolation is compatible with composition.

Limitation:

- MCP is a context/capability protocol, not a durable owner-profile,
  accepted-state, provenance or portable-continuation model.

### 6.8 Cedar authorization semantics — request-specific decisions and
guardrails [S8]

Primary evidence:

- authorization is evaluated for a principal, action, resource and request
  context;
- only relevant policy and entity data need be supplied;
- default deny is possible;
- explicit forbids can override permits;
- diagnostics can identify determining policies and errors.

Q5 support:

- owner preference should not override mandatory safety or prohibition;
- policy evaluation can use only relevant context;
- conflict behavior should be explicit rather than generic
  last-write-wins;
- authorization remains a request-time conclusion.

Limitation:

- Cedar's policy language and exact permit/forbid algorithm are one
  implementation approach. Q5 should retain the semantic guardrail pressure
  without selecting Cedar or a universal conflict algorithm.

### 6.9 Temporal workflow versioning — long-lived compatibility [S9]

Primary evidence:

- long-running executions can outlive workflow-definition changes;
- new executions can use updated behavior while existing executions remain
  on old compatible behavior;
- incompatible change requires explicit versioning or patching;
- old work is not silently reinterpreted under a new definition.

Q5 support:

- changed owner context must receive a per-obligation compatibility
  disposition;
- new work and existing work need not adopt a change at the same instant;
- a changed input is not a hidden hot-swap;
- continuation must retain enough dependency and compatibility information
  for legitimate resume.

Limitation:

- Temporal assumes a durable workflow runtime and deterministic replay
  constraints. Q5 requires semantic compatibility, not Temporal's runtime
  objects or versioning mechanism.

### 6.10 Google ADK state and memory — implementation scopes and explicit
persistence [S10]

Primary evidence:

- distinguishes invocation-temporary, session, user and application state
  scopes;
- user-scoped state can be shared across sessions within one application;
- persistence depends on the selected session service;
- session state and long-term memory are separate concerns;
- memory ingestion and state updates use explicit framework paths.

Q5 support:

- technical storage scope and semantic sharing legitimacy are different;
- a convenient user-wide namespace does not prove owner-wide authority;
- explicit ingestion is preferable to treating every transcript as memory;
- local, session-wide and owner-wide concerns need distinct handling.

Limitation:

- ADK prefixes, state keys, services and memory objects are
  implementation-specific. Its "user scope" is not automatically the Q5
  owner-profile boundary.

### 6.11 Anthropic multi-agent research system — isolated contexts and
checkpointed synthesis [S11]

Primary evidence:

- subagents use separate context windows, tools, prompts and exploration
  trajectories;
- a lead agent receives condensed results rather than one shared full
  context;
- separation of concerns reduces path dependence;
- production practice emphasizes checkpointing, tracing and evaluation.

Q5 support:

- isolation and selective return are viable even within one overall owner
  task;
- full-context replication is not required for useful multi-process work;
- shared context should be projected according to a bounded role and return
  contract.

Limitation:

- this is a production engineering report, not a standard for owner
  identity, consent, memory or durable process state.

## 7. Convergent findings

Strong cross-source convergence supports:

1. Source claim is distinct from accepted truth.

   Origin, integrity or signature verification does not prove the claim is
   suitable for the receiving process.

2. Provenance must survive transformation.

   Derived memory, summaries, corrections and revisions must retain causal
   relation to their sources.

3. Context scope and permission are independent.

   A system can technically possess or locate material without being
   permitted to disclose it to every process.

4. Purpose limitation and minimization are first-class pressures.

   "The same owner uses both processes" is not a sufficient purpose for
   sharing all available information.

5. Least-privilege projection is preferable to full-profile replication.

   A process should receive only what is relevant for its bounded purpose.

6. Permission to disclose and authority to act are different.

   Access to context, a credential or prior owner consent does not authorize
   a new effect automatically.

7. Process acceptance remains local.

   Different processes can legitimately apply different evidence,
   currentness and safety thresholds to the same source claim.

8. Promotion requires an explicit transition.

   Transcript occurrence, repetition, retrieval, model inference or local
   acceptance does not create owner-wide context.

9. Change has dependent-work consequences.

   Correction, revocation or retirement must be reconciled with active
   obligations, cached projections and continuations.

10. Long-lived work needs compatibility, not silent latest-value behavior.

    Existing obligations may need revalidation, migration, pin/drain,
    handoff or explicit suspension.

11. Status and verification can themselves leak information.

    A privacy boundary applies not only to claim content but also to access,
    status-check and correlation behavior.

12. Protected credentials are not ordinary memory.

    Raw secret-bearing capability material requires a separate protected
    boundary.

## 8. Material conflicts and non-convergent practice

### 8.1 Automatic memory versus explicit promotion

Agent frameworks range from automatically persisting conversation-derived
material to requiring explicit ingestion.

Q5 implication:

- do not accept automatic transcript-to-owner-profile promotion;
- memory services may propose or retain derived material, but owner-wide
  admission remains a governed semantic transition.

### 8.2 Broad user scope versus purpose-scoped disclosure

Some frameworks expose convenient user-wide state. Privacy and context
protocols favor selective disclosure and isolated consumers.

Q5 implication:

- implementation-wide user storage is evidence of technical scope only;
- semantic owner-wide applicability still requires relevance, purpose,
  sharing permission and normative ownership.

### 8.3 Immediate global update versus per-obligation compatibility

Mutable application state often exposes the latest value immediately.
Durable workflow systems preserve old behavior or explicitly migrate work.

Q5 implication:

- prefer per-obligation compatibility disposition;
- do not force every active process onto the latest profile input;
- do not let "pinning" bypass revoked disclosure or authority.

### 8.4 Generic inheritance versus policy guardrails

Configuration systems often use overlay precedence. Authorization systems
may use default-deny and prohibition-overrides behavior.

Q5 implication:

- generic last-write-wins is unsafe;
- resolve atomic claims through their normative owners;
- mandatory kernel and process safety constraints are guardrails, not
  lower-priority profile defaults;
- do not freeze one policy algorithm in Q5.

### 8.5 Revocation, suspension, correction and retirement

Credential, authorization, privacy and provenance systems use materially
different change semantics.

Q5 implication:

- do not use one deleted/active boolean;
- distinguish at the semantic level:
  future-use revocation, temporary restriction, factual correction,
  source invalidation and governed retirement;
- exact status names remain downstream.

### 8.6 Pin old context versus honor current privacy/authority

Workflow compatibility can justify running old work under an old definition.
Privacy or authority revocation can prohibit continued use of old inputs.

Q5 implication:

- pinning may preserve interpretation and evidence;
- it does not preserve permission that has been revoked;
- affected work must revalidate, restrict, migrate, stop or return unresolved.

## 9. Evidence for promotion into owner-wide context

Promotion is a durable semantic change in availability and projection scope.
It does not establish universal truth or grant effect authority.

Evidence that can justify promotion should include, as applicable:

1. Atomic concern identification

   The candidate is narrow enough that its source, normative owner,
   purpose and conflicts can be evaluated independently.

2. Legitimate owner-wide intent

   At least one of:

   - explicit owner declaration that a preference or policy is owner-wide;
   - explicit owner or owner-authorized approval that a source-backed
     contextual claim may be projected across stated process purposes;
   - an established standing policy that legitimately covers the candidate.

   Repetition across sessions or processes is evidence for a proposal, not
   an automatic promotion.

3. Cross-process relevance

   The concern has:

   - explicit owner-wide applicability; or
   - demonstrated legitimate use across materially different process
     pressures, followed by owner-authorized admission.

   Mere occurrence in several processes is insufficient if each occurrence
   has a different local meaning.

4. Provenance and derivation

   The candidate retains:

   - who or what asserted it;
   - collection or declaration context;
   - when it was established;
   - transformations, summaries or inferences applied;
   - uncertainty and evidence appropriate to consequence;
   - current source/status information.

   These are semantic requirements, not mandatory schema fields.

5. Purpose and eligible consumers

   The intended cross-process purpose is explicit enough to reject unrelated
   secondary use.

6. Sharing and privacy legitimacy

   The candidate can be projected without violating applicable owner,
   subject, third-party or process sharing limits.

7. Data minimization

   Only the minimum useful claim, abstraction or reference is promoted.

8. Currentness interpretation

   The receiving process can determine whether the material requires
   use-time revalidation, periodic review or event-driven review.

9. Conflict assessment

   Promotion does not:

   - override kernel semantics;
   - weaken mandatory process policy;
   - duplicate another normative owner;
   - expand effect authority;
   - turn capability metadata into permission.

10. Correction, dispute, revocation and retirement route

    The boundary can constrain or stop future projection and notify or
    reconcile dependent work without rewriting history.

11. Governed apply

    The promotion is validated and applied by the normative owner of the
    owner-wide boundary, with evidence of the resulting disposition.

12. Dependent-work treatment

    Existing obligations and continuations that could consume or already
    rely on the concern receive an explicit compatibility or revalidation
    disposition.

## 10. Promotion blockers

Promotion must be blocked or left unresolved when any material condition
below holds:

- the candidate is only a model inference, transcript fragment, temporary
  assumption or unreviewed summary;
- provenance or derivation is missing, ambiguous or materially incomplete;
- the asserted normative owner is not legitimate;
- no explicit owner-wide purpose or approved sharing scope exists;
- the proposal is justified only by "same owner";
- the candidate is stale for its consequence and cannot be revalidated;
- the claim is materially disputed and the proposed consumer cannot operate
  safely under uncertainty;
- the source, disclosure permission or authority has been revoked;
- the candidate conflicts with a kernel invariant or mandatory domain
  policy;
- promotion would broaden effect authority or consent;
- the proposed projection is broader than necessary;
- the candidate contains raw secret-bearing credential material;
- sensitive process-local material is proposed for unrelated secondary use;
- promotion would erase source identity or relabel derived memory as fact;
- no correction, restriction or retirement path exists;
- the change would occur through hidden profile mutation rather than a
  validated apply boundary;
- dependent active work cannot be reconciled or named as unresolved.

A blocked promotion can remain:

- process-local evidence;
- a source claim;
- derived memory;
- a bounded proposal;
- or an unresolved question with a current resolution owner.

Exact dispositions remain downstream.

## 11. Projection into a process

Promotion and projection are different:

- promotion establishes eligibility for bounded owner-wide availability;
- projection supplies a relevant permitted subset to one process;
- process acceptance determines whether that process may rely on it.

A legitimate projection should establish semantically:

- the bounded process purpose;
- why the concern is relevant;
- what minimum material or reference is supplied;
- source and derivation provenance;
- applicable sharing/privacy conditions;
- currentness and status limitations;
- whether use-time revalidation is required;
- whether the concern is descriptive context, owner preference, policy,
  authority evidence or capability metadata;
- conflicts with process-owned policy;
- what the process may do if the material is unavailable or rejected.

Projection must not:

- supply the complete owner profile by default;
- copy unrelated process history;
- expose raw credentials;
- imply authority from context access;
- force the receiving process to accept the claim;
- weaken a mandatory process rule;
- hide whether material is source-backed or derived.

## 12. Provenance, purpose, privacy and currentness

### 12.1 Provenance

Required semantic questions:

- Who asserted or declared the concern?
- Was it supplied directly, observed, inferred or derived?
- Under which process or collection context?
- What evidence supports it?
- What transformations produced the current form?
- What prior material has been corrected, superseded or invalidated?
- What uncertainty remains?

Owner confirmation of a preference and model inference of a preference are
different claims with different normative owners.

### 12.2 Relevance

Relevance is evaluated for the receiving process and current obligation.

A concern can be genuinely owner-wide yet irrelevant to one process.

No process receives owner context solely because it has technical access.

### 12.3 Purpose limitation

Approval for one purpose does not silently permit unrelated reuse.

A process that wants a materially new purpose must obtain a legitimate new
projection or authority disposition.

### 12.4 Least privilege and minimization

Projection should prefer:

- a narrow claim over a complete record;
- an abstract constraint over sensitive source detail when sufficient;
- a validated reference over duplication when the reference remains
  accessible and portable enough for continuation;
- capability use over disclosure of raw secret material.

Exact privacy technology remains open.

### 12.5 Privacy and sharing

Sharing boundaries apply to:

- claim content;
- metadata and provenance;
- source identity where sensitive;
- derived memory;
- access logs and status checks;
- continuation content;
- downstream re-disclosure.

The owner cannot authorize disclosure of third-party material where the
owner is not the legitimate authority.

### 12.6 Staleness

No universal time-to-live is supported.

Currentness depends on:

- claim type;
- source behavior;
- intended purpose;
- consequence of error;
- known change triggers;
- applicable process policy.

Higher-consequence, rapidly changing or externally sourced claims generally
require stronger use-time evidence than durable presentation preferences.

A durable preference remains correctable by the owner and cannot be treated
as immutable.

### 12.7 Correction

Correction should:

- establish the currently accepted replacement through a governed apply
  boundary;
- preserve relation to the prior claim;
- retain evidence of who corrected what and why;
- identify affected projections and active work;
- trigger bounded revalidation where reliance might change.

Correction is not silent overwrite.

### 12.8 Dispute

A dispute should:

- preserve competing claims and their provenance;
- avoid generic last-write-wins;
- identify a current resolution owner;
- constrain high-risk reliance where uncertainty is material;
- permit explicitly safe degraded or provisional behavior where the process
  pack allows it.

### 12.9 Revocation

Revocation can concern different things:

- permission to disclose;
- permission to use;
- action authority;
- source or credential validity;
- technical capability access.

Consequences differ:

- future use or disclosure can become prohibited;
- a pending action can lose authorization;
- an already-applied effect remains historical fact and may require
  compensation rather than fictional rollback;
- the underlying descriptive claim can remain true even when permission to
  use it is withdrawn;
- revocation propagation can require reconciliation.

### 12.10 Retirement

Retirement is governed closure, not simple deletion.

A retired concern should no longer enter new projections unless separately
re-admitted.

Retirement may be blocked while:

- active obligations still depend on the concern;
- a continuation cannot interpret prior accepted work without its
  provenance;
- unresolved authority or effects remain;
- required evidence or audit would be destroyed;
- correction or dispute lineage would become unintelligible.

Retirement can preserve historical evidence without retaining permission
for new use.

Exact retention and erasure policy belongs to Q6 and applicable domain/legal
policy.

## 13. Conflict rules

Q5 should preserve Q4 atomic normative ownership.

### Owner preference versus kernel invariant

Disposition:

- reject the conflicting preference as inapplicable to the affected claim;
- an owner preference cannot legalize a kernel override.

### Owner preference versus mandatory process safety/effect policy

Disposition:

- mandatory process policy constrains the preference;
- the process may request a bounded owner decision only where the policy
  legitimately leaves a choice;
- owner preference is not a bypass.

### Shared source claim versus process-local accepted state

Disposition:

- do not silently overwrite active state;
- validate source, currentness and applicability;
- use compatible resume, revalidation/migration, pin/drain or unresolved
  treatment as appropriate.

### Conflicting source claims

Disposition:

- preserve both sources and evidence;
- receiving process applies its evidence and consequence policy;
- unresolved material names a resolution owner;
- arrival order and profile insertion order do not decide truth.

### Sharing approval versus action authority

Disposition:

- sharing approval permits only the bounded disclosure/use;
- action follows separate validation and authorization.

### Technical capability versus permission

Disposition:

- capability can be reported as available;
- use remains limited by current permission, authority and process policy.

### Revoked permission versus pinned old work

Disposition:

- pinning can preserve interpretation and audit;
- it cannot preserve revoked disclosure or action authority;
- work must restrict, migrate, reauthorize, stop or return unresolved.

## 14. Active obligations and portable continuation

A changed owner-profile input is an observation. It does not silently mutate
the effective process definition or every active obligation.

Each affected obligation requires an explicit disposition.

### 14.1 Changed but compatible input

Possible behavior:

- new work can use the newly admitted input;
- active work can resume after bounded compatibility confirmation;
- no broader authority follows from compatibility.

### 14.2 Materially changed or corrected input

Possible behavior:

- revalidate dependencies and accepted conclusions;
- migrate only the affected state or procedure assumptions;
- preserve prior evidence;
- keep unaffected work stable;
- name unresolved work and its owner.

### 14.3 Stale input

Possible behavior:

- revalidate from an authoritative or acceptable source;
- operate only through a process-pack-declared degraded route that preserves
  mandatory safety, authority, result and continuation obligations;
- otherwise block or wait for named input rather than guess.

Cached owner context is not a substitute for currentness evidence.

### 14.4 Disputed input

Possible behavior:

- suspend high-consequence reliance;
- preserve competing claims;
- continue only where uncertainty is explicitly acceptable under process
  policy;
- route resolution to the legitimate owner.

### 14.5 Disclosure or use permission revoked

Required behavior:

- stop future projection and prohibited use;
- constrain cached or continued copies;
- re-evaluate affected active obligations;
- preserve only evidence/history that remains legitimately retainable;
- do not treat the revocation as proof that the underlying claim is false.

### 14.6 Action authority revoked

Required behavior:

- block pending effects that have not been authoritatively applied;
- reconcile races or outcome-unknown effects;
- retain already-applied effect evidence;
- use a new governed compensation path where appropriate;
- do not infer rollback from revocation.

### 14.7 Conflict with mandatory process policy

Required behavior:

- mandatory policy remains authoritative;
- no best-effort profile override;
- reject, reframe or request only a decision that legitimately remains open.

### 14.8 Shared input cannot be accessed

Required behavior:

- distinguish inaccessible from false, revoked, retired or nonexistent;
- use a declared degraded route only when the input is truly optional;
- otherwise wait, block, migrate or return unresolved with a current owner;
- never fabricate the missing content;
- continuation records the access dependency and legitimate next route.

### 14.9 Retired input

Required behavior:

- prevent entry into new projections;
- close, migrate or drain dependent obligations;
- retain enough provenance to interpret prior accepted work;
- do not leave ownerless references.

### 14.10 Continuation semantic minimum for Q5 pressure

Without defining exact fields, a portable continuation affected by owner
context must preserve enough meaning to determine:

- which obligation depends on owner-wide or local context;
- whether relied material was source-backed, owner-declared, derived,
  provisional or accepted;
- relevant provenance and currentness/status limitations;
- purpose and sharing boundaries;
- action-authority status separately from context availability;
- compatibility with changed context or process definition;
- whether revalidation, migration, restriction, pin/drain, handoff or
  closure is required;
- current next-action and resolution owners;
- the next legitimate action.

Continuation must not:

- embed raw secrets;
- copy sensitive context merely for convenience;
- use an inaccessible opaque reference without declaring the access
  requirement and failure route;
- silently authorize renewed use;
- omit a known dispute, revocation or staleness condition.

Exact continuation representation remains Q9/Q12.

## 15. Health-like privacy and safety pressure

This is a boundary stress test, not actual Health policy.

Pressure characteristics:

- sensitive and potentially high-consequence personal information;
- rapidly changing factual claims;
- strict provenance and evidence needs;
- domain-owned safety and escalation rules;
- purpose-limited sharing;
- stale or revoked permission risk;
- long-lived obligations and continuations.

Candidate owner-wide inputs that can be legitimate in principle:

- explicitly owner-wide language, accessibility or explanation preference;
- approved privacy/sharing defaults;
- explicitly owner-wide decision-routing preferences within mandatory
  domain constraints;
- another approved shared constraint whose cross-process purpose and
  provenance are established.

Concerns that remain process-local by default:

- domain observations and working hypotheses;
- measurements, symptoms, diagnoses, treatment facts or risk estimates;
- one workflow's evidence conclusions;
- clinician, model or process summaries;
- local consent or approval for one bounded disclosure/effect;
- disputed or stale health-related claims.

These concern labels are test pressures, not an actual profile or Health
data model.

Boundary behavior:

- a source-backed health-related claim may be admitted for a specific
  cross-process purpose only through explicit promotion and sharing
  legitimacy;
- owner approval to share does not make the claim clinically true;
- another process does not receive the claim merely because it concerns the
  same owner;
- mandatory domain evidence and safety policy remains process-pack-owned;
- an owner preference cannot lower those requirements;
- stale, disputed, inaccessible or revoked mandatory context blocks risky
  reliance unless the pack defines a safe degraded route;
- continuation minimizes sensitive content and preserves access,
  provenance, currentness and revalidation requirements.

Verdict:

PASS at the semantic boundary.

The boundary supports strict privacy, provenance and fail-closed behavior
without making Health policy universal or copying Health context into a
creative process.

## 16. Game/productive-play creative pressure

This is a boundary stress test, not an actual game or productive-play pack.

Pressure characteristics:

- exploratory and branching work;
- rapid iteration;
- subjective preferences;
- frequently reversible local changes;
- project-specific canon and temporary assumptions;
- optional retrieval or evaluation support;
- lower consequence for some stale preferences;
- frequent owner steering.

Candidate owner-wide inputs that can be legitimate in principle:

- explicitly owner-wide language, presentation or feedback preference;
- an explicitly declared initiative/steering preference;
- approved privacy defaults;
- a broad creative preference explicitly intended to span projects.

Concerns that remain process-local by default:

- local canon;
- project goals and rules;
- branch-specific ideas;
- playtest findings;
- temporary aesthetic hypotheses;
- one project's interpretation of owner taste;
- local approval to publish or change a project artifact.

Boundary behavior:

- repeated preference observed in one project can produce a promotion
  proposal but not a hidden owner-wide update;
- local canon never becomes owner-profile truth;
- a lower-stakes process can define a useful degraded route when optional
  owner context is stale or unavailable;
- uncertainty and changed result quality remain visible;
- irreversible publication still requires separate authority/apply
  semantics;
- no Health-specific safety or evidence policy is imported.

Verdict:

PASS at the semantic boundary.

The same boundary permits flexible creative iteration without turning local
project memory into global authority.

## 17. Cross-pressure verdict

The candidate Q5 boundary supports both:

- strict, privacy-sensitive and consequence-sensitive context handling;
- exploratory, subjective and frequently changing creative work.

It does so without:

- copying one process into another;
- making all owner facts globally available;
- modifying kernel semantics;
- weakening process-owned policy;
- requiring one schema, repository, privacy technology or final
  service-block list.

The cartography return condition is not triggered.

## 18. Failure modes and required defenses

### 18.1 Global-context dumping

Failure:

- every available owner fact, transcript and memory is injected into every
  process.

Consequences:

- privacy leakage;
- irrelevant context;
- correlation;
- prompt contamination;
- accidental authority.

Defense:

- purpose-scoped, minimum relevant projection.

### 18.2 Accidental cross-process authority

Failure:

- one process's approval, consent or action history is interpreted as
  standing authority in another.

Defense:

- separate context availability, disclosure permission, action authority
  and accepted truth.

### 18.3 Stale owner assumptions

Failure:

- an old inferred preference or factual claim remains globally active
  without review.

Defense:

- source/currentness interpretation, use-time revalidation and correction
  propagation.

### 18.4 Secret leakage

Failure:

- tokens, keys, passwords or recovery material enter ordinary memory,
  prompts, traces or continuations.

Defense:

- protected capability boundary; project only non-secret capability facts
  where required.

### 18.5 Automatic local-to-global promotion

Failure:

- transcript occurrence, repeated behavior, local acceptance or memory
  ingestion updates the owner profile.

Defense:

- explicit promotion proposal, validation, owner-wide authority and governed
  apply.

### 18.6 Hidden profile mutation

Failure:

- a model silently edits owner-wide preference or context while reasoning.

Defense:

- proposal, validation, authorization where needed, apply result and
  provenance.

### 18.7 Derived-memory laundering

Failure:

- a summary, inference or preference hypothesis is presented as source fact.

Defense:

- preserve derivation, confidence and upstream dependencies.

### 18.8 Availability/consent conflation

Failure:

- because context can be queried, it is treated as permitted for every use.

Defense:

- purpose- and consumer-specific disclosure/use conclusion.

### 18.9 Consent/action conflation

Failure:

- consent to use data is interpreted as authority to perform a related
  external effect.

Defense:

- separate action proposal, validation, authorization and apply.

### 18.10 Last-write-wins conflict

Failure:

- latest source, profile edit or process update silently wins.

Defense:

- atomic normative ownership, provenance and explicit conflict resolution.

### 18.11 Profile backdoor around mandatory policy

Failure:

- owner preference weakens domain safety, evidence or effect controls.

Defense:

- kernel and mandatory process policy remain non-overridable guardrails.

### 18.12 Continuation leakage

Failure:

- portable continuation copies sensitive content or secrets to ensure
  resumability.

Defense:

- minimum semantic dependency, protected references, access requirements and
  explicit unavailable-state behavior.

### 18.13 Retirement as deletion

Failure:

- removing current availability also destroys evidence needed to interpret
  old work.

Defense:

- governed retirement with lineage, dependency and retention disposition.

### 18.14 Inaccessible reference treated as resolved

Failure:

- a continuation contains an opaque reference that a new carrier cannot
  access, yet reports the work resumable.

Defense:

- declare access requirement, compatibility gap and current resolution
  owner.

### 18.15 Revocation treated as rollback

Failure:

- withdrawing consent or authority is reported as undoing prior processing
  or applied effects.

Defense:

- stop prohibited future use, preserve historical evidence and route any
  compensation as a new governed effect.

### 18.16 Status-check privacy leak

Failure:

- checking whether a claim or credential is current reveals which process
  is using it and when.

Defense:

- include status verification in privacy and minimization analysis.

### 18.17 Profile-completeness bureaucracy

Failure:

- the system optimizes for accumulating and maintaining a comprehensive
  owner profile rather than reducing reconstruction and supporting useful
  owner-facing work.

Defense:

- admit only demonstrated cross-process value;
- project only relevant context;
- evaluate live usefulness rather than surface completeness.

### 18.18 Storage design masquerading as Q5

Failure:

- a vector store, graph, file layout, identity provider or profile object is
  selected before the semantic boundary is established.

Defense:

- return to the four independent conclusions, normative ownership and
  lifecycle obligations; leave representation and implementation to
  downstream work.

## 19. Candidate Q5 architecture directions

These are research directions for architecture-forge, not owner-approved
architecture.

### Direction A — governed owner-context admission and scoped projection

Core idea:

- owner-wide preferences/policies and approved shared contextual claims
  enter the owner boundary only through explicit admission;
- every atomic concern retains normative ownership and provenance;
- processes obtain a minimum purpose-scoped projection;
- the process separately accepts or rejects the projected claim;
- promotion, correction, revocation and retirement use governed change;
- active obligations receive compatibility dispositions.

Useful because:

- directly prevents local facts from becoming global authority;
- preserves source, privacy, purpose, truth and authority distinctions;
- fits Q4 staged admission/activation;
- supports active-work and continuation semantics;
- remains carrier- and implementation-neutral.

Bad, because:

- provenance, projection and lifecycle checks can create ceremony and
  profile-management bureaucracy if every low-risk preference is treated as
  a high-assurance claim.

Required mitigation:

- risk- and consequence-sensitive evidence;
- simple owner declaration paths for low-risk preferences;
- no requirement for one heavyweight lifecycle UI or schema.

### Direction B — inherited owner baseline with process-local overlays

Core idea:

- each process begins from an owner-wide baseline and applies process-local
  additions or overrides.

Useful because:

- conceptually simple;
- easy to explain as shared defaults plus local variation;
- can reduce repeated declaration of low-risk preferences.

Bad, because:

- overlay language invites global dumping, generic precedence, hidden
  authority expansion and accidental weakening of mandatory process policy.

Required constraint if any part is retained:

- it may describe normative layers only;
- it must not use generic last-write-wins;
- process-local material cannot write back automatically;
- kernel and mandatory process rules remain guardrails.

### Direction C — on-demand purpose-bound context disclosure

Core idea:

- processes do not import an owner baseline;
- they request only the specific owner-wide concern needed for a declared
  purpose;
- the boundary returns a permitted minimum projection or an explicit
  unavailable/rejected disposition.

Useful because:

- strongest default minimization and isolation;
- context use becomes observable and purpose-bound;
- reduces persistent cross-process copies;
- fits MCP-like host-controlled context projection.

Bad, because:

- dependence on live access can make continuation fragile, repeat consent
  prompts, increase latency and fail when the context source is unavailable.

Required mitigation:

- portable dependency and access semantics;
- standing bounded owner policy where appropriate;
- legitimate degraded routes;
- explicit inaccessible-context behavior.

## 20. Research recommendation

Recommend that Q5 architecture-forge evaluate:

1. Direction A as the primary architecture backbone.

2. Direction C as the subordinate projection/access pattern inside
   Direction A.

3. Direction B only as a descriptive view of normative layers, not as a
   generic inheritance or override algorithm.

Compact recommendation:

Establish one governed owner-context boundary that owns owner-wide
declaration/admission and sharing scope, but not the truth of every source
claim or the policy of every process. Admit only genuinely owner-wide
preferences, policies and approved shared claims under provenance, purpose,
minimization, privacy and change semantics. Project a minimum relevant subset
on demand or at process admission. Let each process apply its own mandatory
evidence, currentness and safety policy before accepting the material.
Preserve disclosure permission, action authority and accepted truth as
separate conclusions. Re-enter Q4 validation, impact, authority and apply
semantics whenever a material input changes; give every affected active
obligation and continuation an explicit disposition.

This recommendation does not freeze:

- a final category list;
- owner-profile entities or schema;
- exact promotion or lifecycle statuses;
- identifiers, field names or version syntax;
- query or projection protocol;
- retention intervals;
- conflict-resolution algorithm;
- consent UI or approval language;
- privacy technology;
- repository, storage or indexing;
- physical state owner or writer topology;
- process consumer template;
- final service-block list.

## 21. Evidence confidence

### High confidence

Strong primary-source and accepted-parent support exists for:

- claim/source provenance separate from receiving-process truth;
- derivation, revision and invalidation lineage;
- purpose limitation and data minimization;
- isolated/minimum context projection;
- context availability separate from disclosure permission;
- disclosure permission separate from action authority;
- capability and credential possession separate from authority;
- explicit revocation and changed-status handling;
- correction and restricted-use pressure;
- long-lived-work compatibility rather than hidden latest-value behavior;
- secrets excluded from ordinary context and continuation;
- rejection of automatic transcript/local-memory promotion.

### Medium-high confidence

Strong architecture synthesis supports:

- governed owner-context admission and scoped projection as the Q5
  backbone;
- the four independent conclusions;
- explicit promotion evidence and blockers;
- owner-profile responsibility owning admission/sharing rather than all
  claim truth;
- per-obligation context compatibility disposition;
- retirement as governed closure rather than deletion;
- Direction C as a subordinate least-privilege projection mode.

### Medium confidence / forge choices

Q5 forge still needs to choose:

- the exact accepted boundary formulation;
- how much low-risk owner declaration can be treated as immediately
  owner-wide without a separate confirmation step;
- whether every cross-process contextual claim requires explicit owner
  approval or some may enter under a standing approved policy;
- the minimum cross-process-relevance evidence where owner-wide intent was
  not declared in advance;
- default behavior for stale low-consequence preferences;
- when a derived memory may be shared across processes;
- how strongly to prefer reference over materialized projection;
- which disagreements block use versus permit provisional/degraded use;
- how dependent consumers learn of correction or revocation;
- the minimum continuation dependency information.

## 22. Evidence limits

1. No reviewed source defines the desired complete owner-profile boundary.

2. W3C VC and PROV provide claim and provenance semantics but do not define
   process-pack admission, owner authority or portable process continuation.

3. Bitstring Status List provides credential-specific status behavior, not
   a universal owner-context lifecycle.

4. GDPR supplies strong privacy, correction and purpose-limitation pressure
   but is a jurisdiction-specific legal instrument and does not by itself
   define universal substrate semantics.

5. OAuth RFCs address authorization artifacts, not factual truth, memory or
   full consent governance.

6. Cedar demonstrates one authorization conflict algorithm; Q5 must not
   freeze its policy language or implementation.

7. MCP provides strong context-isolation evidence but does not define
   durable owner-wide state or cross-carrier continuation.

8. ADK state scopes demonstrate implementation convenience, not normative
   owner-wide applicability.

9. Temporal provides strong long-lived compatibility evidence but assumes a
   durable workflow runtime and replay model.

10. Anthropic's multi-agent account is an engineering report, not an
    interoperability standard.

11. None of the external sources contains the accepted Q1-Q4 semantic
    relationship, normative-ownership or process-pack model.

12. No actual owner profile was defined, implemented or live-tested.

13. No Health-like or game process was instantiated for this research; the
    pressure tests are semantic refutations, not product validation.

14. No source proves that one physical central profile store is required.

15. No source proves that one federated or decentralized physical topology
    is required.

16. Exact evidence thresholds, retention, dispute adjudication, consent
    categories, continuation fields and representation remain downstream.

17. Protocol or artifact completeness does not prove useful owner-facing
    operation.

Evidence that would materially change the recommendation includes:

- owner-facing trials showing that governed admission/projection creates
  more reconstruction and confirmation burden than it prevents;
- two materially different process pressures that cannot share the proposed
  four-way boundary without copying one consumer into another;
- proof that automatic process-memory promotion can preserve provenance,
  purpose, consent, authority and correction without explicit transition;
- a broadly adopted standard defining portable owner-wide claims,
  permissions, active-work dependencies and cross-runtime continuation;
- an accepted Q1-Q4 revision changing normative ownership or process-pack
  instantiation;
- evidence that purpose-scoped projection cannot support mandatory
  continuation without selecting a storage implementation.

## 23. Child and downstream questions

These do not block Q5 forge.

### Q5 forge must decide

- the accepted semantic definition of the owner-profile/shared-context
  boundary;
- what owner-wide preference/policy and approved shared context mean;
- what remains local by default;
- the four independent conclusions;
- promotion evidence and blockers;
- conflict behavior;
- lifecycle obligations for currentness, correction, dispute, revocation
  and retirement;
- active-work and continuation dispositions;
- the primary architecture direction.

### Q5 child questions

1. Under what standing owner policy, if any, may a low-risk preference
   become owner-wide without a fresh explicit approval?

2. What minimum evidence establishes cross-process relevance when an owner
   has not directly declared owner-wide intent?

3. When may a derived memory be promoted while preserving its inferred
   status and upstream dependencies?

4. Which owner-context changes are compatible with active work as-is and
   which require revalidation or migration?

5. How is a dispute resolved when the owner, an external source and a
   process-local accepted state disagree?

6. How is correction or revocation propagated to processes that received a
   prior projection?

7. How can continuation declare a sensitive dependency without embedding
   the sensitive material?

8. When may retired context remain interpretable for history but unavailable
   for new projection?

9. How should status checks avoid revealing process activity or correlating
   uses?

10. What is the legitimate normative owner when context concerns multiple
    people rather than only the owner?

### Existing downstream routes

- Q6 persistence/history:
  current accepted owner context, provenance history, correction,
  restriction, retirement and retention responsibilities.

- Q8 live interface:
  low-bureaucracy owner declaration, correction, disclosure and dispute
  interaction without exposing internal profile machinery.

- Q9 result/continuation:
  minimum context-dependency, status, access and revalidation semantics in
  result and portable continuation.

- Q10 authority/gates:
  which promotion, sharing, consent, revocation and action changes require
  owner authorization; how standing policy is bounded.

- Q11 evidence/evolution:
  evidence-to-promotion, compatibility, correction, retirement and
  change-review rules.

- Q12 communication/entities:
  exact claim, source, derivation, identity, correlation, projection and
  reference representation.

- Q13 proof:
  conformance scenarios for local-to-global promotion, stale/revoked
  context, secret leakage, conflict and active-work continuation.

- Q14 carrier:
  mapping the semantic boundary to Markdown, chat, applications, stores and
  transports without making a carrier authoritative.

No child question is a hidden prerequisite for the bounded Q5 architecture
decision.

## 24. Q5 architecture-forge handoff

plain_question: |
  Что может legitimately be supplied as shared owner context across
  processes, and what must stay local?

why_it_matters: |
  Multiple processes may need owner-wide preferences, policy, resources,
  constraints or contextual claims. Legitimate sharing can reduce repeated
  reconstruction. Unbounded sharing creates privacy leakage, stale
  assumptions, accidental authority and hidden global state.

expected_answer_shape: state_model

must_decide: |

  - the semantic boundary between owner-wide preference/policy, approved
    shared context and process-local material;
  - how source claims, derived memory, authority/consent and credentials/
    secrets relate to that boundary;
  - the independent conclusions for availability, disclosure/use,
    action authority and accepted process truth;
  - evidence for promotion and mandatory blockers;
  - provenance, relevance, purpose limitation, least privilege and
    privacy/sharing obligations;
  - staleness, correction, dispute, revocation and retirement semantics;
  - conflict behavior under atomic normative ownership;
  - changed-context behavior for active obligations and portable
    continuations;
  - the primary Q5 architecture direction.

must_not_decide: |

  - actual owner profile or personal content;
  - actual Health, game, Zaratusta or Direction OS policy;
  - final context/category catalogue;
  - entity, profile, claim, consent, message, continuation or storage schema;
  - field names, identifiers, version syntax or exact lifecycle enum;
  - repository, database, vector store, knowledge graph, identity provider,
    policy engine or privacy technology;
  - provider, model, framework, runtime, transport, application or
    deployment;
  - physical writer or state topology;
  - consumer template or final service-block list;
  - implementation.

candidate_directions: |

  A. Governed owner-context admission and scoped projection.
     Bad, because it can create lifecycle and confirmation bureaucracy if
     low-risk preferences are treated like high-assurance claims.

  B. Inherited owner baseline with process-local overlays.
     Bad, because generic inheritance and precedence can create global
     dumping, hidden authority and unsafe process-policy override.

  C. On-demand purpose-bound context disclosure.
     Bad, because live access dependence can create repeated prompts,
     unavailable-context failures and fragile continuation.

research_recommendation: |
  Use A as the primary backbone, C as the subordinate projection/access
  pattern, and retain only the normative-layer explanation from B. Do not
  adopt generic overlay precedence.

proof_pressure: |

  - one process-local preference repeated several times but never explicitly
    approved as owner-wide;
  - an owner-declared low-risk preference legitimately projected to both a
    Health-like and game-like process;
  - a sensitive Health-like source claim requested by an unrelated creative
    process;
  - a derived memory that contradicts its source;
  - conflicting source claims with different currentness;
  - a shared-context claim that becomes stale during active work;
  - disclosure permission revoked while a continuation still references the
    claim;
  - action authority revoked after proposal but before apply;
  - raw secret material proposed for ordinary context;
  - owner preference conflicting with mandatory domain safety policy;
  - shared context unavailable on a new carrier;
  - hidden model-generated profile mutation;
  - retired context still needed to interpret historical work;
  - status verification that leaks process activity;
  - a formally complete profile flow that produces owner-facing
    bureaucracy.

return_to_graph_if: |

  - Q5 cannot prevent process-local material from becoming owner-wide
    authority;
  - the answer requires a repository, storage, identity or privacy
    implementation before the semantic boundary can be stated;
  - active obligations cannot remain legitimate when shared context changes;
  - the boundary cannot support both privacy/safety-critical and exploratory
    creative pressures;
  - a newly discovered entity is a hard prerequisite rather than a
    downstream schema or authority question.

## 25. Graph, gap and route verdict

hidden_prerequisite: none
gap_event: none
top_level_rebalance: not_needed
return_to_cartography: not_required
implementation_activation: prohibited
q5_architecture_forge: ready

Why Q5 is ready:

- Q1 fixes the stable kernel and owner-tuned/pluggable-process boundary;
- Q2 separates kernel, reusable-service, process-pack, owner-profile and
  adapter concerns by normative ownership;
- Q3 fixes provenance, authority, apply, result and continuation
  distinctions;
- Q4 fixes staged admission/activation and changed-input treatment;
- primary sources converge on provenance, selective disclosure, purpose
  limitation, least privilege, bounded authorization, revocation and
  long-lived compatibility;
- the candidate boundary passes materially different Health-like and
  game/productive-play pressures;
- unresolved representation, retention, gate and carrier questions fit
  existing Q6-Q14 routes.

Next graph route:

- one bounded Q5 shared-owner-context architecture-forge;
- no implementation, profile content, schema, repository, privacy
  technology or final service-block work.

## 26. Primary-source register

[S1] W3C Verifiable Credentials Data Model v2.0,
     W3C Recommendation, 15 May 2025.
     https://www.w3.org/TR/vc-data-model-2.0/

[S2] W3C PROV-DM: The PROV Data Model,
     W3C Recommendation, 30 April 2013.
     https://www.w3.org/TR/prov-dm/

[S3] W3C Bitstring Status List v1.0,
     W3C Recommendation.
     https://www.w3.org/TR/vc-bitstring-status-list/

[S4] Regulation (EU) 2016/679, official EUR-Lex text.
     Used as privacy/governance pressure, not asserted as universal law.
     https://eur-lex.europa.eu/eli/reg/2016/679/oj

[S5] IETF RFC 9396 — OAuth 2.0 Rich Authorization Requests,
     May 2023.
     https://www.rfc-editor.org/rfc/rfc9396

[S6] IETF RFC 7009 — OAuth 2.0 Token Revocation,
     August 2013.
     https://www.rfc-editor.org/rfc/rfc7009

[S7] Model Context Protocol specification 2025-11-25 — Architecture;
     MCP Security Best Practices.
     https://modelcontextprotocol.io/specification/2025-11-25/architecture
     https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices

[S8] Cedar Policy Language Reference Guide — How Cedar authorization works.
     https://docs.cedarpolicy.com/auth/authorization.html

[S9] Temporal Platform documentation — Workflow versioning,
     Continue-As-New and Workflow message passing.
     https://docs.temporal.io/develop/java/workflows/versioning
     https://docs.temporal.io/workflow-execution/continue-as-new
     https://docs.temporal.io/develop/python/workflows/message-passing

[S10] Google Agent Development Kit documentation — State and Memory.
      https://adk.dev/sessions/state/
      https://adk.dev/sessions/memory/

[S11] Anthropic — How we built our multi-agent research system.
      https://www.anthropic.com/engineering/multi-agent-research-system

External sources observed 2026-07-11.

END_OF_FILE: live/solmax/work/operating-substrate-shared-owner-context-best-practice-research-001.md
