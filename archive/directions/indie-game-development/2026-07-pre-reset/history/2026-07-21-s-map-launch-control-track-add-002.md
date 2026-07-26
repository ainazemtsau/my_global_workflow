RESULT s-map-launch-control-track-add-002 (call: owner-message-2026-07-21-launch-control-process-authority)
direction: indie-game-development
track: launch-control
play: map
node/task: g-b847/track-add-v2
owner_approved: 2026-07-21 — owner said `Можем сохранять его` after requiring that Demo & Launch Control retain all previously accepted responsibilities, use the compatibility limit for now, and explicitly own evidence-driven customization of the operating workflow.

outcome: |
  `g-b847 / Demo & Launch Control` is owner-approved as a root-level parallel
  service track under the indie-game-development outcome.

  This packet is the definitive replacement for the earlier un-applied chat draft
  `s-map-launch-control-track-add-001`. The earlier draft must not be relayed or
  applied separately.

  Demo & Launch Control owns the release-level connection between:
  - the selected Steam Next Fest/demo target and fallback;
  - the owner-approved Demo Contract;
  - cross-track release requirements;
  - dependency and date-determining work;
  - forecast, risks, named cuts and dated gates;
  - daily owner/AI dispatch;
  - evidence-driven adaptation of the management workflow itself.

  The owner-approved Release Directive authority is preserved. Launch Control may
  define the release need, affected gate, priority, required outcome, evidence and
  latest useful date. It may not directly rewrite another track's plan or select that
  track's technical implementation. The target track preserves its authority and
  returns `ACCEPT | COUNTER | BLOCKED` through lawful Direction OS routes.

  Launch Control also receives bounded Process Adaptation Authority. Based on actual
  throughput, review backlog, collisions, blocker age, forecast errors and owner
  friction, it may propose and, after the required owner approval, revise its own:
  - Daily Command format and cadence;
  - event-driven refresh rules;
  - dispatch lanes and safe-parallelism model;
  - review-throughput protections;
  - Release Directive representation;
  - management-dashboard fields and wording;
  - risk, cut and gate operating rules;
  - capacity and prioritization model.

  Process Adaptation Authority does not permit direct edits to `os/**`, KERNEL,
  plays, packet schema, writer validation, product-repository process authority or
  another track's internal plan. When a problem requires such a change, including
  replacement of the numeric `track_wip_limit` mechanism, Launch Control must return
  an evidence-backed maintenance proposal for a separate owner-authorized OS
  maintenance session.

  `track_wip_limit` is set to `99` only as a non-operational compatibility ceiling
  required by the current track-mode schema. It is not a target, capacity estimate,
  slot count, workload indicator or dispatch input. No owner-facing view may describe
  the project as `X/99`, and no work is started merely because the ceiling allows it.

  Actual working load is determined dynamically by Launch Control from:
  - one current owner-primary focus;
  - genuinely parallel-safe AI or executor work;
  - serial or collision-risk work;
  - current review backlog and decision demand;
  - dependencies and blocker conditions;
  - the capacity to inspect and accept returned evidence.

  A separate management dashboard remains part of the accepted outcome. Its main
  screen uses ordinary Russian and explains implications for the game and the current
  day. CALL ids, node ids, commits, paths, architecture terminology and the numeric
  compatibility ceiling remain optional traceability details only.

  The accepted operating order remains:
  1. Stabilization Baseline, Dispatch & Process-Adaptation Contract;
  2. one manual Daily Command dry run against live state;
  3. separate Management Dashboard v1 built from fields proven by the dry run;
  4. recurring morning control and event-driven dispatch refresh.

  Only step 1 is opened now. No management dashboard, recurring entry, Release
  Directive, maintenance CALL, product mutation or cross-track plan amendment is
  created by this map.

  The launch-control baseline root becomes NOW.next. The existing Grid correction
  root remains READY and all other current calls, decisions and statuses are
  preserved.

