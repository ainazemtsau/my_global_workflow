# NEXT_CHAT_CARD Eval

status: active_eval

## Required Checks

- Closure derives continuation from selected main procedure, actual result, passed or explicitly blocked completion check, resolved dependency status, and next intended workflow step.
- If continuation is needed, closure includes post-closed `NEXT_CHAT_CARD`.
- `NEXT_CHAT_CARD` includes title, why, main procedure to start, context to paste, expected result, evidence or return needed, and start instruction.
- `context_to_paste` is complete enough for the user to open the next chat without assembling missing pieces manually.
- `NEXT_CHAT_CARD` is used only after current START goal completion or explicit blocked closure and never carries unfinished dependency work.
- If continuation is not needed, closure states `no_next_chat_needed` with reason.

## Failure Checks

- Card is a placeholder.
- Card hardcodes a global next-step enum instead of deriving from closure facts.
- Card omits main procedure to start.
- Card makes the user reconstruct context from previous chat memory.
- Closure omits both NEXT_CHAT_CARD and no_next_chat_needed.
- Card represents unfinished dependency work, replaces `DEPENDENCY_CALL`, or closes while dependency returns are open/missing/unverified.
- Card or transfer packet is treated as terminal completion for the current START goal.

END_OF_FILE: workflow_v3/evals/NEXT_MOVE_PACKET_EVAL.md
