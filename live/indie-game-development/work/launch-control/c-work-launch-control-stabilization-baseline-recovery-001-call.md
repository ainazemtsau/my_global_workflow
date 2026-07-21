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

END_OF_FILE: live/indie-game-development/work/launch-control/c-work-launch-control-stabilization-baseline-recovery-001-call.md
