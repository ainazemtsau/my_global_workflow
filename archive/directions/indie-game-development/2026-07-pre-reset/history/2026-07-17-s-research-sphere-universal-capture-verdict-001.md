RESULT s-research-sphere-universal-capture-verdict-001 (call: c-research-sphere-foreign-gas-contact-outcomes-001)
direction: indie-game-development
track: canon
play: research
node/task: g-d3a8 / q-sphere-foreign-gas-contact

outcome: |
  Владелец отверг предпосылку, что обычному чужому gameplay gas обязательно
  нужен отдельный gas-to-shell outcome.

  Выбрана текущая owner-approved non-canon basis:

  1. Каждый стандартный Шар может добывать и удерживать любой gameplay gas.
  2. Тип газа сам по себе не повреждает, не ослабляет и не дестабилизирует
     оболочку Шара.
  3. Категории допуска газа, обязательные специальные Шары и матрица
     `gas × shell` отсутствуют.
  4. Если несколько gameplay gases оказываются внутри одного Шара, возможные
     последствия принадлежат общим правилам взаимодействия `gas × gas`;
     Шар не добавляет отдельного compatibility outcome.
  5. Точные gas-reaction thresholds, концентрации, результаты реакции,
     rupture и иные terminal consequences остаются OPEN.
  6. Обычная физика оболочки, поведение содержащегося газа и усиление от
     объёма сохраняются; удалена только gas-specific shell incompatibility.
  7. Специальные Шары или gas-specific instability сохранены только как
     PARKED HYPOTHESIS и могут вернуться после playable evidence, что
     универсальная добыча недостаточно различима или не создаёт решений.

  Исследовательская оценка:
  выбранный владельцем вариант лучше предыдущей рекомендации R. R добавлял
  отдельную deformation/leak ladder без доказательства, что игре вообще нужен
  gas-to-shell consequence layer. Универсальная добыча оставляет сложность
  в движении газа, объёме, поведении груза, смешении, маршруте и физической
  эвакуации, а не в предварительной таблице разрешений.

  Canon admission не проводился. Frame, canon, TREE, CHARTER, product и
  Sc-damage этой сессией не изменены.

evidence: |
  Exact owner verdict from the current session:

  - «любой шар, любой газ может добывать»
  - «он не может повредить шар»
  - «есть шар как добывающая сущность, и им добываются все типы газа»
  - «если чувствуется, что-то прям сильно легко или не хватает какой-то
    комплексности в этот процесс, тогда уже рассмотреть, добавить»
  - «мне кажется, что именно для начала это самый лучший вариант»

  Interpretation of those words:
  - universal capture is the selected current baseline;
  - gas-specific shell damage is rejected from the baseline;
  - specialization is postponed behind playtest evidence rather than kept
    as an active requirement.

  Source checks:
  - Current NOW.md still contains
    `c-research-sphere-foreign-gas-contact-outcomes-001` as a ready canon
    root CALL.
  - `gas-sphere-extraction-custody-frame-v1.md`, blob
    cc64dd2caaedd2eb444e5c0fb8ecfed911e41058, currently marks foreign-gas
    compatibility OPEN and lists rejection, instability, leakage, rupture
    and special Sphere categories only as candidate outcomes.
  - The same frame locates existing decision pressure in visible gas
    movement, geometry, chosen volume, contained-gas tendency and physical
    custody.
  - `minimum-game-frame-v2.md`, blob
    680b93582249336d4ac31629574bed15bc5f2bed, requires understandable
    actions with complex consequences and rejects mandatory parameter
    microcontrol as the basis of play.
  - `gas_coop_game_canon/CORE.md`, blob
    c2fe9c3dc156b91d1f684d490e04d9ea4c85f1b2, preserves the owner compass:
    default actions should not require complexity; the game should be
    difficult but not stuffy and simple but not primitive.

  Done-when disposition:
  - The immediately preceding research brief rendered four equal-depth
    candidate families and one shared scene.
  - The owner used the permitted revise/reject route and selected a simpler
    fifth answer: no special gas-to-shell outcome in the current baseline.
  - Hidden dilution percentages and an arbitrary compatibility matrix are
    explicitly excluded.
  - Canon, damage and implementation remain undecided.

