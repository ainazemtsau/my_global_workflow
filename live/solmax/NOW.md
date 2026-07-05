# NOW — solmax
project:
  name: Zaratusta
  product_repo: github.com/ainazemtsau/zaratusta

active_bet:
  id: b-zara-operate-markdown-manager-v1-full-surface-001
  node: g-zara-operate-state
  status: active
  appetite: 3 focused days
  started: 2026-07-05
  kill_by:
    date: 2026-07-11
    metric: |
      Independent verification of the Zaratusta Markdown operating-manager-v1
      workspace/state surface against full required surface coverage, W20/A1-A13,
      W19 HOW firewall, workspace/effect boundaries, and handback/reporting
      expectations for Direction OS carry-back.
    threshold: |
      PASS only if t-3 verifies product-repo evidence with all required surfaces
      covered: inbox/intake, backlog/open loops, current operating state, week/day,
      reviews, decisions/commitments, source/context, audit/replay, process
      mutation, examples/checks and handback/reporting.

      PASS requires zero hard failures on capture != commitment, proposal !=
      accepted commitment, accepted commitment != completed work, owner approval
      gates, read/write boundaries, side-effect boundaries, topic-open/
      source-context routing, no generic topic blacklist, and no Direction OS
      write path.

      PASS also requires no UI/channel/app surface, API/model vendor/framework/
      subscription adapter, database/storage engine/replay engine/durable writer/
      executable ledger, scheduler, automation, spend controls, external
      integrations, exact permanent schema, or future non-Markdown architecture
      selected as contract.
  forecast: |
    Likely to pass if executor treats the work as a Markdown product surface
    with verifiable examples/checks, not as architecture. The baseline contracts
    already contain the behavioral model; the missing layer is concrete
    workspace/state surface and end-to-end coverage.
  against: |
    This does not prove real recurring use. It also does not complete runtime,
    automation, UI/API, database/storage, or autonomous product readiness.
  definition_of_ready: |
    triage: owner-route-corrected-full-markdown-layer — converge OFF — because
    the owner-corrected route is not a fresh unsettled WHAT-spec node: the
    authority contract is already closed, b92/469 is accepted baseline evidence,
    and the next bounded bet is explicitly the full Markdown operating-manager-v1
    workspace/state surface. The model-bearing HOW choices remain cut, and t-1
    is the early risk gate for coverage before broad implementation.
  cut_list:
    - UI/channel/app surface.
    - API/model vendor/framework/subscription adapter.
    - Database, storage engine, replay engine, durable writer, executable ledger.
    - Scheduler, automation, spend controls, external integrations.
    - Direction OS write path.
    - Exact permanent schema or future non-Markdown architecture.
    - Real owner dogfood week/day operation as acceptance; this bet makes the
      Markdown layer ready, runtime/dogfood comes after verification/review.
    - Product self-development process; Zaratusta repo guardrails do not become
      product direction.
  lens_sweep:
    extensibility: task_required — t-1/t-2 must keep the layer Markdown-only
      and avoid permanent runtime/storage/schema choices.
    real_depth: task_required — t-2/t-3 must cover multi-step operating rhythm,
      not passive memory lookup.
    agent_buildability: task_required — two executor increments plus independent
      verification, each with commit/PR or refutation evidence.
    daily_use_dogfood: task_required_bounded — t-2 must create an owner-operable
      surface; actual recurring dogfood is cut to the next route after review.
    privacy_trust_safety: task_required — t-2/t-3 must preserve Zaratusta-only
      writes, read-only external sources, and owner approval before external/
      irreversible/spend/deletion/message/cross-system effects.
    cost_discipline: task_required_negative_check — no API/vendor/automation/
      spend-bearing implementation is selected.
  riskiest_assumption: |
    A minimal Markdown workspace/state pack can cover the full operating loop
    deeply enough for later runtime/dogfood, while still not choosing a database,
    replay engine, runtime, permanent schema, or app surface.
  next_if_true: |
    Review this bet for closure, then decide the next route: runtime/dogfood
    or evolution.
  next_if_false: |
    Missing surface -> repair executor task.
    WHAT contradiction -> converge.
    HOW-smuggling -> rollback/revert product change and review the cut boundary.

route_status: g-zara-operate-state_active_t1_ready

