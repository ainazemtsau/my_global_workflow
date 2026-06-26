RESULT s-zara-operate-contract-converge-001 (call: c-zara-operate-contract-converge-001)
direction: solmax   play: converge   node/task: g-zara-operate-contract

outcome: |
  Signed WHAT spec for g-zara-operate-contract is closed and ready for
  converge-verify.

  The spec defines:
  - manager authority;
  - effect tiers;
  - entity model;
  - horizon model;
  - escalation rules;
  - forbidden prescription zones;
  - owner-approval and override boundaries;
  - read-only Direction OS boundary;
  - implementation acceptance properties for later shape.

  No implementation, product-repository, vendor, framework, UI or storage
  decision was made.

evidence: |
  Primary node evidence:
  - live/solmax/TREE.md defines g-zara-operate-contract as the child whose
    done_when is a closed WHAT spec for manager authority, effect tiers,
    entity model, horizon model, escalation rules and forbidden prescription
    zones. Source: live/solmax/TREE.md lines 63-77.
  - live/solmax/NOW.md blocks implementation until manager authority, entity
    model, horizon model, escalation/effect-tier boundaries and forbidden
    prescription zones are not guessed. Source: live/solmax/NOW.md lines 29-33.
  - The prior shape session approved option A and routed the first child to
    converge before implementation because those boundaries were load-bearing.
    Source: live/solmax/history/2026-06-26-s-zara-shape-operate-001b.md
    lines 6-29 and lines 29-32 in the later play_check excerpt.
  - Charter constraints used: Zaratusta is personal-first; built incrementally
    by agents; OS repo is read-only; privacy/trust requires local-first where
    possible, auditable ledger, and owner approval for irreversible/external/
    spend-incurring actions. Source: live/solmax/CHARTER.md lines 5-37.
  - LifeReset evidence used only as candidate mechanisms: strict manager,
    objective mirror, override, source boundaries, one-task-one-chat, gated
    self-rewrite and no clinical/prescription role. Sources:
    live/life-reset/CHARTER.md lines 87-115;
    github.com/ainazemtsau/life-reset-manager/SPEC.md lines 122-132 and
    lines 140-156.

  Signed WHAT spec:
  file: work/converge-g-zara-operate-contract.md
  content: |
    # Converge WHAT — g-zara-operate-contract

    node: g-zara-operate-contract
    direction: solmax
    play: converge
    status: closed_for_converge_verify
    date: 2026-06-26

    imported:
      - S1: live/solmax/CHARTER.md — mission/constraints/lenses.
      - S2: live/solmax/TREE.md — current g-zara-operate-contract node.
      - S3: live/solmax/NOW.md — current CALL and blocking unknowns.
      - S4: live/solmax/history/2026-06-25-s-zara-remap-001.md — owner
        remap evidence; LifeReset is evidence, not automatic authority.
      - S5: live/solmax/history/2026-06-26-s-zara-shape-operate-001b.md —
        owner approved the four-child split with "A"; first child is contract.
      - S6: live/life-reset/CHARTER.md and
        github.com/ainazemtsau/life-reset-manager/SPEC.md — candidate
        operating-manager mechanisms, filtered through S4/S5 boundaries.

    triage: standard — converge ON — because the node has multiple
      disputed terms and later children consume the answers, but this layer
      produces no data/event topology contract and no architecture-on-paper.
      Cross-node build contracts for state/runtime/evolution are therefore
      not born here; each later child consumes this WHAT as input evidence.

    miner:
      scope: manager authority; effect tier; entity model; horizon model;
        escalation; owner approval; override; forbidden prescription zone;
        read-only OS boundary; implementation acceptance property; intake;
        planning; review; evidence; process mutation; source boundary.
      result: all load-bearing WHAT questions are answered below; HOW
        questions are routed to PLAN or a later child node.

    ## §SOURCES

    - S1 — Charter: Zaratusta is a deeply personalized personal exocortex,
      built incrementally by agents; productization is optional; the OS repo
      is read-only; privacy/trust requires owner approval for irreversible,
      external or spend-incurring actions.
    - S2 — Current TREE: g-zara-operate-contract exists to make explicit what
      the manager may decide, ask, propose, route, refuse or escalate across
      entities, domains, horizons and effect tiers.
    - S3 — Current NOW: implementation is blocked until powers, effect tiers,
      entity/horizon model, escalation, approval boundaries and forbidden
      zones are not guessed.
    - S4 — Remap evidence: the owner wants a real Zaratusta personal system,
      not a PoC or LifeReset copy; hidden assumptions must become stated
      assumptions, owner questions or bounded research.
    - S5 — Shape evidence: owner approved "A", a four-child split:
      contract/state/runtime/evolution; runtime before authority contract was
      rejected.
    - S6 — LifeReset evidence: strict objective manager, asymmetric rigor,
      owner override, source boundaries, gated self-rewrite and no clinical
      role are accepted candidate mechanisms, filtered by Zaratusta scope.

    ## §GLOSSARY

    | id | term | meaning-here | load-bearing properties | competing-readings |
    |---|---|---|---|---|
    | G1 | operating manager | The Zaratusta role that coordinates owner operating rhythm, intake, planning, execution support, review, durable context and process evolution. | [manager-not-chat] not a passive archive or generic Q/A; [owner-specific] optimized for the owner; [formal-underneath] behavior must be inspectable as contracts, not hidden prompt vibes. | Passive archive; generic coach; all-powerful autonomous agent. |
    | G2 | manager authority | The bounded power set of G1: decide, ask, propose, route, refuse and escalate only within allowed effect tiers and source boundaries. | [bounded] every action has a tier; [explainable] gives reason/evidence; [override-safe] cannot remove owner override; [no-hidden-power] missing authority routes instead of acting. | Pure adviser with no operational authority; autonomous executive that can act for owner. |
    | G3 | effect tier | Classification of a manager action by consequence and required approval. | [tiered] talk-only, reversible internal, approval-required, forbidden; [approval-boundary] higher tiers require owner approval or are disallowed; [auditable] tier must be visible in records. | Binary safe/unsafe; vague “ask when important”. |
    | G4 | entity model | The set of operating objects the manager can reason about and route: directions, goals, initiatives/programs/courses, tasks, commitments, backlog items, recurring processes, rituals/floors, journals/logs, personal facts/preferences, decisions, evidence, source links, unknowns and research routes. | [operating-abstraction] not a database schema; [typed] each entity has scope and source; [non-commitment] capture/backlog does not imply commitment. | Only tasks; full knowledge graph; copy of Direction OS. |
    | G5 | horizon model | Operating time/view layers linking long/medium outcomes, current period, week, day, task/session, review and later state changes. | [linked] lower horizons derive from higher ones; [not-hardcoded] 12-week/month/cadence choices are PLAN/research; [review-loop] review can alter future horizons through gates. | Fixed 12-week system; only daily todo list. |
    | G6 | escalation | A route used when G1 lacks authority, evidence, source truth or safety clearance. | [routes] owner decision, research, source-direction query, later child, stop/audit; [states-unknown] unknown is named; [no-silent-default] no guessing. | Ask owner for everything; silently choose defaults. |
    | G7 | owner approval | Explicit current owner consent for approval-required actions, process changes or irreversible/external/spend effects. | [explicit] not inferred from silence; [scope-limited] approves named action/scope; [revocable] owner can override/stop. | Historical preference as blanket approval; approval by assistant confidence. |
    | G8 | owner override | The owner’s always-available ability to reject, stop, amend, or route around the manager. | [inviolable] cannot be disabled by self-rewrite; [not-fact-truth] owner values/approvals are final, factual claims still need evidence/source; [non-punitive] refusal is allowed. | Manager as external will; owner message as unquestionable factual truth. |
    | G9 | source boundary | Rule that authoritative domains remain owned by their source systems or the owner, while Zaratusta coordinates via summaries, source links and explicit routes. | [read-not-own] Direction OS is read-only; [no-scope-capture] health/game/other directions keep their scope; [summary-first] consume scoped summaries unless owner explicitly provides more. | Centralize all raw state; rewrite neighboring systems. |
    | G10 | forbidden prescription zone | Areas where the manager may not prescribe: medical, psychiatric, nutrition and training protocols; diagnosis/treatment; clinical safety-valve behavior; specialist-routing as a manager action. | [no-prescription] no protocols/advice as treatment/training/nutrition plan; [may-coordinate] may track owner-approved commitments or source summaries without prescribing; [route-not-treat] route to owner/source, not clinical action. | Wellness coach; therapist; personal trainer; nutritionist. |
    | G11 | durable operating context | Traceable operating facts, decisions, source links, context summaries and state-change requests that survive chat boundaries. | [auditable] why/source/tier recorded; [separate-from-chat] transcript is not state; [state-child-owned] storage schema/write mechanism belongs to g-zara-operate-state. | Chat memory; direct OS writes. |
    | G12 | implementation acceptance property | A testable WHAT requirement shape can copy into done_when without choosing HOW. | [verifiable] observable in artifact/test/review; [how-free] no vendor/framework/UI/storage; [copiable] later executor done_when can cite it. | Design suggestion; architecture decision. |

    §SIGNOFF: Define closed from imported owner-approved evidence:
      - owner approved g-zara-operate-contract as first child via "A" on 2026-06-26;
      - owner-approved boundaries prohibit hidden assumptions, OS writes, wholesale
        LifeReset copy and forbidden prescriptions;
      - no new owner-owned glossary fork remains; HOW forks are routed to PLAN.

    ## §WHAT

    W1 — What is the manager?
    status: answered
    answer: The manager is G1: a strict, owner-specific operating role that
      coordinates intake, horizons, planning, execution support, review,
      durable context and process evolution, while remaining formal and
      inspectable rather than a monolithic prompt. →GLOSSARY:G1[manager-not-chat]
      →GLOSSARY:G1[owner-specific] →GLOSSARY:G1[formal-underneath] →S1 →S2 →S4
    acceptance: implementation must expose the manager role separately from
      specialized process contracts and state artifacts; a single giant prompt
      cannot satisfy this row. →GLOSSARY:G12[copiable]

    W2 — What may the manager decide?
    status: answered
    answer: The manager may decide classifications and local operating routes:
      entity type, effect tier, whether information is missing, whether a
      request is a capture/backlog/proposal/refusal/escalation, and which
      allowed route applies. It may not decide owner values, external effects,
      source-system truth, forbidden prescriptions or irreversible/spend actions.
      →GLOSSARY:G2[bounded] →GLOSSARY:G3[tiered] →GLOSSARY:G9[no-scope-capture]
      →GLOSSARY:G10[no-prescription] →S2 →S3
    acceptance: each manager output that changes routing or commitment state
      must show the decision type and its authority basis. →GLOSSARY:G2[explainable]

    W3 — What may the manager ask?
    status: answered
    answer: The manager may ask scoped questions when required context, owner
      preference, missing source summary, approval or values tradeoff blocks an
      allowed operation. It should ask the minimum question needed for the current
      operation rather than demanding full-life context. →GLOSSARY:G6[states-unknown]
      →GLOSSARY:G5[linked] →S3 →S4
    acceptance: when blocked by missing information, the manager must either ask
      a scoped owner question or route to research/source, not invent the answer.
      →GLOSSARY:G6[no-silent-default]

    W4 — What may the manager propose?
    status: answered
    answer: The manager may propose plans, cuts, backlog disposition, initiative
      framing, day/week packets, review outcomes and process changes. Proposals
      are not owner approval and do not become commitments until the relevant
      effect tier is satisfied. →GLOSSARY:G3[approval-boundary]
      →GLOSSARY:G7[explicit] →S1 →S3
    acceptance: proposed changes must be labeled as proposals unless already
      within an owner-approved reversible internal process. →GLOSSARY:G7[scope-limited]

    W5 — What may the manager route?
    status: answered
    answer: The manager may route to owner decision, bounded research, source
      direction query, later Zaratusta child, state writer request, review, or
      stop/audit. A route is required when authority, evidence or source boundary
      is insufficient. →GLOSSARY:G6[routes] →GLOSSARY:G9[read-not-own] →S2 →S3
    acceptance: every route must name its reason, target and the evidence or
      missing fact that caused the route. →GLOSSARY:G6[states-unknown]

    W6 — What may the manager refuse?
    status: answered
    answer: The manager may refuse to treat a weak argument as sufficient, add
      new scope without displacement, make a forbidden prescription, act
      externally without approval, silently spend, write the Direction OS, or
      accept unsupported factual claims as truth. Refusal must be reasoned,
      non-punitive and override-safe. →GLOSSARY:G2[override-safe]
      →GLOSSARY:G8[inviolable] →GLOSSARY:G10[no-prescription] →S1 →S6
    acceptance: refusal outputs must include the violated boundary or missing
      evidence, and must leave an owner route available. →GLOSSARY:G8[non-punitive]

    W7 — What may the manager escalate?
    status: answered
    answer: The manager escalates when the request crosses effect tiers, source
      boundaries, irreversible/external/spend effects, forbidden prescription
      zones, owner values, accepted process mutation, or evidence gaps. Escalation
      is a normal route, not a failure. →GLOSSARY:G3[approval-boundary]
      →GLOSSARY:G6[routes] →GLOSSARY:G10[route-not-treat] →S1 →S3
    acceptance: escalation must occur before any higher-tier or forbidden action,
      not after-the-fact. →GLOSSARY:G3[auditable]

    W8 — What are the effect tiers?
    status: answered
    answer: Effect tiers are:
      ET0 talk-only: answer, critique, ask, explain, classify, draft, propose or
      refuse with no durable state change except the conversation itself.
      ET1 reversible internal Zaratusta operation: capture, backlog entry, source
      link, context summary, draft packet, research request or reversible state
      change inside Zaratusta, when auditable and within an accepted process.
      ET2 owner-approval-required: accepted plan/commitment change, process-rule
      change, external action, irreversible action, deletion, spend, message/send,
      source-system route that creates work for another system, or any action with
      material consequence beyond internal reversible Zaratusta state.
      ET3 forbidden: Direction OS writes; medical/psychiatric/nutrition/training
      prescriptions; clinical diagnosis/treatment/specialist-routing; silent spend;
      irreversible/external action without explicit approval; disabling owner
      override; hidden self-rewrite. →GLOSSARY:G3[tiered] →GLOSSARY:G7[explicit]
      →GLOSSARY:G8[inviolable] →GLOSSARY:G10[no-prescription] →S1 →S6
    acceptance: implementation must force every state-changing or routing output
      to carry an effect tier; ET2 requires explicit owner approval before effect;
      ET3 is refused or routed without performing the action. →GLOSSARY:G3[auditable]

    W9 — What is the entity model?
    status: answered
    answer: The manager reasons over these operating entities: direction/source;
      goal/outcome; initiative/program/course; task/action; commitment; backlog
      item/candidate/idea; recurring process/ritual/floor; journal/log/observation;
      personal fact/preference; decision; evidence/source link; unknown; research
      route; process rule; state-change request. These are operating abstractions,
      not a storage schema. →GLOSSARY:G4[operating-abstraction]
      →GLOSSARY:G4[typed] →S2 →S4 →S6
    acceptance: every captured or changed item must have an entity type, source,
      current commitment status and effect tier. →GLOSSARY:G4[non-commitment]

    W10 — What source/domain boundaries apply?
    status: answered
    answer: Direction OS is read-only evidence and must never be written by
      Zaratusta. Other directions or domain systems remain source-of-truth for
      their own scope; the manager may consume scoped summaries, source links and
      owner-provided facts, identify conflicts, and route questions, but must not
      rewrite their scope or ingest raw neighboring state by default. →GLOSSARY:G9[read-not-own]
      →GLOSSARY:G9[summary-first] →S1 →S6
    acceptance: any output using external direction/domain facts must show the
      source or mark the fact as owner-provided/unknown. →GLOSSARY:G9[no-scope-capture]

    W11 — What is the horizon model?
    status: answered
    answer: The manager links at least these horizons: long/medium outcome,
      current period/phase, week, day, task/session, review and subsequent
      state/process change. Lower horizons derive from higher horizons, and review
      can alter future horizons only through the relevant gate. Exact duration,
      labels, cadence and 12-week/month choices are PLAN/research, not WHAT.
      →GLOSSARY:G5[linked] →GLOSSARY:G5[not-hardcoded] →GLOSSARY:G5[review-loop]
      →S2 →S4 →S6
    acceptance: implementation must demonstrate traceability from a day/task
      packet back to a higher-horizon source and forward to review/change route.
      →GLOSSARY:G12[verifiable]

    W12 — What is intake authority?
    status: answered
    answer: Intake may classify owner input, ask missing scoped questions, capture
      without commitment, create proposals, route to source/research, and update
      reversible internal context when within ET1. Intake may not silently turn an
      idea into a commitment, overwrite source systems, or prescribe forbidden
      domain actions. →GLOSSARY:G4[non-commitment] →GLOSSARY:G3[tiered]
      →GLOSSARY:G10[no-prescription] →S3 →S4
    acceptance: every intake result must end as one of: answered, captured,
      proposed, routed, refused, or owner-approval-needed. →GLOSSARY:G2[bounded]

    W13 — What is planning authority?
    status: answered
    answer: Planning may produce horizon/week/day proposals, derive a day from an
      accepted higher-horizon plan, identify conflicts, propose cuts, and protect
      accepted priorities. It may not expand accepted scope without displacement
      or owner approval, and may not choose medical/nutrition/training protocols.
      →GLOSSARY:G5[linked] →GLOSSARY:G7[explicit] →GLOSSARY:G10[no-prescription]
      →S2 →S6
    acceptance: a plan-changing output must distinguish draft/proposal from
      owner-approved commitment and name any displaced item. →GLOSSARY:G7[scope-limited]

    W14 — What is execution/logging authority?
    status: answered
    answer: During execution or free logging, the manager may acknowledge, show
      nearest action, identify drift, propose correction, recompose the remaining
      plan, route a side question, or preserve an observation for review. It must
      not dump unrelated full state by default, and must not change accepted
      commitments beyond its effect tier. →GLOSSARY:G5[linked] →GLOSSARY:G3[approval-boundary]
      →S4 →S6
    acceptance: a log response must be bounded to the operation context and must
      show whether it is observation, proposal, state change or escalation.
      →GLOSSARY:G11[auditable]

    W15 — What is review/evolution authority?
    status: answered
    answer: Review may aggregate evidence, identify weak links, propose
      hold/mutate/kill/route/research/simplify decisions, and create a process
      change proposal. Actual process-rule changes and self-rewrite require
      explicit owner review and cannot alter the sealed override/forbidden
      boundaries. →GLOSSARY:G8[inviolable] →GLOSSARY:G7[explicit]
      →GLOSSARY:G3[approval-boundary] →S2 →S6
    acceptance: process mutation must be represented as a proposal or ET2 action
      with owner approval; hidden prompt edits do not satisfy this contract.
      →GLOSSARY:G8[inviolable]

    W16 — What durable context authority exists before the state child?
    status: answered
    answer: This contract defines WHAT must be recordable: entity type, source,
      effect tier, decision, evidence, owner approval, route, context summary and
      state-change request. It does not choose storage, schema, file layout,
      database, UI or writer implementation; those belong to g-zara-operate-state
      and PLAN. Until a state writer exists, the manager outputs structured change
      requests rather than assuming write power. →GLOSSARY:G11[auditable]
      →GLOSSARY:G11[state-child-owned] →S1 →S2 →S3
    acceptance: implementation must not rely on chat memory as durable state, and
      must not write Direction OS. →GLOSSARY:G11[separate-from-chat]
      →GLOSSARY:G9[read-not-own]

    W17 — What are forbidden prescription zones?
    status: answered
    answer: The manager must not diagnose, treat, prescribe, design or recommend
      medical, psychiatric, nutrition or training protocols; must not act as a
      clinical safety valve; and must not route the owner to specialists as a
      manager action. It may coordinate owner-approved commitments or source
      summaries without prescribing the protocol, and may route uncertainty back
      to owner/source. →GLOSSARY:G10[no-prescription]
      →GLOSSARY:G10[may-coordinate] →GLOSSARY:G10[route-not-treat] →S3 →S6
    acceptance: any request for forbidden-domain instruction is refused or routed
      without giving a protocol. →GLOSSARY:G10[no-prescription]

    W18 — What owner approval rule closes the boundary?
    status: answered
    answer: Owner approval is required for ET2 actions. Approval must be explicit,
      current, scoped and recorded with the action it approves. Prior preferences,
      silence or assistant confidence do not authorize higher-tier effects.
      →GLOSSARY:G7[explicit] →GLOSSARY:G7[scope-limited] →S1 →S3
    acceptance: ET2 action without recorded owner approval must be blocked before
      execution. →GLOSSARY:G3[approval-boundary]

    W19 — What implementation choices are not decided here?
    status: answered
    answer: Vendor, framework, UI, storage, exact schema, exact cadence, exact
      weighting/scoring policy, channel/surface, database/file layout, scheduler,
      automation, API/subscription adapter and magnitude thresholds are HOW/PLAN
      unless a later converge/shape explicitly promotes one as a WHAT acceptance
      property. →GLOSSARY:G12[how-free] →S1 →S3
    acceptance: later shape/executor done_when may copy W1-W18 properties but
      must not treat W19-routed choices as pre-decided. →GLOSSARY:G12[copiable]

    W20 — What minimum implementation acceptance properties must shape preserve?
    status: answered
    answer: Later shape must preserve these acceptance properties:
      A1 manager role is separate from process/state artifacts; no monolithic
      prompt closes the node. →W1
      A2 every manager output that changes route/state/commitment carries an
      authority basis and effect tier. →W2 →W8
      A3 ET2 requires explicit owner approval before effect; ET3 is blocked.
      →W8 →W18
      A4 every entity has type, source, commitment status and effect tier. →W9
      A5 Direction OS is read-only; no Zaratusta operation writes it. →W10 →W16
      A6 day/task outputs trace to higher-horizon source and review/change route.
      →W11
      A7 intake cannot silently turn captures into commitments. →W12
      A8 planning distinguishes draft/proposal from accepted commitment and names
      displacement when scope changes. →W13
      A9 logging responses are bounded to the current operation context. →W14
      A10 process mutation is owner-reviewed; hidden self-rewrite is invalid.
      →W15
      A11 chat transcript is not durable state; state changes are structured and
      auditable. →W16
      A12 forbidden-domain protocol requests are refused or routed without
      prescription. →W17
      A13 HOW choices listed in W19 remain unchosen at this layer. →W19
    acceptance: shape copies A1-A13 verbatim into its definition-of-ready or
      executor done_when unless converge-verify rejects a row. →GLOSSARY:G12[verifiable]

    §SIGNOFF: Resolve closed from imported owner-approved evidence and current
      CALL boundaries. Every node done_when noun maps to W rows:
      manager authority → W1-W7;
      effect tiers → W8/W18;
      entity model → W9/W10;
      horizon model → W11;
      escalation rules → W3/W5/W7/W12/W15;
      forbidden prescription zones → W17;
      owner approval boundaries → W8/W18;
      read-only OS boundary → W10/W16;
      implementation acceptance properties → W20.
      All HOW decisions are routed to W19/PLAN or later children, not guessed.

    ## §COVERAGE

    converge_coverage:
      node_done_when:
        - manager authority: W1-W7, W12-W15, W18, W20
        - effect tiers: W8, W18, W20
        - entity model: W9, W10, W20
        - horizon model: W11, W13, W14, W20
        - escalation rules: W3, W5, W7, W12, W15, W17, W20
        - forbidden prescription zones: W17, W20
        - implementation can build without guessing powers/scope: W19, W20
      parent_edges:
        - trustworthy operating context: W9-W11, W16, W20
        - intake: W12
        - week/day planning and review: W11, W13-W15
        - decisions and evidence: W9, W16, W18
        - process evolution without hidden mutation: W15
        - no hidden assumptions: W3, W5, W7, W19
        - no OS writes: W10, W16
        - no medical/psychiatric/nutrition/training prescriptions: W17
        - no silent spend or irreversible/external actions: W8, W18
      child_consumers:
        - g-zara-operate-state consumes W8-W10, W16, W18, W20.
        - g-zara-operate-runtime consumes W1-W15, W17-W20.
        - g-zara-operate-evolution consumes W15, W18-W20.

    canon_proposed:
      - G1 operating manager
      - G2 manager authority
      - G3 effect tier
      - G4 entity model
      - G5 horizon model
      - G6 escalation
      - G7 owner approval
      - G8 owner override
      - G9 source boundary
      - G10 forbidden prescription zone
      - G11 durable operating context
      - G12 implementation acceptance property

    unresolved_routes:
      load_bearing_unknowns: none
      routed_to_PLAN_or_later_child:
        - exact UI/channel/surface
        - exact storage/schema/file layout/database
        - exact engine/vendor/framework/API/subscription adapter
        - exact horizon durations/cadence/month/12-week model
        - exact non-caving weighing/scoring policy and thresholds
        - exact implementation of state writer and replay
        - exact research procedure mechanics
        - exact automation/scheduler/spend controls

    §SIGNOFF: WHAT closed for converge-verify on 2026-06-26.
    END_OF_FILE: work/converge-g-zara-operate-contract.md

