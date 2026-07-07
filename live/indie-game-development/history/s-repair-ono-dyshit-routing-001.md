id: s-repair-ono-dyshit-routing-001
direction: indie-game-development
play: repair
node/task: g-d3a8/q-ono-dyshit-core-frame
date: 2026-07-07
status: CHECKPOINT_REPAIR
invalidates:
  - s-canon-ono-dyshit-core-frame-001

outcome: |
  REPAIR / GAP EVENT.

  The previous canon-forge RESULT `s-canon-ono-dyshit-core-frame-001` is invalid and must not be applied as canon.

  Reason:
    The session wrongly treated an unresolved owner-level fork as frozen canon:
      - Bottle the Monster / catch gas first;
      - mission value through gas danger first;
      - hybrid / discriminating proof.

    The owner explicitly corrected that this was supposed to be discussed, compared and gated, not decided by the session.

  Corrected status:
    `q-ono-dyshit-core-frame` is NOT frozen.
    The core-frame question is not ready for canon-forge freeze.
    It must return to a Design Lab / owner-diverge route.

  Owner-approved repair boundary:
    `ОНО ДЫШИТ` may remain as a working title / pitch-label only.
    It is not a source of design truth.

    The title must not imply or smuggle in:
      - living city ontology;
      - gas as subject/creature;
      - gas intent / pursuit / targeting;
      - creature AI;
      - magical sleep/wake aggro;
      - mandatory gas-harvest first core;
      - accepted Bottle the Monster core;
      - exact gas names/types/tools/capture/cargo/timers/economy.

    Principle:
      title follows canon;
      canon does not follow title.

  All pitch/research material is candidate seed only.
  Nothing is imported automatically.
  Every research/pitch idea must be discussed and gated before canon.

evidence: |
  Owner correction in-session:
    - owner rejected the premature freeze:
      "У нас это было два варианта. Я сказал рассмотреть."
      "Это должен быть именно диалог"
      "у нас есть design lab, почему через это не пропускается?"
    - owner diagnosed map/lab routing problem:
      "это как бы комплексный вопрос"
      "есть мап, есть дизайн лап, есть мапа"
      "вообще этот реально сейчас вопрос должен стоять, или он потом выведется сам?"
    - owner accepted repair direction:
      "в принципе я с тобой согласен"
      "всё надо пересмотреть, по всему пройтись"
      "ничего не берем, всё обсуждаем"
    - owner set title boundary:
      "можем как оставить если это название то вообще пофиг"
      "я не хочу что бы это название тянуло на себя одеяло"
      "мы должны руководствоваться нашими основными принципами"
    - owner confirmed:
      "Ок"

  Existing floor-loop discussion supports the required discipline:
    design terms must map to player action / world cause / readable consequence / stake change,
    not become slogan-driven mechanics.

diagnosis: |
  The route failure was not only a bad draft.
  It was a bad transition from cartography/design material into canon-forge.

  What went wrong:
    1. The session took a candidate/recommended framing as if the owner had already selected it.
    2. The session bypassed canon-forge Diverge(owner).
    3. The session treated `q-ono-dyshit-core-frame` as ready-to-freeze when it still contained an unresolved first-core fork.
    4. The map/handoff phrase "if gas extraction is not mandatory" biased the answer instead of preserving the fork.
    5. The title/pitch frame `ОНО ДЫШИТ` risked pulling ontology and mechanics into canon.

corrected_map_status: |
  `q-ono-dyshit-core-frame`:
    status: not_frozen
    routing: needs_design_lab
    reason: unresolved first-core fork and title/pitch contamination risk

  The next question is not:
    "Freeze corrected ОНО ДЫШИТ core frame."

  The next question is:
    "Which first-proof/core-frame branch should the project use, and at what altitude is that decision?"

