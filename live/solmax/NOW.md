# NOW — solmax
project:
  name: Zaratusta
  product_repo: github.com/ainazemtsau/zaratusta

active_bet:
  status: none

route_status: g-zara-operate-contract_shape_bounced_to_converge_owner-boundary-repair

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

  First child remains g-zara-operate-contract, but shape bounced it back to converge
  before activation.

  Owner-approved clarification from shape:
  - Zaratusta manager should not be defined by broad domain prohibitions.
  - The manager may work on any owner-requested domain/topic through the right process
    and source context.
  - The hard boundary is write ownership and side effects: Zaratusta manager writes only
    to its own Zaratusta workspace/repo by default.
  - Other repos/directions/projects are read-only sources by default.
  - Future write access to another system requires an explicit narrow integration/procedure.
  - First implementation layer should be Markdown/GitHub-readable: source registry,
    process registry, owner-context structure, context-loading procedure and examples;
    no DB/API/engine/scheduler/automation now.

blocked_reason: |
  No implementation resumes until converge repairs the exact rows whose forbidden-zone /
  domain-blacklist framing contradicts the owner's clarified process/source/workspace
  model.

  Rows to reopen:
  - G10 forbidden prescription zone
  - W8 ET3 domain-forbidden list
  - W17 forbidden prescription zones
  - W20/A12
  - dependent references in W2/W6/W7/W12/W13 only where they rely on that model

  Keep unless converge finds direct contradiction:
  - Direction OS and other repos/directions/projects are read-only sources by default.
  - Zaratusta manager writes only to its own workspace/repo by default.
  - W19 HOW firewall remains intact.

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
  - live/life-reset/CHARTER.md
  - github.com/ainazemtsau/life-reset-manager/SPEC.md
  - github.com/ainazemtsau/zaratusta

next:
  id: c-zara-operate-contract-converge-owner-boundary-002
  to: session
  direction: solmax
  play: converge
  node: g-zara-operate-contract
  goal: |
    Reopen and repair the operating-manager authority WHAT rows whose forbidden-zone /
    domain-blacklist framing conflicts with the owner's clarified Zaratusta manager model:
    an extensible process/source/workspace system where the manager may work on any
    owner-requested topic through the right process and context, while writes/side effects
    are bounded to its own workspace unless explicitly integrated.
  context: |
    Read:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - live/solmax/LOG.md
    - live/solmax/work/converge-g-zara-operate-contract.md
    - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-verify-001.md
    - live/solmax/history/2026-06-26-s-zara-operate-contract-shape-001.md
    - live/life-reset/CHARTER.md
    - github.com/ainazemtsau/life-reset-manager/SPEC.md

    Prior converge-verify had passed, but shape surfaced a live owner clarification that
    contradicts the hard forbidden-domain framing.

    Preserve owner clarification:
    - Do not build the manager as a list of "you must not do X/Y/Z" prohibitions.
    - The manager may work on any owner-requested topic/domain by loading the right
      process and source context.
    - The real hard boundary is write ownership and side effects.
    - Zaratusta manager writes only to its own Zaratusta workspace/repo by default.
    - Other repos/directions/projects are read-only sources by default.
    - Future write access to another system requires an explicit narrow procedure/integration.
    - The first layer should be Markdown/GitHub-readable: source registry, process registry,
      owner-context structure, context-loading procedure, examples/tests.
    - No DB/API/engine/scheduler/automation now.
    - Deep research should be modeled as a first-class process/route for creating or improving
      processes when external evidence is needed.

    Reopen exact rows/objects:
    - G10 forbidden prescription zone
    - W8 ET3 domain-forbidden list
    - W17 forbidden prescription zones
    - W20/A12
    - dependent references in W2/W6/W7/W12/W13 only where they rely on the same model

    Keep unless converge finds a direct conflict:
    - Direction OS remains read-only.
    - Other repos/directions/projects are read-only sources by default.
    - Zaratusta manager writes only to its own workspace/repo by default.
    - W19 HOW firewall remains: UI/storage/vendor/schema/cadence/scoring/scheduler/API
      decisions are PLAN/later-child, not WHAT.
  boundaries: |
    Do not implement or modify the product repository.
    Do not reopen the old W0/kernel-first route.
    Do not copy LifeReset wholesale.
    Do not preserve W17/A12 merely because converge-verify previously passed; owner has now
    supplied contradictory clarification.
    Do not replace the blacklist with an equally broad new blacklist.
    Do not remove the Direction OS / other-repo read-only boundary unless owner explicitly
    changes it.
    Do not choose UI, storage, engine, database, schema, cadence, scoring, automation or
    scheduler.
  done_when: |
    The reopened rows are repaired or an exact owner decision is requested.
    The repaired WHAT states a positive extensible process/source/workspace model:
    sources, process creation, context loading, owner-context structure, examples/tests,
    review/mutation route and write-boundary semantics.
    Any remaining hard boundary is justified as source integrity, owner approval, state
    ownership or side-effect safety, not as a generic domain blacklist.
    W20/A1-A13 is updated or replaced so the next shape can copy the acceptance surface
    without contradicting the owner's clarification.
  return: |
    RESULT with repaired WHAT rows or exact owner decision needed; state_changes for
    work/NOW/LOG/history; next route to converge-verify if repaired, or awaiting_decision
    if not.
  budget: one converge session

END_OF_FILE: live/solmax/NOW.md
