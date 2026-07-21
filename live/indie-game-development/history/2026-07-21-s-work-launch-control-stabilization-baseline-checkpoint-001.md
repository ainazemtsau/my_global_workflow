RESULT s-work-launch-control-stabilization-baseline-checkpoint-001 (call: c-work-launch-control-stabilization-baseline-001)
direction: indie-game-development
track: launch-control
play: work
node/task: g-b847/stabilization-baseline

outcome: |
  The current owner-present stabilization-baseline session is closed as an
  explicit checkpoint after repeated correction failure on the same point.

  No Stabilization Baseline is claimed accepted, and
  `work/launch-control/stabilization-baseline.md` is not created or changed.

  The Launch Control root itself remains valid and at the same planning
  position. The failure was session execution:

  - the conversation descended from release strategy into demo-mechanics
    design;
  - one subordinate topic (`hook` / later validation evidence) displaced the
    calendar, milestones, forecast, risks, cuts, dispatch and daily operating
    loop;
  - jargon and repeated micro-decisions obscured the complete route;
  - the owner could not see how work would start and how the project would be
    controlled each day.

  A fresh same-position successor is therefore established with a corrected
  recovery contract. It must present one coherent plain-language release
  strategy and the complete baseline draft, rather than reopening individual
  gameplay questions.

  The recovered operating intent is:

  - one release target, fallback and money gate;
  - release-level milestones with dated decision gates;
  - one chain that currently determines the earliest demo date;
  - optimistic / likely / conservative forecast ranges with assumptions;
  - track-level required outcomes, owners, dependencies and blockers;
  - one owner-primary focus plus a variable number of genuinely
    parallel-safe AI launches;
  - one short Daily Command each morning and event-driven refresh after
    results or blockers;
  - explicit risks, cuts and replan conditions;
  - a plain-language read-only dashboard;
  - evidence reduced at owner level to `confirmed | not confirmed`, not a
    separate design workshop;
  - gameplay mechanics, hook construction, floor-loop details and validation
    instrument design routed to Canon, Marketing or capability tracks at the
    appropriate later gate.

  Candidate first internal gate for the complete draft to evaluate and ask
  the owner to accept or correct:

  `2026-07-26 — Launch Control is operational: baseline accepted, one manual
  Daily Command completed, the first lawful work wave selected/launched,
  current truth/next outcome/range/blocker/collision known for every
  demo-critical track, and the first date-determining chain plus scenario
  forecast exists.`

evidence: |
  Owner recovery requirements, actual words:

  - `я же создавал глобального стратега, который, блядь, приведет нас к релизу`
  - `мы создадим какую-то стратегию, там, milestone'ы пропишем или ещё что-то`
  - `я с утра тебя запустил, чтобы обновили dashboard, понятно, что делать, пошли`
  - `нам нужно много параллельной работы запустить`
  - `всё, что я говорю, это не требование`
  - `ты полностью отвечаешь за бизнес`
  - `мы не хотим куда-то сильно углубляться, делать чью-то работу, потому что нам нужно глобально планировать и держать фокус`

  Owner inputs already obtained and preserved as inputs rather than silently
  broadened requirements:

  - `1A`: October remains a conditional target; February is an accepted
    fallback.
  - `2A`: the public demo requires real co-op proof on at least two machines;
    final eight-player proof remains a later product gate.
  - `4A`: the demo is a small but publicly reliable slice.
  - The demo may use a compact preparation / expedition-selection frame and
    focus on the expedition, but exact gameplay scope and mechanics must be
    worked by Canon rather than frozen by Launch Control.
  - Sphere-based gas extraction remains a leading accepted design anchor, not
    permission for Launch Control to specify controls, gas grammar, roster,
    level conditions or implementation.
  - Owner ideas and examples are hypotheses until an explicit owner verdict.

  Direction evidence:

  - `live/indie-game-development/history/2026-07-21-s-map-launch-control-track-add-002.md`
    already assigns Launch Control release strategy, demo scope, calendar,
    daily dispatch, risk/cut control, Release Directives, dashboard and
    evidence-driven process adaptation.
  - The same accepted map fixes the order:
    baseline → manual Daily Command → dashboard → recurring/event-driven
    control.
  - The returning CALL requires one complete baseline, backward milestone
    network, resource-constrained forecast, risks/cuts, lawful directives,
    dynamic capacity, process adaptation, dashboard fields and one dry-run
    successor.
  - `work/program-v2-integration-lab-plan.md` currently records 2/10 accepted
    Program milestones and eight remaining capability/integration milestones.
  - `os/plays/work.md` requires a checkpoint and fresh handoff after two
    failed correction rounds on the same point.

  Fresh official external sources checked on 2026-07-21:

  - Steam Next Fest October 2026:
    https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/2026october
    Event 2026-10-19 through 2026-10-26; registration 2026-08-31;
    required-item review submission 2026-10-05; public store page and demo
    required; one Next Fest participation per title.
  - Steam Next Fest February 2027:
    https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/feb_2027
    Event 2027-02-22 through 2027-03-01; registration 2027-01-10;
    required-item review submission 2027-02-08.
  - CHARTER money gate remains 2026-12-11.

