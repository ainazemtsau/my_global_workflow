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
]

DEPRECATED_PROMPT_DELIVERY_MODES = [
    "request_from_repository",
    "embedded_in_launch_card",
    "pasted_in_current_chat",
    "attached_export",
]

LEGACY_TRANSPORT_PATTERNS = [
    "stage_launch_card: 1",
    "stage_result_packet: 1",
    "card_type:",
    "packet_type:",
    "patch_type:",
]

STALE_METADATA_PATTERNS = [
    "vNext-R REBUILD",
    "test-active",
    "rebuild root only",
    "Installed from roadmap step",
    "Step 7.",
]

REQUIRED_EOF_FILES = [
    "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md",
    "workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md",
    "workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md",
    "workflow/stage_registry/STAGE_REGISTRY.md",
]


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


def add(results: list[Finding], check_id: str, name: str, status: Status, message: str, path: str | None = None) -> None:
    results.append(Finding(check_id=check_id, name=name, status=status, message=message, path=path))


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
                add(results, "CHECK 003", "active_direction_00_07_exist", "FAIL", "Required Direction Project File is missing.", path)
    if not missing:
        add(results, "CHECK 003", "active_direction_00_07_exist", "PASS", "All active Direction Project Files 00-07 exist.")


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
    found = 0
    for path in sorted(transport_dir.glob("*.md")):
        text = read_text(path)
        for token in LEGACY_TRANSPORT_PATTERNS:
            if token in text:
                found += 1
                add(results, "CHECK 010", "legacy_transport_shape_scan", status, f"Legacy transport shape token found: {token}.", rel(path, root))
    if found == 0:
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
    status: Status = "WARN" if mode == "baseline" else "FAIL"
    prompts = stage_prompt_files(root)
    missing = 0
    for path in prompts:
        text = read_text(path)
        if "END_OF_FILE:" not in text:
            missing += 1
            add(results, "CHECK 012", "prompt_eof_markers", status, "Stage prompt lacks END_OF_FILE marker.", rel(path, root))
    if missing == 0:
        add(results, "CHECK 012", "prompt_eof_markers", "PASS", "All stage prompts have END_OF_FILE markers.")


def check_authority_eof_markers(root: Path, results: list[Finding]) -> None:
    missing = 0
    for item in REQUIRED_EOF_FILES:
        path = root / item
        if not path.is_file():
            add(results, "CHECK 013", "authority_eof_markers", "FAIL", "Required authority EOF file is missing.", item)
            missing += 1
            continue
        text = read_text(path)
        expected = f"END_OF_FILE: {item}"
        if expected not in text:
            missing += 1
            add(results, "CHECK 013", "authority_eof_markers", "FAIL", "Required authority EOF marker missing or changed.", item)

    source_path = root / "WORKFLOW_SOURCE_OF_TRUTH.md"
    if source_path.is_file() and "END_OF_FILE:" not in read_text(source_path):
        add(results, "CHECK 013", "authority_eof_markers", "WARN", "WORKFLOW_SOURCE_OF_TRUTH.md lacks END_OF_FILE marker; current baseline treats this as non-blocking because the file is short.", "WORKFLOW_SOURCE_OF_TRUTH.md")

    if missing == 0:
        add(results, "CHECK 013", "authority_eof_markers", "PASS", "Required authority EOF markers are present.")


def check_stale_rebuild_metadata(root: Path, results: list[Finding]) -> None:
    scanned_roots = [
        root / "workflow",
        root / "directions",
        root / "docs",
    ]
    found = 0
    for base in scanned_roots:
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            if ".git" in path.parts:
                continue
            text = read_text(path)
            for token in STALE_METADATA_PATTERNS:
                if token in text:
                    found += 1
                    add(results, "CHECK 014", "stale_rebuild_metadata", "WARN", f"Stale metadata token found: {token}.", rel(path, root))
    if found == 0:
        add(results, "CHECK 014", "stale_rebuild_metadata", "PASS", "No stale rebuild/test-active metadata tokens found in scanned markdown files.")


def check_prompt_schema_duplication(root: Path, results: list[Finding]) -> None:
    tokens = [
        "schema: stage_launch.v1",
        "schema: stage_result.v1",
        "schema: repository_patch.v1",
        "schema: context_request.v1",
        "schema: human_decision.v1",
        "allowed_next",
        "Next Launch Card Required Format",
    ]
    found = 0
    for path in stage_prompt_files(root):
        text = read_text(path)
        matches = [token for token in tokens if token in text]
        if matches:
            found += 1
            add(results, "CHECK 015", "prompt_schema_duplication_scan", "WARN", f"Prompt contains duplicated schema/route surface tokens: {', '.join(matches[:4])}.", rel(path, root))
    if found == 0:
        add(results, "CHECK 015", "prompt_schema_duplication_scan", "PASS", "No obvious prompt schema duplication tokens found.")


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
        if f"directions/{direction}/project_files/07_PHASE_MEMORY_INDEX.md" not in manifest_text:
            missing_refs.append(direction)
    if missing_refs:
        add(results, "CHECK 016", "cross_direction_cache_setup_consistency", "FAIL", f"Manifest missing 07 Phase Memory references for: {', '.join(missing_refs)}.", rel(manifest, root))
    else:
        add(results, "CHECK 016", "cross_direction_cache_setup_consistency", "PASS", "Manifest references active Direction Project Files 00-07 including 07 Phase Memory.")

    if docs_setup.is_file():
        docs_text = read_text(docs_setup)
        if "Workflow Governance" not in docs_text or "07_PHASE_MEMORY_INDEX.md" not in docs_text:
            add(results, "CHECK 016", "cross_direction_cache_setup_consistency", "WARN", "docs/CHATGPT_PROJECT_SETUP.md appears stale versus current Workflow Governance/cache setup.", rel(docs_setup, root))
        else:
            add(results, "CHECK 016", "cross_direction_cache_setup_consistency", "PASS", "docs/CHATGPT_PROJECT_SETUP.md contains Workflow Governance and 07 Phase Memory references.")
    else:
        add(results, "CHECK 016", "cross_direction_cache_setup_consistency", "WARN", "docs/CHATGPT_PROJECT_SETUP.md missing.", rel(docs_setup, root))


def check_project_files_do_not_contain_stage_prompt_bodies(root: Path, results: list[Finding]) -> None:
    found = 0
    suspicious_tokens = [
        "Runtime Stage Prompt",
        "Stage type:",
        "Prompt version:",
        "Reviewable Work Product Rule",
    ]
    for direction in ACTIVE_DIRECTIONS:
        project_dir = root / "directions" / direction / "project_files"
        if not project_dir.exists():
            continue
        for path in project_dir.glob("*.md"):
            text = read_text(path)
            if any(token in text for token in suspicious_tokens) and "workflow/stage_prompts/" in text:
                found += 1
                add(results, "CHECK 017", "project_files_do_not_contain_stage_prompt_bodies", "FAIL", "Direction Project File appears to contain a stage prompt body.", rel(path, root))
    if found == 0:
        add(results, "CHECK 017", "project_files_do_not_contain_stage_prompt_bodies", "PASS", "No full stage prompt bodies detected in active Direction Project Files.")


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
            "Runtime core may still contain compatibility examples or legacy embedded packet blocks",
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
    check_deprecated_prompt_delivery_modes(root, results)
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
    check_runtime_core_packet_schema_reference_cleanup(root, results)
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
