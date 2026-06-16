# converge-g-kernel — RLK W0 WHAT closure (RETROFIT)

> Status: RESOLVE pass. This retrofit imports the already owner-approved W0 kernel shape,
> decomposes each named mechanism into forced WHAT properties, and routes sibling-bearing
> contracts to `converge-arch` before `t-2` freezes the kernel API. The active bet,
> appetite, tasks, kill_by, and done_when are not rewritten here.

## Header — triage and import

```
triage: HEAVY — converge ON — because model? YES (g-kernel defines the product's
        extensibility model and a wrong stub is fatal) AND contract? YES (future engine,
        channel, surface, cognition, memory, and accretion nodes all consume these seams)
        AND decomposes? YES (registry / ledger / envelope / gate / seams).
mode:   RETROFIT — g-kernel is already active; import settled decisions from history
        as born-closed and only route the remaining sibling contracts forward.
imported_from:
        - live/solmax/CHARTER.md
        - live/solmax/TREE.md
        - live/solmax/NOW.md
        - live/solmax/history/s-frame-001.md
        - live/solmax/history/s-map-001.md
        - live/solmax/history/s-shape-001.md
        - live/solmax/history/2026-06-16-s-repair-kernel-t1-state.md
        - C:\projects\zaratusta-product acceptance scaffold at 18d74b1
miner:  in-session explorer pre-pass (read-only) found the surface-kind, approval,
        Store-vs-ledger, upcaster, and kernel-diff spots.
search: in-session researcher strategic_search favored opaque-payload microkernel:
        narrow ports, plugin-owned schemas, generic ledger/envelope/gate contracts.
next_movement: HEAVY + sibling-bearing -> converge-arch before converge-verify.
```

## Source keys

| key | source |
|---|---|
| S1 | `live/solmax/CHARTER.md` |
| S2 | `live/solmax/TREE.md` |
| S3 | `live/solmax/NOW.md` |
| S4 | `live/solmax/history/s-map-001.md` |
| S5 | `live/solmax/history/s-shape-001.md` |
| S6 | `live/solmax/history/2026-06-16-s-repair-kernel-t1-state.md` |
| S7 | `C:\projects\zaratusta-product\openspec\changes\w0-rlk\specs\rlk\spec.md` |
| S8 | `C:\projects\zaratusta-product\src\**\index.ts` W0 scaffold |
| S9 | `C:\projects\zaratusta-product\validation.config` / `REVIEW.md` / setup tests |

## §GLOSSARY — disputed terms

| id | term | meaning here | competing readings closed or routed |
|---|---|---|---|
| G:kernel | RLK kernel | Exactly five public parts; anything requiring a sixth part is a stop/review trigger. | "Useful assistant" vs extension substrate; W0 is substrate only. |
| G:kernel-diff | zero kernel diff | No edit to the five kernel module directories and no edit to the root public kernel barrel/API. Plugin registration, handler, and fixture/test files outside kernel may change. | S7 only says no `src/<kernel-part>/`; S3/S5 say no kernel edits. This pass tightens the mechanical reading. |
| G:capability | capability | A registered extension entry with stable id, kind token, handler reference, and bounded metadata. | Plugin catalog/router vs thin registry. W0 keeps thin registry; loading/routing is fixture/runtime HOW. |
| G:kind | capability kind | Extensible token. Current success axes are tool/channel/memory/process; owner-approved map also names future `surface`. | Closed TypeScript union vs extensible kind list. Closed union is rejected because it would force kernel edits. |
| G:handler | handler reference | Identifier/path/name that runtime fixtures can resolve; the ledger stores references, not executable code. | Executable code in ledger vs pure reference. Code-in-ledger is rejected. |
| G:ledger | append-only JSONL ledger | Durable ordered record stream; one JSON object per line; append-only; replay reads order back. | Raw event log vs memory/store. W0 is raw/audit substrate, not memory/RAG. |
| G:schema-version | schema_version | Per-record ledger schema version, with a current-version constant. | Global DB version vs record version. W0 record version is binding; global migration is later HOW. |
| G:upcaster | upcaster seam | Reserved callable path for version upgrade or typed no-path failure during replay. | Type-only placeholder vs full migration registry. W0 requires seam exposure, not migration framework. |
| G:envelope | typed CALL/RESULT envelope | Product-local execution packet: CALL carries goal/boundaries; RESULT correlates to CALL and carries outcome/evidence. | Direction OS packet/writer semantics. Rejected: product builders do not author OS CALLs. |
| G:boundary | boundary validator | Generic validator for envelope shape and W0 scope limits. | Required-fields-only vs scope enforcement. W0 needs both. |
| G:effect-tier | effect tier 0/1/2 | Classification of requested capability side effects, not of the kernel's own audit append. | Only "block tier 2" vs policy model. W0 keeps generic three-tier gate. |
| G:owner-approval | owner approval | Auditable reference attached to a tier-2 request and bound to that request's id/tier/description. | Any truthy boolean vs artifact reference. W0 may validate presence; later UX/provenance can deepen it. |
| G:engine | Engine seam | Fake/no-op model port in W0. Real Claude/Codex/API/subscription handling is parked to g-engine. | Real model adapter now vs seam only. Real adapter is cut. |
| G:store | Store seam | Port for append/replay access to local storage; JSONL ledger owns concrete record format. | Separate state subsystem vs port over ledger. Separate subsystem is rejected. |
| G:replay | replay | Reading ordered JSONL records to restore equivalent ordered records for W0 acceptance. | Full memory/projection rebuild. Projection contracts route to later nodes. |