fork_to_design_lab:
  question: |
    What is the first core/proof frame for the gas game after the `ОНО ДЫШИТ` pitch material,
    without importing pitch ideas as canon?

  options_to_compare:
    - id: A
      name: Bottle the Monster / gas capture first
      player_action: |
        Players detect hidden/quiet gas, activate or push a valuable state, shape it with building/gas/conditions,
        capture/seal it, carry it under liability, and return safely.
      strong_because: |
        Strongest market hook; "the monster is the air"; clear clip/cargo/greed moment.
      bad_because: |
        Pulls capture implementation, containers, cargo, purity, timers, tools and economy too early;
        can swallow gas-as-field and turn the proof into container/carry design.

    - id: B
      name: Mission value through gas danger first
      player_action: |
        Players enter for object/data/person/proof/shutdown/route/salvage value,
        detect hidden/quiet gas, physically intervene in gas/building/conditions,
        read consequences, keep value/people/route safe, and return.
      strong_because: |
        Cheapest first proof of gas as gameplay before cargo/economy;
        tests detection → intervention → consequence → return liability.
      bad_because: |
        Weaker hook; can collapse into ordinary salvage where gas is only hazard;
        may lose the Bottle the Monster fantasy if framed badly.

    - id: C
      name: Discriminating hybrid
      player_action: |
        Use one shared hidden-gas/intervention/return spine and compare two objective skins:
        non-gas value vs gas-capture value.
      strong_because: |
        Avoids premature canon choice and exposes which branch actually creates better player action/proof.
      bad_because: |
        Wider; can sprawl unless limited to a paper Design Lab or tiny proof-design comparison.

recommended_next: |
  Run a Design Lab / repair-design-lab session before any canon-forge freeze.

  It should answer:
    - what decision must be made now for first proof;
    - what must remain open for later;
    - whether Bottle-first, mission-value-first, or hybrid is recommended;
    - what owner must explicitly approve before canon-forge resumes.

title_boundary: |
  `ОНО ДЫШИТ`:
    status: working_title / pitch_label only
    canon_authority: none

  Allowed:
    - use as temporary label;
    - express player-facing feeling that the place/air seems to breathe;
    - remain in pitch/research notes as candidate framing.

  Forbidden:
    - use the title to justify living-city ontology;
    - use the title to justify gas intent or creature behavior;
    - use the title to force sleep/wake mechanics;
    - use the title to force gas capture as first core;
    - use the title to import pitch examples;
    - use the title to override frozen gas-field / no-agency principles.

