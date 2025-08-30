# Quick Reference - {{ cookiecutter.project_name }}

## Essential Rules (Read This First!)

### Code Style
- **Line length**: 88 chars max
- **Imports**: stdlib → third-party → local (alphabetical)
- **Naming**: `ClassName`, `function_name`, `CONSTANT_NAME`
- **Always**: Use type hints, write docstrings for public functions

### Project Structure
```
src/{{ cookiecutter.package_name }}/
  core/   → Business logic
  api/    → External interfaces  
  db/     → Database code
  utils/  → Helpers
tests/    → Mirror src/ structure
```

### Before Committing
```bash
make format    # Auto-format
make lint      # Check style
make typecheck # Verify types
make test      # Run tests
```

### Test Markers
- `@pytest.mark.unit` - Fast, isolated
- `@pytest.mark.integration` - External deps
- `@pytest.mark.slow` - >1 second

### Common Patterns

**Error Handling**:
```python
# Custom exceptions for domain errors
class ValidationError(Exception): pass

# Be specific
except SpecificError as e:
    logger.error(f"Failed: {e}")
    raise
```

**Type Hints**:
```python
def process(data: dict[str, Any]) -> Optional[Result]:
    ...
```

## Task-Specific Guides

- **Writing tests?** → See `.ai/standards/testing.md`
- **Adding feature?** → Check `.ai/architecture-decisions.md` first
- **Refactoring?** → Follow patterns in `.ai/standards/python-style.md`
- **Git commits?** → Format in `.ai/standards/git-commits.md`

## Commands Cheat Sheet

| Task | Command |
|------|---------|
| Install deps | `make dev` |
| Run tests | `make test` |
| Test coverage | `make test-cov` |
| Format code | `make format` |
| Add dependency | `uv add package` |
{%- if cookiecutter.cli_framework != 'none' %}
| Run CLI | `make run` |
{%- endif %}

## Don'ts
- ❌ Hardcode secrets
- ❌ Ignore type hints  
- ❌ Skip tests
- ❌ Files >500 lines
- ❌ Commit without formatting

## Full Details
Only read if needed for complex tasks:
- `.ai/coding-standards.md` - Comprehensive guide
- `.ai/standards/` - Detailed topic guides