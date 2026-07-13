#!/usr/bin/env python3
"""Executable reference witness for the v21 PLAN binding gate.

The corpus deliberately uses several process boundaries.  A parent launches one
case process; that process materializes immutable authority/candidate fixtures
and launches a fresh validator; the validator launches real CPython compile,
discovery, filtered-runner and union-runner commands.  The only runtime path to
GREEN is the typed registry/recipe executor below.  Product adapters must bind
the same contract to their native stack during SETUP/RE-SYNC.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import inspect
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable


VALIDATOR_RED = 2
HARNESS_FATAL = 3
BINDING_SENTINEL_EXIT = 7
ISOLATION_FLAGS = ["-I", "-S"]
OBSERVED_FIELDS = ["cell", "counter", "hidden", "neighbor"]
FAULT_PHASES = ["before", "during", "after"]


class HarnessError(RuntimeError):
    """The conformance harness itself is invalid; never an expected RED."""


@dataclass(frozen=True, order=True)
class Gap:
    code: str
    path: str
    detail: str = ""

    def row(self) -> dict[str, str]:
        return {"code": self.code, "path": self.path, "detail": self.detail}


@dataclass(frozen=True)
class CompletionProof:
    token: object
    obligation: str
    trace: tuple[dict[str, Any], ...]


FIXTURE_SOURCE = r'''import json
from dataclasses import dataclass

@dataclass(frozen=True)
class Topology:
    open_room: str
    sealed_room: str

    @staticmethod
    def two_room(open_room, sealed_room):
        return Topology(open_room, sealed_room)

@dataclass(frozen=True)
class Impulse:
    face: int
    amount: int

    @staticmethod
    def at_face(face, amount):
        return Impulse(face, amount)

@dataclass(frozen=True)
class SourceInput:
    face: int
    amount: int
    neighbor: int

    @staticmethod
    def at_face(face, amount, neighbor):
        return SourceInput(face, amount, neighbor)

@dataclass(frozen=True)
class OperationId:
    value: str

@dataclass(frozen=True)
class Fault:
    operation_id: OperationId
    phase: str

@dataclass(frozen=True)
class CellResult:
    cell: int
    counter: int
    hidden: int
    neighbor: int

class RouteFault(RuntimeError):
    pass

class Handler:
    def apply(self, core, impulse):
        raise NotImplementedError

class Core:
    def __init__(self):
        self.cell = 2
        self.counter = 3
        self.hidden = 5
        self.neighbor = 0
        self._next_operation = 0

    @classmethod
    def existing(cls, topology):
        if not isinstance(topology, Topology):
            raise TypeError("topology")
        return cls()

    def new_operation_id(self):
        self._next_operation += 1
        return OperationId("op-" + str(self._next_operation))

    def step(self, operation_id, impulse, handler, fault):
        if fault.operation_id != operation_id:
            raise ValueError("fault owner")
        if fault.phase == "before":
            raise RouteFault("before")
        handler.apply(self, impulse)
        if fault.phase == "during":
            raise RouteFault("during")
        self.counter += impulse.amount
        if fault.phase == "after":
            raise RouteFault("after")
        return Audit.for_core(self).read()

    def step_source(self, source):
        self.cell += source.amount
        self.neighbor = source.neighbor
        return Audit.for_core(self).read()

class AuditHandle:
    def __init__(self, core):
        self._core = core

    def read(self):
        return CellResult(
            self._core.cell,
            self._core.counter,
            self._core.hidden,
            self._core.neighbor,
        )

class Audit:
    @staticmethod
    def for_core(core):
        return AuditHandle(core)

class FaultSelector:
    @staticmethod
    def select(operation_id, phase):
        if phase not in {"none", "before", "during", "after"}:
            raise ValueError("phase")
        return Fault(operation_id, phase)

class OwnedHandler(Handler):
    def __init__(self, owner):
        self.owner = owner
        self.calls = 0

    def apply(self, core, impulse):
        if core is not self.owner:
            raise ValueError("owner")
        self.calls += 1
        core.cell += impulse.amount

    def owner_ref(self):
        return self.owner

    def call_count(self):
        return self.calls

class LoopbackOnce(OwnedHandler):
    def __init__(self, owner):
        super().__init__(owner)
        self.delegations = 0

    def apply(self, core, impulse):
        super().apply(core, impulse)
        if self.delegations == 0:
            self.delegations = 1

    def delegation_count(self):
        return self.delegations

class Codec:
    @staticmethod
    def decode_cell_result(raw):
        data = json.loads(raw.decode("utf-8"))
        return CellResult(
            int(data["cell"]),
            int(data["counter"]),
            int(data["hidden"]),
            int(data["neighbor"]),
        )

class Observe:
    @staticmethod
    def cell(value):
        return value.cell

    @staticmethod
    def counter(value):
        return value.counter

    @staticmethod
    def hidden(value):
        return value.hidden

    @staticmethod
    def neighbor(value):
        return value.neighbor

TYPE_PARENTS = {
    "OwnedHandler": ["Handler"],
    "LoopbackOnce": ["OwnedHandler", "Handler"],
}

BINDING_API = {
    "fixture_api.Topology.two_room": ["static", "public", "Topology", [["open_room", "str"], ["sealed_room", "str"]], "Topology"],
    "fixture_api.Impulse.at_face": ["static", "public", "Impulse", [["face", "int"], ["amount", "int"]], "Impulse"],
    "fixture_api.SourceInput.at_face": ["static", "public", "SourceInput", [["face", "int"], ["amount", "int"], ["neighbor", "int"]], "SourceInput"],
    "fixture_api.Core.existing": ["class", "public", "Core", [["topology", "Topology"]], "Core"],
    "fixture_api.Core.new_operation_id": ["instance", "public", "Core", [], "OperationId"],
    "fixture_api.Core.step": ["instance", "public", "Core", [["operation_id", "OperationId"], ["impulse", "Impulse"], ["handler", "Handler"], ["fault", "Fault"]], "CellResult"],
    "fixture_api.Core.step_source": ["instance", "public", "Core", [["source", "SourceInput"]], "CellResult"],
    "fixture_api.Audit.for_core": ["static", "test-harness", "Audit", [["core", "Core"]], "AuditHandle"],
    "fixture_api.AuditHandle.read": ["instance", "test-harness", "AuditHandle", [], "CellResult"],
    "fixture_api.FaultSelector.select": ["static", "internal-test-seam", "FaultSelector", [["operation_id", "OperationId"], ["phase", "str"]], "Fault"],
    "fixture_api.OwnedHandler": ["constructor", "public", "OwnedHandler", [["owner", "Core"]], "OwnedHandler"],
    "fixture_api.OwnedHandler.owner_ref": ["instance", "test-harness", "OwnedHandler", [], "Core"],
    "fixture_api.OwnedHandler.call_count": ["instance", "test-harness", "OwnedHandler", [], "int"],
    "fixture_api.LoopbackOnce": ["constructor", "test-harness", "LoopbackOnce", [["owner", "Core"]], "LoopbackOnce"],
    "fixture_api.LoopbackOnce.delegation_count": ["instance", "test-harness", "LoopbackOnce", [], "int"],
    "fixture_api.Codec.decode_cell_result": ["static", "test-harness", "Codec", [["raw", "bytes"]], "CellResult"],
    "fixture_api.Observe.cell": ["static", "test-harness", "Observe", [["value", "CellResult"]], "int"],
    "fixture_api.Observe.counter": ["static", "test-harness", "Observe", [["value", "CellResult"]], "int"],
    "fixture_api.Observe.hidden": ["static", "test-harness", "Observe", [["value", "CellResult"]], "int"],
    "fixture_api.Observe.neighbor": ["static", "test-harness", "Observe", [["value", "CellResult"]], "int"],
}
'''


GOLDEN_CELL = b'{"cell":3,"counter":4,"hidden":5,"neighbor":0}\n'
GOLDEN_SOURCE = b'{"cell":3,"counter":3,"hidden":5,"neighbor":0}\n'


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def regular_file(path: Path) -> bool:
    try:
        return path.is_file() and not path.is_symlink() and stat.S_ISREG(path.stat().st_mode)
    except OSError:
        return False


def logical_mode(_: Path) -> str:
    return "100644"


def tree_manifest(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix().lower()):
        if path.is_dir():
            continue
        if not regular_file(path):
            rows.append({"path": path.relative_to(root).as_posix(), "invalid": "non-regular"})
            continue
        rows.append(
            {
                "path": path.relative_to(root).as_posix(),
                "mode": logical_mode(path),
                "size": path.stat().st_size,
                "sha256": file_sha256(path),
            }
        )
    return rows


def tree_hash(root: Path) -> str:
    return sha256_bytes(canonical_bytes(tree_manifest(root)))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical_bytes(value))


def add_literal(nodes: list[dict[str, Any]], node_id: str, role: str, value_type: str, value: Any) -> None:
    nodes.append({"id": node_id, "kind": "typed-literal", "role": role, "value_type": value_type, "value": value})


def add_value(
    nodes: list[dict[str, Any]],
    node_id: str,
    kind: str,
    role: str,
    value_type: str,
    producer: str,
    lifetime: str = "obligation",
    owner_ref: str | None = None,
) -> None:
    nodes.append(
        {
            "id": node_id,
            "kind": kind,
            "role": role,
            "value_type": value_type,
            "producer": producer,
            "lifetime": lifetime,
            "owner_ref": owner_ref,
        }
    )


def arg(name: str, value_type: str, source: str) -> dict[str, str]:
    return {"name": name, "type": value_type, "source": source}


def add_call(
    nodes: list[dict[str, Any]],
    node_id: str,
    role: str,
    signature: str,
    style: str,
    visibility: str,
    owner_type: str,
    args: list[dict[str, str]],
    return_type: str,
    output: str | None,
    owner_source: str | None = None,
    expected_exception: str | None = None,
) -> None:
    nodes.append(
        {
            "id": node_id,
            "kind": "callable",
            "role": role,
            "signature": signature,
            "style": style,
            "visibility": visibility,
            "owner_type": owner_type,
            "owner_source": owner_source,
            "args": args,
            "return_type": return_type,
            "output": output,
            "expected_exception": expected_exception,
        }
    )


def add_control(
    nodes: list[dict[str, Any]],
    node_id: str,
    role: str,
    operation_source: str,
    phase_source: str,
    output: str,
) -> None:
    nodes.append(
        {
            "id": node_id,
            "kind": "negative-control",
            "role": role,
            "signature": "fixture_api.FaultSelector.select",
            "style": "static",
            "visibility": "internal-test-seam",
            "owner_type": "FaultSelector",
            "owner_source": None,
            "args": [arg("operation_id", "OperationId", operation_source), arg("phase", "str", phase_source)],
            "return_type": "Fault",
            "output": output,
            "operation_source": operation_source,
            "phase_source": phase_source,
        }
    )


def add_observers(
    nodes: list[dict[str, Any]],
    recipe: list[str],
    prefix: str,
    source: str,
) -> list[str]:
    result: list[str] = []
    for field in OBSERVED_FIELDS:
        call_id = f"call:{prefix}-{field}"
        slot_id = f"slot:{prefix}-{field}"
        add_call(
            nodes,
            call_id,
            f"{prefix}-{field}",
            f"fixture_api.Observe.{field}",
            "static",
            "test-harness",
            "Observe",
            [arg("value", "CellResult", source)],
            "int",
            slot_id,
        )
        add_value(nodes, slot_id, "slot", f"{prefix}-{field}-value", "int", call_id)
        recipe.append(call_id)
        result.append(call_id)
    return result


def base_testability(product_root: Path, acceptance_hash: str) -> dict[str, Any]:
    nodes: list[dict[str, Any]] = []
    fixture_path = product_root / "fixture_api.py"
    nodes.append(
        {
            "id": "source:fixture-api",
            "kind": "source-artifact",
            "role": "fixture-api-source",
            "path": "fixture_api.py",
            "mode": "100644",
            "sha256": file_sha256(fixture_path),
        }
    )
    for node_id, role, value_type, value in [
        ("lit:room-open", "room-open", "str", "open"),
        ("lit:room-sealed", "room-sealed", "str", "sealed"),
        ("lit:face-zero", "face-zero", "int", 0),
        ("lit:amount-one", "amount-one", "int", 1),
        ("lit:neighbor-zero", "neighbor-zero", "int", 0),
        ("lit:phase-none", "phase-none", "str", "none"),
        ("lit:phase-before", "phase-before", "str", "before"),
        ("lit:phase-during", "phase-during", "str", "during"),
        ("lit:phase-after", "phase-after", "str", "after"),
    ]:
        add_literal(nodes, node_id, role, value_type, value)

    recipes: dict[str, list[str]] = {"OB-1": [], "OB-2": [], "OB-3": []}
    routes: dict[str, dict[str, list[str]]] = {
        item: {name: [] for name in ("construct", "act", "observe", "negative", "source", "skeleton")}
        for item in recipes
    }

    # OB-1: all existing harness routes are materialized before the planned
    # public Core.create member reaches its exact missing-member boundary.
    r1 = recipes["OB-1"]
    add_call(
        nodes, "call:ob1-topology", "ob1-topology", "fixture_api.Topology.two_room", "static", "public",
        "Topology", [arg("open_room", "str", "lit:room-open"), arg("sealed_room", "str", "lit:room-sealed")],
        "Topology", "inst:ob1-topology",
    )
    add_value(nodes, "inst:ob1-topology", "instance", "ob1-topology-value", "Topology", "call:ob1-topology")
    r1.append("call:ob1-topology")
    add_call(
        nodes, "call:ob1-core-existing", "ob1-existing-core", "fixture_api.Core.existing", "class", "public",
        "Core", [arg("topology", "Topology", "inst:ob1-topology")], "Core", "inst:ob1-core",
    )
    add_value(nodes, "inst:ob1-core", "instance", "ob1-core-value", "Core", "call:ob1-core-existing", "object")
    r1.append("call:ob1-core-existing")
    add_call(
        nodes, "call:ob1-impulse", "ob1-face-impulse", "fixture_api.Impulse.at_face", "static", "public",
        "Impulse", [arg("face", "int", "lit:face-zero"), arg("amount", "int", "lit:amount-one")],
        "Impulse", "inst:ob1-impulse",
    )
    add_value(nodes, "inst:ob1-impulse", "instance", "ob1-impulse-value", "Impulse", "call:ob1-impulse")
    r1.append("call:ob1-impulse")
    add_call(
        nodes, "call:ob1-handler", "ob1-owned-handler", "fixture_api.OwnedHandler", "constructor", "public",
        "OwnedHandler", [arg("owner", "Core", "inst:ob1-core")], "OwnedHandler", "inst:ob1-handler",
    )
    add_value(
        nodes, "inst:ob1-handler", "instance", "ob1-handler-value", "OwnedHandler", "call:ob1-handler",
        "object", "inst:ob1-core",
    )
    r1.append("call:ob1-handler")
    add_call(
        nodes, "call:ob1-operation", "ob1-operation-id", "fixture_api.Core.new_operation_id", "instance", "public",
        "Core", [], "OperationId", "slot:ob1-operation", "inst:ob1-core",
    )
    add_value(
        nodes, "slot:ob1-operation", "slot", "ob1-operation-value", "OperationId", "call:ob1-operation",
        "operation", "inst:ob1-core",
    )
    r1.append("call:ob1-operation")
    add_control(nodes, "control:ob1-fault-none", "ob1-fault-none", "slot:ob1-operation", "lit:phase-none", "slot:ob1-fault")
    add_value(
        nodes, "slot:ob1-fault", "slot", "ob1-fault-value", "Fault", "control:ob1-fault-none",
        "operation", "slot:ob1-operation",
    )
    r1.append("control:ob1-fault-none")
    add_call(
        nodes, "call:ob1-step", "ob1-existing-step", "fixture_api.Core.step", "instance", "public", "Core",
        [
            arg("operation_id", "OperationId", "slot:ob1-operation"),
            arg("impulse", "Impulse", "inst:ob1-impulse"),
            arg("handler", "Handler", "inst:ob1-handler"),
            arg("fault", "Fault", "slot:ob1-fault"),
        ],
        "CellResult", "inst:ob1-step-result", "inst:ob1-core",
    )
    add_value(nodes, "inst:ob1-step-result", "instance", "ob1-step-result-value", "CellResult", "call:ob1-step")
    r1.append("call:ob1-step")
    add_call(
        nodes, "call:ob1-audit-for", "ob1-audit-handle", "fixture_api.Audit.for_core", "static", "test-harness",
        "Audit", [arg("core", "Core", "inst:ob1-core")], "AuditHandle", "inst:ob1-audit",
    )
    add_value(nodes, "inst:ob1-audit", "instance", "ob1-audit-handle-value", "AuditHandle", "call:ob1-audit-for")
    r1.append("call:ob1-audit-for")
    add_call(
        nodes, "call:ob1-audit-read", "ob1-audit-read", "fixture_api.AuditHandle.read", "instance", "test-harness",
        "AuditHandle", [], "CellResult", "inst:ob1-audit-result", "inst:ob1-audit",
    )
    add_value(nodes, "inst:ob1-audit-result", "instance", "ob1-audit-result-value", "CellResult", "call:ob1-audit-read")
    r1.append("call:ob1-audit-read")
    ob1_audit_observers = add_observers(nodes, r1, "ob1-audit", "inst:ob1-audit-result")
    add_call(
        nodes, "call:ob1-owner-read", "ob1-handler-owner-read", "fixture_api.OwnedHandler.owner_ref", "instance",
        "test-harness", "OwnedHandler", [], "Core", "inst:ob1-owner-read", "inst:ob1-handler",
    )
    add_value(nodes, "inst:ob1-owner-read", "instance", "ob1-owner-read-value", "Core", "call:ob1-owner-read")
    r1.append("call:ob1-owner-read")
    add_call(
        nodes, "call:ob1-calls-read", "ob1-handler-calls-read", "fixture_api.OwnedHandler.call_count", "instance",
        "test-harness", "OwnedHandler", [], "int", "slot:ob1-calls", "inst:ob1-handler",
    )
    add_value(nodes, "slot:ob1-calls", "slot", "ob1-calls-value", "int", "call:ob1-calls-read")
    r1.append("call:ob1-calls-read")
    nodes.append(
        {
            "id": "resource:golden-cell", "kind": "runtime-resource", "role": "ob1-golden-resource",
            "path": "resources/golden-cell.json", "mode": "100644", "size": len(GOLDEN_CELL),
            "sha256": sha256_bytes(GOLDEN_CELL), "output": "slot:ob1-golden-raw", "value_type": "bytes",
        }
    )
    add_value(nodes, "slot:ob1-golden-raw", "slot", "ob1-golden-raw", "bytes", "resource:golden-cell")
    r1.append("resource:golden-cell")
    add_call(
        nodes, "call:ob1-codec", "ob1-golden-codec", "fixture_api.Codec.decode_cell_result", "static", "test-harness",
        "Codec", [arg("raw", "bytes", "slot:ob1-golden-raw")], "CellResult", "inst:ob1-golden",
    )
    add_value(nodes, "inst:ob1-golden", "instance", "ob1-golden-value", "CellResult", "call:ob1-codec")
    r1.append("call:ob1-codec")
    ob1_golden_observers = add_observers(nodes, r1, "ob1-golden", "inst:ob1-golden")
    nodes.append(
        {
            "id": "reflect:ob1-create", "kind": "reflection", "role": "ob1-public-create-missing",
            "signature": "fixture_api.Core.create", "style": "class", "visibility": "public", "owner_type": "Core",
            "args": [arg("topology", "Topology", "inst:ob1-topology")], "return_type": "Core",
            "expected_exception": "AttributeError",
        }
    )
    r1.append("reflect:ob1-create")

    routes["OB-1"]["construct"] = [
        "call:ob1-topology", "call:ob1-core-existing", "call:ob1-impulse", "call:ob1-handler",
        "call:ob1-operation", "control:ob1-fault-none",
    ]
    routes["OB-1"]["act"] = ["call:ob1-step", "reflect:ob1-create"]
    routes["OB-1"]["observe"] = [
        "call:ob1-audit-for", "call:ob1-audit-read", *ob1_audit_observers,
        "call:ob1-owner-read", "call:ob1-calls-read", *ob1_golden_observers,
    ]
    routes["OB-1"]["negative"] = ["reflect:ob1-create", "control:ob1-fault-none"]
    routes["OB-1"]["source"] = ["source:fixture-api", "resource:golden-cell", "call:ob1-codec"]
    routes["OB-1"]["skeleton"] = r1.copy()

    # OB-2: each phase gets a separate Core/operation/fault instance.  The PLAN
    # probe observes every audit field but deliberately makes no rollback/equality
    # assertion; those semantics belong to the later independent acceptance RED.
    r2 = recipes["OB-2"]
    add_call(
        nodes, "call:ob2-topology", "ob2-topology", "fixture_api.Topology.two_room", "static", "public",
        "Topology", [arg("open_room", "str", "lit:room-open"), arg("sealed_room", "str", "lit:room-sealed")],
        "Topology", "inst:ob2-topology",
    )
    add_value(nodes, "inst:ob2-topology", "instance", "ob2-topology-value", "Topology", "call:ob2-topology")
    r2.append("call:ob2-topology")
    add_call(
        nodes, "call:ob2-impulse", "ob2-face-impulse", "fixture_api.Impulse.at_face", "static", "public", "Impulse",
        [arg("face", "int", "lit:face-zero"), arg("amount", "int", "lit:amount-one")], "Impulse", "inst:ob2-impulse",
    )
    add_value(nodes, "inst:ob2-impulse", "instance", "ob2-impulse-value", "Impulse", "call:ob2-impulse")
    r2.append("call:ob2-impulse")
    ob2_construct = ["call:ob2-topology", "call:ob2-impulse"]
    ob2_act: list[str] = []
    ob2_observe: list[str] = []
    ob2_negative: list[str] = []
    for phase in FAULT_PHASES:
        core_call = f"call:ob2-{phase}-core"
        core_value = f"inst:ob2-{phase}-core"
        add_call(
            nodes, core_call, f"ob2-{phase}-core", "fixture_api.Core.existing", "class", "public", "Core",
            [arg("topology", "Topology", "inst:ob2-topology")], "Core", core_value,
        )
        add_value(nodes, core_value, "instance", f"ob2-{phase}-core-value", "Core", core_call, "object")
        r2.append(core_call)
        handler_call = f"call:ob2-{phase}-loopback"
        handler_value = f"inst:ob2-{phase}-loopback"
        add_call(
            nodes, handler_call, f"ob2-{phase}-loopback", "fixture_api.LoopbackOnce", "constructor", "test-harness",
            "LoopbackOnce", [arg("owner", "Core", core_value)], "LoopbackOnce", handler_value,
        )
        add_value(nodes, handler_value, "instance", f"ob2-{phase}-loopback-value", "LoopbackOnce", handler_call, "object", core_value)
        r2.append(handler_call)
        op_call = f"call:ob2-{phase}-operation"
        op_value = f"slot:ob2-{phase}-operation"
        add_call(
            nodes, op_call, f"ob2-{phase}-operation", "fixture_api.Core.new_operation_id", "instance", "public", "Core",
            [], "OperationId", op_value, core_value,
        )
        add_value(nodes, op_value, "slot", f"ob2-{phase}-operation-value", "OperationId", op_call, "operation", core_value)
        r2.append(op_call)
        fault_control = f"control:ob2-fault-{phase}"
        fault_value = f"slot:ob2-fault-{phase}"
        add_control(nodes, fault_control, f"ob2-fault-{phase}", op_value, f"lit:phase-{phase}", fault_value)
        add_value(nodes, fault_value, "slot", f"ob2-fault-{phase}-value", "Fault", fault_control, "operation", op_value)
        r2.append(fault_control)
        before_for = f"call:ob2-{phase}-audit-before-for"
        before_handle = f"inst:ob2-{phase}-audit-before-handle"
        add_call(
            nodes, before_for, f"ob2-{phase}-audit-before-handle", "fixture_api.Audit.for_core", "static", "test-harness",
            "Audit", [arg("core", "Core", core_value)], "AuditHandle", before_handle,
        )
        add_value(nodes, before_handle, "instance", f"ob2-{phase}-audit-before-handle-value", "AuditHandle", before_for)
        r2.append(before_for)
        before_read = f"call:ob2-{phase}-audit-before-read"
        before_result = f"inst:ob2-{phase}-audit-before-result"
        add_call(
            nodes, before_read, f"ob2-{phase}-audit-before-read", "fixture_api.AuditHandle.read", "instance", "test-harness",
            "AuditHandle", [], "CellResult", before_result, before_handle,
        )
        add_value(nodes, before_result, "instance", f"ob2-{phase}-audit-before-result-value", "CellResult", before_read)
        r2.append(before_read)
        before_observers = add_observers(nodes, r2, f"ob2-{phase}-before", before_result)
        step_call = f"call:ob2-{phase}-step"
        add_call(
            nodes, step_call, f"ob2-{phase}-step", "fixture_api.Core.step", "instance", "public", "Core",
            [
                arg("operation_id", "OperationId", op_value), arg("impulse", "Impulse", "inst:ob2-impulse"),
                arg("handler", "Handler", handler_value), arg("fault", "Fault", fault_value),
            ],
            "CellResult", None, core_value, "RouteFault",
        )
        r2.append(step_call)
        after_for = f"call:ob2-{phase}-audit-after-for"
        after_handle = f"inst:ob2-{phase}-audit-after-handle"
        add_call(
            nodes, after_for, f"ob2-{phase}-audit-after-handle", "fixture_api.Audit.for_core", "static", "test-harness",
            "Audit", [arg("core", "Core", core_value)], "AuditHandle", after_handle,
        )
        add_value(nodes, after_handle, "instance", f"ob2-{phase}-audit-after-handle-value", "AuditHandle", after_for)
        r2.append(after_for)
        after_read = f"call:ob2-{phase}-audit-after-read"
        after_result = f"inst:ob2-{phase}-audit-after-result"
        add_call(
            nodes, after_read, f"ob2-{phase}-audit-after-read", "fixture_api.AuditHandle.read", "instance", "test-harness",
            "AuditHandle", [], "CellResult", after_result, after_handle,
        )
        add_value(nodes, after_result, "instance", f"ob2-{phase}-audit-after-result-value", "CellResult", after_read)
        r2.append(after_read)
        after_observers = add_observers(nodes, r2, f"ob2-{phase}-after", after_result)
        delegation_call = f"call:ob2-{phase}-delegation-read"
        delegation_slot = f"slot:ob2-{phase}-delegation"
        add_call(
            nodes, delegation_call, f"ob2-{phase}-delegation-read", "fixture_api.LoopbackOnce.delegation_count", "instance",
            "test-harness", "LoopbackOnce", [], "int", delegation_slot, handler_value,
        )
        add_value(nodes, delegation_slot, "slot", f"ob2-{phase}-delegation-value", "int", delegation_call)
        r2.append(delegation_call)
        ob2_construct.extend([core_call, handler_call, op_call, fault_control])
        ob2_act.append(step_call)
        ob2_observe.extend([before_for, before_read, *before_observers, after_for, after_read, *after_observers, delegation_call])
        ob2_negative.append(fault_control)
    routes["OB-2"]["construct"] = ob2_construct
    routes["OB-2"]["act"] = ob2_act
    routes["OB-2"]["observe"] = ob2_observe
    routes["OB-2"]["negative"] = ob2_negative
    routes["OB-2"]["source"] = ["source:fixture-api"]
    routes["OB-2"]["skeleton"] = r2.copy()

    # OB-3: source-isolation input, audit and golden codec are all executable;
    # their behavioral equality remains outside this PLAN gate.
    r3 = recipes["OB-3"]
    add_call(
        nodes, "call:ob3-topology", "ob3-topology", "fixture_api.Topology.two_room", "static", "public", "Topology",
        [arg("open_room", "str", "lit:room-open"), arg("sealed_room", "str", "lit:room-sealed")],
        "Topology", "inst:ob3-topology",
    )
    add_value(nodes, "inst:ob3-topology", "instance", "ob3-topology-value", "Topology", "call:ob3-topology")
    r3.append("call:ob3-topology")
    add_call(
        nodes, "call:ob3-core", "ob3-existing-core", "fixture_api.Core.existing", "class", "public", "Core",
        [arg("topology", "Topology", "inst:ob3-topology")], "Core", "inst:ob3-core",
    )
    add_value(nodes, "inst:ob3-core", "instance", "ob3-core-value", "Core", "call:ob3-core", "object")
    r3.append("call:ob3-core")
    add_call(
        nodes, "call:ob3-source-input", "ob3-source-input", "fixture_api.SourceInput.at_face", "static", "public",
        "SourceInput", [
            arg("face", "int", "lit:face-zero"), arg("amount", "int", "lit:amount-one"),
            arg("neighbor", "int", "lit:neighbor-zero"),
        ], "SourceInput", "inst:ob3-source-input",
    )
    add_value(nodes, "inst:ob3-source-input", "instance", "ob3-source-input-value", "SourceInput", "call:ob3-source-input")
    r3.append("call:ob3-source-input")
    add_call(
        nodes, "call:ob3-step-source", "ob3-step-source", "fixture_api.Core.step_source", "instance", "public", "Core",
        [arg("source", "SourceInput", "inst:ob3-source-input")], "CellResult", "inst:ob3-step-result", "inst:ob3-core",
    )
    add_value(nodes, "inst:ob3-step-result", "instance", "ob3-step-result-value", "CellResult", "call:ob3-step-source")
    r3.append("call:ob3-step-source")
    ob3_step_observers = add_observers(nodes, r3, "ob3-step", "inst:ob3-step-result")
    add_call(
        nodes, "call:ob3-audit-for", "ob3-audit-handle", "fixture_api.Audit.for_core", "static", "test-harness",
        "Audit", [arg("core", "Core", "inst:ob3-core")], "AuditHandle", "inst:ob3-audit",
    )
    add_value(nodes, "inst:ob3-audit", "instance", "ob3-audit-value", "AuditHandle", "call:ob3-audit-for")
    r3.append("call:ob3-audit-for")
    add_call(
        nodes, "call:ob3-audit-read", "ob3-audit-read", "fixture_api.AuditHandle.read", "instance", "test-harness",
        "AuditHandle", [], "CellResult", "inst:ob3-audit-result", "inst:ob3-audit",
    )
    add_value(nodes, "inst:ob3-audit-result", "instance", "ob3-audit-result-value", "CellResult", "call:ob3-audit-read")
    r3.append("call:ob3-audit-read")
    ob3_audit_observers = add_observers(nodes, r3, "ob3-audit", "inst:ob3-audit-result")
    nodes.append(
        {
            "id": "resource:golden-source", "kind": "runtime-resource", "role": "ob3-golden-resource",
            "path": "resources/golden-source.json", "mode": "100644", "size": len(GOLDEN_SOURCE),
            "sha256": sha256_bytes(GOLDEN_SOURCE), "output": "slot:ob3-golden-raw", "value_type": "bytes",
        }
    )
    add_value(nodes, "slot:ob3-golden-raw", "slot", "ob3-golden-raw", "bytes", "resource:golden-source")
    r3.append("resource:golden-source")
    add_call(
        nodes, "call:ob3-codec", "ob3-golden-codec", "fixture_api.Codec.decode_cell_result", "static", "test-harness",
        "Codec", [arg("raw", "bytes", "slot:ob3-golden-raw")], "CellResult", "inst:ob3-golden",
    )
    add_value(nodes, "inst:ob3-golden", "instance", "ob3-golden-value", "CellResult", "call:ob3-codec")
    r3.append("call:ob3-codec")
    ob3_golden_observers = add_observers(nodes, r3, "ob3-golden", "inst:ob3-golden")
    routes["OB-3"]["construct"] = ["call:ob3-topology", "call:ob3-core", "call:ob3-source-input"]
    routes["OB-3"]["act"] = ["call:ob3-step-source"]
    routes["OB-3"]["observe"] = [
        *ob3_step_observers, "call:ob3-audit-for", "call:ob3-audit-read", *ob3_audit_observers,
        *ob3_golden_observers,
    ]
    routes["OB-3"]["negative"] = ["lit:neighbor-zero"]
    routes["OB-3"]["source"] = ["source:fixture-api", "resource:golden-source", "call:ob3-codec"]
    routes["OB-3"]["skeleton"] = r3.copy()

    manifest = tree_manifest(product_root)
    return {
        "schema": 2,
        "change_id": "c-exec-near-gas-core-authority-001-reference",
        "base_tree_sha256": sha256_bytes(canonical_bytes(manifest)),
        "acceptance_sha256": acceptance_hash,
        "toolchain": actual_toolchain(),
        "input_manifest": manifest,
        "coverage": ["OB-1", "OB-2", "OB-3"],
        "nodes": nodes,
        "recipes": recipes,
        "routes": routes,
    }


def trace_descriptor(node: dict[str, Any], by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    kind = node["kind"]
    if kind == "runtime-resource":
        binding = "resource:" + node["path"]
        args: list[str] = []
        owner = None
        outcome = "returned"
    elif kind == "reflection":
        binding = node["signature"]
        args = [by_id[item["source"]]["role"] for item in node["args"]]
        owner = None
        outcome = "missing:AttributeError"
    else:
        binding = node["signature"]
        args = [by_id[item["source"]]["role"] for item in node["args"]]
        owner = by_id[node["owner_source"]]["role"] if node.get("owner_source") else None
        expected = node.get("expected_exception")
        outcome = "exception:" + expected if expected else "returned"
    output_id = node.get("output")
    return {
        "role": node["role"],
        "binding": binding,
        "owner_role": owner,
        "arg_roles": args,
        "output_role": by_id[output_id]["role"] if output_id else None,
        "outcome": outcome,
    }


def frozen_authority(packet: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    by_id = {row["id"]: row for row in packet["nodes"]}
    done_when = {
        "change_id": packet["change_id"],
        "obligations": [
            {"id": "OB-1", "meaning": "public construction plus owned-handler/audit/golden routes"},
            {"id": "OB-2", "meaning": "operation-local fault selector for before/during/after and loopback/audit routes"},
            {"id": "OB-3", "meaning": "source-isolation input plus full audit and golden codec routes"},
        ],
    }
    spec_obligations: list[dict[str, Any]] = []
    for obligation in ("OB-1", "OB-2", "OB-3"):
        spec_obligations.append(
            {
                "id": obligation,
                "route_roles": {
                    category: [by_id[node_id]["role"] for node_id in packet["routes"][obligation][category]]
                    for category in ("construct", "act", "observe", "negative", "source", "skeleton")
                },
                "trace": [trace_descriptor(by_id[node_id], by_id) for node_id in packet["recipes"][obligation]],
            }
        )
    spec = {
        "change_id": packet["change_id"],
        "observed_fields": OBSERVED_FIELDS,
        "fault_phases": FAULT_PHASES,
        "planned_api": {
            "fixture_api.Core.create": {
                "style": "class",
                "visibility": "public",
                "owner_type": "Core",
                "args": [["topology", "Topology"]],
                "return_type": "Core",
                "base_state": "missing",
            }
        },
        "obligations": spec_obligations,
    }
    return done_when, spec


PACKET_KEYS = {
    "schema", "change_id", "base_tree_sha256", "acceptance_sha256", "toolchain", "input_manifest",
    "coverage", "nodes", "recipes", "routes",
}
NODE_KEYS = {
    "typed-literal": {"id", "kind", "role", "value_type", "value"},
    "source-artifact": {"id", "kind", "role", "path", "mode", "sha256"},
    "instance": {"id", "kind", "role", "value_type", "producer", "lifetime", "owner_ref"},
    "slot": {"id", "kind", "role", "value_type", "producer", "lifetime", "owner_ref"},
    "runtime-resource": {"id", "kind", "role", "path", "mode", "size", "sha256", "output", "value_type"},
    "callable": {
        "id", "kind", "role", "signature", "style", "visibility", "owner_type", "owner_source", "args",
        "return_type", "output", "expected_exception",
    },
    "negative-control": {
        "id", "kind", "role", "signature", "style", "visibility", "owner_type", "owner_source", "args",
        "return_type", "output", "operation_source", "phase_source",
    },
    "reflection": {
        "id", "kind", "role", "signature", "style", "visibility", "owner_type", "args", "return_type",
        "expected_exception",
    },
}
ROUTE_CATEGORIES = ("construct", "act", "observe", "negative", "source", "skeleton")


def add_gap(gaps: list[Gap], code: str, path: str, detail: str = "") -> None:
    gaps.append(Gap(code, path, detail))


def normalized_gaps(gaps: list[Gap]) -> list[Gap]:
    return sorted(set(gaps))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def resolved_inside(root: Path, relative: str) -> Path | None:
    try:
        candidate = (root / relative).resolve()
        candidate.relative_to(root.resolve())
        return candidate
    except (OSError, ValueError):
        return None


def derive_authority(done_when: dict[str, Any], spec: dict[str, Any], gaps: list[Gap]) -> tuple[list[str], dict[str, Any]]:
    done_rows = done_when.get("obligations")
    spec_rows = spec.get("obligations")
    done_ids = [row.get("id") for row in done_rows] if isinstance(done_rows, list) else []
    spec_ids = [row.get("id") for row in spec_rows] if isinstance(spec_rows, list) else []
    if done_ids != spec_ids or not done_ids or any(not isinstance(item, str) for item in done_ids):
        add_gap(gaps, "E_AUTHORITY_UNION", "/authority/obligations", "done_when/spec obligation union differs")
    if len(done_ids) != len(set(done_ids)):
        add_gap(gaps, "E_AUTHORITY_DUPLICATE", "/authority/obligations", "duplicate obligation")
    by_id = {row.get("id"): row for row in spec_rows or [] if isinstance(row, dict) and isinstance(row.get("id"), str)}
    return done_ids, by_id


def actual_toolchain() -> dict[str, Any]:
    interpreter = Path(sys.executable).resolve()
    script = Path(__file__).resolve()
    return {
        "interpreter_path": str(interpreter),
        "interpreter_sha256": file_sha256(interpreter),
        "interpreter_version": sys.version.split()[0],
        "flags": ISOLATION_FLAGS,
        "script_path": str(script),
        "script_sha256": file_sha256(script),
        "dependencies": ["stdlib-only", "fixture_api.py@base-manifest"],
        "commands": ["py_compile", "discover", "filter", "union"],
    }


def compare_toolchain(expected: Any, gaps: list[Gap], prefix: str = "/toolchain") -> None:
    actual = actual_toolchain()
    if not isinstance(expected, dict):
        add_gap(gaps, "E_TOOLCHAIN_SCHEMA", "/toolchain", "toolchain must be object")
        return
    codes = {
        "interpreter_path": "E_TOOLCHAIN_INTERPRETER",
        "interpreter_sha256": "E_TOOLCHAIN_INTERPRETER_HASH",
        "interpreter_version": "E_TOOLCHAIN_VERSION",
        "flags": "E_TOOLCHAIN_FLAGS",
        "script_path": "E_TOOLCHAIN_SCRIPT",
        "script_sha256": "E_TOOLCHAIN_SCRIPT_HASH",
        "dependencies": "E_TOOLCHAIN_DEPENDENCIES",
        "commands": "E_TOOLCHAIN_COMMANDS",
    }
    for key, code in codes.items():
        if expected.get(key) != actual[key]:
            add_gap(gaps, code, prefix + "/" + key, "resolved tool identity differs")


def node_references(node: dict[str, Any]) -> list[str]:
    kind = node.get("kind")
    refs: list[str] = []
    if kind in {"instance", "slot"}:
        if isinstance(node.get("producer"), str):
            refs.append(node["producer"])
        if isinstance(node.get("owner_ref"), str):
            refs.append(node["owner_ref"])
    if kind in {"callable", "negative-control", "reflection"}:
        if isinstance(node.get("owner_source"), str):
            refs.append(node["owner_source"])
        for item in node.get("args", []) if isinstance(node.get("args"), list) else []:
            if isinstance(item, dict) and isinstance(item.get("source"), str):
                refs.append(item["source"])
        if isinstance(node.get("output"), str):
            refs.append(node["output"])
    if kind == "negative-control":
        for key in ("operation_source", "phase_source"):
            if isinstance(node.get(key), str):
                refs.append(node[key])
    if kind == "runtime-resource" and isinstance(node.get("output"), str):
        refs.append(node["output"])
    return refs


def dependency_references(node: dict[str, Any]) -> list[str]:
    kind = node.get("kind")
    refs: list[str] = []
    if kind in {"instance", "slot"}:
        refs.append(node.get("producer"))
        if node.get("owner_ref"):
            refs.append(node.get("owner_ref"))
    elif kind in {"callable", "negative-control", "reflection"}:
        if node.get("owner_source"):
            refs.append(node.get("owner_source"))
        refs.extend(item.get("source") for item in node.get("args", []) if isinstance(item, dict))
        if kind == "negative-control":
            refs.extend([node.get("operation_source"), node.get("phase_source")])
    return [item for item in refs if isinstance(item, str)]


def load_product_module(product_root: Path) -> Any:
    module_path = product_root / "fixture_api.py"
    sys.dont_write_bytecode = True
    sys.modules.pop("fixture_api", None)
    spec = importlib.util.spec_from_file_location("fixture_api", module_path)
    if spec is None or spec.loader is None:
        raise HarnessError("cannot load fixture_api")
    module = importlib.util.module_from_spec(spec)
    sys.modules["fixture_api"] = module
    spec.loader.exec_module(module)
    return module


def resolve_symbol(module: Any, signature: str) -> Any:
    parts = signature.split(".")
    if len(parts) < 2 or parts[0] != "fixture_api":
        raise AttributeError(signature)
    value: Any = module
    for part in parts[1:]:
        value = getattr(value, part)
    return value


def catalog_row(module: Any, signature: str) -> dict[str, Any] | None:
    raw = getattr(module, "BINDING_API", {}).get(signature)
    if not isinstance(raw, list) or len(raw) != 5:
        return None
    style, visibility, owner_type, args, return_type = raw
    return {
        "style": style,
        "visibility": visibility,
        "owner_type": owner_type,
        "args": [{"name": item[0], "type": item[1]} for item in args],
        "return_type": return_type,
    }


def inspect_parameter_names(target: Any, style: str) -> list[str]:
    params = list(inspect.signature(target).parameters.values())
    if style == "instance" and params and params[0].name == "self":
        params = params[1:]
    return [item.name for item in params]


def type_assignable(actual: str, expected: str, module: Any) -> bool:
    if actual == expected:
        return True
    parents = getattr(module, "TYPE_PARENTS", {})
    return expected in parents.get(actual, [])


def runtime_type(value: Any, module: Any) -> str:
    if value is None:
        return "None"
    if type(value) is bytes:
        return "bytes"
    if type(value) is str:
        return "str"
    if type(value) is int:
        return "int"
    for name in (
        "Topology", "Impulse", "SourceInput", "OperationId", "Fault", "CellResult", "Core", "AuditHandle",
        "OwnedHandler", "LoopbackOnce",
    ):
        cls = getattr(module, name, None)
        if cls is not None and isinstance(value, cls):
            return value.__class__.__name__
    return value.__class__.__name__


def audit_packet(
    packet: Any,
    product_root: Path,
    authority_union: list[str],
    authority_by_id: dict[str, Any],
    module: Any,
) -> tuple[list[Gap], dict[str, dict[str, Any]]]:
    gaps: list[Gap] = []
    if not isinstance(packet, dict):
        return [Gap("E_PACKET_SCHEMA", "/", "packet must be object")], {}
    for key in sorted(set(packet) - PACKET_KEYS):
        add_gap(gaps, "E_PACKET_UNKNOWN_FIELD", "/" + key, "planner supplied undeclared field")
    for key in sorted(PACKET_KEYS - set(packet)):
        add_gap(gaps, "E_PACKET_SCHEMA", "/" + key, "missing packet field")
    if packet.get("schema") != 2:
        add_gap(gaps, "E_PACKET_SCHEMA", "/schema", "expected schema 2")
    compare_toolchain(packet.get("toolchain"), gaps, "/packet/toolchain")
    if packet.get("coverage") != authority_union:
        add_gap(gaps, "E_COVERAGE", "/coverage", "coverage differs from independent union")
    actual_manifest = tree_manifest(product_root)
    if packet.get("input_manifest") != actual_manifest:
        add_gap(gaps, "E_INPUT_MANIFEST", "/input_manifest", "exact-base manifest differs")
    if packet.get("base_tree_sha256") != sha256_bytes(canonical_bytes(actual_manifest)):
        add_gap(gaps, "E_BASE_IDENTITY", "/base_tree_sha256", "exact-base tree differs")

    rows = packet.get("nodes")
    if not isinstance(rows, list):
        add_gap(gaps, "E_NODE_SCHEMA", "/nodes", "nodes must be list")
        return normalized_gaps(gaps), {}
    by_id: dict[str, dict[str, Any]] = {}
    roles: dict[str, str] = {}
    for index, row in enumerate(rows):
        path = f"/nodes/{index}"
        if not isinstance(row, dict):
            add_gap(gaps, "E_NODE_SCHEMA", path, "node must be object")
            continue
        node_id = row.get("id")
        if not isinstance(node_id, str) or not node_id:
            add_gap(gaps, "E_NODE_ID", path + "/id", "missing node id")
            continue
        if node_id in by_id:
            add_gap(gaps, "E_NODE_DUPLICATE", "/registry/" + node_id, "duplicate node id")
            continue
        by_id[node_id] = row
        role = row.get("role")
        if not isinstance(role, str) or not role:
            add_gap(gaps, "E_ROLE", "/registry/" + node_id + "/role", "missing role")
        elif role in roles:
            add_gap(gaps, "E_ROLE_DUPLICATE", "/roles/" + role, "role used by multiple nodes")
        else:
            roles[role] = node_id
        kind = row.get("kind")
        if kind not in NODE_KEYS:
            add_gap(gaps, "E_KIND", "/registry/" + node_id + "/kind", "unknown or conflated kind")
            continue
        expected_keys = NODE_KEYS[kind]
        if set(row) != expected_keys:
            add_gap(gaps, "E_NODE_SCHEMA", "/registry/" + node_id, "exact kind schema differs")

    # Collapse every dangling use to one canonical row so a complete sweep is
    # readable instead of producing dozens of cascaded follow-on messages.
    missing_refs: set[str] = set()
    recipes = packet.get("recipes") if isinstance(packet.get("recipes"), dict) else {}
    routes = packet.get("routes") if isinstance(packet.get("routes"), dict) else {}
    for row in by_id.values():
        missing_refs.update(item for item in node_references(row) if item not in by_id)
    for obligation in authority_union:
        steps = recipes.get(obligation)
        if isinstance(steps, list):
            missing_refs.update(item for item in steps if item not in by_id)
        route = routes.get(obligation)
        if isinstance(route, dict):
            for values in route.values():
                if isinstance(values, list):
                    missing_refs.update(item for item in values if item not in by_id)
    for missing in sorted(missing_refs):
        add_gap(gaps, "E_NODE_MISSING", "/registry/" + missing, "referenced binding is absent")

    expected_recipe_keys = authority_union
    union_mismatch = list(recipes) != expected_recipe_keys or list(routes) != expected_recipe_keys
    if list(recipes) != expected_recipe_keys:
        add_gap(gaps, "E_RECIPE_UNION", "/recipes", "recipe union/order differs")
    if list(routes) != expected_recipe_keys:
        add_gap(gaps, "E_ROUTE_UNION", "/routes", "route union/order differs")

    # Exact frozen route/trace descriptors are external authority, never a
    # candidate-provided notion of completeness.
    for obligation in authority_union:
        authority = authority_by_id.get(obligation, {})
        steps = recipes.get(obligation)
        route = routes.get(obligation)
        if not isinstance(steps, list):
            add_gap(gaps, "E_RECIPE", f"/recipes/{obligation}", "missing recipe")
            continue
        if not isinstance(route, dict) or set(route) != set(ROUTE_CATEGORIES):
            add_gap(gaps, "E_ROUTE_SCHEMA", f"/routes/{obligation}", "route categories differ")
            continue
        expected_route_roles = authority.get("route_roles", {})
        for category in ROUTE_CATEGORIES:
            actual_roles = [by_id[item]["role"] for item in route.get(category, []) if item in by_id]
            if not missing_refs and actual_roles != expected_route_roles.get(category):
                add_gap(gaps, "E_ROUTE_ROLES", f"/routes/{obligation}/{category}", "semantic binding roles differ")
        executable_kinds = {"callable", "negative-control", "reflection", "runtime-resource"}
        invalid_recipe_kind = False
        descriptors: list[dict[str, Any]] = []
        for item in steps:
            if item not in by_id or any(ref not in by_id for ref in node_references(by_id[item])):
                continue
            if by_id[item].get("kind") not in executable_kinds:
                add_gap(gaps, "E_RECIPE_KIND", f"/recipes/{obligation}/{item}", "recipe step is not executable")
                invalid_recipe_kind = True
                continue
            descriptors.append(trace_descriptor(by_id[item], by_id))
        if not missing_refs and not invalid_recipe_kind and descriptors != authority.get("trace"):
            add_gap(gaps, "E_TRACE_CONTRACT", f"/recipes/{obligation}", "binding edges differ from frozen trace")

    # Per-kind semantics and exact-base API resolution.
    for node_id, row in by_id.items():
        kind = row.get("kind")
        path = "/registry/" + node_id
        if kind == "typed-literal":
            actual = runtime_type(row.get("value"), module)
            if actual != row.get("value_type"):
                add_gap(gaps, "E_LITERAL_TYPE", path + "/value", "literal runtime type differs")
        elif kind in {"source-artifact", "runtime-resource"}:
            relative = row.get("path")
            target = resolved_inside(product_root, relative) if isinstance(relative, str) else None
            if target is None:
                add_gap(gaps, "E_RESOURCE_ESCAPE", path + "/path", "path escapes product root")
            elif not regular_file(target):
                add_gap(gaps, "E_RESOURCE_MISSING", path + "/path", "regular file absent")
            else:
                if row.get("mode") != logical_mode(target):
                    add_gap(gaps, "E_RESOURCE_MODE", path + "/mode", "mode differs")
                if row.get("sha256") != file_sha256(target):
                    add_gap(gaps, "E_RESOURCE_HASH", path + "/sha256", "blob differs")
                if kind == "runtime-resource" and row.get("size") != target.stat().st_size:
                    add_gap(gaps, "E_RESOURCE_SIZE", path + "/size", "size differs")
                if kind == "runtime-resource" and row.get("value_type") != "bytes":
                    add_gap(gaps, "E_RESOURCE_TYPE", path + "/value_type", "resource must produce bytes")
        elif kind in {"callable", "negative-control"}:
            signature = row.get("signature")
            if not isinstance(signature, str) or not signature:
                add_gap(gaps, "E_SIGNATURE", path + "/signature", "empty signature")
                continue
            catalog = catalog_row(module, signature)
            if catalog is None:
                add_gap(gaps, "E_SIGNATURE", path + "/signature", "signature absent from exact-base API")
                continue
            try:
                target = resolve_symbol(module, signature)
                actual_names = inspect_parameter_names(target, catalog["style"])
            except (AttributeError, TypeError, ValueError):
                add_gap(gaps, "E_SIGNATURE", path + "/signature", "callable cannot resolve")
                continue
            if actual_names != [item["name"] for item in catalog["args"]]:
                add_gap(gaps, "E_API_DECLARATION", path + "/signature", "catalog differs from callable signature")
            for key in ("style", "visibility", "owner_type", "return_type"):
                if row.get(key) != catalog[key]:
                    add_gap(gaps, "E_CALLABLE_" + key.upper(), path + "/" + key, "candidate differs from exact API")
            declared_args = [{"name": item.get("name"), "type": item.get("type")} for item in row.get("args", []) if isinstance(item, dict)]
            if declared_args != catalog["args"]:
                add_gap(gaps, "E_CALLABLE_ARGS", path + "/args", "ordered names/types differ from exact API")
            for index, item in enumerate(row.get("args", []) if isinstance(row.get("args"), list) else []):
                source = by_id.get(item.get("source"))
                if source is not None and not type_assignable(source.get("value_type"), item.get("type"), module):
                    add_gap(gaps, "E_ARG_SOURCE_TYPE", f"{path}/args/{index}/source", "source type is not assignable")
            owner_source = row.get("owner_source")
            if catalog["style"] == "instance":
                source = by_id.get(owner_source)
                if source is None or not type_assignable(source.get("value_type"), catalog["owner_type"], module):
                    add_gap(gaps, "E_OWNER", path + "/owner_source", "concrete owner missing or wrong type")
            elif owner_source is not None:
                add_gap(gaps, "E_OWNER", path + "/owner_source", "non-instance callable has owner source")
            output = row.get("output")
            if output is not None:
                target_row = by_id.get(output)
                if target_row is not None and target_row.get("value_type") != row.get("return_type"):
                    add_gap(gaps, "E_RETURN_SLOT_TYPE", path + "/output", "return slot type differs")
            if kind == "negative-control":
                operation_source = row.get("operation_source")
                phase_source = row.get("phase_source")
                control_args = row.get("args") if isinstance(row.get("args"), list) else []
                first_source = control_args[0].get("source") if len(control_args) > 0 and isinstance(control_args[0], dict) else None
                second_source = control_args[1].get("source") if len(control_args) > 1 and isinstance(control_args[1], dict) else None
                if first_source != operation_source or second_source != phase_source:
                    add_gap(gaps, "E_FAULT_CONTROL_ARGS", path, "selector args differ from ownership metadata")
                output_row = by_id.get(row.get("output"))
                if output_row is not None and (
                    output_row.get("lifetime") != "operation" or output_row.get("owner_ref") != operation_source
                ):
                    add_gap(gaps, "E_FAULT_OWNER", path + "/output", "fault slot is not owned by exact operation")
        elif kind == "reflection":
            planned = authority_by_id.get("__planned_api__", {}).get(row.get("signature"))
            if planned is None:
                add_gap(gaps, "E_REFLECTION_SIGNATURE", path + "/signature", "planned API signature absent")
            else:
                candidate_meta = {
                    "style": row.get("style"), "visibility": row.get("visibility"), "owner_type": row.get("owner_type"),
                    "args": [[item.get("name"), item.get("type")] for item in row.get("args", [])],
                    "return_type": row.get("return_type"), "base_state": "missing",
                }
                if candidate_meta != planned:
                    add_gap(gaps, "E_REFLECTION_META", path, "planned missing-member metadata differs")
                try:
                    resolve_symbol(module, row.get("signature"))
                except AttributeError:
                    pass
                else:
                    add_gap(gaps, "E_REFLECTION_PRESENT", path + "/signature", "planned member is not missing at base")
        if kind in {"instance", "slot"}:
            producer = by_id.get(row.get("producer"))
            if producer is not None and producer.get("output") != node_id:
                add_gap(gaps, "E_PRODUCER_LINK", path + "/producer", "producer/output reverse link differs")
            if row.get("lifetime") not in {"obligation", "object", "operation"}:
                add_gap(gaps, "E_LIFETIME", path + "/lifetime", "unknown lifetime")

    # One output target has exactly one producer, and every dependency graph is
    # acyclic.  These checks are independent and accumulate across obligations.
    producers: dict[str, list[str]] = {}
    for node_id, row in by_id.items():
        output = row.get("output")
        if isinstance(output, str):
            producers.setdefault(output, []).append(node_id)
    for output, values in producers.items():
        if len(values) != 1:
            add_gap(gaps, "E_DUPLICATE_PRODUCER", "/registry/" + output, "multiple producers")

    graph = {node_id: [item for item in dependency_references(row) if item in by_id] for node_id, row in by_id.items()}
    state: dict[str, int] = {}
    cycle_nodes: set[str] = set()

    def visit(node_id: str, stack: list[str]) -> None:
        mark = state.get(node_id, 0)
        if mark == 1:
            cycle_nodes.update(stack[stack.index(node_id):] if node_id in stack else [node_id])
            return
        if mark == 2:
            return
        state[node_id] = 1
        for dependency in graph.get(node_id, []):
            visit(dependency, [*stack, dependency])
        state[node_id] = 2

    for node_id in by_id:
        visit(node_id, [node_id])
    for node_id in sorted(cycle_nodes):
        add_gap(gaps, "E_GRAPH_CYCLE", "/registry/" + node_id, "dependency cycle")

    reachable: set[str] = set()

    def reach(node_id: str) -> None:
        if node_id in reachable or node_id not in by_id:
            return
        reachable.add(node_id)
        row = by_id[node_id]
        for dependency in dependency_references(row):
            reach(dependency)
        output = row.get("output")
        if isinstance(output, str):
            reach(output)

    for obligation in authority_union:
        for node_id in recipes.get(obligation, []) if isinstance(recipes.get(obligation), list) else []:
            reach(node_id)
        route = routes.get(obligation, {})
        if isinstance(route, dict):
            for values in route.values():
                for node_id in values if isinstance(values, list) else []:
                    reach(node_id)
    if not missing_refs and not union_mismatch:
        for node_id in sorted(set(by_id) - reachable):
            add_gap(gaps, "E_UNREACHABLE", "/registry/" + node_id, "node is outside every obligation closure")

    # Ordered recipes must materialize every argument/owner before use.
    literal_ids = {node_id for node_id, row in by_id.items() if row.get("kind") == "typed-literal"}
    if not missing_refs and not union_mismatch:
        for obligation in authority_union:
            available = set(literal_ids)
            for index, node_id in enumerate(recipes.get(obligation, []) if isinstance(recipes.get(obligation), list) else []):
                row = by_id.get(node_id)
                if row is None:
                    continue
                for dependency in dependency_references(row):
                    dep_kind = by_id.get(dependency, {}).get("kind")
                    if dep_kind in {"source-artifact"}:
                        continue
                    if dependency not in available and dep_kind not in {"callable", "negative-control", "runtime-resource"}:
                        add_gap(gaps, "E_USE_BEFORE_PRODUCE", f"/recipes/{obligation}/{index}", dependency)
                output = row.get("output")
                if isinstance(output, str):
                    available.add(output)

    return normalized_gaps(gaps), by_id


class ExecutionRejected(RuntimeError):
    def __init__(self, gaps: list[Gap]):
        super().__init__("binding recipe rejected")
        self.gaps = normalized_gaps(gaps)


def call_target(module: Any, node: dict[str, Any], context: dict[str, Any]) -> Any:
    style = node["style"]
    if style == "instance":
        owner = context[node["owner_source"]]
        return getattr(owner, node["signature"].rsplit(".", 1)[1])
    return resolve_symbol(module, node["signature"])


def execute_recipe(packet: dict[str, Any], product_root: Path, obligation: str, token: object) -> CompletionProof:
    module = load_product_module(product_root)
    by_id = {row["id"]: row for row in packet["nodes"]}
    context: dict[str, Any] = {
        node_id: row["value"] for node_id, row in by_id.items() if row.get("kind") == "typed-literal"
    }
    trace: list[dict[str, Any]] = []
    gaps: list[Gap] = []
    for index, node_id in enumerate(packet["recipes"][obligation]):
        node = by_id[node_id]
        path = f"/runtime/{obligation}/{index}:{node_id}"
        kind = node["kind"]
        if kind == "runtime-resource":
            target = resolved_inside(product_root, node["path"])
            if target is None or not regular_file(target):
                add_gap(gaps, "E_RUNTIME_RESOURCE", path, "resource unavailable")
                continue
            raw = target.read_bytes()
            if len(raw) != node["size"] or sha256_bytes(raw) != node["sha256"]:
                add_gap(gaps, "E_RUNTIME_RESOURCE", path, "resource identity changed")
                continue
            context[node["output"]] = raw
            trace.append(trace_descriptor(node, by_id))
            continue

        if kind == "reflection":
            values: list[Any] = []
            for item in node["args"]:
                value = context.get(item["source"])
                actual = runtime_type(value, module)
                if not type_assignable(actual, item["type"], module):
                    add_gap(gaps, "E_RUNTIME_ARG_TYPE", path + "/" + item["name"], actual)
                values.append(value)
            if gaps:
                continue
            try:
                target = resolve_symbol(module, node["signature"])
            except AttributeError:
                trace.append(trace_descriptor(node, by_id))
                continue
            try:
                target(*values)
            except Exception as error:  # a present route is not the planned missing boundary
                add_gap(gaps, "E_REFLECTION_PRESENT", path, error.__class__.__name__)
            else:
                add_gap(gaps, "E_REFLECTION_PRESENT", path, "member unexpectedly returned")
            continue

        if kind not in {"callable", "negative-control"}:
            add_gap(gaps, "E_RUNTIME_KIND", path, "recipe contains non-executable kind")
            continue
        values = []
        local_gap = False
        if node.get("owner_source"):
            owner = context.get(node["owner_source"])
            actual_owner = runtime_type(owner, module)
            if not type_assignable(actual_owner, node["owner_type"], module):
                add_gap(gaps, "E_RUNTIME_OWNER", path + "/owner", actual_owner)
                local_gap = True
        for item in node["args"]:
            value = context.get(item["source"])
            actual = runtime_type(value, module)
            if not type_assignable(actual, item["type"], module):
                add_gap(gaps, "E_RUNTIME_ARG_TYPE", path + "/" + item["name"], actual)
                local_gap = True
            values.append(value)
        if local_gap:
            continue
        try:
            target = call_target(module, node, context)
            result = target(*values)
        except Exception as error:
            expected = node.get("expected_exception")
            if expected and error.__class__.__name__ == expected:
                trace.append(trace_descriptor(node, by_id))
                continue
            # Product-origin text can never impersonate validator completion.
            add_gap(gaps, "E_ROUTE_EXCEPTION", path, error.__class__.__name__ + ":" + str(error))
            continue
        if node.get("expected_exception"):
            add_gap(gaps, "E_EXPECTED_EXCEPTION", path, "route returned instead of materializing control")
            continue
        actual_return = runtime_type(result, module)
        if not type_assignable(actual_return, node["return_type"], module):
            add_gap(gaps, "E_RUNTIME_RETURN_TYPE", path, actual_return)
            continue
        output = node.get("output")
        if output is not None:
            context[output] = result
        trace.append(trace_descriptor(node, by_id))
    if gaps:
        raise ExecutionRejected(gaps)
    return CompletionProof(token, obligation, tuple(trace))


def generated_probe_source(obligations: list[str]) -> str:
    chunks: list[str] = []
    for obligation in obligations:
        safe = obligation.replace("-", "_")
        chunks.append(
            f"def probe_{safe}(execute, token):\n"
            f"    return execute({obligation!r}, token)\n"
        )
    return "\n".join(chunks)


def load_probe_namespace(path: Path) -> dict[str, Any]:
    source = path.read_text(encoding="utf-8")
    code = compile(source, str(path), "exec")
    namespace: dict[str, Any] = {}
    exec(code, namespace)
    return namespace


def criterion_for(obligation: str, trace: list[dict[str, Any]] | tuple[dict[str, Any], ...]) -> str:
    return f"BINDING_REACHED:{obligation}:" + sha256_bytes(canonical_bytes(list(trace)))


def worker_discover(probe_path: Path, fault: str) -> int:
    try:
        namespace = load_probe_namespace(probe_path)
        discovered = sorted(
            name for name, value in namespace.items() if name.startswith("probe_") and inspect.isfunction(value)
        )
        if fault == "discovery-zero":
            discovered = []
        elif fault == "discovery-duplicate" and discovered:
            discovered = [discovered[0], discovered[0], *discovered[1:]]
        print(json.dumps({"status": "DISCOVERED", "ids": discovered}, sort_keys=True))
        return 0
    except Exception as error:
        print(json.dumps({"status": "WORKER_ERROR", "error": error.__class__.__name__ + ":" + str(error)}, sort_keys=True))
        return HARNESS_FATAL


def invoke_probe(
    packet: dict[str, Any], product_root: Path, probe_path: Path, obligation: str
) -> CompletionProof:
    namespace = load_probe_namespace(probe_path)
    function_name = "probe_" + obligation.replace("-", "_")
    function = namespace.get(function_name)
    if not inspect.isfunction(function):
        raise ExecutionRejected([Gap("E_FILTER_DISCOVERY", "/runtime/" + obligation, "probe function missing")])
    token = object()
    proof = function(lambda item, supplied: execute_recipe(packet, product_root, item, supplied), token)
    if not isinstance(proof, CompletionProof) or proof.token is not token or proof.obligation != obligation:
        raise ExecutionRejected([Gap("E_COMPLETION_PROOF", "/runtime/" + obligation, "unforgeable proof missing")])
    return proof


def worker_filter(packet_path: Path, product_root: Path, probe_path: Path, obligation: str, fault: str) -> int:
    try:
        packet = load_json(packet_path)
        if fault == "filter-pass":
            print(json.dumps({"status": "PASS", "obligation": obligation}, sort_keys=True))
            return 0
        proof = invoke_probe(packet, product_root, probe_path, obligation)
        trace = list(proof.trace)
        criterion = criterion_for(obligation, trace)
        if fault == "wrong-sentinel":
            criterion = "WRONG_SENTINEL"
        print(
            json.dumps(
                {
                    "status": "BINDING_SENTINEL", "obligation": obligation, "criterion": criterion,
                    "trace": trace, "trace_sha256": sha256_bytes(canonical_bytes(trace)),
                },
                sort_keys=True,
            )
        )
        return BINDING_SENTINEL_EXIT
    except ExecutionRejected as error:
        print(json.dumps({"status": "PLAN_RED", "gaps": [item.row() for item in error.gaps]}, sort_keys=True))
        return VALIDATOR_RED
    except Exception as error:
        print(json.dumps({"status": "WORKER_ERROR", "error": error.__class__.__name__ + ":" + str(error)}, sort_keys=True))
        return HARNESS_FATAL


def worker_union(packet_path: Path, product_root: Path, probe_path: Path, obligations: list[str], fault: str) -> int:
    try:
        packet = load_json(packet_path)
        selected = obligations[:-1] if fault == "union-incomplete" else obligations
        rows: list[dict[str, Any]] = []
        gaps: list[Gap] = []
        for obligation in selected:
            try:
                proof = invoke_probe(packet, product_root, probe_path, obligation)
                trace = list(proof.trace)
                rows.append(
                    {
                        "obligation": obligation,
                        "criterion": criterion_for(obligation, trace),
                        "trace": trace,
                        "trace_sha256": sha256_bytes(canonical_bytes(trace)),
                    }
                )
            except ExecutionRejected as error:
                gaps.extend(error.gaps)
        if gaps:
            print(json.dumps({"status": "PLAN_RED", "gaps": [item.row() for item in normalized_gaps(gaps)]}, sort_keys=True))
            return VALIDATOR_RED
        print(json.dumps({"status": "BINDING_SENTINEL_UNION", "rows": rows}, sort_keys=True))
        return BINDING_SENTINEL_EXIT
    except Exception as error:
        print(json.dumps({"status": "WORKER_ERROR", "error": error.__class__.__name__ + ":" + str(error)}, sort_keys=True))
        return HARNESS_FATAL


def parse_single_json(stdout: str) -> dict[str, Any] | None:
    lines = [line for line in stdout.splitlines() if line.strip()]
    if len(lines) != 1:
        return None
    try:
        value = json.loads(lines[0])
    except json.JSONDecodeError:
        return None
    return value if isinstance(value, dict) else None


def run_command(argv: list[str]) -> tuple[subprocess.CompletedProcess[str], dict[str, Any] | None, dict[str, Any]]:
    process = subprocess.run(argv, text=True, capture_output=True, check=False)
    observation = {
        "argv": argv,
        "exit": process.returncode,
        "stdout_sha256": sha256_bytes(process.stdout.encode("utf-8")),
        "stderr_sha256": sha256_bytes(process.stderr.encode("utf-8")),
    }
    return process, parse_single_json(process.stdout), observation


ENVELOPE_KEYS = {
    "schema", "case", "product_root", "base_tree_sha256", "candidate", "observed_candidate", "planner_session",
    "validator_session", "testability", "candidate_event", "done_when", "spec", "acceptance_sha256", "toolchain",
}


def pinned_file(row: Any, path: str, gaps: list[Gap]) -> Path | None:
    if not isinstance(row, dict) or set(row) != {"path", "sha256"}:
        add_gap(gaps, "E_PIN_SCHEMA", path, "expected path and sha256")
        return None
    candidate = Path(str(row.get("path", "")))
    if not candidate.is_absolute() or not regular_file(candidate):
        add_gap(gaps, "E_PIN_FILE", path + "/path", "pinned regular file absent")
        return None
    if file_sha256(candidate) != row.get("sha256"):
        add_gap(gaps, "E_PIN_HASH", path + "/sha256", "pinned blob differs")
        return None
    return candidate


def validation_output(case: str, gaps: list[Gap], receipt: dict[str, Any] | None) -> int:
    normalized = normalized_gaps(gaps)
    if normalized:
        print(json.dumps({"case": case, "status": "PLAN_RED", "gaps": [item.row() for item in normalized]}, sort_keys=True))
        return VALIDATOR_RED
    if receipt is None:
        raise HarnessError("GREEN validation lacks receipt")
    print(json.dumps({"case": case, "status": "PLAN_GATED_GREEN", "receipt": receipt}, sort_keys=True))
    return 0


def validate_envelope(envelope_path: Path, fault: str) -> int:
    try:
        envelope = load_json(envelope_path)
        if not isinstance(envelope, dict):
            raise HarnessError("envelope must be object")
        case = str(envelope.get("case", "unknown"))
        gaps: list[Gap] = []
        for key in sorted(set(envelope) - ENVELOPE_KEYS):
            add_gap(gaps, "E_ENVELOPE_UNKNOWN_FIELD", "/envelope/" + key, "undeclared writer field")
        for key in sorted(ENVELOPE_KEYS - set(envelope)):
            add_gap(gaps, "E_ENVELOPE_SCHEMA", "/envelope/" + key, "missing envelope field")
        if envelope.get("schema") != 1:
            add_gap(gaps, "E_ENVELOPE_SCHEMA", "/envelope/schema", "expected schema 1")
        compare_toolchain(envelope.get("toolchain"), gaps)

        product_root = Path(str(envelope.get("product_root", "")))
        if not product_root.is_absolute() or not product_root.is_dir():
            add_gap(gaps, "E_PRODUCT_ROOT", "/envelope/product_root", "product root absent")
            return validation_output(case, gaps, None)
        before_manifest = tree_manifest(product_root)
        before_hash = sha256_bytes(canonical_bytes(before_manifest))
        if before_hash != envelope.get("base_tree_sha256"):
            add_gap(gaps, "E_BASE_IDENTITY", "/envelope/base_tree_sha256", "observed base differs")

        packet_path = pinned_file(envelope.get("testability"), "/envelope/testability", gaps)
        event_path = pinned_file(envelope.get("candidate_event"), "/envelope/candidate_event", gaps)
        done_path = pinned_file(envelope.get("done_when"), "/envelope/done_when", gaps)
        spec_path = pinned_file(envelope.get("spec"), "/envelope/spec", gaps)
        if None in {packet_path, event_path, done_path, spec_path}:
            after_manifest = tree_manifest(product_root)
            if after_manifest != before_manifest:
                add_gap(gaps, "E_PRODUCT_WRITE", "/product", "tree changed during validation")
            return validation_output(case, gaps, None)

        packet = load_json(packet_path)
        event = load_json(event_path)
        done_when = load_json(done_path)
        frozen_spec = load_json(spec_path)
        acceptance_hash = sha256_bytes(done_path.read_bytes() + spec_path.read_bytes())
        if acceptance_hash != envelope.get("acceptance_sha256"):
            add_gap(gaps, "E_ACCEPTANCE_PIN", "/envelope/acceptance_sha256", "authority bytes differ")
        if not isinstance(packet, dict) or packet.get("acceptance_sha256") != acceptance_hash:
            add_gap(gaps, "E_ACCEPTANCE_PACKET", "/packet/acceptance_sha256", "candidate authority differs")
        if envelope.get("planner_session") == envelope.get("validator_session"):
            add_gap(gaps, "E_ROLE_INDEPENDENCE", "/envelope/validator_session", "planner self-validated")
        if not isinstance(event, dict) or set(event) != {"candidate", "planner_session", "testability_sha256"}:
            add_gap(gaps, "E_CANDIDATE_EVENT", "/candidate_event", "event schema differs")
        else:
            if event.get("candidate") != envelope.get("candidate") or envelope.get("observed_candidate") != envelope.get("candidate"):
                add_gap(gaps, "E_STALE_CANDIDATE", "/envelope/candidate", "candidate/event/observation differ")
            if event.get("planner_session") != envelope.get("planner_session"):
                add_gap(gaps, "E_CANDIDATE_EVENT", "/candidate_event/planner_session", "planner identity differs")
            if event.get("testability_sha256") != envelope.get("testability", {}).get("sha256"):
                add_gap(gaps, "E_CANDIDATE_EVENT", "/candidate_event/testability_sha256", "candidate packet pin differs")

        authority_union, authority_by_id = derive_authority(done_when, frozen_spec, gaps)
        authority_by_id["__planned_api__"] = frozen_spec.get("planned_api", {})
        try:
            module = load_product_module(product_root)
        except Exception as error:
            add_gap(gaps, "E_PRODUCT_LOAD", "/product/fixture_api.py", error.__class__.__name__ + ":" + str(error))
            module = None
        if module is not None:
            packet_gaps, _ = audit_packet(packet, product_root, authority_union, authority_by_id, module)
            gaps.extend(packet_gaps)

        observations: list[dict[str, Any]] = []
        dynamic_gaps: list[Gap] = []
        generated_hash: str | None = None
        if not normalized_gaps(gaps):
            interpreter = Path(sys.executable).resolve()
            script = Path(__file__).resolve()
            with tempfile.TemporaryDirectory(prefix="v21-validator-") as scratch_raw:
                scratch = Path(scratch_raw)
                compile_root = scratch / "compile"
                compile_root.mkdir()
                fixture_copy = compile_root / "fixture_api.py"
                shutil.copyfile(product_root / "fixture_api.py", fixture_copy)
                probe_path = compile_root / "binding_probes.py"
                source = generated_probe_source(authority_union)
                if fault == "compile-failure":
                    source += "\ndef broken(:\n"
                probe_path.write_text(source, encoding="utf-8", newline="\n")
                generated_hash = file_sha256(probe_path)

                compile_ok = False
                if fault == "skip-compile":
                    add_gap(dynamic_gaps, "E_COMPILE_SKIPPED", "/commands/compile", "compile command absent")
                else:
                    compile_argv = [
                        str(interpreter), *ISOLATION_FLAGS, "-m", "py_compile", str(fixture_copy), str(probe_path),
                    ]
                    process, _, observation = run_command(compile_argv)
                    observation["id"] = "compile"
                    observations.append(observation)
                    if process.returncode != 0:
                        add_gap(dynamic_gaps, "E_COMPILE_EXIT", "/commands/compile", "nonzero compiler exit")
                    else:
                        compile_ok = True

                if compile_ok:
                    if fault == "probe-changed":
                        probe_path.write_text(probe_path.read_text(encoding="utf-8") + "\n", encoding="utf-8", newline="\n")
                    if file_sha256(probe_path) != generated_hash:
                        add_gap(dynamic_gaps, "E_PROBE_CHANGED", "/commands/probe_sha256", "probe changed between stages")

                    discovery_fault = fault if fault in {"discovery-zero", "discovery-duplicate"} else "none"
                    discover_argv = [
                        str(interpreter), *ISOLATION_FLAGS, str(script), "--worker", "discover", str(probe_path),
                        discovery_fault,
                    ]
                    process, payload, observation = run_command(discover_argv)
                    observation["id"] = "discover"
                    observations.append(observation)
                    if process.returncode == HARNESS_FATAL:
                        raise HarnessError("discovery worker fatal: " + process.stderr + process.stdout)
                    expected_ids = ["probe_" + item.replace("-", "_") for item in authority_union]
                    if process.returncode != 0 or payload is None or payload.get("status") != "DISCOVERED":
                        add_gap(dynamic_gaps, "E_DISCOVERY_EXIT", "/commands/discover", "discovery command invalid")
                    elif payload.get("ids") != expected_ids:
                        add_gap(dynamic_gaps, "E_DISCOVERY_SET", "/commands/discover/ids", "zero/duplicate/wrong union")

                    for obligation in authority_union:
                        filter_fault = fault if obligation == authority_union[0] and fault in {"filter-pass", "wrong-sentinel"} else "none"
                        filter_argv = [
                            str(interpreter), *ISOLATION_FLAGS, str(script), "--worker", "filter", str(packet_path),
                            str(product_root), str(probe_path), obligation, filter_fault,
                        ]
                        process, payload, observation = run_command(filter_argv)
                        observation["id"] = "filter:" + obligation
                        observations.append(observation)
                        if process.returncode == HARNESS_FATAL:
                            raise HarnessError("filter worker fatal: " + process.stderr + process.stdout)
                        if process.returncode == VALIDATOR_RED and payload and payload.get("status") == "PLAN_RED":
                            for row in payload.get("gaps", []):
                                dynamic_gaps.append(Gap(row["code"], row["path"], row.get("detail", "")))
                            continue
                        if process.returncode == 0 and payload and payload.get("status") == "PASS":
                            add_gap(dynamic_gaps, "E_FILTER_PASS", f"/commands/filter/{obligation}", "probe passed")
                            continue
                        if process.returncode != BINDING_SENTINEL_EXIT or payload is None:
                            add_gap(dynamic_gaps, "E_FILTER_EXIT", f"/commands/filter/{obligation}", "wrong runner exit")
                            continue
                        expected_trace = authority_by_id[obligation]["trace"]
                        expected_criterion = criterion_for(obligation, expected_trace)
                        if payload.get("status") != "BINDING_SENTINEL" or payload.get("criterion") != expected_criterion:
                            add_gap(dynamic_gaps, "E_FILTER_SENTINEL", f"/commands/filter/{obligation}", "wrong criterion")
                        if payload.get("trace") != expected_trace:
                            add_gap(dynamic_gaps, "E_RUNTIME_TRACE", f"/commands/filter/{obligation}/trace", "materialized trace differs")

                    union_fault = fault if fault == "union-incomplete" else "none"
                    union_argv = [
                        str(interpreter), *ISOLATION_FLAGS, str(script), "--worker", "union", str(packet_path),
                        str(product_root), str(probe_path), json.dumps(authority_union), union_fault,
                    ]
                    process, payload, observation = run_command(union_argv)
                    observation["id"] = "union"
                    observations.append(observation)
                    if process.returncode == HARNESS_FATAL:
                        raise HarnessError("union worker fatal: " + process.stderr + process.stdout)
                    if process.returncode == VALIDATOR_RED and payload and payload.get("status") == "PLAN_RED":
                        for row in payload.get("gaps", []):
                            dynamic_gaps.append(Gap(row["code"], row["path"], row.get("detail", "")))
                    elif process.returncode != BINDING_SENTINEL_EXIT or payload is None:
                        add_gap(dynamic_gaps, "E_UNION_EXIT", "/commands/union", "wrong union runner exit")
                    else:
                        expected_rows = [
                            {
                                "obligation": obligation,
                                "criterion": criterion_for(obligation, authority_by_id[obligation]["trace"]),
                                "trace": authority_by_id[obligation]["trace"],
                                "trace_sha256": sha256_bytes(canonical_bytes(authority_by_id[obligation]["trace"])),
                            }
                            for obligation in authority_union
                        ]
                        if payload.get("status") != "BINDING_SENTINEL_UNION" or payload.get("rows") != expected_rows:
                            add_gap(dynamic_gaps, "E_UNION_SET", "/commands/union/rows", "union is incomplete or differs")

        gaps.extend(dynamic_gaps)
        after_manifest = tree_manifest(product_root)
        if after_manifest != before_manifest:
            add_gap(gaps, "E_PRODUCT_WRITE", "/product", "tree changed during read-only validation")
        if file_sha256(Path(__file__).resolve()) != envelope.get("toolchain", {}).get("script_sha256"):
            add_gap(gaps, "E_TOOLCHAIN_CHANGED", "/toolchain/script_sha256", "checker changed during run")

        receipt = None
        if not normalized_gaps(gaps):
            receipt_preimage = {
                "candidate": envelope["candidate"],
                "base_tree_sha256": before_hash,
                "acceptance_sha256": acceptance_hash,
                "testability_sha256": envelope["testability"]["sha256"],
                "candidate_event_sha256": envelope["candidate_event"]["sha256"],
                "validator_session": envelope["validator_session"],
                "validator_pid": os.getpid(),
                "toolchain": actual_toolchain(),
                "generated_probe_sha256": generated_hash,
                "commands": observations,
                "product_before_sha256": sha256_bytes(canonical_bytes(before_manifest)),
                "product_after_sha256": sha256_bytes(canonical_bytes(after_manifest)),
                "product_writes": [],
            }
            receipt = {**receipt_preimage, "plan_receipt_sha256": sha256_bytes(canonical_bytes(receipt_preimage))}
        return validation_output(case, gaps, receipt)
    except HarnessError as error:
        print(json.dumps({"status": "HARNESS_FATAL", "error": str(error)}, sort_keys=True))
        return HARNESS_FATAL
    except Exception as error:
        print(
            json.dumps(
                {"status": "HARNESS_FATAL", "error": error.__class__.__name__ + ":" + str(error)}, sort_keys=True
            )
        )
        return HARNESS_FATAL


@dataclass
class CaseBundle:
    root: Path
    product_root: Path
    packet: dict[str, Any]
    done_when: dict[str, Any]
    spec: dict[str, Any]
    acceptance_hash: str
    envelope_overrides: dict[str, Any]
    fault: str = "none"


MISSING_CASES = {
    "missing-public-create": "reflect:ob1-create",
    "missing-topology": "call:ob1-topology",
    "missing-face-impulse": "call:ob1-impulse",
    "missing-owned-handler": "call:ob1-handler",
    "missing-audit": "call:ob1-audit-read",
    "missing-loopback": "call:ob2-before-loopback",
    "missing-fault-selector-before": "control:ob2-fault-before",
    "missing-fault-selector-during": "control:ob2-fault-during",
    "missing-fault-selector-after": "control:ob2-fault-after",
    "missing-operation-slot": "slot:ob2-before-operation",
    "missing-golden-resource": "resource:golden-cell",
    "missing-codec": "call:ob1-codec",
    "missing-source-input": "call:ob3-source-input",
    "missing-hidden-observer": "call:ob2-after-after-hidden",
}


CASE_NAMES = [
    "valid",
    *MISSING_CASES,
    "two-independent-gaps",
    "planner-self-validates",
    "stale-candidate",
    "planner-supplied-probe",
    "candidate-self-pin",
    "packet-toolchain-substitution",
    "trusts-candidate-union",
    "kind-conflation",
    "empty-signature",
    "unknown-signature",
    "wrong-visibility",
    "wrong-owner",
    "wrong-arg-name",
    "wrong-arg-type",
    "same-type-source-swap",
    "wrong-return-type",
    "wrong-return-slot-type",
    "resource-path-escape",
    "resource-wrong-hash",
    "resource-wrong-mode",
    "resource-wrong-size",
    "fault-owner-generic",
    "fault-cross-operation",
    "self-cycle",
    "unreachable-node",
    "duplicate-slot-producer",
    "use-before-produce",
    "api-declaration-mismatch",
    "route-copies-sentinel",
    "actual-product-write",
    "wrong-base",
    "wrong-acceptance",
    "wrong-testability-pin",
    "fake-interpreter",
    "wrong-interpreter-hash",
    "wrong-version",
    "wrong-script-path",
    "wrong-script-hash",
    "missing-isolation-flag",
    "unlisted-dependency",
    "compile-skipped",
    "compile-failure",
    "discovery-zero",
    "discovery-duplicate",
    "filter-pass",
    "wrong-sentinel",
    "union-incomplete",
    "probe-changed",
]


# Populated below with exact validator rows.  Keeping it separate from mutate_case
# prevents a broken/nonmaterialized mutation from satisfying its own oracle.
CASE_EXPECTED: dict[str, set[tuple[str, str]]] = {
    "valid": set(),
    "missing-public-create": {("E_NODE_MISSING", "/registry/reflect:ob1-create")},
    "missing-topology": {("E_NODE_MISSING", "/registry/call:ob1-topology")},
    "missing-face-impulse": {("E_NODE_MISSING", "/registry/call:ob1-impulse")},
    "missing-owned-handler": {("E_NODE_MISSING", "/registry/call:ob1-handler")},
    "missing-audit": {("E_NODE_MISSING", "/registry/call:ob1-audit-read")},
    "missing-loopback": {("E_NODE_MISSING", "/registry/call:ob2-before-loopback")},
    "missing-fault-selector-before": {("E_NODE_MISSING", "/registry/control:ob2-fault-before")},
    "missing-fault-selector-during": {("E_NODE_MISSING", "/registry/control:ob2-fault-during")},
    "missing-fault-selector-after": {("E_NODE_MISSING", "/registry/control:ob2-fault-after")},
    "missing-operation-slot": {("E_NODE_MISSING", "/registry/slot:ob2-before-operation")},
    "missing-golden-resource": {("E_NODE_MISSING", "/registry/resource:golden-cell")},
    "missing-codec": {("E_NODE_MISSING", "/registry/call:ob1-codec")},
    "missing-source-input": {("E_NODE_MISSING", "/registry/call:ob3-source-input")},
    "missing-hidden-observer": {("E_NODE_MISSING", "/registry/call:ob2-after-after-hidden")},
    "two-independent-gaps": {
        ("E_NODE_MISSING", "/registry/call:ob1-impulse"),
        ("E_NODE_MISSING", "/registry/call:ob3-source-input"),
    },
    "planner-self-validates": {("E_ROLE_INDEPENDENCE", "/envelope/validator_session")},
    "stale-candidate": {("E_STALE_CANDIDATE", "/envelope/candidate")},
    "planner-supplied-probe": {("E_PACKET_UNKNOWN_FIELD", "/probe_source")},
    "candidate-self-pin": {("E_PACKET_UNKNOWN_FIELD", "/candidate")},
    "packet-toolchain-substitution": {
        ("E_TOOLCHAIN_INTERPRETER", "/packet/toolchain/interpreter_path")
    },
    "trusts-candidate-union": {
        ("E_COVERAGE", "/coverage"),
        ("E_RECIPE", "/recipes/OB-3"),
        ("E_RECIPE_UNION", "/recipes"),
        ("E_ROUTE_UNION", "/routes"),
    },
    "kind-conflation": {
        ("E_KIND", "/registry/call:ob1-handler/kind"),
        ("E_RECIPE_KIND", "/recipes/OB-1/call:ob1-handler"),
    },
    "empty-signature": {
        ("E_SIGNATURE", "/registry/call:ob1-impulse/signature"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
    },
    "unknown-signature": {
        ("E_SIGNATURE", "/registry/call:ob1-impulse/signature"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
    },
    "wrong-visibility": {("E_CALLABLE_VISIBILITY", "/registry/call:ob1-impulse/visibility")},
    "wrong-owner": {
        ("E_OWNER", "/registry/call:ob1-step/owner_source"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
    },
    "wrong-arg-name": {("E_CALLABLE_ARGS", "/registry/call:ob1-impulse/args")},
    "wrong-arg-type": {
        ("E_ARG_SOURCE_TYPE", "/registry/call:ob1-impulse/args/0/source"),
        ("E_CALLABLE_ARGS", "/registry/call:ob1-impulse/args"),
    },
    "same-type-source-swap": {("E_TRACE_CONTRACT", "/recipes/OB-1")},
    "wrong-return-type": {
        ("E_CALLABLE_RETURN_TYPE", "/registry/call:ob1-impulse/return_type"),
        ("E_RETURN_SLOT_TYPE", "/registry/call:ob1-impulse/output"),
    },
    "wrong-return-slot-type": {("E_RETURN_SLOT_TYPE", "/registry/call:ob1-calls-read/output")},
    "resource-path-escape": {
        ("E_RESOURCE_ESCAPE", "/registry/resource:golden-cell/path"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
    },
    "resource-wrong-hash": {("E_RESOURCE_HASH", "/registry/resource:golden-cell/sha256")},
    "resource-wrong-mode": {("E_RESOURCE_MODE", "/registry/resource:golden-cell/mode")},
    "resource-wrong-size": {("E_RESOURCE_SIZE", "/registry/resource:golden-cell/size")},
    "fault-owner-generic": {("E_FAULT_OWNER", "/registry/control:ob2-fault-before/output")},
    "fault-cross-operation": {
        ("E_FAULT_CONTROL_ARGS", "/registry/control:ob2-fault-before"),
        ("E_FAULT_OWNER", "/registry/control:ob2-fault-before/output"),
        ("E_USE_BEFORE_PRODUCE", "/recipes/OB-2/5"),
    },
    "self-cycle": {("E_GRAPH_CYCLE", "/registry/inst:ob1-core")},
    "unreachable-node": {("E_UNREACHABLE", "/registry/lit:unreachable")},
    "duplicate-slot-producer": {
        ("E_DUPLICATE_PRODUCER", "/registry/slot:ob1-calls"),
        ("E_UNREACHABLE", "/registry/call:ob1-calls-read-duplicate"),
    },
    "use-before-produce": {
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
        ("E_USE_BEFORE_PRODUCE", "/recipes/OB-1/0"),
    },
    "api-declaration-mismatch": {("E_API_DECLARATION", "/registry/call:ob1-calls-read/signature")},
    "route-copies-sentinel": {("E_ROUTE_EXCEPTION", "/runtime/OB-1/14:call:ob1-calls-read")},
    "actual-product-write": {("E_PRODUCT_WRITE", "/product")},
    "wrong-base": {("E_BASE_IDENTITY", "/envelope/base_tree_sha256")},
    "wrong-acceptance": {("E_ACCEPTANCE_PIN", "/envelope/acceptance_sha256")},
    "wrong-testability-pin": {("E_PIN_HASH", "/envelope/testability/sha256")},
    "fake-interpreter": {("E_TOOLCHAIN_INTERPRETER", "/toolchain/interpreter_path")},
    "wrong-interpreter-hash": {("E_TOOLCHAIN_INTERPRETER_HASH", "/toolchain/interpreter_sha256")},
    "wrong-version": {("E_TOOLCHAIN_VERSION", "/toolchain/interpreter_version")},
    "wrong-script-path": {("E_TOOLCHAIN_SCRIPT", "/toolchain/script_path")},
    "wrong-script-hash": {
        ("E_TOOLCHAIN_CHANGED", "/toolchain/script_sha256"),
        ("E_TOOLCHAIN_SCRIPT_HASH", "/toolchain/script_sha256"),
    },
    "missing-isolation-flag": {("E_TOOLCHAIN_FLAGS", "/toolchain/flags")},
    "unlisted-dependency": {("E_TOOLCHAIN_DEPENDENCIES", "/toolchain/dependencies")},
    "compile-skipped": {("E_COMPILE_SKIPPED", "/commands/compile")},
    "compile-failure": {("E_COMPILE_EXIT", "/commands/compile")},
    "discovery-zero": {("E_DISCOVERY_SET", "/commands/discover/ids")},
    "discovery-duplicate": {("E_DISCOVERY_SET", "/commands/discover/ids")},
    "filter-pass": {("E_FILTER_PASS", "/commands/filter/OB-1")},
    "wrong-sentinel": {("E_FILTER_SENTINEL", "/commands/filter/OB-1")},
    "union-incomplete": {("E_UNION_SET", "/commands/union/rows")},
    "probe-changed": {("E_PROBE_CHANGED", "/commands/probe_sha256")},
}


def materialize_baseline(root: Path) -> CaseBundle:
    product_root = root / "product"
    (product_root / "resources").mkdir(parents=True)
    (product_root / "fixture_api.py").write_text(FIXTURE_SOURCE, encoding="utf-8", newline="\n")
    (product_root / "resources" / "golden-cell.json").write_bytes(GOLDEN_CELL)
    (product_root / "resources" / "golden-source.json").write_bytes(GOLDEN_SOURCE)
    preliminary = base_testability(product_root, "pending")
    done_when, frozen_spec = frozen_authority(preliminary)
    done_bytes = canonical_bytes(done_when)
    spec_bytes = canonical_bytes(frozen_spec)
    acceptance_hash = sha256_bytes(done_bytes + spec_bytes)
    packet = base_testability(product_root, acceptance_hash)
    return CaseBundle(root, product_root, packet, done_when, frozen_spec, acceptance_hash, {})


def find_node(packet: dict[str, Any], node_id: str) -> dict[str, Any]:
    for row in packet["nodes"]:
        if row.get("id") == node_id:
            return row
    raise HarnessError("mutation target absent: " + node_id)


def remove_node(packet: dict[str, Any], node_id: str) -> None:
    before = len(packet["nodes"])
    packet["nodes"] = [row for row in packet["nodes"] if row.get("id") != node_id]
    if len(packet["nodes"]) != before - 1:
        raise HarnessError("remove mutation did not materialize: " + node_id)


def refresh_product_identities(bundle: CaseBundle) -> None:
    manifest = tree_manifest(bundle.product_root)
    bundle.packet["input_manifest"] = manifest
    bundle.packet["base_tree_sha256"] = sha256_bytes(canonical_bytes(manifest))
    source = find_node(bundle.packet, "source:fixture-api")
    source["sha256"] = file_sha256(bundle.product_root / "fixture_api.py")
    for node_id in ("resource:golden-cell", "resource:golden-source"):
        row = find_node(bundle.packet, node_id)
        target = bundle.product_root / row["path"]
        row["size"] = target.stat().st_size
        row["sha256"] = file_sha256(target)


def replace_fixture(bundle: CaseBundle, old: str, new: str) -> None:
    path = bundle.product_root / "fixture_api.py"
    text = path.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise HarnessError("fixture mutation anchor not unique")
    path.write_text(text.replace(old, new), encoding="utf-8", newline="\n")
    refresh_product_identities(bundle)


def mutate_case(bundle: CaseBundle, case: str) -> None:
    packet = bundle.packet
    if case == "valid":
        return
    if case in MISSING_CASES:
        remove_node(packet, MISSING_CASES[case])
        return
    if case == "two-independent-gaps":
        remove_node(packet, "call:ob1-impulse")
        remove_node(packet, "call:ob3-source-input")
    elif case == "planner-self-validates":
        bundle.envelope_overrides["validator_session"] = "plan-author-001"
    elif case == "stale-candidate":
        bundle.envelope_overrides["candidate"] = "P-stale"
    elif case == "planner-supplied-probe":
        packet["probe_source"] = "def planner_probe(): pass"
    elif case == "candidate-self-pin":
        packet["candidate"] = "P-impossible-self-pin"
    elif case == "packet-toolchain-substitution":
        packet["toolchain"]["interpreter_path"] = "C:/missing/packet-python.exe"
    elif case == "trusts-candidate-union":
        packet["coverage"] = ["OB-1", "OB-2"]
        packet["recipes"].pop("OB-3")
        packet["routes"].pop("OB-3")
    elif case == "kind-conflation":
        find_node(packet, "call:ob1-handler")["kind"] = "conflated-instance-callable"
    elif case == "empty-signature":
        find_node(packet, "call:ob1-impulse")["signature"] = ""
    elif case == "unknown-signature":
        find_node(packet, "call:ob1-impulse")["signature"] = "fixture_api.NoSuch.impulse"
    elif case == "wrong-visibility":
        find_node(packet, "call:ob1-impulse")["visibility"] = "private"
    elif case == "wrong-owner":
        find_node(packet, "call:ob1-step")["owner_source"] = "inst:ob1-impulse"
    elif case == "wrong-arg-name":
        find_node(packet, "call:ob1-impulse")["args"][0]["name"] = "wrong_face"
    elif case == "wrong-arg-type":
        find_node(packet, "call:ob1-impulse")["args"][0]["type"] = "str"
    elif case == "same-type-source-swap":
        find_node(packet, "call:ob1-impulse")["args"][1]["source"] = "lit:neighbor-zero"
    elif case == "wrong-return-type":
        find_node(packet, "call:ob1-impulse")["return_type"] = "int"
    elif case == "wrong-return-slot-type":
        find_node(packet, "slot:ob1-calls")["value_type"] = "str"
    elif case == "resource-path-escape":
        find_node(packet, "resource:golden-cell")["path"] = "../outside.json"
    elif case == "resource-wrong-hash":
        find_node(packet, "resource:golden-cell")["sha256"] = "0" * 64
    elif case == "resource-wrong-mode":
        find_node(packet, "resource:golden-cell")["mode"] = "100755"
    elif case == "resource-wrong-size":
        find_node(packet, "resource:golden-cell")["size"] += 1
    elif case == "fault-owner-generic":
        find_node(packet, "slot:ob2-fault-before")["owner_ref"] = "inst:ob2-before-core"
    elif case == "fault-cross-operation":
        find_node(packet, "control:ob2-fault-before")["operation_source"] = "slot:ob2-during-operation"
    elif case == "self-cycle":
        find_node(packet, "inst:ob1-core")["owner_ref"] = "inst:ob1-core"
    elif case == "unreachable-node":
        add_literal(packet["nodes"], "lit:unreachable", "unreachable", "int", 9)
    elif case == "duplicate-slot-producer":
        original = copy.deepcopy(find_node(packet, "call:ob1-calls-read"))
        original["id"] = "call:ob1-calls-read-duplicate"
        original["role"] = "ob1-handler-calls-read-duplicate"
        packet["nodes"].append(original)
    elif case == "use-before-produce":
        steps = packet["recipes"]["OB-1"]
        steps.remove("call:ob1-handler")
        steps.insert(0, "call:ob1-handler")
    elif case == "api-declaration-mismatch":
        replace_fixture(
            bundle,
            "    def call_count(self):\n        return self.calls",
            "    def call_count(self, extra=None):\n        return self.calls",
        )
    elif case == "route-copies-sentinel":
        replace_fixture(
            bundle,
            "    def call_count(self):\n        return self.calls",
            "    def call_count(self):\n        raise RuntimeError('BINDING_REACHED:copied')",
        )
    elif case == "actual-product-write":
        replace_fixture(
            bundle,
            "    def cell(value):\n        return value.cell",
            "    def cell(value):\n        with open(__file__ + '.forbidden-write', 'w', encoding='utf-8') as stream:\n            stream.write('forbidden')\n        return value.cell",
        )
    elif case == "wrong-base":
        bundle.envelope_overrides["base_tree_sha256"] = "0" * 64
    elif case == "wrong-acceptance":
        bundle.envelope_overrides["acceptance_sha256"] = "0" * 64
    elif case == "wrong-testability-pin":
        bundle.envelope_overrides["testability_sha256"] = "0" * 64
    elif case == "fake-interpreter":
        bundle.envelope_overrides["toolchain.interpreter_path"] = "C:/missing/python.exe"
    elif case == "wrong-interpreter-hash":
        bundle.envelope_overrides["toolchain.interpreter_sha256"] = "0" * 64
    elif case == "wrong-version":
        bundle.envelope_overrides["toolchain.interpreter_version"] = "0.0.0"
    elif case == "wrong-script-path":
        bundle.envelope_overrides["toolchain.script_path"] = "C:/missing/v21_conformance.py"
    elif case == "wrong-script-hash":
        bundle.envelope_overrides["toolchain.script_sha256"] = "0" * 64
    elif case == "missing-isolation-flag":
        bundle.envelope_overrides["toolchain.flags"] = ["-I"]
    elif case == "unlisted-dependency":
        bundle.envelope_overrides["toolchain.dependencies"] = ["stdlib-only", "fixture_api.py@base-manifest", "mystery.dll"]
    elif case == "compile-skipped":
        bundle.fault = "skip-compile"
    elif case == "compile-failure":
        bundle.fault = "compile-failure"
    elif case == "discovery-zero":
        bundle.fault = "discovery-zero"
    elif case == "discovery-duplicate":
        bundle.fault = "discovery-duplicate"
    elif case == "filter-pass":
        bundle.fault = "filter-pass"
    elif case == "wrong-sentinel":
        bundle.fault = "wrong-sentinel"
    elif case == "union-incomplete":
        bundle.fault = "union-incomplete"
    elif case == "probe-changed":
        bundle.fault = "probe-changed"
    else:
        raise HarnessError("unknown case: " + case)


def semantic_fingerprint(bundle: CaseBundle) -> str:
    value = {
        "packet": bundle.packet,
        "done_when": bundle.done_when,
        "spec": bundle.spec,
        "product_manifest": tree_manifest(bundle.product_root),
        "overrides": bundle.envelope_overrides,
        "fault": bundle.fault,
    }
    return sha256_bytes(canonical_bytes(value))


def set_override(envelope: dict[str, Any], key: str, value: Any) -> None:
    if key == "testability_sha256":
        envelope["testability"]["sha256"] = value
    elif key.startswith("toolchain."):
        envelope["toolchain"][key.split(".", 1)[1]] = value
    else:
        envelope[key] = value


def finalize_bundle(bundle: CaseBundle, case: str) -> Path:
    authority_root = bundle.root / "authority"
    candidate_root = bundle.root / "candidate"
    done_path = authority_root / "done_when.json"
    spec_path = authority_root / "spec.json"
    packet_path = candidate_root / "TESTABILITY.json"
    event_path = bundle.root / "writer" / "candidate-event.json"
    envelope_path = bundle.root / "writer" / "binding-validator-call.json"
    write_json(done_path, bundle.done_when)
    write_json(spec_path, bundle.spec)
    write_json(packet_path, bundle.packet)
    event = {
        "candidate": "P-001",
        "planner_session": "plan-author-001",
        "testability_sha256": file_sha256(packet_path),
    }
    write_json(event_path, event)
    envelope = {
        "schema": 1,
        "case": case,
        "product_root": str(bundle.product_root.resolve()),
        "base_tree_sha256": tree_hash(bundle.product_root),
        "candidate": "P-001",
        "observed_candidate": "P-001",
        "planner_session": "plan-author-001",
        "validator_session": "plan-binding-validator-001",
        "testability": {"path": str(packet_path.resolve()), "sha256": file_sha256(packet_path)},
        "candidate_event": {"path": str(event_path.resolve()), "sha256": file_sha256(event_path)},
        "done_when": {"path": str(done_path.resolve()), "sha256": file_sha256(done_path)},
        "spec": {"path": str(spec_path.resolve()), "sha256": file_sha256(spec_path)},
        "acceptance_sha256": sha256_bytes(done_path.read_bytes() + spec_path.read_bytes()),
        "toolchain": actual_toolchain(),
    }
    for key, value in bundle.envelope_overrides.items():
        set_override(envelope, key, value)
    write_json(envelope_path, envelope)
    return envelope_path


def run_case(case: str, enforce: bool = True) -> int:
    if case not in CASE_NAMES:
        print(json.dumps({"status": "HARNESS_FATAL", "error": "unknown case " + case}, sort_keys=True))
        return HARNESS_FATAL
    try:
        with tempfile.TemporaryDirectory(prefix="v21-case-") as root_raw:
            bundle = materialize_baseline(Path(root_raw))
            before = semantic_fingerprint(bundle)
            mutate_case(bundle, case)
            after = semantic_fingerprint(bundle)
            if case == "valid" and before != after:
                raise HarnessError("valid case mutated")
            if case != "valid" and before == after:
                raise HarnessError("negative mutation did not materialize")
            envelope_path = finalize_bundle(bundle, case)
            script = Path(__file__).resolve()
            interpreter = Path(sys.executable).resolve()
            process = subprocess.run(
                [str(interpreter), *ISOLATION_FLAGS, str(script), "--validate", str(envelope_path), bundle.fault],
                text=True,
                capture_output=True,
                check=False,
            )
            payload = parse_single_json(process.stdout)
            if process.returncode == HARNESS_FATAL or payload is None or payload.get("status") == "HARNESS_FATAL":
                raise HarnessError("validator fatal: " + process.stdout + process.stderr)
            actual_rows = {
                (row["code"], row["path"]) for row in payload.get("gaps", [])
                if isinstance(row, dict) and isinstance(row.get("code"), str) and isinstance(row.get("path"), str)
            }
            expected_exit = 0 if case == "valid" else VALIDATOR_RED
            if not enforce:
                print(
                    json.dumps(
                        {
                            "case": case, "validator_exit": process.returncode, "status": payload.get("status"),
                            "rows": sorted([list(item) for item in actual_rows]), "materialized_before": before,
                            "materialized_after": after,
                        },
                        sort_keys=True,
                    )
                )
                return 0
            if case not in CASE_EXPECTED:
                raise HarnessError("case has no independent expected rows: " + case)
            if process.returncode != expected_exit:
                raise HarnessError(f"validator exit {process.returncode}, expected {expected_exit}: {process.stdout}")
            if actual_rows != CASE_EXPECTED[case]:
                raise HarnessError(
                    "wrong rejection rows for " + case + ": actual=" + repr(sorted(actual_rows))
                    + " expected=" + repr(sorted(CASE_EXPECTED[case]))
                )
            expected_status = "PLAN_GATED_GREEN" if case == "valid" else "PLAN_RED"
            if payload.get("status") != expected_status:
                raise HarnessError("wrong validator status for " + case)
            print(
                json.dumps(
                    {
                        "case": case, "status": "CASE_PASS", "validator_status": expected_status,
                        "validator_exit": process.returncode, "materialized_before": before,
                        "materialized_after": after, "rows": sorted([list(item) for item in actual_rows]),
                    },
                    sort_keys=True,
                )
            )
            return 0
    except HarnessError as error:
        print(json.dumps({"case": case, "status": "HARNESS_FATAL", "error": str(error)}, sort_keys=True))
        return HARNESS_FATAL
    except Exception as error:
        print(
            json.dumps(
                {"case": case, "status": "HARNESS_FATAL", "error": error.__class__.__name__ + ":" + str(error)},
                sort_keys=True,
            )
        )
        return HARNESS_FATAL


def run_parent() -> int:
    script = Path(__file__).resolve()
    interpreter = Path(sys.executable).resolve()
    outcomes: list[dict[str, Any]] = []
    for case in CASE_NAMES:
        process = subprocess.run(
            [str(interpreter), *ISOLATION_FLAGS, str(script), "--case", case],
            text=True,
            capture_output=True,
            check=False,
        )
        payload = parse_single_json(process.stdout)
        if process.returncode != 0 or payload is None or payload.get("case") != case or payload.get("status") != "CASE_PASS":
            print(process.stdout, end="")
            print(process.stderr, end="", file=sys.stderr)
            print(
                json.dumps(
                    {"status": "V21_CONFORMANCE_FATAL", "case": case, "exit": process.returncode}, sort_keys=True
                )
            )
            return HARNESS_FATAL
        rows = {
            (item[0], item[1]) for item in payload.get("rows", [])
            if isinstance(item, list) and len(item) == 2 and all(isinstance(part, str) for part in item)
        }
        if rows != CASE_EXPECTED[case]:
            raise HarnessError("parent observed wrong exact rows for " + case)
        if case == "valid" and payload.get("materialized_before") != payload.get("materialized_after"):
            raise HarnessError("parent observed valid mutation")
        if case != "valid" and payload.get("materialized_before") == payload.get("materialized_after"):
            raise HarnessError("parent observed unmaterialized negative")
        outcomes.append(payload)
    result = {
        "status": "V21_CONFORMANCE_GREEN",
        "interpreter_path": str(interpreter),
        "interpreter_sha256": file_sha256(interpreter),
        "interpreter_version": sys.version.split()[0],
        "isolation_flags": ISOLATION_FLAGS,
        "script_sha256": file_sha256(script),
        "positive_cases": 1,
        "negative_cases": len(CASE_NAMES) - 1,
        "case_digest": sha256_bytes(canonical_bytes(outcomes)),
        "contour": ["case-child", "validator-child", "compile-child", "discover-child", "filter-children", "union-child"],
    }
    print(json.dumps(result, sort_keys=True))
    return 0


def main(argv: list[str]) -> int:
    if not argv:
        return run_parent()
    if len(argv) == 2 and argv[0] == "--case":
        return run_case(argv[1], enforce=True)
    if len(argv) == 2 and argv[0] == "--raw-case":
        return run_case(argv[1], enforce=False)
    if len(argv) == 3 and argv[0] == "--validate":
        return validate_envelope(Path(argv[1]), argv[2])
    if len(argv) >= 2 and argv[0] == "--worker":
        mode = argv[1]
        if mode == "discover" and len(argv) == 4:
            return worker_discover(Path(argv[2]), argv[3])
        if mode == "filter" and len(argv) == 7:
            return worker_filter(Path(argv[2]), Path(argv[3]), Path(argv[4]), argv[5], argv[6])
        if mode == "union" and len(argv) == 7:
            obligations = json.loads(argv[5])
            if not isinstance(obligations, list) or any(not isinstance(item, str) for item in obligations):
                raise HarnessError("union obligation list invalid")
            return worker_union(Path(argv[2]), Path(argv[3]), Path(argv[4]), obligations, argv[6])
    print(
        "usage: v21_conformance.py [--case CASE|--raw-case CASE|--validate ENVELOPE FAULT|--worker ...]",
        file=sys.stderr,
    )
    return HARNESS_FATAL


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
