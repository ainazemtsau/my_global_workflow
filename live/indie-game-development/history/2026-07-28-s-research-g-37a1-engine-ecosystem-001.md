# RESULT s-research-g-37a1-engine-ecosystem-001

call: owner-direct-2026-07-28-engine-ecosystem-research
direction: indie-game-development
play: research
node/task: g-37a1/engine-ecosystem

outcome: |
  Вопрос: какой готовый, полуготовый или альтернативный технический стек быстрее
  и с меньшим риском доведёт утверждённое ядро до packaged proof на двух машинах:
  остаться на Unity, сменить движок или взять специализированную платформу.

  КОРОТКИЙ ВЕРДИКТ. Сейчас движок менять не следует. Это не вердикт «Unity
  навсегда» и не защита sunk cost. У Unity-проекта есть три полезных актива,
  которых нет у пустого проекта на другом движке: CPU C# gas transport,
  determinism/replication contract и FishNet edge. Старый product check отнёс
  rewrite к structure/topology, а не к этим слоям. После amendment живых строк
  шестнадцать, retired row 7 больше нельзя считать шестым rewrite; прежние
  50-90 focused days являются только stale dependency map, а не свежим forecast.

  Главная buy/build-граница поэтому не «купить симуляцию газа», а «купить или
  сузить runtime topology + meshing + collider substrate». Ни один найденный
  asset не покупает специфический контракт игры: атомарный dig -> changed solid
  cells/faces -> graded aperture -> conservative migration двух газов ->
  replicated state -> full reset. Это останется собственной интеграцией в любом
  движке.

  UNITY SHORTLIST.

  1. Digger PRO 8.1: региональная list price около $99; runtime sphere/custom
     brushes, async queue, mesh colliders, reset/persistence, removed-matter и
     modified-voxel aggregates. Networking отсутствует; vendor предлагает
     передавать параметры операции. Он может снять ориентировочно 12-25 дней
     geometry/collider work, но только если spike докажет two-machine convergence
     и Core остаётся единственной authority. Критический пробел: public
     ModificationResult не отдаёт координаты changed voxels/faces или новую
     adjacency, поэтому Digger нельзя заранее назвать authoritative topology.

  2. Voxel Play 4: более широкий full-source voxel-world stack; smooth Surface
     Nets, runtime edits, colliders, save/load, voxel/chunk APIs, RLE chunk
     buffers и официальный Mirror path. Это ближе к точному topology read model,
     но не имеет FishNet adapter и может потребовать заменить world
     representation. Ориентировочный gross saving 15-30 дней только если grid
     маппится на существующий gas field без второго сетевого мира.

  3. Narrow Core-owned cell grid: не marketplace asset, но важный контрольный
     backend. Фиксированный участок, material only removed, full reset and no
     infinite streaming делают задачу уже универсального voxel engine. Если
     blocky/quantized representation допустима, именно этот вариант может быть
     быстрее и проверяемее любого general-purpose plugin.

  4. Voxel Digging Master 1.2.0: $24, bounded URP template, Marching Cubes,
     Jobs/Burst, FPS body, runtime dig/fill and delta saves. Выпущен весной 2026,
     шесть reviews; networking не заявлен. Это дешёвый source/prototype probe, не
     production bet.

  5. Voxelica 2.0.3: $50, runtime sculpting, persistence, multi-material,
     Jobs/Burst and modular hulls. Network/deterministic edit contract публично
     не доказан. Это longlist comparator, не текущий лидер.

  Dungeon Architect Unity 1.23 остаётся полезным procedural generation toolkit,
  но не shipped runtime excavation engine: GPU Voxels для Unity только
  Exploring/Coming. В текущем core level generation прямо исключена, поэтому DA
  не сокращает этот результат. Но это не значит, что его future value равен
  нулю: следующий demo outcome снова требует генератор, поэтому существующая
  Unity-лицензия может экономить будущую работу. Состав и cross-engine entitlement
  покупки надо проверить у vendor; маркетинговое «one license» не является
  доказательством переноса Unity Asset Store purchase на Fab.

  Zibra Smoke & Fire, BrazeFX, Obi, Unreal FluidNinja и Niagara не имеют в
  публичной документации контракта deterministic cross-machine state,
  replication and finite two-species conservation. Их допустимая роль —
  downstream visual adapter после authoritative solver; не замена gas core.

  ENGINE ALTERNATIVES.

  Godot 4.7.1 + Zylann Voxel Tools — сильнейшая настоящая open-source
  альтернатива. Godot and Voxel Tools are MIT; Voxel Tools actively supplies
  runtime editable smooth/block terrain, caves and collision. Но tagged Voxel
  Tools 1.6 targets Godot 4.6; multiplayer synchronization docs call the feature
  very experimental, synchronizer is documented for VoxelTerrain rather than
  VoxelLodTerrain, and GDExtension-to-C# access is reflection-based. Pure C# gas
  contracts may port, while FishNet, scenes, renderer and build wiring do not.
  Comparative range 45-110 focused days is LOW-confidence inference, not a
  forecast. Verdict: best fallback/bakeoff target if Unity topology candidates
  fail, not a demonstrated acceleration now.

  Unreal 5.8 + Voxel Plugin 2 is the strongest commercial non-Unity candidate.
  Voxel Plugin costs about $349 and offers volumetric terrain, runtime sculpt,
  collision and save/load, but current 2.0p8 supports UE 5.6/5.7, calls runtime
  edits experimental, provides no out-of-box edit replication and no simple
  removed-material gameplay result. Porting C#/FishNet adds the same integration
  bottleneck the plugin does not solve. Dungeon Architect 3.6 on Unreal has a
  shipped GPU voxel generator and multiplayer dungeon build, but published docs
  do not demonstrate repeated player-authored post-build digging or replication
  of those edits. FluidNinja explicitly does not support multiplayer. Verdict:
  stronger visuals/tooling, no credible time advantage for this core.

  Luanti is the only mature full voxel game platform found with digging,
  player physics and client/server multiplayer already native. It becomes
  competitive only if block world, Lua/C++ and a Minecraft-like representation
  are acceptable; otherwise it changes the product and discards C#/FishNet.
  Voxel Farm has relevant middleware but stale public Unity/UE4 surfaces,
  partial/closed source tiers and no current deterministic-network proof.
  Flax, O3DE, Stride, Bevy/Fyrox, OpenVDB, Blast and Flow do not remove the
  central mutable-topology/network/gas transaction and therefore are not speed
  paths.

  RECOMMENDED PROBE, not implementation authorization. Freeze one engine-neutral
  acceptance trace, then compare Digger, Voxel Play 4 and narrow Core grid under
  the same kill gates. A host command must: (1) remove a player-chosen volume;
  (2) give the same topology checksum on two packaged machines at one ordered
  tick; (3) update collision so the player enters and jumps out; (4) map width to
  graded conductivity; (5) preserve total mass of both gases; (6) reject/resolve
  overlapping two-player edits deterministically; (7) survive replay/late-join
  or an explicitly scoped substitute; (8) full-reset to the exact initial
  checksum; (9) meet a named frame-time/queue budget with no dropped command.

  This bakeoff measures time from today's product, including port/learning tax.
  It should separately record the repeatable native cost after one-time port, so
  current Unity assets do not masquerade as engine quality. Godot is opened only
  if all Unity backends miss a kill gate or budget; Unreal only if its voxel
  preview, version/license and C# port questions first receive evidence.

  SWITCH RULE. Change engines only when the alternative passes every correctness
  gate and shows a material risk-adjusted advantage larger than the uncertainty,
  after port/learning cost and 12-18-month maintenance are counted. A prettier
  local digging demo or nominally fewer first-slice days is insufficient.

