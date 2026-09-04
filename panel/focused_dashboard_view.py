"""Focused acceptance for the still-disabled direction dashboard view.

Run:  python panel/focused_dashboard_view.py

The production HTTP endpoint feeds the production app.js renderer for three
directions. In-memory negative controls prove that each named guard can fail.
"""
import copy
import json
import os
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRECTIONS = ("direction-os", "indie-game-development", "solmax")


def start_panel():
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
    process = subprocess.Popen(
        [sys.executable, os.path.join(ROOT, "panel", "serve.py"),
         "--port", str(port), "--no-open"],
        cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    base = f"http://127.0.0.1:{port}/"
    for _ in range(50):
        try:
            with urllib.request.urlopen(base + "api/state", timeout=2) as response:
                if response.status == 200:
                    return process, base
        except (urllib.error.URLError, ConnectionError):
            time.sleep(0.1)
    process.terminate()
    raise RuntimeError("panel did not start")


def source_codes(base):
    codes = set(DIRECTIONS)
    counts = {}
    for direction in DIRECTIONS:
        with urllib.request.urlopen(
                base + "api/section/" + direction + "/dashboard", timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
        counts[direction] = {block["id"]: block["count"] for block in data["blocks"]}
        for block in data["blocks"]:
            codes.add(block["id"])
            for row in block["rows"]:
                if row.get("id"):
                    codes.add(str(row["id"]))
                if row.get("sha"):
                    codes.add(str(row["sha"]))
    return codes, counts


def violations(payload, codes):
    bad = []
    if len(payload["renders"]) != 3:
        bad.append("three-renders")
    for render in payload["renders"]:
        if render["blockCount"] != 4:
            bad.append("four-blocks")
        if any(block["previewRows"] > 5 for block in render["blocks"]):
            bad.append("compactness")
        if any(not block["numberVisible"] or not block["howVisible"]
               for block in render["blocks"]):
            bad.append("count-with-how")
        if any(not block["moreWasHidden"] or not block["moreOpened"]
               for block in render["blocks"]):
            bad.append("expand-in-place")
        if not render["hashUnchangedByToggles"]:
            bad.append("toggle-navigation")
        if render["chartCount"] != 1 or render["chartCells"] != 30:
            bad.append("chart-count")
        if render["inlineStyleCount"]:
            bad.append("inline-style")
        if render["writeControlCount"]:
            bad.append("read-only-control")
        for code in codes:
            if code and (code in render["before"] or code in render["after"]):
                bad.append("code-leak")
                break
    links = [link["href"] for render in payload["renders"] for link in render["links"]]
    if not any("/goals/" in (href or "") for href in links):
        bad.append("goal-link")
    if not any((href or "").endswith("/history") for href in links):
        bad.append("history-link")
    records = [fact for render in payload["renders"] for fact in render["recordFacts"]]
    if not records or any(not fact["wasHidden"] or not fact["opened"] or not fact["text"]
                          for fact in records):
        bad.append("record-text")
    if any(request["method"] != "GET" for request in payload["requests"]):
        bad.append("read-only-request")
    return sorted(set(bad))


def negative_controls(good, codes):
    probes = {}

    broken = copy.deepcopy(good)
    broken["renders"][0]["blocks"][0]["previewRows"] = 6
    probes["compactness"] = "compactness" in violations(broken, codes)

    broken = copy.deepcopy(good)
    broken["renders"][0]["links"] = []
    for render in broken["renders"][1:]:
        render["links"] = [link for link in render["links"] if "/goals/" not in (link["href"] or "")]
    probes["links"] = "goal-link" in violations(broken, codes)

    broken = copy.deepcopy(good)
    broken["renders"][0]["chartCount"] = 2
    probes["chart-count"] = "chart-count" in violations(broken, codes)

    broken = copy.deepcopy(good)
    broken["renders"][0]["after"] += " direction-os"
    probes["code-leak"] = "code-leak" in violations(broken, codes)

    broken = copy.deepcopy(good)
    broken["renders"][0]["inlineStyleCount"] = 1
    probes["inline-style"] = "inline-style" in violations(broken, codes)

    broken = copy.deepcopy(good)
    broken["requests"].append({"url": "/api/write", "method": "POST"})
    probes["read-only"] = "read-only-request" in violations(broken, codes)
    return probes


def main():
    process, base = start_panel()
    try:
        codes, counts = source_codes(base)
        run = subprocess.run(
            ["node", os.path.join(ROOT, "panel", "focused_dashboard_view.cjs"),
             base, *DIRECTIONS], cwd=ROOT, capture_output=True, text=True,
            encoding="utf-8", errors="replace")
        if run.returncode != 0:
            raise RuntimeError(run.stderr or run.stdout)
        payload = json.loads(run.stdout)
        bad = violations(payload, codes)
        probes = negative_controls(payload, codes)
        if bad or not all(probes.values()):
            raise AssertionError({"violations": bad, "negative_controls": probes})
        print("ACCEPTED dashboard view")
        print("HTTP/UI counts:", json.dumps(counts, ensure_ascii=False, sort_keys=True))
        print("renders:", json.dumps({r["direction"]: {
            "blocks": r["blockCount"], "chart": r["chartCount"],
            "cells": r["chartCells"], "links": len(r["links"]),
            "records": len(r["recordFacts"])} for r in payload["renders"]},
            ensure_ascii=False, sort_keys=True))
        print("negative controls:", json.dumps(probes, ensure_ascii=False, sort_keys=True))
    finally:
        process.terminate()
        process.wait(timeout=10)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("FAILED dashboard view:", error)
        raise
