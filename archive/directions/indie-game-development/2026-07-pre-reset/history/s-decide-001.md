# RECORD — s-decide-001 (decision, 2026-06-13) — frontier-model routing for GasCoopGame engineering

Owner-confirmed decision on the frontier model/harness for the engineering executor, chosen via a
5-agent web-grounded analysis (workflow w8n35cgfb / wf_1b219118-504) after Fable 5 became unavailable.
A decision record, not a play execution; the operative routing lives in NOW.md (c-exec-002
surface / model_routing).

DECISION (owner «подтверждаю», 2026-06-13): **DUAL-MODEL**.
- BUILD = Claude Code + Claude Opus 4.8 (planner + autonomous builder); reserve ultracode/Dynamic
  Workflows for bounded heavy legs (Claude Pro has no hard token cap; sustained autonomy may need Max/API).
- VALIDATE = OpenAI Codex CLI + GPT-5.5 xhigh, read-only / fresh-context / sandboxed (different family).

HONEST FRAMING (from the workflow's bias-critic, which caught the synthesis over-favoring Claude):
the validator is the WEAKER model, so its real job is a cheap INDEPENDENT GATE-RUNNER (re-run the
per-tick hash check across host + 2 headless clients, the engine-free boundary build, dotnet test from
fresh context, flag divergence) — NOT the authority on frontier netcode reasoning. BINDING acceptance =
green gates + evidence + owner human spot-review on novel netcode. No determinism/netcode benchmark
exists for either model — fitness is inferred, which is exactly why the independent gate-run + human
matter. Confidence: HIGH on builder, MEDIUM on validator efficacy, LOW on the unmeasured
determinism/netcode transfer.

WHY: owner holds BOTH ChatGPT Pro + Claude Pro (second family is sunk cost); repo is harness-agnostic;
Opus leads hard multi-file + long-context repo work (SWE-bench Pro 69 vs 59; 1M-context 68 vs 45) and
is the named Unity-C# pick now that Fable 5 is gone; GPT-5.5 leads terminal/sandbox/efficiency — ideal
for the gate-run.

FLIP / REVISIT IF: Fable 5 restored (original #1; pulled 2026-06-12 under a US export-control directive
Anthropic is disputing) -> revisit builder; OR Claude Pro can't sustain the build -> single-vendor
Codex/GPT-5.5 (token-efficient, kernel-sandboxed) with a human/same-family review gate; OR work turns
terminal/CI/sandbox-heavy -> Codex.

state_changes: NOW.md c-exec-002 surface -> fresh-chat + model_routing note (above); no task/bet change
(t-1 stays ready). Saved to model memory (gascoopgame-engineering-model-routing); flag for a knowledge/
entry at the next review.
next: t-1 (c-exec-002) runs in a FRESH Claude Code session in the dev worktree (builder = Opus 4.8);
independent Codex/GPT-5.5 gate-run before merge.

END_OF_FILE: live/indie-game-development/history/s-decide-001.md