sources: |
  Primary evidence used:
  - local approved core and current product fit receipts:
    work/core-requirements-g-37a1.md;
    history/2026-07-28-s-research-g-37a1-engine-fit-check-001.md.
  - Digger: https://assetstore.unity.com/packages/tools/terrain/digger-pro-voxel-terrain-sculpting-149753
    and https://ofux.github.io/Digger-Documentation/Runtime.html and /FAQ.html.
  - Voxel Play 4: https://store.kronnect.com/products/voxel-play-4 and
    https://kronnect.com/docs/voxel-play-4/multiplayer-api/.
  - Voxel Digging Master: https://assetstore.unity.com/packages/templates/packs/voxel-digging-master-366534.
  - Voxelica: https://assetstore.unity.com/packages/tools/terrain/voxelica-voxel-engine-162883.
  - Dungeon Architect: https://dungeonarchitect.dev/ and
    https://blog.dungeonarchitect.dev/roadmap-unity/.
  - Godot/Voxel Tools: https://godotengine.org/license/,
    https://github.com/Zylann/godot_voxel and
    https://voxel-tools.readthedocs.io/en/latest/multiplayer/.
  - Unreal/Voxel Plugin: https://www.unrealengine.com/license,
    https://docs.voxelplugin.com/knowledgebase/blueprints/runtime-edits-and-sculpting
    and https://docs.voxelplugin.com/resources/licensing.
  - Luanti: https://github.com/luanti-org/luanti.