owner_directive: |
  The first Zaratusta implementation route is g-zara-operate: the LifeReset-derived
  personal operating-manager capability becomes the real Personal Operating System
  phase of Zaratusta, not a PoC and not a separate LifeReset project.

  Owner-approved split from 2026-06-26 remains: g-zara-operate-contract,
  g-zara-operate-state, g-zara-operate-runtime, g-zara-operate-evolution.

  Preserved operating boundary: topic-open through process/source/context; writes
  default only to the Zaratusta workspace/repo; other repos/directions/projects
  are read-only sources by default; future non-Zaratusta writes require explicit
  narrow integration/procedure; deep research is a first-class process route.

  Owner correction in c-solmax-zaratusta-markdown-manager-v1-route-repair-004:
  the next bet must not narrow to state/replay/converge-only work. It must
  shape and then implement the full Markdown operating-manager-v1 layer:
  inbox/intake, backlog/open loops, week/day, reviews, current state,
  source/context, audit/replay, process mutation, examples/checks and handback
  rules. Quality remains priority; this layer must be complete in Markdown
  before later app/runtime/automation work.

  Owner approved option A in the writer-bounced shape exchange: activate the bet
  as written with appetite 3 focused days, full required Markdown surface scope,
  three tasks, risk gate first, kill_by 2026-07-11, cut list, lens sweep and
  first executor CALL.

tasks:
  - id: t-1
    kind: executor
    status: active
    goal: |
      Create the product-repo full-surface coverage scaffold that tests the
      riskiest assumption before broad implementation.
    done_when: |
      Product repo commit/PR contains a Markdown-readable coverage scaffold
      mapping every required surface to concrete product artifacts/checks:
      inbox/intake, backlog/open loops, current operating state, week/day,
      reviews, decisions/commitments, source/context, audit/replay, process
      mutation, examples/checks and handback/reporting. The scaffold identifies
      reused baseline files, files needing creation/update, W19/HOW not-chosen
      items, and any missing required surface before t-2 proceeds.
    evaluator: independent verification in t-3
    rollback: |
      Revert or repair any scaffold that narrows the route to state/replay-only,
      check-only, manual-use prose, or that smuggles forbidden HOW choices.

  - id: t-2
    kind: executor
    status: open
    goal: |
      Implement the full minimal Markdown operating-manager-v1 workspace/state
      layer in the Zaratusta product repo.
    done_when: |
      Product repo commit/PR creates or updates the minimal Markdown artifacts,
      templates, contracts, examples and checks needed to operate the complete
      v1 layer across inbox/intake, backlog/open loops, current state, week/day,
      reviews, decisions/commitments, source/context, audit/replay, process
      mutation, examples/checks and handback/reporting. No forbidden HOW choice,
      generic topic blacklist or Direction OS write path is introduced.
    evaluator: independent verification in t-3
    rollback: |
      Revert or repair any product-repo artifact that weakens W20/A1-A13,
      violates workspace/effect boundaries, introduces a Direction OS write
      path, or smuggles W19/HOW choices.

  - id: t-3
    kind: session
    status: open
    goal: |
      Independently try to refute that the product repo now contains the full
      Markdown operating-manager-v1 workspace/state surface.
    done_when: |
      Verifier reads the product repo commit/PR evidence from t-1 and t-2 plus
      the accepted baseline files. PASS requires all required surfaces covered,
      W20/A1-A13 preserved, W19 HOW firewall clean, workspace/effect boundaries
      preserved, no Direction OS write path, topic-open/source-context handling
      intact, no generic topic blacklist and no forbidden implementation choice.
      FAIL names exact missing/contradictory rows and routes product gap to
      repair executor task, WHAT contradiction to converge, and HOW-smuggling
      to rollback/review cut.
    evaluator: n/a

recurring: []
decisions: []

open_calls:
  - id: c-zara-operate-markdown-manager-v1-full-surface-t1-001
    to: executor
    for: t-1
    issued: 2026-07-05
    note: full-surface coverage scaffold in Zaratusta product repo

preserved_evidence:
  - live/solmax/CHARTER.md
  - live/solmax/TREE.md
  - live/solmax/LOG.md
  - live/solmax/work/converge-g-zara-operate-contract.md
  - live/solmax/history/2026-07-04-c-solmax-zaratusta-markdown-manager-v1-route-repair-004.md
  - live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md
  - live/solmax/history/2026-07-05-s-zara-operate-markdown-manager-v1-full-shape-repair-001.md
  - live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-surface-t1-001.md
  - github.com/ainazemtsau/zaratusta@79578ac87c73591000409f9f82a3bb4d0e33aa5b
  - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631
  - github.com/ainazemtsau/zaratusta@469e6996ea120073168bf350d54cf8e56135f30d
  - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/contracts/operating-manager-v1.md
  - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/contracts/operating-manager-v1-source-basis.md
  - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/docs/decisions/0002-operating-manager-v1-surface.md
  - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/examples/operating-manager-v1-examples.md

next: work/calls/c-zara-operate-markdown-manager-v1-full-surface-t1-001.md
END_OF_FILE: live/solmax/NOW.md
