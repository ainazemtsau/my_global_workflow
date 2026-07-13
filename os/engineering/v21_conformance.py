#!/usr/bin/env python3
"""Executable conformance witness for the v21 PLAN binding handoff.

This is deliberately self-contained: the parent process pins the real Python
interpreter and launches every positive/negative case in a fresh child process.
Product adapters must implement the same contract with their real compiler,
discovery tool and filtered runner; this witness only supplies OS-owned truth.
"""

from __future__ import annotations

import copy
import hashlib
import inspect
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable


class ConformanceError(RuntimeError):
    pass


class BindingSentinel(RuntimeError):
    pass


@dataclass(frozen=True)
class CellResult:
    cell: int
    counter: int
    hidden: int
    neighbor: int


@dataclass(frozen=True)
class Fault:
    operation_id: str
    phase: str


class Core:
    """Exact-base fixture API. The proposed public create member is absent."""

    def __init__(self) -> None:
        self.cell = 2
        self.counter = 3
        self.hidden = 5
        self.neighbor = 0
        self._next_operation = 0

    @classmethod
    def existing(cls, topology: tuple[str, str]) -> "Core":
        if topology != ("open", "sealed"):
            raise ValueError("wrong topology")
        return cls()

    def new_operation_id(self) -> str:
        self._next_operation += 1
        return f"core-{id(self):x}-step-{self._next_operation}"

    def step(
        self,
        operation_id: str,
        impulse: tuple[int, int],
        handler: "OwnedHandler | LoopbackOnce",
        fault: Fault,
    ) -> CellResult:
        if fault.operation_id != operation_id:
            raise ConformanceError("fault escaped its operation")
        before = Audit.for_core(self).read()
        try:
            if fault.phase == "before":
                raise BindingSentinel("fault-before")
            handler.handle(self, impulse)
            if fault.phase == "during":
                raise BindingSentinel("fault-during")
            self.counter += impulse[1]
            if fault.phase == "after":
                raise BindingSentinel("fault-after")
            return Audit.for_core(self).read()
        except BindingSentinel:
            self.cell = before.cell
            self.counter = before.counter
            self.hidden = before.hidden
            self.neighbor = before.neighbor
            raise

    def step_source(self, source: tuple[int, int, int]) -> CellResult:
        _, amount, neighbor = source
        self.cell += amount
        self.neighbor = neighbor
        return Audit.for_core(self).read()


class AuditHandle:
    def __init__(self, core: Core) -> None:
        self._core = core

    def read(self) -> CellResult:
        return CellResult(
            self._core.cell,
            self._core.counter,
            self._core.hidden,
            self._core.neighbor,
        )


class Audit:
    @staticmethod
    def for_core(core: Core) -> AuditHandle:
        return AuditHandle(core)


class FaultSelector:
    @staticmethod
    def select(operation_id: str, phase: str) -> Fault:
        if phase not in {"none", "before", "during", "after"}:
            raise ValueError("unknown phase")
        return Fault(operation_id, phase)


class OwnedHandler:
    def __init__(self, owner: Core) -> None:
        self.owner = owner
        self.calls = 0

    def handle(self, core: Core, impulse: tuple[int, int]) -> None:
        if core is not self.owner:
            raise ConformanceError("handler owner mismatch")
        self.calls += 1
        core.cell += impulse[1]


class LoopbackOnce(OwnedHandler):
    def __init__(self, owner: Core) -> None:
        super().__init__(owner)
        self.delegations = 0

    def handle(self, core: Core, impulse: tuple[int, int]) -> None:
        super().handle(core, impulse)
        if self.delegations == 0:
            self.delegations = 1


def decode_cell_result(raw: bytes) -> CellResult:
    data = json.loads(raw.decode("utf-8"))
    if set(data) != {"cell", "counter", "hidden", "neighbor"}:
        raise ConformanceError("golden codec shape mismatch")
    return CellResult(**{name: int(value) for name, value in data.items()})


NODE_GROUPS: dict[str, set[str]] = {
    "OB-1": {
        "reflection:core-create",
        "fixture:two-room-open-sealed",
        "fixture:face-impulse",
        "fixture:owned-handler",
        "callable:audit-for-read",
        "callable:golden-codec",
        "resource:golden-cell",
        "slot:ob1-operation",
        "slot:ob1-fault",
    },
    "OB-2": {
        "producer:core-existing",
        "fixture:two-room-open-sealed",
        "fixture:face-impulse",
        "fixture:loopback-once",
        "callable:audit-for-read",
        "slot:ob2-operation",
        "slot:ob2-fault",
        "control:fault-before",
        "control:fault-during",
        "control:fault-after",
    },
    "OB-3": {
        "producer:core-existing",
        "fixture:single-source-neighbor-zero",
        "callable:audit-for-read",
        "callable:golden-codec",
        "resource:golden-source",
        "callable:compare-all-fields",
    },
}