confidence: |
  HIGH that no engine/plugin supplies the exact topology-gas-network transaction;
  HIGH that immediate migration has no evidenced time advantage; HIGH that DA
  does not solve current-core digging and may retain future generation value.

  MEDIUM that Digger, Voxel Play 4 and a narrow grid are the right first bakeoff
  set. Digger's aggregate-only public result API and Voxel Play's larger world
  ownership are both material unknowns.

  LOW for all day savings and comparative totals. Marketplace documentation can
  establish capabilities, not integration duration. The prior 50-90-day Unity
  number is stale after owner amendments and was never a forecast.

limits: |
  No asset was bought or run; no Unity, Godot or Unreal project was mutated; no
  product code was written. Prices are regional, pre-tax snapshots and sales may
  end. No vendor was contacted about source access, cross-store entitlement,
  budget caps or unreleased roadmap dates.

  Three fresh same-family adversarial pre-passes revised the report: Digger was
  demoted from sole favourite to co-equal spike candidate; DA future option value
  was restored; source claims were narrowed from impossibility to absence of a
  published contract. This is not binding fresh G5 closure evidence.

state_changes: |
  Against fresh live/indie-game-development state:
  - set NOW.md `updated` to `2026-07-28 by s-research-g-37a1-engine-ecosystem-001`;
  - preserve the current sole frontier `c-converge-verify-g-37a1-core-rows-001`,
    all calls, route order, tasks, bet, forecast status and TREE/CHARTER;
  - upsert only issue `i-engine-fit-decision-ladder`: append this ecosystem
    research to `review_when`, explicitly marking the old 50-90 range stale for
    the sixteen live rows and recording the no-migration-now / three-backend
    Unity bakeoff recommendation as evidence, not the owner's step-5 verdict;
    append this receipt to its `evidence`;
  - append the `log` line below once to LOG.md and save this complete RESULT as
    history/2026-07-28-s-research-g-37a1-engine-ecosystem-001.md.
  Maintain every END_OF_FILE trailer and preserve unrelated current edits.

captures:
  - The expensive decision is ownership of topology truth, not the engine logo.
  - Digger's public ModificationResult is aggregate-only; a geometry plugin that
    cannot expose exact changed cells may remain only a mesh/collider projection.
  - Dungeon Architect has zero current-core acceleration but nonzero future
    generation option value; sunk purchase price and avoided future work are
    different quantities.
  - Blocky 3D or 2.5D could remove more work than an engine switch, but that is a
    product representation decision for the owner, not an engineering shortcut
    to take silently.

decisions_needed:
  - At owner step 5 after the required fresh row verification: choose whether
    blocky 3D and/or 2.5D are admissible representations, then approve or reject
    the bounded topology-backend bakeoff. No owner verdict is inferred here.

play_check:
  - "1 Recite: done - one bounded question compared ready Unity assets, Godot,
    Unreal and specialized stacks against the sixteen live core lines."
  - "2 Investigate: done - primary vendor/project sources were checked; five
    independent generator branches were merged and deduplicated."
  - "3 Confidence: done - stated capabilities, inferred day deltas, conflicts,
    stale baseline and answer-changing probes are separated."
  - "4 Close: done - recommendation, sources, confidence, limits and the exact
    return-to-parent marker are present; no engine-fate verdict was attributed to
    the owner."

log: 2026-07-28 | s-research-g-37a1-engine-ecosystem-001 | research | direction | g-37a1/engine-ecosystem: no current engine migration has an evidenced time advantage; preserve the existing C# gas/determinism/FishNet assets, treat Dungeon Architect as future generation option rather than a core-digging solution, and compare Digger PRO, Voxel Play 4 and a narrow Core-owned grid under one two-machine topology-gas-reset contract before any engine verdict; Godot plus Voxel Tools is the strongest open-source fallback and Unreal plus Voxel Plugin the strongest commercial fallback, but both add port tax while retaining experimental edit-replication seams. -> history/2026-07-28-s-research-g-37a1-engine-ecosystem-001.md

next: |
  return-to-parent i-engine-fit-decision-ladder; preserve current route frontier
  c-converge-verify-g-37a1-core-rows-001

END_OF_FILE: live/indie-game-development/history/2026-07-28-s-research-g-37a1-engine-ecosystem-001.md
