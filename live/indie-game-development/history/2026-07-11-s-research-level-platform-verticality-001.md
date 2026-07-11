# RESULT — s-research-level-platform-verticality-001 (2026-07-11)

session: s-research-level-platform-verticality-001 (Codex; play: research; checkpoint extending pending phase decision)
direction: indie-game-development / g-9c41 / level-platform verticality

## Owner summary

Verticality добавлена как standing future requirement без преждевременного строительства большого уровня. Главная
архитектурная поправка: `module` — единица размещения/bake, а `room/region` — единица topology/gas; один module обязан
допускать 1:N logical rooms на разных высотах, собственный internal room graph и external sockets, каждый из которых
ссылается на конкретную внутреннюю room. Connections и apertures резервируются для всех шести направлений.

Это усиливает, но не решает pending d-level-platform-phasing-001: рекомендованная Phase 1 строит generic 3D contract
и validators, Phase 2 — DA/PGG adapters/runtime. В Phase 1 достаточно дешёвого contract fixture: один маленький
compound module, две комнаты на разных Z и одна внутренняя вертикальная связь. Огромный модуль, лестницы/лифты,
navigation, streaming и production vertical content остаются отложенными.

```text
RESULT s-research-level-platform-verticality-001 (call: owner-plain-level-verticality-2026-07-11)
direction: indie-game-development   play: research   node/task: g-9c41/level-platform-verticality
outcome: |
  CHECKPOINT / OWNER REQUIREMENT FOLDED, PHASE VERDICT STILL PENDING. The non-canonical platform brief now requires
  full-3D `Level → ModuleInstance → LogicalRoom/Region → structure cells` hierarchy; one module may contain 1:N
  logical rooms at different heights, internal connections are distinct from external sockets, and connections/
  apertures are modeled across ±X/±Y/±Z. Phase 1 reserves this with a minimal two-stacked-room compound-module
  contract fixture; huge vertical content and traversal/runtime complexity remain deferred. No canon, phase choice,
  downstream CALL or product code is changed; primary NOW.next remains Phase 0.
evidence: |
  Owner words this session: «будут вертикальные уровни», «большие модули, состоящие из комнат», «внутри он разбит
  на комнаты, и мы ... должны это парсить как комнаты», and «это не надо сейчас делать ... мы должны закладывать».
  Current product code read-only at GasCoopGame_dev@5faeffb7: TopologyVolume already has Min/Extent X/Y/Z and
  VoxelFaces already exposes Neg/Pos X/Y/Z (six directions), so the lower grid is genuinely 3D. The missing upper
  contracts remain: BuiltSceneRoomReader emits one RoomSpec per module root and derives a wall opening only from
  Door-kit height; StructureVoxelizer explicitly skips `normalAxis == 2` (Z-normal apertures); SceneTopologyComposer
  still emits empty anchors. knowledge/g9c41-gas-engine-SPEC.md also names floor/ceiling apertures as an expressiveness
  extension rather than a current implementation.
  Established: the hierarchy/cardinality and six-direction representation must be reserved before vendor adapters;
  actual giant-module content is deferred by owner instruction. Inference needing PLAN: exact manifest type names,
  stable-id derivation, room-vs-region cardinality and whether the minimal stacked fixture opens a structural aperture
  now or only proves schema/validator expressibility. review: n/a — research-only, no product/canon change.
state_changes: |
  PATCH non-canonical work/level-platform-phasing-2026-07-11.md with the owner verticality requirement, explicit
  Level→ModuleInstance→LogicalRoom hierarchy, internal/external connections, six-direction reservation, minimal
  stacked-room Phase 1 fixture, and named deferrals.
  live/indie-game-development/NOW.md: set updated to
  `2026-07-11 by s-research-level-platform-verticality-001`; PATCH pending decision
  `d-level-platform-phasing-001.recommendation` to include full 3D, module!=room, compound 1:N rooms and six-direction
  connections; preserve its options and preserve all bet/tasks/open_calls/other decisions/recurring/current next.
  live/indie-game-development/LOG.md: append exactly the `log:` line below once.
  live/indie-game-development/work/board/dashboard.html: update the existing phasing decision row and add the owner
  verticality requirement to the 2026-07-11 journal; preserve all other current sections, including concurrent Gate-Q.
  Save this full RESULT once at
  live/indie-game-development/history/2026-07-11-s-research-level-platform-verticality-001.md.
  No CHARTER.md, TREE.md, knowledge canon, task status, open_call, product repo or NOW.next change.
captures:
  - Hierarchy invariant: ModuleInstance is a placement/bake container; LogicalRoom/Region is topology/gas truth;
    cardinality is 1:N and external sockets reference one internal room.
  - Full-3D invariant: connection/aperture planes carry one of six normals; never encode all vertical movement as a
    wall portal or floor number outside the integer coordinate frame.
  - Phase 1 non-vacuous reservation: tiny compound fixture with two rooms at different Z and one internal vertical
    connection; no art/DA runtime/traversal needed.
  - Deferred honestly: huge 80×80×20–40 m content, stairs/ladders/elevators/navmesh, streaming/perf policy and
    floor/ceiling breach implementation.
decisions_needed:
  - q: d-level-platform-phasing-001 — choose the phasing with the new vertical/compound-module requirement folded in.
    options: ["A: clean rephase — Phase 1 generic 3D contract/validators; old Phase 1 becomes Phase 2 adapters/runtime; Phase 3 production extensions/vertical content", "B: keep numbering — Phase 1A generic 3D contract/validators; Phase 1B adapters/runtime; Phase 2 production extensions/vertical content", "C: keep current Phase 1 unchanged and add the standard later"]
    recommendation: "A; vertical compound modules make contract-before-adapters even more important. B remains a naming-only alternative; C would bake one-module=one-room and wall-only assumptions into the first real DA integration."
play_check:
  - 1 Recite: done — bounded addition = reserve vertical levels/compound modules now without building huge content.
  - 2 Investigate: done — checked current brief/canon and live product 3D volume/faces versus one-root reader,
    wall-only aperture and empty-anchor limits at dev@5faeffb7; no web or product writes needed.
  - 3 Confidence: done — separated already-3D lower grid and owner-mandated cardinality from provisional manifest/
    stable-id choices and explicitly split do-now reservation from deferred production implementation.
  - 4 Close: done as checkpoint — brief/decision extended, primary next preserved, and A/B owner verdict still required
    before any phase rewrite or PLAN-only CALL.
log: 2026-07-11 — research/checkpoint (g-9c41/level-platform verticality, s-research-level-platform-verticality-001): owner added the standing future requirement for vertical levels and compound modules containing 1:N logical rooms; the platform brief now reserves a full-3D hierarchy, internal/external six-direction connections and a minimal stacked-room contract proof while deferring huge-module content. d-level-platform-phasing-001 still awaits A/B; primary next remains Phase 0. → history/2026-07-11-s-research-level-platform-verticality-001.md
next: |
  awaiting_decision d-level-platform-phasing-001; primary direction next remains
  work/c-exec-lv-ingest-phase0-call.md. On owner A/B verdict, a fresh session ratifies the chosen phase naming and
  authors the generic 3D platform PLAN-only CALL; no BUILD starts from this checkpoint.
```

END_OF_FILE: live/indie-game-development/history/2026-07-11-s-research-level-platform-verticality-001.md
