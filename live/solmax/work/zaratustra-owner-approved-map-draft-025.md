# Zaratustra — owner-approved map draft

Status: **OWNER-APPROVED CHECKPOINT DRAFT; NOT YET LIVE TREE AUTHORITY**

Approved: 2026-08-12
Parent: `g-zara`
Required before apply: fresh `map_evidence` and returning `map` leg

This file preserves the exact substantive map approved by the owner. The
returning map leg may make only source-backed corrections required by fresh
evidence. Any material correction returns to the owner; no contradiction means
apply this map without asking him to approve the same content again.

## Shared architecture boundary

The product vocabulary is:

```text
Area
├─ Capabilities
│  └─ typed Operations
├─ Workflows
├─ shared State / Policy / Projections
└─ Workflow Runs
   └─ Steps / Events / Results
```

There is no top-level runtime entity named `Process`. A workflow is one
bounded multi-step scenario; a run is one execution of a versioned workflow.
An Area is the long-lived bounded domain owning its vocabulary, state, policy,
privacy boundary, capabilities and projections.

Load-bearing invariants for every node:

1. Free prose is an opaque payload to deterministic code. Python may validate
   only predefined structured fields, exact identifiers, enums, references,
   ranges, sizes, transitions, permissions and effect tiers. It never uses
   regex, keywords, headings, substring search or heuristics to infer meaning,
   routing, success, evidence, authority or state from prose.
2. A human or another model may understand or grade prose. A model returns its
   semantic judgment as a separately typed object; Python validates that
   object's schema and concrete values, not the prose or explanation.
3. There is no custom procedure language, prompt compiler or interpreter.
   Workflows have explicit registered handlers. Metadata exists for contracts,
   validation, routing, visualization and observability, not as a home-grown
   executable DSL.
4. The local web UI is a first-class owner interface from node 1. It reads
   typed owner projections through an explicit local interface; it does not
   scan folders or parse prose for state. Markdown may be rendered as an opaque
   artifact. The primary UI is simple, visual, owner-readable and hides raw
   ids/technical metadata behind optional details.
5. The web server is localhost-only by default, read-first, without external
   analytics. Commands and writes, when later allowed, use the same typed
   authority/effect contracts as every other surface.
6. A logical Area does not imply one repository, service or database. Physical
   storage is a replaceable binding chosen from evidence, not frozen by this
   map.
7. Old Health Reclamation is requirements/evidence/migration source only. Its
   Markdown, runtime, state and M2/M3 labels do not automatically become a
   Zaratustra Area, capability, workflow or authoritative state.

## 1. `g-zara-health-vertical` — first useful and visible Health slice

### goal

The owner can use a local Zaratustra web interface to run one genuinely useful
multi-step Health workflow built on explicit Area, Capability, Operation,
Workflow and Run contracts, with qualified execution, observable steps and no
implicit dependence on the legacy Health runtime.

### done_when

1. Minimal versioned contracts exist for Area, Capability, Operation,
   Workflow, Step, Run, state transition, effect, artifact, owner projection
   and trace event; each has a stable identity and machine-validated fields.
2. A new Health Area, one bounded Health Capability and one useful multi-step
   Workflow are implemented on those contracts. The legacy Health material is
   cited as evidence only; no folder or Markdown import silently grants
   runtime or state authority.
3. Every step declares typed input/output, required/optional context refs,
   allowed effects and writes, possible next transitions, executor
   requirements and closure states. Missing/ambiguous/unauthorized input fails
   closed rather than being inferred from prose.
4. At least one real subscription/local/cloud executor path runs through a
   registered adapter. The owner sees target Area/Capability/Workflow,
   recommended model+provider+access mode, reason, alternatives and exact
   owner action.
5. Eval Harness contains versioned normal, edge and adversarial cases; exact
   contracts use deterministic tests, semantic prose is judged only by owner
   or model returning typed verdicts, and step/end-to-end traces are graded.
6. A localhost web UI shows a simple home view, Health view, Workflow graph,
   current Run/step, pending owner action and concise eval/trace status from
   typed projections. No central page parses free text or knows Health-specific
   folder layout.
7. The owner completes at least three real low-consequence runs; at least one
   is explicitly useful, and every other run ends in honest success, bounded
   owner question, diagnostic block or recoverable failure.
8. A fresh separate refutation checks the contracts, opaque-prose invariant,
   privacy/effects, eval evidence, web projection and real-use claim.

### why

This creates first real use, tests depth beyond plain chat and proves the
smallest extensible kernel with visible owner value. It directly advances all
three Zaratustra success criteria rather than producing another abstract core.

