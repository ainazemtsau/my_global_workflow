#!/usr/bin/env python3
"""
Read-only static validation checks for Workflow vNext-R runtime cleanup.

This script intentionally performs no writes.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, Literal


Status = Literal["PASS", "WARN", "FAIL", "INFO"]


ACTIVE_DIRECTIONS = [
    "workflow-governance",
    "solo-max-productive",
    "indie-game-development",
    "health-and-beauty",
]

REQUIRED_SHARED_RUNTIME_FILES = [
    "WORKFLOW_SOURCE_OF_TRUTH.md",
    "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md",
    "workflow/runtime/CONTEXT_ACQUISITION_POLICY.md",
    "workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md",
    "workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md",
    "workflow/stage_registry/STAGE_REGISTRY.md",
]

REQUIRED_DIRECTION_PROJECT_FILES = [
    "00_DIRECTION_START_HERE.md",
    "01_DIRECTION_STATE.md",
    "02_CURRENT_PHASE.md",
    "03_FOCUS_REGISTER.md",
    "04_ACTIVE_GOAL.md",
    "05_PORTFOLIO_QUEUE.md",
    "06_CONTEXT_LIBRARY_INDEX.md",
    "07_PHASE_MEMORY_INDEX.md",
    "08_DIRECTION_MAP.md",
]

DEPRECATED_PROMPT_DELIVERY_MODES = [
    "request_" "from_repository",
    "request\\_" "from\\_repository",
    "repository-request",
    "embedded_" "in_launch_card",
    "pasted_" "in_current_chat",
    "attached_" "export",
]

LEGACY_TRANSPORT_ACTIVE_SHAPE_TOKENS = [
    "stage_launch_card: 1",
    "stage_result_packet: 1",
    "card_type:",
    "packet_type:",
    "patch_type:",
    "codex_wave_card: 1",
]

LEGACY_TRANSPORT_COMPATIBILITY_FILES = {
    "workflow/transport/CODEX_RETURN_PACKET.md": [
        "packet_type: codex_return_packet",
        "schema: codex_return_packet.v1",
        "CODEX_RETURN_PACKET_BEGIN",
        "CODEX_RETURN_PACKET_END",
    ],
    "workflow/transport/CODEX_WAVE_CARD.md": [
        "codex_wave_card: 1",
        "CODEX_WAVE_CARD_BEGIN",
        "CODEX_WAVE_CARD_END",
        "allowed_targets",
        "forbidden_targets",
    ],
}

STALE_METADATA_PATTERNS = [
    "vNext-R REBUILD",
    "test-active",
    "rebuild root only",
    "Installed from roadmap step",
    "Step 7.",
]

REQUIRED_EOF_FILES = [
    "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md",
    "workflow/runtime/CONTEXT_ACQUISITION_POLICY.md",
    "workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md",
    "workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md",
    "workflow/stage_registry/STAGE_REGISTRY.md",
]

TERMINAL_ALLOWED_NEXT_TOKENS = {
    "Context Request",
    "Human Decision",
    "Stop",
}

SPECIAL_ALLOWED_NEXT_TOKENS = {
    "continue_current_stage": "B1_PROBLEM",
    "Direction pause/archive": "P9_PHASE_CLOSE",
}

ROUTER_ALLOWED_NEXT_PHRASE = "any appropriate stage"

FORBIDDEN_ALLOWED_NEXT_TOKENS = {
    "topology_launch_bundle",
    "codex_return",
}


@dataclass
class Finding:
    check_id: str
    name: str
    status: Status
    message: str
    path: str | None = None


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def markdown_files(root: Path) -> Iterable[Path]:
    skip_parts = {".git", ".venv", "node_modules", "__pycache__"}
    for path in root.rglob("*.md"):
        if any(part in skip_parts for part in path.parts):
            continue
        yield path


def stage_prompt_files(root: Path) -> list[Path]:
    prompt_dir = root / "workflow" / "stage_prompts"
    if not prompt_dir.exists():
        return []
    return sorted(prompt_dir.glob("*.md"))


def parse_registry_rows(root: Path) -> list[dict[str, str]]:
    path = root / "workflow/stage_registry/STAGE_REGISTRY.md"
    if not path.is_file():
        return []

    rows: list[dict[str, str]] = []
    for line in read_text(path).splitlines():
        if not line.startswith("| ") or "`workflow/stage_prompts/" not in line:
            continue

        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 8:
            continue

        rows.append(
            {
                "stage_id": cells[0],
                "stage_name": cells[1],
                "runtime_role": cells[2],
                "prompt_path": cells[3].strip("`"),
                "prompt_status": cells[4],
                "target_runtime": cells[5],
                "activation": cells[6],
                "allowed_next": cells[7],
            }
        )
    return rows


def split_allowed_next(value: str) -> list[str]:
    return [token.strip() for token in value.split(",") if token.strip()]


def add(results: list[Finding], check_id: str, name: str, status: Status, message: str, path: str | None = None) -> None:
    results.append(Finding(check_id=check_id, name=name, status=status, message=message, path=path))


def eof_marker_errors(path: Path, root: Path) -> list[str]:
    repo_path = rel(path, root)
    expected = f"END_OF_FILE: {repo_path}"
    text = read_text(path)
    marker_count = text.count(expected)
    errors: list[str] = []

    if marker_count != 1:
        errors.append(f"marker_count={marker_count}")

    stripped = text.rstrip()
    last_line = stripped.splitlines()[-1].strip() if stripped else ""
    normalized_last_line = last_line.strip("`")
    if normalized_last_line != expected:
        errors.append("marker_is_last_non_whitespace=false")
        if expected in stripped:
            errors.append("content_after_marker=true")

    return errors


def check_markdown_fence_balance(root: Path, results: list[Finding]) -> None:
    failures = 0
    for path in markdown_files(root):
        text = read_text(path)
        if text.count("```") % 2 != 0:
            failures += 1
            add(results, "CHECK 001", "markdown_fence_balance", "FAIL", "Unbalanced triple-backtick fence.", rel(path, root))
    if failures == 0:
        add(results, "CHECK 001", "markdown_fence_balance", "PASS", "All scanned markdown files have balanced triple-backtick fences.")


def check_required_shared_runtime_files(root: Path, results: list[Finding]) -> None:
    missing = []
    for item in REQUIRED_SHARED_RUNTIME_FILES:
        if not (root / item).is_file():
            missing.append(item)
            add(results, "CHECK 002", "required_shared_runtime_files_exist", "FAIL", "Required shared runtime file is missing.", item)
    if not missing:
        add(results, "CHECK 002", "required_shared_runtime_files_exist", "PASS", "All required shared runtime files exist.")


def check_active_direction_files(root: Path, results: list[Finding]) -> None:
    missing = []
    for direction in ACTIVE_DIRECTIONS:
        for filename in REQUIRED_DIRECTION_PROJECT_FILES:
            path = f"directions/{direction}/project_files/{filename}"
            if not (root / path).is_file():
                missing.append(path)
                add(results, "CHECK 003", "active_direction_00_08_exist", "FAIL", "Required Direction Project File is missing.", path)
    if not missing:
        add(results, "CHECK 003", "active_direction_00_08_exist", "PASS", "All active Direction Project Files 00-08 exist.")


def check_active_direction_project_instructions(root: Path, results: list[Finding]) -> None:
    missing = []
    for direction in ACTIVE_DIRECTIONS:
        path = f"directions/{direction}/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md"
        if not (root / path).is_file():
            missing.append(path)
            add(results, "CHECK 004", "active_direction_project_instructions_exist", "FAIL", "Direction Project Instructions file is missing.", path)
    if not missing:
        add(results, "CHECK 004", "active_direction_project_instructions_exist", "PASS", "All active Direction Project Instructions files exist.")


def check_registry_authority_markers(root: Path, results: list[Finding]) -> None:
    path = root / "workflow/stage_registry/STAGE_REGISTRY.md"
    if not path.is_file():
        add(results, "CHECK 005", "registry_authority_markers", "FAIL", "STAGE_REGISTRY.md missing.", rel(path, root))
        return

    text = read_text(path)
    required_terms = [
        "sole authority",
        "canonical stage IDs",
        "stage identity",
        "stage prompt path",
        "prompt status",
        "target runtime",
        "stage activation",
        "allowed_next",
    ]
    missing = [term for term in required_terms if term not in text]
    if missing:
        add(results, "CHECK 005", "registry_authority_markers", "FAIL", f"Registry authority markers missing: {', '.join(missing)}.", rel(path, root))
    else:
        add(results, "CHECK 005", "registry_authority_markers", "PASS", "Registry authority markers are present.", rel(path, root))


def check_runtime_core_no_duplicate_full_transition_table(root: Path, results: list[Finding]) -> None:
    path = root / "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
    if not path.is_file():
        add(results, "CHECK 006", "runtime_core_no_duplicate_full_transition_table", "FAIL", "Runtime core missing.", rel(path, root))
        return

    text = read_text(path)
    forbidden_table_hint = re.search(r"\|\s*stage[_ ]?id\s*\|.*\|\s*allowed_next\s*\|", text, flags=re.IGNORECASE)
    required_guard = "Do not maintain a transition table in this runtime core" in text

    if forbidden_table_hint:
        add(results, "CHECK 006", "runtime_core_no_duplicate_full_transition_table", "FAIL", "Runtime core appears to contain a full stage/allowed_next table.", rel(path, root))
    elif not required_guard:
        add(results, "CHECK 006", "runtime_core_no_duplicate_full_transition_table", "FAIL", "Runtime core duplicate-transition-table guard text is missing.", rel(path, root))
    else:
        add(results, "CHECK 006", "runtime_core_no_duplicate_full_transition_table", "PASS", "Runtime core does not appear to maintain a duplicate full transition table.", rel(path, root))


def check_registry_validation_rules(root: Path, results: list[Finding]) -> None:
    path = root / "workflow/stage_registry/STAGE_REGISTRY.md"
    if not path.is_file():
        add(results, "CHECK 007", "registry_validation_rules_present", "FAIL", "STAGE_REGISTRY.md missing.", rel(path, root))
        return

    text = read_text(path)
    required_fragments = [
        "Runtime core must not maintain a second full",
        "Stage prompts must not be treated as authority",
        "interface files, if present, are derived/reference",
        "Transport route fields, if present, are snapshots",
        "Terminal card types are not canonical stage IDs",
    ]
    missing = [fragment for fragment in required_fragments if fragment not in text]
    if missing:
        add(results, "CHECK 007", "registry_validation_rules_present", "FAIL", f"Registry validation rule fragments missing: {len(missing)}.", rel(path, root))
    else:
        add(results, "CHECK 007", "registry_validation_rules_present", "PASS", "Registry validation rule fragments are present.", rel(path, root))


def check_registry_present_prompt_files(root: Path, results: list[Finding]) -> None:
    path = root / "workflow/stage_registry/STAGE_REGISTRY.md"
    if not path.is_file():
        add(results, "CHECK 007A", "registry_present_prompt_files_exist", "FAIL", "STAGE_REGISTRY.md missing.", rel(path, root))
        return

    missing = []
    text = read_text(path)
    for line in text.splitlines():
        if not line.startswith("|") or "`workflow/stage_prompts/" not in line or "| present |" not in line:
            continue

        match = re.search(r"`(workflow/stage_prompts/[^`]+\.md)`", line)
        if not match:
            continue

        prompt_path = match.group(1)
        if not (root / prompt_path).is_file():
            missing.append(prompt_path)
            add(
                results,
                "CHECK 007A",
                "registry_present_prompt_files_exist",
                "FAIL",
                "Registry row marks prompt as present, but prompt file is missing.",
                prompt_path,
            )

    if not missing:
        add(results, "CHECK 007A", "registry_present_prompt_files_exist", "PASS", "All registry rows marked present have prompt files.")


def check_registry_allowed_next_tokens(root: Path, results: list[Finding]) -> None:
    check_id = "CHECK 007B"
    name = "registry_allowed_next_tokens"
    registry_path = root / "workflow/stage_registry/STAGE_REGISTRY.md"
    if not registry_path.is_file():
        add(results, check_id, name, "FAIL", "STAGE_REGISTRY.md missing.", rel(registry_path, root))
        return

    rows = parse_registry_rows(root)
    stage_ids = [row["stage_id"] for row in rows]
    stage_id_set = set(stage_ids)
    failures = 0

    for stage_id in sorted(stage_id_set):
        count = stage_ids.count(stage_id)
        if count != 1:
            failures += 1
            add(results, check_id, name, "FAIL", f"Canonical stage ID appears {count} times in registry: {stage_id}.", rel(registry_path, root))

    for row in rows:
        stage_id = row["stage_id"]
        for token in split_allowed_next(row["allowed_next"]):
            if token == ROUTER_ALLOWED_NEXT_PHRASE and stage_id == "ROUTER_STAGE_LAUNCHER":
                continue
            if token in stage_id_set:
                continue
            if token in TERMINAL_ALLOWED_NEXT_TOKENS:
                continue
            if token in SPECIAL_ALLOWED_NEXT_TOKENS:
                expected_stage = SPECIAL_ALLOWED_NEXT_TOKENS[token]
                if stage_id == expected_stage:
                    continue
                failures += 1
                add(
                    results,
                    check_id,
                    name,
                    "FAIL",
                    f"Special allowed_next token `{token}` is only allowed for {expected_stage}, not {stage_id}.",
                    rel(registry_path, root),
                )
                continue
            if token in FORBIDDEN_ALLOWED_NEXT_TOKENS:
                failures += 1
                add(results, check_id, name, "FAIL", f"Forbidden non-route token appears in allowed_next: {token}.", rel(registry_path, root))
                continue

            failures += 1
            add(results, check_id, name, "FAIL", f"Unknown allowed_next token for {stage_id}: {token}.", rel(registry_path, root))

    if failures == 0:
        add(results, check_id, name, "PASS", "All allowed_next tokens are canonical stage IDs, terminal outputs, or approved special tokens.")


def check_r0_recovery_prompt_status(root: Path, results: list[Finding]) -> None:
    check_id = "CHECK 007C"
    name = "r0_recovery_prompt_status"
    registry_path = root / "workflow/stage_registry/STAGE_REGISTRY.md"
    prompt_path = root / "workflow/stage_prompts/R0_RECOVERY_CLOSE.md"
    if not registry_path.is_file():
        add(results, check_id, name, "FAIL", "STAGE_REGISTRY.md missing.", rel(registry_path, root))
        return

    rows = [row for row in parse_registry_rows(root) if row["stage_id"] == "R0_RECOVERY_CLOSE"]
    if len(rows) != 1:
        add(results, check_id, name, "FAIL", f"Expected exactly one R0_RECOVERY_CLOSE registry row, found {len(rows)}.", rel(registry_path, root))
        return

    row = rows[0]
    status = row["prompt_status"]
    activation = row["activation"]
    exists = prompt_path.is_file()

    if status == "missing_prompt" and activation == "unavailable_until_prompt_installed" and not exists:
        add(results, check_id, name, "PASS", "R0_RECOVERY_CLOSE missing_prompt exception is valid.")
    elif status == "missing_prompt" and exists:
        add(results, check_id, name, "FAIL", "R0 prompt file exists while registry still marks missing_prompt.", rel(prompt_path, root))
    elif status == "present" and not exists:
        add(results, check_id, name, "FAIL", "R0 registry row is present but prompt file is missing.", rel(prompt_path, root))
    elif status == "present" and exists:
        add(results, check_id, name, "PASS", "R0 prompt file and present registry status are aligned.")
    else:
        add(results, check_id, name, "FAIL", f"Unexpected R0 registry status/activation combination: {status} / {activation}.", rel(registry_path, root))


def check_deprecated_prompt_delivery_modes(root: Path, results: list[Finding]) -> None:
    found = 0
    for path in stage_prompt_files(root):
        text = read_text(path)
        for token in DEPRECATED_PROMPT_DELIVERY_MODES:
            if token in text:
                found += 1
                add(results, "CHECK 008", "deprecated_prompt_delivery_modes_absent", "FAIL", f"Deprecated prompt delivery mode found: {token}.", rel(path, root))
    if found == 0:
        add(results, "CHECK 008", "deprecated_prompt_delivery_modes_absent", "PASS", "No deprecated prompt delivery modes found in stage prompts.")


def check_stage_prompt_forbidden_patterns(root: Path, results: list[Finding]) -> None:
    check_id = "CHECK 008A"
    name = "stage_prompt_forbidden_patterns"
    patterns = [
        ("deprecated prompt delivery", r"request\\?_from\\?_repository|repository-request"),
        ("direct-main maintenance policy", r"use direct-main repository maintenance policy|direct-main repository maintenance|direct_main|direct main"),
        ("stable downstream stage list", r"Stable downstream stage list"),
        ("stage-development testing override", r"Stage-development testing override"),
        ("first real direction test", r"First real Direction test"),
        ("testing status residue", r"Testing status"),
        ("prompt-local allowed_next field", r"^\s*allowed_next\s*:"),
        ("prompt-local allowed_next table", r"\|\s*stage[_ ]?id\s*\|.*\|\s*allowed_next\s*\|"),
        ("allowed next heading", r"^#{1,6}\s+Allowed next\b"),
        ("default downstream route heading", r"^#{1,6}\s+Default downstream route\b"),
    ]

    failures = 0
    for path in stage_prompt_files(root):
        text = read_text(path)
        for label, pattern in patterns:
            if re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
                failures += 1
                add(results, check_id, name, "FAIL", f"Forbidden stage prompt residue found: {label}.", rel(path, root))

    if failures == 0:
        add(results, check_id, name, "PASS", "No forbidden prompt delivery, direct-main, test residue, or prompt-local allowed_next authority patterns found.")


def check_stage_prompt_route_authority_residue(root: Path, results: list[Finding]) -> None:
    check_id = "CHECK 008B"
    name = "stage_prompt_route_authority_residue"
    rows = parse_registry_rows(root)
    allowed_by_stage = {row["stage_id"]: set(split_allowed_next(row["allowed_next"])) for row in rows}
    stage_ids = {row["stage_id"] for row in rows}
    prompt_stage_by_path = {
        Path(row["prompt_path"]).name: row["stage_id"]
        for row in rows
        if row["prompt_path"].startswith("workflow/stage_prompts/")
    }

    route_keywords = [
        "route to",
        "route directly to",
        "route back",
        "next route",
        "selected route",
        "normal route",
        "default route",
        "allowed route",
        "launch to",
        "launch card to",
        "emit a next launch",
        "may route",
        "must route",
        "should route",
    ]
    explicit_non_authority = [
        "registry_review_candidate",
        "not registry-valid",
        "not registry valid",
        "registry-valid fallback",
        "route conflict",
        "forbidden route",
        "do not emit",
        "do not route",
        "must not route",
        "not allowed",
        "unless registry",
        "desired owner",
        "unavailable",
        "do not invent",
        "source_state.from_stage",
    ]

    failures = 0
    for path in stage_prompt_files(root):
        current_stage = prompt_stage_by_path.get(path.name)
        if not current_stage or current_stage == "ROUTER_STAGE_LAUNCHER":
            continue

        allowed = allowed_by_stage.get(current_stage, set())
        for line_no, line in enumerate(read_text(path).splitlines(), 1):
            lowered = line.lower()
            if not any(keyword in lowered for keyword in route_keywords):
                continue

            mentioned_stage_ids = [stage_id for stage_id in stage_ids if stage_id in line]
            if not mentioned_stage_ids:
                continue

            if any(marker in lowered for marker in explicit_non_authority):
                continue

            for stage_id in mentioned_stage_ids:
                if stage_id == current_stage or stage_id in allowed:
                    continue
                failures += 1
                add(
                    results,
                    check_id,
                    name,
                    "FAIL",
                    f"Prompt appears to present non-registry route `{stage_id}` as normal/allowed/default at line {line_no}.",
                    rel(path, root),
                )

    if failures == 0:
        add(results, check_id, name, "PASS", "No prompt-local normal route examples conflict with registry allowed_next.")


def check_ad_wf_rt_001_boundary(root: Path, results: list[Finding]) -> None:
    prompts = stage_prompt_files(root)
    if not prompts:
        add(results, "CHECK 009", "ad_wf_rt_001_boundary_present", "FAIL", "No stage prompt files found.", "workflow/stage_prompts/")
        return

    missing = []
    for path in prompts:
        text = read_text(path)
        if "AD-WF-RT-001" not in text:
            missing.append(path)
            add(results, "CHECK 009", "ad_wf_rt_001_boundary_present", "FAIL", "AD-WF-RT-001 boundary missing.", rel(path, root))
    if not missing:
        add(results, "CHECK 009", "ad_wf_rt_001_boundary_present", "PASS", f"AD-WF-RT-001 boundary present in {len(prompts)} stage prompts.")


def check_legacy_transport_shapes(root: Path, results: list[Finding], mode: str) -> None:
    transport_dir = root / "workflow" / "transport"
    if not transport_dir.exists():
        add(results, "CHECK 010", "legacy_transport_shape_scan", "WARN" if mode == "baseline" else "FAIL", "workflow/transport/ directory is missing.", "workflow/transport/")
        return

    status: Status = "WARN" if mode == "baseline" else "FAIL"
    active_found = 0
    compatibility_hits = 0

    def is_legacy_compatibility_context(rel_path: str, lines: list[str], line_index: int, token: str) -> bool:
        allowed_terms = LEGACY_TRANSPORT_COMPATIBILITY_FILES.get(rel_path)
        if not allowed_terms:
            return False

        line = lines[line_index]
        if not any(term in line for term in allowed_terms):
            return False

        # Compatibility aliases must be in an explicitly marked compatibility section.
        # Scan backward to the nearest markdown H2/H3/H4 heading.
        for idx in range(line_index, -1, -1):
            heading = lines[idx].strip()
            if re.match(r"^#{2,4}\s+", heading):
                heading_lower = heading.lower()
                return "compatibility" in heading_lower or "legacy" in heading_lower

        return False

    for path in sorted(transport_dir.glob("*.md")):
        rel_path = rel(path, root)
        lines = read_text(path).splitlines()

        for line_index, line in enumerate(lines):
            for token in LEGACY_TRANSPORT_ACTIVE_SHAPE_TOKENS:
                if token not in line:
                    continue

                if is_legacy_compatibility_context(rel_path, lines, line_index, token):
                    compatibility_hits += 1
                    continue

                active_found += 1
                add(
                    results,
                    "CHECK 010",
                    "legacy_transport_shape_scan",
                    status,
                    f"Active legacy transport shape token found outside documented compatibility aliases: {token}.",
                    f"{rel_path}:{line_index + 1}",
                )

    if active_found == 0:
        if compatibility_hits:
            add(
                results,
                "CHECK 010",
                "legacy_transport_shape_scan",
                "PASS",
                f"No active legacy transport shape tokens found; {compatibility_hits} documented compatibility alias occurrence(s) tolerated.",
            )
        else:
            add(results, "CHECK 010", "legacy_transport_shape_scan", "PASS", "No legacy transport shape tokens found.")


def check_transport_apply_template(root: Path, results: list[Finding], mode: str) -> None:
    transport_dir = root / "workflow" / "transport"
    status: Status = "WARN" if mode == "baseline" else "FAIL"
    if not transport_dir.exists():
        add(results, "CHECK 011", "transport_apply_template_presence", status, "workflow/transport/ directory is missing.", "workflow/transport/")
        return

    found = False
    for path in sorted(transport_dir.glob("*.md")):
        if "codex_repository_maintenance_apply.v1" in read_text(path):
            found = True
            break

    if found:
        add(results, "CHECK 011", "transport_apply_template_presence", "PASS", "codex_repository_maintenance_apply.v1 transport template reference found.")
    else:
        add(results, "CHECK 011", "transport_apply_template_presence", status, "No dedicated codex_repository_maintenance_apply.v1 transport template/reference found under workflow/transport/.")


def check_prompt_eof_markers(root: Path, results: list[Finding], mode: str) -> None:
    prompts = stage_prompt_files(root)
    failures = 0
    for path in prompts:
        errors = eof_marker_errors(path, root)
        if errors:
            failures += 1
            add(results, "CHECK 012", "prompt_eof_markers", "FAIL", f"Stage prompt EOF marker is not structurally valid: {', '.join(errors)}.", rel(path, root))
    if failures == 0:
        add(results, "CHECK 012", "prompt_eof_markers", "PASS", "All stage prompts have exactly one EOF marker as the final marker line.")


def check_authority_eof_markers(root: Path, results: list[Finding]) -> None:
    failures = 0
    checked_paths: set[Path] = set()
    for item in REQUIRED_EOF_FILES:
        path = root / item
        if not path.is_file():
            add(results, "CHECK 013", "authority_eof_markers", "FAIL", "Required authority EOF file is missing.", item)
            failures += 1
            continue
        checked_paths.add(path)
        errors = eof_marker_errors(path, root)
        if errors:
            failures += 1
            add(results, "CHECK 013", "authority_eof_markers", "FAIL", f"Required authority EOF marker is not structurally valid: {', '.join(errors)}.", item)

    for path in sorted((root / "workflow/runtime").glob("*.md")):
        if path in checked_paths:
            continue
        if "END_OF_FILE:" not in read_text(path):
            continue
        errors = eof_marker_errors(path, root)
        if errors:
            failures += 1
            add(results, "CHECK 013", "authority_eof_markers", "FAIL", f"Runtime EOF marker is not structurally valid: {', '.join(errors)}.", rel(path, root))

    source_path = root / "WORKFLOW_SOURCE_OF_TRUTH.md"
    if source_path.is_file() and "END_OF_FILE:" not in read_text(source_path):
        add(results, "CHECK 013", "authority_eof_markers", "WARN", "WORKFLOW_SOURCE_OF_TRUTH.md lacks END_OF_FILE marker; current baseline treats this as non-blocking because the file is short.", "WORKFLOW_SOURCE_OF_TRUTH.md")

    if failures == 0:
        add(results, "CHECK 013", "authority_eof_markers", "PASS", "Required authority and runtime EOF markers are structurally valid.")


def check_stale_rebuild_metadata(root: Path, results: list[Finding]) -> None:
    scanned_roots = [
        root / "workflow",
        root / "directions",
        root / "docs",
    ]

    excluded_exact_paths = {
        "workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md",
    }

    excluded_prefixes = (
        "workflow/validation/",
    )

    def is_excluded_stale_metadata_path(path: Path) -> bool:
        rel_path = rel(path, root)

        if rel_path in excluded_exact_paths:
            return True

        if any(rel_path.startswith(prefix) for prefix in excluded_prefixes):
            return True

        if rel_path.startswith("directions/") and "/execution_logs/" in rel_path:
            return True

        return False

    found = 0
    for base in scanned_roots:
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            if ".git" in path.parts:
                continue
            if is_excluded_stale_metadata_path(path):
                continue

            text = read_text(path)
            for token in STALE_METADATA_PATTERNS:
                if token in text:
                    found += 1
                    add(results, "CHECK 014", "stale_rebuild_metadata", "WARN", f"Stale metadata token found: {token}.", rel(path, root))

    if found == 0:
        add(results, "CHECK 014", "stale_rebuild_metadata", "PASS", "No stale rebuild/test-active metadata tokens found in scanned runtime-facing markdown files.")


def check_prompt_schema_duplication(root: Path, results: list[Finding]) -> None:
    """Fail packet/proof/readiness schema bodies in stage prompts.

    Compact status fields such as `execution_readiness_status` and
    `next_action_proof_status` remain valid stage-specific obligations.
    """
    schema_patterns = [
        ("workflow_packet anchor", r"^\s*workflow_packet:\s*1\s*$"),
        ("stage_result.v1 schema", r"^\s*schema:\s*stage_result\.v1\s*$"),
        ("stage_launch.v1 schema", r"^\s*schema:\s*stage_launch\.v1\s*$"),
        ("repository_patch.v1 schema", r"^\s*schema:\s*repository_patch\.v1\s*$"),
        ("execution_log_entry.v1 schema", r"^\s*schema:\s*execution_log_entry\.v1\s*$"),
        ("context_request.v1 schema", r"^\s*schema:\s*context_request\.v1\s*$"),
        ("human_decision.v1 schema", r"^\s*schema:\s*human_decision\.v1\s*$"),
        ("stop.v1 schema", r"^\s*schema:\s*stop\.v1\s*$"),
        ("codex_return.v1 schema", r"^\s*schema:\s*codex_return\.v1\s*$"),
        ("horizon_acceptance_proof body", r"^horizon_acceptance_proof:\s*$"),
        ("active_frontier body", r"^active_frontier:\s*$"),
        ("next_action_proof body", r"^next_action_proof:\s*$"),
        ("minimum_sufficient_solution_proof body", r"^minimum_sufficient_solution_proof:\s*$"),
        ("audit_readiness body", r"^audit_readiness:\s*$"),
        ("research_readiness body", r"^research_readiness:\s*$"),
        ("execution_readiness body", r"^execution_readiness:\s*$"),
        ("allowed_next markdown table", r"\|\s*stage[_ ]?id\s*\|.*\|\s*allowed_next\s*\|"),
        ("legacy next launch format heading", r"Next Launch Card Required Format"),
    ]

    failures = 0
    for path in stage_prompt_files(root):
        text = read_text(path)
        matches: list[str] = []

        for label, pattern in schema_patterns:
            if re.search(pattern, text, flags=re.MULTILINE | re.IGNORECASE):
                matches.append(label)

        if matches:
            failures += 1
            add(
                results,
                "CHECK 015",
                "prompt_schema_duplication_scan",
                "FAIL",
                f"Stage prompt contains packet/proof schema body or route-table residue: {', '.join(matches[:5])}.",
                rel(path, root),
            )

    if failures == 0:
        add(results, "CHECK 015", "prompt_schema_duplication_scan", "PASS", "No packet/proof schema bodies or prompt-local route tables detected in stage prompts.")


def check_cross_direction_cache_setup(root: Path, results: list[Finding]) -> None:
    # Required files are already hard-checked in CHECK 003 and CHECK 004.
    manifest = root / "workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md"
    docs_setup = root / "docs/CHATGPT_PROJECT_SETUP.md"

    if not manifest.is_file():
        add(results, "CHECK 016", "cross_direction_cache_setup_consistency", "FAIL", "Runtime cache manifest missing.", rel(manifest, root))
        return

    manifest_text = read_text(manifest)
    missing_refs = []
    for direction in ACTIVE_DIRECTIONS:
        for filename in ("07_PHASE_MEMORY_INDEX.md", "08_DIRECTION_MAP.md"):
            if f"directions/{direction}/project_files/{filename}" not in manifest_text:
                missing_refs.append(f"{direction}/{filename}")
    if missing_refs:
        add(results, "CHECK 016", "cross_direction_cache_setup_consistency", "FAIL", f"Manifest missing active Direction cache references for: {', '.join(missing_refs)}.", rel(manifest, root))
    else:
        add(results, "CHECK 016", "cross_direction_cache_setup_consistency", "PASS", "Manifest references active Direction Project Files 00-08 including 08 Direction Map.")

    if docs_setup.is_file():
        docs_text = read_text(docs_setup)
        if "Workflow Governance" not in docs_text or "07_PHASE_MEMORY_INDEX.md" not in docs_text or "08_DIRECTION_MAP.md" not in docs_text:
            add(results, "CHECK 016", "cross_direction_cache_setup_consistency", "WARN", "docs/CHATGPT_PROJECT_SETUP.md appears stale versus current Workflow Governance/cache setup.", rel(docs_setup, root))
        else:
            add(results, "CHECK 016", "cross_direction_cache_setup_consistency", "PASS", "docs/CHATGPT_PROJECT_SETUP.md contains Workflow Governance, 07 Phase Memory, and 08 Direction Map references.")
    else:
        add(results, "CHECK 016", "cross_direction_cache_setup_consistency", "WARN", "docs/CHATGPT_PROJECT_SETUP.md missing.", rel(docs_setup, root))


def check_project_files_do_not_contain_stage_prompt_bodies(root: Path, results: list[Finding]) -> None:
    failures = 0
    embedded_prompt_tokens = [
        "schema: stage_prompt.v1",
        "Runtime Stage Prompt",
        "END_OF_FILE: workflow/stage_prompts/",
    ]
    default_load_markers = [
        "default project file",
        "default project files",
        "load by default",
        "always load",
        "default context",
    ]
    for direction in ACTIVE_DIRECTIONS:
        project_dir = root / "directions" / direction / "project_files"
        if not project_dir.exists():
            continue
        for file_name in REQUIRED_DIRECTION_PROJECT_FILES:
            path = project_dir / file_name
            if not path.is_file():
                continue
            text = read_text(path)
            if "workflow/stage_prompts/" not in text:
                continue

            if all(token in text for token in embedded_prompt_tokens):
                failures += 1
                add(results, "CHECK 017", "project_files_do_not_contain_stage_prompt_bodies", "FAIL", "Direction Project File appears to contain a stage prompt body.", rel(path, root))
                continue

            for line_no, line in enumerate(text.splitlines(), 1):
                lowered = line.lower()
                if "workflow/stage_prompts/" in line and any(marker in lowered for marker in default_load_markers):
                    failures += 1
                    add(
                        results,
                        "CHECK 017",
                        "project_files_do_not_contain_stage_prompt_bodies",
                        "FAIL",
                        f"Direction Project File appears to list a stage prompt as default-loaded context at line {line_no}.",
                        rel(path, root),
                    )

    if failures == 0:
        add(results, "CHECK 017", "project_files_do_not_contain_stage_prompt_bodies", "PASS", "No embedded stage prompt bodies or default-loaded stage prompt paths detected in active Direction Project Files 00-08.")


def check_interface_path_detection(root: Path, results: list[Finding]) -> None:
    old_path = root / "workflow/interfaces"
    actual_path = root / "workflow/stage_registry/interfaces"
    if old_path.exists():
        add(results, "CHECK 018", "interface_path_detection", "INFO", "workflow/interfaces/ exists.", rel(old_path, root))
    elif actual_path.exists():
        add(results, "CHECK 018", "interface_path_detection", "INFO", "workflow/interfaces/ is absent; interface files appear under workflow/stage_registry/interfaces/.", rel(actual_path, root))
    else:
        add(results, "CHECK 018", "interface_path_detection", "INFO", "No workflow interface directory detected.")


def check_codex_schema_regression(root: Path, results: list[Finding]) -> None:
    """Hard-check Codex Return/Wave canonical schema boundaries.

    This check prevents drift back to legacy Codex packet schema names in
    stage prompts and unauthorized runtime surfaces.
    """
    check_id = "CHECK 019"
    name = "codex_return_wave_schema_regression"
    failures = 0

    def require_anchors(file_path: str, anchors: list[str], description: str) -> None:
        nonlocal failures
        path = root / file_path
        if not path.is_file():
            failures += 1
            add(results, check_id, name, "FAIL", f"{description} file is missing.", file_path)
            return

        text = read_text(path)
        missing = [anchor for anchor in anchors if anchor not in text]
        if missing:
            failures += 1
            add(
                results,
                check_id,
                name,
                "FAIL",
                f"{description} missing required anchors: {', '.join(missing[:5])}.",
                file_path,
            )

    require_anchors(
        "workflow/transport/CODEX_RETURN_PACKET.md",
        [
            "workflow_packet: 1",
            "type: codex_return",
            "schema: codex_return.v1",
            "Legacy compatibility aliases",
            "schema: codex_return_packet.v1 -> schema: codex_return.v1",
        ],
        "Codex Return transport canonical schema",
    )

    require_anchors(
        "workflow/transport/CODEX_WAVE_CARD.md",
        [
            "workflow_packet: 1",
            "type: codex_wave",
            "schema: codex_wave.v1",
            "Legacy compatibility aliases",
            "codex_wave_card: 1 -> workflow_packet: 1 / type: codex_wave / schema: codex_wave.v1",
        ],
        "Codex Wave transport canonical schema",
    )

    require_anchors(
        "workflow/codex/CODEX_RETURN_PACKET_CONTRACT.md",
        [
            "Schema authority boundary",
            "workflow/transport/CODEX_RETURN_PACKET.md",
            "type: codex_return",
            "schema: codex_return.v1",
            "DONE claim rule",
        ],
        "Codex Return semantic contract",
    )

    require_anchors(
        "workflow/codex/CODEX_WAVE_CARD_CONTRACT.md",
        [
            "Schema authority boundary",
            "workflow/transport/CODEX_WAVE_CARD.md",
            "type: codex_wave",
            "schema: codex_wave.v1",
            "Task Master is never canonical for workflow content",
        ],
        "Codex Wave semantic contract",
    )

    require_anchors(
        "workflow/codex/WAVE_RECORD_TEMPLATE.md",
        [
            "Codex Wave/Return schema compatibility note",
            "codex_wave.v1",
            "codex_return.v1",
        ],
        "Wave Record schema compatibility note",
    )

    forbidden_prompt_tokens = [
        "codex_return_packet.v1",
        "packet_type: codex_return_packet",
        "CODEX_RETURN_PACKET_BEGIN",
        "CODEX_RETURN_PACKET_END",
        "codex_wave_card: 1",
        "CODEX_WAVE_CARD_BEGIN",
        "CODEX_WAVE_CARD_END",
        "allowed_targets:",
        "forbidden_targets:",
    ]

    for path in stage_prompt_files(root):
        text = read_text(path)
        for token in forbidden_prompt_tokens:
            if token in text:
                failures += 1
                add(
                    results,
                    check_id,
                    name,
                    "FAIL",
                    f"Legacy Codex schema token found in stage prompt: {token}.",
                    rel(path, root),
                )

    compatibility_allowed_paths = {
        "workflow/transport/CODEX_RETURN_PACKET.md",
        "workflow/transport/CODEX_WAVE_CARD.md",
        "workflow/codex/CODEX_RETURN_PACKET_CONTRACT.md",
        "workflow/codex/CODEX_WAVE_CARD_CONTRACT.md",
        "workflow/codex/WAVE_RECORD_TEMPLATE.md",
    }

    legacy_tokens = [
        "codex_return_packet.v1",
        "packet_type: codex_return_packet",
        "CODEX_RETURN_PACKET_BEGIN",
        "CODEX_RETURN_PACKET_END",
        "codex_wave_card: 1",
        "CODEX_WAVE_CARD_BEGIN",
        "CODEX_WAVE_CARD_END",
        "allowed_targets",
        "forbidden_targets",
    ]

    for base in [root / "workflow" / "transport", root / "workflow" / "codex"]:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            rel_path = rel(path, root)
            if rel_path in compatibility_allowed_paths:
                continue
            text = read_text(path)
            for token in legacy_tokens:
                if token in text:
                    failures += 1
                    add(
                        results,
                        check_id,
                        name,
                        "FAIL",
                        f"Legacy Codex schema token appears outside allowed compatibility files: {token}.",
                        rel_path,
                    )

    if failures == 0:
        add(
            results,
            check_id,
            name,
            "PASS",
            "Codex Return/Wave canonical schema anchors are present and no unauthorized legacy schema tokens were found.",
        )


def check_transport_authority_boundary(root: Path, results: list[Finding]) -> None:
    """Hard-check that transport schema authority boundary matches completed conversion."""
    check_id = "CHECK 020"
    name = "transport_authority_boundary"
    failures = 0

    required_anchors = {
        "workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md": [
            "Canonical packet schemas and transport templates",
            "workflow/transport/*.md",
            "Runtime core must not maintain full packet schema bodies",
        ],
        "workflow/stage_registry/STAGE_REGISTRY.md": [
            "Packet schema templates are owned by:",
            "workflow/transport/*.md",
            "Runtime packet-use behavior, formalization coupling, repository maintenance policy, and runtime precedence remain owned by:",
        ],
        "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md": [
            "Packet template authority boundary",
            "workflow/transport/*.md",
            "Runtime core remains authority for runtime behavior",
        ],
    }

    forbidden_stale_phrases = {
        "workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md": [
            "temporary: `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`; future cleanup may promote `workflow/transport/*.md` after canonical schema conversion",
            "Until `workflow/transport/*.md` is converted to canonical",
            "convert `workflow/transport/*.md` into canonical schema authority",
            "Runtime core may still contain compatibility examples or legacy embedded packet blocks",
        ],
        "workflow/stage_registry/STAGE_REGISTRY.md": [
            "Packet contracts live in `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md` until transport schemas are formally converted.",
            "Packet contracts live in `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md` until transport schemas are formally converted",
        ],
    }

    for file_path, anchors in required_anchors.items():
        path = root / file_path
        if not path.is_file():
            failures += 1
            add(results, check_id, name, "FAIL", "Required transport authority boundary file is missing.", file_path)
            continue

        text = read_text(path)
        missing = [anchor for anchor in anchors if anchor not in text]
        if missing:
            failures += 1
            add(
                results,
                check_id,
                name,
                "FAIL",
                f"Transport authority boundary anchors missing: {', '.join(missing[:5])}.",
                file_path,
            )

    for file_path, phrases in forbidden_stale_phrases.items():
        path = root / file_path
        if not path.is_file():
            continue

        text = read_text(path)
        for phrase in phrases:
            if phrase in text:
                failures += 1
                add(
                    results,
                    check_id,
                    name,
                    "FAIL",
                    f"Stale pre-transport-conversion authority wording remains: {phrase[:120]}",
                    file_path,
                )

    transport_required = {
        "workflow/transport/STAGE_LAUNCH_CARD.md": "schema: stage_launch.v1",
        "workflow/transport/STAGE_RESULT_PACKET.md": "schema: stage_result.v1",
        "workflow/transport/CONTEXT_REQUEST_CARD.md": "schema: context_request.v1",
        "workflow/transport/HUMAN_DECISION_CARD.md": "schema: human_decision.v1",
        "workflow/transport/REPOSITORY_PATCH.md": "schema: repository_patch.v1",
        "workflow/transport/CODEX_REPOSITORY_MAINTENANCE_APPLY.md": "schema: codex_repository_maintenance_apply.v1",
        "workflow/transport/CODEX_RETURN_PACKET.md": "schema: codex_return.v1",
        "workflow/transport/CODEX_WAVE_CARD.md": "schema: codex_wave.v1",
    }

    for file_path, anchor in transport_required.items():
        path = root / file_path
        if not path.is_file():
            failures += 1
            add(results, check_id, name, "FAIL", "Required canonical transport template is missing.", file_path)
            continue

        text = read_text(path)
        if "workflow_packet: 1" not in text or anchor not in text:
            failures += 1
            add(
                results,
                check_id,
                name,
                "FAIL",
                f"Canonical transport template anchor missing: workflow_packet: 1 / {anchor}.",
                file_path,
            )

    if failures == 0:
        add(
            results,
            check_id,
            name,
            "PASS",
            "Transport packet-template authority boundary is aligned with completed transport conversion.",
        )


def check_runtime_core_packet_schema_reference_cleanup(root: Path, results: list[Finding]) -> None:
    """Hard-check that runtime core no longer owns full packet schema bodies."""
    check_id = "CHECK 021"
    name = "runtime_core_packet_schema_reference_cleanup"
    failures = 0

    runtime_path = root / "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
    if not runtime_path.is_file():
        add(results, check_id, name, "FAIL", "Runtime core file is missing.", "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md")
        return

    text = read_text(runtime_path)

    required_references = [
        "workflow/transport/CONTEXT_REQUEST_CARD.md",
        "workflow/transport/HUMAN_DECISION_CARD.md",
        "workflow/transport/STAGE_LAUNCH_CARD.md",
        "workflow/transport/STAGE_RESULT_PACKET.md",
        "workflow/transport/REPOSITORY_PATCH.md",
        "workflow/transport/CODEX_REPOSITORY_MAINTENANCE_APPLY.md",
        "workflow/transport/EXECUTION_LOG_ENTRY.md",
        "workflow/transport/DOCUMENTATION_MAINTENANCE_GATE.md",
    ]

    missing_refs = [ref for ref in required_references if ref not in text]
    if missing_refs:
        failures += 1
        add(
            results,
            check_id,
            name,
            "FAIL",
            f"Runtime core missing canonical transport references: {', '.join(missing_refs[:5])}.",
            "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md",
        )

    full_body_patterns = [
        ("context_request", r"workflow_packet:\s*1\s*\n\s*type:\s*context_request\s*\n\s*schema:\s*context_request\.v1"),
        ("human_decision", r"workflow_packet:\s*1\s*\n\s*type:\s*human_decision\s*\n\s*schema:\s*human_decision\.v1"),
        ("stage_launch", r"workflow_packet:\s*1\s*\n\s*type:\s*stage_launch\s*\n\s*schema:\s*stage_launch\.v1"),
        ("stage_result", r"workflow_packet:\s*1\s*\n\s*type:\s*stage_result\s*\n\s*schema:\s*stage_result\.v1"),
        ("repository_patch", r"workflow_packet:\s*1\s*\n\s*type:\s*repository_patch\s*\n\s*schema:\s*repository_patch\.v1"),
        ("codex_repository_maintenance_apply", r"workflow_packet:\s*1\s*\n\s*type:\s*codex_repository_maintenance_apply\s*\n\s*schema:\s*codex_repository_maintenance_apply\.v1"),
        ("execution_log_entry", r"workflow_packet:\s*1\s*\n\s*(?:type|packet_type):\s*execution_log_entry\s*\n\s*schema:\s*execution_log_entry\.v1"),
        ("documentation_maintenance_gate", r"workflow_packet:\s*1\s*\n\s*(?:type|packet_type):\s*documentation_maintenance_gate\s*\n\s*schema:\s*documentation_maintenance_gate\.v1"),
    ]

    for label, pattern in full_body_patterns:
        if re.search(pattern, text, flags=re.MULTILINE):
            failures += 1
            add(
                results,
                check_id,
                name,
                "FAIL",
                f"Runtime core still contains full packet schema body: {label}.",
                "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md",
            )

    behavior_anchors = [
        "Runtime core remains authority for runtime behavior",
        "FIRST RESPONSE IS NOT FORMAL CLOSE",
        "Repository maintenance is not product/project execution",
        "Every repository maintenance apply/read-back must report whether manual Project Files refresh is required",
    ]

    missing_behavior = [anchor for anchor in behavior_anchors if anchor not in text]
    if missing_behavior:
        failures += 1
        add(
            results,
            check_id,
            name,
            "FAIL",
            f"Runtime behavior anchors missing after packet schema cleanup: {', '.join(missing_behavior[:5])}.",
            "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md",
        )

    if failures == 0:
        add(
            results,
            check_id,
            name,
            "PASS",
            "Runtime core references canonical transport templates and no full packet schema bodies were detected.",
        )


def check_runtime_core_registry_snapshot_cleanup(root: Path, results: list[Finding]) -> None:
    """Hard-check that runtime core does not duplicate registry stage tables."""
    check_id = "CHECK 022"
    name = "runtime_core_registry_snapshot_cleanup"
    failures = 0

    runtime_path = root / "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
    ad_path = root / "workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md"

    if not runtime_path.is_file():
        add(results, check_id, name, "FAIL", "Runtime core file is missing.", "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md")
        return

    runtime_text = read_text(runtime_path)

    required_runtime_anchors = [
        "Runtime stage registry authority lives in:",
        "workflow/stage_registry/STAGE_REGISTRY.md",
        "Runtime core must not maintain stage identity tables",
        "Phase Progress Gate and Phase Closure Contract",
        "Do not maintain a transition table in this runtime core",
    ]

    missing_runtime = [anchor for anchor in required_runtime_anchors if anchor not in runtime_text]
    if missing_runtime:
        failures += 1
        add(
            results,
            check_id,
            name,
            "FAIL",
            f"Runtime core registry-boundary anchors missing: {', '.join(missing_runtime[:5])}.",
            "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md",
        )

    forbidden_runtime_patterns = [
        ("stage_snapshot_table_header", r"\|\s*Stage ID\s*\|\s*Name\s*\|\s*Runtime role\s*\|\s*Prompt source\s*\|"),
        ("router_stage_snapshot_row", r"\|\s*ROUTER\\?_STAGE\\?_LAUNCHER\s*\|\s*Router / Stage Launcher\s*\|"),
        ("d0_stage_snapshot_row", r"\|\s*D0\\?_DIRECTION\\?_SETUP\s*\|\s*Direction Setup\s*\|"),
        ("c2_stage_snapshot_row", r"\|\s*C2\\?_CODEX\\?_EXECUTE\s*\|\s*Codex Execute\s*\|"),
    ]

    for label, pattern in forbidden_runtime_patterns:
        if re.search(pattern, runtime_text, flags=re.MULTILINE):
            failures += 1
            add(
                results,
                check_id,
                name,
                "FAIL",
                f"Runtime core still appears to contain duplicate registry snapshot table residue: {label}.",
                "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md",
            )

    stale_runtime_phrases = [
        "Until the later runtime-core packet-schema reference cleanup is applied",
        "embedded packet examples or compatibility blocks",
    ]

    for phrase in stale_runtime_phrases:
        if phrase in runtime_text:
            failures += 1
            add(
                results,
                check_id,
                name,
                "FAIL",
                f"Runtime core stale completed-cleanup wording remains: {phrase}",
                "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md",
            )

    if not ad_path.is_file():
        failures += 1
        add(results, check_id, name, "FAIL", "AD-WF-RT-001 decision file is missing.", "workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md")
    else:
        ad_text = read_text(ad_path)
        required_ad_anchors = [
            "runtime-core packet schema bodies were replaced by transport references",
            "duplicate runtime-core registry snapshot text was replaced with a pointer",
        ]
        missing_ad = [anchor for anchor in required_ad_anchors if anchor not in ad_text]
        if missing_ad:
            failures += 1
            add(
                results,
                check_id,
                name,
                "FAIL",
                f"AD-WF-RT-001 completed-cleanup anchors missing: {', '.join(missing_ad[:5])}.",
                "workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md",
            )

        stale_ad_phrases = [
            "replace embedded packet schema blocks in runtime core with links to `workflow/transport/*.md`",
            "until the later runtime-core packet-schema reference cleanup",
        ]

        for phrase in stale_ad_phrases:
            if phrase in ad_text:
                failures += 1
                add(
                    results,
                    check_id,
                    name,
                    "FAIL",
                    f"AD-WF-RT-001 stale deferred/completed cleanup wording remains: {phrase}",
                    "workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md",
                )

    if failures == 0:
        add(
            results,
            check_id,
            name,
            "PASS",
            "Runtime core registry snapshot is removed, registry authority pointer is present, and completed-cleanup notes are current.",
        )


def check_direction_worktree_repository_maintenance_contract(root: Path, results: list[Finding]) -> None:
    """Hard-check direction worktree repository maintenance policy anchors."""
    check_id = "CHECK 023"
    name = "direction_worktree_repository_maintenance_contract"
    failures = 0

    required = {
        "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md": [
            "Worktree-aware repository maintenance policy",
            "C:\\my_global_workflow",
            "C:\\my_global_workflow_worktrees\\workflow-governance",
            "codex/direction-workflow-governance",
            "codex/direction-solo-max-productive",
            "codex/direction-indie-game-development",
            "codex/direction-health-and-beauty",
            "git fetch origin",
            "git rebase origin/main",
            "Do not use the main worktree as an ordinary Direction working tree.",
        ],
        "workflow/transport/CODEX_REPOSITORY_MAINTENANCE_APPLY.md": [
            "worktree_policy:",
            "direction_worktree_map:",
            "worktree_branch_then_main_integration",
            "merge_or_pr_into_main: true",
            "direct_main_allowed: explicit_override_only",
        ],
        "docs/CHATGPT_PROJECT_SETUP.md": [
            "Direction worktree repository maintenance setup",
            "C:\\my_global_workflow_worktrees\\health-and-beauty",
            "codex/direction-health-and-beauty",
        ],
    }

    project_instruction_requirements = {
        "directions/workflow-governance/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md": [
            "Direction worktree repository maintenance",
            "C:\\my_global_workflow_worktrees\\workflow-governance",
            "codex/direction-workflow-governance",
        ],
        "directions/solo-max-productive/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md": [
            "Direction worktree repository maintenance",
            "C:\\my_global_workflow_worktrees\\solo-max-productive",
            "codex/direction-solo-max-productive",
        ],
        "directions/indie-game-development/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md": [
            "Direction worktree repository maintenance",
            "C:\\my_global_workflow_worktrees\\indie-game-development",
            "codex/direction-indie-game-development",
        ],
        "directions/health-and-beauty/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md": [
            "Direction worktree repository maintenance",
            "C:\\my_global_workflow_worktrees\\health-and-beauty",
            "codex/direction-health-and-beauty",
        ],
    }

    required.update(project_instruction_requirements)

    for file_path, anchors in required.items():
        path = root / file_path
        if not path.is_file():
            failures += 1
            add(results, check_id, name, "FAIL", "Required worktree policy file is missing.", file_path)
            continue

        text = read_text(path)
        missing = [anchor for anchor in anchors if anchor not in text]
        if missing:
            failures += 1
            add(
                results,
                check_id,
                name,
                "FAIL",
                f"Direction worktree policy anchors missing: {', '.join(missing[:5])}.",
                file_path,
            )

    forbidden_runtime = {
        "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md": [
            "### 14.4 Direct-main maintenance policy",
            "the default branch policy is direct-main maintenance unless the approved patch explicitly says otherwise",
        ],
        "workflow/transport/CODEX_REPOSITORY_MAINTENANCE_APPLY.md": [
            "mode: direct_main",
            "commit_directly: true",
        ],
    }

    for file_path, tokens in forbidden_runtime.items():
        path = root / file_path
        if not path.is_file():
            continue

        text = read_text(path)
        for token in tokens:
            if token in text:
                failures += 1
                add(
                    results,
                    check_id,
                    name,
                    "FAIL",
                    f"Stale direct-main default wording remains: {token}.",
                    file_path,
                )

    if failures == 0:
        add(
            results,
            check_id,
            name,
            "PASS",
            "Direction worktree repository maintenance policy anchors are present and stale direct-main default wording is absent.",
        )


def check_context_acquisition_policy_authority(root: Path, results: list[Finding]) -> None:
    check_id = "CHECK 024"
    name = "context_acquisition_policy_authority"
    failures = 0

    required = {
        "workflow/runtime/CONTEXT_ACQUISITION_POLICY.md": [
            "schema: context_acquisition_policy.v1",
            "## Acquisition order",
            "## GitHub-first rule",
            "## Context Request audit",
            "## Stage-close launch boundary",
        ],
        "workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md": [
            "Repository/context acquisition order before Context Request",
            "workflow/runtime/CONTEXT_ACQUISITION_POLICY.md",
        ],
        "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md": [
            "For exact repository context or exact stage prompt paths, apply `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md` before returning Context Request",
            "For exact repository context or exact stage prompt paths, has `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md` been applied before Context Request?",
        ],
        "workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md": [
            "owns GitHub read completeness verification, not source acquisition order",
            "Source/context acquisition order is owned by `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md`",
        ],
        "workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md": [
            "workflow/runtime/CONTEXT_ACQUISITION_POLICY.md",
        ],
    }

    for file_path, anchors in required.items():
        path = root / file_path
        if not path.is_file():
            failures += 1
            add(results, check_id, name, "FAIL", "Required context acquisition authority file is missing.", file_path)
            continue
        text = read_text(path)
        missing = [anchor for anchor in anchors if anchor not in text]
        if missing:
            failures += 1
            add(results, check_id, name, "FAIL", f"Missing context acquisition authority anchors: {', '.join(missing[:5])}.", file_path)

    if failures == 0:
        add(results, check_id, name, "PASS", "Context acquisition policy authority anchors are present.")


def check_github_first_acquisition_before_context_request(root: Path, results: list[Finding]) -> None:
    check_id = "CHECK 025"
    name = "github_first_acquisition_before_context_request"
    failures = 0

    required = {
        "workflow/transport/CONTEXT_REQUEST_CARD.md": [
            "acquisition_audit:",
            "github_connector:",
            "not exposed",
        ],
        "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md": [
            '"Not uploaded as a Project File or attachment" is not enough to declare missing context.',
        ],
    }

    for direction in ACTIVE_DIRECTIONS:
        required[f"directions/{direction}/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md"] = [
            "Before returning Context Request for an exact repository path or exact stage prompt path",
            "attempt verified GitHub acquisition before asking Codex/user to export",
            "acquisition_audit",
        ]

    for file_path, anchors in required.items():
        path = root / file_path
        if not path.is_file():
            failures += 1
            add(results, check_id, name, "FAIL", "Required GitHub-first acquisition file is missing.", file_path)
            continue
        text = read_text(path)
        missing = [anchor for anchor in anchors if anchor not in text]
        if missing:
            failures += 1
            add(results, check_id, name, "FAIL", f"Missing GitHub-first acquisition anchors: {', '.join(missing[:5])}.", file_path)

    if failures == 0:
        add(results, check_id, name, "PASS", "GitHub-first acquisition anchors are present before Context Request.")


def check_acquisition_order_not_duplicated(root: Path, results: list[Finding]) -> None:
    check_id = "CHECK 026"
    name = "acquisition_order_not_duplicated"
    policy_rel = "workflow/runtime/CONTEXT_ACQUISITION_POLICY.md"
    policy_path = root / policy_rel
    failures = 0

    if not policy_path.is_file():
        add(results, check_id, name, "FAIL", "Context acquisition policy file is missing.", policy_rel)
        return

    policy_text = read_text(policy_path)
    section_match = re.search(r"## Acquisition order\s+(.*?)(?:\n## |\Z)", policy_text, flags=re.S)
    if not section_match:
        add(results, check_id, name, "FAIL", "Canonical acquisition order section is missing.", policy_rel)
        return

    order_items: list[str] = []
    for item_number in range(1, 6):
        item_match = re.search(rf"^{item_number}\.\s+(.+)$", section_match.group(1), flags=re.M)
        if item_match:
            order_items.append(item_match.group(1).strip())

    if len(order_items) != 5:
        failures += 1
        add(results, check_id, name, "FAIL", "Canonical policy must contain exactly five numbered acquisition items.", policy_rel)

    scan_prefixes = (
        "workflow/runtime/",
        "workflow/transport/",
        "workflow/stage_registry/",
        "workflow/validation/",
        "docs/",
        "directions/",
    )

    for path in markdown_files(root):
        rel_path = rel(path, root)
        if rel_path == policy_rel:
            continue
        if not rel_path.startswith(scan_prefixes):
            continue

        text = read_text(path)
        matched_items = sum(1 for item in order_items if item and item in text)
        if matched_items >= 4:
            failures += 1
            add(results, check_id, name, "FAIL", "Acquisition order appears copied outside the canonical policy file.", rel_path)

    if failures == 0:
        add(results, check_id, name, "PASS", "Complete acquisition order is confined to the canonical policy file.")


def check_stage_close_launch_boundary(root: Path, results: list[Finding]) -> None:
    check_id = "CHECK 027"
    name = "stage_close_launch_boundary"
    failures = 0

    required = {
        "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md": [
            "must not request next-stage prompt text, next-stage attachments, or downstream execution-only repository exports merely so the downstream stage can run",
            "The next stage chat/run performs acquisition under `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md`",
        ],
        "workflow/transport/STAGE_LAUNCH_CARD.md": [
            "next_stage_context_policy:",
            "downstream_prompt_required_for_current_close: false",
            "downstream_execution_context_required_for_current_close: false",
            "request_downstream_context_only_if_needed_to_form_launch_card: true",
        ],
    }

    for file_path, anchors in required.items():
        path = root / file_path
        if not path.is_file():
            failures += 1
            add(results, check_id, name, "FAIL", "Required stage-close boundary file is missing.", file_path)
            continue
        text = read_text(path)
        missing = [anchor for anchor in anchors if anchor not in text]
        if missing:
            failures += 1
            add(results, check_id, name, "FAIL", f"Missing stage-close boundary anchors: {', '.join(missing[:5])}.", file_path)

    if failures == 0:
        add(results, check_id, name, "PASS", "Stage-close launch boundary anchors are present.")


def check_prompt_delivery_github_connector_mode(root: Path, results: list[Finding]) -> None:
    check_id = "CHECK 028"
    name = "prompt_delivery_github_connector_mode"
    failures = 0

    required = {
        "workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md": [
            "github_connector_verified_full_read",
            "must not mean \"skip GitHub acquisition and ask the user/Codex immediately.\"",
        ],
        "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md": [
            "github_connector_verified_full_read",
            "prompt text remains unavailable after allowed acquisition attempts",
        ],
        "workflow/transport/STAGE_LAUNCH_CARD.md": [
            "github_connector_verified_full_read",
        ],
    }

    forbidden = {
        "workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md": [
            "manual_prompt_required` means the chat must request the exact stage prompt from the user/Codex and must not auto-fetch",
        ],
        "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md": [
            "manual_prompt_required`: prompt text is not available; the chat must request the exact prompt from the user/Codex",
        ],
    }

    for file_path, anchors in required.items():
        path = root / file_path
        if not path.is_file():
            failures += 1
            add(results, check_id, name, "FAIL", "Required prompt delivery file is missing.", file_path)
            continue
        text = read_text(path)
        missing = [anchor for anchor in anchors if anchor not in text]
        if missing:
            failures += 1
            add(results, check_id, name, "FAIL", f"Missing prompt delivery anchors: {', '.join(missing[:5])}.", file_path)

    for file_path, tokens in forbidden.items():
        path = root / file_path
        if not path.is_file():
            continue
        text = read_text(path)
        for token in tokens:
            if token in text:
                failures += 1
                add(results, check_id, name, "FAIL", "manual_prompt_required still bypasses acquisition policy.", file_path)

    if failures == 0:
        add(results, check_id, name, "PASS", "GitHub connector prompt delivery mode and manual fallback semantics are present.")


def check_branch_workstream_execution_contract(root: Path, results: list[Finding]) -> None:
    check_id = "CHECK 021"
    name = "branch_workstream_execution_contract"
    failures = 0

    required_files = {
        "workflow/transport/TOPOLOGY_LAUNCH_BUNDLE.md": [
            "schema: topology_launch_bundle.v1",
            "selected_topology:",
            "synthesis_plan:",
            "state_policy:",
        ],
        "workflow/transport/WORKSTREAM_LAUNCH_CARD.md": [
            "schema: workstream_launch_card.v1",
            "dependency_policy:",
            "artifact_policy:",
            "return_contract:",
        ],
        "workflow/transport/WORKSTREAM_RESULT_CARD.md": [
            "schema: workstream_result_card.v1",
            "synthesis_readiness:",
            "state_policy_confirmation:",
            "parent_must_read_full_artifact: false",
        ],
        "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md": [
            "Branch / Workstream Execution Topology",
            "Branchability gate",
            "Heavy artifacts do not flow back to the parent chat by default",
            "A branch is not an Active Goal",
            "Topology Launch Bundle",
        ],
        "workflow/stage_prompts/E1_EXECUTION_BRIEF.md": [
            "Branch / Workstream Topology Gate",
            "topology_launch_bundle.v1",
            "workstream_result_card.v1",
            "Parallel branches are allowed only when confidently independent",
        ],
        "workflow/stage_prompts/R1_GOAL_REVIEW_DISTILL.md": [
            "Branch / workstream result boundary",
            "workstream_result_card.v1",
            "branch-only result",
        ],
    }

    for file_path, anchors in required_files.items():
        path = root / file_path
        if not path.is_file():
            failures += 1
            add(results, check_id, name, "FAIL", "Required branch/workstream file is missing.", file_path)
            continue
        text = read_text(path)
        missing = [anchor for anchor in anchors if anchor not in text]
        if missing:
            failures += 1
            add(results, check_id, name, "FAIL", f"Missing branch/workstream anchors: {', '.join(missing[:5])}.", file_path)

    branch_prompt_files = [
        "workflow/stage_prompts/D1_DEEP_RESEARCH.md",
        "workflow/stage_prompts/A1_AUDIT.md",
        "workflow/stage_prompts/F0_FAST_DIRECT.md",
        "workflow/stage_prompts/S3_DECIDE.md",
        "workflow/stage_prompts/C1_CODEX_GRAPH_PLAN.md",
        "workflow/stage_prompts/B1_PROBLEM.md",
    ]

    for file_path in branch_prompt_files:
        path = root / file_path
        if not path.is_file():
            failures += 1
            add(results, check_id, name, "FAIL", "Branch-capable stage prompt missing.", file_path)
            continue
        text = read_text(path)
        required = [
            "Branch / workstream mode",
            "workstream_result_card.v1",
            "do not close the parent Goal",
            "do not run phase_progress_gate",
        ]
        missing = [anchor for anchor in required if anchor not in text]
        if missing:
            failures += 1
            add(results, check_id, name, "FAIL", f"Missing branch-mode anchors: {', '.join(missing)}.", file_path)

    if failures == 0:
        add(results, check_id, name, "PASS", "Branch/workstream execution transport and prompt anchors are present.")


def summarize(results: list[Finding]) -> str:
    if any(item.status == "FAIL" for item in results):
        return "BLOCKED"
    if any(item.status == "WARN" for item in results):
        return "PASS_WITH_CLEANUP"
    return "PASS"


def run(root: Path, mode: str) -> list[Finding]:
    results: list[Finding] = []
    check_markdown_fence_balance(root, results)
    check_required_shared_runtime_files(root, results)
    check_active_direction_files(root, results)
    check_active_direction_project_instructions(root, results)
    check_registry_authority_markers(root, results)
    check_runtime_core_no_duplicate_full_transition_table(root, results)
    check_registry_validation_rules(root, results)
    check_registry_present_prompt_files(root, results)
    check_registry_allowed_next_tokens(root, results)
    check_r0_recovery_prompt_status(root, results)
    check_deprecated_prompt_delivery_modes(root, results)
    check_stage_prompt_forbidden_patterns(root, results)
    check_stage_prompt_route_authority_residue(root, results)
    check_ad_wf_rt_001_boundary(root, results)
    check_legacy_transport_shapes(root, results, mode)
    check_transport_apply_template(root, results, mode)
    check_prompt_eof_markers(root, results, mode)
    check_authority_eof_markers(root, results)
    check_stale_rebuild_metadata(root, results)
    check_prompt_schema_duplication(root, results)
    check_cross_direction_cache_setup(root, results)
    check_project_files_do_not_contain_stage_prompt_bodies(root, results)
    check_interface_path_detection(root, results)
    check_codex_schema_regression(root, results)
    check_transport_authority_boundary(root, results)
    check_branch_workstream_execution_contract(root, results)
    check_runtime_core_packet_schema_reference_cleanup(root, results)
    check_runtime_core_registry_snapshot_cleanup(root, results)
    check_direction_worktree_repository_maintenance_contract(root, results)
    check_context_acquisition_policy_authority(root, results)
    check_github_first_acquisition_before_context_request(root, results)
    check_acquisition_order_not_duplicated(root, results)
    check_stage_close_launch_boundary(root, results)
    check_prompt_delivery_github_connector_mode(root, results)
    return results

def print_text(results: list[Finding], root: Path, mode: str) -> None:
    summary = summarize(results)
    print("Workflow Runtime Static Checks")
    print(f"mode: {mode}")
    print(f"root: {root}")
    print(f"summary: {summary}")
    print()

    for item in results:
        path = f" [{item.path}]" if item.path else ""
        print(f"{item.status:<5} {item.check_id} {item.name}{path}")
        print(f"      {item.message}")

    print()
    print(f"Blocking failures: {sum(1 for item in results if item.status == 'FAIL')}")
    print(f"Warnings: {sum(1 for item in results if item.status == 'WARN')}")
    print(f"Info: {sum(1 for item in results if item.status == 'INFO')}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Read-only Workflow vNext-R runtime static checks.")
    parser.add_argument("--root", default=".", help="Repository root. Default: current directory.")
    parser.add_argument("--mode", choices=["baseline", "strict"], default="baseline", help="Validation mode.")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format.")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        print(f"ERROR: root does not exist or is not a directory: {root}", file=sys.stderr)
        return 2

    try:
        results = run(root, args.mode)
        summary = summarize(results)

        if args.format == "json":
            payload = {
                "summary": summary,
                "mode": args.mode,
                "root": str(root),
                "blocking_failures": sum(1 for item in results if item.status == "FAIL"),
                "warnings": sum(1 for item in results if item.status == "WARN"),
                "info": sum(1 for item in results if item.status == "INFO"),
                "results": [asdict(item) for item in results],
            }
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        else:
            print_text(results, root, args.mode)

        return 1 if summary == "BLOCKED" else 0
    except Exception as exc:
        print(f"ERROR: validation failed unexpectedly: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