## §WHAT-A — born-closed imports

| id | decided WHAT | status | source |
|---|---|---|---|
| I1 | W0 contains exactly five parts: Capability Registry, JSONL ledger, CALL/RESULT envelope + boundary validator, effect-tier gate, Engine + Store seams. | answered | S2, S3, S5, S7 |
| I2 | CI must prove third-plugin zero kernel diff, JSONL replay, and tier-2 rejection without owner approval. | answered | S2, S3, S5, S7 |
| I3 | W0 does not include real engine, channels, UI/surface, memory/RAG, deployment/auth, marketplace, OS read capability, or OS write path. | answered | S1, S3, S5, S9 |
| I4 | Engine in W0 is fake/no-op only; subscription/API/failover belongs to g-engine. | answered | S1, S2, S3, S5 |
| I5 | OS relation is future read-only capability; OS write is forbidden, not merely a tier-2 effect. | answered | S1, S2, S3 |
| I6 | Surface is owner-accepted as a future capability kind ("5th kind") and must not force kernel churn. | answered | S4, S2 |
| I7 | Product repo setup and acceptance scaffold exist; current scaffold is not final kernel implementation. | answered | S6, S7, S8, S9 |

## §WHAT-B — mechanism decomposition

| id | mechanism | forced WHAT property | status | cites |
|---|---|---|---|---|
| W1 | part count | Public kernel module set is exactly the five named parts. A sixth top-level kernel module fails W0. | answered | I1 |
| W2 | dependency boundary | Cross-module imports go through public `index.ts` surfaces; internal imports across kernel parts are violations. | answered | S9 |
| W3 | zero kernel diff | Third-plugin proof fails if any existing kernel module dir or root public kernel barrel/API changes. New plugin registration, handler, and fixture/test files outside kernel are allowed. | answered | G:kernel-diff, I2 |
| W4 | registry identity | Capability id is stable and unique. Duplicate ids fail deterministically; ids are not inferred from handler file names. | answered | G:capability |
| W5 | registry kind | `kind` is extensible data, not a closed kernel union. `surface` must be addable later without editing kernel code. | answered | G:kind, I6 |
| W6 | registry handler | Registry stores handler reference only. Plugin-owned schemas and executable handlers live outside kernel. | answered | G:handler |
| W7 | registry metadata | Any safety/boundary metadata is bounded data consumed generically; no policy DSL, per-plugin gate code, or router subsystem enters W0. | answered | G:capability, G:effect-tier |
| W8 | ledger append | Ledger writes one JSON object per line and never mutates earlier lines in place. | answered | G:ledger |
| W9 | ledger version | Every ledger record carries `schema_version`; W0 current version is explicit. | answered | G:schema-version |
| W10 | ledger payload | Kernel ledger accepts opaque payloads so plugin-specific event unions do not require kernel edits. | answered | G:ledger, G:kernel-diff |
| W11 | ledger replay | W0 replay restores the same ordered records. Memory/RAG/projection semantics are not part of W0. | answered | G:replay, I3 |
| W12 | upcaster seam | Replay must have a reserved upcaster hook or typed no-path failure for non-current schema versions. Migration chains are not W0. | answered | G:upcaster |
| W13 | auditability | Accepted CALLs, RESULTs, effect decisions, and approval references must be representable as ledger records. | answered | G:ledger, G:envelope, G:effect-tier |
| W14 | envelope scope | Product envelope is not a Direction OS packet. A product executor/builder never authors the next OS CALL. | answered | G:envelope, S9 |
| W15 | call/result correlation | RESULT correlates to CALL by id; evidence is explicit data, not prose-only hidden in logs. | answered | G:envelope |
| W16 | boundary validation | Validator checks envelope shape and W0 hard limits: no real engine, channel, UI/surface, memory/RAG, deployment/auth, marketplace, OS read implementation, or OS write path. | answered | G:boundary, I3, I5 |
| W17 | execution visibility | Accepted execution path is ledger-visible through CALL/RESULT/effect records; invisible side effects are outside W0 acceptance. | answered | W13, W15 |
| W18 | tier semantics | Tier 0 = local/pure/read or reversible no-risk capability work; tier 1 = reversible local state effect; tier 2 = irreversible, external, spend-incurring, or personal-data-egress effect. OS write stays forbidden. | answered | S1, G:effect-tier |
| W19 | tier-2 gate | Tier-2 request without owner approval is rejected. Tier-2 with approval carries an approval reference bound to the request. | answered | G:owner-approval, I2 |
| W20 | gate extensibility | Gate consumes generic `EffectRequest`; adding a plugin must not edit gate code. | answered | G:effect-tier, G:kernel-diff |
| W21 | Engine seam | W0 Engine is fake/no-op and typed enough to swap later; no provider, budget, failover, prompt, or subscription logic enters W0. | answered | G:engine, I4 |
| W22 | Store seam | Store is the append/replay port over local storage; JSONL ledger owns record format and replay semantics. Store is not a second state system. | answered | G:store, G:ledger |
| W23 | Store boundary | Store must not read/write the Direction OS repo. Future OS read capability is separate and hard read-only. | answered | G:store, I5 |
| W24 | acceptance fixtures | Fake capabilities exist only to prove registry/diff/replay/gate mechanics; they are not product features. | answered | I2, I3 |
| W25 | no hidden sixth component | Schema registry, migration registry, policy DSL, dispatcher/router, memory store, and provider adapter are allowed only if folded into the five parts without new kernel component ownership. | answered | I1, I3 |