### edge

The owner has a real previously used Health scenario, rich positive/negative
evidence, ten years of engineering experience, paid model subscriptions and a
working Direction OS build harness. The slice can therefore be tested against
his actual work instead of invented demos, while old artifacts remain evidence
rather than authority.

### risk

Interfaces, evals or the web shell could become the product while the Health
workflow remains useless. Revisit the cut if three real runs yield no useful
result, if the UI/metadata work grows faster than the vertical workflow, or if
the legacy process is being wrapped rather than explicitly re-authored.

## 2. `g-zara-trusted-context-state` — trusted context and portable state

### goal

A fresh run or different qualified executor receives exactly the permitted,
current and provenance-bearing context it needs and can resume useful work
without the previous transcript or automatic loading of unrelated history.

### done_when

1. Each Area/Capability/Workflow declares required and optional sources,
   freshness, sensitivity, size budget and read/write authority.
2. Context is assembled only from explicit typed references; whole history,
   archives, neighboring Areas and personal data never enter "just in case".
3. Every included datum records source, version/hash, acquisition time,
   privacy class and reason for inclusion; the owner can see why a model saw it.
4. Facts, decisions, statuses, references and transitions are structured;
   notes and model outputs remain opaque artifacts and are never mined by
   Python into facts.
5. One authoritative owner exists for each fact. Other capabilities/Areas use
   typed references or projections rather than divergent copies.
6. A fresh run resumes from a versioned continuation without prior chat and
   does not present stale/incompatible context as current.
7. Tests cover missing required source, stale data, forbidden source, changed
   reference, budget overflow, conflicting versions and read-only boundary.
8. The web UI shows state/provenance/continuation in owner language through
   projections, not direct database or filesystem interpretation.

### why

Trustworthy continuity is what turns isolated model calls into a personalized
exocortex and enables depth across Areas without contaminating contexts.

### edge

The owner already operates several real Git-backed processes and understands
contracts, provenance and audit. Those give unusually strong test material for
selective context and recovery.

### risk

Provenance machinery may add more burden than manual file selection. Revisit
if real runs still require the owner to assemble most context or the projection
is less understandable than a small explicit file set.

## 3. `g-zara-model-qualification-routing` — qualified economical routing

### goal

For each typed operation/workflow, Zaratustra recommends and uses the least
expensive available model-provider-access combination that has demonstrated
the required quality, tools, privacy and safety for that exact configuration.

### done_when

1. The executor registry separates model family, concrete variant/snapshot,
   provider, access mode (`local | subscription | cloud_api`), runtime/adapter,
   tools, context limits, privacy, effects, availability, quota and cost.
2. Eval results qualify an exact combination of procedure/workflow version,
   prompt/instruction version, model/provider/access, adapter, tools and
   context policy; there is no global "best model" rating.
3. Routing uses only typed requirements and qualification records, never
   Python interpretation of the payload prose.
4. Selection order is privacy/safety, required capabilities/quality, then
   cost/quota/latency. Fallback is pre-authorized or explicitly asks/blocks;
   no silent provider substitution occurs.
5. At least two real access paths work, including a paid subscription path;
   local and multiple cloud/API/subscription providers (including Qwen-family
   offerings) are representable without kernel changes.
6. The owner can override a recommendation only with another qualified
   option; an unqualified combination gives a plain explanation and evidence
   link.
7. Material change of workflow, instruction, adapter, tool set or model
   snapshot invalidates the affected qualification until rerun.
8. The web view explains recommendations and alternatives in owner language
   and exposes the supporting benchmark on demand.

### why

This sends simple work to local/cheap models, reserves frontier subscriptions
for hard planning and makes model switching measurable without weakening
privacy or results.

### edge

The owner already has real repetitive workloads and several subscriptions;
qualification can use his tasks rather than public leaderboards that ignore
his tools, files and rules.

### risk

Maintaining benchmarks may cost more than routing saves. If qualification does
not change real choices after several workflows, reduce it to a manually
maintained allowed/recommended list with regression gates.

## 4. `g-zara-extensible-areas-workflows` — extension without core redesign

### goal

New Areas, Capabilities, Operations and Workflows can be developed, tested,
owner-approved and registered without changing central routing, authority,
trace or web-navigation semantics.

### done_when

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

### why

This is the mechanical proof behind the root extensibility criterion: the Nth
capability is registration plus handler and tests, not another kernel rewrite.

### edge

The owner already has several materially different domains and Workflow 2 as
requirements/negative evidence, so extensibility can be tested against real
differences rather than toy plugins.

### risk