KIND_BY_PREFIX = {
    "reflection": "callable",
    "fixture": "instance",
    "callable": "callable",
    "resource": "runtime-resource",
    "slot": "slot",
    "producer": "producer",
    "control": "negative-control",
}

OBSERVED_FIELDS = ["cell", "counter", "hidden", "neighbor"]
CRITERIA = {
    "OB-1": "OB-1 binding route reached missing member",
    "OB-2": "OB-2 binding route reached sentinel",
    "OB-3": "OB-3 binding route reached sentinel",
}


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def base_packet() -> dict[str, Any]:
    nodes: list[dict[str, Any]] = []
    for obligation in ("OB-1", "OB-2", "OB-3"):
        for node_id in sorted(NODE_GROUPS[obligation]):
            if any(row["id"] == node_id for row in nodes):
                continue
            prefix = node_id.split(":", 1)[0]
            nodes.append(
                {
                    "id": node_id,
                    "kind": KIND_BY_PREFIX[prefix],
                    "type": "fixture." + node_id.replace(":", "."),
                    "owner": "operation-instance" if node_id.endswith("fault") else "fixture-validator",
                    "signature": node_id,
                    "visibility": "public" if prefix in {"fixture", "producer"} else "test-harness",
                    "args": [],
                    "returns": "void" if prefix == "control" else "fixture.value",
                    "depends_on": [],
                }
            )
    return {
        "schema": 1,
        "base": "B-001",
        "candidate": "P-001",
        "acceptance_hash": sha256_bytes(b"DW-1\nDW-2\nDW-3\n"),
        "planner_session": "plan-author-001",
        "validator_session": "plan-binding-validator-001",
        "observed_candidate": "P-001",
        "product_writes": [],
        "planner_supplied_probe_source": False,
        "complete_sweep": True,
        "derived_obligations": ["OB-1", "OB-2", "OB-3"],
        "coverage": ["OB-1", "OB-2", "OB-3"],
        "observed_fields": OBSERVED_FIELDS.copy(),
        "fault_phases": ["before", "during", "after"],
        "nodes": nodes,
        "toolchain": {
            "interpreter": str(Path(sys.executable).resolve()),
            "version": sys.version.split()[0],
        },
    }


def node_map(packet: dict[str, Any]) -> dict[str, dict[str, Any]]:
    rows = packet.get("nodes")
    if not isinstance(rows, list):
        raise ConformanceError("nodes must be a list")
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        node_id = row.get("id")
        if not isinstance(node_id, str) or node_id in result:
            raise ConformanceError("node id missing or duplicated")
        result[node_id] = row
    return result


def validate_structure(packet: dict[str, Any]) -> dict[str, dict[str, Any]]:
    if packet.get("planner_session") == packet.get("validator_session"):
        raise ConformanceError("planner self-validated")
    if packet.get("product_writes") != []:
        raise ConformanceError("binding validator wrote product")
    if packet.get("candidate") != packet.get("observed_candidate"):
        raise ConformanceError("stale candidate")
    if packet.get("planner_supplied_probe_source") is not False:
        raise ConformanceError("planner supplied probe source")
    if packet.get("complete_sweep") is not True:
        raise ConformanceError("incomplete sweep")
    if packet.get("derived_obligations") != ["OB-1", "OB-2", "OB-3"]:
        raise ConformanceError("validator did not derive the full union")
    if packet.get("coverage") != packet.get("derived_obligations"):
        raise ConformanceError("candidate coverage differs from derived union")
    if packet.get("observed_fields") != OBSERVED_FIELDS:
        raise ConformanceError("atomic observation is not full-state")
    if packet.get("fault_phases") != ["before", "during", "after"]:
        raise ConformanceError("negative phase sweep is incomplete")

    nodes = node_map(packet)
    for obligation, required in NODE_GROUPS.items():
        missing = sorted(required - nodes.keys())
        if missing:
            raise ConformanceError(f"{obligation} missing bindings: {','.join(missing)}")
    for node_id, row in nodes.items():
        prefix = node_id.split(":", 1)[0]
        expected_kind = KIND_BY_PREFIX[prefix]
        if row.get("kind") != expected_kind:
            raise ConformanceError(f"kind conflation: {node_id}")
        if node_id in {"slot:ob1-fault", "slot:ob2-fault"} and row.get("owner") != "operation-instance":
            raise ConformanceError(f"fault slot lacks operation-instance ownership: {node_id}")
        for key in ("type", "owner", "signature", "visibility", "args", "returns", "depends_on"):
            if key not in row:
                raise ConformanceError(f"{node_id} missing {key}")
        for dependency in row["depends_on"]:
            if dependency not in nodes:
                raise ConformanceError(f"{node_id} unresolved dependency {dependency}")
    return nodes


