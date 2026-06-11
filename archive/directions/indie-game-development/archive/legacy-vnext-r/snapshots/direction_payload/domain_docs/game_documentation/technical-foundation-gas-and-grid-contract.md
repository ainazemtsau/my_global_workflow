# Technical Foundation — Gas and Grid Contract

## Gas ↔ Grid contract

### Peer foundation

`Gas runtime` и `legacy global Grid` фиксируются как взаимозависимый foundation. Этот boundary не поддерживает схему, в которой Gas можно честно вынуть как самодостаточный asset, а spatial substrate “доделать потом”.

При этом `Gas.Topology` остаётся частью Gas runtime, но только как gas-facing runtime projection / validation layer над общим spatial substrate. Это не делает room topology, room authority или room anchors собственностью Gas.

### Gas-owned responsibilities

Gas владеет host-authoritative gas truth: fixed-step runtime, execution order, substance behavior, mass accounting, reconcile между уровнями представления и gas-side authoritative snapshots / query / visual derivation.

Это включает собственно gas model и её иерархию `T1 / T2 / T3-derived paths`, но не spatial authority уровня.

Gas также владеет gas-facing topology runtime: versioned active / pending state, deterministic ordering для gas consumers, explicit apply / update pipeline для входящего topology / door state и fail-fast validation того, что пришедшая spatial surface консистентна.

### Grid-owned responsibilities

Grid владеет общим spatial substrate: тем, что считается комнатой, `room identity`, `room authority`, `room bounds / cell partitioning`, а также подготовленными `room-data surfaces`, на которые Gas опирается для локализации.

Grid также владеет world semantics для portal / door / room-anchor surfaces. Gas может читать и зеркалить эти факты внутри `Gas.Topology`, но не должен бесшумно авторить их как свои.

### Shared contract surfaces

- **Room identity and localization surface**
Grid должен давать стабильный `roomId`, `room-membership / localization surface` и не-перекрывающиеся `room bounds`, достаточные для room resolution и room-based runtime.
- **Connectivity and portal identity surface**
Grid должен давать `room adjacency` вместе с детерминированной семантикой `connectionId / portalId`, достаточной для transport graph и portal-flux accounting.
- **Door-state surface**
Door state должен приходить как явный shared input на уровне connection, меняться без скрытого полного rebuild и считаться частью transport graph, а не cosmetic scene state.
- **Room-anchor and aperture surface**
Grid должен поставлять подготовленные `room anchors` и `aperture snapshots` со стабильными tags / identities, пригодными для doorway inflow и room-local detail.
- **Topology lifecycle and validation surface**
Shared topology должна поддерживать `versioned active / pending state`, queued changes и проверяемые invariants: unique room ids, symmetric neighbors, non-overlapping bounds, deterministic ids / order.
- **Spatial metrics surface**
Grid должен давать `room-size data`, достаточные для capacity model: `room volume` либо `cell-count / cell-volume equivalent`, если прямой volume не задан.

### Non-owned responsibilities

Gas не должен:

- решать, что считается комнатой, или перенумеровывать `room / portal identity` под удобство своего runtime;
- geometry-rescan’ить уровень, чтобы заново строить `room anchors` или `apertures`;
- угадывать `door state` по визуалу, коллайдерам или proximity;
- подменять отсутствующие `room bounds`, capacities или connection graph скрытыми fallback’ами, hardcoded tunables или self-healing.

Если required surfaces отсутствуют или сломаны, корректное поведение — fail-fast.