state_changes: |
  Re-read current state before applying. Apply only the semantic operations
  below and preserve all concurrent unrelated state.

  1. ADD ONLY IF ABSENT:

     Target:
     live/indie-game-development/work/
     c-work-sphere-universal-capture-frame-001-call.md

     Exact content:

     CALL c-work-sphere-universal-capture-frame-001
     to: session
     direction: indie-game-development
     track: canon
     play: work
     node: g-d3a8

     goal: |
       Persist the owner's selected non-canon universal Sphere capture
       baseline in the existing extraction/custody frame so future work no
       longer treats gas-to-shell incompatibility as an active requirement.

     context: |
       Read:
       - live/indie-game-development/NOW.md
       - live/indie-game-development/work/
         gas-sphere-extraction-custody-frame-v1.md
       - live/indie-game-development/work/minimum-game-frame-v2.md
       - live/indie-game-development/history/
         2026-07-17-s-research-sphere-universal-capture-verdict-001.md
       - current gas_coop_game_canon CORE.md and INDEX.md.

       Owner-selected meaning:
       - every standard Sphere can capture and hold every gameplay gas;
       - gas type alone does not damage, weaken or destabilize the Sphere;
       - no required special Sphere category or gas-by-shell compatibility
         matrix exists;
       - if multiple gases occupy a Sphere, any consequence belongs to the
         ordinary gas-to-gas rules, not a separate Sphere compatibility rule;
       - gas-specific Sphere instability or specialization is a parked future
         hypothesis, revisited only after playable evidence that universal
         capture lacks sufficient distinction or decision pressure.

       Exact owner words are recorded in the named history receipt.

     boundaries: |
       Owner-present and text only.
       Update only the foreign-gas compatibility statements and directly
       contradictory wording in the existing non-canon frame.
       Preserve the frame's extraction, custody, shell/gas/volume,
       physical-carry and readability conclusions except where the new owner
       verdict explicitly removes gas-specific shell compatibility.
       Do not run Gate Q or canon admission.
       Do not define gas roster, gas reactions, concentrations, thresholds,
       rupture, damage, health, economy, controls, UI, capacity, helper count,
       carry tuning, networking, balance or implementation.
       Preserve minimum-game-frame-v2.md, canon, TREE, CHARTER, product and
       Sc-damage unchanged.

     done_when: |
       1. The frame unambiguously states that every standard Sphere can
          capture every gameplay gas.
       2. Gas type alone cannot damage or destabilize the Sphere.
       3. The former OPEN gas-to-shell outcome list no longer contradicts the
          selected baseline.
       4. Mixed-gas consequences are assigned only to future/common gas-to-gas
          rules without defining them here.
       5. Specialized Spheres or instability are labelled PARKED and
          evidence-triggered, not a current requirement.
       6. The artifact remains owner-approved non-canon Frame and all named
          boundaries remain unchanged.
       7. The owner receives an exact readable diff and can correct or accept
          the wording.

     return: |
       Updated frame artifact; owner-readable exact diff; trace to the
       recorded owner verdict; boundary check; one RESULT.

     budget: one owner-present text-only session

     END_OF_FILE:
     live/indie-game-development/work/
     c-work-sphere-universal-capture-frame-001-call.md

     Rebase handling:
     - target absent → add with exact content;
     - target present and byte-identical → already satisfied;
     - target present with different content → do not overwrite or merge;
       stop and route to repair.

  2. UPDATE live/indie-game-development/NOW.md:

     2.1. Remove only the complete `open_calls` item whose stable id is:

          c-research-sphere-foreign-gas-contact-outcomes-001

     2.2. Ensure exactly one parentless same-track successor item exists with
          these semantic fields:

          id: c-work-sphere-universal-capture-frame-001
          track: canon
          status: ready
          to: session
          for: "g-d3a8 / persist owner-approved non-canon universal Sphere capture baseline"
          issued: 2026-07-17
          call: work/c-work-sphere-universal-capture-frame-001-call.md
          note: "READY / OWNER-PRESENT. Persist only the selected universal-capture baseline in the existing non-canon Sphere frame. No canon admission, gas-reaction design, damage or implementation."

     Successor invariants:
     - no parent;
     - no waiting_on;
     - no second canon root;
     - preserve all other tracks and calls.

     Rebase handling:
     - returning id present, successor absent → remove returning id and add
       successor;
     - returning id absent, valid successor present → already satisfied;
     - both present → remove returning id and retain exactly one successor;
     - successor present with conflicting meaning → stop and route to repair.

     2.3. Preserve the current valid `NOW.next.call` unless it equals the
          removed returning id. If it equals the removed id, replace it with
          `c-work-sphere-universal-capture-frame-001`.

     Preserve unchanged:
     - bet;
     - tasks;
     - track_wip_limit and tracks;
     - unrelated open_calls;
     - recurring;
     - existing unrelated decisions;
     - every valid concurrent default not pointing to the removed id.

  3. ADD ONLY IF ABSENT:

     Target:
     live/indie-game-development/history/
     2026-07-17-s-research-sphere-universal-capture-verdict-001.md

     Content:
     this complete RESULT packet, beginning with the RESULT line and ending
     with the final line of RESULT.next.

     Rebase handling:
     - target absent → add;
     - target present and byte-identical → already satisfied;
     - target present with different content → stop and route to repair;
     - do not modify earlier history receipts.

  4. APPEND EXACTLY ONE LINE TO
     live/indie-game-development/LOG.md if absent, immediately before its
     END_OF_FILE marker:

     2026-07-17 · s-research-sphere-universal-capture-verdict-001 · research · canon · g-d3a8 · owner selected universal Sphere capture: every standard Sphere takes every gameplay gas, gas type alone cannot damage the shell, compatibility exceptions parked behind playable evidence · history/2026-07-17-s-research-sphere-universal-capture-verdict-001.md

     Preserve all existing LOG lines and the END_OF_FILE marker.

  5. PRESERVE UNCHANGED IN THIS SESSION:

     - live/indie-game-development/work/
       gas-sphere-extraction-custody-frame-v1.md
     - live/indie-game-development/work/minimum-game-frame-v2.md
     - live/indie-game-development/TREE.md
     - live/indie-game-development/CHARTER.md
     - gas_coop_game_canon/**
     - all product repositories
     - Sc-damage
     - exact gas roster and gas-to-gas reactions
     - concentrations and reaction thresholds
     - rupture and durability rules
     - damage, health, economy, controls, UI, capacity, helper count,
       carry tuning, networking, balance and implementation.

captures:
  - "PARKED HYPOTHESIS: rare gas-specific Sphere or instability may be reconsidered only after playable evidence that universal capture remains too flat after gas behavior, volume, route and gas-to-gas consequences are present; never introduce it as a default compatibility matrix."

decisions_needed: []

play_check:
  - >
      1 Recite: done — evaluated the owner's proposed universal-capture
      baseline and separated it from the parked specialization idea.
  - >
      2 Investigate: done — re-read authoritative NOW, the current Sphere
      extraction/custody frame, Minimum Game Frame v2 and current CORE;
      confirmed that compatibility was OPEN rather than required.
  - >
      3 Confidence: done — established source constraints were separated from
      the design judgment; the main risk and the exact playable-evidence
      trigger for reconsideration were named.
  - >
      4 Close: done — exact owner verdict cited:
      «любой шар, любой газ может добывать»;
      «он не может повредить шар»;
      «если чувствуется... не хватает какой-то комплексности... тогда уже
      рассмотреть, добавить»;
      «именно для начала это самый лучший вариант».

log: >
  2026-07-17 · s-research-sphere-universal-capture-verdict-001 · research · canon · g-d3a8 · owner selected universal Sphere capture: every standard Sphere takes every gameplay gas, gas type alone cannot damage the shell, compatibility exceptions parked behind playable evidence · history/2026-07-17-s-research-sphere-universal-capture-verdict-001.md

next: |
  CALL c-work-sphere-universal-capture-frame-001
  status: ready
  track: canon
  play: work
  goal: persist the selected non-canon universal Sphere capture baseline in
  gas-sphere-extraction-custody-frame-v1.md without canon admission or
  downstream design expansion

END_OF_FILE: live/indie-game-development/history/2026-07-17-s-research-sphere-universal-capture-verdict-001.md