def assert_same_audit(before: CellResult, after: CellResult) -> None:
    for name in OBSERVED_FIELDS:
        if getattr(before, name) != getattr(after, name):
            raise ConformanceError(f"atomic control corrupted {name}")


def exercise_obligation(obligation: str) -> None:
    topology = ("open", "sealed")
    impulse = (0, 1)
    if obligation == "OB-1":
        if getattr(Core, "create", None) is not None:
            raise ConformanceError("exact-base absent route unexpectedly exists")
        core = Core.existing(topology)
        handler = OwnedHandler(core)
        operation = core.new_operation_id()
        fault = FaultSelector.select(operation, "none")
        core.step(operation, impulse, handler, fault)
        golden = decode_cell_result(b'{"cell":3,"counter":4,"hidden":5,"neighbor":0}')
        if Audit.for_core(core).read() != golden or handler.owner is not core or handler.calls != 1:
            raise ConformanceError("owned handler/golden/audit route mismatch")
        return

    if obligation == "OB-2":
        for phase in ("before", "during", "after"):
            core = Core.existing(topology)
            before = Audit.for_core(core).read()
            loopback = LoopbackOnce(core)
            operation = core.new_operation_id()
            fault = FaultSelector.select(operation, phase)
            try:
                core.step(operation, impulse, loopback, fault)
            except BindingSentinel:
                pass
            else:
                raise ConformanceError(f"negative control {phase} did not fire")
            assert_same_audit(before, Audit.for_core(core).read())
            if loopback.delegations not in {0, 1}:
                raise ConformanceError("loopback delegated more than once")
        first = Core.existing(topology)
        second = Core.existing(topology)
        wrong_fault = FaultSelector.select(first.new_operation_id(), "none")
        try:
            second.step(second.new_operation_id(), impulse, OwnedHandler(second), wrong_fault)
        except ConformanceError:
            pass
        else:
            raise ConformanceError("cross-operation fault reuse was accepted")
        return

    if obligation == "OB-3":
        core = Core.existing(topology)
        observed = core.step_source((0, 1, 0))
        golden = decode_cell_result(b'{"cell":3,"counter":3,"hidden":5,"neighbor":0}')
        if observed != golden or Audit.for_core(core).read() != golden:
            raise ConformanceError("source isolation/golden route mismatch")
        return

    raise ConformanceError(f"unknown obligation {obligation}")


def generate_probe_source(obligation: str) -> str:
    safe = obligation.replace("-", "_")
    return (
        f"def probe_{safe}():\n"
        f"    exercise_obligation({obligation!r})\n"
        f"    raise BindingSentinel({CRITERIA[obligation]!r})\n"
    )


def actual_compile_discover_run(packet: dict[str, Any]) -> dict[str, Any]:
    expected_ids = ["probe_OB_1", "probe_OB_2", "probe_OB_3"]
    sources = [generate_probe_source(item) for item in packet["derived_obligations"]]
    combined = "\n".join(sources)
    with tempfile.TemporaryDirectory(prefix="v21-binding-") as scratch:
        source_path = Path(scratch) / "binding_probes.py"
        source_path.write_text(combined, encoding="utf-8", newline="\n")
        before = sha256_bytes(source_path.read_bytes())
        code = compile(source_path.read_text(encoding="utf-8"), str(source_path), "exec")
        namespace: dict[str, Any] = {
            "BindingSentinel": BindingSentinel,
            "exercise_obligation": exercise_obligation,
        }
        exec(code, namespace)
        discovered = sorted(
            name for name, value in namespace.items() if name.startswith("probe_") and inspect.isfunction(value)
        )
        if discovered != expected_ids:
            raise ConformanceError("discovery is not the exact unique obligation union")
        criteria: list[str] = []
        for name in discovered:
            try:
                namespace[name]()
            except BindingSentinel as error:
                criteria.append(str(error))
            else:
                raise ConformanceError(f"{name} passed instead of reaching binding RED")
        after = sha256_bytes(source_path.read_bytes())
        if before != after:
            raise ConformanceError("validator mutated generated probe source")
    if criteria != [CRITERIA[item] for item in packet["derived_obligations"]]:
        raise ConformanceError("wrong filtered RED criterion")
    return {
        "compile_exit": 0,
        "discovered": expected_ids,
        "criteria": criteria,
        "generated_source_hash": sha256_bytes(combined.encode()),
    }


