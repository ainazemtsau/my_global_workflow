RESULT s-map-g-d3a8-frame-v2-reconciliation-001 (call: c-map-g-d3a8-frame-v2-reconciliation-001)
direction: indie-game-development   play: map   node/task: g-d3a8
owner_approved: 2026-07-15 — owner: «я аппруваю (можешь добавить маркер)»

outcome: |
  Существует точная, owner-approved коррекция ветки g-d3a8 и необходимой
  NOW-маршрутизации.

  Коррекция:
  - полностью заменяет устаревшую текущую карточку g-d3a8, а не добавляет
    очередной superseded-баннер;
  - ставит Minimum Game Frame v2 как текущую whole-game design basis,
    явно не являющуюся каноном;
  - удаляет действующее design-утверждение solo-startable / 1–4;
  - фиксирует меняющийся состав 4–8, обязательную поддержку полной восьмёрки,
    открытый нижний предел ниже четырёх и отсутствие соло как текущей
    дизайн-цели;
  - устанавливает лестницу authority:
    FRAME → OWNER-SELECTED PAPER ANSWER → separate CANON ADMISSION;
  - сохраняет пять реальных макроразвилок и честные пределы бумажного
    доказательства;
  - делает c-research-q-coop-interdependence-002 READY PARALLEL / paper-only;
  - регистрирует canon reconciliation как первую готовую фазу;
  - регистрирует полный eight-player consistency sweep как HELD до закрытия
    canon reconciliation;
  - оставляет c-shape-sc-damage-001 HELD;
  - не меняет CHARTER, канон, продукт, реализацию, основной инженерный маршрут
    или unrelated TREE branches.

  Никакой файл не изменялся непосредственно этой сессией. Ниже находится
  точный пакет для mechanical writer.

evidence: |
  1. Current stale TREE basis:
     - live/indie-game-development/TREE.md
     - fetched SHA: 065b5f814d8d0ce3f7da60f10526a471eb708ce6
     - current g-d3a8 says:
       "solo-startable, co-op-optimal (1–4 players via parametric scaling...)".

  2. Accepted whole-game frame:
     - live/indie-game-development/work/minimum-game-frame-v2.md
     - SHA: 680b93582249336d4ac31629574bed15bc5f2bed
     - status: FRAME READY
     - owner_verdict: "FRAME READY"
     - authority: current owner-approved whole-game design basis; not canon.

  3. Binding player-count owner requirement:
     - live/indie-game-development/knowledge/
       g9c41-players-8-owner-requirement.md
     - SHA: d82f2cc6cd6b60e8fdd755fc5da92d3a2c4ed9c8
     - owner words:
       «так как мы рассчитываем на кооператив, то есть мы вообще не обращаем
       внимания на то, как соло играть. То есть это пока не в компетенции.
       То есть мне кооператив, и мне важно, чтобы он поддерживал 8 игроков.
       То есть минимально, в принципе, неважно. Мне важно, чтобы было
       8 игроков, потому что у нас как раз таки компания 8 человек, и это,
       в принципе, важное требование.»

  4. Current canon boundary:
     - gas_coop_game_canon/CONSTITUTION.md SHA:
       705e8bbf76766ec9492e84644fe3715cd4f3e000
     - its active co-op pillar still says "1–4 игрока, соло-стартуемо";
       this session does not modify it.
     - gas_coop_game_canon/canon/c-001-investigation-readiness.md SHA:
       65a0b69cb6c662dd83d2482890f1fe003a57e2aa
     - c-001 remains bounded to the conscious investigation → operation
       transition and explicitly excludes Bubble, co-op roles, damage,
       economy and progression.

  5. Current routing basis:
     - live/indie-game-development/NOW.md
     - fetched SHA: efada05bf8ec6282aac788f4ed1bb0ec42d405d3
     - c-map-g-d3a8-frame-v2-reconciliation-001 is currently READY;
     - c-research-q-coop-interdependence-002 is currently HELD until this
       reconciliation closes;
     - c-shape-sc-damage-001 is currently HELD until ready canon spec.

  6. Owner evidence in this session, verbatim:
     - named-file evidence and fresh map_evidence waiver:
       «1, используем названные файлы»
     - skeleton acceptance and durable phased route:
       «я скелет принимаю, мы можем идти фазами»
     - per-node verdict:
       «Принимаю смысл карточки g-d3a8»
     - dependency order:
       «Порядок принимаю: canon repair первым, co-op research готов параллельно»
     - whole corrected branch and routing:
       «Финальную ветку g-d3a8 и маршрутизацию утверждаю»

  7. Done-when coverage:
     - Frame v2 reflected: replacement goal + done_when 1 and 3;
     - eight-player requirement reflected: goal + done_when 2;
     - frame / paper answer / canon separated: goal + done_when 1 and 5;
     - remaining macro forks named: done_when 4;
     - immediate dependencies named: detail dependency map + NOW calls;
     - unrelated TREE unchanged: stable single-node replacement;
     - co-op continuation disposition: READY PARALLEL / paper-only;
     - exact owner approval: quoted above.

