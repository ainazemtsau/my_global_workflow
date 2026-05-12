# Real Direction Test Cases

Use this file to record real Direction behavior test cases.

## Test case shape

```yaml
test_case:
  test_id:
  direction_path:
  scenario:
  files_loaded:
  expected_behavior:
  actual_behavior:
  result:
  finding_id:
```

## Rules

- Use `directions/*/project_files/` only when auditing real Direction behavior.
- Do not load sibling Directions by default.
- Do not modify tested Direction files unless a separate approved repository patch authorizes it.
