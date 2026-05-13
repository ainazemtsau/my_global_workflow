# Open Findings

Use `FINDING_REGISTER.md` as the canonical schema.

## WFG-FINDING-2026-05-13-001 — GitHub long-file reads can truncate required workflow authority files

```yaml
finding_id: WFG-FINDING-2026-05-13-001
status: accepted
area: github_context_transport
severity: P1
confidence: high
summary: "Required workflow authority files and long stage prompts can be truncated by GitHub connector tool response token budget."
patch_needed: true
patch_id: WFG_PATCH_2026_05_13_GITHUB_LONG_FILE_READ_GUARD
next_action: "Apply patch and refresh Project Files runtime cache."
```
