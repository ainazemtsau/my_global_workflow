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

import ast
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
CONTRACT_LOCATOR = "direction-os://live/os/engineering/CONTRACT_VERSION"
PRODUCT_STAMP_PATH = "validation.config"
CONTRACT_RELATIVE_PATH = "os/engineering/CONTRACT_VERSION"
CHECKER_RELATIVE_PATH = "os/engineering/v21_conformance.py"
CANONICAL_AUTHORITY_REF = "refs/heads/main"
ALLOWED_PRODUCT_IMPORTS = {"dataclasses", "json"}
FORBIDDEN_PRODUCT_CALLS = {"__import__", "compile", "eval", "exec", "open"}
FORBIDDEN_PRODUCT_ATTRIBUTES = {"_exit", "_getframe", "modules", "stderr", "stdin", "stdout"}
CONTROLLER_TYPE_PARENTS = {
    "OwnedHandler": {"Handler"},
    "LoopbackOnce": {"OwnedHandler", "Handler"},
}
ACTIVE_AUTHORITY: dict[str, Any] | None = None


def _initial_module_files() -> tuple[str, ...]:
    script = Path(__file__).resolve()
    rows: set[str] = set()
    for module in tuple(sys.modules.values()):
        raw = getattr(module, "__file__", None)
        if not isinstance(raw, str):
            continue
        try:
            path = Path(raw).resolve()
        except OSError:
            continue
        if path != script and path.is_file() and not path.is_symlink():
            rows.add(str(path))
    for path in Path(sys.executable).resolve().parent.glob("python*.dll"):
        if path.is_file() and not path.is_symlink():
            rows.add(str(path.resolve()))
    return tuple(sorted(rows, key=str.lower))


BOOT_MODULE_FILES = _initial_module_files()


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

@dataclass(frozen=True)
class HandlerTypeRef:
    handler_type: type

    @staticmethod
    def owned():
        return HandlerTypeRef(OwnedHandler)

@dataclass(frozen=True)
class CustomKindMap:
    kind: str
    handler_type: HandlerTypeRef

    @staticmethod
    def one(kind, handler_type):
        if type(kind) is not str or not isinstance(handler_type, HandlerTypeRef):
            raise TypeError("custom kind map")
        return CustomKindMap(kind, handler_type)

    def handler_type_ref(self):
        return self.handler_type

    def kind_value(self):
        return self.kind

@dataclass(frozen=True)
class ReactionRuleSet:
    custom: CustomKindMap

    @staticmethod
    def from_custom(custom):
        if not isinstance(custom, CustomKindMap):
            raise TypeError("custom reactions")
        return ReactionRuleSet(custom)

    def custom_map(self):
        return self.custom

@dataclass(frozen=True)
class GasScenario:
    topology: Topology
    reactions: ReactionRuleSet
    source: SourceInput

    @staticmethod
    def compose(topology, reactions, source):
        if not isinstance(topology, Topology):
            raise TypeError("scenario topology")
        if not isinstance(reactions, ReactionRuleSet):
            raise TypeError("scenario reactions")
        if not isinstance(source, SourceInput):
            raise TypeError("scenario source")
        return GasScenario(topology, reactions, source)

    def reaction_rules(self):
        return self.reactions

    def source_ref(self):
        return self.source

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

    def step_reaction(self, operation_id, impulse, handler, reactions, kind, fault):
        if fault.operation_id != operation_id:
            raise ValueError("reaction fault owner")
        if fault.phase == "before":
            raise RouteFault("reaction-before")
        if reactions.custom.kind != kind:
            raise ValueError("reaction kind")
        if reactions.custom.handler_type.handler_type is not type(handler):
            raise ValueError("reaction handler type")
        handler.apply(self, impulse)
        if fault.phase == "during":
            raise RouteFault("reaction-during")
        self.counter += impulse.amount
        if fault.phase == "after":
            raise RouteFault("reaction-after")
        return Audit.for_core(self).read()

    def step_source_controlled(self, operation_id, source, fault):
        if fault.operation_id != operation_id:
            raise ValueError("source fault owner")
        if fault.phase == "before":
            raise RouteFault("source-before")
        self.cell += source.amount
        if fault.phase == "during":
            raise RouteFault("source-during")
        self.neighbor = source.neighbor
        if fault.phase == "after":
            raise RouteFault("source-after")
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

