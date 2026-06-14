# Play: converge-arch

Purpose: close the cross-node CONTRACTS a converged node consumes or produces, and — heavy node only — work its high-risk architecture as a refuted chain into an architecture-on-paper that rides PLAN as input evidence, never into done_when. No gate touched; closure refuted by converge-verify before shape.

Reads: work/converge-<node>.md (closed §GLOSSARY/§WHAT), TREE.md, NOW.md, knowledge/contract-*, sibling canon.
Writes: work/converge-<node>.md (§CONTRACTS) and, heavy, work/converge-<node>-arch.md; NOW.md (open_calls, decisions); LOG.md. Proposes contract canon for review/pulse; never writes knowledge/.

Precondition: converge WHAT spec closed (converge done) AND node is sibling-bearing (→ DECLARE) or heavy (→ DECLARE + DECOMPOSE + ARCHITECT). Reached via CALL `to: session, play: converge-arch`.

## Steps

1. **Declare** — for any node consuming-from / producing-for a sibling, freeze a CONSUMER-DRIVEN contract before build. §CONTRACTS: the consumer states what data/events/topology flow, which direction, on what triggering event — behavioral, e.g. "gas-sim requires from grid: changed cells + new adjacency, whenever topology changes." HOW (push-vs-poll, wire format, cadence, layout) is NOT in the contract → `→ PLAN`. Completeness pass CHECKED AGAINST THE TREE: name every node this node's outputs touch or whose outputs it reads. A consumed contract whose producer node does not exist yet → an explicit build-order dependency (producer converges FIRST), never dropped. Changing a contract a built sibling depends on is an explicit ADDED/MODIFIED/REMOVED delta. Sign contracts (G7). Propose two-sided contract canon (read_by names both nodes).

2. **Decompose** (heavy) — sketch the node into sub-systems; decide which become sub-nodes (each re-enters TRIAGE via converge). Internal seams → internal contracts in §CONTRACTS (WHAT side; HOW stays `→ PLAN`).

3. **Architect** (heavy) — work each HIGH-RISK architecture question through the WHAT loop: surface → dependencies → `call:research` strategic_search (3–5 refuted options) → owner-signed pick. Multiplayer / determinism / scale are SCORING CRITERIA that mechanically reject failing options (a float solver fails a deterministic integer core). Questions are EMERGENT (born from the decomposition sketch) and RECURSIVE (one pick spawns the next: tiering → seam → per-tier representation). RISK LINE: only high-risk / shape-defining / costly-to-reverse decisions are worked here; low-risk (buffer layout, byte format) stays `→ PLAN`. One miner gap-hunt: "which architecture question did we NOT ask?" Record per question a refuted table + signed pick in work/converge-<node>-arch.md. Sign picks (G7).

4. **Close & route** — verify closure (below). Architecture-on-paper rides the executor CALL's `context` as INPUT EVIDENCE only — PLAN commits the binding ADR; if the paper-best fails in code, PLAN escalates back. Emit play_check `contract_coverage: every TREE interaction → a §CONTRACTS entry`, `arch_open: 0`, `arch_in_context_only: PASS` (no pick in done_when). `next` = converge-verify (then shape; shape may split into child nodes per its split rule / G9, each re-entering TRIAGE).

## Done when
§CONTRACTS: every TREE-checked interaction has an entry; no consumed contract dangles (producer named, even if unbuilt); no line cites an open §WHAT/term; no HOW token (push/poll/format/cadence) — those are `→ PLAN`. Heavy: zero open high-risk architecture questions; every pick has a refuted comparison + signed recommendation; seams recorded as contracts; no architecture-on-paper leaked into done_when (`context`-only). `§SIGNOFF` exists for Declare and (heavy) Architect. Set handed to converge-verify before shape.

## Notes
- Owner asks fold into the converge set's three-batch G7 limit: Declare's contract sign-off and (heavy) the architecture picks — never scattered.
- Contract-order trap: a consumer (gas) may reference an unconverged producer (grid). Either converge the producer FIRST, or record an owner-confirmed dangling dependency the producer's later converge consumes unchanged.
- HONEST: the layer gives a researched recommendation; PLAN owns the binding ADR. The firewall keeps architecture-on-paper out of done_when — only WHAT acceptance criteria + contract requirements are copied there by shape.

END_OF_FILE: os/plays/converge-arch.md