state_changes: |
  Apply atomically against fresh current state using stable ids. Preserve all
  unrelated tracks, calls, decisions, receipts and concurrent updates.

  live/indie-game-development/NOW.md:

  1. SET `updated` to:
     `2026-07-21 by s-work-launch-control-stabilization-baseline-checkpoint-001`.

  2. REMOVE returning root open_call by exact id:
     `c-work-launch-control-stabilization-baseline-001`.

  3. ADD exactly one same-position root successor if absent:

       - id: c-work-launch-control-stabilization-baseline-recovery-001
         track: launch-control
         status: ready
         to: session
         for: "g-b847 / fresh recovery of the complete plain-language release-control baseline"
         issued: 2026-07-21
         call: work/launch-control/c-work-launch-control-stabilization-baseline-recovery-001-call.md
         receipts:
           - history/2026-07-21-s-work-launch-control-stabilization-baseline-checkpoint-001.md
         note: "READY / DEFAULT / FRESH-SESSION RECOVERY / OWNER INPUTS COMPLETE. Present one coherent release strategy and full baseline draft; do not reopen gameplay mechanics, hook frameworks or validation-instrument design. The artifact must show target/fallback, release milestones, first five-day gate, current date-determining chain, scenario forecast, risks/cuts, track obligations, Daily Command, dynamic parallelism, process adaptation and dashboard fields in ordinary Russian. No dispatch, dashboard, recurring control, product mutation or OS change before owner acceptance."

  4. SET `next.call` to:
     `c-work-launch-control-stabilization-baseline-recovery-001`.

  5. Preserve `track_wip_limit: 99` solely as the existing compatibility
     ceiling. Do not derive load or occupancy from it.

  6. Preserve every unrelated open call and decision, including their current
     statuses and receipts.

  live/indie-game-development/work/launch-control/c-work-launch-control-stabilization-baseline-recovery-001-call.md:

  - CREATE only if absent, using the exact CALL carried in `next` below.
  - End it with:
    `END_OF_FILE: live/indie-game-development/work/launch-control/c-work-launch-control-stabilization-baseline-recovery-001-call.md`
  - If the path exists with materially different meaning, stop with a semantic
    collision; do not overwrite.

  live/indie-game-development/work/launch-control/stabilization-baseline.md:

  - NO CHANGE.
  - Do not create or claim acceptance from this checkpoint.

  live/indie-game-development/TREE.md:

  - NO CHANGE.
  - `g-b847` remains parallel and unfinished at the same planning position.

  live/indie-game-development/work/launch-control/dashboard.html:

  - DO NOT CREATE.

  live/indie-game-development/work/board/dashboard.html:

  - NO CHANGE.

  recurring:

  - NO CHANGE.
  - Do not create morning control yet.

  All product repositories, Canon repository, Marketing artifacts, other
  track plans, `os/**`, KERNEL, plays, packet schema and writer validation:

  - NO CHANGE.

  live/indie-game-development/LOG.md:

  - APPEND exactly once before the existing END_OF_FILE marker:

    `2026-07-21 · s-work-launch-control-stabilization-baseline-checkpoint-001 · work · launch-control · g-b847/stabilization-baseline: checkpoint after repeated scope/communication failure; Launch Control root remains valid, no baseline is claimed accepted, mechanics/hook/evidence deep-dives are removed from the management session, and one fresh recovery root will present the complete plain-language release strategy, milestone chain, five-day gate, forecast, risk/cut model, Daily Command and dashboard specification in one coherent draft. → history/2026-07-21-s-work-launch-control-stabilization-baseline-checkpoint-001.md`

  live/indie-game-development/history/2026-07-21-s-work-launch-control-stabilization-baseline-checkpoint-001.md:

  - CREATE only if absent.
  - SAVE this complete RESULT exactly once.
  - End with:
    `END_OF_FILE: live/indie-game-development/history/2026-07-21-s-work-launch-control-stabilization-baseline-checkpoint-001.md`

