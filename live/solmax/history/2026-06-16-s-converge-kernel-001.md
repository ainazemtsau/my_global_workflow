RESULT s-converge-kernel-001 (call: c-converge-kernel-001)
direction: solmax   play: converge   node/task: g-kernel

outcome: |
  RETROFIT converge for g-kernel is complete as a spec-layer pass.
  `work/converge-g-kernel.md` now defines the W0 RLK mechanism meanings for t-2/t-3:
  Capability Registry, append-only JSONL ledger, CALL/RESULT envelope + boundary validator,
  effect-tier gate, and Engine + Store seams.

  The pass found real white spots but did not widen W0:
  - `surface` is an owner-accepted future capability kind, so the registry must not freeze
    a closed kind union that forces kernel edits.
  - Zero-kernel-diff now includes both the five kernel module directories and the root
    public kernel barrel/API, while plugin registration/handler/fixture files stay outside.
  - JSONL ledger owns record format/replay; Store is a port, not a second state subsystem.
  - Owner approval is an auditable approval reference bound to a tier-2 request; W0 may
    validate presence, later UX/provenance can deepen it.

  Because the node is sibling-bearing, the next movement is converge-arch before
  converge-verify.

evidence: |
  - Added `live/solmax/work/converge-g-kernel.md` with:
    - triage: HEAVY / converge ON;
    - glossary of disputed W0 terms;
    - §WHAT mechanism decomposition rows W1-W25;
    - sibling contract rows X1-X7 routed to converge-arch;
    - coverage map and §SIGNOFF.
  - Read Direction state: `live/solmax/NOW.md`, `TREE.md`, `CHARTER.md`,
    `history/s-map-001.md`, `history/s-shape-001.md`, and
    `history/2026-06-16-s-repair-kernel-t1-state.md`.
  - Product scaffold evidence read from `C:\projects\zaratusta-product`:
    `openspec/changes/w0-rlk/specs/rlk/spec.md`, `src/**/index.ts`,
    `validation.config`, `REVIEW.md`, and setup tests.
  - In-session read-only explorer pre-pass
    `019ece83-3a04-7bf1-9295-051f555dd0d2` identified surface-kind,
    approval, Store-vs-ledger, upcaster, and kernel-diff gaps.
  - In-session read-only strategic_search pre-pass
    `019ece83-6bf2-7e82-b1b2-ed299e2d73d0` selected the opaque-payload
    microkernel line and killed closed kernel unions / policy DSL / framework reuse.

assumptions: |
  - The product scaffold is evidence, not final W0 API; t-2 may still adjust TypeScript
    types/specs to match the converge rows.
  - `surface` does not need a new owner decision because `history/s-map-001.md` records it
    as owner-accepted and says the charter does not need an edit.
  - Existing owner decisions about the TypeScript/Node stack and the local product path
    remain pending before t-2; this converge pass does not answer them.

cuts: |
  - No product code was changed.
  - No active bet, task, appetite, kill_by, TREE, or CHARTER text was rewritten.
  - No real engine/channel/UI/surface/memory/RAG/deployment/auth/marketplace/OS-read
    implementation was added.
  - No sixth kernel component was introduced.

cost: |
  One session. Two same-session read-only subagents were used as converge miner and
  strategic_search pre-passes. No binding fresh G5 review was run.

manual-acceptance: |
  None requested in this pass. Binding acceptance still requires:
  - converge-arch to close sibling-bearing contracts; and
  - fresh converge-verify/G5 refutation after arch closure and product evidence.

state_changes: |
  Added:
    - live/solmax/work/converge-g-kernel.md
    - live/solmax/history/2026-06-16-s-converge-kernel-001.md

  NOW.md:
    - Add `c-converge-kernel-001` to `open_calls` as done.
    - Add `c-converge-arch-kernel-001` to `open_calls` as ready.
    - Replace `next` with ready_call `c-converge-arch-kernel-001` while preserving
      the existing pending owner decisions before t-2.

  LOG.md:
    - Add newest-first:
      "2026-06-16 — converge g-kernel: retrofit closed W0 RLK mechanism meanings,
      tightened zero-kernel-diff semantics, and routed sibling-bearing
      Engine/channel/surface/memory/OS-read contracts to converge-arch.
      → history/2026-06-16-s-converge-kernel-001.md"

decisions_needed: |
  No new owner decision is raised by this converge pass.
  Existing NOW.md decisions about the W0 stack and local product path remain pending
  before launching t-2.

play_check:
  - "1 Import settled decisions: done — frame/map/shape, NOW, TREE, repair result, and product scaffold imported; W0 shape rows marked born-closed."
  - "2 Triage: done — g-kernel is HEAVY because it is model-bearing, sibling-bearing, and mechanism-decomposed."
  - "3 Glossary/miner: done — disputed terms were seeded and checked by a read-only explorer pre-pass."
  - "4 Strategic search: done — opaque-payload microkernel survived; closed unions, framework reuse, policy DSL, and OS integration in W0 were killed."
  - "5 §WHAT decomposition: done — W1-W25 cover W0 mechanisms; X1-X7 route sibling contracts to converge-arch."
  - "6 Signoff/next: done — W0-internal terms are signed for t-2/t-3; next is converge-arch before converge-verify."

log: "converge g-kernel: retrofit closed W0 RLK mechanism meanings, tightened zero-kernel-diff semantics, and routed sibling-bearing Engine/channel/surface/memory/OS-read contracts to converge-arch"

next: |
  CALL c-converge-arch-kernel-001
  to: session   direction: solmax   play: converge-arch   node: g-kernel
  goal: |
    g-kernel sibling contracts are explicit enough that g-engine, g-channel, g-surface,
    g-memory, g-cognition, and g-accrete can consume RLK without widening W0 or forcing
    kernel edits for new capability kinds.
  context: |
    - Direction state: live/solmax/NOW.md, live/solmax/TREE.md, live/solmax/CHARTER.md.
    - Converge retrofit: live/solmax/work/converge-g-kernel.md.
    - Source history: live/solmax/history/s-map-001.md,
      live/solmax/history/s-shape-001.md,
      live/solmax/history/2026-06-16-s-repair-kernel-t1-state.md.
    - Product scaffold evidence: C:\projects\zaratusta-product at commit
      18d74b1114428be8df5ece48bf6d89f3b2776a75.
    - Rows to close: X1-X7 in work/converge-g-kernel.md.
  boundaries: |
    - Spec-layer only; no product code.
    - Do not change active_bet, tasks, appetite, kill_by, TREE, or CHARTER.
    - Do not widen W0 beyond exactly five kernel parts.
    - Do not implement real engine, channels, UI/surface, memory/RAG, deployment/auth,
      marketplace, or OS-read capability.
    - Preserve pending owner decisions about TypeScript/Node stack and local product path.
  done_when: |
    All sibling-bearing rows X1-X7 have explicit contracts or explicit parking rationale:
    Engine request/result/error shape; channel response contract; surface kind/API;
    memory ledger read model; cognition trace needs; OS read-only boundary; and
    zero-kernel-diff API surface. No new W0 kernel component is introduced.
  return: |
    RESULT with evidence, updates to work/converge-g-kernel.md or a companion arch artifact,
    and next -> converge-verify if the contracts are closed; otherwise exact decisions_needed.
  budget: one session

END_OF_FILE: live/solmax/history/2026-06-16-s-converge-kernel-001.md
