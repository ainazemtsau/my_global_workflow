# converge-g-kernel - RLK W0 question set (RETROFIT, repaired)

> Repair note, 2026-06-16: the previous version of this file over-closed
> model-proposed interpretations as `answered` / `signoff` without owner
> approval. This repaired version is a FORM/AGENDA pass. Only §BORN-CLOSED is
> answered from history. §NEEDS OWNER SIGNOFF is an agenda for discussion, not
> a decision record.

## Header - triage and import

```
triage: HEAVY - converge ON - because g-kernel defines the product's extension
        model, is consumed by sibling nodes, and decomposes into registry /
        ledger / envelope / gate / engine-store seams.
mode:   RETROFIT FORM - g-kernel is already active, so import settled history
        as born-closed and frame the remaining white spots for owner resolve.
status: NOT RESOLVED. NOT SIGNED. Do not treat this file as t-2/t-3 API lock.
next:   owner resolve on §NEEDS OWNER SIGNOFF before converge-arch or t-2 API
        freeze. After owner signoff, reroute to converge-arch or converge-verify.
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
| S8 | `C:\projects\zaratusta-product\src\**\index.ts` setup scaffold |
| S9 | `C:\projects\zaratusta-product\validation.config` / `REVIEW.md` / setup tests |

## §BORN-CLOSED - already decided before this retrofit

| id | decided fact | source |
|---|---|---|
| B1 | W0 target is exactly five parts and no sixth: Capability Registry; JSONL ledger; CALL/RESULT envelope + boundary validator; effect-tier gate; Engine + Store seams. | S2, S3, S5, S7 |
| B2 | CI/acceptance must prove third-plugin zero kernel diff, JSONL replay, and tier-2 rejection without owner approval. | S2, S3, S5, S7 |
| B3 | W0 excludes real engine, channels, UI/surface, memory/RAG, deployment/auth, marketplace, OS read implementation, and OS write path. | S1, S3, S5, S9 |
| B4 | Engine in W0 is fake/no-op only; subscription/API/failover belongs to g-engine. | S1, S2, S3, S5 |
| B5 | Zaratusta may later read the Direction OS repo read-only; writing to the OS is forbidden. | S1, S2, S3 |
| B6 | The map records `surface` as a future kind / fifth type of capability. This does NOT decide the W0 TypeScript representation. | S4, S2 |
| B7 | Product setup exists and has a W0 acceptance scaffold; that scaffold is not itself owner signoff on the final kernel API. | S6, S7, S8, S9 |

## §NEEDS OWNER SIGNOFF - white spots to discuss

Every row below is a proposal candidate, not an answer. A later resolve/signoff
must either accept, change, or explicitly defer each row before t-2/t-3 are
treated as kernel API freeze.

| id | spot | why it matters | candidate recommendation |
|---|---|---|---|
| Q1 | Capability kind representation: closed union vs extension-safe kind token. | Current scaffold has four kinds; map already names future `surface`. A closed union may force kernel edits. | Prefer extension-safe representation, or include `surface` now. Owner must choose. |
| Q2 | Mechanical boundary of "zero kernel diff". | OpenSpec says no files under `src/<kernel-part>/`; shape says no kernel edits. Root public barrel/API may be a hidden kernel surface. | Prefer counting five module dirs plus public barrel/API as kernel. Owner must sign. |
| Q3 | Registry lifecycle. | Duplicate ids, replacement, deprecation, and active/inactive semantics affect replay and plugin accretion. | Minimal W0: stable unique id and deterministic duplicate rejection; lifecycle beyond that later. |
| Q4 | Handler reference meaning. | Ledger/registry should not accidentally store executable code or import paths that become platform lock-in. | Registry stores a handler reference only; runtime fixture resolves it outside kernel. |
| Q5 | Registry safety metadata. | Gate/boundary may need plugin-declared policy without becoming a sixth subsystem. | Allow bounded data fields only; no policy DSL/rules engine in W0. |
| Q6 | Ledger replay scope. | Replay could mean raw ordered records, registry projection, effect projection, or future memory substrate. | W0 proves raw ordered record replay only; projections belong to later contracts unless owner signs otherwise. |
| Q7 | Upcaster behavior. | "Reserved seam" can mean type-only placeholder or executable replay path. | W0 should expose a seam plus deterministic unsupported-version failure; no migration framework. |
| Q8 | CALL/RESULT envelope fields. | Too few fields may under-spec future nodes; too many leaks channel/memory/workflow into W0. | Keep product-local CALL/RESULT correlation + goal/boundaries/outcome/evidence; do not copy OS writer semantics. |
| Q9 | Boundary validator rule set. | Required-fields-only validation misses W0 cuts; too much validation becomes future policy engine. | Validate shape plus W0 hard cuts: no real engine/channel/UI/memory/deployment/OS write. |
| Q10 | Tier 0/1/2 semantics. | Privacy/safety gate is central; wrong tiers make owner approval either noisy or bypassable. | Draft: tier 0 local/read/pure; tier 1 reversible local write; tier 2 irreversible/external/spend/data-egress. OS write forbidden outside tiers. |
| Q11 | Owner approval artifact. | `owner_approval_id?: string` could be any truthy value or a real auditable reference. | Treat as approval reference bound to request id/tier/description; W0 may only validate presence. |
| Q12 | Effect decision ledgering. | Auditability depends on whether allowed/rejected decisions become ledger-visible. | Represent effect decision and approval reference as ledger records, without building UX. |
| Q13 | Store vs JSONL ledger ownership. | Current Store seam has `append/replay`, overlapping ledger language; this could create a second state subsystem. | Store is a port over local storage; JSONL ledger owns record format and replay semantics. |
| Q14 | Engine seam minimum shape. | Too-thin fake `complete(input: string)` may fail later provider swap; too-rich shape leaks g-engine into W0. | Keep fake/no-op, but discuss minimum request/result/error contract before API freeze. |
| Q15 | Third-plugin fixture and diff oracle. | Acceptance depends on exact file boundaries and expected changed files. | Define fixture paths and diff oracle before t-3; do not let executor improvise the proof. |

## Owner discussion agenda

Recommended discussion order:

1. Q1 + Q2: extension kind model and zero-kernel-diff boundary.
2. Q6 + Q7 + Q13: ledger, replay, upcaster, Store ownership.
3. Q8 + Q9: envelope and boundary validator scope.
4. Q10 + Q11 + Q12: effect tiers and owner approval evidence.
5. Q3 + Q4 + Q5 + Q15: registry and acceptance fixture details.
6. Q14: Engine seam minimum, only after W0 boundary is clear.

Possible owner choices for the whole agenda:

| option | effect | recommendation |
|---|---|---|
| A. Hold t-2 and resolve Q1-Q15 now. | Slower, but prevents accidental kernel API freeze by executor defaults. | Recommended. |
| B. Let t-2 proceed with scaffold defaults and treat Q1-Q15 as implementation details. | Faster, but accepts drift risk and may recreate the skipped-converge bug. | Not recommended. |
| C. Accept the candidate recommendations above as owner-approved. | Fastest, but only valid if the owner explicitly signs this option after reading. | Acceptable only with explicit owner words. |

## §COVERAGE MAP - what the agenda covers

| W0 target | white-spot rows |
|---|---|
| Capability Registry | Q1, Q3, Q4, Q5, Q15 |
| Append-only JSONL ledger with schema_version and upcaster seam | Q6, Q7, Q12, Q13 |
| Typed CALL/RESULT envelope + boundary validator | Q8, Q9 |
| Effect-tier gate 0/1/2 -> owner approval for tier-2 | Q10, Q11, Q12 |
| Engine + Store seams | Q13, Q14 |
| Zero-kernel-diff proof | Q1, Q2, Q5, Q15 |

## §SIGNOFF

Define signoff:
- Not signed. Only §BORN-CLOSED is imported as answered.

Resolve signoff:
- Not signed. Q1-Q15 require owner resolve or explicit deferral.

Verification signoff:
- Not run. Prior explorer/researcher subagents were same-session pre-passes only.
- Binding verification must happen later in a fresh review/verify session after owner
  resolve and product evidence.

END_OF_FILE: live/solmax/work/converge-g-kernel.md