captures:
  - "Canon input, not Launch Control requirement: compact preparation/expedition-selection frame around a repeatable expedition and Sphere-centered gas extraction may be a strong demo direction; exact loop, gas states, tools, level conditions, number of variants and interaction rules remain Canon work."
  - "Management communication rule: owner ideas are hypotheses until explicit verdict; Launch Control must challenge scope, stop diffusion, explain business meaning in ordinary Russian and keep every discussion tied to a date, milestone, risk, cut or dispatch decision."

decisions_needed: []

play_check:
  - "1 Recite: done — the release-control goal and complete done_when were restated, but the session subsequently lost the release-level altitude."
  - "2 Owner inputs (owner): done — inputs include `я же создавал глобального стратега, который, блядь, приведет нас к релизу`, `мы создадим какую-то стратегию, там, milestone'ы пропишем`, `я с утра тебя запустил, чтобы обновили dashboard, понятно, что делать, пошли`, `всё, что я говорю, это не требование` and `ты полностью отвечаешь за бизнес`; previously selected 1A, 2A and 4A are preserved as inputs."
  - "3 Do the work: checkpoint — partial calendar/demo-boundary inputs were gathered, but the session repeatedly descended into Canon-level mechanics and premature hook/evidence detail instead of producing the complete release baseline; two-strikes requires a fresh handoff."
  - "4 Self-check: done — final done_when is not met: no accepted artifact, complete milestone network, forecast, risk/cut model, Daily Command contract or owner acceptance exists; no false completion is claimed."
  - "5 Close: done — current call is replaced atomically by one same-position fresh recovery CALL; root and unrelated state are preserved; no dashboard, recurring control, directive, dispatch, product work or OS mutation is opened."

log: 2026-07-21 · s-work-launch-control-stabilization-baseline-checkpoint-001 · work · launch-control · g-b847/stabilization-baseline: checkpoint after repeated scope/communication failure; Launch Control root remains valid, no baseline is claimed accepted, mechanics/hook/evidence deep-dives are removed from the management session, and one fresh recovery root will present the complete plain-language release strategy, milestone chain, five-day gate, forecast, risk/cut model, Daily Command and dashboard specification in one coherent draft.

