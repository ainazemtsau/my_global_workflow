# Converge-arch — g-health-core KERNEL (Declare + Decompose + Architect; assembly surface, removable; not a state file)

> Produced by the converge-arch play, session s-health-core-kernel-converge-arch-001 (2026-06-20). HEAVY node, RETROFIT.
> Authority is the §SIGNOFF below + the RESULT in history/, never this file alone. This file DECLARES the kernel's
> cross-cutting CONTRACTS on paper ON TOP of two born-closed inputs it never re-opens:
> (1) the signed kernel WHAT — work/converge-g-health-core-kernel.md (§KW-MEM/SM/RT/REG/GOV/LAY/AF/ADD, §WA-K1–K12,
>     §OWNER DECISIONS Package A F1–F16 + B-1..B-4, §KERNEL-PLAN-AGENDA KP1–KP12);
> (2) the signed data/contract layer — work/converge-g-health-core.md (CA1–CA9, §ARCH Q1–Q6/AA1–AA3, P1–P27).
> Governance baseline imported: work/core-kernel-governance-lifecycle-spec.md (FM1–FM12).
> Read-only assembly + adversarial verification: workflow wf_4eee70ff-ec6 (9 agents: declare + independent §KW-coverage
> oracle + 4 architecture refuted-chains + 3 attackers). Two attackers independently corrected the draft (5 orphan
> §KW rows bound; one over-called owner-fork demoted to system-locked) — closes ZERO new owner gates.

## §SCOPE & FRAME
The KERNEL §KW set has NO cross-NODE sibling contract of its own. It is entirely a **producer → all-domains
INHERITANCE surface**: the kernel ENGINE (runtime primitives + governance lifecycle) is the producer; every domain
(g-health-nutrition-system [parked], g-health-training-activity-system [parked], every future domain) is a consumer
that inherits it UNCHANGED — so no domain reinvents the engine (the exact defect that got the nutrition slice
rejected 2026-06-20). These 14 kernel contracts (KC1–KC14) are COMPLEMENTARY to, and layered ON TOP of, the
data-layer's CA1–CA9 (data/concept contracts: phase, metric-trio, day_type, attach-point, parse surface), which they
REUSE unchanged (CA4 attach-point, CA5 day_type isolation, CA6/CA7 CORE template + parse/library/procedure surface,
CA8 schema_version) rather than re-open.

## §DECOMPOSE (Step 2)
**Sub-systems (10+ internal):** single router/interpreter · working-state cursor · state-machine (definition/cursor
split) · procedure registry · content-authority lifecycle · owner-approval gate · writer-applier barrier ·
confirm-by-layer dispatch · render-before-decision gate · one-chat-one-job/handoff · provenance space · thin-domain
attach · anti-fragility/extension · cold-start bootstrap.

**Sub-node decision: NONE new.** Every kernel part is a CORE-owned engine part of the SAME node (g-health-core),
authored together as one indivisible kernel; none is separately shippable or separately owner-decidable (every
governance term is signed as one Package-A/B set; KC12 forbids a domain owning an engine part; splitting any
primitive into its own node would fragment the single-router / single-registry / single-lifecycle invariants the
kernel exists to guarantee). The ONLY sub-nodes remain the already-tree'd PARKED domains — TIER-3 consumers of this
kernel, not kernel sub-systems. (Mirrors the data-layer converge-arch: 10 sub-systems, sub-nodes NONE.)

**Internal seams (WHAT side; HOW → PLAN):**
- **S1 router↔registry** — the router obtains term→procedure resolution ONLY by registry lookup; routing authority is
  a per-entry property, never folder/location. (KG7/KR2; grammar→KP4, path→P20)
- **S2 router↔cursor** — the router resolves current state by validating the cursor (evidence) against the machine,
  and is the sole mover of the cursor; never reconstructs position from chat memory. (KR4/KS7; cursor shape→KP2/KP1)
- **S3 router↔state-machine DEFINITION (authority)** — the definition is authority for what is legal (cursor is only
  evidence); on drift the router BLOCKS to repair, never guesses. (KR4/KS4; def shape→KP2)
- **S4 writer-barrier↔approval-gate** — the writer-applier rejects any ACTIVE-targeted write lacking the gate's
  owner-approval marker; mechanically closes no-role-both registry-side (an authoring procedure may write only
  PROPOSED). (KG4/KV10; marker→KP5, writable-status→KP4)
- **S5 state-machine↔lifecycle — ORTHOGONAL** — a state authorizes which family may become PROPOSED/ACTIVE
  (structural); the lifecycle `status` leaf is the authority carrier (governance); a cursor in a state NEVER confers
  ACTIVE authority. The two axes couple at exactly ONE one-way point: render-before-decision (S see KQ3 / KC9).
  (KS3/KS8/KV1)
- **S6 registry↔state-machine join** — a registry entry binds which state(s) a procedure is valid in; dispatch is
  keyed by the resolved STATE, not a free term. (KG3/KR2; valid-states→KP4, labels→KP2)
