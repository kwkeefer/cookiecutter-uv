{%- if cookiecutter.use_claude_agents == 'yes' -%}
---
description: Implement a new feature following project conventions
---

# New Feature Implementation

Follow this checklist when implementing new features.

## Before Starting

1. **Check existing patterns**: Look for similar features in the codebase
2. **Review ADRs**: Check `docs/adrs/` for relevant architectural decisions
3. **Identify the right module**:
   - Business logic → `src/{{ cookiecutter.package_name }}/core/`
   - Shared helpers → `src/{{ cookiecutter.package_name }}/utils/`

## Implementation Steps

1. **Create module** in appropriate directory under `src/{{ cookiecutter.package_name }}/`

2. **Add corresponding test file** mirroring the source path:
   ```
   src/{{ cookiecutter.package_name }}/core/new_feature.py
   tests/core/test_new_feature.py
   ```

3. **Write tests first** (or alongside) with proper markers:
   ```python
   @pytest.mark.unit
   def test_feature_happy_path():
       # Arrange, Act, Assert
   ```

4. **Implement with type hints**:
   ```python
   def process_feature(data: dict[str, Any]) -> Result:
       """Process the feature data."""
       ...
   ```

5. **Run quality checks**:
   ```bash
   make format && make lint && make typecheck && make test
   ```

## Checklist

- [ ] Module placed in correct directory
- [ ] Test file mirrors source structure
- [ ] All functions have type hints
- [ ] Tests have `@pytest.mark.unit` or `@pytest.mark.integration`
- [ ] Follows AAA pattern (Arrange, Act, Assert)
- [ ] Custom exceptions for domain errors
- [ ] All checks pass: `make format lint typecheck test`
{%- endif %}