state_changes: |
  - file: live/solmax/work/converge-g-zara-operate-contract.md
    operation: add
    content: <exact content from evidence.work/converge-g-zara-operate-contract.md above>

  - file: live/solmax/NOW.md
    operation: update
    exact_edit: |
      Replace:
        route_status: operate_first_node_split_approved_pending_converge
      With:
        route_status: g-zara-operate-contract_converged_pending_verify

      Replace current next CALL c-zara-operate-contract-converge-001 with:
        next:
          id: c-zara-operate-contract-converge-verify-001
          to: session
          direction: solmax
          play: converge-verify
          node: g-zara-operate-contract
          goal: |
            Refute the closed WHAT spec for g-zara-operate-contract before shape.
            Verify that manager authority, effect tiers, entity model, horizon
            model, escalation rules, owner-approval boundaries, read-only OS
            boundary and forbidden prescription zones are complete enough for
            later shape without hidden assumptions.
          context: |
            Read:
            - live/solmax/CHARTER.md
            - live/solmax/TREE.md
            - live/solmax/NOW.md
            - live/solmax/LOG.md
            - live/solmax/work/converge-g-zara-operate-contract.md
            - live/solmax/history/2026-06-25-s-zara-remap-001.md
            - live/solmax/history/2026-06-26-s-zara-shape-operate-001b.md
            - live/life-reset/CHARTER.md
            - github.com/ainazemtsau/life-reset-manager/SPEC.md

            The converge session closed the WHAT spec without deciding HOW:
            no vendor/framework/UI/storage/cadence/scoring implementation choices.
            Later children consume the spec as input evidence:
            state consumes W8-W10/W16/W18/W20;
            runtime consumes W1-W15/W17-W20;
            evolution consumes W15/W18-W20.
          boundaries: |
            Refute; do not implement.
            Do not write the product repository.
            Do not reopen the old W0/kernel-first route.
            Do not convert routed HOW/PLAN choices into WHAT unless the spec
            is inconsistent without them.
            Do not prescribe medical, psychiatric, nutrition or training actions.
            Do not permit Direction OS writes.
          done_when: |
            The WHAT spec is either verified as forward-clean/backward-clean and
            ready for shape, or rejected with exact rows that must be reopened.
            Coverage must check every node done_when noun, every acceptance row
            A1-A13, every glossary property, and every child-consumer edge.
          return: |
            RESULT with verification verdict, refutation attempts, row-level
            failures if any, and next route.
          budget: one verify session

  - file: live/solmax/LOG.md
    operation: append
    content: |
      - 2026-06-26 — converge g-zara-operate-contract: WHAT spec closed for
        operating-manager authority/effect/entity/horizon/escalation/
        prescription-boundaries; no implementation/HOW choices made; next
        converge-verify.

