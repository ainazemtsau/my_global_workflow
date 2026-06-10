# Adapter: ChatGPT Project

How to run OS sessions in a ChatGPT Project. One project per direction.

## Setup (once per direction)

1. Create a ChatGPT Project named after the direction.
2. Paste the payload from `os/adapters/SESSION_PAYLOAD.md` into Project Instructions, replacing `<direction-id>`.
3. Connect the GitHub connector to `ainazemtsau/my_global_workflow` so sessions read rules and `live/<direction-id>/` themselves.
4. No connector available? Upload the stable rule files as Project Files: `os/KERNEL.md`, `os/schema/packets.md`, `os/schema/direction-files.md`, all of `os/plays/`. **Never upload `live/**` state as files** — it changes every session and goes stale; state arrives via the CALL or the connector.

## Running a session

1. Paste the CALL (from `NOW.md → next` or the previous RESULT). Paste long context files first, the CALL last — models obey best what sits at the start (instructions) and the end (current job) of context.
2. Converse normally; the session works its play.
3. It ends with a RESULT block → relay it to the writer (see coding-agent adapter), which commits state and hands you the next CALL.

## When to route here

Good for: frame interviews, long thinking dialogs in work sessions, mobile use, cheaper/simpler tasks. State-heavy plays (shape, review, pulse, repair) and anything reading many repo files run with fewer relay hops in an agentic CLI (coding-agent adapter).

END_OF_FILE: os/adapters/chatgpt-project.md
