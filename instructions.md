# Cookiecutter Template Implementation Guide for Modern Python Project

## Objective
Create a cookiecutter template that generates a modern Python project with uv support, following 2024 best practices with src layout and mirrored test structure.

## High-Level Structure Overview

### Template Repository Structure
Create a repository called `cookiecutter-python-uv` with:
- `cookiecutter.json` - Configuration file with project variables
- `hooks/` directory - Pre and post-generation scripts
- `{{cookiecutter.project_slug}}/` - The actual template files
- Documentation - README explaining usage

### Key Variables to Define in cookiecutter.json
- Basic info: author name, email, project name/slug/package name
- Python version preference
- Optional features: Docker, GitHub Actions, pre-commit, CLI framework choice
- License type
- Whether to include example code

## Implementation Steps

### Step 1: Core Project Structure
Create the template directory structure that mirrors the "Modern Python Project" layout we discussed:
- `src/{{package_name}}/` with subdirectories for core, api, db, utils
- `tests/` that mirrors the src structure (not split by unit/integration)
- Supporting directories: docs, config, scripts, .github/workflows

### Step 2: Dynamic pyproject.toml
Create a pyproject.toml template that:
- Uses uv/hatchling for build system
- Conditionally includes dependencies based on user choices (CLI framework, etc.)
- Configures pytest with markers for unit/integration/slow tests
- Sets up ruff and mypy with sensible defaults
- Includes pytest configuration that points to src layout

### Step 3: Test Structure
Set up tests/ to mirror src/ structure with:
- A shared conftest.py at tests root
- Test files that follow the pattern `test_*.py`
- Example tests that use pytest markers (@pytest.mark.unit, @pytest.mark.integration)

### Step 4: Conditional Features
Use Jinja2 templating to conditionally include:
- CLI setup (Click/Typer/Argparse/None)
- Docker files (Dockerfile and docker-compose.yml)
- GitHub Actions workflow
- Pre-commit configuration
- Example code in each module

### Step 5: Development Tooling
Include templates for:
- Makefile with common commands (test, lint, format, build, run)
- Pre-commit hooks configuration (if selected)
- GitHub Actions CI pipeline (if selected)
- Environment configuration (.env.example)

### Step 6: Hooks
Create pre/post generation hooks to:
- Validate project naming conventions
- Initialize git repository
- Run `uv init --no-project` and `uv sync` after generation
- Set up pre-commit hooks if selected
- Clean up any unwanted files based on user choices

## Key Design Decisions

### File Organization
- All Python source in `src/{{package_name}}/`
- Tests mirror source structure, not organized by type
- Configuration in `config/` directory
- Scripts in `scripts/` directory

### Testing Strategy
- Use pytest markers instead of directory separation
- Include examples of both unit and integration tests
- Provide Makefile targets for running different test types

### Development Workflow
- Makefile as primary interface for common tasks
- uv for dependency management
- ruff for linting/formatting
- mypy for type checking
- pytest for testing

### Conditional Complexity
Keep the template simple by default but allow opting into:
- Docker containerization
- CI/CD pipelines
- CLI interfaces
- Pre-commit hooks

## Usage Instructions for End Users

The template should be usable with:
```bash
cookiecutter gh:yourusername/cookiecutter-python-uv
cd project-name
make dev  # Sets up development environment
make test  # Runs tests
```

## Tips for Implementation

1. Start minimal - get a basic template working first
2. Add conditional features incrementally
3. Test the template by generating projects with different options
4. Include a generated example in the repo to show what it produces
5. Document which decisions are made by default vs customizable

## Files Priority Order

Start with these core files:
1. cookiecutter.json (defines all variables)
2. pyproject.toml template
3. Basic source and test structure
4. Makefile
5. README template

Then add optional features:
6. Docker support
7. GitHub Actions
8. Pre-commit configuration

