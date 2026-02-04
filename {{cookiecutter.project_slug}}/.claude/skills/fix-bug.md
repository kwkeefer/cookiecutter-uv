{%- if cookiecutter.use_claude_agents == 'yes' -%}
---
description: Fix a bug using test-driven development
---

# Bug Fix (TDD Approach)

Fix bugs by first reproducing them with a failing test.

## Process

### 1. Reproduce with a Failing Test

Write a test that demonstrates the bug:

```python
@pytest.mark.unit
def test_bug_reproduction():
    """Regression test for [describe bug]."""
    # Arrange - Set up the conditions that trigger the bug
    input_data = {"problematic": "value"}

    # Act - Execute the code path
    result = buggy_function(input_data)

    # Assert - What SHOULD happen (currently fails)
    assert result.status == "success"
```

Run to confirm it fails:
```bash
make test
```

### 2. Fix the Bug

Make the minimal change needed to fix the issue.

### 3. Verify the Fix

```bash
make test          # Confirm the new test passes
make test-cov      # Check no coverage regression
```

### 4. Check for Regressions

```bash
make lint && make typecheck && make test
```

## Checklist

- [ ] Wrote failing test that reproduces the bug
- [ ] Test has proper marker (`@pytest.mark.unit` or `@pytest.mark.integration`)
- [ ] Fix is minimal and focused
- [ ] All existing tests still pass
- [ ] No new linting or type errors

## Commit Format

```
fix: <describe what was fixed>

Closes #<issue-number>
```
{%- endif %}