state_changes:
  - repo: ainazemtsau/my_global_workflow
    action: create_file
    path: live/indie-game-development/history/s-repair-ono-dyshit-routing-001.md
    content_source: this_full_RESULT_block

  - repo: ainazemtsau/my_global_workflow
    action: append_line
    path: live/indie-game-development/LOG.md
    content: |-
      2026-07-07 — REPAIR / gap event (g-d3a8/q-ono-dyshit-core-frame): previous canon-forge RESULT s-canon-ono-dyshit-core-frame-001 invalidated. It prematurely froze an unresolved fork as canon. Owner clarified the branch "Bottle the Monster / gas capture first" vs "mission value through gas danger first" vs hybrid must be discussed through Design Lab / owner-diverge, not chosen by the session. `ОНО ДЫШИТ` may remain only as working title / pitch-label and must not pull ontology, creature AI, magical sleep/wake, harvest-first core, exact gas names/tools/capture/cargo/timers/economy or any pitch/research seed into canon. q-ono-dyshit-core-frame status = NOT frozen / needs Design Lab. → history/s-repair-ono-dyshit-routing-001.md

  - repo: ainazemtsau/my_global_workflow
    action: edit_file
    path: live/indie-game-development/NOW.md
    operations:
      - ensure_open_call_absent_or_mark_invalid:
          id: c-canon-ono-dyshit-core-frame-001
          note: |
            If still present, close as invalidated by repair; do not route to writer as frozen canon.
      - add_open_call:
          id: c-designlab-ono-dyshit-core-frame-fork-001
          to: session
          for: g-d3a8 / q-ono-dyshit-core-frame fork
          issued: 2026-07-07
          call: work/c-designlab-ono-dyshit-core-frame-fork-001-call.md
          note: |
            REPAIR follow-up after invalid premature freeze. Owner clarified that "Bottle the Monster / gas capture first"
            vs "mission value through gas danger first" vs hybrid proof was not decided and must be discussed through
            Design Lab / owner-diverge. `ОНО ДЫШИТ` may remain as working title only; it must not pull design truth,
            gas agency, magical sleep/wake, harvest-first core, exact gas names/tools/capture/cargo/timers/economy or
            pitch/research seeds into canon. Goal: compare first-proof/core-frame branches at player-action altitude and
            return a recommendation + owner decision, no canon freeze.
      - replace_parallel_track_state:
          id: g-d3a8
          value: |-
            parked — REPAIR s-repair-ono-dyshit-routing-001: previous q-ono-dyshit-core-frame freeze packet invalidated.
            Core frame NOT frozen. Owner clarified the branch Bottle-the-Monster/gas-capture-first vs mission-value-through-
            gas-danger-first vs hybrid proof must be discussed through Design Lab / owner-diverge, not chosen by session.
            `ОНО ДЫШИТ` may remain only as working title / pitch-label; it has no canon authority and must not pull ontology,
            creature AI, magical sleep/wake, harvest-first core, exact gas names/tools/capture/cargo/timers/economy or any
            pitch/research seed into canon. Next open call: c-designlab-ono-dyshit-core-frame-fork-001.

  - repo: ainazemtsau/my_global_workflow
    action: create_file
    path: live/indie-game-development/work/c-designlab-ono-dyshit-core-frame-fork-001-call.md
    content: |-
      CALL c-designlab-ono-dyshit-core-frame-fork-001
      to: session
      direction: indie-game-development
      play: local/design-lab
      node: g-d3a8
      question: q-ono-dyshit-core-frame-fork
      parent: s-repair-ono-dyshit-routing-001
      surface: any / repo root `C:\my_global_workflow_worktrees\indie-game-development`

      goal: |
        Run a Design Lab on the unresolved first-core / first-proof fork behind `q-ono-dyshit-core-frame`.

        Compare:
        - Bottle the Monster / gas capture first;
        - mission value through gas danger first;
        - discriminating hybrid proof.

        The session must not freeze canon. It must produce an owner-readable comparison, recommendation and explicit owner decision point.

      context: |
        Read:
        - live/indie-game-development/history/s-repair-ono-dyshit-routing-001.md
        - live/indie-game-development/history/s-cartography-ono-dyshit-core-frame-001.md
        - live/indie-game-development/history/s-canon-gas-interaction-playable-anchors-001.md
        - live/indie-game-development/work/concept-share-2026-07-07.md
        - live/indie-game-development/work/concept-pitch-2026-07-07.md
        - live/indie-game-development/work/concept-hooks-research-2026-07-07.md
        - live/indie-game-development/work/design-labs/gas-interaction-gameplay-001.md
        - live/indie-game-development/work/canon-maps/gas-interaction-map.md
        - live/indie-game-development/knowledge/mechanic-lenses.md

        Also read canon repo:
        - questions/q-gas-role.md
        - questions/q-gas-value-forms.md
        - questions/q-field-capture-principles.md
        - questions/q-cargo-containment-principles.md
        - questions/q-coop-shape.md
        - questions/q-expedition-macrocycle.md
        - questions/q-floor-board-kernel.md
        - questions/q-floor-loop.md
        - questions/q-floor-gas-work-verbs.md
        - questions/q-field-legibility.md
        - questions/q-two-player-floor-greybox-proof.md
        - maps/World.md

        Owner repair boundary:
        - Nothing from `ОНО ДЫШИТ` pitch/research is canon by default.
        - `ОНО ДЫШИТ` may remain as working title / pitch-label only.
        - Title follows canon; canon does not follow title.
        - Do not let title imply living city, gas subjectivity, creature AI, magic sleep/wake, harvest-first law, exact gas names/tools/capture/cargo/timers/economy.
        - Every pitch/research idea must be discussed and gated.

      boundaries: |
        Do not freeze a canon card.
        Do not choose a branch without owner approval.
        Do not treat previous s-canon-ono-dyshit-core-frame-001 as valid.
        Do not import pitch/research ideas automatically.
        Do not solve exact gas roster, names, gas types, tools, capture implementation, containers, cargo system, timers, economy, progression, final VFX or fun certification.
        Do not make gas into creature AI.
        Do not make sleep/wake magical aggro.
        Do not let working title drive mechanics.

      done_when: |
        A local/design-lab RESULT contains:
        1. clear statement of the unresolved fork;
        2. player-action loop for Bottle-first;
        3. player-action loop for mission-value-first;
        4. player-action loop for hybrid/discriminating proof;
        5. what each option proves;
        6. what each option risks / pulls into scope;
        7. how each option preserves or violates frozen principles;
        8. recommendation with "bad, because" for alternatives;
        9. explicit owner decision needed before canon-forge resumes;
        10. title-boundary preserved;
        11. no canon freeze;
        12. exact state_changes only through RESULT.

      return: |
        RESULT with readable Russian owner summary first, then machine RESULT block.

      budget: one session

  - repo: ainazemtsau/gas_coop_game_canon
    action: do_not_apply
    target_from_invalid_result: questions/q-ono-dyshit-core-frame.md
    reason: previous RESULT invalidated; q-ono-dyshit-core-frame not frozen

  - repo: ainazemtsau/gas_coop_game_canon
    action: do_not_apply
    target_from_invalid_result: maps/World.md q-ono-dyshit-core-frame entry and spawned child notes
    reason: previous RESULT invalidated; Design Lab must happen first

  - repo: ainazemtsau/gas_coop_game_canon
    action: if_already_applied_revert_or_mark_void
    targets:
      - questions/q-ono-dyshit-core-frame.md
      - questions/q-hidden-atmosphere-detection.md
      - questions/q-mission-value-vs-gas-harvest.md
      - questions/q-one-more-pass-pull.md
      - questions/q-first-playable-proof-slice.md
      - questions/q-gas-harvest-candidate.md
      - questions/q-cargo-containment-reentry.md
      - maps/World.md changes from s-canon-ono-dyshit-core-frame-001
    reason: |
      These were proposed by the invalid premature freeze. They must not remain as canon outputs unless a later Design Lab and owner-approved canon-forge reintroduce them.