state_changes: |
  1. TREE.md — replace exactly one existing node.

     path:
       live/indie-game-development/TREE.md

     stable_target:
       root.children[id=g-d3a8]

     base_sha:
       065b5f814d8d0ce3f7da60f10526a471eb708ce6

     operation:
       Replace the entire current g-d3a8 node from "- id: g-d3a8" through
       the end of its detail field. Preserve its position between g-9c41
       and g-7e15. Do not alter root.map_order, any sibling node, or the
       file's END_OF_FILE marker.

     replacement: |
         - id: g-d3a8
           goal: |
             The game's design truth is coherent and current across an explicit
             authority ladder rather than treated as one finished document:

             1. Minimum Game Frame v2 is the owner-approved whole-game design
                basis and is not canon.
             2. An unresolved design question becomes an OWNER-SELECTED PAPER
                ANSWER only through an owner-present paper verdict.
             3. A paper answer becomes canon only through a separate
                owner-present canon-admission decision.

             At whole-game altitude the game is designed first for changing
             4–8-player groups, with support for the full group of eight as a
             hard design and support requirement. The exact supported lower
             bound below four remains OPEN, and solo is not a current design
             target.

             The branch preserves the Frame-v2 player promise and anchors:
             gas is the shared physical medium and regular expedition value;
             safe return converts extraction into lasting power for the current
             run; predictable tools differ from exceptional artifacts; a run is
             short, difficult and finite, with full wipe and a fast meaningful
             restart; and the Ball/Bubble remains the principal visible
             extraction DESIGN ANCHOR while its exact behavior stays OPEN.

             The branch progressively resolves gas grammar and roster,
             temporary co-op composition, expedition economy and progression,
             artifacts, depth and end-state, failure and recovery, and lore
             without promoting hypotheses, examples or untested mechanics to
             frame or canon authority.

           why: |
             This branch turns the root's pride, gameplay-depth and co-op-first
             criteria into design truth that the engine, canon and storefront can
             consume without authority drift. The explicit
             FRAME → OWNER-SELECTED PAPER ANSWER → CANON ladder lets the
             owner/AI workflow resolve bounded questions without pretending that
             paper proves fun, while the owner's available eight-person group
             provides a direct route to later real co-op evidence.

           done_when: |
             All are true:

             1. A current design document and source/status map identify
                Minimum Game Frame v2 as FRAME READY and not canon, and
                unambiguously distinguish:
                - statements accepted at FRAME altitude;
                - OWNER-SELECTED PAPER ANSWERS;
                - answers separately admitted to CANON;
                - still-OPEN questions;
                - claims requiring playable or external evidence.
                No hypothesis, example or paper answer gains canon authority
                by implication.

             2. The whole-game design states explicitly that:
                - changing 4–8-player groups are the primary current design range;
                - support for the full group of eight is mandatory;
                - the exact supported lower bound below four remains OPEN;
                - solo is outside the current design target.

             3. The Frame-v2 anchors remain intact without silently fixing their
                open implementation:
                - gas is the shared physical environment and regular expedition
                  value;
                - only safely returned gas becomes durable power for the current
                  run;
                - predictable tools and exceptional artifacts have different jobs;
                - one run is short, difficult and finite;
                - full wipe ends the run and the next start reaches meaningful
                  decisions quickly;
                - Ball/Bubble is the principal extraction DESIGN ANCHOR, while
                  filling, control, capacity, durability, rupture, required hands
                  and rare alternatives remain OPEN;
                - c-001 remains limited to the conscious
                  investigation → operation transition.

             4. Each remaining Frame-v2 macro fork is either resolved through
                the authority ladder or remains explicitly OPEN:
                - economy or access that makes meaningful gas return produce
                  progression without making near-empty systematic returns optimal;
                - artifact origin, frequency and run-shaping role;
                - depth, staging-zone structure and final objective;
                - wipe/reset state, persistence, metaprogression and permitted
                  exceptions;
                - temporary subgroup and role composition, additional value from
                  4–8 players, attendance continuity, scaling and the supported
                  lower bound.

             5. Current canon is indexed against the frame. Any contradiction is
                handled through an explicit amendment or supersession chain,
                never by silently expanding or rewriting a canon card.
                c-001 remains bounded to its declared question and does not
                acquire extraction, Bubble, co-op-composition, damage, economy
                or progression authority.

             6. Gas grammar is designed rather than accumulated as decorative
                content:
                - every base gas has a gameplay job involving a decision, risk,
                  tool, route, consequence or co-op pressure;
                - the design catalogue may be effectively unlimited, while
                  g-9c41 owns the bounded, tunable concurrent-per-node
                  engineering budget;
                - reactions, mixing and anomalous gases remain consistent with
                  honest physical behavior: no creature intelligence, scripted
                  gas scares or hidden cheating;
                - exact roster, states, reactions and tuning remain separate
                  design questions.

             7. Selected design answers are checked against g-9c41 for
                simulability and pass a structured paper red-team for internal
                consistency, dominant strategies, loopholes, degenerate
                combinations and balance hypotheses. Executable-config
                self-play may be added once the relevant g-9c41 surface exists,
                but it does not replace human play.

             8. Evidence limits remain explicit. Paper work does not certify fun,
                meaningful co-op, pacing, onboarding, runtime legibility,
                production cost, market response or the actual play value of
                eight players. Those require playable and external evidence.

             9. The owner gives an explicit verdict that he is proud of the
                resulting design, based on the current evidence level rather
                than claims beyond it.

           status: parked

           detail: |
             Current reconciliation and lineage:
             - history/2026-07-15-s-map-g-d3a8-frame-v2-reconciliation-001.md
             - history/s-map-002.md

             Current authority:
             - FRAME: work/minimum-game-frame-v2.md — FRAME READY 2026-07-14;
               whole-game design basis, not canon.
             - OWNER REQUIREMENT:
               knowledge/g9c41-players-8-owner-requirement.md — eight-player
               support is mandatory; solo is outside the current design target.
             - CANON: gas_coop_game_canon/CONSTITUTION.md, CORE.md, INDEX.md
               and canon cards.
             - CURRENT CARD: c-001 resolves only the conscious
               investigation → operation transition.

             Authority route:
             FRAME READY
             → OWNER-SELECTED PAPER ANSWER
             → separate owner-present CANON ADMISSION.

             Dependency map:
             - consistency lane:
               c-map-g-d3a8-frame-v2-reconciliation-001 [CLOSED]
               → c-repair-canon-frame-v2-eight-player-001 [READY FIRST]
               → c-repair-eight-player-live-consistency-sweep-001
                 [HELD until canon repair closes];

             - design lane:
               c-map-g-d3a8-frame-v2-reconciliation-001 [CLOSED]
               → c-research-q-coop-interdependence-002
                 [READY PARALLEL / PAPER-ONLY]
               → possible OWNER-SELECTED PAPER ANSWER
               → separate owner-present canon-admission CALL;

             - c-shape-sc-damage-001 remains HELD until a ready canon
               specification explicitly changes that disposition.

             The canon reconciliation changes no mechanics. The live
             consistency sweep scans only current authoritative/live surfaces
             and does not rewrite historical evidence.

             Work continues as a parallel creative/canon track through
             owner-present sessions and adds no second active bet or active
             tasks. Existing procedures remain local/canon-forge and
             local/canon-status, subject to the authority route above.

             Superseded g-d3a8 wording remains recoverable through
             history/s-map-002.md and git history. TREE.md carries only the
             current readable card; no duplicate legacy copy is created in
             archive.

     postconditions:
       - root.children contains exactly one g-d3a8 node.
       - No active g-d3a8 text says "1–4 players" or "solo-startable".
       - g-9c41 and g-7e15 byte content is preserved unless independently
         changed by concurrent work.
       - All unrelated TREE content is preserved after semantic rebase.
       - TREE.md retains its END_OF_FILE marker.

  2. NOW.md — consume the completed map CALL and persist the phase route.

     path:
       live/indie-game-development/NOW.md

     base_sha:
       efada05bf8ec6282aac788f4ed1bb0ec42d405d3

     operations:
       a. Set the header update marker to:
          updated: 2026-07-15 by s-map-g-d3a8-frame-v2-reconciliation-001

       b. Remove open_calls entry by stable id:
          c-map-g-d3a8-frame-v2-reconciliation-001

       c. Add the following READY call before
          c-research-q-coop-interdependence-002:

          - id: c-repair-canon-frame-v2-eight-player-001
            to: session
            for: g-d3a8 / canon top-law reconciliation with Frame v2 and mandatory eight-player support
            issued: 2026-07-15
            note: |
              READY PARALLEL / FIRST g-d3a8 CONSISTENCY PHASE:
              owner-present correction of the current canon top law so active
              "1–4 / solo-startable" no longer contradicts accepted Frame v2
              and the mandatory eight-player requirement. No mechanics,
              paper-answer selection, c-001 expansion, TREE/CHARTER/product
              change or unrelated canon rewrite. Full CALL is the `next`
              packet in history/
              2026-07-15-s-map-g-d3a8-frame-v2-reconciliation-001.md.

       d. Replace only the note of the existing
          open_calls[id=c-research-q-coop-interdependence-002] with:

          note: |
            READY PARALLEL / PAPER-ONLY: g-d3a8 Frame-v2 reconciliation
            closed owner-approved. Resume the exact preserved co-op
            composition question under Frame v2 and the mandatory
            eight-player requirement. It may return an
            OWNER-SELECTED PAPER ANSWER or an honest block; canon admission
            remains a separate owner-present CALL and Sc-damage remains
            HELD. Full CALL:
            history/2026-07-14-s-repair-minimum-game-frame-v2-001.md.

       e. Add after c-research-q-coop-interdependence-002:

          - id: c-repair-eight-player-live-consistency-sweep-001
            to: session
            for: g-d3a8 + current live surfaces / eight-player consistency sweep
            issued: 2026-07-15
            note: |
              HELD until c-repair-canon-frame-v2-eight-player-001 closes.
              Then scan current authoritative/live surfaces for stale
              "1–4", "2–4", "solo-startable" and equivalent meanings;
              classify each as correct-now, engineering hygiene,
              parked/deferred or historical evidence, and propose only the
              minimal owner-approved corrections. Never rewrite history.
              Full held CALL is preserved in
              history/2026-07-15-s-map-g-d3a8-frame-v2-reconciliation-001.md.

       f. Preserve open_calls[id=c-shape-sc-damage-001] unchanged and HELD.

       g. Preserve all tasks, bet data, decisions, recurring entries,
          unrelated open_calls and the current direction-level NOW.next after
          semantic rebase. In particular, this branch route does not replace
          the current engineering next.

     exact held CALL definition to preserve in this history:

       CALL c-repair-eight-player-live-consistency-sweep-001
       to: session
       direction: indie-game-development
       play: repair
       node: g-d3a8
       surface: any
       parent: s-map-g-d3a8-frame-v2-reconciliation-001

       goal: |
         Every current authoritative/live surface either reflects accepted
         Frame v2 and mandatory support for eight players or has an explicit,
         evidence-backed disposition, without rewriting historical evidence
         or unrelated branches.

       context: |
         Run only after c-repair-canon-frame-v2-eight-player-001 closes and
         read its history RESULT.

         Also read:
         - live/indie-game-development/NOW.md
         - live/indie-game-development/CHARTER.md
         - live/indie-game-development/TREE.md
         - live/indie-game-development/work/minimum-game-frame-v2.md
         - live/indie-game-development/knowledge/
           g9c41-players-8-owner-requirement.md
         - live/indie-game-development/history/
           2026-07-15-s-map-g-d3a8-frame-v2-reconciliation-001.md
         - the completed canon-reconciliation history RESULT
         - current gas_coop_game_canon entrypoints and canon index
         - current live work/CALL surfaces whose wording makes an active
           player-count or solo-support claim.

         Search current authoritative/live material for:
         - "1–4"
         - "2–4"
         - "solo-startable"
         - equivalent claims that make four the maximum or solo a current
           design target.

         Historical RESULTs, archived sources and superseded evidence are
         provenance, not active text to rewrite.

       boundaries: |
         Owner-present, text only.
         Do not generate mechanics, roles, scaling formulas, networking
         design, Bubble controls, damage or implementation.
         Do not reopen Frame v2 or the mandatory eight-player requirement.
         Do not rewrite history, archives or old evidence.
         Do not silently change TREE: every TREE correction requires the
         owner's explicit in-session G9 approval.
         Do not alter unrelated goals merely to normalize wording.
         Preserve a clean one-player engine test when it is explicitly
         engineering hygiene rather than a promised solo game mode.
         Parked commercial/demo wording may be deferred with an explicit
         owner-readable reason rather than prematurely redesigned.

       done_when: |
         1. A complete current-authority occurrence list exists.
         2. Every occurrence is classified as one of:
            - correct now;
            - minimal correction required;
            - engineering hygiene, not a design promise;
            - parked/deferred until its branch wakes;
            - historical evidence, no edit.
         3. Exact minimal corrections are shown together and the owner
            explicitly approves them or blocks them.
         4. No historical evidence or unrelated branch is rewritten.
         5. Current live state has no unclassified contradiction with Frame v2
            or mandatory eight-player support.
         6. Any remaining deferred item names its wake condition and owner.

       return: |
         Short Russian consistency brief;
         occurrence/disposition table;
         exact minimal diffs;
         verbatim owner verdict;
         one RESULT.

       budget: one owner-present text-only session

  3. LOG.md — append exactly one line.

     path:
       live/indie-game-development/LOG.md

     append: |
       2026-07-15 — map/close (g-d3a8/c-map-g-d3a8-frame-v2-reconciliation-001, s-map-g-d3a8-frame-v2-reconciliation-001): owner approved the clean Frame-v2 g-d3a8 replacement and phased routing — mandatory eight-player support, solo outside current target, FRAME→PAPER→CANON authority ladder, canon repair READY first, co-op composition READY PARALLEL, live consistency sweep HELD behind canon repair, Sc-damage still HELD; unrelated TREE/CHARTER/canon/product and engineering next unchanged. → history/2026-07-15-s-map-g-d3a8-frame-v2-reconciliation-001.md

  4. history — save this full RESULT verbatim.

     path:
       live/indie-game-development/history/
       2026-07-15-s-map-g-d3a8-frame-v2-reconciliation-001.md

     postcondition:
       The file contains this complete RESULT and ends with:
       END_OF_FILE: live/indie-game-development/history/2026-07-15-s-map-g-d3a8-frame-v2-reconciliation-001.md

  5. Explicit no-change surfaces:
     - live/indie-game-development/CHARTER.md
     - gas_coop_game_canon/**
     - product repositories
     - implementation
     - root.map_order
     - all TREE nodes other than g-d3a8
     - direction-level NOW.next
     - all unrelated NOW state

captures:
  - "Owner-facing decision artifacts must be presented as clear, well-formatted Markdown; YAML/state syntax is machine-only and belongs in the final writer packet."

decisions_needed: []

play_check:
  - "1 Recite: done — mission/root success and current g-d3a8 state were restated through the contradiction brief; the correction remains bounded to design/canon coherence under the existing root."
  - "2 Candidates & evidence (owner): done — owner selected the named saved files and explicitly waived a fresh map_evidence pass: «1, используем названные файлы»."
  - "3 Skeleton (owner): done — six-part authority/dependency skeleton shown; owner accepted it and the durable phased route: «я скелет принимаю, мы можем идти фазами»."
  - "4 Cards: done — one existing node card, g-d3a8, was fully re-authored from Frame v2, the eight-player requirement, current TREE/canon and c-001; edge = engineering depth + OS bounded questions + available eight-player group; risk = authority-layer collapse."
  - "5 Per-node verdict (owner): done — owner: «Принимаю смысл карточки g-d3a8»."
  - "6 Order (owner): done — owner: «Порядок принимаю: canon repair первым, co-op research готов параллельно»."
  - "7 Depth check: done — no children or tasks added to TREE; one existing top-level outcome node replaced, concrete work remains in NOW.open_calls."
  - "8 Lens sweep on the map: done — gameplay depth and co-op-first owned directly by g-d3a8; technical feasibility linked to g-9c41; scope protected by paper/playable evidence split; commercial and audience remain in existing sibling branches, so no duplicate node is needed."
  - "9 Close (owner): done — final compact branch and routing approved verbatim: «Финальную ветку g-d3a8 и маршрутизацию утверждаю»."

log: "map/close g-d3a8: owner approved clean Frame-v2/eight-player branch replacement and durable phased routing; canon repair READY first, co-op paper question READY PARALLEL, live consistency sweep HELD behind canon repair, Sc-damage HELD; unrelated state preserved."

next: |
  BRANCH CONTINUATION — READY PARALLEL.
  This CALL is the owner-approved first g-d3a8 consistency phase.
  It does not replace the current direction-level NOW.next.

  CALL c-repair-canon-frame-v2-eight-player-001
  to: session
  direction: indie-game-development
  play: repair
  node: g-d3a8
  surface: any
  parent: s-map-g-d3a8-frame-v2-reconciliation-001

  goal: |
    The current canon top law and its amendment trail accurately reflect
    accepted Minimum Game Frame v2 and the mandatory eight-player owner
    requirement, eliminating the active "1–4 / solo-startable" contradiction
    without changing mechanics or expanding existing canon cards.

  context: |
    Read:
    - os/KERNEL.md
    - os/plays/repair.md
    - live/indie-game-development/NOW.md
    - live/indie-game-development/CHARTER.md
    - live/indie-game-development/TREE.md
    - live/indie-game-development/work/minimum-game-frame-v2.md
    - live/indie-game-development/knowledge/
      g9c41-players-8-owner-requirement.md
    - live/indie-game-development/history/
      2026-07-14-s-repair-minimum-game-frame-v2-001.md
    - live/indie-game-development/history/
      2026-07-15-s-map-g-d3a8-frame-v2-reconciliation-001.md
    - current gas_coop_game_canon:
      CONSTITUTION.md, CORE.md, INDEX.md, AMENDMENTS.md and
      canon/c-001-investigation-readiness.md
    - relevant git history of the canon repository.

    Current accepted state:
    - Minimum Game Frame v2 is FRAME READY and is the current whole-game
      design basis, but is not canon.
    - The primary current design range is a changing group of 4–8.
    - Support for the full group of eight is mandatory.
    - The exact supported lower bound below four remains OPEN.
    - Solo is not a current design target.
    - c-001 remains bounded to the conscious investigation → operation
      transition.

    Exact contradiction:
    - current canon CONSTITUTION pillar 1 still says
      "1–4 игрока, соло-стартуемо";
    - higher/current owner-approved Frame and owner requirement say mandatory
      eight-player support and no present solo design target.

    This is a current-law reconciliation, not a new mechanic question and not
    admission of Frame v2 wholesale into canon.

  boundaries: |
    Owner-present, text only.
    Touch only the exact canon top-law contradiction and the necessary
    amendment/supersession trail.
    Do not change TREE, CHARTER, NOW's unrelated routes, product or
    implementation.
    Do not activate Gate Q, generate mechanics, select a paper answer or
    decide co-op roles, scaling formulas, lower-bound details, networking,
    Bubble controls, damage, economy or progression.
    Do not expand or rewrite c-001.
    Do not treat all of Frame v2 as canon.
    Do not rewrite unrelated canon pillars, CORE content or cards.
    Preserve the old wording as historical provenance, not as a parallel
    active norm.
    c-research-q-coop-interdependence-002 remains READY PARALLEL / paper-only.
    c-shape-sc-damage-001 remains HELD.

  done_when: |
    1. The contradiction is stated in owner-readable language.
    2. The exact current canon correction and amendment/supersession trail are
       shown before any mutation.
    3. The owner explicitly approves the correction or blocks it.
    4. On approval, current canon no longer presents "1–4" as the maximum or
       "solo-startable" as an active design requirement.
    5. Current canon states only the accepted player-count direction:
       - changing 4–8-player groups are the primary current range;
       - support for the full group of eight is mandatory;
       - the exact supported lower bound below four remains OPEN;
       - solo is not a current design target.
    6. The correction does not canonize unresolved co-op mechanics or all of
       Frame v2.
    7. c-001 and all unrelated canon content remain unchanged.
    8. On approved close,
       c-repair-eight-player-live-consistency-sweep-001 becomes READY;
       on block it remains HELD with the exact blocker.
    9. The owner's verdict is returned verbatim in one RESULT.

  return: |
    Short Russian contradiction brief;
    exact canon-law and amendment diff;
    impact/non-impact map;
    disposition of the held consistency sweep;
    verbatim owner verdict;
    one RESULT.

  budget: one owner-present text-only session

END_OF_FILE: live/indie-game-development/history/2026-07-15-s-map-g-d3a8-frame-v2-reconciliation-001.md
