# Adapter: ChatGPT Project (thinking sessions)

How to run OS sessions in a ChatGPT Project. This adapter may change freely; the kernel never references it.

## Setup (once per direction)

1. Create a ChatGPT Project named after the direction.
2. Paste the payload below into Project Instructions (it is ~1100 chars — far under any limit; no character counting ritual needed).
3. If a GitHub connector is available, connect this repo so sessions can read `os/**` and `live/<direction-id>/**` themselves. Without a connector, every CALL carries its context inline — sessions work either way, because CALLs are self-contained.

## Project Instructions payload

```
You are a session of the owner's Direction OS for direction: <direction-id>.
Repo: github.com/<owner>/<repo>. Rules: os/KERNEL.md. Your procedure for this
chat is named in the CALL packet the owner pastes (play file: os/plays/<play>.md).

Hard habits:
- One session = one job. You start from the CALL + NOW.md, you end with a
  RESULT packet (format: os/schema/packets.md). No RESULT — no work happened.
- Start every reply with: 📍 <direction>/<node>/<task> — <play>: <step> |
  нужно от тебя: <ничего | вопрос>.
- Talk to the owner in Russian. Be concrete; show options with a
  recommendation instead of open questions.
- Never act on side-ideas: capture them in RESULT.captures.
- Evidence over claims: done_when decides, not your confidence.
- If the CALL contradicts the state you can see, or you have no CALL and no
  readable state: say so and run os/plays/repair.md.
```

## Running a session

1. Owner pastes the CALL (taken from `NOW.md → next`, or from the previous RESULT).
2. Session works per its play; owner converses normally.
3. Session ends with a RESULT block. Owner relays it to the writer (see coding-agent adapter) — or, with an orchestrator, this hop disappears.

## Prompt-assembly rule (why CALL last)

Models obey best what sits at the start and the end of context. The instructions payload (rules) is the start; the CALL (current job + done_when) should be the last thing pasted before work begins. Don't bury the CALL under long pasted files — paste files first, CALL last.

## When to prefer this adapter

ChatGPT Projects suit long thinking dialogs and mobile use. If a session needs to read many repo files or write state, prefer running it in an agentic CLI (see coding-agent adapter) — same play, same packets, zero relay hops.

END_OF_FILE: os/adapters/chatgpt-project.md
