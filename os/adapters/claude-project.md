# Adapter: Claude Project (claude.ai)

How to run OS sessions in a Claude Project. One project per direction. Functionally mirrors the ChatGPT adapter — same payload, same packets.

## Setup (once per direction)

1. Create a Claude Project named after the direction.
2. Paste the payload from `os/adapters/SESSION_PAYLOAD.md` into the project's custom instructions, replacing `<direction-id>`.
3. Connect the GitHub integration / repo sync to `ainazemtsau/my_global_workflow` (project knowledge), or rely on self-contained CALLs and pasted NOW.md — both work.
4. If syncing repo files into project knowledge: sync `os/**` only. **Never sync or upload `live/**` as static knowledge** — it goes stale; state arrives via the CALL or a fresh paste.

## Running a session

Identical to ChatGPT: paste context first, CALL last; session ends with a RESULT; RESULT goes to the writer.

## When to route here

Good for: complex reasoning-heavy sessions (shape, review, hard work tasks) when you route by model strength. The owner's stated split — simpler tasks to ChatGPT, harder to Claude — is expressed at paste time or via the optional `surface:` hint in a CALL; nothing else in the OS changes between platforms.

Note: a Claude Code session on the workflow repo can replace this entirely for state-heavy plays — it reads and writes state itself (zero relay hops), per the coding-agent adapter.

END_OF_FILE: os/adapters/claude-project.md