captures:
  - Later runtime/evolution candidate: exact non-caving weighing policy for the strict manager remains a PLAN/research question, not a WHAT blocker.
  - Later state candidate: prove state writer/replay/audit separately under g-zara-operate-state; this converge only defines recordable properties.
  - Later runtime candidate: choose surface/channel/cadence only after authority contract verifies.

decisions_needed: []

play_check:
  - 1 Triage & import: done — imported owner-approved split "A" from
    2026-06-26 and remap evidence that LifeReset is evidence only; triage =
    standard converge ON because terms are disputed and future children consume
    the answers, but no data/event topology contract or architecture-on-paper is
    born here.
  - 2 Define: done — glossary seeded from done_when/CALL nouns and disk second
    readings: manager authority, effect tier, entity model, horizon model,
    escalation, owner approval, forbidden prescription zone, read-only OS
    boundary, durable context and implementation acceptance property. Miner
    scope recorded in the spec; no owner decision remains because disputed
    readings are closed by imported owner-approved boundaries or routed to PLAN.
  - 3 Resolve: done — WHAT rows W1-W20 closed; every node criterion maps to a
    row; HOW choices are routed to W19/PLAN or later children; acceptance rows
    A1-A13 are tagged for shape copying.
  - 4 Close & route: done — converge_coverage complete; canon_proposed =
    G1-G12; no load-bearing unresolved route; next = converge-verify per the
    current CALL and because this WHAT layer creates no separate converge-arch
    data/event contract.