captures:
  - id: title-follows-canon
    text: |
      `ОНО ДЫШИТ` can remain as working title / pitch label, but has zero design authority. If a mechanic is justified only by the title, it fails.
  - id: fork-must-not-hide-in-proof
    text: |
      First playable proof will implicitly choose an objective/value branch unless the fork is made explicit first.
  - id: pitch-material-candidate-only
    text: |
      Bottle the Monster, sleep/wake, gas names, live canister, seal-at-peak, price windows, concrete tools/cargo/timers/economy remain candidate seeds only.

decisions_needed:
  - id: d-ono-dyshit-core-frame-fork-001
    q: |
      Which first-proof/core-frame branch should canon-forge inherit after Design Lab:
      Bottle the Monster / gas capture first, mission value through gas danger first, or a constrained hybrid comparison?
    why_it_matters: |
      The first playable proof will otherwise make this choice silently. A hidden choice can drag in cargo/economy or weaken the market hook without owner approval.
    options:
      - option: Bottle the Monster / gas capture first
        bad_because: Pulls capture implementation, containers, cargo, tools, timers and economy into first proof; may swallow field-read gameplay.
      - option: Mission value through gas danger first
        bad_because: Weaker hook; can become ordinary salvage-with-hazard if gas stops being the central system.
      - option: Constrained hybrid
        bad_because: Wider and easier to sprawl; must be tightly bounded as discriminating lab/proof.
    recommendation: |
      Run the Design Lab first and decide after its comparison. Do not freeze any branch now.

play_check:
  - step: "Repair trigger"
    status: done
    evidence: |
      Owner challenged previous freeze as unauthorized and asked why Design Lab/map route was bypassed.

  - step: "Diagnose conflict"
    status: done
    evidence: |
      Previous RESULT treated an unresolved fork as canon. Owner clarified nothing is accepted automatically.

  - step: "Owner-approved correction"
    status: done
    owner_words: |
      "всё надо пересмотреть, по всему пройтись"
      "ничего не берем, всё обсуждаем"
      "я не хочу что бы это название тянуло на себя одеяло"
      "мы должны руководствоваться нашими основными принципами"
      "Ок"

  - step: "State route"
    status: done
    evidence: |
      State changes invalidate prior freeze, register Design Lab fork call, and preserve title boundary.

  - step: "Close"
    status: done
    evidence: |
      This RESULT closes the repair checkpoint and provides exact writer instructions.

next: |
  CALL c-designlab-ono-dyshit-core-frame-fork-001
  to: session
  direction: indie-game-development
  play: local/design-lab
  node: g-d3a8
  question: q-ono-dyshit-core-frame-fork
  parent: s-repair-ono-dyshit-routing-001

log_summary: |
  Repair closed: previous q-ono-dyshit-core-frame freeze invalidated. Nothing from `ОНО ДЫШИТ` pitch/research is canon by default. Title can remain as working label only and must not drive mechanics. Core branch returns to Design Lab: Bottle-first vs mission-value-first vs constrained hybrid.
END_OF_FILE: live/indie-game-development/history/s-repair-ono-dyshit-routing-001.md
