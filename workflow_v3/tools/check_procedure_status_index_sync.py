"""Validate registry procedure statuses against Workflow v3 index labels."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = REPO_ROOT / "workflow_v3/control_plane/PROCEDURE_REGISTRY.md"
INDEX_PATHS = [
    REPO_ROOT / "workflow_v3/README.md",
    REPO_ROOT / "workflow_v3/interfaces/99_COVERAGE_MATRIX.md",
    REPO_ROOT / "workflow_v3/completion/WORKFLOW_V3_COMPLETION_MATRIX.md",
    REPO_ROOT / "workflow_v3/completion/WORKFLOW_V3_REPOSITORY_COMPLETION_AUDIT.md",
]

REGISTRY_ROW_RE = re.compile(
    r"^\|\s*`(?P<entrypoint>[^`]+)`\s*\|\s*`(?P<ref>workflow_v3/procedures/[^`]+)`\s*\|"
)
STATUS_RE = re.compile(r"^status:\s*(?P<status>\S+)\s*$")

STALE_STUB_TERMS = (
    "pending-authoring stub",
    "procedure stub",
    "procedure stubs",
    "migration stub",
    "stub until separately migrated",
)
ACTIVE_LABEL_TERMS = (
    "active procedure",
    "active storage adapter procedure",
)
GLOBAL_FORBIDDEN_PHRASES = (
    "procedure stubs under `workflow_v3/procedures/**`",
    "migration stub until separately migrated",
)


@dataclass
class InventoryRow:
    entrypoint: str
    procedure_ref: str
    status: str
    index_label_findings: list[str] = field(default_factory=list)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_registry() -> list[tuple[str, str]]:
    refs: list[tuple[str, str]] = []
    for line in read_text(REGISTRY_PATH).splitlines():
        match = REGISTRY_ROW_RE.match(line)
        if match:
            refs.append((match.group("entrypoint"), match.group("ref")))
    return refs


def extract_status(path: Path) -> str | None:
    for line in read_text(path).splitlines():
        match = STATUS_RE.match(line)
        if match:
            return match.group("status")
    return None


def contains_any(text: str, terms: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(term in lowered for term in terms)


def next_section_status(line: str, current: str) -> str:
    lowered = line.strip().lower()
    if lowered.startswith("##"):
        if "stub reference" in lowered or "procedure stub reference" in lowered:
            return "stub"
        if "active procedure reference" in lowered:
            return "active"
        return "other"
    if "active procedure references:" in lowered:
        return "active"
    if "pending-authoring stub procedure references:" in lowered:
        return "stub"
    if "covered by canonical procedure stubs" in lowered:
        return "stub"
    return current


def label_contexts(index_path: Path, procedure_ref: str) -> list[tuple[int, str, str]]:
    basename = Path(procedure_ref).name
    contexts: list[tuple[int, str, str]] = []
    section_status = "other"
    for line_number, line in enumerate(read_text(index_path).splitlines(), start=1):
        section_status = next_section_status(line, section_status)
        if procedure_ref in line or basename in line:
            contexts.append((line_number, line, section_status))
    return contexts


def scan_index_labels(row: InventoryRow) -> list[str]:
    problems: list[str] = []
    ref_count = 0
    is_stub = row.status == "stub_procedure_pending_authoring"
    is_active = row.status.startswith("active_")

    for index_path in INDEX_PATHS:
        rel_index = index_path.relative_to(REPO_ROOT).as_posix()
        for line_number, line, section_status in label_contexts(index_path, row.procedure_ref):
            ref_count += 1
            lowered = line.lower()
            line_ref = f"{rel_index}:{line_number}"
            if is_active and (contains_any(lowered, STALE_STUB_TERMS) or section_status == "stub"):
                problems.append(
                    f"{line_ref} labels active `{row.procedure_ref}` with stale stub wording"
                )
            elif is_stub and (contains_any(lowered, ACTIVE_LABEL_TERMS) or section_status == "active"):
                problems.append(
                    f"{line_ref} labels stub `{row.procedure_ref}` as active"
                )

    if ref_count == 0:
        row.index_label_findings.append("no index refs")
    elif problems:
        row.index_label_findings.extend(problems)
    else:
        row.index_label_findings.append(f"{ref_count} index ref(s) OK")
    return problems


def scan_global_index_phrases() -> list[str]:
    problems: list[str] = []
    for index_path in INDEX_PATHS:
        rel_index = index_path.relative_to(REPO_ROOT).as_posix()
        for line_number, line in enumerate(read_text(index_path).splitlines(), start=1):
            lowered = line.lower()
            for phrase in GLOBAL_FORBIDDEN_PHRASES:
                if phrase in lowered:
                    problems.append(f"{rel_index}:{line_number} contains stale phrase `{phrase}`")
    matrix_text = read_text(REPO_ROOT / "workflow_v3/completion/WORKFLOW_V3_COMPLETION_MATRIX.md")
    if "workflow_v3/tools/check_procedure_status_index_sync.py" not in matrix_text:
        problems.append(
            "workflow_v3/completion/WORKFLOW_V3_COMPLETION_MATRIX.md does not mention the inventory check"
        )
    audit_text = read_text(REPO_ROOT / "workflow_v3/completion/WORKFLOW_V3_REPOSITORY_COMPLETION_AUDIT.md")
    if "Registry entry -> procedure file exists -> status -> index labels" not in audit_text:
        problems.append(
            "workflow_v3/completion/WORKFLOW_V3_REPOSITORY_COMPLETION_AUDIT.md lacks the status/index checklist"
        )
    return problems


def shorten(value: str, max_length: int) -> str:
    if len(value) <= max_length:
        return value
    return value[: max_length - 3] + "..."


def print_inventory(rows: list[InventoryRow]) -> None:
    headers = ("entrypoint", "procedure_ref", "status", "index_label_findings")
    widths = (32, 76, 32, 34)
    print("Procedure status/index inventory")
    print(
        "| "
        + " | ".join(header.ljust(width) for header, width in zip(headers, widths))
        + " |"
    )
    print("| " + " | ".join("-" * width for width in widths) + " |")
    for row in rows:
        findings = "; ".join(row.index_label_findings)
        values = (
            row.entrypoint,
            row.procedure_ref,
            row.status,
            findings,
        )
        print(
            "| "
            + " | ".join(shorten(value, width).ljust(width) for value, width in zip(values, widths))
            + " |"
        )


def main() -> int:
    registry_refs = parse_registry()
    rows: list[InventoryRow] = []
    problems: list[str] = []

    if not registry_refs:
        problems.append(f"No procedure refs found in {REGISTRY_PATH.relative_to(REPO_ROOT).as_posix()}")

    for entrypoint, procedure_ref in registry_refs:
        procedure_path = REPO_ROOT / procedure_ref
        if not procedure_path.exists():
            row = InventoryRow(entrypoint, procedure_ref, "MISSING")
            row.index_label_findings.append("missing procedure file")
            rows.append(row)
            problems.append(f"`{procedure_ref}` is missing")
            continue

        status = extract_status(procedure_path)
        row = InventoryRow(entrypoint, procedure_ref, status or "MISSING_STATUS")
        rows.append(row)
        if status is None:
            row.index_label_findings.append("missing top-level status")
            problems.append(f"`{procedure_ref}` has no top-level status line")
            continue

        problems.extend(scan_index_labels(row))

    problems.extend(scan_global_index_phrases())
    print_inventory(rows)

    if problems:
        print()
        print("Mismatches:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print()
    print("Procedure status/index sync check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
