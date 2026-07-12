# CHARTER — solmax

## Mission

Build **Solmax** as an umbrella direction for owner-facing AI systems and
reusable operating architecture that help the owner think, act and run
complex stateful processes with deep personalization and evidence-gated
growth.

The first product/application branch is **Zaratusta** — a personal, deeply
personalized AI exocortex (second brain) that helps the owner think and act
with great depth across all aspects of life and work, growing toward the full
EXOCORTEX vision.

Zaratusta remains the first consumer, failure-case and evidence source for
Solmax. It is not the whole scope of Solmax.

The reusable **operating-substrate** route is a separate architecture/spec
effort for AI-led stateful owner/project processes. It is not a child task
inside Zaratusta and must proceed through owner-led architecture/spec
cartography before design or implementation.

The system is built incrementally by background AI agents under owner review.
Personal-first; turning any branch into a product/business is an open future
option, not an obligation.

## Success criteria

There is no deadline (owner). These are state-based definitions of "succeeded," not dates.

Placement note:
Current success criteria SC1-SC3 still measure the Zaratusta branch. The
operating-substrate branch success criteria are intentionally not invented in
this repair; they will be co-created through architecture/spec cartography.

1. **Real deep use** *(primary — the guard against the "perpetual core draft" failure)*
   - The owner regularly relies on Zaratusta in **at least 3 distinct areas** of life/work, where it gives deep, personalized help he would not otherwise have.
   - Measured by real recurring use, not by the number of features built.

2. **Proven extensibility** *(the core ambition)*
   - At least several live capabilities (orientation: ≥8) span **all four extension axes** — tool, channel, memory, process.
   - Each capability was added with **~zero kernel diff** (add the Nth capability = one registration + a handler, no kernel edit).

3. **Depth beyond a plain chat** *(the "mega-brain" bar)*
   - At least one real, hard process that the owner judges **clearly better** than a session in a plain ChatGPT/Claude — multi-step, personalized, and aware of his priorities.

Personal-vs-product is handled as a checkpoint in Constraints, not a success criterion, so success never forces a product outcome.

## Constraints

- **Build mode:** the system is built primarily by **background AI agents** (Codex / Claude Code) under owner review. Work is decomposed into **small, agent-buildable, independently-verifiable increments** with clear contracts/tests/done_when. The owner orchestrates and reviews in spare time; he does not hand-code large stretches.
- **Money:** new cash budget ≈ $0; the cognitive engine is the owner's **already-paid subscriptions, not the API**, until he explicitly decides otherwise. ⚠️ subscription `claude -p` draws a separate ~$20/mo Agent-SDK credit that silently halts when exhausted — the engine layer must budget and fail over.
- **Priority / do-no-harm:** this is the owner's **lowest-priority** direction. It must not steal time or attention from higher-priority directions (game, health). Solmax never preempts an active bet in a higher-priority direction.
- **Relationship to the OS:** Zaratusta may read the workflow-OS repo **read-only**, as one capability among many; it **never writes** to it. The OS remains a separate living system.
- **Anti-perpetual-draft (from the worst-failure):** the core stays **tiny and stable on purpose**. Effort goes to accreting real, used capabilities and to depth — not to endlessly re-architecting the kernel. Re-opening the kernel design needs an explicit reason (like a concept that is not casually reopened).
- **Personal-vs-product checkpoint:** if/when the system delivers real personal value, the owner makes an explicit decision whether to keep it personal or productize it. Until then it is personal.
- **Privacy / trust:** it holds the owner's whole-life data → local-first where possible, an auditable ledger, and **owner approval for irreversible / external / spend-incurring actions** (effect-tier gate).
- **New repo:** the product lives in a new repo, **Zaratusta**, separate from the OS.
- **Umbrella placement:** Zaratusta and reusable operating-substrate are
  sibling branches under Solmax. Current Zaratusta artifacts are evidence,
  not authority. No substrate implementation bet, product repo, test harness
  or Direction OS kernel change is activated by this placement repair.

## Lenses

1. **Extensibility** — every bet keeps the kernel tiny; capability is added by registration; "the Nth capability = ~0 kernel diff." Work that bloats the kernel is suspect.
2. **Real depth** — a capability must produce deep, personalized, multi-step help, not Q→A; the bar is "better than a plain ChatGPT/Claude session."
3. **Agent-buildability** — work decomposes into increments a background agent can build and that are verifiable (test / contract / done_when), because the owner builds via agents + review, not hands-on hours.
4. **Daily use / dogfood** — a capability counts only when actually used and helping (the guard against the perpetual-draft failure).
5. **Privacy / trust / safety** — least-surprise; owner approval for irreversible/external/spendy actions; local-first; auditable ledger.
6. **Cost discipline** — engine on subscriptions; the credit cliff and compute budget are first-class; no silent spend.

## Owner edges

1. **Ready design + a working OS prototype**
   - Proving fact: a worked ~2000-line EXOCORTEX concept and a live markdown kernel (LOG/history/plays/gates) that is already a partial realization of EXOCORTEX. A large head start on design.

2. **Enterprise engineering depth**
   - Proving fact: 10 years of professional software development (Java/full-stack) → architecture, ports, contracts, and event-log come naturally.

3. **Orchestration skill + paid subscriptions**
   - Proving fact: the owner already drives Codex / Claude Code as executors in his OS → he can build via background agents cheaply on subscriptions (exactly the build mode).

4. **OS as the build harness**
   - Proving fact: the Direction OS decomposes work into frame/map/shape/work/review with done_when evidence and gates, compensating for solo blind spots and keeping the kernel disciplined.

5. **Owner is the only user**
   - Proving fact: a perfect, immediate product feedback loop — no audience-discovery problem (unlike the game direction).

## Risk posture