next: |
  CALL c-work-launch-control-stabilization-baseline-recovery-001
  to: session
  direction: indie-game-development
  track: launch-control
  play: work
  node: g-b847
  task: stabilization-baseline-recovery
  issued: 2026-07-21 (s-work-launch-control-stabilization-baseline-checkpoint-001)

  goal: |
    У владельца есть один принятый, понятный без управленческого жаргона
    release-control baseline, который показывает весь путь от текущего
    состояния до Steam demo: цель и fallback, этапы, даты, цепочку,
    определяющую срок, прогноз, риски и cuts, обязанности треков, ежедневный
    owner/AI dispatch, правила перепланирования и будущий dashboard.

  context: |
    Read fresh:
    - `live/indie-game-development/CHARTER.md`
    - `live/indie-game-development/TREE.md`
    - `live/indie-game-development/NOW.md`
    - `live/indie-game-development/work/program-v2-integration-lab-plan.md`
    - `live/indie-game-development/history/2026-07-21-s-map-launch-control-track-add-002.md`
    - `live/indie-game-development/history/2026-07-21-s-work-launch-control-stabilization-baseline-checkpoint-001.md`
    - current accepted Canon, Marketing and capability-track evidence only
      to determine release obligations, dependencies and state; do not reopen
      their internal design.

    Owner inputs are complete. Do not repeat the interview.

    Exact owner recovery expectations:
    - `я же создавал глобального стратега, который, блядь, приведет нас к релизу`
    - `мы создадим какую-то стратегию, там, milestone'ы пропишем или ещё что-то`
    - `я с утра тебя запустил, чтобы обновили dashboard, понятно, что делать, пошли`
    - `нам нужно много параллельной работы запустить`
    - `всё, что я говорю, это не требование`
    - `ты полностью отвечаешь за бизнес`
    - `мы не хотим куда-то сильно углубляться, делать чью-то работу, потому что нам нужно глобально планировать и держать фокус`

    Already selected owner inputs:
    - October is a conditional target and February is the accepted fallback.
    - Public demo requires real co-op on at least two machines; final
      eight-player proof remains later.
    - Demo is a small but publicly reliable slice.
    - A compact repeatable expedition frame is acceptable; exact mechanics
      and content belong to Canon.
    - Full economy is not automatically required for the demo.
    - Owner examples and ideas remain hypotheses until explicit verdict.

    Official dates to verify first-hand again:
    - October 2026 Next Fest:
      https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/2026october
    - February 2027 Next Fest:
      https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/feb_2027
    - Preserve the CHARTER money gate `2026-12-11`.

    Candidate first internal gate to evaluate:
    `2026-07-26 — control operational: baseline accepted, one manual Daily
    Command completed, first lawful work wave selected/launched, current
    truth/next result/date range/blocker/collision known for every
    demo-critical track, and critical-chain/forecast v1 exists.`

  boundaries: |
    This is release strategy and operating control, not a game-design
    workshop.

    Do not decide or deeply discuss:
    - sleeping gas;
    - exact floor loop;
    - Sphere controls or filling;
    - Counter / Brake / Time;
    - gas roster;
    - exact tools;
    - level conditions;
    - number of maps or generator design;
    - destruction implementation;
    - detailed hook framework;
    - playtest questionnaire or validation thresholds.

    State only the release-level result required from the owning track.
    Route internal design to Canon, Marketing or capability tracks.

    Use ordinary Russian. Any unavoidable term must be defined immediately in
    one plain sentence. Internal ids and architecture language are optional
    traceability only.

    Treat every owner idea as a hypothesis unless the owner explicitly accepts
    it. Challenge scope, calendar cost and commercial value rather than
    automatically agreeing.

    Present one coherent whole strategy and complete artifact draft. Do not
    reopen a sequence of isolated micro-decisions.

    Do not mutate product repositories, another track's plan, Canon,
    Marketing, dashboard, recurring control or `os/**`.
    Do not issue engineering work, a Release Directive or actual recurring
    dispatch in this baseline session.
    Ignore `track_wip_limit: 99` as workload or capacity.

  done_when: |
    1. One complete draft exists for
       `work/launch-control/stabilization-baseline.md`, primarily in ordinary
       Russian and naming owner inputs, state evidence and external sources.

    2. The first screen gives the owner the whole strategy:
       target/fallback, current release milestone, nearest dated gate, current
       date-determining chain, first five-day objective and how daily control
       works.

    3. The artifact defines 5-7 release-level milestones from current state to
       festival-ready demo, each with outcome, owner tracks, entry/exit gate,
       useful date and explicit non-scope. Program's technical milestones are
       nested evidence, not substituted for the release plan.

    4. Current state is summarized by track in plain language:
       what is proven, next release-relevant outcome, blocker/dependency,
       collision risk and whether it can run safely in parallel.

    5. One current date-determining chain and near-determining work are named.
       Optimistic, likely and conservative ranges are shown with explicit
       assumptions and confidence limits; October is neither promised nor
       dismissed without those assumptions.

    6. Top risks have signal, owner, prevention, contingency, named cut and
       latest useful decision date.

    7. The lawful Release Directive model defines release need, affected gate,
       required outcome, evidence and useful date; target tracks answer
       `ACCEPT | COUNTER | BLOCKED` without plan mutation or a new packet type.

    8. The operating model defines:
       - one owner-primary focus;
       - variable parallel-safe AI work;
       - serial/collision-risk work;
       - queue-next work;
       - review/decision load;
       - event-driven refill;
       - one short Daily Command and its exact fields.
       Numeric WIP compatibility is ignored.

    9. The Process Adaptation Contract includes the communication recovery
       rules from the checkpoint and the lawful boundaries for target-track
       work versus separate OS maintenance.

    10. The future dashboard field list is plain-language and directly mirrors
        the Daily Command: goal, milestone, nearest date, yesterday, primary
        today, parallel today, blocked, decisions, date-determining chain,
        forecast, risk/cut and next refresh.

    11. One first dated internal gate is accepted and exactly one ready
        successor CALL is returned for a manual Daily Command dry run.

    12. The owner accepts or corrects the complete baseline in actual words.
        No downstream control mechanism opens before that verdict.

  return: |
    One work RESULT containing the accepted baseline artifact path, exact owner
    words, release strategy, milestone chain, target/fallback verdict,
    scenario forecast, risks/cuts, track obligations, Daily Command and
    dashboard contracts, first dated gate and exactly one manual Daily Command
    dry-run successor or one exact blocker.

  budget: one fresh owner-present planning session
  surface: owner-present

END_OF_FILE: live/indie-game-development/history/2026-07-21-s-work-launch-control-stabilization-baseline-checkpoint-001.md
