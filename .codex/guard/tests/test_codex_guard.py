import json
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "codex_guard.py"


def run_guard(payload, event):
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--event", event],
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        check=True,
    )
    return json.loads(proc.stdout)


class CodexGuardTests(unittest.TestCase):
    def test_bad_close_blocked(self):
        result = run_guard(
            {
                "last_assistant_message": (
                    "RESULT for c-visual-006: verified and closed. "
                    "state_changes remove open_call and status: done."
                )
            },
            "Stop",
        )
        self.assertEqual(result["decision"], "block")
        self.assertIn("binding fresh G5", result["reason"])

    def test_checkpoint_allowed(self):
        result = run_guard(
            {
                "last_assistant_message": (
                    "Checkpoint RESULT for c-visual-006. Product merge evidence recorded; "
                    "close remains pending and open_call pending."
                )
            },
            "Stop",
        )
        self.assertEqual(result, {"continue": True})

    def test_g5_close_allowed(self):
        result = run_guard(
            {
                "last_assistant_message": (
                    "RESULT for c-visual-006 closed with binding fresh-session G5 review "
                    "evidence passed; state_changes remove open_call."
                )
            },
            "Stop",
        )
        self.assertEqual(result, {"continue": True})

    def test_product_main_write_blocked(self):
        result = run_guard(
            {
                "tool_name": "shell_command",
                "tool_input": {
                    "workdir": "C:/projects/Unity/GasCoopGame",
                    "command": "git add Assets && git commit -m visual",
                },
            },
            "PreToolUse",
        )
        self.assertEqual(result["decision"], "block")
        self.assertIn("product-repo", result["reason"])

    def test_product_main_read_allowed(self):
        result = run_guard(
            {
                "tool_name": "shell_command",
                "tool_input": {
                    "workdir": "C:/projects/Unity/GasCoopGame",
                    "command": "git status --short",
                },
            },
            "PreToolUse",
        )
        self.assertEqual(result, {"continue": True})

    def test_c_visual_005_side_repair_blocked(self):
        result = run_guard(
            {
                "tool_name": "apply_patch",
                "tool_input": {
                    "patch": (
                        "*** Update File: docs/results/c-visual-005.md\n"
                        "@@\n-c-visual-006 note\n+c-visual-006 repaired\n"
                    )
                },
            },
            "PreToolUse",
        )
        self.assertEqual(result["decision"], "block")
        self.assertIn("owner_ack_side_repair", result["reason"])

    def test_side_repair_with_ack_allowed(self):
        result = run_guard(
            {
                "tool_name": "apply_patch",
                "tool_input": {
                    "patch": (
                        "owner_ack_side_repair:repair-1\n"
                        "*** Update File: docs/results/c-visual-005.md\n"
                        "@@\n-c-visual-006 note\n+c-visual-006 repaired\n"
                    )
                },
            },
            "PreToolUse",
        )
        self.assertEqual(result, {"continue": True})

    def test_malformed_json_fail_closed(self):
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), "--event", "Stop"],
            input="{not-json",
            text=True,
            capture_output=True,
            check=True,
        )
        result = json.loads(proc.stdout)
        self.assertEqual(result["decision"], "block")
        self.assertIn("Malformed hook JSON", result["reason"])


if __name__ == "__main__":
    unittest.main()
