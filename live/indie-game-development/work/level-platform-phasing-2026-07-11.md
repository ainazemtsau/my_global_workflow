# Level platform phasing after PGG spike — research brief (2026-07-11)

status: research recommendation; NOT owner-ratified; source of decision `d-level-platform-phasing-001`

## Verdict

The generic level/module standard must precede real Dungeon Architect / PGG integration. Adding it as a later
Phase 2 while leaving today's Phase 1 unchanged would put the contract after the first production modules and repeat
the spike's failure mode. Recommended clean phasing:

- Phase 0 — finish the already-built generator-blind seam and authoritative placed-gas-source path.
- Phase 1 — build a technology-neutral Level/Module Contract plus authoring/build/engine validators.
- Phase 2 — implement DA, PGG, hand-authored and optional library adapters against that contract, plus runtime build
  and seed/ProfileHash handshake.
- Phase 3 — produce real rooms and add typed level features/content through the extension seams.

Phase 1A/1B is a viable lower-churn naming alternative, but the dependency remains hard: contract/validators first,
adapters/runtime second.

## What Phase 0 actually does

Phase 0 is a vertical seam proof on simple hand-tagged geometry, not a generalized level-production platform.

It proves:

1. A built Unity scene can be read without consuming a generator model or leaking Unity/DA types into Core.
2. Simple room and door markers become integer `RoomSpec`/`LinkSpec`, then `TopologyDocument`, then the layered grid.
3. A placed `GasSourceMarker` becomes an engine-free, canonically sorted `GasSourceSpec` at the containing 50 cm cell.
4. Initial seeding and continuous injection live in the authoritative engine step rather than the render adapter, so
   the source affects the deterministic meaning checksum.
5. The owner-visible fixture is two rectangular rooms, one door and one placed source; gas emerges from the object and
   crosses the door.

Phase 0 deliberately does NOT prove:

- real DA or PGG generation;
- a reusable module authoring contract;
- exact irregular occupancy;
- exact mesh-derived door apertures;
- item/prop/machine/spawn anchors;
- module validation;
- runtime shared-seed/ProfileHash session handshake.

Its best reusable result is the typed-extension pattern: read a built-scene marker into a deterministic engine-free
spec, validate/resolve it once, and feed authority through an explicit seam. `GasSourceSpec` is one feature, not the
universal feature model.

## What the old Phase 1 intended

The current direction knowledge describes Phase 1 as:

- minimal real SnapGridFlow module set and flow graph;
- runtime `LevelBootstrap` / `Dungeon.Build()` / `OnPostDungeonBuild`;
- shared seed and normalized `ProfileHash` handshake;
- the SAME `BuiltSceneRoomReader` and source reader unchanged behind the real DA build.

The PGG spike invalidates the last premise for production modules. The reader can detect modules and connections, but
its representation is not physically faithful enough: room renderers collapse to AABBs, the active Door kit supplies
only a vertical opening count, horizontal aperture position is lost, and item metadata produces no anchors. Therefore
old Phase 1 combines three jobs in the wrong order: platform contract, vendor adaptation, and runtime integration.

## What is already genuinely generic

The code already has a useful lower half:

- `TopologyDocument` and `ITopologyProducer` are engine-free and generator-agnostic.
- `Voxelizer` consumes normalized integer topology + `ApertureSpec[]`, not vendor objects.
- `TopologyConformance` is a deterministic engine admission gate.
- `ApertureSpec` already represents a 25 cm sub-face rectangle.
- `GasSourceSpec` demonstrates a typed feature outside topology.
- marker discovery and canonical sorting are generator-blind.

But the upper half is still provisional:

- `DaLevel`, `IDaRoomReader`, and `DaTopologyProducer` are named around one vendor despite carrying generic data.
- `BuiltSceneRoomReader` directly knows DA type names and converts every room to one renderer AABB.
- `SceneTopologyComposer` always emits `Array.Empty<TopologyAnchor>()`.
- current `ApertureSpec` validation proves that a declaration lies on a shared region boundary; it does not independently
  prove that the built mesh contains that exact hole.
- `TopologyConformance` validates an engine document, not whether a reusable prefab is a valid project module.
- the existing `TopologyAnchor` has only volume + local XYZ; it has no feature kind, orientation, schema version or
  typed payload reference.

The generic Phase 1 should preserve the lower half and replace/generalize the provisional upper half.

## Two contracts, not one vendor-shaped standard

### 1. Project Module Contract

A reusable module must carry project-owned, technology-neutral authoring data:

- schema version and stable module id;
- grid frame: gas 50 cm, structure/placement 25 cm;
- pivot, envelope, floor datum and allowed rotations;
- coarse region envelope and exact structural occupancy;
- connection sockets, role/capacity and reserved clearance zones;
- project portal profile and exact aperture geometry;
- feature anchors and typed feature declarations;
- deterministic bake identity and dependency policy.

PGG, DA and library metadata are not this contract. Their adapters/bakers normalize into it.

### 2. Built Level Manifest

After any generator or hand-authored composition, one normalized built-level result should contain, conceptually:

- build identity: schema/profile versions, seed/build key and canonical hash inputs;
- coarse topology: regions, adjacency, portals and breach surfaces;
- exact structure: occupied cells/sub-faces and apertures;
- instantiated anchors and typed feature specs;
- diagnostics needed to explain rejection.

Names are provisional. The key rule is one normalized output independent of producer identity.

```text
hand-authored | PGG bake | DA SGF | future generator | library importer
                              ↓
                    Project Module Contract
                              ↓
                        ModuleValidator
                              ↓
                      Built Level Manifest
                              ↓
                      BuiltLevelValidator
                              ↓
       TopologyDocument + exact structure + typed feature specs
                              ↓
                 Voxelizer / authoritative simulation
```

