{%- if cookiecutter.use_claude_agents == 'yes' -%}
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

{{ cookiecutter.project_short_description }}

- **Package**: `{{ cookiecutter.package_name }}`
- **Python**: {{ cookiecutter.python_version }}+
- **Tools**: uv, pytest, ruff, mypy
{%- if cookiecutter.cli_framework != 'none' %}
- **CLI**: {{ cookiecutter.cli_framework }}
{%- endif %}

## Dependencies

**Never edit pyproject.toml directly for dependencies.** Use uv commands:

```bash
uv add package              # Add production dependency
uv add --dev package        # Add dev dependency
uv remove package           # Remove dependency
```

This keeps pyproject.toml and uv.lock in sync.

## Commands

```bash
make dev          # Setup environment
make test         # Run all tests
make test-unit    # Fast tests only
make lint         # Check style
make format       # Auto-format
make typecheck    # Type checking
{%- if cookiecutter.cli_framework != 'none' %}
make run          # Run CLI
{%- endif %}
```

## Project Structure

```
src/{{ cookiecutter.package_name }}/
├── core/    # Business logic
├── utils/   # Shared helpers (no app imports)
└── cli.py   # CLI entry point (if selected)
tests/       # Mirrors src/ structure
docs/adrs/   # Architecture Decision Records
```

## Code Style

- **Line length**: 88 chars
- **Type hints**: Required on all functions
- **Imports**: stdlib → third-party → local (handled by ruff)
- **Naming**: `ClassName`, `function_name`, `CONSTANT_NAME`
- `utils/` should not import from other app modules

### Patterns

```python
# Logging
logger = logging.getLogger(__name__)

# Errors - use custom exceptions, never bare except
from {{ cookiecutter.package_name }}.core.exceptions import ValidationError

# Composition over inheritance
from typing import Protocol

class Repository(Protocol):
    def get(self, id: str) -> Model: ...

class Service:
    def __init__(self, repo: Repository):
        self._repo = repo
```

## Testing

Tests mirror source structure:
- `src/{{ cookiecutter.package_name }}/core/feature.py` → `tests/core/test_feature.py`

### Markers (Required)
```python
@pytest.mark.unit         # No external deps, <100ms
@pytest.mark.integration  # External deps (DB, API)
@pytest.mark.slow         # >1 second
```

### AAA Pattern
```python
def test_feature_behavior(self):
    # Arrange
    user = User(name="test")

    # Act
    result = service.process(user)

    # Assert
    assert result.status == "success"
```

## Git Commits

Format: `<type>: <subject>`

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

```
feat: add user authentication
fix: resolve database connection timeout
refactor: extract validation into separate module
```

## Architecture Decisions

See `docs/adrs/` for Architecture Decision Records:
- 001: src/ layout
- 002: Mirrored test structure
- 003: Module organization
- 004: Deep modules (prefer cohesive modules over many small files)
{%- endif %}