def validate(packet: dict[str, Any]) -> dict[str, Any]:
    validate_structure(packet)
    observations = actual_compile_discover_run(packet)
    return {
        "candidate": packet["candidate"],
        "testability_hash": sha256_bytes(canonical_bytes(packet)),
        "validator_session": packet["validator_session"],
        "product_writes": [],
        **observations,
    }


def mutate(packet: dict[str, Any], case: str) -> None:
    if case.startswith("missing:"):
        target = case.split(":", 1)[1]
        packet["nodes"] = [row for row in packet["nodes"] if row["id"] != target]
    elif case == "planner-self-validates":
        packet["validator_session"] = packet["planner_session"]
    elif case == "validator-product-write":
        packet["product_writes"] = ["tests/forbidden.py"]
    elif case == "stale-candidate":
        packet["observed_candidate"] = "P-stale"
    elif case == "planner-supplies-probe":
        packet["planner_supplied_probe_source"] = True
    elif case == "incomplete-sweep":
        packet["complete_sweep"] = False
    elif case == "trusts-candidate-union":
        packet["derived_obligations"] = ["OB-1", "OB-2"]
        packet["coverage"] = ["OB-1", "OB-2"]
    elif case == "coverage-mismatch":
        packet["coverage"] = ["OB-1", "OB-2"]
    elif case == "kind-conflation":
        next(row for row in packet["nodes"] if row["id"] == "fixture:owned-handler")["kind"] = "runtime-resource"
    elif case == "fault-owner-generic":
        next(row for row in packet["nodes"] if row["id"] == "slot:ob2-fault")["owner"] = "operation:Step"
    elif case == "hidden-unobserved":
        packet["observed_fields"].remove("hidden")
    elif case == "negative-after-missing":
        packet["fault_phases"].remove("after")
    elif case == "unresolved-dependency":
        packet["nodes"][0]["depends_on"] = ["fixture:does-not-exist"]
    elif case != "valid":
        raise ConformanceError(f"unknown case {case}")


INVALID_CASES = [
    *(f"missing:{node}" for node in sorted(set().union(*NODE_GROUPS.values()))),
    "planner-self-validates",
    "validator-product-write",
    "stale-candidate",
    "planner-supplies-probe",
    "incomplete-sweep",
    "trusts-candidate-union",
    "coverage-mismatch",
    "kind-conflation",
    "fault-owner-generic",
    "hidden-unobserved",
    "negative-after-missing",
    "unresolved-dependency",
]


def run_case(case: str) -> int:
    packet = base_packet()
    try:
        mutate(packet, case)
        receipt = validate(packet)
    except Exception as error:  # the child reports the exact rejected class
        print(json.dumps({"case": case, "status": "RED", "error": str(error)}, sort_keys=True))
        return 2
    print(json.dumps({"case": case, "status": "GREEN", "receipt": receipt}, sort_keys=True))
    return 0


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_parent() -> int:
    script = Path(__file__).resolve()
    interpreter = Path(sys.executable).resolve()
    cases = ["valid", *INVALID_CASES]
    outcomes: list[dict[str, Any]] = []
    for case in cases:
        process = subprocess.run(
            [str(interpreter), "-I", "-S", str(script), "--case", case],
            text=True,
            capture_output=True,
            check=False,
        )
        expected = 0 if case == "valid" else 2
        if process.returncode != expected:
            print(process.stdout, end="")
            print(process.stderr, end="", file=sys.stderr)
            raise ConformanceError(f"case {case} exit {process.returncode}, expected {expected}")
        outcomes.append(json.loads(process.stdout))
    result = {
        "status": "V21_CONFORMANCE_GREEN",
        "interpreter_path": str(interpreter),
        "interpreter_sha256": file_sha256(interpreter),
        "interpreter_version": sys.version.split()[0],
        "script_sha256": file_sha256(script),
        "positive_cases": 1,
        "negative_cases": len(INVALID_CASES),
        "case_digest": sha256_bytes(canonical_bytes(outcomes)),
    }
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--case":
        raise SystemExit(run_case(sys.argv[2]))
    if len(sys.argv) != 1:
        raise SystemExit("usage: v21_conformance.py [--case CASE]")
    raise SystemExit(run_parent())
