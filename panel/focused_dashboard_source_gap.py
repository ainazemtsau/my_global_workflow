"""Focused acceptance for dashboard source-gap semantics.

Run:  python panel/focused_dashboard_source_gap.py
Exit: 0 only when an honest zero is distinct from a missing source.
"""

import datetime
import json
import os
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request

import yaml


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PANEL_DIR = os.path.join(ROOT, "panel")
LIVE_DIR = os.path.join(ROOT, "live")
DIRECTIONS = ("direction-os", "indie-game-development", "solmax")
BLOCK_IDS = ("running", "stalled", "done_in_window", "problems")


def fail(message):
    raise AssertionError(message)


def fetch(base, path):
    with urllib.request.urlopen(base + path, timeout=10) as response:
        return response.status, json.loads(response.read().decode("utf-8"))


def start_panel():
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
    process = subprocess.Popen(
        [sys.executable, os.path.join(PANEL_DIR, "serve.py"),
         "--port", str(port), "--no-open"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    base = f"http://127.0.0.1:{port}"
    for _ in range(40):
        try:
            status, _ = fetch(base, "/api/state")
            if status == 200:
                return process, base
        except (urllib.error.URLError, ConnectionError, json.JSONDecodeError):
            time.sleep(0.25)
    process.terminate()
    fail("server did not become ready")


def read_cards(direction):
    sys.path.insert(0, PANEL_DIR)
    import cards

    found = {}
    live = os.path.join(LIVE_DIR, direction, "cards")
    for folder, closed in ((live, False), (os.path.join(live, "closed"), True)):
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            if not name.endswith(".md"):
                continue
            head, blocks = cards.read_card(os.path.join(folder, name))
            head["_closed"] = closed
            found[str(head["id"])] = (head, blocks)
    return found


def expected_counts(direction):
    cards = read_cards(direction)
    with open(os.path.join(LIVE_DIR, direction, "NOW.md"), encoding="utf-8") as source:
        now = yaml.safe_load(source.read()) or {}
    bet = now.get("bet")
    live_heads = [head for head, _ in cards.values() if not head["_closed"]]
    running = sum(
        (head.get("_kind") == "node" and head.get("status") == "active")
        or (head.get("_kind") == "task" and head.get("_bet") == bet
            and head.get("status") == "open")
        or (head.get("_kind") == "call" and head.get("status") in ("ready", "running"))
        for head in live_heads
    )
    stalled = sum(head.get("status") in ("blocked", "waiting", "paused")
                  for head in live_heads)
    problems = sum(head.get("_kind") == "issue" for head in live_heads)

    today = datetime.date.today()
    first = today - datetime.timedelta(days=29)
    history = os.path.join(LIVE_DIR, direction, "history")
    done = 0
    if os.path.isdir(history):
        for name in os.listdir(history):
            if len(name) < 10 or not name.endswith(".md"):
                continue
            try:
                day = datetime.date.fromisoformat(name[:10])
            except ValueError:
                continue
            done += first <= day <= today
    return {"running": running, "stalled": stalled,
            "done_in_window": done, "problems": problems}


def verify_missing_source_is_still_named():
    sys.path.insert(0, PANEL_DIR)
    import serve

    original_live = serve.LIVE_DIR
    try:
        with tempfile.TemporaryDirectory() as source_root:
            serve.LIVE_DIR = source_root
            block = serve.dash_done("missing-source-probe")
    finally:
        serve.LIVE_DIR = original_live
    if block["id"] != "done_in_window" or not block["gap"]:
        fail(f"missing history source was not named: {block}")
    if "history" not in block["gap"] or block["count"] != 0:
        fail(f"missing history reason is not specific: {block}")


def main():
    process, base = start_panel()
    responses = {}
    try:
        for direction in DIRECTIONS:
            status, data = fetch(base, f"/api/section/{direction}/dashboard")
            if status != 200:
                fail(f"{direction}: HTTP {status}, expected 200")
            responses[direction] = data
    finally:
        process.terminate()
        process.wait(timeout=10)

    for direction, data in responses.items():
        build = data.get("build") or {}
        if (not build.get("commit") or not build.get("commit_date")
                or not build.get("root") or "stale" not in build):
            fail(f"{direction}: incomplete freshness header: {build}")
        blocks = data.get("blocks") or []
        if tuple(block.get("id") for block in blocks) != BLOCK_IDS:
            fail(f"{direction}: expected four blocks {BLOCK_IDS}, got {blocks}")
        if any(not block.get("how") for block in blocks):
            fail(f"{direction}: every block must carry a non-empty how")
        got_counts = {block["id"]: block.get("count") for block in blocks}
        want_counts = expected_counts(direction)
        if got_counts != want_counts:
            fail(f"{direction}: row counts {got_counts}, independently counted {want_counts}")
        gaps = data.get("blocks_without_source")
        if gaps != []:
            fail(f"{direction}: blocks_without_source == {gaps!r}, expected []")

    solmax = responses["solmax"]
    running = next(block for block in solmax["blocks"] if block["id"] == "running")
    if running["count"] != 0 or running["gap"] is not None:
        fail(f"solmax running is not an honest zero: {running}")
    if "активной ставки нет" not in (running.get("note") or ""):
        fail(f"solmax running does not name why its source-backed count is zero: {running}")

    verify_missing_source_is_still_named()
    counts = {direction: {block["id"]: block["count"]
                          for block in data["blocks"]}
              for direction, data in responses.items()}
    gaps = {direction: data["blocks_without_source"]
            for direction, data in responses.items()}
    print("ACCEPTED dashboard source-gap semantics")
    print("counts:", json.dumps(counts, ensure_ascii=False, sort_keys=True))
    print("blocks_without_source:", json.dumps(gaps, ensure_ascii=False, sort_keys=True))
    print("death-threshold-2: 0 of 4 blocks without source")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print("FAILED dashboard source-gap semantics:", error)
        raise SystemExit(1)
