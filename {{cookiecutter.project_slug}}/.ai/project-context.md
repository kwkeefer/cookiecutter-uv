# Project Context for {{ cookiecutter.project_name }}

## Overview
{{ cookiecutter.project_short_description }}

## Project Type
- **Name**: {{ cookiecutter.project_name }}
- **Package**: {{ cookiecutter.package_name }}
- **Version**: {{ cookiecutter.version }}
- **Python Version**: {{ cookiecutter.python_version }}
- **Author**: {{ cookiecutter.full_name }} ({{ cookiecutter.email }})

## Technology Stack
- **Language**: Python {{ cookiecutter.python_version }}
- **Package Manager**: uv
- **Build System**: Hatchling
- **Testing Framework**: pytest
- **Linting/Formatting**: ruff
- **Type Checking**: mypy
{%- if cookiecutter.cli_framework != 'none' %}
- **CLI Framework**: {{ cookiecutter.cli_framework }}
{%- endif %}
{%- if cookiecutter.use_docker == 'yes' %}
- **Containerization**: Docker
{%- endif %}
{%- if cookiecutter.use_github_actions == 'yes' %}
- **CI/CD**: GitHub Actions
{%- endif %}
{%- if cookiecutter.use_pre_commit == 'yes' %}
- **Git Hooks**: pre-commit
{%- endif %}

## Project Structure
```
{{ cookiecutter.project_slug }}/
├── src/{{ cookiecutter.package_name }}/   # Main package source code
│   ├── core/                              # Core business logic
│   ├── api/                               # API interfaces
│   ├── db/                                # Database modules
│   └── utils/                             # Utility functions
├── tests/                                 # Test suite (mirrors src structure)
├── docs/                                  # Documentation
├── config/                                # Configuration files
└── scripts/                               # Utility scripts
```

## Key Design Decisions
1. **Source Layout**: Using `src/` layout for better testing isolation and import clarity
2. **Test Structure**: Tests mirror source structure for easy navigation
3. **Test Markers**: Using pytest markers (@pytest.mark.unit, @pytest.mark.integration) instead of directory separation
4. **Development Workflow**: Makefile as primary interface for common tasks

## Development Commands
- `make dev` - Set up development environment
- `make test` - Run all tests
- `make test-unit` - Run unit tests only
- `make test-integration` - Run integration tests only
- `make lint` - Run linting checks
- `make format` - Format code
- `make typecheck` - Type checking
- `make build` - Build distribution packages
{%- if cookiecutter.cli_framework != 'none' %}
- `make run` - Run the CLI application
{%- endif %}

## Current State
- [ ] Initial project setup
- [ ] Core functionality implementation
- [ ] API design and implementation
- [ ] Database integration
- [ ] Testing coverage
- [ ] Documentation
- [ ] Deployment configuration

## Important Files
- `pyproject.toml` - Project configuration and dependencies
- `Makefile` - Development automation
- `.ai/` - AI assistant instructions and context
- `tests/conftest.py` - Shared test fixtures

## Notes for AI Assistants
- Always use the `src/` layout when adding new modules
- Create corresponding test files in the mirrored test structure
- Use type hints for all function signatures
- Follow existing code style and patterns
- Run `make format` and `make lint` before committing
- Update this file when making significant architectural changes