# TREE — solmax

owner_approved:
  status: true
  evidence:
    - '2026-06-24: owner approved resetting Zaratusta TREE to root-only before a fresh evidence-led map.'
    - '2026-06-26: owner approved g-zara-operate as a 4-child first-node split; first child is g-zara-operate-contract.'
    - '2026-07-02: owner approved TREE closure for g-zara-operate-contract after review verdict met. Owner words: "Нужен исправленный RESULT/repair, который явно несёт owner approval для TREE closure и приводит NOW.next к текущему writer-формату."'

tree_validity:
  state: operate_first_node_split_approved
  note: |
    The former kernel-first seven-node map is not executable. Its nodes and
    architecture remain evidence in history/s-map-001.md and related files.

    Zaratusta now starts with the LifeReset-derived operating-manager outcome
    as a bounded first node, split into four child outcomes. The first child
    routes to converge before any implementation.

root:
  id: g-zara
  status: shaped
  goal: |
    Zaratusta — a personal, deeply personalized AI exocortex the owner actually
    relies on deeply across several areas of life and work, built to accumulate
    trustworthy capabilities and grow toward the full EXOCORTEX vision.
  done_when: |
    All hold unless the charter is explicitly revised:

    1. The owner relies on Zaratusta deeply and recurringly in at least
       3 distinct areas of life/work.

    2. Several live capabilities span tool, channel, memory and process axes
       without requiring repeated core redesign.

    3. At least one real hard process is judged by the owner clearly better
       than a plain ChatGPT/Claude session: multi-step, personalized and aware
       of his actual priorities.
  why: |
    This is the enduring Zaratusta outcome. The LifeReset-derived operating
    manager is the first proving phase, not a separate root or product.
  children:
    - id: g-zara-operate
      status: parked
      goal: |
        Zaratusta operates as the owner's real Personal Operating System:
        it coordinates week/day rhythm, intake, planning, execution support,
        review, durable context and evidence-gated evolution with deep
        personalization and safe manager authority.
      done_when: |
        The owner can rely on Zaratusta as a personal operating manager in
        real recurring use: it maintains trustworthy operating context,
        routes intake, supports week/day planning and review, preserves
        decisions and evidence, and evolves its processes without hidden
        assumptions, OS writes, medical/psychiatric/nutrition/training
        prescriptions, silent spend or irreversible/external actions.
      why: |
        This is the owner-approved first Zaratusta node: the LifeReset-derived
        operating manager becomes a real personal system, not a PoC, before
        broader exocortex expansion.
      children:
        - id: g-zara-operate-contract
          status: done
          appetite: 2 focused days
          kill_by: |
            metric: independent verification of the Zaratusta Markdown/GitHub-readable
              contract pack against W20/A1-A13 and W19 HOW firewall
            threshold: |
              By 2026-07-05, t-3 must verify product-repo evidence with A1-A13 all
              covered; zero hard failures on topic-open rule, write boundary, owner
              approval/side-effect boundary and HOW firewall; no domain blacklist; no
              OS write path; and no DB/API/runtime/storage/schema/cadence/vendor/
              scheduler/automation chosen as contract.
            date: 2026-07-05
          goal: |
            The operating manager has a signed authority and entity contract:
            what it may decide, ask, propose, route, refuse or escalate is
            explicit across owner entities, work/life domains, horizons and
            effect tiers.
          done_when: |
            A closed WHAT spec defines manager authority, effect tiers,
            entity model, horizon model, escalation rules and forbidden
            prescription zones; implementation can build against it without
            guessing powers or scope.
          why: |
            Every later operating feature depends on whether the manager is
            allowed to act, remember, ask, change state or only advise.

        - id: g-zara-operate-state
          status: parked
          goal: |
            Zaratusta has durable operating state and context that are
            auditable, recoverable and separate from the Direction OS writer.
          done_when: |
            The system can persist and replay operating facts, decisions,
            source links, open loops and context summaries in its own state;
            it can read the workflow OS only as a source and cannot write it;
            recovery and audit are demonstrable.
          why: |
            A personal operating system is not real if it forgets, invents
            continuity or corrupts the external OS state.

        - id: g-zara-operate-runtime
          status: parked
          goal: |
            The owner can actually run week/day/intake/planning/execution/review
            through Zaratusta in ordinary use.
          done_when: |
            A minimal operating loop handles real owner intake, produces and
            revises week/day operating packets, tracks open loops, supports
            execution review, and is judged by the owner more useful than a
            plain chat for this operating rhythm.
          why: |
            Daily use and dogfood are the guard against another abstract core
            draft; runtime is where the manager proves value.

        - id: g-zara-operate-evolution
          status: parked
          goal: |
            The operating manager improves its processes through explicit
            review, research and evidence-gated change rather than hidden
            self-mutation.
          done_when: |
            Reviews create accepted facts, rejected changes, research calls
            and proposed process updates with evidence; capabilities evolve
            by bounded registration/handler increments, not kernel churn or
            silent prompt edits.
          why: |
            The system must grow toward the full exocortex without becoming
            an unbounded bet or uncontrolled self-rewrite.

END_OF_FILE: live/solmax/TREE.md