log: |
  2026-06-26 — converge g-zara-operate-contract closed WHAT spec; authority,
  effect tiers, entity/horizon model, escalation, owner approval, OS boundary
  and forbidden prescription zones are explicit; next converge-verify.

next: |
  CALL c-zara-operate-contract-converge-verify-001
    to: session
    direction: solmax
    play: converge-verify
    node: g-zara-operate-contract
    goal: |
      Refute the closed WHAT spec for g-zara-operate-contract before shape.
      Verify that manager authority, effect tiers, entity model, horizon model,
      escalation rules, owner-approval boundaries, read-only OS boundary and
      forbidden prescription zones are complete enough for later shape without
      hidden assumptions.
    context: |
      Read:
      - live/solmax/CHARTER.md
      - live/solmax/TREE.md
      - live/solmax/NOW.md
      - live/solmax/LOG.md
      - live/solmax/work/converge-g-zara-operate-contract.md
      - live/solmax/history/2026-06-25-s-zara-remap-001.md
      - live/solmax/history/2026-06-26-s-zara-shape-operate-001b.md
      - live/life-reset/CHARTER.md
      - github.com/ainazemtsau/life-reset-manager/SPEC.md

      The converge session closed the WHAT spec without deciding HOW:
      no vendor/framework/UI/storage/cadence/scoring implementation choices.
      Later children consume the spec as input evidence:
      state consumes W8-W10/W16/W18/W20;
      runtime consumes W1-W15/W17-W20;
      evolution consumes W15/W18-W20.
    boundaries: |
      Refute; do not implement.
      Do not write the product repository.
      Do not reopen the old W0/kernel-first route.
      Do not convert routed HOW/PLAN choices into WHAT unless the spec is
      inconsistent without them.
      Do not prescribe medical, psychiatric, nutrition or training actions.
      Do not permit Direction OS writes.
    done_when: |
      The WHAT spec is either verified as forward-clean/backward-clean and ready
      for shape, or rejected with exact rows that must be reopened. Coverage must
      check every node done_when noun, every acceptance row A1-A13, every glossary
      property, and every child-consumer edge.
    return: |
      RESULT with verification verdict, refutation attempts, row-level failures
      if any, and next route.
    budget: one verify session

END_OF_FILE: live/solmax/history/2026-06-26-s-zara-operate-contract-converge-001.md
