#!/usr/bin/env python3
"""Repo-scoped Codex hook guard for Direction-OS maintenance hazards."""

from __future__ import annotations

import argparse
import json
import re
import shlex
import sys
from pathlib import Path, PureWindowsPath
from typing import Any


ROOT = Path(__file__).resolve().parent
POLICY_PATH = ROOT / "policy.json"

WRITE_TOOL_NAMES = {
    "apply_patch",
    "edit",
    "write",
    "create_file",
    "move",
    "delete",
    "shell_command",
    "exec_command",
}

PRODUCT_WRITE_WORDS = re.compile(
    r"\b(git\s+(?:add|commit|push|checkout|switch|merge|rebase|reset|restore|clean|apply|stash)|"
    r"apply_patch|set-content|add-content|out-file|new-item|remove-item|move-item|copy-item|"
    r"del|erase|rm|mv|cp)\b",
    re.IGNORECASE,
)

CLOSE_WORDS = re.compile(r"\b(done|verified|closed|complete(?:d)?)\b", re.IGNORECASE)
STATE_CLOSE_WORDS = re.compile(
    r"(remove[sd]?\s+open_call|clear[sd]?\s+open_call|delete[sd]?\s+open_call|"
    r"open_calls\s*:\s*\[\s*\]|status\s*:\s*done|task\s*[-\w]*\s*done|state_changes)",
    re.IGNORECASE,
)
PENDING_WORDS = re.compile(
    r"(checkpoint|pending\s+close|close\s+pending|leave[sd]?\s+close\s+pending|"
    r"open_call\s+pending|close\s+remains\s+pending)",
    re.IGNORECASE,
)
FRESH_G5_WORDS = re.compile(
    r"(binding|fresh(?:-session)?)"
    r"(?=[\s\S]{0,120}\b(?:g5|review|refutation)\b)"
    r"(?=[\s\S]{0,180}\b(?:evidence|pass|passed|survived|clean|verified)\b)",
    re.IGNORECASE,
)


def decision_block(reason: str) -> dict[str, Any]:
    return {"decision": "block", "reason": reason}


def decision_allow() -> dict[str, Any]:
    return {"continue": True}