**explore**

Rationale: no external stakes, no deadline, no money gate; the value is open-ended compounding, and over-controlling it would kill the compounding. Two hard guards remain: **anti-perpetual-draft** (SC1 + the dogfood lens) and **do-no-harm** to higher-priority directions.

## Outside view

Solo "build my own AGI / second brain / exocortex" projects have a very high abandonment / perpetual-tinkering base rate — most die as endless core refactors that are never actually used (exactly the owner's worst-failure). The few that compound win by (1) a tiny stable core plus capability accretion (VS Code, Home Assistant, Obsidian — extensible platforms that lasted years) and (2) being genuinely used from early on (tools-for-thought winners). Current analogues: OpenClaw (local-first multi-channel agent gateway), Letta/MemGPT (agent memory). Implication for sequencing: keep the kernel tiny and stable, ship capabilities that get used, and measure success by real use + accretion, not by core perfection — the RLK plan.

Reference cases used during frame:
- Personal second-brain / "my own AGI" abandonment base rate: perpetual core refactors that are never used.
- VS Code / Home Assistant / Obsidian: tiny stable core + plugin ecosystem → multi-year survival and accretion.
- OpenClaw: local-first multi-channel agent gateway (reference for the channel/body axis).
- Letta / MemGPT: agent memory as a first-class concern.
- Prior Solmax design workflows this session (wf_8570804a concept menu, wf_d1ea25b7 RLK core) supplied the engine/cost/landscape evidence.

## Canonical repos

- Direction state repo: `github.com/ainazemtsau/my_global_workflow` (this OS repo).
- Product/application repo: **Zaratusta** —
  `github.com/ainazemtsau/zaratusta`, locally `C:\projects\Zaratusta`.
  Zaratusta is the first Solmax consumer/failure-case/evidence source, not
  the whole scope of Solmax.
- Operating-substrate implementation repo:
  `github.com/ainazemtsau/solmax-operating-substrate`.
  The owner selected it on 2026-07-12 as the bounded bootstrap
  implementation surface for the reusable operating-substrate branch.
  Repository, layout, stack, tooling, serialization, runtime and topology
  choices made there remain implementation-specific and do not become
  substrate architecture. Zaratusta remains the first consumer,
  failure-case and evidence source rather than substrate authority.
- The Direction OS repo remains separate. Zaratusta may read it read-only as
  one capability among many; neither Zaratusta nor the operating-substrate
  route writes to it outside Direction OS writer procedure.

## Pre-mortem

This direction failed three years from now because one or more of the following happened.

### 1. Perpetual core draft (the worst-failure)

**Failure mode:** the kernel was re-architected endlessly; capabilities never accreted or got used.

**Mitigation:** SC1 (real use in ≥3 areas) + the dogfood lens + the anti-perpetual-draft constraint; re-opening the kernel needs an explicit reason.

**Kill_by candidate:** if, after the kernel exists, ~5 increments pass with kernel churn but **zero new actually-used capability**, freeze the kernel and put all effort into capability accretion (or reframe).

### 2. Time-sink that steals from priority directions

**Failure mode:** the low-priority direction became a rabbit hole; game and/or health slipped.

**Mitigation:** the do-no-harm constraint; built by background agents + spare-time review, not focus blocks; Solmax never preempts a higher-priority active bet.

**Kill_by candidate:** if game or health visibly slip because of Solmax, Solmax pauses.

### 3. Background agents produce slop / unverifiable mess

**Failure mode:** agents generated large unreviewable code; the owner could not keep up; quality rotted; kernel discipline was lost.

**Mitigation:** the agent-buildability lens — small increments with tests/contracts/done_when; the RLK "0-line kernel diff" acceptance test as a mechanical gate; increment size kept to the owner's review cadence.

**Accepted risk / kill:** if the review backlog grows faster than it is cleared, shrink the increment size or slow agent throughput.

### 4. Just another chat wrapper — depth never materialized

**Failure mode:** it answered Q→A; the promised deep, priority-aware, multi-step help never appeared; SC3 was never met.

**Mitigation:** the real-depth lens; SC3 explicit; the cognition loop (plug-in #1) designed for multi-step/personalized work; verify "better than a plain session" on a real task.

**Kill_by candidate:** if, after the cognition loop ships, it is not judged better than a plain session on any real task, redesign the loop rather than adding features.

### 5. Subscription economics / credit cliff killed regular use

**Failure mode:** the ~$20 Agent-SDK credit ran out and background runs silently stopped; or ToS friction.

**Mitigation:** the cost-discipline lens; the engine layer budgets + detect-and-fail-over to codex; deterministic work routed off-LLM; the API seam kept ready.

**Accepted risk:** the API funding decision may need to come earlier than hoped (an explicit checkpoint); state stays intact via the ledger.

### 6. Privacy breach / irreversible action / OS contamination

**Failure mode:** a capability sent/deleted/spent without approval, or leaked personal data; OR the read-only OS link wrote back and corrupted the live OS.

**Mitigation:** the effect-tier gate (tier-2 → owner approval); local-first; the auditable ledger; least-privilege; the OS link is hard read-only and tested, never the writer.

**Kill / stop trigger:** a single unreviewed irreversible action is a stop-and-audit trigger. Writing to the OS is forbidden, not an accepted risk.

### 7. Vision sprawl — chasing the full EXOCORTEX too early

**Failure mode:** Dream Lab / the learning loop / omnichannel were attempted before the core and basic capabilities were actually used.

**Mitigation:** wave discipline (W0→W3+); big-vision items only as plug-ins after the core is used; new ideas default to parked; map/shape cut lists.

**Kill_by candidate:** any shaped bet without a cut list is invalid (G6).

END_OF_FILE: live/solmax/CHARTER.md