evidence: |
  Owner evidence:
  - Initial need: `ввести какой-нибудь отдельный трек, условно, менеджмент`,
    which would build global plans, examine risks and dates, control scope and keep
    the Steam Fest demo goal on course.
  - Track choice: `я согласен с рекомендованным вариантом`.
  - Dashboard requirement: the owner explicitly requested a second dashboard focused
    on global management rather than implementation detail.
  - Daily-dispatch requirement: the owner requested a morning document recommending
    which tracks to launch, what each should achieve that day, what can run in
    parallel and what should remain the primary focus.
  - Cross-track authority requirement: the owner clarified that Launch Control should
    be able to send release requirements to participating tracks when strategy changes,
    without directly rewriting their plans.
  - Exact Release Directive verdict:
    `принять карточку с Release Directive authority`.
  - Dashboard-language requirement: ordinary language, avoiding technical terminology
    and internal codes on the main screen.
  - Numeric-limit correction: the owner rejected treating the old `9` as real capacity
    and stated that actual workload should be decided inside the new track.
  - Compatibility-ceiling acceptance: `окей, с этим лимитом`.
    This packet interprets those words as approval of the proposed hidden technical
    ceiling `99`, not as approval of a real ninety-nine-work-item load.
  - Process-adaptation requirement:
    `в треке еще отдельно пропишем, что он может кастомизировать рабочий процесс`,
    so that it can make the operating model maximally effective.
  - Future-limit handling:
    if the compatibility mechanism causes a real problem, the owner wants the track
    to be able to reconstruct the approach rather than preserve it permanently.
  - Final G9 close: `Можем сохранять его`.

  Current Direction and OS evidence:
  - Fresh `TREE.md` blob `505e10494d6a0b67d5a096785e435244053f8472`
    contains no `g-b847`.
  - Fresh `NOW.md` blob `78c8400ef6bb8bcde49dd2af29a4e06467412065`
    contains no launch-control track or root and currently records
    `track_wip_limit: 9`.
  - Repository searches found no committed `g-b847`, no committed
    `c-work-launch-control-stabilization-baseline-001` and no committed history for
    the earlier chat draft, so this packet is the only track-add RESULT to apply.
  - Existing history states that `9` was introduced only because the schema required
    a positive ceiling; it was explicitly not a recommendation to fill nine slots.
  - KERNEL G1 and current writer validation still require a positive owner-approved
    `track_wip_limit` in track mode. Removing or making it nullable requires an OS
    maintenance change, not a Direction track RESULT.
  - Program's accepted route owns technical Integration Lab progress and capability
    intake. It does not own the full release calendar, Demo Contract, daily capacity
    dispatch or adaptation of the management operating model.
  - Current `LOG.md` has an intact `END_OF_FILE` marker.

  Strategic evidence reused by the track-add fast path:
  - The completed owner-requested research compared critical-path scheduling,
    rolling-wave planning, continuous risk management, WIP/ageing control, dated
    decision gates and visual Obeya-style control.
  - The resulting recommendation was a separate Demo & Launch Control authority,
    not generic management bureaucracy and not an expansion of Integration Lab.
  - The current Program route tracks technical capability acceptance but does not
    own the complete release calendar, demo cuts, dynamic AI dispatch or management
    process improvement.