def load_policy() -> dict[str, Any]:
    with POLICY_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def flatten_strings(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        out: list[str] = []
        for item in value.values():
            out.extend(flatten_strings(item))
        return out
    if isinstance(value, list):
        out = []
        for item in value:
            out.extend(flatten_strings(item))
        return out
    return []


def text_blob(payload: dict[str, Any]) -> str:
    preferred = [
        "last_assistant_message",
        "final_response",
        "response",
        "message",
        "text",
    ]
    parts = [str(payload[key]) for key in preferred if isinstance(payload.get(key), str)]
    if not parts:
        parts = flatten_strings(payload)
    return "\n".join(parts)


def get_event(payload: dict[str, Any], cli_event: str | None) -> str:
    if cli_event:
        return cli_event
    for key in ("hook_event_name", "hook_event", "event"):
        if isinstance(payload.get(key), str):
            return str(payload[key])
    return ""


def norm_path(value: str) -> str:
    if not value:
        return ""
    value = value.strip().strip('"').strip("'").replace("\\", "/")
    try:
        return str(PureWindowsPath(value)).replace("\\", "/").lower()
    except Exception:
        return value.lower()


def contains_path(haystack: str, path: str) -> bool:
    if not haystack or not path:
        return False
    return norm_path(path) in norm_path(haystack)


def payload_tool_name(payload: dict[str, Any]) -> str:
    for key in ("tool_name", "name", "tool"):
        if isinstance(payload.get(key), str):
            return str(payload[key]).lower()
    return ""


def payload_tool_input(payload: dict[str, Any]) -> Any:
    for key in ("tool_input", "input", "arguments", "args", "parameters"):
        if key in payload:
            return payload[key]
    return {}


def command_from_payload(payload: dict[str, Any]) -> str:
    tool_input = payload_tool_input(payload)
    if isinstance(tool_input, dict):
        for key in ("command", "cmd", "script"):
            if isinstance(tool_input.get(key), str):
                return str(tool_input[key])
    for key in ("command", "cmd", "script"):
        if isinstance(payload.get(key), str):
            return str(payload[key])
    return ""


def workdir_from_payload(payload: dict[str, Any]) -> str:
    tool_input = payload_tool_input(payload)
    if isinstance(tool_input, dict):
        for key in ("workdir", "cwd", "working_directory"):
            if isinstance(tool_input.get(key), str):
                return str(tool_input[key])
    for key in ("workdir", "cwd", "working_directory"):
        if isinstance(payload.get(key), str):
            return str(payload[key])
    return ""


def is_allowed_product_git_read(command: str) -> bool:
    try:
        tokens = shlex.split(command, posix=False)
    except ValueError:
        tokens = command.split()
    lowered = [token.strip('"').strip("'").lower() for token in tokens]
    if not lowered or lowered[0] != "git":
        return False
    verb = ""
    idx = 1
    while idx < len(lowered):
        token = lowered[idx]
        if token in ("-c", "--git-dir", "--work-tree"):
            idx += 2
            continue
        if token in ("-C", "-c"):
            idx += 2
            continue
        if token.startswith("-"):
            idx += 1
            continue
        verb = token
        break
    return verb in {"status", "diff", "show", "log", "fetch"}


def targets_product_repo(payload: dict[str, Any], policy: dict[str, Any]) -> bool:
    blob = text_blob(payload)
    command = command_from_payload(payload)
    workdir = workdir_from_payload(payload)
    for repo in policy.get("product_repos", []):
        if contains_path(workdir, repo) or contains_path(command, repo) or contains_path(blob, repo):
            return True
    return False


def blocks_product_write(payload: dict[str, Any], policy: dict[str, Any]) -> str | None:
    if not targets_product_repo(payload, policy):
        return None
    command = command_from_payload(payload)
    tool = payload_tool_name(payload)
    if command and PRODUCT_WRITE_WORDS.search(command):
        return "Blocked product-repo write/stage/commit/push risk for C:/projects/Unity/GasCoopGame."
    if command and is_allowed_product_git_read(command):
        return None
    if tool in WRITE_TOOL_NAMES or not command:
        return "Blocked product-repo write/stage/commit/push risk for C:/projects/Unity/GasCoopGame."
    return "Blocked non-allowlisted product-repo command; only git status/diff/show/log/fetch are allowed."


def blocks_side_repair(payload: dict[str, Any], policy: dict[str, Any]) -> str | None:
    blob = text_blob(payload)
    command = command_from_payload(payload)
    combined = "\n".join([blob, command, workdir_from_payload(payload)])
    direction = str(policy["direction_id"])
    protected = str(policy["protected_side_repair_path"])
    if direction not in combined or not contains_path(combined, protected):
        return None
    ack_pattern = re.compile(str(policy["side_repair_ack_pattern"]))
    if ack_pattern.search(combined):
        return None
    tool = payload_tool_name(payload)
    if tool in WRITE_TOOL_NAMES or PRODUCT_WRITE_WORDS.search(command) or "apply_patch" in combined:
        return (
            f"Blocked side repair to {protected} during {direction}; "
            "include owner_ack_side_repair:<id> to override."
        )
    return None


def blocks_bad_close(payload: dict[str, Any], policy: dict[str, Any]) -> str | None:
    msg = text_blob(payload)
    direction = str(policy["direction_id"])
    if direction not in msg:
        return None
    has_state_close = bool(STATE_CLOSE_WORDS.search(msg))
    has_close = bool(CLOSE_WORDS.search(msg))
    has_pending = bool(PENDING_WORDS.search(msg))
    has_binding_g5 = bool(FRESH_G5_WORDS.search(msg))
    if has_binding_g5:
        return None
    if has_pending and not has_state_close and "closed" not in msg.lower():
        return None
    if has_close or has_state_close:
        return (
            f"Blocked {direction} close/done claim without binding fresh G5/review evidence. "
            "Checkpoint text is allowed only when close remains pending."
        )
    return None


def evaluate(payload: dict[str, Any], cli_event: str | None = None) -> dict[str, Any]:
    try:
        policy = load_policy()
    except Exception as exc:
        return decision_block(f"Guard policy could not be loaded: {exc}")

    event = get_event(payload, cli_event)
    if event == "Stop":
        reason = blocks_bad_close(payload, policy)
        if reason:
            return decision_block(reason)
        return decision_allow()

    if event in {"PreToolUse", "PostToolUse"}:
        for check in (blocks_product_write, blocks_side_repair):
            reason = check(payload, policy)
            if reason:
                return decision_block(reason)
        return decision_allow()

    return decision_allow()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", default=None)
    args = parser.parse_args(argv)
    try:
        payload = json.load(sys.stdin)
    except Exception as exc:
        print(json.dumps(decision_block(f"Malformed hook JSON; failing closed: {exc}")))
        return 0
    print(json.dumps(evaluate(payload, args.event)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