- **S7 partial-write atomicity (inside the barrier)** — a governed transition is two durable writes in a FIXED order:
  persist the artifact/status-flip WITH evidence FIRST, advance the cursor SECOND, so a crash leaves a re-runnable
  state, never a cursor ahead of unactivated content. (KD4/KV11; protocol→KP10)

**Build-order — THREE-TIER STACK:**
- **TIER-1** = the signed data/contract layer (CA1–CA9, W1–W79, WA1–WA12) — imported born-closed; the kernel is built
  ON it, never re-opened.
- **TIER-2** = the kernel runtime + governance (KC1–KC14) — built next, as ONE indivisible engine.
- **TIER-3** = thin domains (nutrition [parked], training [parked], future) — each = {namespaced data, one procedure
  per term, one registry line, one state-machine instance}, zero engine code. CA6 already removed the
  nutrition→training edge, so after the kernel the two converge in EITHER order.
- **Intra-kernel (TIER-2):** (1) runtime primitives as co-built co-primitives — KC1 router resolving over KC2 cursor +
  KC3 state-machine grammar + KC4 registry; (2) governance in dependency order — KC5 status → KC6 gate → KC7 barrier →
  KC8 confirm-by-layer → KC9 render-gate → KC10 one-job → KC11 provenance; (3) engine invariants resting on all of
  it — KC12 thin-attach, KC13 anti-fragility, KC14 cold-start + journey-proof LAST.
- **HARD ORDERING RULE:** the lifecycle + gate + writer-barrier + the binding journey proof (KC5/KC6/KC7/KC14) must
  all be green BEFORE any TIER-3 domain content is allowed to reach ACTIVE — WA-K10 makes the real
  SEED→PROPOSED→ACTIVE journey proof a binding precondition before any domain runs.

## §KERNEL-CONTRACTS (Step 1 Declare; consumer-driven; producer = g-health-core kernel for ALL; HOW → KP/P)
Each: consumer · flow (behavioral, firewall-clean) · direction · trigger · build-order · §KW rows · WA-K · KP/P.

### A. RUNTIME PRIMITIVES
- **KC1 — single router / procedure-interpreter (sole entry).** consumer: every domain (each turn). flow: every turn
  reaches output or runs a procedure ONLY after the one interpreter resolves WHICH domain is active (KD1), then
  resolves the current state from the cursor against the state-machine, then dispatches to exactly the procedure that
  state authorizes; it carries no domain computation, touches no output-heavy artifact, runs a preflight reject-set
  that FAILS CLOSED before classifying the message; a turn that outputs/runs without passing it is illegal; no domain
  stands up a second dispatcher; **a procedure may emit an owner QUESTION only for an irreducible owner_fact —
  asking an expert variable is preflight-rejected (KD2/FM1 ask-guard).** direction: domain turn → interpreter →
  dispatched procedure (one-way). trigger: startup / unresolved-state owner message / workflow write or checkpoint; a
  provider switch is a fresh turn re-resolving from the committed cursor; never self-firing. build-order: TIER-2, first
  runtime primitive. §KW: KR1–KR8,KR10,KR12,KR13,KD1,**KD2**. WA-K: WA-K1, WA-K11. KP: KP3 boot-sequence, KP12
  domain-signal, KP2 guard-predicate (preflight), P25 thin-index.
