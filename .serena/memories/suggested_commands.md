# Suggested Commands

- Check branch: `git.exe branch --show-current`
- Pull main: `git.exe pull --ff-only origin main`
- Search files: `rg --files`
- Search text: `rg -n "pattern" path`
- Check staged scope: `git.exe diff --cached --name-only`
- Whitespace check: `git.exe diff --check`
- Status: `git.exe status --short`
- Last commit: `git.exe log -1 --oneline`
- Commit diff names: `git.exe diff HEAD~1..HEAD --name-only`

On this Windows/Codex setup, prefixing Git invocations with `& git.exe` avoids shell policy quirks for some commands.