class OperationControl:
    @staticmethod
    def impulse(operation_id, value):
        if not isinstance(operation_id, OperationId) or not isinstance(value, Impulse):
            raise TypeError("operation impulse")
        return value

    @staticmethod
    def handler(operation_id, value):
        if not isinstance(operation_id, OperationId) or not isinstance(value, Handler):
            raise TypeError("operation handler")
        return value

    @staticmethod
    def source(operation_id, value):
        if not isinstance(operation_id, OperationId) or not isinstance(value, SourceInput):
            raise TypeError("operation source")
        return value

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
    def __init__(self, owner, scenario):
        self.owner = owner
        self.calls = 0
        if not isinstance(scenario, GasScenario):
            raise TypeError("loopback scenario")
        self.scenario = scenario
        self.delegations = 0

    def apply(self, core, impulse):
        OwnedHandler.apply(self, core, impulse)
        if self.delegations == 0:
            self.delegations = 1

    def delegation_count(self):
        return self.delegations

    def delegation_scenario(self):
        return self.scenario

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
    "fixture_api.HandlerTypeRef.owned": ["static", "test-harness", "HandlerTypeRef", [], "HandlerTypeRef"],
    "fixture_api.CustomKindMap.one": ["static", "test-harness", "CustomKindMap", [["kind", "str"], ["handler_type", "HandlerTypeRef"]], "CustomKindMap"],
    "fixture_api.CustomKindMap.handler_type_ref": ["instance", "test-harness", "CustomKindMap", [], "HandlerTypeRef"],
    "fixture_api.CustomKindMap.kind_value": ["instance", "test-harness", "CustomKindMap", [], "str"],
    "fixture_api.ReactionRuleSet.from_custom": ["static", "test-harness", "ReactionRuleSet", [["custom", "CustomKindMap"]], "ReactionRuleSet"],
    "fixture_api.ReactionRuleSet.custom_map": ["instance", "test-harness", "ReactionRuleSet", [], "CustomKindMap"],
    "fixture_api.GasScenario.compose": ["static", "test-harness", "GasScenario", [["topology", "Topology"], ["reactions", "ReactionRuleSet"], ["source", "SourceInput"]], "GasScenario"],
    "fixture_api.GasScenario.reaction_rules": ["instance", "test-harness", "GasScenario", [], "ReactionRuleSet"],
    "fixture_api.GasScenario.source_ref": ["instance", "test-harness", "GasScenario", [], "SourceInput"],
    "fixture_api.Core.existing": ["class", "public", "Core", [["topology", "Topology"]], "Core"],
    "fixture_api.Core.new_operation_id": ["instance", "public", "Core", [], "OperationId"],
    "fixture_api.Core.step": ["instance", "public", "Core", [["operation_id", "OperationId"], ["impulse", "Impulse"], ["handler", "Handler"], ["fault", "Fault"]], "CellResult"],
    "fixture_api.Core.step_source": ["instance", "public", "Core", [["source", "SourceInput"]], "CellResult"],
    "fixture_api.Core.step_reaction": ["instance", "public", "Core", [["operation_id", "OperationId"], ["impulse", "Impulse"], ["handler", "Handler"], ["reactions", "ReactionRuleSet"], ["kind", "str"], ["fault", "Fault"]], "CellResult"],
    "fixture_api.Core.step_source_controlled": ["instance", "public", "Core", [["operation_id", "OperationId"], ["source", "SourceInput"], ["fault", "Fault"]], "CellResult"],
    "fixture_api.Audit.for_core": ["static", "test-harness", "Audit", [["core", "Core"]], "AuditHandle"],
    "fixture_api.AuditHandle.read": ["instance", "test-harness", "AuditHandle", [], "CellResult"],
    "fixture_api.FaultSelector.select": ["static", "internal-test-seam", "FaultSelector", [["operation_id", "OperationId"], ["phase", "str"]], "Fault"],
    "fixture_api.OperationControl.impulse": ["static", "internal-test-seam", "OperationControl", [["operation_id", "OperationId"], ["value", "Impulse"]], "Impulse"],
    "fixture_api.OperationControl.handler": ["static", "internal-test-seam", "OperationControl", [["operation_id", "OperationId"], ["value", "Handler"]], "Handler"],
    "fixture_api.OperationControl.source": ["static", "internal-test-seam", "OperationControl", [["operation_id", "OperationId"], ["value", "SourceInput"]], "SourceInput"],
    "fixture_api.OwnedHandler": ["constructor", "public", "OwnedHandler", [["owner", "Core"]], "OwnedHandler"],
    "fixture_api.OwnedHandler.owner_ref": ["instance", "test-harness", "OwnedHandler", [], "Core"],
    "fixture_api.OwnedHandler.call_count": ["instance", "test-harness", "OwnedHandler", [], "int"],
    "fixture_api.LoopbackOnce": ["constructor", "test-harness", "LoopbackOnce", [["owner", "Core"], ["scenario", "GasScenario"]], "LoopbackOnce"],
    "fixture_api.LoopbackOnce.delegation_count": ["instance", "test-harness", "LoopbackOnce", [], "int"],
    "fixture_api.LoopbackOnce.delegation_scenario": ["instance", "test-harness", "LoopbackOnce", [], "GasScenario"],
    "fixture_api.Codec.decode_cell_result": ["static", "test-harness", "Codec", [["raw", "bytes"]], "CellResult"],
    "fixture_api.Observe.cell": ["static", "test-harness", "Observe", [["value", "CellResult"]], "int"],
    "fixture_api.Observe.counter": ["static", "test-harness", "Observe", [["value", "CellResult"]], "int"],
    "fixture_api.Observe.hidden": ["static", "test-harness", "Observe", [["value", "CellResult"]], "int"],
    "fixture_api.Observe.neighbor": ["static", "test-harness", "Observe", [["value", "CellResult"]], "int"],
}
'''

HOSTILE_FIXTURE_SOURCE = FIXTURE_SOURCE.replace(
    "import json\n", "import json\nimport sys\nsys._getframe()\n", 1
)
HIDDEN_IMPORT_FIXTURE_SOURCE = FIXTURE_SOURCE.replace(
    "import json\n", "import json\nimport hidden_helper\n", 1
)
HIDDEN_HELPER_SOURCE = "VALUE = 1\n"
MALFORMED_CATALOG_FIXTURE_SOURCE = FIXTURE_SOURCE.replace(
    '[["open_room", "str"], ["sealed_room", "str"]]', "[1]", 1
)
MALFORMED_PARENTS_FIXTURE_SOURCE = FIXTURE_SOURCE.replace(
    '    "OwnedHandler": ["Handler"],', '    "OwnedHandler": [1],', 1
)
BUILTINS_ESCAPE_FIXTURE_SOURCE = FIXTURE_SOURCE.replace(
    "from dataclasses import dataclass\n",
    'from dataclasses import dataclass\n_B = __builtins__\n_M = _B["__import__"]("__main__")\n'
    '_M.run_command = lambda argv: None\n',
    1,
)


def _approved_product_callees() -> frozenset[str]:
    syntax = ast.parse(FIXTURE_SOURCE)
    return frozenset(ast.unparse(item.func) for item in ast.walk(syntax) if isinstance(item, ast.Call))


APPROVED_PRODUCT_CALLEES = _approved_product_callees()


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


def tree_observation(root: Path) -> list[dict[str, Any]]:
    """Content plus write-sensitive metadata for the read-only product tree."""
    rows: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix().lower()):
        if path.is_dir():
            continue
        if not regular_file(path):
            rows.append({"path": path.relative_to(root).as_posix(), "invalid": "non-regular"})
            continue
        observed = path.stat()
        rows.append(
            {
                "path": path.relative_to(root).as_posix(),
                "mode": logical_mode(path),
                "size": observed.st_size,
                "sha256": file_sha256(path),
                "mtime_ns": observed.st_mtime_ns,
            }
        )
    return rows


def tree_hash(root: Path) -> str:
    return sha256_bytes(canonical_bytes(tree_manifest(root)))


def copy_product_snapshot(source: Path, target: Path, manifest: list[dict[str, Any]]) -> None:
    target.mkdir(parents=True)
    for row in manifest:
        if "invalid" in row:
            raise HarnessError("cannot mirror non-regular product entry")
        source_path = source / row["path"]
        target_path = target / row["path"]
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source_path, target_path)
    if tree_manifest(target) != manifest:
        raise HarnessError("scratch product mirror differs from pinned base")


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
            "subject_sources": [phase_source],
        }
    )


def promote_operation_control(
    nodes: list[dict[str, Any]], node_id: str, operation_source: str, subject_sources: list[str]
) -> None:
    node = next((item for item in reversed(nodes) if item.get("id") == node_id), None)
    if node is None or node.get("kind") != "callable":
        raise HarnessError("operation-control promotion target absent: " + node_id)
    node["kind"] = "negative-control"
    node.pop("expected_exception", None)
    node["operation_source"] = operation_source
    node["subject_sources"] = subject_sources


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
            "module": "fixture_api",
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
        ("lit:custom-kind-a", "custom-kind-a", "str", "custom-a"),
        ("lit:custom-kind-b", "custom-kind-b", "str", "custom-b"),
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
        nodes, "call:ob1-handler-alt", "ob1-owned-handler-alt", "fixture_api.OwnedHandler", "constructor", "public",
        "OwnedHandler", [arg("owner", "Core", "inst:ob1-core")], "OwnedHandler", "inst:ob1-handler-alt",
    )
    add_value(
        nodes, "inst:ob1-handler-alt", "instance", "ob1-handler-alt-value", "OwnedHandler",
        "call:ob1-handler-alt", "object", "inst:ob1-core",
    )
    r1.append("call:ob1-handler-alt")
    add_call(
        nodes, "call:ob1-source-input", "ob1-scenario-source", "fixture_api.SourceInput.at_face", "static", "public",
        "SourceInput", [
            arg("face", "int", "lit:face-zero"), arg("amount", "int", "lit:amount-one"),
            arg("neighbor", "int", "lit:neighbor-zero"),
        ], "SourceInput", "inst:ob1-source-input",
    )
    add_value(
        nodes, "inst:ob1-source-input", "instance", "ob1-scenario-source-value", "SourceInput",
        "call:ob1-source-input",
    )
    r1.append("call:ob1-source-input")
    add_call(
        nodes, "call:ob1-source-input-alt", "ob1-scenario-source-alt", "fixture_api.SourceInput.at_face", "static", "public",
        "SourceInput", [
            arg("face", "int", "lit:face-zero"), arg("amount", "int", "lit:neighbor-zero"),
            arg("neighbor", "int", "lit:neighbor-zero"),
        ], "SourceInput", "inst:ob1-source-input-alt",
    )
    add_value(
        nodes, "inst:ob1-source-input-alt", "instance", "ob1-scenario-source-alt-value", "SourceInput",
        "call:ob1-source-input-alt",
    )
    r1.append("call:ob1-source-input-alt")
    add_call(
        nodes, "call:ob1-handler-type", "ob1-handler-type", "fixture_api.HandlerTypeRef.owned", "static",
        "test-harness", "HandlerTypeRef", [], "HandlerTypeRef",
        "inst:ob1-handler-type",
    )
    add_value(
        nodes, "inst:ob1-handler-type", "instance", "ob1-handler-type-value", "HandlerTypeRef",
        "call:ob1-handler-type",
    )
    r1.append("call:ob1-handler-type")
    add_call(
        nodes, "call:ob1-custom-map", "ob1-custom-kind-map", "fixture_api.CustomKindMap.one", "static",
        "test-harness", "CustomKindMap", [
            arg("kind", "str", "lit:custom-kind-a"),
            arg("handler_type", "HandlerTypeRef", "inst:ob1-handler-type"),
        ], "CustomKindMap", "inst:ob1-custom-map",
    )
    add_value(
        nodes, "inst:ob1-custom-map", "instance", "ob1-custom-kind-map-value", "CustomKindMap",
        "call:ob1-custom-map", "object", "inst:ob1-handler-type",
    )
    r1.append("call:ob1-custom-map")
    add_call(
        nodes, "call:ob1-custom-map-alt", "ob1-custom-kind-map-alt", "fixture_api.CustomKindMap.one", "static",
        "test-harness", "CustomKindMap", [
            arg("kind", "str", "lit:custom-kind-b"),
            arg("handler_type", "HandlerTypeRef", "inst:ob1-handler-type"),
        ], "CustomKindMap", "inst:ob1-custom-map-alt",
    )
    add_value(
        nodes, "inst:ob1-custom-map-alt", "instance", "ob1-custom-kind-map-alt-value", "CustomKindMap",
        "call:ob1-custom-map-alt", "object", "inst:ob1-handler-type",
    )
    r1.append("call:ob1-custom-map-alt")
    add_call(
        nodes, "call:ob1-reaction-rules", "ob1-reaction-rules", "fixture_api.ReactionRuleSet.from_custom", "static",
        "test-harness", "ReactionRuleSet", [arg("custom", "CustomKindMap", "inst:ob1-custom-map")],
        "ReactionRuleSet", "inst:ob1-reaction-rules",
    )
    add_value(
        nodes, "inst:ob1-reaction-rules", "instance", "ob1-reaction-rules-value", "ReactionRuleSet",
        "call:ob1-reaction-rules", "object", "inst:ob1-custom-map",
    )
    r1.append("call:ob1-reaction-rules")
    add_call(
        nodes, "call:ob1-scenario", "ob1-gas-scenario", "fixture_api.GasScenario.compose", "static", "test-harness",
        "GasScenario", [
            arg("topology", "Topology", "inst:ob1-topology"),
            arg("reactions", "ReactionRuleSet", "inst:ob1-reaction-rules"),
            arg("source", "SourceInput", "inst:ob1-source-input"),
        ], "GasScenario", "inst:ob1-scenario",
    )
    add_value(
        nodes, "inst:ob1-scenario", "instance", "ob1-gas-scenario-value", "GasScenario", "call:ob1-scenario",
        "object", "inst:ob1-core",
    )
    r1.append("call:ob1-scenario")
    add_call(
        nodes, "call:ob1-custom-handler-read", "ob1-custom-handler-read", "fixture_api.CustomKindMap.handler_type_ref",
        "instance", "test-harness", "CustomKindMap", [], "HandlerTypeRef", "inst:ob1-custom-handler-read",
        "inst:ob1-custom-map",
    )
    add_value(
        nodes, "inst:ob1-custom-handler-read", "instance", "ob1-custom-handler-read-value", "HandlerTypeRef",
        "call:ob1-custom-handler-read",
    )
    r1.append("call:ob1-custom-handler-read")
    add_call(
        nodes, "call:ob1-custom-kind-read", "ob1-custom-kind-read", "fixture_api.CustomKindMap.kind_value",
        "instance", "test-harness", "CustomKindMap", [], "str", "slot:ob1-custom-kind-read", "inst:ob1-custom-map",
    )
    add_value(
        nodes, "slot:ob1-custom-kind-read", "slot", "ob1-custom-kind-read-value", "str",
        "call:ob1-custom-kind-read",
    )
    r1.append("call:ob1-custom-kind-read")
    add_call(
        nodes, "call:ob1-rules-map-read", "ob1-rules-map-read", "fixture_api.ReactionRuleSet.custom_map",
        "instance", "test-harness", "ReactionRuleSet", [], "CustomKindMap", "inst:ob1-rules-map-read",
        "inst:ob1-reaction-rules",
    )
    add_value(
        nodes, "inst:ob1-rules-map-read", "instance", "ob1-rules-map-read-value", "CustomKindMap",
        "call:ob1-rules-map-read",
    )
    r1.append("call:ob1-rules-map-read")
    add_call(
        nodes, "call:ob1-scenario-rules-read", "ob1-scenario-rules-read", "fixture_api.GasScenario.reaction_rules",
        "instance", "test-harness", "GasScenario", [], "ReactionRuleSet", "inst:ob1-scenario-rules-read",
        "inst:ob1-scenario",
    )
    add_value(
        nodes, "inst:ob1-scenario-rules-read", "instance", "ob1-scenario-rules-read-value", "ReactionRuleSet",
        "call:ob1-scenario-rules-read",
    )
    r1.append("call:ob1-scenario-rules-read")
    add_call(
        nodes, "call:ob1-scenario-source-read", "ob1-scenario-source-read", "fixture_api.GasScenario.source_ref",
        "instance", "test-harness", "GasScenario", [], "SourceInput", "inst:ob1-scenario-source-read",
        "inst:ob1-scenario",
    )
    add_value(
        nodes, "inst:ob1-scenario-source-read", "instance", "ob1-scenario-source-read-value", "SourceInput",
        "call:ob1-scenario-source-read",
    )
    r1.append("call:ob1-scenario-source-read")
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
        "call:ob1-handler-alt", "call:ob1-source-input", "call:ob1-source-input-alt",
        "call:ob1-handler-type", "call:ob1-custom-map", "call:ob1-custom-map-alt",
        "call:ob1-reaction-rules", "call:ob1-scenario",
        "call:ob1-operation", "control:ob1-fault-none",
    ]
    routes["OB-1"]["act"] = ["call:ob1-step", "reflect:ob1-create"]
    routes["OB-1"]["observe"] = [
        "call:ob1-custom-handler-read", "call:ob1-custom-kind-read", "call:ob1-rules-map-read",
        "call:ob1-scenario-rules-read", "call:ob1-scenario-source-read",
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
    add_call(
        nodes, "call:ob2-scenario-source", "ob2-scenario-source", "fixture_api.SourceInput.at_face", "static", "public",
        "SourceInput", [
            arg("face", "int", "lit:face-zero"), arg("amount", "int", "lit:amount-one"),
            arg("neighbor", "int", "lit:neighbor-zero"),
        ], "SourceInput", "inst:ob2-scenario-source",
    )
    add_value(
        nodes, "inst:ob2-scenario-source", "instance", "ob2-scenario-source-value", "SourceInput",
        "call:ob2-scenario-source",
    )
    r2.append("call:ob2-scenario-source")
    add_call(
        nodes, "call:ob2-handler-type", "ob2-handler-type", "fixture_api.HandlerTypeRef.owned", "static", "test-harness",
        "HandlerTypeRef", [], "HandlerTypeRef", "inst:ob2-handler-type",
    )
    add_value(
        nodes, "inst:ob2-handler-type", "instance", "ob2-handler-type-value", "HandlerTypeRef",
        "call:ob2-handler-type",
    )
    r2.append("call:ob2-handler-type")
    add_call(
        nodes, "call:ob2-scenario-map", "ob2-scenario-map", "fixture_api.CustomKindMap.one", "static", "test-harness",
        "CustomKindMap", [
            arg("kind", "str", "lit:custom-kind-a"),
            arg("handler_type", "HandlerTypeRef", "inst:ob2-handler-type"),
        ], "CustomKindMap", "inst:ob2-scenario-map",
    )
    add_value(
        nodes, "inst:ob2-scenario-map", "instance", "ob2-scenario-map-value", "CustomKindMap",
        "call:ob2-scenario-map", "object", "inst:ob2-handler-type",
    )
    r2.append("call:ob2-scenario-map")
    add_call(
        nodes, "call:ob2-scenario-rules", "ob2-scenario-rules", "fixture_api.ReactionRuleSet.from_custom", "static",
        "test-harness", "ReactionRuleSet", [arg("custom", "CustomKindMap", "inst:ob2-scenario-map")],
        "ReactionRuleSet", "inst:ob2-scenario-rules",
    )
    add_value(
        nodes, "inst:ob2-scenario-rules", "instance", "ob2-scenario-rules-value", "ReactionRuleSet",
        "call:ob2-scenario-rules", "object", "inst:ob2-scenario-map",
    )
    r2.append("call:ob2-scenario-rules")
    add_call(
        nodes, "call:ob2-scenario", "ob2-gas-scenario", "fixture_api.GasScenario.compose", "static", "test-harness",
        "GasScenario", [
            arg("topology", "Topology", "inst:ob2-topology"),
            arg("reactions", "ReactionRuleSet", "inst:ob2-scenario-rules"),
            arg("source", "SourceInput", "inst:ob2-scenario-source"),
        ], "GasScenario", "inst:ob2-scenario",
    )
    add_value(
        nodes, "inst:ob2-scenario", "instance", "ob2-gas-scenario-value", "GasScenario", "call:ob2-scenario",
    )
    r2.append("call:ob2-scenario")
    ob2_construct = [
        "call:ob2-topology", "call:ob2-impulse", "call:ob2-scenario-source", "call:ob2-handler-type",
        "call:ob2-scenario-map", "call:ob2-scenario-rules", "call:ob2-scenario",
    ]
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
            "LoopbackOnce", [
                arg("owner", "Core", core_value), arg("scenario", "GasScenario", "inst:ob2-scenario"),
            ], "LoopbackOnce", handler_value,
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
        impulse_control = f"call:ob2-{phase}-impulse-control"
        impulse_slot = f"slot:ob2-{phase}-impulse-control"
        add_call(
            nodes, impulse_control, f"ob2-{phase}-impulse-control", "fixture_api.OperationControl.impulse", "static",
            "internal-test-seam", "OperationControl", [
                arg("operation_id", "OperationId", op_value), arg("value", "Impulse", "inst:ob2-impulse"),
            ], "Impulse", impulse_slot,
        )
        promote_operation_control(nodes, impulse_control, op_value, ["inst:ob2-impulse"])
        add_value(
            nodes, impulse_slot, "slot", f"ob2-{phase}-impulse-control-value", "Impulse", impulse_control,
            "operation", op_value,
        )
        r2.append(impulse_control)
        handler_control = f"call:ob2-{phase}-handler-control"
        handler_slot = f"slot:ob2-{phase}-handler-control"
        add_call(
            nodes, handler_control, f"ob2-{phase}-handler-control", "fixture_api.OperationControl.handler", "static",
            "internal-test-seam", "OperationControl", [
                arg("operation_id", "OperationId", op_value), arg("value", "Handler", handler_value),
            ], "Handler", handler_slot,
        )
        promote_operation_control(nodes, handler_control, op_value, [handler_value])
        add_value(
            nodes, handler_slot, "slot", f"ob2-{phase}-handler-control-value", "Handler", handler_control,
            "operation", op_value,
        )
        r2.append(handler_control)
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
                arg("operation_id", "OperationId", op_value), arg("impulse", "Impulse", impulse_slot),
                arg("handler", "Handler", handler_slot), arg("fault", "Fault", fault_value),
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
        ob2_construct.extend([core_call, handler_call, op_call, fault_control, impulse_control, handler_control])
        ob2_act.append(step_call)
        ob2_observe.extend([before_for, before_read, *before_observers, after_for, after_read, *after_observers, delegation_call])
        ob2_negative.extend([fault_control, impulse_control, handler_control])

    # A successful loopback route is separate from the three throwing fault
    # routes so its returned CellResult and ownership/delegation surfaces are
    # constructible rather than inferred from an exception path.
    add_call(
        nodes, "call:ob2-success-core", "ob2-success-core", "fixture_api.Core.existing", "class", "public", "Core",
        [arg("topology", "Topology", "inst:ob2-topology")], "Core", "inst:ob2-success-core",
    )
    add_value(nodes, "inst:ob2-success-core", "instance", "ob2-success-core-value", "Core", "call:ob2-success-core", "object")
    r2.append("call:ob2-success-core")
    add_call(
        nodes, "call:ob2-success-loopback", "ob2-success-loopback", "fixture_api.LoopbackOnce", "constructor",
        "test-harness", "LoopbackOnce", [
            arg("owner", "Core", "inst:ob2-success-core"), arg("scenario", "GasScenario", "inst:ob2-scenario"),
        ], "LoopbackOnce",
        "inst:ob2-success-loopback",
    )
    add_value(
        nodes, "inst:ob2-success-loopback", "instance", "ob2-success-loopback-value", "LoopbackOnce",
        "call:ob2-success-loopback", "object", "inst:ob2-success-core",
    )
    r2.append("call:ob2-success-loopback")
    add_call(
        nodes, "call:ob2-success-operation", "ob2-success-operation", "fixture_api.Core.new_operation_id", "instance",
        "public", "Core", [], "OperationId", "slot:ob2-success-operation", "inst:ob2-success-core",
    )
    add_value(
        nodes, "slot:ob2-success-operation", "slot", "ob2-success-operation-value", "OperationId",
        "call:ob2-success-operation", "operation", "inst:ob2-success-core",
    )
    r2.append("call:ob2-success-operation")
    add_control(
        nodes, "control:ob2-success-fault-none", "ob2-success-fault-none", "slot:ob2-success-operation",
        "lit:phase-none", "slot:ob2-success-fault",
    )
    add_value(
        nodes, "slot:ob2-success-fault", "slot", "ob2-success-fault-value", "Fault",
        "control:ob2-success-fault-none", "operation", "slot:ob2-success-operation",
    )
    r2.append("control:ob2-success-fault-none")
    add_call(
        nodes, "call:ob2-success-impulse-control", "ob2-success-impulse-control",
        "fixture_api.OperationControl.impulse", "static", "internal-test-seam", "OperationControl", [
            arg("operation_id", "OperationId", "slot:ob2-success-operation"),
            arg("value", "Impulse", "inst:ob2-impulse"),
        ], "Impulse", "slot:ob2-success-impulse-control",
    )
    promote_operation_control(
        nodes, "call:ob2-success-impulse-control", "slot:ob2-success-operation", ["inst:ob2-impulse"]
    )
    add_value(
        nodes, "slot:ob2-success-impulse-control", "slot", "ob2-success-impulse-control-value", "Impulse",
        "call:ob2-success-impulse-control", "operation", "slot:ob2-success-operation",
    )
    r2.append("call:ob2-success-impulse-control")
    add_call(
        nodes, "call:ob2-success-handler-control", "ob2-success-handler-control",
        "fixture_api.OperationControl.handler", "static", "internal-test-seam", "OperationControl", [
            arg("operation_id", "OperationId", "slot:ob2-success-operation"),
            arg("value", "Handler", "inst:ob2-success-loopback"),
        ], "Handler", "slot:ob2-success-handler-control",
    )
    promote_operation_control(
        nodes, "call:ob2-success-handler-control", "slot:ob2-success-operation", ["inst:ob2-success-loopback"]
    )
    add_value(
        nodes, "slot:ob2-success-handler-control", "slot", "ob2-success-handler-control-value", "Handler",
        "call:ob2-success-handler-control", "operation", "slot:ob2-success-operation",
    )
    r2.append("call:ob2-success-handler-control")
    add_call(
        nodes, "call:ob2-success-step", "ob2-success-step", "fixture_api.Core.step", "instance", "public", "Core",
        [
            arg("operation_id", "OperationId", "slot:ob2-success-operation"),
            arg("impulse", "Impulse", "slot:ob2-success-impulse-control"),
            arg("handler", "Handler", "slot:ob2-success-handler-control"),
            arg("fault", "Fault", "slot:ob2-success-fault"),
        ], "CellResult", "inst:ob2-success-result", "inst:ob2-success-core",
    )
    add_value(
        nodes, "inst:ob2-success-result", "instance", "ob2-success-result-value", "CellResult",
        "call:ob2-success-step",
    )
    r2.append("call:ob2-success-step")
    success_observers = add_observers(nodes, r2, "ob2-success-return", "inst:ob2-success-result")
    add_call(
        nodes, "call:ob2-success-owner-read", "ob2-success-owner-read", "fixture_api.OwnedHandler.owner_ref",
        "instance", "test-harness", "OwnedHandler", [], "Core", "inst:ob2-success-owner-read",
        "inst:ob2-success-loopback",
    )
    add_value(
        nodes, "inst:ob2-success-owner-read", "instance", "ob2-success-owner-read-value", "Core",
        "call:ob2-success-owner-read",
    )
    r2.append("call:ob2-success-owner-read")
    add_call(
        nodes, "call:ob2-success-calls-read", "ob2-success-calls-read", "fixture_api.OwnedHandler.call_count",
        "instance", "test-harness", "OwnedHandler", [], "int", "slot:ob2-success-calls",
        "inst:ob2-success-loopback",
    )
    add_value(nodes, "slot:ob2-success-calls", "slot", "ob2-success-calls-value", "int", "call:ob2-success-calls-read")
    r2.append("call:ob2-success-calls-read")
    add_call(
        nodes, "call:ob2-success-delegation-read", "ob2-success-delegation-read",
        "fixture_api.LoopbackOnce.delegation_count", "instance", "test-harness", "LoopbackOnce", [], "int",
        "slot:ob2-success-delegation", "inst:ob2-success-loopback",
    )
    add_value(
        nodes, "slot:ob2-success-delegation", "slot", "ob2-success-delegation-value", "int",
        "call:ob2-success-delegation-read",
    )
    r2.append("call:ob2-success-delegation-read")
    add_call(
        nodes, "call:ob2-success-scenario-read", "ob2-success-scenario-read",
        "fixture_api.LoopbackOnce.delegation_scenario", "instance", "test-harness", "LoopbackOnce", [],
        "GasScenario", "inst:ob2-success-scenario-read", "inst:ob2-success-loopback",
    )
    add_value(
        nodes, "inst:ob2-success-scenario-read", "instance", "ob2-success-scenario-read-value", "GasScenario",
        "call:ob2-success-scenario-read",
    )
    r2.append("call:ob2-success-scenario-read")
    ob2_construct.extend([
        "call:ob2-success-core", "call:ob2-success-loopback", "call:ob2-success-operation",
        "control:ob2-success-fault-none", "call:ob2-success-impulse-control", "call:ob2-success-handler-control",
    ])
    ob2_act.append("call:ob2-success-step")
    ob2_observe.extend([
        *success_observers, "call:ob2-success-owner-read", "call:ob2-success-calls-read",
        "call:ob2-success-delegation-read", "call:ob2-success-scenario-read",
    ])
    ob2_negative.extend([
        "control:ob2-success-fault-none", "call:ob2-success-impulse-control", "call:ob2-success-handler-control",
    ])

    # A second, heterogeneous operation-local control reaches the custom
    # reaction handler route instead of the direct impulse route above.
    add_call(
        nodes, "call:ob2-reaction-core", "ob2-reaction-core", "fixture_api.Core.existing", "class", "public", "Core",
        [arg("topology", "Topology", "inst:ob2-topology")], "Core", "inst:ob2-reaction-core",
    )
    add_value(nodes, "inst:ob2-reaction-core", "instance", "ob2-reaction-core-value", "Core", "call:ob2-reaction-core", "object")
    r2.append("call:ob2-reaction-core")
    add_call(
        nodes, "call:ob2-reaction-handler", "ob2-reaction-handler", "fixture_api.OwnedHandler", "constructor", "public",
        "OwnedHandler", [arg("owner", "Core", "inst:ob2-reaction-core")], "OwnedHandler",
        "inst:ob2-reaction-handler",
    )
    add_value(
        nodes, "inst:ob2-reaction-handler", "instance", "ob2-reaction-handler-value", "OwnedHandler",
        "call:ob2-reaction-handler", "object", "inst:ob2-reaction-core",
    )
    r2.append("call:ob2-reaction-handler")
    add_call(
        nodes, "call:ob2-reaction-owner-read", "ob2-reaction-owner-read",
        "fixture_api.OwnedHandler.owner_ref", "instance", "test-harness", "OwnedHandler", [], "Core",
        "inst:ob2-reaction-owner-read", "inst:ob2-reaction-handler",
    )
    add_value(
        nodes, "inst:ob2-reaction-owner-read", "instance", "ob2-reaction-owner-read-value", "Core",
        "call:ob2-reaction-owner-read",
    )
    r2.append("call:ob2-reaction-owner-read")
    ob2_observe.append("call:ob2-reaction-owner-read")
    add_call(
        nodes, "call:ob2-reaction-map", "ob2-reaction-map", "fixture_api.CustomKindMap.one", "static", "test-harness",
        "CustomKindMap", [
            arg("kind", "str", "lit:custom-kind-a"),
            arg("handler_type", "HandlerTypeRef", "inst:ob2-handler-type"),
        ], "CustomKindMap", "inst:ob2-reaction-map",
    )
    add_value(
        nodes, "inst:ob2-reaction-map", "instance", "ob2-reaction-map-value", "CustomKindMap",
        "call:ob2-reaction-map", "object", "inst:ob2-handler-type",
    )
    r2.append("call:ob2-reaction-map")
    add_call(
        nodes, "call:ob2-reaction-rules", "ob2-reaction-rules", "fixture_api.ReactionRuleSet.from_custom", "static",
        "test-harness", "ReactionRuleSet", [arg("custom", "CustomKindMap", "inst:ob2-reaction-map")],
        "ReactionRuleSet", "inst:ob2-reaction-rules",
    )
    add_value(
        nodes, "inst:ob2-reaction-rules", "instance", "ob2-reaction-rules-value", "ReactionRuleSet",
        "call:ob2-reaction-rules", "object", "inst:ob2-reaction-map",
    )
    r2.append("call:ob2-reaction-rules")
    add_call(
        nodes, "call:ob2-reaction-operation", "ob2-reaction-operation", "fixture_api.Core.new_operation_id", "instance",
        "public", "Core", [], "OperationId", "slot:ob2-reaction-operation", "inst:ob2-reaction-core",
    )
    add_value(
        nodes, "slot:ob2-reaction-operation", "slot", "ob2-reaction-operation-value", "OperationId",
        "call:ob2-reaction-operation", "operation", "inst:ob2-reaction-core",
    )
    r2.append("call:ob2-reaction-operation")
    add_control(
        nodes, "control:ob2-reaction-fault", "ob2-reaction-fault", "slot:ob2-reaction-operation",
        "lit:phase-before", "slot:ob2-reaction-fault",
    )
    add_value(
        nodes, "slot:ob2-reaction-fault", "slot", "ob2-reaction-fault-value", "Fault",
        "control:ob2-reaction-fault", "operation", "slot:ob2-reaction-operation",
    )
    r2.append("control:ob2-reaction-fault")
    add_call(
        nodes, "call:ob2-reaction-impulse-control", "ob2-reaction-impulse-control",
        "fixture_api.OperationControl.impulse", "static", "internal-test-seam", "OperationControl", [
            arg("operation_id", "OperationId", "slot:ob2-reaction-operation"),
            arg("value", "Impulse", "inst:ob2-impulse"),
        ], "Impulse", "slot:ob2-reaction-impulse-control",
    )
    promote_operation_control(
        nodes, "call:ob2-reaction-impulse-control", "slot:ob2-reaction-operation", ["inst:ob2-impulse"]
    )
    add_value(
        nodes, "slot:ob2-reaction-impulse-control", "slot", "ob2-reaction-impulse-control-value", "Impulse",
        "call:ob2-reaction-impulse-control", "operation", "slot:ob2-reaction-operation",
    )
    r2.append("call:ob2-reaction-impulse-control")
    add_call(
        nodes, "call:ob2-reaction-handler-control", "ob2-reaction-handler-control",
        "fixture_api.OperationControl.handler", "static", "internal-test-seam", "OperationControl", [
            arg("operation_id", "OperationId", "slot:ob2-reaction-operation"),
            arg("value", "Handler", "inst:ob2-reaction-handler"),
        ], "Handler", "slot:ob2-reaction-handler-control",
    )
    promote_operation_control(
        nodes, "call:ob2-reaction-handler-control", "slot:ob2-reaction-operation", ["inst:ob2-reaction-handler"]
    )
    add_value(
        nodes, "slot:ob2-reaction-handler-control", "slot", "ob2-reaction-handler-control-value", "Handler",
        "call:ob2-reaction-handler-control", "operation", "slot:ob2-reaction-operation",
    )
    r2.append("call:ob2-reaction-handler-control")
    add_call(
        nodes, "call:ob2-reaction-step", "ob2-reaction-step", "fixture_api.Core.step_reaction", "instance", "public", "Core",
        [
            arg("operation_id", "OperationId", "slot:ob2-reaction-operation"),
            arg("impulse", "Impulse", "slot:ob2-reaction-impulse-control"),
            arg("handler", "Handler", "slot:ob2-reaction-handler-control"),
            arg("reactions", "ReactionRuleSet", "inst:ob2-reaction-rules"),
            arg("kind", "str", "lit:custom-kind-a"),
            arg("fault", "Fault", "slot:ob2-reaction-fault"),
        ], "CellResult", None, "inst:ob2-reaction-core", "RouteFault",
    )
    r2.append("call:ob2-reaction-step")
    ob2_construct.extend([
        "call:ob2-reaction-core", "call:ob2-reaction-handler", "call:ob2-reaction-map",
        "call:ob2-reaction-rules", "call:ob2-reaction-operation", "control:ob2-reaction-fault",
        "call:ob2-reaction-impulse-control", "call:ob2-reaction-handler-control",
    ])
    ob2_act.append("call:ob2-reaction-step")
    ob2_negative.extend([
        "control:ob2-reaction-fault", "call:ob2-reaction-impulse-control", "call:ob2-reaction-handler-control",
    ])
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
    add_call(
        nodes, "call:ob3-controlled-core", "ob3-controlled-core", "fixture_api.Core.existing", "class", "public", "Core",
        [arg("topology", "Topology", "inst:ob3-topology")], "Core", "inst:ob3-controlled-core",
    )
    add_value(
        nodes, "inst:ob3-controlled-core", "instance", "ob3-controlled-core-value", "Core",
        "call:ob3-controlled-core", "object",
    )
    r3.append("call:ob3-controlled-core")
    add_call(
        nodes, "call:ob3-source-operation", "ob3-source-operation", "fixture_api.Core.new_operation_id", "instance",
        "public", "Core", [], "OperationId", "slot:ob3-source-operation", "inst:ob3-controlled-core",
    )
    add_value(
        nodes, "slot:ob3-source-operation", "slot", "ob3-source-operation-value", "OperationId",
        "call:ob3-source-operation", "operation", "inst:ob3-controlled-core",
    )
    r3.append("call:ob3-source-operation")
    add_control(
        nodes, "control:ob3-source-fault", "ob3-source-fault", "slot:ob3-source-operation", "lit:phase-after",
        "slot:ob3-source-fault",
    )
    add_value(
        nodes, "slot:ob3-source-fault", "slot", "ob3-source-fault-value", "Fault", "control:ob3-source-fault",
        "operation", "slot:ob3-source-operation",
    )
    r3.append("control:ob3-source-fault")
    add_call(
        nodes, "call:ob3-source-control", "ob3-source-control", "fixture_api.OperationControl.source", "static",
        "internal-test-seam", "OperationControl", [
            arg("operation_id", "OperationId", "slot:ob3-source-operation"),
            arg("value", "SourceInput", "inst:ob3-source-input"),
        ], "SourceInput", "slot:ob3-source-control",
    )
    promote_operation_control(
        nodes, "call:ob3-source-control", "slot:ob3-source-operation", ["inst:ob3-source-input"]
    )
    add_value(
        nodes, "slot:ob3-source-control", "slot", "ob3-source-control-value", "SourceInput",
        "call:ob3-source-control", "operation", "slot:ob3-source-operation",
    )
    r3.append("call:ob3-source-control")
    add_call(
        nodes, "call:ob3-source-controlled-step", "ob3-source-controlled-step",
        "fixture_api.Core.step_source_controlled", "instance", "public", "Core", [
            arg("operation_id", "OperationId", "slot:ob3-source-operation"),
            arg("source", "SourceInput", "slot:ob3-source-control"),
            arg("fault", "Fault", "slot:ob3-source-fault"),
        ], "CellResult", None, "inst:ob3-controlled-core", "RouteFault",
    )
    r3.append("call:ob3-source-controlled-step")
    add_call(
        nodes, "call:ob3-controlled-audit-for", "ob3-controlled-audit-handle", "fixture_api.Audit.for_core", "static",
        "test-harness", "Audit", [arg("core", "Core", "inst:ob3-controlled-core")], "AuditHandle",
        "inst:ob3-controlled-audit",
    )
    add_value(
        nodes, "inst:ob3-controlled-audit", "instance", "ob3-controlled-audit-value", "AuditHandle",
        "call:ob3-controlled-audit-for",
    )
    r3.append("call:ob3-controlled-audit-for")
    add_call(
        nodes, "call:ob3-controlled-audit-read", "ob3-controlled-audit-read", "fixture_api.AuditHandle.read",
        "instance", "test-harness", "AuditHandle", [], "CellResult", "inst:ob3-controlled-audit-result",
        "inst:ob3-controlled-audit",
    )
    add_value(
        nodes, "inst:ob3-controlled-audit-result", "instance", "ob3-controlled-audit-result-value", "CellResult",
        "call:ob3-controlled-audit-read",
    )
    r3.append("call:ob3-controlled-audit-read")
    controlled_observers = add_observers(nodes, r3, "ob3-controlled-after", "inst:ob3-controlled-audit-result")
    routes["OB-3"]["construct"] = [
        "call:ob3-topology", "call:ob3-core", "call:ob3-source-input", "call:ob3-controlled-core",
        "call:ob3-source-operation", "control:ob3-source-fault", "call:ob3-source-control",
    ]
    routes["OB-3"]["act"] = ["call:ob3-step-source", "call:ob3-source-controlled-step"]
    routes["OB-3"]["observe"] = [
        *ob3_step_observers, "call:ob3-audit-for", "call:ob3-audit-read", *ob3_audit_observers,
        *ob3_golden_observers, "call:ob3-controlled-audit-for", "call:ob3-controlled-audit-read",
        *controlled_observers,
    ]
    routes["OB-3"]["negative"] = [
        "lit:neighbor-zero", "control:ob3-source-fault", "call:ob3-source-control",
    ]
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


def reference_descriptor(node: dict[str, Any], by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """Frozen shallow identity for every value or artifact used by a route."""
    kind = node["kind"]
    value: dict[str, Any] = {"kind": kind, "role": node["role"]}
    if kind == "typed-literal":
        value.update({"value_type": node["value_type"], "value": node["value"]})
    elif kind == "source-artifact":
        value.update(
            {
                "module": node["module"], "path": node["path"], "mode": node["mode"],
                "sha256": node["sha256"],
            }
        )
    elif kind == "runtime-resource":
        value.update(
            {
                "path": node["path"], "mode": node["mode"], "size": node["size"],
                "sha256": node["sha256"], "value_type": node["value_type"],
            }
        )
    elif kind in {"instance", "slot"}:
        owner_ref = node.get("owner_ref")
        producer = node.get("producer")
        value.update(
            {
                "value_type": node["value_type"], "lifetime": node["lifetime"],
                "owner_role": by_id[owner_ref]["role"] if owner_ref in by_id else None,
                "producer_role": by_id[producer]["role"] if producer in by_id else None,
            }
        )
    else:
        value["binding"] = node.get("signature")
    return value


def route_reference_descriptor(node: dict[str, Any], by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    if node["kind"] in {"typed-literal", "source-artifact", "runtime-resource", "instance", "slot"}:
        return reference_descriptor(node, by_id)
    return {"kind": node["kind"], "role": node["role"]}


def trace_descriptor(node: dict[str, Any], by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    kind = node["kind"]
    if kind == "runtime-resource":
        binding = "resource:" + node["path"]
        style = "resource"
        visibility = "frozen"
        owner_type = None
        args: list[dict[str, Any]] = []
        owner = None
        outcome = "returned"
    else:
        binding = node["signature"]
        style = node["style"]
        visibility = node["visibility"]
        owner_type = node["owner_type"]
        args = [
            {
                "name": item["name"], "type": item["type"],
                "source": reference_descriptor(by_id[item["source"]], by_id),
            }
            for item in node["args"]
        ]
        owner = reference_descriptor(by_id[node["owner_source"]], by_id) if node.get("owner_source") else None
        if kind == "reflection":
            outcome = "missing:AttributeError"
        else:
            expected = node.get("expected_exception")
            outcome = "exception:" + expected if expected else "returned"
    output_id = node.get("output")
    descriptor = {
        "kind": kind,
        "role": node["role"],
        "binding": binding,
        "style": style,
        "visibility": visibility,
        "owner_type": owner_type,
        "owner": owner,
        "args": args,
        "return_type": node.get("return_type", node.get("value_type")),
        "output": reference_descriptor(by_id[output_id], by_id) if output_id else None,
        "outcome": outcome,
    }
    if kind == "negative-control":
        descriptor["operation"] = reference_descriptor(by_id[node["operation_source"]], by_id)
        descriptor["subjects"] = [
            reference_descriptor(by_id[source], by_id) for source in node["subject_sources"]
        ]
    return descriptor


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
                "route_bindings": {
                    category: [route_reference_descriptor(by_id[node_id], by_id) for node_id in packet["routes"][obligation][category]]
                    for category in ("construct", "act", "observe", "negative", "source", "skeleton")
                },
                "trace": [trace_descriptor(by_id[node_id], by_id) for node_id in packet["recipes"][obligation]],
            }
        )
    spec = {
        "change_id": packet["change_id"],
        "observed_fields": OBSERVED_FIELDS,
        "fault_phases": FAULT_PHASES,
        "literal_authority": {
            row["role"]: {"value_type": row["value_type"], "value": row["value"]}
            for row in packet["nodes"] if row["kind"] == "typed-literal"
        },
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
    "source-artifact": {"id", "kind", "role", "module", "path", "mode", "sha256"},
    "instance": {"id", "kind", "role", "value_type", "producer", "lifetime", "owner_ref"},
    "slot": {"id", "kind", "role", "value_type", "producer", "lifetime", "owner_ref"},
    "runtime-resource": {"id", "kind", "role", "path", "mode", "size", "sha256", "output", "value_type"},
    "callable": {
        "id", "kind", "role", "signature", "style", "visibility", "owner_type", "owner_source", "args",
        "return_type", "output", "expected_exception",
    },
    "negative-control": {
        "id", "kind", "role", "signature", "style", "visibility", "owner_type", "owner_source", "args",
        "return_type", "output", "operation_source", "subject_sources",
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


def witness_product_config(version: int) -> dict[str, Any]:
    return {
        "synced_contract_version": version,
        "retry_budget": {"per_gate": 3, "fresh_context_after": 2},
        "mutation": {"kill_rate_floor": 70, "scope": "diff"},
        "escalation": {"after_attempts": 3, "action": "stop-and-contact-owner"},
        "roots": {
            "source": ".", "resources": "resources", "results": "docs/results",
            "reviews": "docs/reviews", "changes": "openspec/changes",
        },
        "product_result_template": "docs/results/{change_id}.md",
        "handoff_command": "python tools/check.py --deliver",
        "plan_handoff_trust_roots": [
            {"path": "validation.config", "mode": "100644"},
            {"path": "fixture_api.py", "mode": "100644"},
            {"path": "resources/golden-cell.json", "mode": "100644"},
            {"path": "resources/golden-source.json", "mode": "100644"},
        ],
    }


def product_stamp_bytes(version: int) -> bytes:
    return canonical_bytes(witness_product_config(version))


def write_product_stamp(product_root: Path, version: int) -> None:
    (product_root / PRODUCT_STAMP_PATH).write_bytes(product_stamp_bytes(version))


def product_contract_authority(product_root: Path, gaps: list[Gap] | None = None) -> dict[str, Any] | None:
    path = product_root / PRODUCT_STAMP_PATH
    if not regular_file(path):
        if gaps is not None:
            add_gap(gaps, "E_CONTRACT_PRODUCT_STAMP", "/product/validation.config", "stamp file absent")
        return None
    try:
        value = load_json(path)
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        if gaps is not None:
            add_gap(gaps, "E_CONTRACT_PRODUCT_STAMP", "/product/validation.config", error.__class__.__name__)
        return None
    version = value.get("synced_contract_version") if isinstance(value, dict) else None
    if type(version) is not int or value != witness_product_config(version):
        if gaps is not None:
            add_gap(
                gaps, "E_CONTRACT_PRODUCT_CONFIG", "/product/validation.config",
                "exact closed workflow config required",
            )
        return None
    return {
        "path": str(path.resolve()),
        "mode": logical_mode(path),
        "sha256": file_sha256(path),
        "current": version,
    }


def embedded_reference_authority(
    source: str = FIXTURE_SOURCE, hidden_helper: bool = False
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Adapter-reviewed grammar derived from OS-owned bytes, never candidate P."""
    with tempfile.TemporaryDirectory(prefix="v21-authority-") as root_raw:
        product_root = Path(root_raw)
        (product_root / "resources").mkdir()
        (product_root / "fixture_api.py").write_text(source, encoding="utf-8", newline="\n")
        if hidden_helper:
            (product_root / "hidden_helper.py").write_text(HIDDEN_HELPER_SOURCE, encoding="utf-8", newline="\n")
        (product_root / "resources" / "golden-cell.json").write_bytes(GOLDEN_CELL)
        (product_root / "resources" / "golden-source.json").write_bytes(GOLDEN_SOURCE)
        write_product_stamp(product_root, live_contract_version())
        return frozen_authority(base_testability(product_root, "embedded-authority"))


def derive_authority(done_when: Any, spec: Any, gaps: list[Gap]) -> tuple[list[str], dict[str, Any]]:
    profiles = [
        embedded_reference_authority(), embedded_reference_authority(HOSTILE_FIXTURE_SOURCE),
        embedded_reference_authority(HIDDEN_IMPORT_FIXTURE_SOURCE, hidden_helper=True),
        embedded_reference_authority(MALFORMED_CATALOG_FIXTURE_SOURCE),
        embedded_reference_authority(MALFORMED_PARENTS_FIXTURE_SOURCE),
        embedded_reference_authority(BUILTINS_ESCAPE_FIXTURE_SOURCE),
    ]
    selected = next((item for item in profiles if done_when == item[0] and spec == item[1]), None)
    reference_done, reference_spec = selected or profiles[0]
    if selected is None:
        if done_when != reference_done:
            add_gap(gaps, "E_AUTHORITY_DONE_WHEN", "/authority/done_when", "frozen meanings differ from reviewed adapter grammar")
        if spec != reference_spec:
            add_gap(gaps, "E_AUTHORITY_SPEC", "/authority/spec", "frozen route grammar is incomplete or differs")
    reference_rows = reference_spec["obligations"]
    union = [row["id"] for row in reference_rows]
    by_id = {row["id"]: row for row in reference_rows}
    return union, by_id


def dependency_manifest(paths: list[Path] | tuple[str, ...]) -> list[dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for raw in paths:
        path = Path(raw).resolve()
        if not regular_file(path):
            raise HarnessError("toolchain dependency disappeared: " + str(path))
        key = str(path).lower()
        rows[key] = {"path": str(path), "sha256": file_sha256(path)}
    return [rows[key] for key in sorted(rows)]


def loaded_dependency_manifest() -> list[dict[str, str]]:
    paths: list[Path] = []
    for module in tuple(sys.modules.values()):
        raw = getattr(module, "__file__", None)
        if isinstance(raw, str):
            try:
                path = Path(raw).resolve()
            except OSError:
                continue
            if regular_file(path):
                paths.append(path)
    for path in Path(sys.executable).resolve().parent.glob("python*.dll"):
        if regular_file(path):
            paths.append(path.resolve())
    return dependency_manifest(paths)


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
        "dependencies": dependency_manifest(BOOT_MODULE_FILES),
        "commands": ["py_compile", "discover", "filter", "product-exec", "union"],
    }


def git_command(args: list[str], git_dir: Path | None = None, cwd: Path | None = None) -> bytes:
    argv = ["git"]
    if git_dir is not None:
        argv.extend(["--git-dir", str(git_dir)])
    argv.extend(args)
    process = subprocess.run(argv, cwd=str(cwd) if cwd is not None else None, capture_output=True, check=False)
    if process.returncode != 0:
        detail = process.stderr.decode("utf-8", errors="replace").strip()
        raise HarnessError("git authority command failed: " + detail)
    return process.stdout


def canonical_repo_id(remote_url: str) -> str:
    raw = remote_url.strip().replace("\\", "/").rstrip("/")
    if raw.lower().endswith(".git"):
        raw = raw[:-4]
    if "://" not in raw and not raw.startswith("git@"):
        raw = str(Path(raw).resolve()).replace("\\", "/")
    return raw.lower()


def contract_current_from_bytes(raw: bytes) -> int:
    try:
        lines = raw.decode("utf-8").splitlines()
    except UnicodeError as error:
        raise HarnessError("contract authority is not UTF-8") from error
    current_rows = [line for line in lines if line.startswith("current:")]
    if len(current_rows) != 1:
        raise HarnessError("live contract authority has no unique current ordinal")
    try:
        current = int(current_rows[0].split(":", 1)[1].strip())
    except ValueError as error:
        raise HarnessError("live contract ordinal is invalid") from error
    return current


def git_object_identity(git_dir: Path, commit: str, relative: str, include_current: bool) -> dict[str, Any]:
    listing = git_command(["ls-tree", commit, "--", relative], git_dir=git_dir).decode("utf-8").strip()
    parts = listing.split(None, 3)
    if len(parts) != 4 or parts[1] != "blob" or parts[3] != relative or parts[0] != "100644":
        raise HarnessError("authority object missing or non-regular: " + relative)
    blob = parts[2]
    raw = git_command(["cat-file", "blob", blob], git_dir=git_dir)
    result: dict[str, Any] = {
        "path": relative, "mode": parts[0], "git_blob": blob, "sha256": sha256_bytes(raw),
    }
    if include_current:
        result["current"] = contract_current_from_bytes(raw)
    return result


def resolve_remote_authority(remote_url: str, common_dir: Path) -> dict[str, Any]:
    if not common_dir.is_absolute() or not common_dir.is_dir():
        raise HarnessError("authority cache common-dir absent")
    output = git_command(["ls-remote", "--exit-code", remote_url, CANONICAL_AUTHORITY_REF]).decode("utf-8").strip()
    rows = [line.split() for line in output.splitlines() if line.strip()]
    if len(rows) != 1 or len(rows[0]) != 2 or rows[0][1] != CANONICAL_AUTHORITY_REF:
        raise HarnessError("canonical remote main did not resolve uniquely")
    ref_sha = rows[0][0]
    git_command(["fetch", "--no-tags", remote_url, ref_sha], git_dir=common_dir)
    return {
        "source": "canonical-remote-main",
        "repo_id": canonical_repo_id(remote_url),
        "remote_url": remote_url,
        "common_dir": str(common_dir.resolve()),
        "ref": CANONICAL_AUTHORITY_REF,
        "observed_ref_sha": ref_sha,
        "contract": git_object_identity(common_dir, ref_sha, CONTRACT_RELATIVE_PATH, True),
        "checker": git_object_identity(common_dir, ref_sha, CHECKER_RELATIVE_PATH, False),
    }


def authority_stable_projection(row: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in row.items() if key != "observed_ref_sha"}


def authority_schema_valid(row: Any) -> bool:
    if not isinstance(row, dict) or set(row) != {
        "source", "repo_id", "remote_url", "common_dir", "ref", "observed_ref_sha", "contract", "checker",
    }:
        return False
    if (
        row.get("source") != "canonical-remote-main" or row.get("ref") != CANONICAL_AUTHORITY_REF
        or not all(nonempty_text(row.get(key)) for key in ("repo_id", "remote_url", "common_dir", "observed_ref_sha"))
    ):
        return False
    contract = row.get("contract")
    checker = row.get("checker")
    return (
        isinstance(contract, dict) and set(contract) == {"path", "mode", "git_blob", "sha256", "current"}
        and contract.get("path") == CONTRACT_RELATIVE_PATH and contract.get("mode") == "100644"
        and type(contract.get("current")) is int
        and all(nonempty_text(contract.get(key)) for key in ("git_blob", "sha256"))
        and isinstance(checker, dict) and set(checker) == {"path", "mode", "git_blob", "sha256"}
        and checker.get("path") == CHECKER_RELATIVE_PATH and checker.get("mode") == "100644"
        and all(nonempty_text(checker.get(key)) for key in ("git_blob", "sha256"))
    )


def independently_resolve_authority(row: Any, gaps: list[Gap], path: str) -> dict[str, Any] | None:
    if not authority_schema_valid(row):
        add_gap(gaps, "E_CONTRACT_RESOLVER", path, "closed canonical remote/main resolver row required")
        return None
    if row["repo_id"] != canonical_repo_id(row["remote_url"]):
        add_gap(gaps, "E_CONTRACT_RESOLVER", path + "/repo_id", "canonical remote identity differs")
        return None
    try:
        fresh = resolve_remote_authority(row["remote_url"], Path(row["common_dir"]))
    except HarnessError as error:
        add_gap(gaps, "E_CONTRACT_RESOLVER", path, str(error))
        return None
    if authority_stable_projection(row) != authority_stable_projection(fresh):
        add_gap(gaps, "E_CONTRACT_AUTHORITY", path, "fresh remote object identities differ")
    script = Path(__file__).resolve()
    contract_path = script.with_name("CONTRACT_VERSION")
    if file_sha256(script) != fresh["checker"]["sha256"]:
        add_gap(gaps, "E_CONTRACT_CHECKER", path + "/checker", "executing checker is not remote/main object")
    if not regular_file(contract_path) or file_sha256(contract_path) != fresh["contract"]["sha256"]:
        add_gap(gaps, "E_CONTRACT_CHECKOUT", path + "/contract", "adjacent contract is not remote/main object")
    return fresh


def set_active_authority(row: dict[str, Any]) -> None:
    global ACTIVE_AUTHORITY
    if not authority_schema_valid(row):
        raise HarnessError("active authority seed schema invalid")
    ACTIVE_AUTHORITY = copy.deepcopy(row)


def live_contract_authority() -> dict[str, Any]:
    if ACTIVE_AUTHORITY is None:
        raise HarnessError("explicit remote authority seed absent")
    return copy.deepcopy(ACTIVE_AUTHORITY)


def live_contract_version() -> int:
    return live_contract_authority()["contract"]["current"]


def initialize_bare_repository(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    git_command(["init", "--bare", str(path)])


def canonical_remote_from_commit(root: Path, source: str, commit: str) -> dict[str, Any]:
    remote = root / "canonical-remote.git"
    cache = root / "resolver-cache.git"
    initialize_bare_repository(remote)
    initialize_bare_repository(cache)
    git_command(
        ["fetch", "--no-tags", source, f"{commit}:{CANONICAL_AUTHORITY_REF}"],
        git_dir=remote,
    )
    git_command(["symbolic-ref", "HEAD", CANONICAL_AUTHORITY_REF], git_dir=remote)
    return resolve_remote_authority(str(remote.resolve()), cache.resolve())


def committed_candidate_authority(root: Path) -> tuple[dict[str, Any], str]:
    script = Path(__file__).resolve()
    repo_root = Path(
        git_command(["rev-parse", "--show-toplevel"], cwd=script.parent).decode("utf-8").strip()
    ).resolve()
    head = git_command(["rev-parse", "HEAD"], cwd=repo_root).decode("ascii").strip()
    checker_bytes = git_command(["show", f"{head}:{CHECKER_RELATIVE_PATH}"], cwd=repo_root)
    contract_bytes = git_command(["show", f"{head}:{CONTRACT_RELATIVE_PATH}"], cwd=repo_root)
    if script.read_bytes() != checker_bytes:
        raise HarnessError("executing checker is not the exact committed candidate object")
    adjacent = script.with_name("CONTRACT_VERSION")
    if not regular_file(adjacent) or adjacent.read_bytes() != contract_bytes:
        raise HarnessError("adjacent contract is not the exact committed candidate object")
    return canonical_remote_from_commit(root, str(repo_root), head), head


def development_fixture_authority(root: Path) -> tuple[dict[str, Any], str]:
    work = root / "candidate-work"
    work.mkdir(parents=True)
    git_command(["init", "-b", "main"], cwd=work)
    git_command(["config", "user.email", "v21@example.invalid"], cwd=work)
    git_command(["config", "user.name", "v21 witness"], cwd=work)
    git_command(["config", "core.autocrlf", "false"], cwd=work)
    for relative, source in (
        (CHECKER_RELATIVE_PATH, Path(__file__).resolve()),
        (CONTRACT_RELATIVE_PATH, Path(__file__).resolve().with_name("CONTRACT_VERSION")),
    ):
        target = work / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())
    git_command(["add", "--all"], cwd=work)
    git_command(["commit", "-m", "development authority fixture"], cwd=work)
    commit = git_command(["rev-parse", "HEAD"], cwd=work).decode("ascii").strip()
    return canonical_remote_from_commit(root / "remote", str(work), commit), commit


def materialize_case_authority(root: Path, seed: dict[str, Any]) -> dict[str, Any]:
    if not authority_schema_valid(seed):
        raise HarnessError("parent authority seed invalid")
    return canonical_remote_from_commit(root, seed["remote_url"], seed["observed_ref_sha"])


def advance_case_remote(authority: dict[str, Any], changes: dict[str, bytes]) -> None:
    with tempfile.TemporaryDirectory(prefix="v21-authority-advance-") as work_raw:
        work = Path(work_raw)
        git_command(["clone", authority["remote_url"], str(work)])
        git_command(["config", "user.email", "v21@example.invalid"], cwd=work)
        git_command(["config", "user.name", "v21 witness"], cwd=work)
        for relative, raw in changes.items():
            target = work / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
        git_command(["add", "--all"], cwd=work)
        git_command(["commit", "-m", "authority mutation fixture"], cwd=work)
        git_command(["push", "origin", f"HEAD:{CANONICAL_AUTHORITY_REF}"], cwd=work)


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
    if set(expected) != set(codes):
        add_gap(gaps, "E_TOOLCHAIN_SCHEMA", prefix, "toolchain fields differ from closed schema")
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
        if isinstance(node.get("operation_source"), str):
            refs.append(node["operation_source"])
        for source in node.get("subject_sources", []) if isinstance(node.get("subject_sources"), list) else []:
            if isinstance(source, str):
                refs.append(source)
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
            refs.append(node.get("operation_source"))
            refs.extend(node.get("subject_sources", []) if isinstance(node.get("subject_sources"), list) else [])
    return [item for item in refs if isinstance(item, str)]


def source_artifact(packet: Any, product_root: Path, gaps: list[Gap] | None = None) -> tuple[dict[str, Any], Path] | None:
    rows = packet.get("nodes") if isinstance(packet, dict) else None
    if not isinstance(rows, list):
        if gaps is not None:
            add_gap(gaps, "E_SOURCE_COUNT", "/registry/source-artifact", "exactly one runtime source is required")
        return None
    sources = [row for row in rows if isinstance(row, dict) and row.get("kind") == "source-artifact"]
    if len(sources) != 1:
        if gaps is not None:
            add_gap(gaps, "E_SOURCE_COUNT", "/registry/source-artifact", "exactly one runtime source is required")
        return None
    row = sources[0]
    module_name = row.get("module")
    relative = row.get("path")
    target = resolved_inside(product_root, relative) if isinstance(relative, str) else None
    if not isinstance(module_name, str) or not module_name or target is None or target.suffix != ".py":
        if gaps is not None:
            add_gap(gaps, "E_SOURCE_MODULE", "/registry/" + str(row.get("id", "source")), "module/path is not executable Python source")
        return None
    if target.stem != module_name or not regular_file(target):
        if gaps is not None:
            add_gap(gaps, "E_SOURCE_MODULE", "/registry/" + str(row.get("id", "source")), "module does not name its exact source path")
        return None
    return row, target


def product_source_capability_gaps(syntax: ast.Module, source_id: str) -> list[Gap]:
    """Positive, witness-specific Python capability grammar for product bytes."""
    reasons: set[str] = set()
    imported_modules: set[str] = set()
    allowed_top_assignments = {"TYPE_PARENTS", "BINDING_API"}
    for statement in syntax.body:
        if isinstance(statement, ast.Import):
            if any(item.name != "json" or item.asname is not None for item in statement.names):
                reasons.add("top-import")
            imported_modules.update((item.asname or item.name.split(".", 1)[0]) for item in statement.names)
        elif isinstance(statement, ast.ImportFrom):
            if (
                statement.level != 0 or statement.module != "dataclasses" or len(statement.names) != 1
                or statement.names[0].name != "dataclass" or statement.names[0].asname is not None
            ):
                reasons.add("top-import-from")
        elif isinstance(statement, ast.ClassDef):
            for decorator in statement.decorator_list:
                if not (
                    isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Name)
                    and decorator.func.id == "dataclass" and not decorator.args
                    and len(decorator.keywords) == 1 and decorator.keywords[0].arg == "frozen"
                    and isinstance(decorator.keywords[0].value, ast.Constant)
                    and decorator.keywords[0].value.value is True
                ):
                    reasons.add("class-decorator")
            if any(not isinstance(base, ast.Name) for base in statement.bases):
                reasons.add("dynamic-class-base")
        elif isinstance(statement, ast.Assign):
            if (
                len(statement.targets) != 1 or not isinstance(statement.targets[0], ast.Name)
                or statement.targets[0].id not in allowed_top_assignments
            ):
                reasons.add("executable-top-level")
            else:
                try:
                    ast.literal_eval(statement.value)
                except (ValueError, TypeError):
                    reasons.add("nonliteral-authority")
        else:
            reasons.add("executable-top-level")

    forbidden_nodes = (
        ast.Global, ast.Nonlocal, ast.Lambda, ast.Delete, ast.With, ast.AsyncWith, ast.Try,
        ast.While, ast.For, ast.AsyncFor, ast.ListComp, ast.SetComp, ast.DictComp,
        ast.GeneratorExp, ast.Await, ast.Yield, ast.YieldFrom, ast.NamedExpr,
    )

    def root_name(value: ast.AST) -> str | None:
        while isinstance(value, ast.Attribute):
            value = value.value
        return value.id if isinstance(value, ast.Name) else None

    for node in ast.walk(syntax):
        if isinstance(node, forbidden_nodes):
            reasons.add("forbidden-node:" + node.__class__.__name__)
        if isinstance(node, ast.Name) and "__" in node.id:
            reasons.add("dunder-name")
        if isinstance(node, ast.Attribute) and "__" in node.attr:
            reasons.add("dunder-attribute")
        if isinstance(node, ast.Subscript):
            key = node.slice
            if isinstance(key, ast.Constant) and isinstance(key.value, str) and "__" in key.value:
                reasons.add("dunder-subscript")
        if isinstance(node, ast.Call):
            if isinstance(node.func, (ast.Subscript, ast.Lambda)):
                reasons.add("dynamic-callee")
            else:
                try:
                    callee = ast.unparse(node.func)
                except Exception:
                    callee = ""
                if callee not in APPROVED_PRODUCT_CALLEES:
                    reasons.add("unapproved-callee:" + callee)
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if isinstance(target, ast.Attribute) and root_name(target) in imported_modules:
                    reasons.add("imported-module-mutation")
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for decorator in node.decorator_list:
                if not isinstance(decorator, ast.Name) or decorator.id not in {"staticmethod", "classmethod"}:
                    reasons.add("function-decorator")
    if not reasons:
        return []
    return [
        Gap(
            "E_SOURCE_PROCESS_ESCAPE", "/registry/" + source_id,
            ",".join(sorted(reasons)),
        )
    ]


def source_catalog_schema_gaps(catalog: Any, parents: Any, source_id: str) -> list[Gap]:
    gaps: list[Gap] = []
    base = "/registry/" + source_id
    if not isinstance(catalog, dict) or not catalog:
        return [Gap("E_SOURCE_CATALOG", base + "/BINDING_API", "nonempty literal object required")]
    for signature, row in catalog.items():
        path = base + "/BINDING_API/" + str(signature)
        if not nonempty_text(signature) or not isinstance(row, list) or len(row) != 5:
            add_gap(gaps, "E_SOURCE_CATALOG", path, "API row must have five fields")
            continue
        style, visibility, owner_type, args, return_type = row
        if style not in {"static", "class", "instance", "constructor"}:
            add_gap(gaps, "E_SOURCE_CATALOG", path + "/0", "closed callable style required")
        if visibility not in {"public", "test-harness", "internal-test-seam"}:
            add_gap(gaps, "E_SOURCE_CATALOG", path + "/1", "closed visibility required")
        if not nonempty_text(owner_type):
            add_gap(gaps, "E_SOURCE_CATALOG", path + "/2", "owner type required")
        if not isinstance(args, list):
            add_gap(gaps, "E_SOURCE_CATALOG", path + "/3", "ordered argument rows required")
        else:
            for index, item in enumerate(args):
                if (
                    not isinstance(item, list) or len(item) != 2
                    or not nonempty_text(item[0]) or not nonempty_text(item[1])
                ):
                    add_gap(gaps, "E_SOURCE_CATALOG", f"{path}/3/{index}", "argument name/type row differs")
        if not nonempty_text(return_type):
            add_gap(gaps, "E_SOURCE_CATALOG", path + "/4", "return type required")
    if not isinstance(parents, dict):
        add_gap(gaps, "E_SOURCE_CATALOG", base + "/TYPE_PARENTS", "literal parent object required")
    else:
        for child, values in parents.items():
            path = base + "/TYPE_PARENTS/" + str(child)
            if (
                not nonempty_text(child) or not isinstance(values, list) or not values
                or any(not nonempty_text(value) for value in values)
                or len(set(values)) != len(values) or child in values
            ):
                add_gap(gaps, "E_SOURCE_CATALOG", path, "nonempty unique parent type rows required")
    return normalized_gaps(gaps)


def static_api_model(packet: Any, product_root: Path, gaps: list[Gap]) -> dict[str, Any] | None:
    """Inspect the exact source without importing product code into the validator."""
    resolved = source_artifact(packet, product_root, gaps)
    if resolved is None:
        return None
    source_row, source_path = resolved
    try:
        syntax = ast.parse(source_path.read_text(encoding="utf-8"), filename=str(source_path))
    except (OSError, UnicodeError, SyntaxError) as error:
        add_gap(gaps, "E_SOURCE_PARSE", "/registry/" + str(source_row.get("id", "source")) + "/path", error.__class__.__name__)
        return None
    capability_gaps = product_source_capability_gaps(syntax, str(source_row.get("id", "source")))
    gaps.extend(capability_gaps)
    if capability_gaps:
        return None
    assignments: dict[str, Any] = {}
    classes: dict[str, ast.ClassDef] = {}
    for statement in syntax.body:
        if isinstance(statement, (ast.Assign, ast.AnnAssign)):
            targets = statement.targets if isinstance(statement, ast.Assign) else [statement.target]
            if len(targets) == 1 and isinstance(targets[0], ast.Name):
                try:
                    assignments[targets[0].id] = ast.literal_eval(statement.value)
                except (ValueError, TypeError):
                    pass
        elif isinstance(statement, ast.ClassDef):
            classes[statement.name] = statement
    catalog = assignments.get("BINDING_API")
    parents = assignments.get("TYPE_PARENTS")
    catalog_gaps = source_catalog_schema_gaps(catalog, parents, str(source_row.get("id", "source")))
    gaps.extend(catalog_gaps)
    if catalog_gaps:
        return None
    module_name = source_row["module"]
    parameters: dict[str, list[str]] = {}
    for class_name, class_node in classes.items():
        init = next((item for item in class_node.body if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) and item.name == "__init__"), None)
        if init is not None:
            parameters[f"{module_name}.{class_name}"] = [item.arg for item in init.args.args[1:]]
        for item in class_node.body:
            if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) or item.name == "__init__":
                continue
            names = [arg_node.arg for arg_node in item.args.args]
            decorator_names = {decorator.id for decorator in item.decorator_list if isinstance(decorator, ast.Name)}
            if not ({"staticmethod"} & decorator_names) and names:
                names = names[1:]
            parameters[f"{module_name}.{class_name}.{item.name}"] = names
    return {
        "module": module_name,
        "path": source_row["path"],
        "catalog": catalog,
        "type_parents": parents,
        "parameters": parameters,
    }


def load_product_module(packet: dict[str, Any], product_root: Path) -> Any:
    resolved = source_artifact(packet, product_root)
    if resolved is None:
        raise HarnessError("validated runtime source is absent")
    source_row, module_path = resolved
    module_name = source_row["module"]
    sys.dont_write_bytecode = True
    sys.modules.pop(module_name, None)
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise HarnessError("cannot load runtime source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def resolve_symbol(module: Any, signature: str) -> Any:
    parts = signature.split(".")
    if len(parts) < 2 or parts[0] != module.__name__:
        raise AttributeError(signature)
    value: Any = module
    for part in parts[1:]:
        value = getattr(value, part)
    return value


def catalog_row(api_model: dict[str, Any], signature: str) -> dict[str, Any] | None:
    raw = api_model.get("catalog", {}).get(signature)
    if not isinstance(raw, list) or len(raw) != 5:
        return None
    style, visibility, owner_type, args, return_type = raw
    if (
        style not in {"static", "class", "instance", "constructor"}
        or visibility not in {"public", "test-harness", "internal-test-seam"}
        or not nonempty_text(owner_type) or not nonempty_text(return_type)
        or not isinstance(args, list)
        or any(
            not isinstance(item, list) or len(item) != 2
            or not nonempty_text(item[0]) or not nonempty_text(item[1])
            for item in args
        )
    ):
        return None
    return {
        "style": style,
        "visibility": visibility,
        "owner_type": owner_type,
        "args": [{"name": item[0], "type": item[1]} for item in args],
        "return_type": return_type,
    }


def type_assignable(actual: str, expected: str, model: Any) -> bool:
    if actual == expected:
        return True
    parents = model.get("type_parents", {}) if isinstance(model, dict) else getattr(model, "TYPE_PARENTS", {})
    values = parents.get(actual, []) if isinstance(parents, dict) else []
    return isinstance(values, list) and expected in values


BUILTIN_RUNTIME_TYPES: dict[str, type[Any]] = {
    "None": type(None), "bytes": bytes, "str": str, "int": int,
    "AttributeError": AttributeError, "TypeError": TypeError, "ValueError": ValueError,
    "RuntimeError": RuntimeError,
}


def builtin_type_token(name: str) -> str:
    return "builtin:" + sha256_bytes(canonical_bytes(["builtin-type", name]))


def product_type_token(packet: dict[str, Any], name: str) -> str:
    source = next(
        (
            row for row in packet.get("nodes", [])
            if isinstance(row, dict) and row.get("kind") == "source-artifact"
        ),
        None,
    )
    if source is None or not nonempty_text(source.get("sha256")) or not nonempty_text(source.get("module")):
        raise HarnessError("source identity absent while deriving runtime type token")
    return "product:" + sha256_bytes(
        canonical_bytes(["product-type", source["sha256"], source["module"], name])
    )


def declared_type_token(packet: dict[str, Any], name: str) -> str:
    if name in BUILTIN_RUNTIME_TYPES:
        return builtin_type_token(name)
    return product_type_token(packet, name)


def worker_value_identity(value: Any, module: Any, packet: dict[str, Any]) -> tuple[str, str] | None:
    actual_class = type(value)
    for name, expected_class in BUILTIN_RUNTIME_TYPES.items():
        if actual_class is expected_class:
            return name, builtin_type_token(name)
    name = getattr(actual_class, "__name__", None)
    if not nonempty_text(name):
        return None
    selected_class = getattr(module, name, None)
    if not isinstance(selected_class, type) or selected_class is not actual_class:
        return None
    return name, product_type_token(packet, name)


def worker_value_assignable(
    value: Any, expected: str, module: Any, packet: dict[str, Any]
) -> tuple[bool, str | None]:
    identity = worker_value_identity(value, module, packet)
    if identity is None:
        return False, None
    actual_name, token = identity
    builtin = BUILTIN_RUNTIME_TYPES.get(expected)
    if builtin is not None:
        return type(value) is builtin, token
    expected_class = getattr(module, expected, None)
    if not isinstance(expected_class, type):
        return False, token
    parents = getattr(module, "TYPE_PARENTS", {})
    declared_parents = parents.get(actual_name, []) if isinstance(parents, dict) else []
    allowed = actual_name == expected or (
        isinstance(declared_parents, list) and expected in declared_parents
    )
    return allowed and isinstance(value, expected_class), token


def literal_runtime_type(value: Any) -> str:
    if value is None:
        return "None"
    if type(value) is bytes:
        return "bytes"
    if type(value) is str:
        return "str"
    if type(value) is int:
        return "int"
    return value.__class__.__name__


def nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value) and value == value.strip()


def valid_optional_text(value: Any) -> bool:
    return value is None or nonempty_text(value)


def node_shape_valid(row: dict[str, Any], node_id: str, gaps: list[Gap]) -> bool:
    kind = row.get("kind")
    path = "/registry/" + node_id
    valid = nonempty_text(row.get("id")) and nonempty_text(row.get("role")) and nonempty_text(kind)
    if kind == "typed-literal":
        valid = valid and nonempty_text(row.get("value_type"))
    elif kind == "source-artifact":
        valid = valid and all(nonempty_text(row.get(key)) for key in ("module", "path", "mode", "sha256"))
    elif kind in {"instance", "slot"}:
        valid = valid and all(nonempty_text(row.get(key)) for key in ("value_type", "producer", "lifetime"))
        valid = valid and valid_optional_text(row.get("owner_ref"))
    elif kind == "runtime-resource":
        valid = valid and all(
            nonempty_text(row.get(key)) for key in ("path", "mode", "sha256", "output", "value_type")
        )
        valid = valid and type(row.get("size")) is int and row["size"] >= 0
    elif kind in {"callable", "negative-control", "reflection"}:
        valid = valid and all(
            nonempty_text(row.get(key)) for key in ("signature", "style", "visibility", "owner_type", "return_type")
        )
        args = row.get("args")
        if not isinstance(args, list):
            valid = False
        else:
            for item in args:
                if not isinstance(item, dict) or set(item) != {"name", "type", "source"}:
                    valid = False
                    continue
                if not all(nonempty_text(item.get(key)) for key in ("name", "type", "source")):
                    valid = False
        if kind == "callable":
            valid = valid and valid_optional_text(row.get("owner_source"))
            valid = valid and valid_optional_text(row.get("output"))
            valid = valid and valid_optional_text(row.get("expected_exception"))
        elif kind == "negative-control":
            valid = valid and valid_optional_text(row.get("owner_source"))
            valid = valid and nonempty_text(row.get("output"))
            valid = valid and nonempty_text(row.get("operation_source"))
            subjects = row.get("subject_sources")
            valid = valid and isinstance(subjects, list) and bool(subjects)
            if isinstance(subjects, list):
                valid = valid and all(nonempty_text(source) for source in subjects)
        else:
            valid = valid and nonempty_text(row.get("expected_exception"))
    if not valid:
        add_gap(gaps, "E_NODE_SCHEMA", path, "nested node schema differs")
    return valid


def audit_packet(
    packet: Any,
    product_root: Path,
    authority_union: list[str],
    authority_by_id: dict[str, Any],
    api_model: dict[str, Any] | None,
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
    if not rows:
        add_gap(gaps, "E_EMPTY_BINDING_CONTRACT", "/nodes", "binding registry cannot be empty")
    by_id: dict[str, dict[str, Any]] = {}
    roles: dict[str, str] = {}
    schema_invalid: set[str] = set()
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
        if not isinstance(kind, str) or kind not in NODE_KEYS:
            add_gap(gaps, "E_KIND", "/registry/" + node_id + "/kind", "unknown or conflated kind")
            schema_invalid.add(node_id)
            continue
        expected_keys = NODE_KEYS[kind]
        if set(row) != expected_keys:
            add_gap(gaps, "E_NODE_SCHEMA", "/registry/" + node_id, "exact kind schema differs")
            schema_invalid.add(node_id)
        elif not node_shape_valid(row, node_id, gaps):
            schema_invalid.add(node_id)

    recipes_value = packet.get("recipes")
    routes_value = packet.get("routes")
    recipes_container_valid = isinstance(recipes_value, dict)
    routes_container_valid = isinstance(routes_value, dict)
    recipes: dict[str, list[str]] = {}
    routes: dict[str, dict[str, list[str]]] = {}
    if not isinstance(recipes_value, dict):
        add_gap(gaps, "E_RECIPE_SCHEMA", "/recipes", "recipes must be an ordered object")
    else:
        for obligation, values in recipes_value.items():
            if not nonempty_text(obligation) or not isinstance(values, list) or any(not nonempty_text(item) for item in values):
                add_gap(gaps, "E_RECIPE_SCHEMA", "/recipes/" + str(obligation), "recipe ids must be nonempty strings")
            else:
                recipes[obligation] = values
    if not isinstance(routes_value, dict):
        add_gap(gaps, "E_ROUTE_SCHEMA", "/routes", "routes must be an ordered object")
    else:
        for obligation, route in routes_value.items():
            if not nonempty_text(obligation) or not isinstance(route, dict):
                add_gap(gaps, "E_ROUTE_SCHEMA", "/routes/" + str(obligation), "route must be object")
                continue
            valid_route = True
            for category, values in route.items():
                if category not in ROUTE_CATEGORIES or not isinstance(values, list) or any(not nonempty_text(item) for item in values):
                    add_gap(
                        gaps, "E_ROUTE_SCHEMA", f"/routes/{obligation}/{category}",
                        "route ids must be nonempty strings",
                    )
                    valid_route = False
            if valid_route:
                routes[obligation] = route

    # Collapse every dangling use to one canonical row so a complete sweep is
    # readable instead of producing dozens of cascaded follow-on messages.
    missing_refs: set[str] = set()
    obligation_missing_refs: dict[str, set[str]] = {obligation: set() for obligation in authority_union}
    for node_id, row in by_id.items():
        if node_id in schema_invalid:
            continue
        missing_refs.update(item for item in node_references(row) if item not in by_id)
    for obligation in authority_union:
        steps = recipes.get(obligation)
        if isinstance(steps, list):
            obligation_missing_refs[obligation].update(item for item in steps if item not in by_id)
            for item in steps:
                if item in by_id and item not in schema_invalid:
                    obligation_missing_refs[obligation].update(
                        reference for reference in node_references(by_id[item]) if reference not in by_id
                    )
        route = routes.get(obligation)
        if isinstance(route, dict):
            for values in route.values():
                if isinstance(values, list):
                    obligation_missing_refs[obligation].update(item for item in values if item not in by_id)
                    for item in values:
                        if item in by_id and item not in schema_invalid:
                            obligation_missing_refs[obligation].update(
                                reference for reference in node_references(by_id[item]) if reference not in by_id
                            )
        missing_refs.update(obligation_missing_refs[obligation])
    for missing in sorted(missing_refs):
        add_gap(gaps, "E_NODE_MISSING", "/registry/" + missing, "referenced binding is absent")

    expected_recipe_keys = authority_union
    union_mismatch = (
        not recipes_container_valid or not routes_container_valid
        or list(recipes) != expected_recipe_keys or list(routes) != expected_recipe_keys
    )
    if recipes_container_valid and list(recipes) != expected_recipe_keys:
        add_gap(gaps, "E_RECIPE_UNION", "/recipes", "recipe union/order differs")
    if routes_container_valid and list(routes) != expected_recipe_keys:
        add_gap(gaps, "E_ROUTE_UNION", "/routes", "route union/order differs")

    # Exact frozen route/trace descriptors are external authority, never a
    # candidate-provided notion of completeness.
    for obligation in authority_union:
        obligation_missing = obligation_missing_refs[obligation]
        authority = authority_by_id.get(obligation, {})
        steps = recipes.get(obligation)
        route = routes.get(obligation)
        steps_valid = isinstance(steps, list)
        route_valid = isinstance(route, dict) and set(route) == set(ROUTE_CATEGORIES)
        if recipes_container_valid and not steps_valid:
            add_gap(gaps, "E_RECIPE", f"/recipes/{obligation}", "missing recipe")
        if routes_container_valid and not route_valid:
            add_gap(gaps, "E_ROUTE_SCHEMA", f"/routes/{obligation}", "route categories differ")
        if not by_id:
            continue
        obligation_invalid: set[str] = set()
        for item in steps if steps_valid else []:
            if item in schema_invalid:
                obligation_invalid.add(item)
            elif item in by_id:
                obligation_invalid.update(ref for ref in node_references(by_id[item]) if ref in schema_invalid)
        expected_route_roles = authority.get("route_roles", {})
        expected_route_bindings = authority.get("route_bindings", {})
        for category in ROUTE_CATEGORIES if route_valid else []:
            route_items = route.get(category, [])
            actual_roles = [by_id[item]["role"] for item in route_items if item in by_id and item not in schema_invalid]
            route_invalid = {item for item in route_items if item in schema_invalid}
            for item in route_items:
                if item in by_id and item not in schema_invalid:
                    route_invalid.update(ref for ref in node_references(by_id[item]) if ref in schema_invalid)
            if not obligation_missing and not route_invalid and actual_roles != expected_route_roles.get(category):
                add_gap(gaps, "E_ROUTE_ROLES", f"/routes/{obligation}/{category}", "semantic binding roles differ")
            if not obligation_missing and not route_invalid:
                actual_bindings = [route_reference_descriptor(by_id[item], by_id) for item in route_items]
                if actual_bindings != expected_route_bindings.get(category):
                    add_gap(gaps, "E_ROUTE_BINDINGS", f"/routes/{obligation}/{category}", "literal/artifact/value bindings differ")
        executable_kinds = {"callable", "negative-control", "reflection", "runtime-resource"}
        invalid_recipe_kind = False
        descriptors: list[dict[str, Any]] = []
        for item in steps if steps_valid else []:
            if (
                item not in by_id or item in schema_invalid
                or any(ref not in by_id or ref in schema_invalid for ref in node_references(by_id[item]))
            ):
                continue
            if by_id[item].get("kind") not in executable_kinds:
                add_gap(gaps, "E_RECIPE_KIND", f"/recipes/{obligation}/{item}", "recipe step is not executable")
                invalid_recipe_kind = True
                continue
            descriptors.append(trace_descriptor(by_id[item], by_id))
        if (
            steps_valid and not obligation_missing and not obligation_invalid and not invalid_recipe_kind
            and descriptors != authority.get("trace")
        ):
            add_gap(gaps, "E_TRACE_CONTRACT", f"/recipes/{obligation}", "binding edges differ from frozen trace")

    # Per-kind semantics and exact-base API resolution.
    for node_id, row in by_id.items():
        if node_id in schema_invalid:
            continue
        kind = row.get("kind")
        path = "/registry/" + node_id
        if kind == "typed-literal":
            actual = literal_runtime_type(row.get("value"))
            if actual != row.get("value_type"):
                add_gap(gaps, "E_LITERAL_TYPE", path + "/value", "literal runtime type differs")
            expected_literal = authority_by_id.get("__literal_authority__", {}).get(row.get("role"))
            if expected_literal != {"value_type": row.get("value_type"), "value": row.get("value")}:
                add_gap(gaps, "E_LITERAL_AUTHORITY", path + "/value", "literal value differs from frozen authority")
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
            if api_model is None:
                continue
            signature = row.get("signature")
            if not isinstance(signature, str) or not signature:
                add_gap(gaps, "E_SIGNATURE", path + "/signature", "empty signature")
                continue
            catalog = catalog_row(api_model, signature)
            if catalog is None:
                add_gap(gaps, "E_SIGNATURE", path + "/signature", "signature absent from exact-base API")
                continue
            actual_names = api_model.get("parameters", {}).get(signature)
            if actual_names is None:
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
                if source is not None and not type_assignable(source.get("value_type"), item.get("type"), api_model):
                    add_gap(gaps, "E_ARG_SOURCE_TYPE", f"{path}/args/{index}/source", "source type is not assignable")
            owner_source = row.get("owner_source")
            if catalog["style"] == "instance":
                source = by_id.get(owner_source)
                if source is None or not type_assignable(source.get("value_type"), catalog["owner_type"], api_model):
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
                subject_sources = row.get("subject_sources") if isinstance(row.get("subject_sources"), list) else []
                control_args = row.get("args") if isinstance(row.get("args"), list) else []
                control_sources = [item.get("source") for item in control_args if isinstance(item, dict)]
                if control_sources != [operation_source, *subject_sources]:
                    add_gap(
                        gaps, "E_NEGATIVE_CONTROL_ARGS", path,
                        "ordered control args differ from operation/subject ownership metadata",
                    )
                output_row = by_id.get(row.get("output"))
                if output_row is not None and (
                    output_row.get("lifetime") != "operation" or output_row.get("owner_ref") != operation_source
                ):
                    add_gap(
                        gaps, "E_NEGATIVE_CONTROL_OWNER", path + "/output",
                        "control output is not owned by the exact operation",
                    )
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
                if api_model is not None and row.get("signature") in api_model.get("parameters", {}):
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
    def nested_authority_roles(value: Any) -> set[str]:
        values: set[str] = set()
        if isinstance(value, dict):
            for key, item in value.items():
                if key in {"role", "owner_role", "producer_role"} and nonempty_text(item):
                    values.add(item)
                else:
                    values.update(nested_authority_roles(item))
        elif isinstance(value, list):
            for item in value:
                values.update(nested_authority_roles(item))
        return values

    expected_roles: set[str] = set()
    missing_dependency_roles: set[str] = set()
    for obligation in authority_union:
        authority = authority_by_id.get(obligation, {})
        expected_roles.update(nested_authority_roles(authority))
        steps = recipes.get(obligation)
        trace = authority.get("trace") if isinstance(authority, dict) else None
        if isinstance(steps, list) and isinstance(trace, list):
            for index, node_id in enumerate(steps):
                if node_id not in by_id and index < len(trace) and isinstance(trace[index], dict):
                    dependency_roles = nested_authority_roles(trace[index])
                    dependency_roles.discard(trace[index].get("role"))
                    missing_dependency_roles.update(dependency_roles)
    for node_id in sorted(set(by_id) - reachable):
        row = by_id[node_id]
        direct_resolvable = (
            node_id not in schema_invalid
            and all(ref in by_id and ref not in schema_invalid for ref in node_references(row))
        )
        uncertain_authority_root = (
            (union_mismatch and row.get("role") in expected_roles)
            or row.get("role") in missing_dependency_roles
        )
        if direct_resolvable and not uncertain_authority_root:
            add_gap(gaps, "E_UNREACHABLE", "/registry/" + node_id, "node is outside every resolvable obligation closure")

    # Ordered recipes must materialize every argument/owner before use.
    literal_ids = {
        node_id for node_id, row in by_id.items()
        if row.get("kind") == "typed-literal" and node_id not in schema_invalid
    }
    for obligation in authority_union:
        steps = recipes.get(obligation)
        if not isinstance(steps, list):
            continue
        recipe_resolvable = all(
            node_id in by_id and node_id not in schema_invalid
            and all(ref in by_id and ref not in schema_invalid for ref in node_references(by_id[node_id]))
            for node_id in steps
        )
        if not recipe_resolvable:
            continue
        available = set(literal_ids)
        for index, node_id in enumerate(steps):
            row = by_id[node_id]
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


def execute_recipe(
    packet: dict[str, Any], product_root: Path, obligation: str, token: object, fault: str = "none",
    raw_events_only: bool = False,
) -> CompletionProof | list[dict[str, Any]]:
    # Capture controller primitives before loading product code.  The product is
    # confined to this worker and cannot replace the parent validator command path.
    safe_load_product_module = load_product_module
    safe_worker_value_assignable = worker_value_assignable
    safe_resolved_inside = resolved_inside
    safe_regular_file = regular_file
    safe_sha256_bytes = sha256_bytes
    safe_resolve_symbol = resolve_symbol
    completion_type = CompletionProof
    by_id = {row["id"]: row for row in packet["nodes"]}
    descriptor_by_id = {} if raw_events_only else {
        node_id: trace_descriptor(row, by_id)
        for node_id, row in by_id.items()
        if row.get("kind") in {"callable", "negative-control", "reflection", "runtime-resource"}
    }
    module = safe_load_product_module(packet, product_root)
    context: dict[str, Any] = {
        node_id: row["value"] for node_id, row in by_id.items() if row.get("kind") == "typed-literal"
    }
    trace: list[dict[str, Any]] = []
    raw_events: list[dict[str, Any]] = []
    gaps: list[Gap] = []

    def record(
        node_id: str, kind: str, outcome: str, return_type: str | None,
        owner_type: str | None, arg_types: list[str],
    ) -> None:
        if raw_events_only:
            raw_events.append(
                {
                    "node_id": node_id, "kind": kind, "outcome": outcome, "return_type": return_type,
                    "owner_type": owner_type, "arg_types": arg_types,
                }
            )
        else:
            trace.append(descriptor_by_id[node_id])

    for index, node_id in enumerate(packet["recipes"][obligation]):
        node = by_id[node_id]
        path = f"/runtime/{obligation}/{index}:{node_id}"
        kind = node["kind"]
        if kind == "runtime-resource":
            target = safe_resolved_inside(product_root, node["path"])
            if target is None or not safe_regular_file(target):
                add_gap(gaps, "E_RUNTIME_RESOURCE", path, "resource unavailable")
                continue
            raw = target.read_bytes()
            if len(raw) != node["size"] or safe_sha256_bytes(raw) != node["sha256"]:
                add_gap(gaps, "E_RUNTIME_RESOURCE", path, "resource identity changed")
                continue
            context[node["output"]] = raw
            record(node_id, kind, "returned", builtin_type_token("bytes"), None, [])
            continue

        if kind == "reflection":
            values: list[Any] = []
            reflection_arg_types: list[str] = []
            local_gap = False
            for item in node["args"]:
                value = context.get(item["source"])
                assignable, actual = safe_worker_value_assignable(value, item["type"], module, packet)
                if not assignable:
                    add_gap(gaps, "E_RUNTIME_ARG_TYPE", path + "/" + item["name"], actual or "foreign")
                    local_gap = True
                values.append(value)
                reflection_arg_types.append(actual or "foreign")
            if local_gap:
                continue
            try:
                if fault == "foreign-same-name-exception" and obligation == "OB-1":
                    foreign = type("AttributeError", (Exception,), {})
                    raise foreign("same-name")
                target = safe_resolve_symbol(module, node["signature"])
            except Exception as error:
                if type(error) is AttributeError:
                    record(
                        node_id, kind, "missing:" + builtin_type_token("AttributeError"),
                        None, None, reflection_arg_types,
                    )
                    continue
                add_gap(gaps, "E_REFLECTION_PRESENT", path, "foreign-exception-identity")
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
        actual_arg_types: list[str] = []
        local_gap = False
        actual_owner: str | None = None
        if node.get("owner_source"):
            owner = context.get(node["owner_source"])
            if fault == "foreign-same-name-owner" and obligation == "OB-1" and node_id == "call:ob1-step":
                owner = type("Core", (), {})()
            assignable, actual_owner = safe_worker_value_assignable(owner, node["owner_type"], module, packet)
            if not assignable:
                add_gap(gaps, "E_RUNTIME_OWNER", path + "/owner", actual_owner or "foreign")
                local_gap = True
        for item in node["args"]:
            value = context.get(item["source"])
            if (
                fault == "foreign-same-name-arg" and obligation == "OB-1"
                and node_id == "call:ob1-step" and item["name"] == "impulse"
            ):
                value = type("Impulse", (), {})()
            assignable, actual = safe_worker_value_assignable(value, item["type"], module, packet)
            if not assignable:
                add_gap(gaps, "E_RUNTIME_ARG_TYPE", path + "/" + item["name"], actual or "foreign")
                local_gap = True
            values.append(value)
            actual_arg_types.append(actual or "foreign")
        if local_gap:
            continue
        try:
            if fault == "product-sentinel" and obligation == "OB-1" and node_id == "call:ob1-calls-read":
                raise RuntimeError("BINDING_REACHED:copied")
            if node["style"] == "instance":
                target = getattr(context[node["owner_source"]], node["signature"].rsplit(".", 1)[1])
            else:
                target = safe_resolve_symbol(module, node["signature"])
            if (
                fault == "foreign-same-name-exception" and obligation == "OB-2"
                and node_id == "call:ob2-before-step"
            ):
                foreign = type("RouteFault", (Exception,), {})
                raise foreign("same-name")
            result = target(*values)
        except Exception as error:
            expected = node.get("expected_exception")
            expected_class = getattr(module, expected, None) if isinstance(expected, str) else None
            if expected in BUILTIN_RUNTIME_TYPES:
                expected_class = BUILTIN_RUNTIME_TYPES[expected]
            if expected and isinstance(expected_class, type) and type(error) is expected_class:
                record(
                    node_id, kind, "exception:" + declared_type_token(packet, expected),
                    None, actual_owner, actual_arg_types,
                )
                continue
            # Product-origin text can never impersonate validator completion.
            add_gap(gaps, "E_ROUTE_EXCEPTION", path, error.__class__.__name__ + ":" + str(error))
            continue
        if node.get("expected_exception"):
            add_gap(gaps, "E_EXPECTED_EXCEPTION", path, "route returned instead of materializing control")
            continue
        if fault == "foreign-same-name-return" and obligation == "OB-1" and node_id == "call:ob1-step":
            result = type("CellResult", (), {})()
        assignable, actual_return = safe_worker_value_assignable(result, node["return_type"], module, packet)
        if not assignable:
            add_gap(gaps, "E_RUNTIME_RETURN_TYPE", path, actual_return or "foreign")
            continue
        output = node.get("output")
        if output is not None:
            context[output] = result
        record(node_id, kind, "returned", actual_return, actual_owner, actual_arg_types)
    if gaps:
        raise ExecutionRejected(gaps)
    if raw_events_only:
        return raw_events
    return completion_type(token, obligation, tuple(trace))


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
    packet: dict[str, Any], product_root: Path, probe_path: Path, obligation: str, fault: str = "none"
) -> CompletionProof:
    execute = execute_recipe
    completion_type = CompletionProof
    namespace = load_probe_namespace(probe_path)
    function_name = "probe_" + obligation.replace("-", "_")
    function = namespace.get(function_name)
    if not inspect.isfunction(function):
        raise ExecutionRejected([Gap("E_FILTER_DISCOVERY", "/runtime/" + obligation, "probe function missing")])
    token = object()
    proof = function(lambda item, supplied: execute(packet, product_root, item, supplied, fault), token)
    if not isinstance(proof, completion_type) or proof.token is not token or proof.obligation != obligation:
        raise ExecutionRejected([Gap("E_COMPLETION_PROOF", "/runtime/" + obligation, "unforgeable proof missing")])
    return proof


def invoke_probe_events(
    packet: dict[str, Any], product_root: Path, probe_path: Path, obligation: str, fault: str = "none"
) -> list[dict[str, Any]]:
    namespace = load_probe_namespace(probe_path)
    function_name = "probe_" + obligation.replace("-", "_")
    function = namespace.get(function_name)
    if not inspect.isfunction(function):
        raise ExecutionRejected([Gap("E_FILTER_DISCOVERY", "/runtime/" + obligation, "probe function missing")])
    token = object()
    result = function(
        lambda item, supplied: execute_recipe(
            packet, product_root, item, supplied, fault, raw_events_only=True
        ),
        token,
    )
    if not isinstance(result, list) or any(not isinstance(item, dict) for item in result):
        raise ExecutionRejected([Gap("E_RAW_EVENT", "/runtime/" + obligation, "raw event list missing")])
    return result


def controller_declared_type_names(packet: dict[str, Any]) -> set[str]:
    names: set[str] = set(BUILTIN_RUNTIME_TYPES)
    for row in packet.get("nodes", []):
        if not isinstance(row, dict):
            continue
        for key in ("value_type", "owner_type", "return_type", "expected_exception"):
            if nonempty_text(row.get(key)):
                names.add(row[key])
        for item in row.get("args", []) if isinstance(row.get("args"), list) else []:
            if isinstance(item, dict) and nonempty_text(item.get("type")):
                names.add(item["type"])
    names.update(CONTROLLER_TYPE_PARENTS)
    for values in CONTROLLER_TYPE_PARENTS.values():
        names.update(values)
    return names


def controller_type_assignable(actual: Any, expected: Any, packet: dict[str, Any]) -> bool:
    if not isinstance(actual, str) or not isinstance(expected, str):
        return False
    for actual_name in controller_declared_type_names(packet):
        if actual != declared_type_token(packet, actual_name):
            continue
        return actual_name == expected or expected in CONTROLLER_TYPE_PARENTS.get(actual_name, set())
    return False


def controller_trace_from_events(
    packet: dict[str, Any], obligation: str, events: Any
) -> tuple[list[dict[str, Any]] | None, list[Gap]]:
    path = "/runtime/" + obligation + "/events"
    if not isinstance(events, list):
        return None, [Gap("E_RAW_EVENT", path, "raw events absent")]
    by_id = {row["id"]: row for row in packet["nodes"]}
    steps = packet["recipes"][obligation]
    gaps: list[Gap] = []
    if len(events) != len(steps):
        add_gap(gaps, "E_RAW_EVENT", path, "event count differs from recipe")
    for index, node_id in enumerate(steps):
        if index >= len(events):
            break
        event = events[index]
        event_path = f"{path}/{index}"
        expected_keys = {"node_id", "kind", "outcome", "return_type", "owner_type", "arg_types"}
        if not isinstance(event, dict) or set(event) != expected_keys:
            add_gap(gaps, "E_RAW_EVENT", event_path, "event schema differs")
            continue
        node = by_id[node_id]
        if event.get("node_id") != node_id or event.get("kind") != node.get("kind"):
            add_gap(gaps, "E_RAW_EVENT", event_path, "event identity differs")
            continue
        kind = node["kind"]
        expected_outcome = (
            "missing:" + builtin_type_token("AttributeError") if kind == "reflection"
            else "exception:" + declared_type_token(packet, node["expected_exception"])
            if node.get("expected_exception")
            else "returned"
        )
        if event.get("outcome") != expected_outcome:
            add_gap(gaps, "E_RAW_EVENT", event_path + "/outcome", "actual outcome differs")
        expected_args = node.get("args", []) if kind != "runtime-resource" else []
        actual_args = event.get("arg_types")
        if not isinstance(actual_args, list) or len(actual_args) != len(expected_args):
            add_gap(gaps, "E_RAW_EVENT", event_path + "/arg_types", "argument type vector differs")
        else:
            for arg_index, (actual, expected) in enumerate(zip(actual_args, expected_args)):
                if not controller_type_assignable(actual, expected["type"], packet):
                    add_gap(gaps, "E_RAW_EVENT", f"{event_path}/arg_types/{arg_index}", "argument type differs")
        expected_owner = node.get("owner_type") if node.get("style") == "instance" else None
        if expected_owner is None:
            if event.get("owner_type") is not None:
                add_gap(gaps, "E_RAW_EVENT", event_path + "/owner_type", "unexpected owner")
        elif not controller_type_assignable(event.get("owner_type"), expected_owner, packet):
            add_gap(gaps, "E_RAW_EVENT", event_path + "/owner_type", "owner type differs")
        expected_return = None if expected_outcome != "returned" else (
            "bytes" if kind == "runtime-resource" else node.get("return_type")
        )
        if expected_return is None:
            if event.get("return_type") is not None:
                add_gap(gaps, "E_RAW_EVENT", event_path + "/return_type", "exception returned a value")
        elif not controller_type_assignable(event.get("return_type"), expected_return, packet):
            add_gap(gaps, "E_RAW_EVENT", event_path + "/return_type", "return type differs")
    if gaps:
        return None, normalized_gaps(gaps)
    return [trace_descriptor(by_id[node_id], by_id) for node_id in steps], []


def runtime_dependency_gaps(
    rows: Any, packet: dict[str, Any], product_root: Path, probe_path: Path, obligation: str
) -> list[Gap]:
    gaps: list[Gap] = []
    if not isinstance(rows, list):
        return [Gap("E_RUNTIME_DEPENDENCY", "/runtime/" + obligation + "/dependencies", "manifest absent")]
    expected = {
        str(Path(item["path"]).resolve()).lower(): item["sha256"]
        for item in actual_toolchain()["dependencies"]
    }
    script = Path(__file__).resolve()
    expected[str(script).lower()] = file_sha256(script)
    selected_source = source_artifact(packet, product_root)
    if selected_source is None:
        return [Gap("E_RUNTIME_DEPENDENCY", "/runtime/" + obligation + "/dependencies", "source absent")]
    source_row, source_path = selected_source
    expected[str(source_path.resolve()).lower()] = source_row["sha256"]
    seen: set[str] = set()
    for index, item in enumerate(rows):
        path_key = f"/runtime/{obligation}/dependencies/{index}"
        if not isinstance(item, dict) or set(item) != {"path", "sha256"}:
            add_gap(gaps, "E_RUNTIME_DEPENDENCY", path_key, "dependency row schema differs")
            continue
        raw_path = item.get("path")
        digest = item.get("sha256")
        if not nonempty_text(raw_path) or not nonempty_text(digest):
            add_gap(gaps, "E_RUNTIME_DEPENDENCY", path_key, "dependency identity absent")
            continue
        path = Path(raw_path).resolve()
        key = str(path).lower()
        if key in seen:
            add_gap(gaps, "E_RUNTIME_DEPENDENCY", path_key, "duplicate dependency")
            continue
        seen.add(key)
        if key not in expected:
            add_gap(gaps, "E_RUNTIME_DEPENDENCY", path_key, "extra runtime dependency")
        elif expected[key] != digest or not regular_file(path) or file_sha256(path) != digest:
            add_gap(gaps, "E_RUNTIME_DEPENDENCY", path_key, "runtime dependency identity changed")
    missing = sorted(set(expected) - seen)
    if missing:
        add_gap(
            gaps, "E_RUNTIME_DEPENDENCY", "/runtime/" + obligation + "/dependencies",
            "missing exact dependencies: " + ",".join(missing),
        )
    return normalized_gaps(gaps)


def worker_product_exec(
    packet_path: Path, product_root: Path, probe_path: Path, obligation: str, fault: str
) -> int:
    try:
        packet = load_json(packet_path)
        if fault == "copied-trace-no-events":
            by_id = {row["id"]: row for row in packet["nodes"]}
            copied_trace = [trace_descriptor(by_id[node_id], by_id) for node_id in packet["recipes"][obligation]]
            print(
                json.dumps(
                    {"status": "PRODUCT_TRACE", "obligation": obligation, "trace": copied_trace}, sort_keys=True
                )
            )
            return 0
        events = invoke_probe_events(packet, product_root, probe_path, obligation, fault)
        dependencies = loaded_dependency_manifest()
        if fault == "dependencies-empty":
            dependencies = []
        elif fault == "dependency-omitted-one" and dependencies:
            dependencies = dependencies[1:]
        print(
            json.dumps(
                {
                    "status": "PRODUCT_EVENTS", "obligation": obligation, "events": events,
                    "dependencies": dependencies,
                },
                sort_keys=True,
            )
        )
        return 0
    except ExecutionRejected as error:
        print(json.dumps({"status": "PLAN_RED", "gaps": [item.row() for item in error.gaps]}, sort_keys=True))
        return VALIDATOR_RED
    except Exception as error:
        print(json.dumps({"status": "WORKER_ERROR", "error": error.__class__.__name__ + ":" + str(error)}, sort_keys=True))
        return HARNESS_FATAL


def controller_product_exec(
    packet_path: Path, product_root: Path, probe_path: Path, obligation: str, fault: str
) -> tuple[list[dict[str, Any]] | None, list[Gap], dict[str, Any]]:
    script = Path(__file__).resolve()
    interpreter = Path(sys.executable).resolve()
    argv = [
        str(interpreter), *ISOLATION_FLAGS, str(script), "--worker", "product-exec", str(packet_path),
        str(product_root), str(probe_path), obligation, fault,
    ]
    process, payload, observation = run_command(argv)
    observation["id"] = "product-exec:" + obligation
    if process.returncode == HARNESS_FATAL:
        raise HarnessError("product-exec fatal: " + process.stderr + process.stdout)
    if process.returncode == VALIDATOR_RED and payload and payload.get("status") == "PLAN_RED":
        gaps = [
            Gap(row["code"], row["path"], row.get("detail", ""))
            for row in payload.get("gaps", [])
            if isinstance(row, dict) and isinstance(row.get("code"), str) and isinstance(row.get("path"), str)
        ]
        return None, normalized_gaps(gaps), observation
    if (
        process.returncode != 0 or payload is None or payload.get("status") != "PRODUCT_EVENTS"
        or payload.get("obligation") != obligation or not isinstance(payload.get("events"), list)
    ):
        return None, [Gap("E_PRODUCT_EXEC", "/runtime/" + obligation, "product child result invalid")], observation
    observation["parsed"] = {
        key: copy.deepcopy(payload[key]) for key in ("status", "obligation", "events", "dependencies")
    }
    packet = load_json(packet_path)
    dependency_gaps = runtime_dependency_gaps(
        payload.get("dependencies"), packet, product_root, probe_path, obligation
    )
    if dependency_gaps:
        return None, dependency_gaps, observation
    trace, event_gaps = controller_trace_from_events(packet, obligation, payload["events"])
    if event_gaps:
        return None, event_gaps, observation
    return trace, [], observation


def worker_filter(packet_path: Path, product_root: Path, probe_path: Path, obligation: str, fault: str) -> int:
    try:
        criterion = criterion_for
        digest = sha256_bytes
        canonical = canonical_bytes
        dumps = json.dumps
        write_stdout = sys.stdout.write
        if fault == "filter-pass":
            write_stdout(dumps({"status": "PASS", "obligation": obligation}, sort_keys=True) + "\n")
            return 0
        trace, product_gaps, product_observation = controller_product_exec(
            packet_path, product_root, probe_path, obligation, fault
        )
        if product_gaps:
            raise ExecutionRejected(product_gaps)
        if trace is None:
            raise HarnessError("product trace absent without gaps")
        criterion_value = criterion(obligation, trace)
        if fault == "wrong-sentinel":
            criterion_value = "WRONG_SENTINEL"
        write_stdout(
            dumps(
                {
                    "status": "BINDING_SENTINEL", "obligation": obligation, "criterion": criterion_value,
                    "trace": trace, "trace_sha256": digest(canonical(trace)), "product_exec": product_observation,
                },
                sort_keys=True,
            ) + "\n"
        )
        return BINDING_SENTINEL_EXIT
    except ExecutionRejected as error:
        write_stdout(dumps({"status": "PLAN_RED", "gaps": [item.row() for item in error.gaps]}, sort_keys=True) + "\n")
        return VALIDATOR_RED
    except Exception as error:
        write_stdout(dumps({"status": "WORKER_ERROR", "error": error.__class__.__name__ + ":" + str(error)}, sort_keys=True) + "\n")
        return HARNESS_FATAL


def worker_union(packet_path: Path, product_root: Path, probe_path: Path, obligations: list[str], fault: str) -> int:
    try:
        criterion = criterion_for
        digest = sha256_bytes
        canonical = canonical_bytes
        dumps = json.dumps
        write_stdout = sys.stdout.write
        selected = obligations[:-1] if fault == "union-incomplete" else obligations
        rows: list[dict[str, Any]] = []
        gaps: list[Gap] = []
        for obligation in selected:
            try:
                trace, product_gaps, product_observation = controller_product_exec(
                    packet_path, product_root, probe_path, obligation, fault
                )
                if product_gaps:
                    raise ExecutionRejected(product_gaps)
                if trace is None:
                    raise HarnessError("product trace absent without gaps")
                rows.append(
                    {
                        "obligation": obligation,
                        "criterion": criterion(obligation, trace),
                        "trace": trace,
                        "trace_sha256": digest(canonical(trace)),
                        "product_exec": product_observation,
                    }
                )
            except ExecutionRejected as error:
                gaps.extend(error.gaps)
        if gaps:
            write_stdout(dumps({"status": "PLAN_RED", "gaps": [item.row() for item in normalized_gaps(gaps)]}, sort_keys=True) + "\n")
            return VALIDATOR_RED
        write_stdout(dumps({"status": "BINDING_SENTINEL_UNION", "rows": rows}, sort_keys=True) + "\n")
        return BINDING_SENTINEL_EXIT
    except Exception as error:
        write_stdout(dumps({"status": "WORKER_ERROR", "error": error.__class__.__name__ + ":" + str(error)}, sort_keys=True) + "\n")
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
    "schema", "case", "change_id", "product_root", "base_tree_sha256", "candidate", "observed_candidate", "planner_session",
    "validator_session", "testability", "candidate_event", "done_when", "spec", "acceptance_sha256", "toolchain",
    "contract_locator", "contract_authority", "contract_version", "product_contract_version",
    "product_contract_authority", "direction_tip_diagnostic",
}


def pin_row(root: Path, target: Path) -> dict[str, str]:
    relative = target.resolve().relative_to(root.resolve()).as_posix()
    return {
        "path": str(target.resolve()), "relative_path": relative,
        "mode": logical_mode(target), "sha256": file_sha256(target),
    }


def pinned_file(
    row: Any, root: Path, expected_relative: str, path: str, gaps: list[Gap]
) -> Path | None:
    if not isinstance(row, dict) or set(row) != {"path", "relative_path", "mode", "sha256"}:
        add_gap(gaps, "E_PIN_SCHEMA", path, "closed canonical relative path/mode/blob pin required")
        return None
    expected = (root / expected_relative).resolve()
    candidate = Path(str(row.get("path", "")))
    if row.get("relative_path") != expected_relative or not candidate.is_absolute() or candidate.resolve() != expected:
        add_gap(gaps, "E_PIN_PATH", path + "/path", "canonical handoff-relative path differs")
        return None
    if not regular_file(candidate):
        add_gap(gaps, "E_PIN_FILE", path + "/path", "pinned regular file absent")
        return None
    if row.get("mode") != logical_mode(candidate):
        add_gap(gaps, "E_PIN_MODE", path + "/mode", "pinned logical/git mode differs")
        return None
    if file_sha256(candidate) != row.get("sha256"):
        add_gap(gaps, "E_PIN_HASH", path + "/sha256", "pinned blob differs")
        return None
    return candidate


def reverify_immutable_inputs(
    pins: dict[str, dict[str, str]], gaps: list[Gap], stage: str
) -> bool:
    valid = True
    for label, row in pins.items():
        path = Path(row["path"])
        if (
            not regular_file(path) or logical_mode(path) != row["mode"]
            or file_sha256(path) != row["sha256"]
        ):
            add_gap(gaps, "E_IMMUTABLE_INPUT", "/immutable/" + label, "changed at " + stage)
            valid = False
    return valid


def validation_output(case: str, gaps: list[Gap], receipt: dict[str, Any] | None) -> int:
    normalized = normalized_gaps(gaps)
    if normalized:
        print(json.dumps({"case": case, "status": "PLAN_RED", "gaps": [item.row() for item in normalized]}, sort_keys=True))
        return VALIDATOR_RED
    if receipt is None:
        raise HarnessError("GREEN validation lacks receipt")
    print(json.dumps({"case": case, "status": "PLAN_GATED_GREEN", "receipt": receipt}, sort_keys=True))
    return 0


def product_exec_projection_valid(value: Any, obligation: str) -> bool:
    if not isinstance(value, dict) or not isinstance(value.get("parsed"), dict):
        return False
    parsed = value["parsed"]
    return (
        set(parsed) == {"status", "obligation", "events", "dependencies"}
        and parsed.get("status") == "PRODUCT_EVENTS" and parsed.get("obligation") == obligation
        and isinstance(parsed.get("events"), list) and bool(parsed["events"])
        and isinstance(parsed.get("dependencies"), list) and bool(parsed["dependencies"])
    )


def receipt_projection_gaps(value: Any, obligations: list[str]) -> list[Gap]:
    path = "/receipt/parsed_evidence"
    if not isinstance(value, dict) or set(value) != {"discovery_ids", "filters", "union"}:
        return [Gap("E_RECEIPT_PROJECTION", path, "closed parsed evidence projection required")]
    expected_ids = ["probe_" + item.replace("-", "_") for item in obligations]
    if value.get("discovery_ids") != expected_ids:
        return [Gap("E_RECEIPT_PROJECTION", path + "/discovery_ids", "discovery projection differs")]
    filters = value.get("filters")
    if not isinstance(filters, list) or len(filters) != len(obligations):
        return [Gap("E_RECEIPT_PROJECTION", path + "/filters", "one parsed filter row per obligation required")]
    for index, (obligation, row) in enumerate(zip(obligations, filters)):
        if (
            not isinstance(row, dict) or row.get("status") != "BINDING_SENTINEL"
            or row.get("obligation") != obligation or not isinstance(row.get("trace"), list)
            or not nonempty_text(row.get("criterion")) or not nonempty_text(row.get("trace_sha256"))
            or not product_exec_projection_valid(row.get("product_exec"), obligation)
        ):
            return [Gap("E_RECEIPT_PROJECTION", f"{path}/filters/{index}", "parsed filter/product evidence differs")]
    union = value.get("union")
    if not isinstance(union, dict) or union.get("status") != "BINDING_SENTINEL_UNION":
        return [Gap("E_RECEIPT_PROJECTION", path + "/union", "parsed union result absent")]
    rows = union.get("rows")
    if not isinstance(rows, list) or len(rows) != len(obligations):
        return [Gap("E_RECEIPT_PROJECTION", path + "/union/rows", "union row set differs")]
    for index, (obligation, row) in enumerate(zip(obligations, rows)):
        if (
            not isinstance(row, dict) or row.get("obligation") != obligation
            or not isinstance(row.get("trace"), list) or not nonempty_text(row.get("criterion"))
            or not nonempty_text(row.get("trace_sha256"))
            or not product_exec_projection_valid(row.get("product_exec"), obligation)
        ):
            return [Gap("E_RECEIPT_PROJECTION", f"{path}/union/rows/{index}", "nested union evidence differs")]
    return []


def validate_envelope(
    envelope_path: Path, fault: str, authority_seed_path: Path, authority_seed_mode: str,
    authority_seed_sha256: str,
) -> int:
    try:
        envelope_path = envelope_path.resolve()
        handoff_root = envelope_path.parent.parent
        if envelope_path != (handoff_root / "writer" / "binding-validator-call.json").resolve():
            raise HarnessError("validator envelope path is not canonical")
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
        expected_seed_path = (handoff_root / "writer" / "authority-seed.json").resolve()
        seed_valid = (
            authority_seed_path.is_absolute() and authority_seed_path.resolve() == expected_seed_path
            and regular_file(expected_seed_path) and logical_mode(expected_seed_path) == authority_seed_mode
            and file_sha256(expected_seed_path) == authority_seed_sha256
        )
        if not seed_valid:
            add_gap(gaps, "E_CONTRACT_SEED", "/authority-seed", "external canonical path/mode/blob pin differs")
            return validation_output(case, gaps, None)
        seed = load_json(expected_seed_path)
        live_contract = independently_resolve_authority(seed, gaps, "/authority-seed/resolver")
        if live_contract is None:
            return validation_output(case, gaps, None)
        set_active_authority(live_contract)
        if envelope.get("contract_locator") != CONTRACT_LOCATOR:
            add_gap(gaps, "E_CONTRACT_LOCATOR", "/envelope/contract_locator", "canonical authority locator differs")
        envelope_authority = envelope.get("contract_authority")
        if not authority_schema_valid(envelope_authority):
            add_gap(gaps, "E_CONTRACT_RESOLVER", "/envelope/contract_authority", "closed resolver row differs")
        elif authority_stable_projection(envelope_authority) != authority_stable_projection(live_contract):
            add_gap(gaps, "E_CONTRACT_AUTHORITY", "/envelope/contract_authority", "fresh remote authority differs")
        if envelope.get("contract_version") != live_contract["contract"]["current"]:
            add_gap(gaps, "E_CONTRACT_PACKET_VERSION", "/envelope/contract_version", "finalized packet is not current")
        compare_toolchain(envelope.get("toolchain"), gaps)

        product_root = Path(str(envelope.get("product_root", "")))
        if not product_root.is_absolute() or not product_root.is_dir():
            add_gap(gaps, "E_PRODUCT_ROOT", "/envelope/product_root", "product root absent")
            return validation_output(case, gaps, None)
        before_manifest = tree_manifest(product_root)
        before_observation = tree_observation(product_root)
        before_hash = sha256_bytes(canonical_bytes(before_manifest))
        checker_before = file_sha256(Path(__file__).resolve())
        actual_product_contract = product_contract_authority(product_root, gaps)
        if actual_product_contract is not None:
            if envelope.get("product_contract_authority") != actual_product_contract:
                add_gap(
                    gaps, "E_CONTRACT_PRODUCT_AUTHORITY", "/envelope/product_contract_authority",
                    "writer observation differs from actual product stamp",
                )
            actual_version = actual_product_contract["current"]
            if actual_version != live_contract["contract"]["current"] or envelope.get("product_contract_version") != actual_version:
                add_gap(
                    gaps, "E_CONTRACT_PRODUCT_VERSION", "/product/validation.config/synced_contract_version",
                    "actual product stamp, packet and live authority must be exactly equal",
                )
        if before_hash != envelope.get("base_tree_sha256"):
            add_gap(gaps, "E_BASE_IDENTITY", "/envelope/base_tree_sha256", "observed base differs")

        packet_path = pinned_file(
            envelope.get("testability"), handoff_root, "candidate/TESTABILITY.json", "/envelope/testability", gaps
        )
        event_path = pinned_file(
            envelope.get("candidate_event"), handoff_root, "writer/candidate-event.json",
            "/envelope/candidate_event", gaps,
        )
        done_path = pinned_file(
            envelope.get("done_when"), handoff_root, "authority/done_when.json", "/envelope/done_when", gaps
        )
        spec_path = pinned_file(
            envelope.get("spec"), handoff_root, "authority/spec.json", "/envelope/spec", gaps
        )
        if None in {packet_path, event_path, done_path, spec_path}:
            after_manifest = tree_manifest(product_root)
            if after_manifest != before_manifest:
                add_gap(gaps, "E_PRODUCT_WRITE", "/product", "tree changed during validation")
            return validation_output(case, gaps, None)

        immutable_pins: dict[str, dict[str, str]] = {
            "testability": {
                "path": str(packet_path), "mode": envelope["testability"]["mode"],
                "sha256": envelope["testability"]["sha256"],
            },
            "candidate-event": {
                "path": str(event_path), "mode": envelope["candidate_event"]["mode"],
                "sha256": envelope["candidate_event"]["sha256"],
            },
            "done-when": {
                "path": str(done_path), "mode": envelope["done_when"]["mode"],
                "sha256": envelope["done_when"]["sha256"],
            },
            "spec": {
                "path": str(spec_path), "mode": envelope["spec"]["mode"],
                "sha256": envelope["spec"]["sha256"],
            },
        }
        if actual_product_contract is not None:
            immutable_pins["product-config"] = {
                key: str(actual_product_contract[key]) for key in ("path", "mode", "sha256")
            }
        reverify_immutable_inputs(immutable_pins, gaps, "initial-load")

        packet = load_json(packet_path)
        event = load_json(event_path)
        done_when = load_json(done_path)
        frozen_spec = load_json(spec_path)
        acceptance_hash = sha256_bytes(done_path.read_bytes() + spec_path.read_bytes())
        if acceptance_hash != envelope.get("acceptance_sha256"):
            add_gap(gaps, "E_ACCEPTANCE_PIN", "/envelope/acceptance_sha256", "authority bytes differ")
        if not isinstance(packet, dict) or packet.get("acceptance_sha256") != acceptance_hash:
            add_gap(gaps, "E_ACCEPTANCE_PACKET", "/packet/acceptance_sha256", "candidate authority differs")
        planner_session = envelope.get("planner_session")
        validator_session = envelope.get("validator_session")
        if not nonempty_text(planner_session):
            add_gap(gaps, "E_SESSION_ID", "/envelope/planner_session", "nonempty planner session required")
        if not nonempty_text(validator_session):
            add_gap(gaps, "E_SESSION_ID", "/envelope/validator_session", "nonempty validator session required")
        if nonempty_text(planner_session) and nonempty_text(validator_session) and planner_session == validator_session:
            add_gap(gaps, "E_ROLE_INDEPENDENCE", "/envelope/validator_session", "planner self-validated")
        if not nonempty_text(envelope.get("candidate")) or not nonempty_text(envelope.get("observed_candidate")):
            add_gap(gaps, "E_CANDIDATE_ID", "/envelope/candidate", "nonempty external candidate identity required")
        if not isinstance(event, dict) or set(event) != {"candidate", "planner_session", "testability"}:
            add_gap(gaps, "E_CANDIDATE_EVENT", "/candidate_event", "event schema differs")
        else:
            if event.get("candidate") != envelope.get("candidate") or envelope.get("observed_candidate") != envelope.get("candidate"):
                add_gap(gaps, "E_STALE_CANDIDATE", "/envelope/candidate", "candidate/event/observation differ")
            if event.get("planner_session") != envelope.get("planner_session"):
                add_gap(gaps, "E_CANDIDATE_EVENT", "/candidate_event/planner_session", "planner identity differs")
            testability_pin = envelope.get("testability") if isinstance(envelope.get("testability"), dict) else {}
            expected_event_pin = {
                key: testability_pin.get(key) for key in ("relative_path", "mode", "sha256")
            }
            if event.get("testability") != expected_event_pin:
                add_gap(gaps, "E_CANDIDATE_EVENT", "/candidate_event/testability", "candidate packet pin differs")

        authority_change_values = [
            value.get("change_id") for value in (done_when, frozen_spec) if isinstance(value, dict)
        ]
        expected_change_id = (
            authority_change_values[0]
            if len(authority_change_values) == 2
            and nonempty_text(authority_change_values[0])
            and authority_change_values[0] == authority_change_values[1]
            else None
        )
        packet_change_id = packet.get("change_id") if isinstance(packet, dict) else None
        if (
            not nonempty_text(expected_change_id) or packet_change_id != expected_change_id
            or envelope.get("change_id") != expected_change_id
        ):
            add_gap(gaps, "E_CHANGE_ID", "/packet/change_id", "packet/envelope/frozen authority change ids differ")

        authority_union, authority_by_id = derive_authority(done_when, frozen_spec, gaps)
        _, reference_spec = embedded_reference_authority()
        authority_by_id["__planned_api__"] = reference_spec["planned_api"]
        authority_by_id["__literal_authority__"] = reference_spec["literal_authority"]
        api_model = static_api_model(packet, product_root, gaps)
        packet_gaps, _ = audit_packet(packet, product_root, authority_union, authority_by_id, api_model)
        gaps.extend(packet_gaps)

        observations: list[dict[str, Any]] = []
        parsed_evidence: dict[str, Any] = {"discovery_ids": None, "filters": [], "union": None}
        dynamic_gaps: list[Gap] = []
        controller_write_journal: list[dict[str, str]] = []
        generated_hash: str | None = None
        if not normalized_gaps(gaps):
            interpreter = Path(sys.executable).resolve()
            script = Path(__file__).resolve()
            with tempfile.TemporaryDirectory(prefix="v21-validator-") as scratch_raw:
                scratch = Path(scratch_raw)
                runtime_root = scratch / "product"
                copy_product_snapshot(product_root, runtime_root, before_manifest)
                if api_model is None:
                    raise HarnessError("static source model absent after GREEN audit")
                source_copy = runtime_root / api_model["path"]
                probe_root = scratch / "probes"
                probe_root.mkdir()
                probe_path = probe_root / "binding_probes.py"
                source = generated_probe_source(authority_union)
                if fault == "compile-failure":
                    source += "\ndef broken(:\n"
                probe_path.write_text(source, encoding="utf-8", newline="\n")
                generated_hash = file_sha256(probe_path)
                immutable_pins["probe"] = {
                    "path": str(probe_path.resolve()), "mode": logical_mode(probe_path),
                    "sha256": generated_hash,
                }

                compile_ok = False
                if fault == "skip-compile":
                    add_gap(dynamic_gaps, "E_COMPILE_SKIPPED", "/commands/compile", "compile command absent")
                else:
                    reverify_immutable_inputs(immutable_pins, dynamic_gaps, "pre-compile")
                    compile_argv = [
                        str(interpreter), *ISOLATION_FLAGS, "-m", "py_compile", str(source_copy), str(probe_path),
                    ]
                    process, _, observation = run_command(compile_argv)
                    observation["id"] = "compile"
                    observations.append(observation)
                    if process.returncode != 0:
                        add_gap(dynamic_gaps, "E_COMPILE_EXIT", "/commands/compile", "nonzero compiler exit")
                    else:
                        compile_ok = True
                    reverify_immutable_inputs(immutable_pins, dynamic_gaps, "post-compile")

                if compile_ok:
                    if fault == "probe-changed":
                        probe_path.write_text(probe_path.read_text(encoding="utf-8") + "\n", encoding="utf-8", newline="\n")
                    if file_sha256(probe_path) != generated_hash:
                        add_gap(dynamic_gaps, "E_PROBE_CHANGED", "/commands/probe_sha256", "probe changed between stages")

                    discovery_fault = fault if fault in {"discovery-zero", "discovery-duplicate"} else "none"
                    reverify_immutable_inputs(immutable_pins, dynamic_gaps, "pre-discovery")
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
                    else:
                        parsed_evidence["discovery_ids"] = copy.deepcopy(payload["ids"])
                    if fault == "toctou-post-discovery":
                        packet_path.write_bytes(packet_path.read_bytes() + b" ")
                    reverify_immutable_inputs(immutable_pins, dynamic_gaps, "post-discovery")

                    for obligation_index, obligation in enumerate(authority_union):
                        ob1_faults = {
                            "filter-pass", "wrong-sentinel", "product-sentinel", "copied-trace-no-events",
                            "dependencies-empty", "dependency-omitted-one", "foreign-same-name-return",
                            "foreign-same-name-arg", "foreign-same-name-owner",
                        }
                        target_obligation = "OB-2" if fault == "foreign-same-name-exception" else authority_union[0]
                        filter_fault = fault if obligation == target_obligation and (
                            fault in ob1_faults or fault == "foreign-same-name-exception"
                        ) else "none"
                        filter_argv = [
                            str(interpreter), *ISOLATION_FLAGS, str(script), "--worker", "filter", str(packet_path),
                            str(runtime_root), str(probe_path), obligation, filter_fault,
                        ]
                        reverify_immutable_inputs(immutable_pins, dynamic_gaps, "pre-filter:" + obligation)
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
                        parsed_evidence["filters"].append(copy.deepcopy(payload))
                        if fault == "toctou-mid-filter" and obligation_index == 0:
                            spec_path.write_bytes(spec_path.read_bytes() + b" ")
                        reverify_immutable_inputs(immutable_pins, dynamic_gaps, "post-filter:" + obligation)

                    union_fault = fault if fault in {"union-incomplete", "product-sentinel"} else "none"
                    if fault == "toctou-pre-union":
                        event_path.write_bytes(event_path.read_bytes() + b" ")
                    reverify_immutable_inputs(immutable_pins, dynamic_gaps, "pre-union")
                    union_argv = [
                        str(interpreter), *ISOLATION_FLAGS, str(script), "--worker", "union", str(packet_path),
                        str(runtime_root), str(probe_path), json.dumps(authority_union), union_fault,
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
                        actual_rows = payload.get("rows") if isinstance(payload.get("rows"), list) else []
                        semantic_rows = [
                            {key: row.get(key) for key in ("obligation", "criterion", "trace", "trace_sha256")}
                            for row in actual_rows if isinstance(row, dict)
                        ]
                        if payload.get("status") != "BINDING_SENTINEL_UNION" or semantic_rows != expected_rows:
                            add_gap(dynamic_gaps, "E_UNION_SET", "/commands/union/rows", "union is incomplete or differs")
                        else:
                            parsed_evidence["union"] = copy.deepcopy(payload)
                    reverify_immutable_inputs(immutable_pins, dynamic_gaps, "post-union")
                reverify_immutable_inputs(immutable_pins, dynamic_gaps, "final-execution")
            immutable_pins.pop("probe", None)

        if fault == "persistent-product-write":
            controller_write_journal.append({"action": "create", "path": "forbidden-write.txt"})
            (product_root / "forbidden-write.txt").write_text("forbidden", encoding="utf-8", newline="\n")
        elif fault == "transient-product-write":
            target = product_root / "fixture_api.py"
            before_stat = target.stat()
            controller_write_journal.append({"action": "append-truncate-restore-mtime", "path": "fixture_api.py"})
            with target.open("r+b") as stream:
                stream.seek(0, os.SEEK_END)
                stream.write(b"X")
                stream.flush()
                os.fsync(stream.fileno())
                stream.truncate(before_stat.st_size)
            os.utime(target, ns=(before_stat.st_atime_ns, before_stat.st_mtime_ns))

        gaps.extend(dynamic_gaps)
        reverify_immutable_inputs(immutable_pins, gaps, "pre-receipt")
        after_manifest = tree_manifest(product_root)
        after_observation = tree_observation(product_root)
        if after_observation != before_observation:
            add_gap(gaps, "E_PRODUCT_WRITE", "/product", "tree changed during read-only validation")
        if controller_write_journal:
            add_gap(gaps, "E_PRODUCT_WRITE", "/product", "controller write journal is nonempty")
        if file_sha256(Path(__file__).resolve()) != checker_before:
            add_gap(gaps, "E_TOOLCHAIN_CHANGED", "/toolchain/script_sha256", "checker changed during run")

        receipt = None
        receipt_evidence = copy.deepcopy(parsed_evidence)
        if fault == "receipt-evidence-omitted" and isinstance(receipt_evidence.get("filters"), list):
            if receipt_evidence["filters"]:
                receipt_evidence["filters"][0].pop("product_exec", None)
        if not normalized_gaps(gaps):
            gaps.extend(receipt_projection_gaps(receipt_evidence, authority_union))
        if not normalized_gaps(gaps):
            receipt_preimage = {
                "candidate": envelope["candidate"],
                "base_tree_sha256": before_hash,
                "acceptance_sha256": acceptance_hash,
                "testability_sha256": envelope["testability"]["sha256"],
                "candidate_event_sha256": envelope["candidate_event"]["sha256"],
                "handoff_pins": {
                    key: {
                        field: envelope[key][field] for field in ("relative_path", "mode", "sha256")
                    }
                    for key in ("testability", "candidate_event", "done_when", "spec")
                },
                "validator_session": envelope["validator_session"],
                "validator_pid": os.getpid(),
                "toolchain": actual_toolchain(),
                "generated_probe_sha256": generated_hash,
                "commands": observations,
                "parsed_evidence": receipt_evidence,
                "product_before_sha256": sha256_bytes(canonical_bytes(before_manifest)),
                "product_after_sha256": sha256_bytes(canonical_bytes(after_manifest)),
                "product_observation_before_sha256": sha256_bytes(canonical_bytes(before_observation)),
                "product_observation_after_sha256": sha256_bytes(canonical_bytes(after_observation)),
                "product_writes": controller_write_journal,
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
    "missing-fault-slot": "slot:ob2-fault-before",
    "missing-operation-slot": "slot:ob2-before-operation",
    "missing-golden-resource": "resource:golden-cell",
    "missing-codec": "call:ob1-codec",
    "missing-source-input": "call:ob3-source-input",
    "missing-hidden-observer": "call:ob2-after-after-hidden",
    "missing-owner-observer": "call:ob1-owner-read",
    "missing-audit-counter-observer": "call:ob2-after-after-counter",
    "missing-delegation-observer": "call:ob2-after-delegation-read",
    "missing-handler-type-ref": "call:ob1-handler-type",
    "missing-custom-kind-map": "call:ob1-custom-map",
    "missing-reaction-rules": "call:ob1-reaction-rules",
    "missing-reaction-handler": "call:ob2-reaction-handler",
    "missing-reaction-owner-observer": "call:ob2-reaction-owner-read",
    "missing-gas-scenario": "call:ob1-scenario",
    "missing-success-return-observer": "call:ob2-success-return-cell",
    "missing-success-scenario-observer": "call:ob2-success-scenario-read",
    "missing-success-loopback-plant": "call:ob2-success-loopback",
    "missing-success-loopback-action": "call:ob2-success-step",
    "missing-impulse-operation-control": "call:ob2-before-impulse-control",
    "missing-handler-operation-control": "call:ob2-before-handler-control",
    "missing-reaction-fault-control": "control:ob2-reaction-fault",
    "missing-reaction-impulse-control": "call:ob2-reaction-impulse-control",
    "missing-reaction-handler-control": "call:ob2-reaction-handler-control",
    "missing-source-fault-control": "control:ob3-source-fault",
    "missing-source-operation-control": "call:ob3-source-control",
}


CASE_NAMES = [
    "valid",
    "unrelated-tip-diagnostic",
    *MISSING_CASES,
    "two-independent-gaps",
    "mixed-missing-and-literal-gaps",
    "mixed-source-and-missing-gaps",
    "mixed-missing-and-unreachable",
    "mixed-missing-and-use-before-produce",
    "malformed-recipes-mixed-independent",
    "malformed-routes-mixed-source",
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
    "wrong-open-literal",
    "wrong-fault-phase-literal",
    "source-path-substitution",
    "product-imports-validator-main",
    "empty-authority-grammar",
    "empty-candidate-and-authority",
    "missing-signature-field",
    "nodes-not-list",
    "malformed-args",
    "wrong-change-id",
    "empty-planner-session",
    "null-validator-session",
    "handler-type-nickname-substitution",
    "wrong-custom-kind-edge",
    "wrong-scenario-source-edge",
    "wrong-success-observer-source",
    "wrong-reaction-control-operation",
    "wrong-source-control-operation",
    "wrong-impulse-control-subject",
    "wrong-handler-control-subject",
    "wrong-source-control-subject",
    "hostile-sys-getframe-authority",
    "hidden-unlisted-product-import",
    "malformed-source-catalog-args",
    "malformed-type-parent-row",
    "builtins-subscript-module-mutation",
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
    "transient-product-write",
    "wrong-base",
    "wrong-acceptance",
    "wrong-testability-pin",
    "same-bytes-wrong-pin-path",
    "wrong-pinned-mode",
    "old-finalized-contract-replay",
    "future-product-contract",
    "changed-contract-authority",
    "arbitrary-wt-ref",
    "wrong-remote-selection",
    "stale-authority-checkout",
    "stale-local-main-vs-remote-main",
    "arbitrary-local-contract",
    "fetch-unavailable",
    "arbitrary-contract-locator",
    "missing-product-stamp",
    "singleton-product-config",
    "extra-product-config",
    "old-actual-product-stamp",
    "tampered-product-stamp-observation",
    "fake-interpreter",
    "wrong-interpreter-hash",
    "wrong-version",
    "wrong-script-path",
    "wrong-script-hash",
    "missing-isolation-flag",
    "unlisted-dependency",
    "extra-toolchain-field",
    "dependencies-empty",
    "dependency-omitted-one",
    "compile-skipped",
    "compile-failure",
    "discovery-zero",
    "discovery-duplicate",
    "filter-pass",
    "wrong-sentinel",
    "copied-trace-no-events",
    "foreign-same-name-return",
    "foreign-same-name-arg",
    "foreign-same-name-owner",
    "foreign-same-name-exception",
    "receipt-evidence-omitted",
    "toctou-post-discovery",
    "toctou-mid-filter",
    "toctou-pre-union",
    "union-incomplete",
    "probe-changed",
]
GREEN_CASES = {"valid", "unrelated-tip-diagnostic"}


# Populated below with exact validator rows.  Keeping it separate from mutate_case
# prevents a broken/nonmaterialized mutation from satisfying its own oracle.
CASE_EXPECTED: dict[str, set[tuple[str, str]]] = {
    "valid": set(),
    "unrelated-tip-diagnostic": set(),
    "missing-public-create": {("E_NODE_MISSING", "/registry/reflect:ob1-create")},
    "missing-topology": {("E_NODE_MISSING", "/registry/call:ob1-topology")},
    "missing-face-impulse": {("E_NODE_MISSING", "/registry/call:ob1-impulse")},
    "missing-owned-handler": {("E_NODE_MISSING", "/registry/call:ob1-handler")},
    "missing-audit": {("E_NODE_MISSING", "/registry/call:ob1-audit-read")},
    "missing-loopback": {("E_NODE_MISSING", "/registry/call:ob2-before-loopback")},
    "missing-fault-selector-before": {("E_NODE_MISSING", "/registry/control:ob2-fault-before")},
    "missing-fault-selector-during": {("E_NODE_MISSING", "/registry/control:ob2-fault-during")},
    "missing-fault-selector-after": {("E_NODE_MISSING", "/registry/control:ob2-fault-after")},
    "missing-fault-slot": {("E_NODE_MISSING", "/registry/slot:ob2-fault-before")},
    "missing-operation-slot": {("E_NODE_MISSING", "/registry/slot:ob2-before-operation")},
    "missing-golden-resource": {("E_NODE_MISSING", "/registry/resource:golden-cell")},
    "missing-codec": {("E_NODE_MISSING", "/registry/call:ob1-codec")},
    "missing-source-input": {("E_NODE_MISSING", "/registry/call:ob3-source-input")},
    "missing-hidden-observer": {("E_NODE_MISSING", "/registry/call:ob2-after-after-hidden")},
    "missing-owner-observer": {("E_NODE_MISSING", "/registry/call:ob1-owner-read")},
    "missing-audit-counter-observer": {("E_NODE_MISSING", "/registry/call:ob2-after-after-counter")},
    "missing-delegation-observer": {("E_NODE_MISSING", "/registry/call:ob2-after-delegation-read")},
    "missing-handler-type-ref": {("E_NODE_MISSING", "/registry/call:ob1-handler-type")},
    "missing-custom-kind-map": {("E_NODE_MISSING", "/registry/call:ob1-custom-map")},
    "missing-reaction-rules": {("E_NODE_MISSING", "/registry/call:ob1-reaction-rules")},
    "missing-reaction-handler": {("E_NODE_MISSING", "/registry/call:ob2-reaction-handler")},
    "missing-reaction-owner-observer": {("E_NODE_MISSING", "/registry/call:ob2-reaction-owner-read")},
    "missing-gas-scenario": {("E_NODE_MISSING", "/registry/call:ob1-scenario")},
    "missing-success-return-observer": {("E_NODE_MISSING", "/registry/call:ob2-success-return-cell")},
    "missing-success-scenario-observer": {("E_NODE_MISSING", "/registry/call:ob2-success-scenario-read")},
    "missing-success-loopback-plant": {("E_NODE_MISSING", "/registry/call:ob2-success-loopback")},
    "missing-success-loopback-action": {("E_NODE_MISSING", "/registry/call:ob2-success-step")},
    "missing-impulse-operation-control": {("E_NODE_MISSING", "/registry/call:ob2-before-impulse-control")},
    "missing-handler-operation-control": {("E_NODE_MISSING", "/registry/call:ob2-before-handler-control")},
    "missing-reaction-fault-control": {("E_NODE_MISSING", "/registry/control:ob2-reaction-fault")},
    "missing-reaction-impulse-control": {("E_NODE_MISSING", "/registry/call:ob2-reaction-impulse-control")},
    "missing-reaction-handler-control": {("E_NODE_MISSING", "/registry/call:ob2-reaction-handler-control")},
    "missing-source-fault-control": {("E_NODE_MISSING", "/registry/control:ob3-source-fault")},
    "missing-source-operation-control": {("E_NODE_MISSING", "/registry/call:ob3-source-control")},
    "two-independent-gaps": {
        ("E_NODE_MISSING", "/registry/call:ob1-impulse"),
        ("E_NODE_MISSING", "/registry/call:ob3-source-input"),
    },
    "mixed-missing-and-literal-gaps": {
        ("E_NODE_MISSING", "/registry/call:ob1-impulse"),
        ("E_LITERAL_AUTHORITY", "/registry/lit:phase-before/value"),
        ("E_TRACE_CONTRACT", "/recipes/OB-2"),
    },
    "mixed-source-and-missing-gaps": {
        ("E_NODE_MISSING", "/registry/slot:ob2-fault-before"),
        ("E_ROUTE_BINDINGS", "/routes/OB-1/source"),
        ("E_ROUTE_BINDINGS", "/routes/OB-3/source"),
        ("E_SOURCE_MODULE", "/registry/source:fixture-api"),
    },
    "mixed-missing-and-unreachable": {
        ("E_LITERAL_AUTHORITY", "/registry/lit:unreachable/value"),
        ("E_NODE_MISSING", "/registry/call:ob3-source-input"),
        ("E_UNREACHABLE", "/registry/lit:unreachable"),
    },
    "mixed-missing-and-use-before-produce": {
        ("E_NODE_MISSING", "/registry/call:ob3-source-input"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
        ("E_USE_BEFORE_PRODUCE", "/recipes/OB-1/0"),
    },
    "malformed-recipes-mixed-independent": {
        ("E_LITERAL_AUTHORITY", "/registry/lit:phase-before/value"),
        ("E_LITERAL_AUTHORITY", "/registry/lit:unreachable/value"),
        ("E_NODE_MISSING", "/registry/call:ob3-source-input"),
        ("E_RECIPE_SCHEMA", "/recipes"),
        ("E_UNREACHABLE", "/registry/lit:unreachable"),
    },
    "malformed-routes-mixed-source": {
        ("E_ROUTE_SCHEMA", "/routes"),
        ("E_SOURCE_MODULE", "/registry/source:fixture-api"),
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
        ("E_ROUTE_SCHEMA", "/routes/OB-3"),
        ("E_ROUTE_UNION", "/routes"),
    },
    "kind-conflation": {("E_KIND", "/registry/call:ob1-handler/kind")},
    "empty-signature": {("E_NODE_SCHEMA", "/registry/call:ob1-impulse")},
    "unknown-signature": {
        ("E_SIGNATURE", "/registry/call:ob1-impulse/signature"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
    },
    "wrong-visibility": {
        ("E_CALLABLE_VISIBILITY", "/registry/call:ob1-impulse/visibility"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
    },
    "wrong-owner": {
        ("E_OWNER", "/registry/call:ob1-step/owner_source"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
    },
    "wrong-arg-name": {
        ("E_CALLABLE_ARGS", "/registry/call:ob1-impulse/args"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
    },
    "wrong-arg-type": {
        ("E_ARG_SOURCE_TYPE", "/registry/call:ob1-impulse/args/0/source"),
        ("E_CALLABLE_ARGS", "/registry/call:ob1-impulse/args"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
    },
    "same-type-source-swap": {("E_TRACE_CONTRACT", "/recipes/OB-1")},
    "wrong-open-literal": {
        ("E_LITERAL_AUTHORITY", "/registry/lit:room-open/value"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
        ("E_TRACE_CONTRACT", "/recipes/OB-2"),
        ("E_TRACE_CONTRACT", "/recipes/OB-3"),
    },
    "wrong-fault-phase-literal": {
        ("E_LITERAL_AUTHORITY", "/registry/lit:phase-before/value"),
        ("E_TRACE_CONTRACT", "/recipes/OB-2"),
    },
    "source-path-substitution": {
        ("E_SOURCE_MODULE", "/registry/source:fixture-api"),
        ("E_ROUTE_BINDINGS", "/routes/OB-1/source"),
        ("E_ROUTE_BINDINGS", "/routes/OB-2/source"),
        ("E_ROUTE_BINDINGS", "/routes/OB-3/source"),
    },
    "product-imports-validator-main": {
        ("E_SOURCE_PROCESS_ESCAPE", "/registry/source:fixture-api"),
        ("E_ROUTE_BINDINGS", "/routes/OB-1/source"),
        ("E_ROUTE_BINDINGS", "/routes/OB-2/source"),
        ("E_ROUTE_BINDINGS", "/routes/OB-3/source"),
    },
    "empty-authority-grammar": {("E_AUTHORITY_SPEC", "/authority/spec")},
    "empty-candidate-and-authority": {
        ("E_AUTHORITY_SPEC", "/authority/spec"),
        ("E_EMPTY_BINDING_CONTRACT", "/nodes"),
        ("E_SOURCE_COUNT", "/registry/source-artifact"),
    },
    "missing-signature-field": {("E_NODE_SCHEMA", "/registry/call:ob1-impulse")},
    "nodes-not-list": {
        ("E_NODE_SCHEMA", "/nodes"),
        ("E_SOURCE_COUNT", "/registry/source-artifact"),
    },
    "malformed-args": {("E_NODE_SCHEMA", "/registry/call:ob1-impulse")},
    "wrong-change-id": {("E_CHANGE_ID", "/packet/change_id")},
    "empty-planner-session": {("E_SESSION_ID", "/envelope/planner_session")},
    "null-validator-session": {("E_SESSION_ID", "/envelope/validator_session")},
    "handler-type-nickname-substitution": {
        ("E_LITERAL_AUTHORITY", "/registry/lit:handler-nickname/value"),
        ("E_LITERAL_TYPE", "/registry/lit:handler-nickname/value"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
    },
    "wrong-custom-kind-edge": {("E_TRACE_CONTRACT", "/recipes/OB-1")},
    "wrong-scenario-source-edge": {("E_TRACE_CONTRACT", "/recipes/OB-1")},
    "wrong-success-observer-source": {("E_TRACE_CONTRACT", "/recipes/OB-2")},
    "wrong-reaction-control-operation": {("E_TRACE_CONTRACT", "/recipes/OB-2")},
    "wrong-source-control-operation": {
        ("E_TRACE_CONTRACT", "/recipes/OB-3"),
        ("E_USE_BEFORE_PRODUCE", "/recipes/OB-3/23"),
    },
    "wrong-impulse-control-subject": {
        ("E_NEGATIVE_CONTROL_ARGS", "/registry/call:ob2-before-impulse-control"),
        ("E_TRACE_CONTRACT", "/recipes/OB-2"),
        ("E_USE_BEFORE_PRODUCE", "/recipes/OB-2/11"),
    },
    "wrong-handler-control-subject": {
        ("E_NEGATIVE_CONTROL_ARGS", "/registry/call:ob2-before-handler-control"),
        ("E_TRACE_CONTRACT", "/recipes/OB-2"),
        ("E_USE_BEFORE_PRODUCE", "/recipes/OB-2/12"),
    },
    "wrong-source-control-subject": {
        ("E_NEGATIVE_CONTROL_ARGS", "/registry/call:ob3-source-control"),
        ("E_TRACE_CONTRACT", "/recipes/OB-3"),
        ("E_USE_BEFORE_PRODUCE", "/recipes/OB-3/23"),
    },
    "hostile-sys-getframe-authority": {
        ("E_SOURCE_PROCESS_ESCAPE", "/registry/source:fixture-api"),
    },
    "hidden-unlisted-product-import": {
        ("E_SOURCE_PROCESS_ESCAPE", "/registry/source:fixture-api"),
    },
    "malformed-source-catalog-args": {
        ("E_SOURCE_CATALOG", "/registry/source:fixture-api/BINDING_API/fixture_api.Topology.two_room/3/0"),
    },
    "malformed-type-parent-row": {
        ("E_SOURCE_CATALOG", "/registry/source:fixture-api/TYPE_PARENTS/OwnedHandler"),
    },
    "builtins-subscript-module-mutation": {
        ("E_SOURCE_PROCESS_ESCAPE", "/registry/source:fixture-api"),
    },
    "wrong-return-type": {
        ("E_CALLABLE_RETURN_TYPE", "/registry/call:ob1-impulse/return_type"),
        ("E_RETURN_SLOT_TYPE", "/registry/call:ob1-impulse/output"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
    },
    "wrong-return-slot-type": {
        ("E_RETURN_SLOT_TYPE", "/registry/call:ob1-calls-read/output"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
    },
    "resource-path-escape": {
        ("E_RESOURCE_ESCAPE", "/registry/resource:golden-cell/path"),
        ("E_ROUTE_BINDINGS", "/routes/OB-1/skeleton"),
        ("E_ROUTE_BINDINGS", "/routes/OB-1/source"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
    },
    "resource-wrong-hash": {
        ("E_RESOURCE_HASH", "/registry/resource:golden-cell/sha256"),
        ("E_ROUTE_BINDINGS", "/routes/OB-1/skeleton"),
        ("E_ROUTE_BINDINGS", "/routes/OB-1/source"),
    },
    "resource-wrong-mode": {
        ("E_RESOURCE_MODE", "/registry/resource:golden-cell/mode"),
        ("E_ROUTE_BINDINGS", "/routes/OB-1/skeleton"),
        ("E_ROUTE_BINDINGS", "/routes/OB-1/source"),
    },
    "resource-wrong-size": {
        ("E_RESOURCE_SIZE", "/registry/resource:golden-cell/size"),
        ("E_ROUTE_BINDINGS", "/routes/OB-1/skeleton"),
        ("E_ROUTE_BINDINGS", "/routes/OB-1/source"),
    },
    "fault-owner-generic": {
        ("E_NEGATIVE_CONTROL_OWNER", "/registry/control:ob2-fault-before/output"),
        ("E_TRACE_CONTRACT", "/recipes/OB-2"),
    },
    "fault-cross-operation": {
        ("E_NEGATIVE_CONTROL_ARGS", "/registry/control:ob2-fault-before"),
        ("E_NEGATIVE_CONTROL_OWNER", "/registry/control:ob2-fault-before/output"),
        ("E_TRACE_CONTRACT", "/recipes/OB-2"),
        ("E_USE_BEFORE_PRODUCE", "/recipes/OB-2/10"),
    },
    "self-cycle": {
        ("E_GRAPH_CYCLE", "/registry/inst:ob1-core"),
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
    },
    "unreachable-node": {
        ("E_LITERAL_AUTHORITY", "/registry/lit:unreachable/value"),
        ("E_UNREACHABLE", "/registry/lit:unreachable"),
    },
    "duplicate-slot-producer": {
        ("E_DUPLICATE_PRODUCER", "/registry/slot:ob1-calls"),
        ("E_UNREACHABLE", "/registry/call:ob1-calls-read-duplicate"),
    },
    "use-before-produce": {
        ("E_TRACE_CONTRACT", "/recipes/OB-1"),
        ("E_USE_BEFORE_PRODUCE", "/recipes/OB-1/0"),
    },
    "api-declaration-mismatch": {
        ("E_API_DECLARATION", "/registry/call:ob1-calls-read/signature"),
        ("E_API_DECLARATION", "/registry/call:ob2-success-calls-read/signature"),
        ("E_ROUTE_BINDINGS", "/routes/OB-1/source"),
        ("E_ROUTE_BINDINGS", "/routes/OB-2/source"),
        ("E_ROUTE_BINDINGS", "/routes/OB-3/source"),
    },
    "route-copies-sentinel": {("E_ROUTE_EXCEPTION", "/runtime/OB-1/27:call:ob1-calls-read")},
    "actual-product-write": {("E_PRODUCT_WRITE", "/product")},
    "transient-product-write": {("E_PRODUCT_WRITE", "/product")},
    "wrong-base": {("E_BASE_IDENTITY", "/envelope/base_tree_sha256")},
    "wrong-acceptance": {("E_ACCEPTANCE_PIN", "/envelope/acceptance_sha256")},
    "wrong-testability-pin": {("E_PIN_HASH", "/envelope/testability/sha256")},
    "same-bytes-wrong-pin-path": {("E_PIN_PATH", "/envelope/testability/path")},
    "wrong-pinned-mode": {("E_PIN_MODE", "/envelope/done_when/mode")},
    "old-finalized-contract-replay": {
        ("E_CONTRACT_PACKET_VERSION", "/envelope/contract_version"),
        ("E_CONTRACT_PRODUCT_VERSION", "/product/validation.config/synced_contract_version"),
    },
    "future-product-contract": {
        ("E_CONTRACT_PRODUCT_VERSION", "/product/validation.config/synced_contract_version"),
    },
    "changed-contract-authority": {
        ("E_CONTRACT_AUTHORITY", "/envelope/contract_authority"),
    },
    "arbitrary-wt-ref": {("E_CONTRACT_RESOLVER", "/envelope/contract_authority")},
    "wrong-remote-selection": {("E_CONTRACT_AUTHORITY", "/envelope/contract_authority")},
    "stale-authority-checkout": {
        ("E_CONTRACT_AUTHORITY", "/authority-seed/resolver"),
        ("E_CONTRACT_AUTHORITY", "/envelope/contract_authority"),
        ("E_CONTRACT_CHECKER", "/authority-seed/resolver/checker"),
    },
    "stale-local-main-vs-remote-main": {
        ("E_CONTRACT_AUTHORITY", "/authority-seed/resolver"),
        ("E_CONTRACT_AUTHORITY", "/envelope/contract_authority"),
        ("E_CONTRACT_CHECKOUT", "/authority-seed/resolver/contract"),
        ("E_CONTRACT_PACKET_VERSION", "/envelope/contract_version"),
        ("E_CONTRACT_PRODUCT_VERSION", "/product/validation.config/synced_contract_version"),
    },
    "arbitrary-local-contract": {("E_CONTRACT_AUTHORITY", "/envelope/contract_authority")},
    "fetch-unavailable": {("E_CONTRACT_RESOLVER", "/authority-seed/resolver")},
    "arbitrary-contract-locator": {("E_CONTRACT_LOCATOR", "/envelope/contract_locator")},
    "missing-product-stamp": {("E_CONTRACT_PRODUCT_STAMP", "/product/validation.config")},
    "singleton-product-config": {("E_CONTRACT_PRODUCT_CONFIG", "/product/validation.config")},
    "extra-product-config": {("E_CONTRACT_PRODUCT_CONFIG", "/product/validation.config")},
    "old-actual-product-stamp": {
        ("E_CONTRACT_PRODUCT_VERSION", "/product/validation.config/synced_contract_version"),
    },
    "tampered-product-stamp-observation": {
        ("E_CONTRACT_PRODUCT_AUTHORITY", "/envelope/product_contract_authority"),
    },
    "fake-interpreter": {("E_TOOLCHAIN_INTERPRETER", "/toolchain/interpreter_path")},
    "wrong-interpreter-hash": {("E_TOOLCHAIN_INTERPRETER_HASH", "/toolchain/interpreter_sha256")},
    "wrong-version": {("E_TOOLCHAIN_VERSION", "/toolchain/interpreter_version")},
    "wrong-script-path": {("E_TOOLCHAIN_SCRIPT", "/toolchain/script_path")},
    "wrong-script-hash": {("E_TOOLCHAIN_SCRIPT_HASH", "/toolchain/script_sha256")},
    "missing-isolation-flag": {("E_TOOLCHAIN_FLAGS", "/toolchain/flags")},
    "unlisted-dependency": {("E_TOOLCHAIN_DEPENDENCIES", "/toolchain/dependencies")},
    "extra-toolchain-field": {("E_TOOLCHAIN_SCHEMA", "/packet/toolchain")},
    "dependencies-empty": {("E_RUNTIME_DEPENDENCY", "/runtime/OB-1/dependencies")},
    "dependency-omitted-one": {("E_RUNTIME_DEPENDENCY", "/runtime/OB-1/dependencies")},
    "compile-skipped": {("E_COMPILE_SKIPPED", "/commands/compile")},
    "compile-failure": {("E_COMPILE_EXIT", "/commands/compile")},
    "discovery-zero": {("E_DISCOVERY_SET", "/commands/discover/ids")},
    "discovery-duplicate": {("E_DISCOVERY_SET", "/commands/discover/ids")},
    "filter-pass": {("E_FILTER_PASS", "/commands/filter/OB-1")},
    "wrong-sentinel": {("E_FILTER_SENTINEL", "/commands/filter/OB-1")},
    "copied-trace-no-events": {("E_PRODUCT_EXEC", "/runtime/OB-1")},
    "foreign-same-name-return": {
        ("E_RUNTIME_RETURN_TYPE", "/runtime/OB-1/19:call:ob1-step"),
    },
    "foreign-same-name-arg": {
        ("E_RUNTIME_ARG_TYPE", "/runtime/OB-1/19:call:ob1-step/impulse"),
    },
    "foreign-same-name-owner": {
        ("E_RUNTIME_OWNER", "/runtime/OB-1/19:call:ob1-step/owner"),
    },
    "foreign-same-name-exception": {
        ("E_ROUTE_EXCEPTION", "/runtime/OB-2/19:call:ob2-before-step"),
    },
    "receipt-evidence-omitted": {
        ("E_RECEIPT_PROJECTION", "/receipt/parsed_evidence/filters/0"),
    },
    "toctou-post-discovery": {("E_IMMUTABLE_INPUT", "/immutable/testability")},
    "toctou-mid-filter": {("E_IMMUTABLE_INPUT", "/immutable/spec")},
    "toctou-pre-union": {("E_IMMUTABLE_INPUT", "/immutable/candidate-event")},
    "union-incomplete": {("E_UNION_SET", "/commands/union/rows")},
    "probe-changed": {
        ("E_IMMUTABLE_INPUT", "/immutable/probe"),
        ("E_PROBE_CHANGED", "/commands/probe_sha256"),
    },
}


def materialize_baseline(root: Path) -> CaseBundle:
    product_root = root / "product"
    (product_root / "resources").mkdir(parents=True)
    (product_root / "fixture_api.py").write_text(FIXTURE_SOURCE, encoding="utf-8", newline="\n")
    (product_root / "resources" / "golden-cell.json").write_bytes(GOLDEN_CELL)
    (product_root / "resources" / "golden-source.json").write_bytes(GOLDEN_SOURCE)
    write_product_stamp(product_root, live_contract_version())
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


def adopt_reviewed_source_profile(bundle: CaseBundle, source: str, hidden_helper: bool = False) -> None:
    (bundle.product_root / "fixture_api.py").write_text(source, encoding="utf-8", newline="\n")
    helper = bundle.product_root / "hidden_helper.py"
    if hidden_helper:
        helper.write_text(HIDDEN_HELPER_SOURCE, encoding="utf-8", newline="\n")
    elif helper.exists():
        helper.unlink()
    refresh_product_identities(bundle)
    bundle.done_when, bundle.spec = frozen_authority(bundle.packet)
    bundle.acceptance_hash = sha256_bytes(canonical_bytes(bundle.done_when) + canonical_bytes(bundle.spec))
    bundle.packet["acceptance_sha256"] = bundle.acceptance_hash


def mutate_case(bundle: CaseBundle, case: str) -> None:
    packet = bundle.packet
    if case == "valid":
        return
    if case == "unrelated-tip-diagnostic":
        bundle.envelope_overrides["direction_tip_diagnostic"] = "diagnostic-only:unrelated-tip-b"
        return
    if case in MISSING_CASES:
        remove_node(packet, MISSING_CASES[case])
        return
    if case == "two-independent-gaps":
        remove_node(packet, "call:ob1-impulse")
        remove_node(packet, "call:ob3-source-input")
    elif case == "mixed-missing-and-literal-gaps":
        remove_node(packet, "call:ob1-impulse")
        find_node(packet, "lit:phase-before")["value"] = "after"
    elif case == "mixed-source-and-missing-gaps":
        remove_node(packet, "slot:ob2-fault-before")
        source = find_node(packet, "source:fixture-api")
        source["path"] = "resources/golden-cell.json"
        source["module"] = "fixture_api"
        source["sha256"] = file_sha256(bundle.product_root / source["path"])
    elif case == "mixed-missing-and-unreachable":
        remove_node(packet, "call:ob3-source-input")
        add_literal(packet["nodes"], "lit:unreachable", "unreachable", "int", 9)
    elif case == "mixed-missing-and-use-before-produce":
        remove_node(packet, "call:ob3-source-input")
        steps = packet["recipes"]["OB-1"]
        steps.remove("call:ob1-handler")
        steps.insert(0, "call:ob1-handler")
    elif case == "malformed-recipes-mixed-independent":
        packet["recipes"] = []
        remove_node(packet, "call:ob3-source-input")
        find_node(packet, "lit:phase-before")["value"] = "after"
        add_literal(packet["nodes"], "lit:unreachable", "unreachable", "int", 9)
    elif case == "malformed-routes-mixed-source":
        packet["routes"] = "bad"
        source = find_node(packet, "source:fixture-api")
        source["path"] = "resources/golden-cell.json"
        source["module"] = "fixture_api"
        source["sha256"] = file_sha256(bundle.product_root / source["path"])
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
    elif case == "wrong-open-literal":
        find_node(packet, "lit:room-open")["value"] = "sealed"
    elif case == "wrong-fault-phase-literal":
        find_node(packet, "lit:phase-before")["value"] = "after"
    elif case == "source-path-substitution":
        source = find_node(packet, "source:fixture-api")
        source["path"] = "resources/golden-cell.json"
        source["module"] = "fixture_api"
        source["sha256"] = file_sha256(bundle.product_root / source["path"])
    elif case == "product-imports-validator-main":
        replace_fixture(
            bundle,
            "from dataclasses import dataclass",
            "from dataclasses import dataclass\nimport __main__\n__main__.run_command = lambda argv: None",
        )
    elif case == "empty-authority-grammar":
        for obligation in bundle.spec["obligations"]:
            obligation["trace"] = []
            obligation["route_roles"] = {category: [] for category in ROUTE_CATEGORIES}
            obligation["route_bindings"] = {category: [] for category in ROUTE_CATEGORIES}
        packet["acceptance_sha256"] = sha256_bytes(canonical_bytes(bundle.done_when) + canonical_bytes(bundle.spec))
    elif case == "empty-candidate-and-authority":
        for obligation in bundle.spec["obligations"]:
            obligation["trace"] = []
            obligation["route_roles"] = {category: [] for category in ROUTE_CATEGORIES}
            obligation["route_bindings"] = {category: [] for category in ROUTE_CATEGORIES}
        packet["nodes"] = []
        packet["recipes"] = {obligation: [] for obligation in packet["coverage"]}
        packet["routes"] = {
            obligation: {category: [] for category in ROUTE_CATEGORIES} for obligation in packet["coverage"]
        }
        packet["acceptance_sha256"] = sha256_bytes(canonical_bytes(bundle.done_when) + canonical_bytes(bundle.spec))
    elif case == "missing-signature-field":
        find_node(packet, "call:ob1-impulse").pop("signature")
    elif case == "nodes-not-list":
        packet["nodes"] = {}
    elif case == "malformed-args":
        find_node(packet, "call:ob1-impulse")["args"] = "bad"
    elif case == "wrong-change-id":
        packet["change_id"] = "other-change"
    elif case == "empty-planner-session":
        bundle.envelope_overrides["planner_session"] = ""
    elif case == "null-validator-session":
        bundle.envelope_overrides["validator_session"] = None
    elif case == "handler-type-nickname-substitution":
        add_literal(packet["nodes"], "lit:handler-nickname", "handler-nickname", "HandlerTypeRef", "OwnedHandler")
        find_node(packet, "call:ob1-custom-map")["args"][1]["source"] = "lit:handler-nickname"
    elif case == "wrong-custom-kind-edge":
        find_node(packet, "call:ob1-custom-map")["args"][0]["source"] = "lit:custom-kind-b"
    elif case == "wrong-scenario-source-edge":
        find_node(packet, "call:ob1-scenario")["args"][2]["source"] = "inst:ob1-source-input-alt"
    elif case == "wrong-success-observer-source":
        find_node(packet, "call:ob2-success-return-cell")["args"][0]["source"] = "inst:ob2-before-audit-before-result"
    elif case == "wrong-reaction-control-operation":
        find_node(packet, "call:ob2-reaction-handler-control")["args"][0]["source"] = "slot:ob2-success-operation"
        find_node(packet, "call:ob2-reaction-handler-control")["operation_source"] = "slot:ob2-success-operation"
        find_node(packet, "slot:ob2-reaction-handler-control")["owner_ref"] = "slot:ob2-success-operation"
    elif case == "wrong-source-control-operation":
        find_node(packet, "call:ob3-source-control")["args"][0]["source"] = "slot:ob2-success-operation"
        find_node(packet, "call:ob3-source-control")["operation_source"] = "slot:ob2-success-operation"
        find_node(packet, "slot:ob3-source-control")["owner_ref"] = "slot:ob2-success-operation"
    elif case == "wrong-impulse-control-subject":
        control = find_node(packet, "call:ob2-before-impulse-control")
        control["args"][1]["source"] = "inst:ob1-impulse"
    elif case == "wrong-handler-control-subject":
        control = find_node(packet, "call:ob2-before-handler-control")
        control["args"][1]["source"] = "inst:ob2-during-loopback"
    elif case == "wrong-source-control-subject":
        control = find_node(packet, "call:ob3-source-control")
        control["args"][1]["source"] = "inst:ob1-source-input-alt"
    elif case == "hostile-sys-getframe-authority":
        adopt_reviewed_source_profile(bundle, HOSTILE_FIXTURE_SOURCE)
    elif case == "hidden-unlisted-product-import":
        adopt_reviewed_source_profile(bundle, HIDDEN_IMPORT_FIXTURE_SOURCE, hidden_helper=True)
    elif case == "malformed-source-catalog-args":
        adopt_reviewed_source_profile(bundle, MALFORMED_CATALOG_FIXTURE_SOURCE)
    elif case == "malformed-type-parent-row":
        adopt_reviewed_source_profile(bundle, MALFORMED_PARENTS_FIXTURE_SOURCE)
    elif case == "builtins-subscript-module-mutation":
        adopt_reviewed_source_profile(bundle, BUILTINS_ESCAPE_FIXTURE_SOURCE)
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
        bundle.fault = "product-sentinel"
    elif case == "actual-product-write":
        bundle.fault = "persistent-product-write"
    elif case == "transient-product-write":
        bundle.fault = "transient-product-write"
    elif case == "wrong-base":
        bundle.envelope_overrides["base_tree_sha256"] = "0" * 64
    elif case == "wrong-acceptance":
        bundle.envelope_overrides["acceptance_sha256"] = "0" * 64
    elif case == "wrong-testability-pin":
        bundle.envelope_overrides["testability_sha256"] = "0" * 64
    elif case == "same-bytes-wrong-pin-path":
        alternate = bundle.root / "alternate" / "TESTABILITY.json"
        write_json(alternate, packet)
        bundle.envelope_overrides["testability.path"] = str(alternate.resolve())
        bundle.envelope_overrides["testability.relative_path"] = "alternate/TESTABILITY.json"
    elif case == "wrong-pinned-mode":
        bundle.envelope_overrides["done_when.mode"] = "100755"
    elif case == "old-finalized-contract-replay":
        bundle.envelope_overrides["contract_version"] = 20
        bundle.envelope_overrides["product_contract_version"] = 20
    elif case == "future-product-contract":
        write_product_stamp(bundle.product_root, 99)
        refresh_product_identities(bundle)
    elif case == "changed-contract-authority":
        bundle.envelope_overrides["contract_authority.checker.sha256"] = "0" * 64
    elif case == "arbitrary-wt-ref":
        bundle.envelope_overrides["contract_authority.ref"] = "refs/heads/wt/arbitrary"
    elif case == "wrong-remote-selection":
        bundle.envelope_overrides["contract_authority.remote_url"] = "C:/missing/not-canonical.git"
        bundle.envelope_overrides["contract_authority.repo_id"] = "local:C:/missing/not-canonical.git"
    elif case in {"stale-authority-checkout", "stale-local-main-vs-remote-main", "fetch-unavailable"}:
        bundle.envelope_overrides["direction_tip_diagnostic"] = "diagnostic-only:" + case
    elif case == "arbitrary-local-contract":
        bundle.envelope_overrides["contract_authority.contract.sha256"] = "0" * 64
    elif case == "arbitrary-contract-locator":
        bundle.envelope_overrides["contract_locator"] = "direction-os://arbitrary/CONTRACT_VERSION"
    elif case == "missing-product-stamp":
        (bundle.product_root / PRODUCT_STAMP_PATH).unlink()
        refresh_product_identities(bundle)
    elif case == "singleton-product-config":
        (bundle.product_root / PRODUCT_STAMP_PATH).write_bytes(
            canonical_bytes({"synced_contract_version": live_contract_version()})
        )
        refresh_product_identities(bundle)
    elif case == "extra-product-config":
        config_path = bundle.product_root / PRODUCT_STAMP_PATH
        config = load_json(config_path)
        config["unexpected"] = True
        config_path.write_bytes(canonical_bytes(config))
        refresh_product_identities(bundle)
    elif case == "old-actual-product-stamp":
        write_product_stamp(bundle.product_root, 20)
        refresh_product_identities(bundle)
    elif case == "tampered-product-stamp-observation":
        bundle.envelope_overrides["product_contract_authority.sha256"] = "0" * 64
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
        bundle.envelope_overrides["toolchain.dependencies"] = ["stdlib-only", "registry-source@base-manifest", "mystery.dll"]
    elif case == "extra-toolchain-field":
        packet["toolchain"]["unlisted_load"] = "C:/mystery.dll"
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
    elif case == "copied-trace-no-events":
        bundle.fault = "copied-trace-no-events"
    elif case in {
        "dependencies-empty", "dependency-omitted-one", "foreign-same-name-return",
        "foreign-same-name-arg", "foreign-same-name-owner", "foreign-same-name-exception",
        "receipt-evidence-omitted", "toctou-post-discovery", "toctou-mid-filter", "toctou-pre-union",
    }:
        bundle.fault = case
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
    elif any(key.startswith(prefix + ".") for prefix in ("testability", "candidate_event", "done_when", "spec")):
        parent, child = key.split(".", 1)
        envelope[parent][child] = value
    elif key.startswith("toolchain."):
        envelope["toolchain"][key.split(".", 1)[1]] = value
    elif key.startswith("contract_authority."):
        parts = key.split(".")[1:]
        target = envelope["contract_authority"]
        for part in parts[:-1]:
            if not isinstance(target.get(part), dict):
                raise HarnessError("cannot override absent contract authority field: " + key)
            target = target[part]
        target[parts[-1]] = value
    elif key.startswith("product_contract_authority."):
        if isinstance(envelope.get("product_contract_authority"), dict):
            envelope["product_contract_authority"][key.split(".", 1)[1]] = value
        else:
            raise HarnessError("cannot override absent product contract authority")
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
    packet_pin = pin_row(bundle.root, packet_path)
    event = {
        "candidate": "P-001",
        "planner_session": bundle.envelope_overrides.get("planner_session", "plan-author-001"),
        "testability": {
            key: packet_pin[key] for key in ("relative_path", "mode", "sha256")
        },
    }
    write_json(event_path, event)
    product_contract = product_contract_authority(bundle.product_root)
    envelope = {
        "schema": 1,
        "case": case,
        "change_id": bundle.packet.get("change_id"),
        "product_root": str(bundle.product_root.resolve()),
        "base_tree_sha256": tree_hash(bundle.product_root),
        "candidate": "P-001",
        "observed_candidate": "P-001",
        "planner_session": "plan-author-001",
        "validator_session": "plan-binding-validator-001",
        "testability": packet_pin,
        "candidate_event": pin_row(bundle.root, event_path),
        "done_when": pin_row(bundle.root, done_path),
        "spec": pin_row(bundle.root, spec_path),
        "acceptance_sha256": sha256_bytes(done_path.read_bytes() + spec_path.read_bytes()),
        "toolchain": actual_toolchain(),
        "contract_locator": CONTRACT_LOCATOR,
        "contract_authority": live_contract_authority(),
        "contract_version": live_contract_version(),
        "product_contract_version": product_contract["current"] if product_contract is not None else None,
        "product_contract_authority": product_contract,
        "direction_tip_diagnostic": "diagnostic-only:unrelated-tip-a",
    }
    for key, value in bundle.envelope_overrides.items():
        set_override(envelope, key, value)
    write_json(envelope_path, envelope)
    return envelope_path


def run_case(case: str, authority_seed_path: Path, enforce: bool = True) -> int:
    if case not in CASE_NAMES:
        print(json.dumps({"status": "HARNESS_FATAL", "error": "unknown case " + case}, sort_keys=True))
        return HARNESS_FATAL
    try:
        with tempfile.TemporaryDirectory(prefix="v21-case-") as root_raw:
            root = Path(root_raw)
            parent_seed = load_json(authority_seed_path)
            case_authority = materialize_case_authority(root / "authority-fixture", parent_seed)
            set_active_authority(case_authority)
            case_seed_path = root / "writer" / "authority-seed.json"
            write_json(case_seed_path, case_authority)
            bundle = materialize_baseline(root)
            before = semantic_fingerprint(bundle)
            mutate_case(bundle, case)
            after = semantic_fingerprint(bundle)
            if case == "valid" and before != after:
                raise HarnessError("valid case mutated")
            if case != "valid" and before == after:
                raise HarnessError("negative mutation did not materialize")
            envelope_path = finalize_bundle(bundle, case)
            if case == "unrelated-tip-diagnostic":
                advance_case_remote(case_authority, {"unrelated-tip.txt": b"advance\n"})
            elif case == "stale-authority-checkout":
                advance_case_remote(
                    case_authority,
                    {CHECKER_RELATIVE_PATH: Path(__file__).resolve().read_bytes() + b"\n# stale-checkout-fixture\n"},
                )
            elif case == "stale-local-main-vs-remote-main":
                contract_text = Path(__file__).resolve().with_name("CONTRACT_VERSION").read_text(encoding="utf-8")
                current_line = next(line for line in contract_text.splitlines() if line.startswith("current:"))
                mutated = contract_text.replace(current_line, "current: 999", 1).encode("utf-8")
                advance_case_remote(case_authority, {CONTRACT_RELATIVE_PATH: mutated})
            elif case == "fetch-unavailable":
                remote = Path(case_authority["remote_url"])
                remote.rename(remote.with_name(remote.name + ".offline"))
            script = Path(__file__).resolve()
            interpreter = Path(sys.executable).resolve()
            seed_mode = logical_mode(case_seed_path)
            seed_sha = file_sha256(case_seed_path)
            process = subprocess.run(
                [
                    str(interpreter), *ISOLATION_FLAGS, str(script), "--validate", str(envelope_path), bundle.fault,
                    str(case_seed_path.resolve()), seed_mode, seed_sha,
                ],
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
            expected_exit = 0 if case in GREEN_CASES else VALIDATOR_RED
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
            expected_status = "PLAN_GATED_GREEN" if case in GREEN_CASES else "PLAN_RED"
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


def run_parent_with_authority(authority: dict[str, Any], authority_ref_sha: str) -> int:
    script = Path(__file__).resolve()
    interpreter = Path(sys.executable).resolve()
    if len(CASE_NAMES) != len(set(CASE_NAMES)) or set(CASE_NAMES) != set(CASE_EXPECTED):
        print(json.dumps({"status": "V21_CONFORMANCE_FATAL", "error": "case/oracle registry mismatch"}, sort_keys=True))
        return HARNESS_FATAL
    outcomes: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="v21-parent-seed-") as seed_root_raw:
        seed_path = Path(seed_root_raw) / "authority-seed.json"
        write_json(seed_path, authority)
        for case in CASE_NAMES:
            process = subprocess.run(
                [
                    str(interpreter), *ISOLATION_FLAGS, str(script), "--case", case,
                    "--authority-seed", str(seed_path.resolve()),
                ],
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
            parent_error = None
            if rows != CASE_EXPECTED[case]:
                parent_error = "wrong exact rows"
            elif case in GREEN_CASES and case == "valid" and payload.get("materialized_before") != payload.get("materialized_after"):
                parent_error = "valid case mutated"
            elif case not in GREEN_CASES and payload.get("materialized_before") == payload.get("materialized_after"):
                parent_error = "negative did not materialize"
            if parent_error is not None:
                print(json.dumps({"status": "V21_CONFORMANCE_FATAL", "case": case, "error": parent_error}, sort_keys=True))
                return HARNESS_FATAL
            outcomes.append(payload)
    result = {
        "status": "V21_CONFORMANCE_GREEN",
        "interpreter_path": str(interpreter),
        "interpreter_sha256": file_sha256(interpreter),
        "interpreter_version": sys.version.split()[0],
        "isolation_flags": ISOLATION_FLAGS,
        "script_sha256": file_sha256(script),
        "checker_sha256": file_sha256(script),
        "authority_ref_sha": authority_ref_sha,
        "positive_cases": len(GREEN_CASES),
        "negative_cases": len(CASE_NAMES) - len(GREEN_CASES),
        "case_digest": sha256_bytes(canonical_bytes(outcomes)),
        "corpus_digest": sha256_bytes(canonical_bytes(outcomes)),
        "contour": [
            "case-child", "validator-child", "compile-child", "discover-child",
            "product-free-filter-controller-children", "product-exec-children", "union-controller-child",
        ],
    }
    print(json.dumps(result, sort_keys=True))
    return 0


def run_parent() -> int:
    try:
        with tempfile.TemporaryDirectory(prefix="v21-committed-authority-") as root_raw:
            authority, ref_sha = committed_candidate_authority(Path(root_raw))
            return run_parent_with_authority(authority, ref_sha)
    except HarnessError as error:
        print(json.dumps({"status": "V21_CONFORMANCE_FATAL", "error": str(error)}, sort_keys=True))
        return HARNESS_FATAL


def main(argv: list[str]) -> int:
    if not argv:
        return run_parent()
    if len(argv) == 4 and argv[0] in {"--case", "--raw-case"} and argv[2] == "--authority-seed":
        return run_case(argv[1], Path(argv[3]), enforce=argv[0] == "--case")
    if len(argv) == 2 and argv[0] in {"--dev-case", "--dev-raw-case"}:
        with tempfile.TemporaryDirectory(prefix="v21-dev-authority-") as root_raw:
            authority, _ = development_fixture_authority(Path(root_raw))
            seed_path = Path(root_raw) / "authority-seed.json"
            write_json(seed_path, authority)
            return run_case(argv[1], seed_path, enforce=argv[0] == "--dev-case")
    if len(argv) == 1 and argv[0] == "--dev-suite":
        with tempfile.TemporaryDirectory(prefix="v21-dev-authority-") as root_raw:
            authority, ref_sha = development_fixture_authority(Path(root_raw))
            return run_parent_with_authority(authority, ref_sha)
    if len(argv) == 6 and argv[0] == "--validate":
        return validate_envelope(Path(argv[1]), argv[2], Path(argv[3]), argv[4], argv[5])
    if len(argv) >= 2 and argv[0] == "--worker":
        mode = argv[1]
        if mode == "discover" and len(argv) == 4:
            return worker_discover(Path(argv[2]), argv[3])
        if mode == "product-exec" and len(argv) == 7:
            return worker_product_exec(Path(argv[2]), Path(argv[3]), Path(argv[4]), argv[5], argv[6])
        if mode == "filter" and len(argv) == 7:
            return worker_filter(Path(argv[2]), Path(argv[3]), Path(argv[4]), argv[5], argv[6])
        if mode == "union" and len(argv) == 7:
            obligations = json.loads(argv[5])
            if not isinstance(obligations, list) or any(not isinstance(item, str) for item in obligations):
                raise HarnessError("union obligation list invalid")
            return worker_union(Path(argv[2]), Path(argv[3]), Path(argv[4]), obligations, argv[6])
    print(
        "usage: v21_conformance.py [--dev-suite|--dev-case CASE|--dev-raw-case CASE|--worker ...]",
        file=sys.stderr,
    )
    return HARNESS_FATAL


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