- **KC2 — working-state cursor (non-authoritative execution position).** consumer: every domain (one cursor instance
  per domain-per-procedure in its own namespace; never reads another's). flow: holds ONLY the in-progress execution
  position (active machine id, current node, the single open job/card, awaited owner input, transient scratch) and
  NEVER derived numbers/prescriptions/metrics/owner-facing content; non-authoritative + transient (loss+rebuild loses
  no owner-facing content, re-derivable from durable artifacts + handoff); is the file-form of one-chat-one-job;
  advanced only when the one interpreter is triggered; carries a grammar-version leaf, forward-migrates on touch;
  EXEMPT from confirm-before-save as a non-content control file. direction: interpreter reads then advances; durable
  artifacts + handoff re-seed on cold resume (one-way control file, never authority). trigger: opened on a multi-turn
  procedure start; advanced only on trigger; retired to provenance at a terminal state. build-order: TIER-2 co-primitive
  with KC1. §KW: KM1–KM11. WA-K: WA-K11, WA-K2. KP: KP1 cursor path/name/token, KP2 cursor shape, P23 schema_version
  (CA8 inherited).
- **KC3 — state-machine (static DEFINITION graph + mutable CURSOR split).** consumer: every domain (one machine
  instance). flow: the pair definition-graph + cursor in SEPARATE carriers so a cursor in a state confers no authority
  on what that state would produce; each state authorizes exactly ONE output family (or an owner-question, or a
  logging block) and forbids the rest; each transition has a guard preflight that must pass AND whose upstream artifact
  must be ACTIVE before the cursor advances; each state declares allowed_next_states, non-adjacent jumps rejected; the
  blocked/owner-input flag is a NON-BLOCKING pause (graceful revisable default on no-answer, safety brakes excepted);
  only the one interpreter advances the cursor; a state gates which family may become PROPOSED/ACTIVE; the DEFINITION
  itself (stage ordering + allowed-transition set) is an OWNER-APPROVED ACTIVE artifact riding the gate. direction:
  definition (authority for legal) constrains → interpreter advances cursor within it; the definition is published to
  the domain as a gate-bound ACTIVE artifact. trigger: consulted every turn (state resolution); the definition
  transitions only through the owner-approval gate. build-order: TIER-2 grammar co-primitive; a domain's instance is
  TIER-3 and rides the gate. §KW: KS1–KS10. WA-K: WA-K12, WA-K6. KP: KP2 def+cursor shapes + guard language + per-domain
  state/edge/family enum & labels, P11 phase enum.
- **KC4 — procedure registry (term = one bounded procedure).** consumer: every domain (appends its own entries; the
  interpreter AND the writer-applier both key off it). flow: each executable term binds to EXACTLY one bounded
  procedure (one responsibility = the one-chat-one-job boundary); an entry binds the typed tuple
  term→procedure-file + trigger + scope + stop + valid-state(s) + writable-artifact-family + writable-status +
  approval-class; the interpreter resolves term→procedure SOLELY by registry lookup, never folder/location; the entry
  binds which state(s) a procedure is valid in (the registry×state-machine join) and which family + which MAX lifecycle
  status it may write (an authoring procedure is bound to write only PROPOSED, never ACTIVE — KG4); the trigger
  value-domain is the closed set {owner, chat-turn, checkpoint}, so a cron trigger is unregisterable; a global entry is
  distinguished from a namespaced domain entry (may bind only its own targets); a new domain/procedure is added by
  APPENDING an entry, zero edit to any core file or other entry; each entry carries an approval-class
  {confirm-before-save | decide-and-inform}. direction: domain appends → interpreter + writer-applier read (one-way,
  data-driven). trigger: read on every dispatch + every persist; appended on authoring (triggered). build-order: TIER-2
  co-primitive with KC1; consumed by KC6/KC7. §KW: KG1–KG9, KR10. WA-K: WA-K9, WA-K1. KP: KP4 registry-line grammar,
  P19 procedure-definition template, P20 registry path + folder structure.

### B. GOVERNANCE LIFECYCLE (every domain inherits)
- **KC5 — content-authority lifecycle status property.** consumer: every owner-facing artifact in every domain. flow:
  every owner-facing artifact carries a mandatory `status` on SEED→PROPOSED→ACTIVE→SUPERSEDED; only ACTIVE is
  authority; authority is a per-artifact property, NEVER folder/location; ≤1 ACTIVE per family; single-hop SEED→ACTIVE
  and PROPOSED→ACTIVE-without-approval forbidden; AI-authored owner-facing content always lands PROPOSED (never
  directly ACTIVE), while low-stakes daily log entries stay decide-and-inform. direction: kernel defines the lifecycle
  → every domain artifact inherits the property + legal transitions (one-way). trigger: on author or status-transition
  attempt. build-order: TIER-2, FIRST governance primitive (before gate/barrier/any domain ACTIVE content). §KW: KV1,
  KV2, KV3. WA-K: WA-K4. KP: KP5 approval-marker (the ACTIVE-marker the property is checked against).
- **KC6 — owner-approval gate / no-role-both.** consumer: every domain (any authoring procedure). flow: an
  AI-authoring procedure may write only PROPOSED; PROPOSED→ACTIVE only on the owner's explicit echoed words scoped to a
  named artifact + version + date, ONE artifact at a time; silence/timeout never promotes and a bare "да" is not valid
  approval; no single role both authors content AND activates it; **approval granularity is two-tier — program/cycle
  individually, derived renders one packet at a time, never one blanket gate (KV7/F6); the approval marker
  (owner_approved/approved_words) is MANDATORY on any ACTIVE artifact and materiality-checked (KV6, the FM11 bite;
  schema→KP5).** direction: owner approval is the only inbound flipping PROPOSED→ACTIVE; the gate rejects any other
  path (one-way). trigger: on an attempted PROPOSED→ACTIVE; never time-driven. build-order: TIER-2, after KC5, before
  KC7 + any domain ACTIVE artifact. §KW: KV4, KV5, KV17, KG4, **KV6, KV7**. WA-K: WA-K3. KP: KP5 approval-marker
  schema + materiality-check.
- **KC7 — writer-applier barrier + evidence-of-transition.** consumer: every domain (every durable status flip). flow:
  persistence of an ACTIVE flip happens in a SEPARATE writer-phase distinct from the proposing chat; the reject-set
  refuses any ACTIVE-targeted write lacking owner-approval OR evidence-of-transition, plus skip-hop,
  render-before-decision, safety-fact deletion, sourceless-or-stale claim, multi-job bundle, out-of-scope target;
  evidence-of-transition = commit + diff + re-read, refuted OUTSIDE the producing chat; an irreducible owner safety
  fact is AI-non-deletable and a before/after preservation check FAILS if any disappears without an owner-resolution
  record; **an ACTIVE material claim must cite a repo-backed source with a freshness marker, fail-closed if missing or
  stale (KV12; threshold→KP8).** direction: proposed-and-approved content → writer-phase persists with the barrier;
  rejects back to the producing turn (one-way). trigger: when an approved transition is to be persisted; refutation in
  a separate session. build-order: TIER-2, after KC6, before any domain ACTIVE content. §KW: KV10, KV11, KV17, KV18,
  KV19, KD4, **KV12**. WA-K: WA-K5. KP: KP6 evidence mechanism per provider, KP5 materiality-check, KP10 partial-write
  atomicity, KP8 freshness threshold.
- **KC8 — confirm-by-layer dispatch + readable-for-owner.** consumer: every domain (procedures dispatched by stakes).
  flow: the kernel dispatches by stakes on the axis authoring-vs-adjustment: first-time authored owner-facing content +
  any SEED/PROPOSED→ACTIVE flip present a readable "result + what will be saved" (NEVER raw writer/YAML files) and
  persist only after the owner's explicit confirmation; daily logging AND review-driven adjustments of already-ACTIVE
  anchors stay decide-and-inform; confirm-before-save begins as strict initial scaffolding with an explicit later relax
  path, taken only by a separate owner decision after N proven error-free passes, never by timer or silently. direction:
  kernel classifies each procedure by stakes → confirm-gated or decide-and-inform handling (one-way at dispatch).
  trigger: at dispatch, every turn. build-order: TIER-2, atop KC6 + KC4 approval-class, before any domain authoring.
  §KW: KV20, KV21, KV-B2, KR11, KG9. WA-K: WA-K2. KP: KP11 relax-trigger N, KP4 approval-class field.
- **KC9 — render-before-decision gate.** consumer: every domain (any downstream projection). flow: a downstream
  projection becomes PROPOSED/ACTIVE only after its upstream program + cycle are ACTIVE, each carrying a justification
  chain; enforced at DISPATCH (the state gates which family may become PROPOSED/ACTIVE) AND re-validated by the writer
  AT WRITE TIME (upstream re-checked ACTIVE at write, not only at dispatch); **the gate-vs-derive partition is a kernel
  property: authored families are gated, a derived family (e.g. grocery from ACTIVE menu+base-prep) is DERIVED and
  must-not-lie, never separately approved (KV8/F5; the concrete per-domain family list belongs to the domain layer).**
  direction: upstream ACTIVE status authorizes → the downstream projection may be proposed/activated; blocked otherwise
  (one-way precedence, dispatch + write). trigger: at dispatch when a projection-family procedure is selected, and
  re-checked at write. build-order: TIER-2, atop KC3 (KS8) + KC5/KC7, before any domain projection reaches ACTIVE. §KW:
  KV9, KS8, KL4, KD5, **KV8**. WA-K: WA-K6. KP: KP2 guard-predicate (upstream-ACTIVE preflight).
- **KC10 — one-chat-one-job + handoff packet.** consumer: every domain (each job). flow: a job = one bounded
  deliverable from a closed job-type enum; a non-logging job with >1 content family is writer-rejected; the one
  same-state logging exception is a logging block with ≤1 clarifier and no content artifact; every router turn returns
  current-state + why + what-is-blocked + exactly ONE bounded output/question/action + owner-input-needed + next card,
  and >1 state or unauthorized content is invalid; every job closes with a mandatory handoff packet (outcome+status,
  evidence-of-transition, owner-approval status, single next card) from which the next chat opens. direction: kernel
  bounds each job and emits the handoff → next chat opens from it (one-way continuity). trigger: every router turn and
  job close. build-order: TIER-2, atop KC1 (one-output) + KC7 (multi-family reject). §KW: KR9, KV15, KV16. WA-K: WA-K7.
  KP: KP9 handoff-packet schema.
- **KC11 — provenance space + supersede retention + re-import-via-gate.** consumer: every domain (SEED/evidence/
  superseded artifacts). flow: SEED, evidence, prototype, superseded artifacts live in a namespace-distinct PROVENANCE
  space, non-authoritative by the status property regardless of location; a full PROPOSED draft is visible there
  pre-approval; a SUPERSEDED artifact is retained (not hard-deleted); reuse OUT of provenance only by re-import through
  the owner-approval gate; deletion of genuinely dirty files is a separate later cleanup job. direction: non-authority
  artifacts → provenance namespace; reuse flows back only through the gate (one-way out, gated back in). trigger: on
  supersession or seed/evidence creation; on a reuse attempt. build-order: TIER-2, atop KC5 + KC6. §KW: KV13, KV14,
  KA7. WA-K: WA-K4. KP: KP7 provenance-space path/layout.

### C. ENGINE INVARIANTS
- **KC12 — thin-domain attach meta-contract.** consumer: every domain (the exact shape to attach). flow: a domain is
  EXACTLY {namespaced data, one bounded procedure per term, one registry line, one state-machine instance in the kernel
  grammar} — and NOTHING else, ZERO engine code (no interpreter/router/lifecycle/cursor/registry of its own); the
  kernel owns the engine (the one router, the state-machine grammar, the registry mechanism, the governance
  lifecycle/gate/barrier, and the CORE-owned parse/library/value-grammar surface) and a domain may NEVER own or
  duplicate an engine part; a domain reads core concepts but never widens/mutates core schema and never writes another
  domain's namespace; it attaches via exactly one declarative registry line + one folder naming its namespace,
  state-machine-instance entry point, and procedure set; carries its own cursor instance advanced only by the kernel
  interpreter; training reuses the IDENTICAL kernel and never reads another domain's files; each domain stamps the
  inherited schema_version/forward-migration convention (CA8) and loads the determinism-load-bearing convention-carrier
  checklist (CA9). direction: kernel publishes the engine + attach shape → a domain conforms with only data/terms/
  ordering (one-way: engine down, never up). trigger: on domain attach + every turn that picks the domain up.
  build-order: TIER-2/3 boundary — the meta-contract is kernel-tier; a concrete domain is TIER-3 (either order after
  the kernel). §KW: KL1–KL10. WA-K: WA-K9, WA-K12. KP: KP4 registry grammar, P21 attach-point + x_key syntax, P20
  registry path/folders, P23 schema_version (CA8), P5 convention-carrier checklist (CA9).
- **KC13 — anti-fragility invariant (binding acceptance).** consumer: the whole multi-domain system. flow: removing
  any one domain (delete its folder + its one registry line) leaves the kernel + all other domains GREEN (every
  remaining derived number resolves, no dangling reference, no broken dispatch), and disabling/superseding one
  procedure leaves its siblings green; the atomic isolation unit is one procedure (fix = edit one file, replace = swap
  one), no edit to siblings or the router; a broken procedure FAILS CLOSED on its own job (no ACTIVE output, no partial
  cross-file write) rather than corrupting siblings/core; the router is data-driven off the registry and simply does
  not dispatch a removed procedure (graceful absence, not a halting error); a removed/superseded part moves to
  provenance (re-importable via the gate), never hard-deleted. direction: kernel containment + data-driven dispatch →
  each domain/procedure independently removable (one-way isolation property). trigger: asserted as a binding acceptance
  check (remove-a-domain / disable-a-procedure proof); enforced at runtime by fail-closed containment. build-order:
  TIER-2, rests on KC4 + KC7/KC11; a binding acceptance precondition before domains are trusted. §KW: KA1–KA6,KA8,KA9,
  KA10. WA-K: WA-K8. KP: KP4 registry/manifest + per-procedure schema + x_key grammar, P20 registry/folders.
- **KC14 — cold-start bootstrap + journey-proof precondition.** consumer: every domain (first run; the journey proof
  precedes any domain running). flow: the first run of a domain (no cursor yet) resolves to a fixed BOOTSTRAP state
  that authors the cursor + the state-machine instance THROUGH THE GATE as a durable repo artifact, with NO ad-hoc
  in-chat bootstrap; and a real end-to-end JOURNEY proof — one actual artifact walked SEED→PROPOSED→ACTIVE through the
  gate, carrying evidence-of-transition — is a binding acceptance precondition that must hold before any domain runs.
  direction: kernel bootstrap authors the first durable instance via the gate; the journey proof gates the whole kernel
  before any domain (one-way precondition). trigger: on a domain's first run (cursor absent); the journey proof is a
  one-time binding acceptance gate. build-order: TIER-2 LAST — depends on KC5/KC6/KC7 green so the journey can be
  walked; must pass before any TIER-3 domain reaches ACTIVE. §KW: KD3, KD1, KR4. WA-K: WA-K10. KP: KP3 boot-sequence,
  KP6 evidence mechanism, KP12 domain-signal (bootstrap of active-domain resolution). See KQ2 for the recursion
  resolution (kernel-owned universal bootstrap machine).

§CONTRACTS completeness (recomputed against the ACTUAL authored KC1–KC14 kw_rows after the adversarial completeness
pass bound 5 orphans — KV6/KV7→KC6, KV8→KC9, KV12→KC7, KD2→KC1): all 90 normative §KW rows
(KM1–11, KS1–10, KR1–13, KG1–9, KV1–21+KV-B2, KL1–10, KA1–10, KD1–5) have a contract home; ZERO orphans. WA-K1–K12
each carried by ≥1 contract. No HOW token in any flow.

## §KERNEL-ARCH (Step 3 Architect; refuted chains; ride PLAN as INPUT EVIDENCE only, never into done_when)
Emergent from the decomposition, recursive, on the risk line. ALL system-decided (research-and-decide) — **owner_gate_batch = []** (confirmed by two independent attackers; see §SIGNOFF).

**KQ1 — writer-applier LOCUS in a no-runtime single-LLM-per-chat system** (carrier of the ROOT defect FM10/FM11;
inherited by every domain). Options: (a) a fresh writer session/turn opening from the prior handoff packet, reading the
committed PROPOSED draft + owner_approved marker, performing the SEED/PROPOSED→ACTIVE flip + evidence — **SUPPORTED**;
(b) a headless one-shot invocation (claude -p / codex exec) — **SUPPORTED** (HOW-equivalent of (a): a separate
triggered context, → KP6); (c) a documented second PASS within the SAME chat — **REFUTED** (the activating context is
the authoring context → FM10/KS7/KV17/WA-K3; can't be "outside the producing chat" for KV11/WA-K5; = the rejected
nutrition defect); (d) owner commits — **REFUTED/struck** (KV18/F2 contradicts W4); (e) a background writer daemon/cron/
server — **REFUTED** (no-runtime: KR5 preflight, KG8 closed trigger set, W1/W2; breaks W8). **PICK:** the writer-applier
runs in a SEPARATE context from the authoring chat (fresh session OR headless one-shot — both satisfy the identical
signed WHAT: no-role-both + evidence-outside-producing-chat); the discriminating invariant is identity-of-context, and
the realization choice + per-provider evidence mechanics ride KP6/KP9/KP5/KP10. **new_owner_fork: NO** (F2 already
signed the owner-owned locus fork; only the firewalled HOW remains).

**KQ2 — cold-start bootstrap recursion** (a domain has no cursor/machine, yet B-3/KS10/WA-K12 require its DEFINITION to
be an owner-approved ACTIVE artifact authored VIA THE GATE — chicken-and-egg). Options: **O1 a kernel-owned UNIVERSAL
bootstrap state-machine** every domain implicitly starts in when no cursor/definition exists, whose sole authorized
output is the kernel procedure "author THIS domain's definition (+ initial cursor) as PROPOSED → owner gate → ACTIVE"
(the bootstrap machine + procedure are kernel engine parts inherited unchanged; domain identity + the PROPOSED
definition are DATA, never per-domain code) — **SUPPORTED/PICKED**; O2 domain authors its own bootstrap ad-hoc in-chat
— **REFUTED** (= FM3 verbatim, the original trust-collapse; proposer self-activates = FM10; no durable carrier / no
evidence WA-K5/WA-K10); O3 kernel HARDCODES each domain's machine — **REFUTED** (adding a domain edits a CORE file →
KA2/KG6/WA-K8/KL1 broken; remove leaves dead kernel branches; kernel grows O(#domains)); O4 a domain ships its
definition ACTIVE at attach with no journey — **REFUTED** (forbidden single-hop / PROPOSED→ACTIVE-without-approval
KV2/WA-K4; skips the gate KV4/KV5/B-3; no journey proof F8/WA-K10; FM5); O5 pre-seed an EMPTY ACTIVE machine per domain
— **REFUTED** (placeholder auto-promoted to ACTIVE = FM5/KV2; still needs a real bootstrap state → collapses to O1 or
O2). **Why O1 is forced:** KD3 system-locks the mechanism shape; KR10 (router/registry CORE-owned, inherited) +
KL1/WA-K9 (domain ships zero engine code) + KA6/WA-K8 + KA2/KG6 (add = 1 folder+1 line, remove leaves siblings green)
force ownership to "the kernel, once, universally." The first definition so produced — walked SEED→PROPOSED→ACTIVE with
evidence — IS the binding journey proof (F8/WA-K10). **new_owner_fork: NO.** HOW → KP2 (bootstrap def/edge), KP1
(cold-start detection on a file basis), KP4 (the bootstrap procedure's registry entry), KP5/KP6/KP9/KP10.

**KQ3 — governance lifecycle vs domain state-machine: SAME or ORTHOGONAL?** (conflation re-introduces FM5/FM6 — the
rejected slice). **PICK: ORTHOGONAL — two independent axes joined by ONE one-way seam.** Invariant **INV-ORTH:** the
DOMAIN state-machine (a per-domain ordering instance; its cursor advances stage→stage, each stage AUTHORIZING exactly
one family to be authored/PROPOSED) and the GOVERNANCE lifecycle (a per-ARTIFACT status leaf SEED→PROPOSED→ACTIVE→
SUPERSEDED) are orthogonal: cursor position NEVER sets/implies an artifact's status, and status NEVER moves the cursor;
reaching a stage UNLOCKS the right to PROPOSE that family, and only the owner gate (KV4) flips it ACTIVE. The SEAM is
one-way and read-only — render-before-decision: a downstream stage may produce a PROPOSED/ACTIVE artifact only after
its upstream stage's artifact carries status=ACTIVE (KS8 at dispatch, KV9 governance block, KD5 re-validated at write).
The two axes touch at exactly that ONE write-time guard, nowhere else. Refuted: ONE unified machine (stage-reached ==
ACTIVE → FM5/FM6 collapse); STATUS-encoded-by-stage-folder (FM12); a SHARED four-state alphabet for both (KL3/KS9
violation + FM5). This is the already-signed KS8↔KV9 pair re-validated by KD5 — converge-arch only NAMES it as the
single coupling point (= internal seam S5). **new_owner_fork: NO.**

**KQ-rev (miner gap-hunt) — DEFINITION-REVERSION vs IN-FLIGHT CURSOR.** The miner's mandatory "which question did we
NOT ask?": when a domain's state-machine DEFINITION (an owner-approved ACTIVE artifact, KS10/B-3) is legitimately
RE-VERSIONED (re-order / add / remove a stage), what is the fate of an in-flight cursor (KM1) sitting at a state the new
definition removed/renumbered? A real hole: KR4 covers cursor-vs-machine inconsistency-drift but NOT a previously-valid
cursor orphaned by a legitimate re-version; KM2/KM7 cover cursor LOSS but not a surviving cursor under a CHANGED
definition; CA8/W65–W67 migrate file-grammar field-SHAPE, a DISTINCT axis (the trap is conflating "migrate the file's
schema_version" with "re-map the cursor's semantic POSITION across a redefined graph"). Options: A auto-migrate (silent
best-effort re-map) — **REFUTED** (reconstructs position by inference → KR4; can fire a render against the wrong
upstream → FM5/FM6; content-bearing inference with no owner visibility → W4/KV21); B hard-block EVERY in-flight cursor
on ANY re-version — **REFUTED** (over-broad; a cursor parked at an untouched still-valid state is not in drift →
KA6/WA-K8/KS2; converts a blast-radius-bounded edit into a domain-wide halt); **C impact-classified, fail-closed
re-validation** — **PICKED:** a re-version (an owner-approved ACTIVE flip) triggers a KR4-style re-validation of every
in-flight cursor against the NEW definition; still-valid cursors proceed UNTOUCHED (WA-K8); an ORPHANED cursor (state
removed/renumbered / outgoing edge deleted) is treated as KR4 drift → BLOCK to one bounded repair that REBUILDS position
from durable artifacts + handoff (KM2/KM7), never a silent auto-map; a removed stage holding a KV19 owner-resolution
record surfaces in the repair, never silently dropped. **The block-and-rebuild SHAPE is system-locked** (KR4 + KM2/KM7
+ KA4/KA6).
- **WHO authors the rebuilt orphan-cursor position → FORCED to "system-proposes / owner-confirms" — system-locked, NO
  new owner gate.** The miner initially over-called this a new owner fork (KD6); TWO independent attackers
  (firewall + owner-fork) refuted that and the signed set forces it: KM11 (the cursor is a non-content control file,
  EXEMPT from confirm-before-save — rebuilding it is not authoring owner-facing content) · KV20 (a position-rebuild of
  an already-ACTIVE journey is an ADJUSTMENT, not first-time authoring → decide-and-inform side) · KV21 (the rebuild is
  a readable owner-confirmed step) · KS6 (graceful revisable default on no-answer) · W21/G7-2 (no re-pester — refutes
  "a fresh first-class owner decision per orphaned journey"). The "fold a migration-mapping table into the re-version
  approval" alternative is a HOW/mechanism choice (table FORMAT → PLAN), not an owner value-decision. **new_owner_fork:
  NO.**
- **PLAN residual (NOT minted into the signed agenda):** the orphan-detection predicate (state removed/renumbered/edge
  deleted), the re-validation trigger wiring, and the repair-presentation/mapping format ride existing **KP2**
  (guard-predicate language + per-domain state/edge enum) + **KP10** (the re-version flip and any cursor repair are TWO
  writes, artifact/status-first then cursor, per KD4). Whether a cursor detects its definition was re-versioned by
  reusing the existing schema_version, a new version leaf, or a content hash is wholly a PLAN/KP2 decision — stated
  here only as the behavioral WHAT (a cursor must be able to detect a newer definition than the one it last validated
  against). A dedicated PLAN slot may be cut at PLAN if warranted; it is NOT stamped into the owner-signed KP1–KP12
  here. The companion gap **KQ-concurrent** (two sessions opening the same domain cursor concurrently — largely
  absorbed by KM7 handoff-as-single-open-card-token + git-merge surfacing the conflict loudly; no owner fork) is
  flagged for a one-line PLAN note.

## §KP-ROUTING (every KP1–KP12 + reused data-layer P-slots routed to a contract/pick; firewall respected)
KP1 cursor path/name/token → KC2 · KP2 def+cursor shapes + guard language + per-domain state/edge/family enum → KC3
(+ KQ2 bootstrap def, KQ-rev orphan predicate) · KP3 boot-sequence index + load policy → KC1/KC14 (ties P25) · KP4
registry-line grammar → KC4/KC12/KC13 (ties P19/P20/P21) · KP5 approval-marker schema + materiality-check → KC6 (S4) ·
KP6 evidence-of-transition mechanism per provider → KC7 (+ KQ1 writer realization) · KP7 provenance-space path/layout →
KC11 · KP8 freshness threshold → KC7 (KV12) · KP9 handoff-packet schema → KC10 · KP10 partial-write atomicity → KC7
(S7; + KQ-rev repair) · KP11 relax-trigger N → KC8 (KV-B2) · KP12 domain-selection signal format → KC1 (KD1) · reused:
P20 registry path → KC4/KC12 · P21 attach-point + x_key → KC12 (reuses CA4) · P23 schema_version + migration → KC2/KC12
(reuses CA8) · P5 convention-carrier checklist → KC12 (reuses CA9) · P11 phase enum → KC3 (reuses data-layer) · P25
thin-index → KC1. No KP orphaned; no KP leaks into a WA-K/done_when line.

## §FIREWALL & §COVERAGE (mechanical; completeness rests on converge-verify, correctness on the owner gate)
- **Firewall: CLEAN.** Every contract flow + every seam flow states WHAT/DIRECTION/TRIGGER only; no file path/name,
  wire/serialization format, push-vs-poll, cadence/interval magnitude, grammar/syntax/regex, schema field-layout, or
  threshold value in any flow. Signed WHAT-language that LOOKS like HOW is not HOW: "YAML" (KC8) is verbatim from
  KV21/WA-K2; the closed trigger set {owner, chat-turn, checkpoint} is the signed value-domain KG8 (bounds what is
  registerable), not a cadence; "commit+diff+re-read" (KC7) and "echoed-words+named-artifact+version+date" (KC6) are
  the signed acceptance content WA-K3/WA-K5 (marker schema→KP5, mechanism→KP6); "N proven passes" (KC8) is a behavioral
  relax condition (value→KP11). The 4 architecture picks keep the PICK at behavioral WHAT and fence mechanism tokens
  (claude -p / codex exec; file shapes; mapping-table format) to KP slots as input evidence; NONE leaks into a done_when
  line.
- **Coverage:** all 90 normative §KW rows → a KC1–KC14 home (5 orphans bound: KV6/KV7→KC6, KV8→KC9, KV12→KC7, KD2→KC1).
  WA-K1–K12 each carried. Every TREE interaction = the kernel→all-domains inheritance surface (uniform), plus the
  data-layer cross-node CA1–CA9 reused unchanged; no dangling consumed contract (every consumer is a parked/future
  domain inheriting the kernel; the kernel is the producer, built TIER-2 first).
- **arch_open: 0** (KQ1–KQ3 + KQ-rev closed; gap-hunt done). **arch_in_context_only: PASS** (no pick in any done_when;
  all ride PLAN). **contract_coverage: PASS.**

## §SIGNOFF — converge-arch (Declare + Architect)
status: **CLOSED, no new owner decision (owner_gate_batch = [])** — session s-health-core-kernel-converge-arch-001,
2026-06-20. The 14 engine-inheritance contracts KC1–KC14 + 7 internal seams S1–S7 are declared consumer-driven with
build-order deps; firewall clean; the KP1–KP12 routing recorded; coverage vs the §KW rows complete (5 orphan rows
bound after the adversarial completeness pass). All 4 architecture picks (KQ1 writer-locus, KQ2 cold-start bootstrap,
KQ3 lifecycle/state-machine orthogonality, KQ-rev definition-reversion) are SYSTEM-DECIDED (research-and-decide),
forced by already-signed rows; the miner's one over-called owner fork (KD6) was demoted to a system-locked pick by two
independent attackers (KM11 + KV20 + KV21 + KS6 + W21 force "system-proposes/owner-confirms"). Relitigation guard:
CLEAN — no signed §KW/§WA-K/§OWNER-DECISION (Package A F1–F16 + B-1..B-4) row contradicted; no daemon/cron/server
introduced; owner never hand-edits; provider-independence intact. Owner gates spent across the kernel converge set:
**2** (Define "Пакет A" + Resolve/forks "по рекомендациям") — converge-arch adds none, matching the data-layer
converge-arch zero-new-gate precedent. → next = **converge-verify** (a SEPARATE refutation session: independent oracle
attacks completeness + traces every weight-bearing value; only a clean verify reaches shape).

## §ROUTE
next → **converge-verify** (c-health-core-kernel-converge-verify-001): refute this §KERNEL-CONTRACTS + §KERNEL-ARCH set
in a fresh session (completeness vs §KW + WA-K; firewall re-sweep; build-order non-dangling; no pick leaked to
done_when; the 5 just-bound orphan rows verified homed; the KQ-rev system-locked demotion re-refuted). A clean verify
→ **shape** (shape copies §WA-K1–K12 verbatim into the executor done_when (G5), carries §KERNEL-CONTRACTS KC1–KC14 +
§ARCH picks as architecture-on-paper input evidence, and the KP1–KP12 agenda as PLAN input; shape may split into the
parked domain child nodes, each re-entering TRIAGE).

END_OF_FILE: live/health/work/converge-g-health-core-kernel-arch.md