A universal factory may reappear before useful Areas exist. If onboarding one
addition needs more platform code than domain work, keep a manual explicit
package template and return to dogfood.

## 5. `g-zara-daily-owner-use` — everyday control and demonstrated value

### goal

The local web UI becomes the owner's simple daily surface for starting,
understanding, handing off and resuming AI work, with recurring useful reliance
across at least three life/work Areas and one hard workflow clearly better than
a plain chat session.

### done_when

1. Home view emphasizes attention, pending decisions, active Areas/runs,
   blocks and recommended next action with minimal technical text.
2. Area, Workflow and Run views show simple status cards, graph/timeline,
   provenance, model recommendation, results and safe actions; raw technical
   data stays behind optional details.
3. At least two real ingress/execution surfaces interoperate through the same
   typed packets, including local UI/CLI and a subscription/web handoff or
   equivalent channel.
4. A packet can start in one surface, run in another and resume fresh without
   transcript reconstruction; duplicate message/run identity cannot duplicate
   an external effect.
5. The owner relies on Zaratustra recurringly in at least three distinct Areas
   of life/work.
6. The owner explicitly judges at least one real multi-step personalized
   workflow clearly better than a standalone ChatGPT/Claude session.
7. Evidence distinguishes useful result, honest block, manual context burden,
   repeated use, abandonment/return-to-chat, latency and resource use rather
   than counting raw launches.
8. UI mutations use typed commands and authority/effect checks; the projection
   layer never becomes a second state owner.

### why

This directly closes the charter's primary anti-perpetual-draft criterion and
the depth criterion; all earlier infrastructure is justified only if this node
becomes true.

### edge

The owner is the only user and already works daily across several AI surfaces,
so feedback is immediate and there is no audience-discovery dependency.

### risk

The UI and handoffs may add bureaucracy. If Zaratustra takes more steps than it
saves, automate the one proven high-friction transition or simplify the
projection instead of growing a universal portal.

## 6. `g-zara-governed-improvement` — governed self-improvement

### goal

Zaratustra can turn real failures and opportunities into researched,
implemented and benchmarked candidate changes while only the owner can approve
activation, authority expansion or rollback of an active version.

### done_when

1. A real trace/feedback item can create a typed ImprovementCandidate naming
   evidence, affected versions, hypothesis, expected effect, risk, budget,
   verification and rollback.
2. Models may analyze opaque artifacts and return typed findings; Python only
   validates fields/references and never mines prose.
3. Candidate changes remain isolated from active versions and cannot change
   process/workflow instructions, handlers, router, rights, eval thresholds or
   active state before owner approval.
4. Baseline and candidate are compared on regression, new problem and adverse
   cases, semantic owner/model verdicts, safety, latency and resource use.
5. Critical regression or unauthorized effect blocks the candidate even when
   the target case improves.
6. A fresh independent review presents a short owner decision: change,
   evidence, gains, losses, risks and recommendation.
7. Only the owner's exact verdict activates; previous version and evidence
   remain rollback-capable.
8. One complete cycle from a real problem reaches accepted improvement or
   justified rejection within a fixed attempt/budget ceiling.

### why

This enables evidence-gated compounding toward the exocortex vision without
hidden prompt mutation or self-expanded authority.

### edge

The owner's Direction OS already supplies working patterns for separate roles,
evidence, review and explicit verdicts, which can be adapted into a much smaller
product change loop.

### risk

The system may generate more proposals than value. If the review queue grows
or most candidates fail to improve real work, retain structured issue capture
but make improvement launches manual.

## Approved order and selection

1. `g-zara-health-vertical`
2. `g-zara-trusted-context-state`
3. `g-zara-model-qualification-routing`
4. `g-zara-extensible-areas-workflows`
5. `g-zara-daily-owner-use`
6. `g-zara-governed-improvement`

Dogfood begins in node 1. Node 5 proves recurring use across three Areas.
Governed improvement is last because it needs real failures rather than
synthetic optimization targets.

The owner selected node 1 as the first readiness route.

## Approved old-tree disposition

- Preserve `g-zara-operate-contract` as completed historical evidence.
- Mark unfinished `g-zara-operate`, `g-zara-operate-state`,
  `g-zara-operate-runtime` and `g-zara-operate-evolution` as dropped/superseded
  by this map; do not claim their done_when was met.
- Do not reactivate `g-operating-substrate-first-process-creator`.
- Do not change `g-operating-substrate` or promote Zaratustra implementation
  choices into substrate architecture.

END_OF_FILE: live/solmax/work/zaratustra-owner-approved-map-draft-025.md
