# NOW — solmax
project:
  name: Zaratusta
  product_repo: github.com/ainazemtsau/zaratusta

active_bet:
  status: none

route_status: g-zara-operate-contract_converge_verify_passed_pending_shape

owner_directive: |
  The first Zaratusta implementation route is g-zara-operate: the LifeReset-derived
  personal operating-manager capability becomes the real Personal Operating System phase
  of Zaratusta, not a PoC and not a separate LifeReset project.

  The owner approved option A on 2026-06-26: g-zara-operate is split into four child
  outcomes:
  - g-zara-operate-contract
  - g-zara-operate-state
  - g-zara-operate-runtime
  - g-zara-operate-evolution

  First child remains g-zara-operate-contract. Shape bounced it back to converge, converge
  repaired the authority WHAT rows that had encoded the wrong forbidden-domain/blacklist
  model, trace repair fixed invalid glossary references, and converge-verify has now passed.

  Preserved owner clarification:
  - Zaratusta manager should not be defined by broad domain prohibitions.
  - The manager may work on any owner-requested domain/topic through the right process
    and source context.
  - The hard boundary is write ownership and side effects: Zaratusta manager writes only
    to its own Zaratusta workspace/repo by default.
  - Other repos/directions/projects are read-only sources by default.
  - Future write access to another system requires an explicit narrow integration/procedure.
  - First implementation layer should be Markdown/GitHub-readable: source registry,
    process registry, owner-context structure, context-loading procedure and examples/tests;
    no DB/API/engine/scheduler/automation now.
  - Deep research is a first-class process/route for creating or improving processes when
    external evidence is needed.

blocked_reason: |
  No implementation resumes until g-zara-operate-contract is shaped into a bounded bet.
  The repaired WHAT has passed converge-verify:
  - complete=PASS
  - backward_clean=PASS
  - forward_clean=PASS
  - smuggling=PASS
  - row_failures=none

  Shape must copy W20/A1-A13 into Definition-of-Ready or executor done_when unless it finds
  a new exact contradiction. W19 remains the PLAN agenda.

tasks: []
recurring: []
decisions: []
open_calls: []

preserved_evidence:
  - live/solmax/CHARTER.md
  - live/solmax/TREE.md
  - live/solmax/LOG.md
  - live/solmax/work/converge-g-zara-operate-contract.md
  - live/solmax/history/2026-06-25-s-zara-remap-001.md
  - live/solmax/history/2026-06-26-s-zara-shape-operate-001b.md
  - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-verify-001.md
  - live/solmax/history/2026-06-26-s-zara-operate-contract-shape-001.md
  - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-owner-boundary-002.md
  - live/solmax/history/2026-06-27-s-zara-operate-contract-converge-verify-owner-boundary-002.md
  - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-trace-repair-003.md
  - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-verify-trace-repair-004.md
  - live/life-reset/CHARTER.md
  - github.com/ainazemtsau/life-reset-manager/SPEC.md
  - github.com/ainazemtsau/zaratusta