state_changes: |
  Apply atomically against fresh current state. Use node, track, call and decision ids
  as semantic anchors. Preserve all concurrent changes outside the declared intent.

  live/indie-game-development/TREE.md:
    - In the existing `owner_approved:` ledger, APPEND exactly once:
      `2026-07-21 — history/2026-07-21-s-map-launch-control-track-add-002.md
      («Можем сохранять его», g-b847 parallel)`.

    - UPSERT by stable id `g-b847` as a direct child of root `g-a7f2`, positioned
      after `g-d3a8` and before `g-c5d1`.
      If absent, ADD the card below.
      If an earlier compatible chat-draft version was applied concurrently, UPDATE
      only this node's declared fields to the complete card below and preserve any
      unrelated current TREE changes:

        - id: g-b847
          goal: "Demo & Launch Control: выбранная стратегия демо и Steam Next Fest остаётся исполнимой через понятный Demo Contract, связанную цепочку обязательных результатов, динамический owner/AI dispatch и адаптируемый по evidence управляющий процесс."
          done_when: |
            Целевой фестиваль и fallback приняты; Demo Contract задаёт player promise, MUST/SHOULD/CUT, quality floor, explicit non-goals и внешний acceptance; цепочка работ, определяющая дату демо, forecast, top risks, cuts и gates остаются актуальными; Launch Control формулирует Release Directives, а целевые треки отвечают ACCEPT/COUNTER/BLOCKED через существующие CALL/RESULT routes; отдельный management dashboard обычными словами показывает курс и Today Command; фактическая нагрузка определяется динамически по owner-focus, безопасной AI-параллельности, review throughput, зависимостям и collisions; собственный управляющий процесс пересматривается по evidence о throughput и friction, а изменения os/** маршрутизируются в отдельную owner-authorized maintenance session.
          why: Без отдельного владельца календаря, demo scope, cross-track demand, ежедневной AI-capacity и адаптации управляющего процесса качественная локальная работа может не сложиться в демо к выбранной дате.
          status: parallel
          detail: history/2026-07-21-s-map-launch-control-track-add-002.md

    - If `g-b847.detail` already contains a compatible earlier track-add history
      pointer, preserve it and append the new authoritative pointer rather than
      deleting historical evidence.
    - Preserve root `g-a7f2`, every existing node, parent relationship, status,
      done_when and detail outside `g-b847` unchanged.
    - Postcondition: exactly one `g-b847` exists as a direct child of `g-a7f2`.

  live/indie-game-development/NOW.md:
    - SET `updated` to:
      `2026-07-21 by s-map-launch-control-track-add-002`.

    - SET `track_wip_limit` from `9` to `99`.
      - If fresh current state is already `99`, this is a no-op.
      - The value is a compatibility ceiling only.
      - Do not add occupancy prose, `X/99`, slot language or a recommendation to
        fill available positions.
      - If fresh current state has a different later owner-approved value, do not
        overwrite it silently; report the semantic conflict.

    - In `tracks`, UPSERT by id `launch-control`, directly after `program`:

      `{id: launch-control, label: "Demo & Launch Control", mode: parallel, for: g-b847}`.

    - In `open_calls`, UPSERT by stable call id
      `c-work-launch-control-stabilization-baseline-001`:

        - id: c-work-launch-control-stabilization-baseline-001
          track: launch-control
          status: ready
          to: session
          for: "g-b847 / owner-present Stabilization Baseline, Dispatch & Process-Adaptation Contract"
          issued: 2026-07-21
          call: work/launch-control/c-work-launch-control-stabilization-baseline-001-call.md
          receipts:
            - history/2026-07-21-s-map-launch-control-track-add-002.md
          note: "READY / DEFAULT / OWNER-PRESENT / PLANNING ONLY / NO DASHBOARD YET / NO DIRECTIVE DISPATCH / NO OS MUTATION. First establish one owner-approved release baseline: Demo Contract, target and fallback, dependency network, resource-constrained forecast, risks, cuts, gates, lawful Release Directive representation, dynamic owner/AI capacity rules, bounded Process Adaptation Authority and a plain-language dashboard specification. The numeric WIP value is compatibility-only and is not a capacity model."

    - If the compatible call already exists from an earlier applied draft:
      - preserve compatible current receipts and append the new history receipt once;
      - update `for`, `call` and `note` to the complete meanings above;
      - do not create a second launch-control root.

    - SET `next.call` to:
      `c-work-launch-control-stabilization-baseline-001`.

    - KEEP `c-work-grid-v1-document-authority-correction-001` READY and unchanged,
      but it is no longer the default.

    - KEEP `bet: null`, `tasks: []` and `recurring: []`.

    - Preserve every unrelated track, call, receipt, decision and status.

    - Do not calculate or record a real workload from the number of registered roots,
      waiting calls, blocked calls, paused calls or pending decisions.

    - Postcondition:
      - `track_wip_limit: 99` exists solely to satisfy current schema;
      - actual working load remains undefined until the launch-control baseline
        accepts a dynamic capacity model;
      - no existing track is paused or dropped merely to add launch-control.

  live/indie-game-development/work/launch-control/c-work-launch-control-stabilization-baseline-001-call.md:
    - CREATE if absent with the exact complete content below.
    - If the exact earlier chat-draft version exists, REPLACE the whole file with the
      exact complete content below.
    - If another materially different current version exists, stop and report a
      semantic conflict rather than merging procedure meanings silently.

        CALL c-work-launch-control-stabilization-baseline-001
        to: session
        direction: indie-game-development
        track: launch-control
        play: work
        node: g-b847
        task: stabilization-baseline
        issued: 2026-07-21 (s-map-launch-control-track-add-002)

        goal: |
          У владельца есть принятый Stabilization Baseline, Dispatch &
          Process-Adaptation Contract, который превращает цель Steam Next Fest
          в понятный Demo Contract, сравнимые календарные стратегии, связанную
          цепочку обязательных результатов, evidence-backed forecast, risk/cut
          model, динамический cross-track dispatch и адаптируемый управляющий процесс.

        context: |
          Read fresh:
          - `live/indie-game-development/CHARTER.md`
          - `live/indie-game-development/TREE.md`
          - `live/indie-game-development/NOW.md`
          - `live/indie-game-development/work/program-v2-integration-lab-plan.md`
          - `live/indie-game-development/history/2026-07-21-s-map-launch-control-track-add-002.md`
          - current accepted Canon, Marketing and capability-track evidence needed
            to distinguish demo-blocking decisions from full-game work.

          Refresh the current official Steam event dates and eligibility first-hand.
          Preserve the Charter money gate `2026-12-11`.

          Owner-approved operating boundaries:
          - Demo & Launch Control is separate from Integration Lab.
          - Program owns technical Integration Lab routing and capability acceptance.
          - Launch Control owns release strategy, demo scope, date-oriented
            prioritization, daily dispatch and adaptation of its own operating model.
          - A separate management dashboard is wanted, but it is a read-only view,
            not a source of truth.
          - Its main screen uses ordinary Russian and remains understandable without
            CALL ids, node ids, commits, architecture terms or OS terminology.
          - Launch Control owns release need, priority, affected gate, required
            outcome, evidence and useful date.
          - Target tracks own implementation and may answer
            `ACCEPT | COUNTER | BLOCKED`.
          - One owner-primary focus is combined with a dynamic number of genuinely
            parallel-safe AI sessions; dispatch may refresh after results or blockers.
          - `track_wip_limit: 99` is a compatibility ceiling required by the current
            schema. It is not workload, capacity, quota, slot count or a dashboard
            metric.
          - Actual load is determined from primary focus, parallel safety, review
            throughput, dependencies, collisions, owner decisions and returned work.
          - Launch Control may adapt its own cadence, dispatch model, dashboard fields,
            review controls, Release Directive form, risk/cut rules and replan triggers
            when evidence shows a better operating model.
          - Launch Control does not directly edit `os/**`, KERNEL, plays, packet
            schema, writer validation, another track's plan or product process
            authority.
          - When improvement requires an OS-level change, including replacement of
            the numeric WIP mechanism, Launch Control returns an evidence-backed
            proposal for a separate owner-authorized maintenance session.
          - Accepted order:
            baseline → manual Daily Command dry run → management dashboard v1
            → recurring morning and event-driven control.

          `Release Directive` and `Process Adaptation` are operating concepts, not
          additional Direction OS packet types. Their lawful representation must use
          existing work artifacts, CALL/RESULT packets, owner routing and target-track
          or maintenance admission rules.

        boundaries: |
          Owner-present planning and co-creation only.

          Do not mutate any product repository, code, test, scene, asset or product doc.
          Do not edit another track's master plan, technical contract or current CALL.
          Do not issue an engineering CALL or launch any currently READY implementation.
          Do not create the management dashboard in this session.
          Do not add a recurring entry or run a Daily Command yet.
          Do not dispatch a Release Directive yet.
          Do not edit `os/**`, KERNEL, plays, packet schema or writer validation.
          Do not issue an OS maintenance change from inside this work CALL.
          Do not invent a third packet type or an illegal cross-track child CALL.
          Do not change current call statuses or silently decide Canon questions.
          Do not claim that October is feasible or impossible before the linked
          baseline and explicit assumptions support that conclusion.
          Do not treat `track_wip_limit: 99` as capacity, show `X/99`, recommend
          filling available slots or block a useful dispatch merely because of an
          invented occupancy interpretation.
          Do not expose internal codes as primary owner-facing dashboard language;
          they may exist only as optional evidence links.

        done_when: |
          1. One owner-approved artifact exists at
             `work/launch-control/stabilization-baseline.md`, written primarily in
             ordinary Russian and naming its owner inputs, state evidence and
             external sources.

          2. The artifact compares the live target and fallback strategies using
             freshly verified official event dates, the `2026-12-11` money gate,
             explicit assumptions and dated owner decision gates.

          3. A Demo Contract defines the player promise, session shape, mandatory
             player-visible proof, `MUST / SHOULD / CUT`, quality floor, explicit
             non-goals and external acceptance method.

          4. A backward milestone network connects festival-ready evidence to
             Program, Canon, Grid, Gas, Character, Level, Presentation and Marketing
             only where each is actually required.

          5. A resource-constrained chain identifies what currently determines the
             demo date, near-determining work, owner-attention constraints, safe
             parallelism, collision risks and optimistic/likely/conservative ranges.

          6. Facts, active issues, assumptions and future risks are separated.
             Top risks have observable signals, prevention, contingency, named cuts
             and latest useful decision dates.

          7. The Release Directive contract is mapped onto existing Direction OS
             CALL/RESULT and target-track admission rules. It defines
             `ACCEPT | COUNTER | BLOCKED` without direct cross-track plan mutation
             or a new packet type.

          8. The initial dynamic owner/AI capacity model is accepted:
             - one primary focus;
             - a variable number of genuinely parallel-safe launches;
             - serial/collision-risk work;
             - queue-next work;
             - review and owner-decision load;
             - event-driven refill conditions.
             The model explicitly ignores the numeric compatibility ceiling as a
             workload or dispatch input.

          9. A Process Adaptation Contract is accepted. It states:
             - which Launch Control operating artifacts and rules it may revise;
             - which evidence can trigger a revision;
             - how owner approval and history are preserved;
             - how changes are evaluated against throughput and demo progress;
             - which boundaries require target-track work;
             - which boundaries require a separate OS maintenance session;
             - how the numeric WIP mechanism will be escalated if it ever blocks or
               distorts useful work.

          10. A plain-language field specification is accepted for the future separate
              management dashboard. Every field answers a practical owner question;
              technical identifiers and the compatibility ceiling remain optional
              traceability only.

          11. One first internal gate and one lawful ready successor CALL are returned
              for a manual Daily Command dry run. No dashboard or recurring control
              is created before that dry run is reviewed.

          12. The owner accepts or corrects the complete baseline in actual words.
              Without owner acceptance, the launch-control root remains at the same
              planning position and no downstream control mechanism is opened.

        return: |
          One work RESULT containing the accepted baseline artifact path; exact owner
          words; target/fallback verdict; established facts versus assumptions;
          Demo Contract; determining and near-determining chains; risk/cut table;
          lawful Release Directive representation; dynamic capacity rules;
          Process Adaptation Contract; dashboard field specification; first dated
          gate; and exactly one manual Daily Command dry-run successor or one exact
          blocker.

        budget: one fresh owner-present planning session
        surface: owner-present

        END_OF_FILE: live/indie-game-development/work/launch-control/c-work-launch-control-stabilization-baseline-001-call.md

  live/indie-game-development/LOG.md:
    - APPEND exactly once immediately before the existing `END_OF_FILE` marker:

      `2026-07-21 · s-map-launch-control-track-add-002 · map · launch-control · g-b847/track-add-v2: owner approved Demo & Launch Control with Release Directive and bounded Process Adaptation authority, a separate plain-language management dashboard, stabilization-first ordering and dynamic daily/event-driven AI dispatch; track_wip_limit becomes a hidden compatibility ceiling of 99 rather than capacity, one planning-only baseline root becomes default, Grid stays READY, and no dashboard, recurring control, directive, maintenance or product work starts. → history/2026-07-21-s-map-launch-control-track-add-002.md`

  live/indie-game-development/history/2026-07-21-s-map-launch-control-track-add-002.md:
    - CREATE only if absent.
    - SAVE this complete RESULT exactly once.
    - ADD final trailer:
      `END_OF_FILE: live/indie-game-development/history/2026-07-21-s-map-launch-control-track-add-002.md`

  live/indie-game-development/work/program-v2-integration-lab-plan.md:
    - NO CHANGE.
    - Program remains technical Integration Lab and capability-intake authority.

  live/indie-game-development/work/board/dashboard.html:
    - NO CHANGE.
    - It remains the Implementation & Product Proof view.

  live/indie-game-development/work/launch-control/dashboard.html:
    - DO NOT CREATE.
    - Its structure is designed during the baseline and implementation follows only
      after the manual Daily Command dry run.

  live/indie-game-development/CHARTER.md:
    - NO CHANGE.

  os/**:
    - NO CHANGE.
    - Any future replacement of the numeric WIP mechanism requires a separate
      owner-authorized maintenance session.

  All product, canon and marketing repositories and all unrelated
  Direction work/history/knowledge files:
    - NO CHANGE.

captures: []

decisions_needed: []

play_check:
  - "1 Recite: done — the Steam commercial-game mission, money gate, playable/craft criteria, current Integration-led technical structure and missing release-control owner were restated."
  - "2 Candidates & evidence (owner): done — owner candidates were global planning, dates, risks, cuts, daily dispatch, a separate management dashboard and cross-track release requirements; the owner explicitly requested and received deep research. The track-add fast path reused current CHARTER/TREE/NOW, Program evidence and that research."
  - "3 Skeleton (owner): done — the whole route was shown as Demo & Launch Control → Stabilization Baseline → manual Daily Command → separate dashboard → recurring/event-driven refresh. Owner accepted the route."
  - "4 Cards: done — g-b847 has an outcome, verifiable done_when, root-success why, owner/AI edge, Release Directive boundary, Process Adaptation boundary and management-overproduction risk."
  - "5 Per-node verdict (owner): done — exact owner words: `принять карточку с Release Directive authority`; later amendment: `в треке еще отдельно пропишем, что он может кастомизировать рабочий процесс`."
  - "6 Order (owner): done — owner accepted stabilization first, then one live Daily Command dry run, then dashboard, then recurring/event-driven control."
  - "7 Depth check: done — only one root-level parallel outcome and one bounded root CALL are created; no child nodes, implementation legs, dashboard, recurring obligation, directive or maintenance task is pre-created."
  - "8 Lens sweep: done — commercial/traction is covered by target, gates and money-route control; core gameplay by Demo Contract and player-visible proof; co-op by requiring evidence before claims; technical feasibility by dependency/collision/risk modelling while preserving track authority; scope/production by MUST/SHOULD/CUT, dynamic capacity and named cuts; audience workflow by binding demo/store/Marketing needs to the release route. No additional node is required."
  - "9 Close (owner): done — exact final owner words `Можем сохранять его`; `окей, с этим лимитом` accepts the proposed compatibility ceiling for now, while the owner requires Launch Control to reconstruct the approach later if evidence shows the mechanism is harmful."

log: 2026-07-21 · s-map-launch-control-track-add-002 · map · launch-control · g-b847/track-add-v2: owner approved Demo & Launch Control with Release Directive and bounded Process Adaptation authority, a separate plain-language management dashboard, stabilization-first ordering and dynamic daily/event-driven AI dispatch; track_wip_limit becomes a hidden compatibility ceiling of 99 rather than capacity, one planning-only baseline root becomes default, Grid stays READY, and no dashboard, recurring control, directive, maintenance or product work starts. → history/2026-07-21-s-map-launch-control-track-add-002.md

next: |
  CALL c-work-launch-control-stabilization-baseline-001
  to: session
  direction: indie-game-development
  track: launch-control
  play: work
  node: g-b847
  task: stabilization-baseline
  status: ready
  artifact: work/launch-control/c-work-launch-control-stabilization-baseline-001-call.md
  goal: У владельца есть принятый Stabilization Baseline, Dispatch & Process-Adaptation Contract, превращающий цель Steam Next Fest в Demo Contract, сравнимые стратегии, связанную цепочку обязательных результатов, evidence-backed forecast, risk/cut model, динамический cross-track dispatch и адаптируемый управляющий процесс.
  default: yes

END_OF_FILE: live/indie-game-development/history/2026-07-21-s-map-launch-control-track-add-002.md