## §WHAT-C — sibling-bearing contracts routed to converge-arch

These rows are intentionally not solved inside this converge pass because they name contracts
between g-kernel and parked sibling nodes. They are the reason `next_movement = converge-arch`.

| id | edge | contract to close in converge-arch | why it matters |
|---|---|---|---|
| X1 | g-kernel -> g-engine | Exact Engine request/response/error shape that is sufficient for later Claude/Codex/subscription adapters while W0 remains fake. | Prevents W0 from under-specifying the seam or leaking provider logic early. |
| X2 | g-kernel -> g-channel | Channel plugin contract: inbound message -> CALL envelope -> same-channel response, through ledger and gate. | Avoids adding channel fields to W0 envelope prematurely. |
| X3 | g-kernel -> g-surface | `surface` as first-class future kind and what surface capabilities may read/write through envelope/ledger/gate. | Current scaffold omits `surface`; API must not freeze a closed kind union. |
| X4 | g-kernel -> g-memory | Ledger read model/provenance that memory can consume without turning W0 ledger into RAG or SQLite. | Prevents memory needs from widening JSONL replay now. |
| X5 | g-kernel -> g-cognition | Process plugin trace contract: multi-step CALL/RESULT/effect records are visible enough for later "better than chat" proof. | Prevents cognition from inventing a parallel trace format. |
| X6 | g-kernel -> g-accrete | OS read-only capability contract and negative proof that OS write is impossible. | Protects the Direction OS boundary before any OS-reading capability is added. |
| X7 | g-kernel -> root SC2 | Mechanical definition of zero kernel diff across all capability kinds, including the public barrel/API. | Keeps SC2 measurable instead of rhetorical. |

## §COVERAGE MAP

### W0 acceptance target to rows

| target | covered by |
|---|---|
| Capability Registry | W4, W5, W6, W7 |
| Append-only JSONL ledger with schema_version and upcaster seam | W8, W9, W10, W11, W12, W13 |
| Typed CALL/RESULT envelope + boundary validator | W14, W15, W16, W17 |
| Effect-tier gate 0/1/2 -> owner approval for tier-2 | W18, W19, W20 |
| Engine + Store seams | W21, W22, W23 |
| Exactly five parts and no sixth | W1, W25 |
| Third-plugin zero kernel diff | W3, W5, W6, W10, W20, X7 |
| JSONL replay | W8, W9, W10, W11, W12 |
| Tier-2 rejection | W18, W19 |

### Existing scaffold drift to rows

| observed scaffold point | converge ruling |
|---|---|
| `CapabilityKind = "tool" | "channel" | "memory" | "process"` | Conflicts with accepted future `surface`; t-2 should avoid a closed kernel union or include an extension-safe representation. See W5/X3. |
| `LedgerEnvelope.payload: unknown` | Acceptable and desirable for zero kernel diff. See W10. |
| `LedgerUpcaster` interface exists but replay behavior is not specified | W12 requires seam invocation or typed no-path failure, not a full migration system. |
| `BoundaryValidator.validate(call)` has no rule list | W16 supplies the W0 rule surface. |
| `EffectRequest.owner_approval_id?: string` | W19 says the approval id is an artifact reference bound to the request; W0 may validate presence. |
| `Store.append/replay` overlaps JSONL ledger language | W22 closes ownership: Store is a port; ledger owns concrete format. |
| Acceptance spec says no files under `src/<kernel-part>/` | W3 tightens kernel-diff to include root public barrel/API as kernel surface. |

## §SIGNOFF

Define signoff:
- All disputed W0 terms above have one selected meaning for `t-2/t-3`.
- The selected meanings are derived from owner-approved frame/map/shape plus the current W0 scaffold evidence; no new owner-only product fork is introduced here.

Resolve signoff:
- W0-internal mechanism rows W1-W25 are forward-clean for implementation.
- Sibling-bearing rows X1-X7 are routed to `converge-arch`; they should be closed before `converge-verify` and before `t-2/t-3` are treated as freezing the kernel API.
- No product code is changed by this pass.

Verification signoff:
- In-session miner and strategic_search were same-session pre-passes only.
- Binding done verification still requires a fresh `converge-verify` / G5 refutation after the arch pass and after product evidence exists.

END_OF_FILE: live/solmax/work/converge-g-kernel.md