next:
  id: c-zara-operate-contract-shape-002
  to: session
  direction: solmax
  play: shape
  node: g-zara-operate-contract
  goal: |
    Shape g-zara-operate-contract into a bounded implementation bet that preserves the
    verified operating-manager authority WHAT after owner-boundary repair and trace repair.
  context: |
    Read:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - live/solmax/LOG.md
    - live/solmax/work/converge-g-zara-operate-contract.md
    - live/solmax/history/2026-06-26-s-zara-operate-contract-shape-001.md
    - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-owner-boundary-002.md
    - live/solmax/history/2026-06-27-s-zara-operate-contract-converge-verify-owner-boundary-002.md
    - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-trace-repair-003.md
    - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-verify-trace-repair-004.md
    - live/life-reset/CHARTER.md
    - github.com/ainazemtsau/life-reset-manager/SPEC.md

    Converge-verify passed after trace repair:
    - complete=PASS
    - backward_clean=PASS
    - forward_clean=PASS
    - smuggling=PASS
    - row_failures=none

    Copy W20/A1-A13 into Definition-of-Ready or executor done_when unless shape finds a
    new exact contradiction:
    - A1 manager role is separate from source registry, process contracts,
      owner-context structure and state artifacts; no monolithic prompt closes the node.
    - A2 every manager output that changes route/state/commitment carries an authority
      basis, process/source context basis, effect tier and workspace/write boundary.
    - A3 no generic domain/topic blacklist: the manager may work on any owner-requested
      topic through the right process and source context.
    - A4 every source/context item has source id/path/link, owner/scope, read/write
      status, freshness/trust marker and allowed use.
    - A5 every nontrivial operation declares the loaded source/context bundle, missing
      context and route if context is insufficient.
    - A6 owner-context structure represents durable owner facts, preferences, decisions,
      approvals, evidence, unknowns, context summaries and state-change requests inside
      Zaratusta workspace.
    - A7 process registry entries are inspectable contracts with purpose, inputs, outputs,
      authority/effect tier, required source context, owner approval gates and examples/tests.
    - A8 no matching process routes to process draft/research/review; process creation or
      mutation is a proposal or ET2 action with owner approval; hidden self-rewrite is invalid.
    - A9 Direction OS and other repos/directions/projects are read-only sources by default;
      Zaratusta writes only to its own workspace/repo unless an explicit narrow
      integration/procedure is approved.
    - A10 external, irreversible, spend, deletion, message/send or material cross-system
      effects require explicit scoped owner approval before effect.
    - A11 intake/planning/logging preserve commitment semantics: captures are not commitments;
      plans distinguish proposal from accepted commitment and name displacement; log responses
      are bounded to loaded context.
    - A12 high-stakes/source-owned requests are routed by process/source/context: examples/tests
      must show answer/summarize/draft/track/route behavior without topic refusal, while
      unsourced source-owned instructions and unapproved side effects are blocked before effect.
    - A13 first implementation layer is GitHub/Markdown-readable source registry, process
      registry, owner-context structure, context-loading procedure and examples/tests; exact
      UI/storage/vendor/schema/cadence/scoring/scheduler/automation/API choices remain
      unchosen at this layer.

    No separate §CONTRACTS section exists in the converge file; W20/A1-A13 are the contract
    surface to preserve.

    Treat W19 routed choices as PLAN agenda, not as WHAT:
    - exact UI/channel/surface
    - exact storage/schema/file layout/database
    - exact engine/vendor/framework/API/subscription adapter
    - exact horizon durations/cadence/month/12-week model
    - exact non-caving weighing/scoring policy and thresholds
    - exact implementation of state writer and replay
    - exact research procedure mechanics
    - exact automation/scheduler/spend controls
    - exact external integration procedure for future non-Zaratusta writes
    - exact source registry/process registry/owner-context file layout

    Preserve child-consumer edges:
    - g-zara-operate-state consumes W8-W10, W16, W18, W20.
    - g-zara-operate-runtime consumes W1-W20.
    - g-zara-operate-evolution consumes W15, W18-W20.
  boundaries: |
    Do not implement or modify the product repository.
    Do not reopen the old W0/kernel-first route.
    Do not copy LifeReset wholesale.
    Do not reintroduce a generic domain/topic blacklist.
    Do not change the owner-approved rule that the manager may work on any owner-requested
    topic through the right process and source context.
    Do not weaken the write boundary: Zaratusta writes only to its own workspace/repo by
    default; other repos/directions/projects remain read-only sources by default; future
    writes elsewhere require explicit narrow integration/procedure.
    Do not choose UI, storage engine, database, exact schema, exact cadence, scoring,
    automation, scheduler, vendor, framework or API/subscription adapter.
    Do not convert W19 HOW/PLAN choices into WHAT unless shape finds a contradiction that
    must bounce to converge.
  done_when: |
    An owner-approved bounded bet for g-zara-operate-contract exists with appetite, kill_by,
    cut list, lens sweep and tasks that include the riskiest assumption.
    Shape copies W20/A1-A13 into the bet's Definition-of-Ready or executor done_when and
    carries W19 as PLAN agenda.
    If any verified WHAT row becomes inconsistent during shape, the exact row is bounced to
    converge instead of guessed.
  return: |
    RESULT with approved bet or exact bounce, TREE/NOW/LOG state_changes, evidence, and
    next ready work/verify route.
  budget: one shape session

END_OF_FILE: live/solmax/NOW.md
