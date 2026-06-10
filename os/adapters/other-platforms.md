# Adapter: any other chat platform (Gemini Gem, new tools, plain chats)

The OS is platform-agnostic by construction: rules in git, self-contained CALL/RESULT packets, writer serializing all state changes. Any chat tool that can hold a conversation can run a session.

## Recipe

1. If the platform has a custom-instructions slot (Gemini Gem, system prompt, etc.): paste `os/adapters/SESSION_PAYLOAD.md` payload with `<direction-id>` filled. One gem/profile per direction.
2. If it has repo access (connector, file search): point it at `ainazemtsau/my_global_workflow`.
3. If it has neither: start each chat by pasting, in this order — the payload, the play file, NOW.md, then the CALL last. CALLs are self-contained, so even a bare chat works; it just costs one extra paste.
4. RESULT goes to the writer as always.

## Migration between platforms

There is nothing to migrate. State never lives in a platform; abandoning a platform loses nothing. Setting up a new one is steps 1–2 above (≈2 minutes per direction).

END_OF_FILE: os/adapters/other-platforms.md