## DA and PGG are not symmetric adapters

- Dungeon Architect SnapGridFlow is the runtime layout/composition adapter: it chooses and connects modules.
- PGG is an editor-time module-population/bake adapter: it fills reserved interior zones, then emits a static prefab.
- Hand-authored prefabs are a first-class adapter/control.
- Library assets use optional one-way import/normalization adapters. Core must not grow special cases for raw vendor
  modules; an asset that cannot normalize is rejected or wrapped outside authority.

Every path must converge on the project-owned contract before the game consumes the module.

## Validation platform

One validator is not enough; the boundaries fail for different reasons.

### ModuleValidator — before registration/composition

Rejects bad reusable prefabs:

- off-grid pivot/envelope/socket/door profile;
- wrong socket count for endpoint/pass-through/junction/hub role;
- geometry or PGG content inside connection clearance;
- mismatch between declared 25 cm occupancy/aperture and independently sampled built mesh/colliders;
- anchors outside legal occupancy or missing required metadata;
- PGG runtime components, missing dependencies or forbidden vendor state after bake.

The validator may derive and refute geometric facts. It may schema-check semantic design payloads, but it must not
invent them: material, breach threshold, item kind and similar meaning remain owner/fixture-authored typed data.

### Adapter/bake conformance — at vendor boundary

Checks that the PGG bake, DA registration or library import produced the same project contract without silently
dropping information. Vendor-specific data ends here.

### BuiltLevelValidator — after composition

Checks the actual assembled level:

- no physical gaps, overlaps or mismatched connection profiles;
- every logical connection has exactly the physical aperture it declares;
- irregular occupancy remains exact;
- every feature instance resolves to a valid region/cell/anchor;
- one/two/three/four-module acceptance configurations build;
- same normalized input twice yields the same manifest/profile hash.

### Engine admission — existing lower gate

`TopologyConformance` and `Voxelizer` continue rejecting malformed normalized engine data. They do not replace the
module and built-level validators because they cannot see the reusable prefab or original mesh truth.

## Extensible items and level features

Do not put every future object into `TopologyDocument` or an untyped string/object dictionary. Split WHERE from WHAT:

- `LevelAnchor` (provisional name): stable id, owning region/cell, position, orientation, tags/version.
- typed feature specs that reference an anchor: `GasSourceSpec`, `ItemSpawnSpec`, `PlayerSpawnSpec`, `MachineSpec`,
  `ValveSpec`, `LootSocketSpec`, etc.
- one reader/validator/consumer per typed feature class, composed through a registry or explicit catalog.

Structural truth (occupancy, portals, apertures, breach surfaces) belongs to topology/structure. Dynamic or gameplay
payloads belong to typed feature sets. The existing decision to keep gas mass outside `TopologyDocument` remains
correct and is the model for future features.

Unknown authoritative feature kinds must fail loudly. Unknown cosmetic-only features may be ignored only if they are
explicitly classified cosmetic.

## Irregular geometry needs two resolutions of truth

One room-level AABB is acceptable only as a coarse envelope, never as exact near-grid occupancy. The contract should
carry both:

- coarse region/envelope data for far topology;
- exact 25 cm structure occupancy/apertures for the near grid.

The Phase 1 PLAN must choose how coarse irregular rooms map to volumes (exact rectangular decomposition, a separate
occupancy mask attached to one logical region, or another deterministic representation) without changing the player's
room identity merely to satisfy AABB machinery.

## Recommended phases

### Phase 0 — close existing proof

Binding re-review + owner-eye + merge. No expansion into module standards.

### Phase 1 — Generic Level/Module Contract + Validation Platform

PLAN first, then bounded BUILDs. Deliver the two normalized contracts, typed feature-extension rule, exact geometry
truth path, module/built-level validators and hand-authored reference fixtures. No DA/PGG production dependency is
required to prove the contract.

### Phase 2 — Technology adapters + real runtime generation

DA SnapGridFlow runtime adapter, PGG editor-time baker, optional library importers, real `LevelBootstrap`, shared seed,
normalized manifest/ProfileHash handshake, and real 1/2/3/4-module acceptance.

### Phase 3 — Production modules and feature expansion

Real room kit/content plus item/machine/spawn/valve/etc. feature types added through the Phase 1 extension contract.
This phase is not a license for speculative genericity: add a typed feature when a real M1 need appears.

## Options for owner verdict

1. **Clean rephase (recommended):** Phase 1 = contract/validators; old Phase 1 moves to Phase 2; production expansion
   becomes Phase 3. Clearest dependency and least chance of repeating build-before-contract.
2. **Historical numbering:** Phase 1A = contract/validators, Phase 1B = adapters/runtime, Phase 2 = production. Less
   documentation churn, but the hard gate between 1A and 1B must remain explicit.
3. **Leave Phase 1 unchanged, standard later:** reject. Real adapters/modules would be accepted through a reader already
   known to lose occupancy, aperture position and anchors.

## Confidence and limits

Established from current code/canon: Phase 0 scope, current Phase 1 promise, generic lower contracts, AABB/aperture/
anchor gaps, the 50/25 cm structure rule, and the canon requirement to re-derive geometric markers from mesh.

Recommended/inferred: exact names and container split (`ProjectModuleContract`, `BuiltLevelManifest`, `LevelAnchor`) and
whether Phase 1 uses occupancy masks or rectangular decomposition. Those are PLAN decisions, not ratified architecture.

END_OF_FILE: live/indie-game-development/work/level-platform-phasing-2026-07-11.md
