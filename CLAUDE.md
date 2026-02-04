# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a cookiecutter template for generating modern Python projects using [uv](https://github.com/astral-sh/uv) with src layout and comprehensive tooling. It creates production-ready Python 3.8+ projects with configurable features including CLI frameworks, Docker, GitHub Actions, and pre-commit hooks.

## Commands

### Generate a New Project
```bash
# Using uvx (recommended, no install needed)
uvx cookiecutter /path/to/cookiecutter-uv

# Or from GitHub
uvx cookiecutter https://github.com/kwkeefer/cookiecutter-uv
```

### Test Template Generation
```bash
# Generate with all features for testing
uvx cookiecutter --no-input . \
  project_name="Test Project" \
  use_docker=yes \
  use_github_actions=yes \
  use_pre_commit=yes \
  use_claude_agents=yes \
  cli_framework=click \
  include_example_code=yes
```

### Verify Generated Project
```bash
cd generated_project
make dev   # Install dependencies
make test  # Run tests
make lint  # Check linting
```

## Architecture

### Template Structure
- `cookiecutter.json` - Template variables and defaults
- `hooks/pre_gen_project.py` - Validates package name (Python module rules) and Python version (>= 3.8)
- `hooks/post_gen_project.py` - Removes optional files, runs `git init`, `uv sync`, installs pre-commit
- `{{cookiecutter.project_slug}}/` - Template files that become the generated project

### Key Template Variables
- `project_slug` - Auto-generated from `project_name` (lowercase, underscores)
- `package_name` - Defaults to `project_slug`, must be valid Python identifier
- `python_version` - Default "3.12", validates >= 3.8
- Feature toggles: `use_docker`, `use_github_actions`, `use_pre_commit`, `use_claude_agents`, `include_example_code`
- `cli_framework` - One of: none, click, typer, argparse

### Generated Project Layout
```
src/package_name/
├── core/       # Business logic
├── utils/      # Shared helpers (no app imports)
└── cli.py      # CLI entry point (if framework selected)
tests/          # Mirrors src structure
```

### Conditional File Removal (post_gen_project.py)
The post-generation hook removes files based on user choices:
- `use_docker=no` removes Dockerfile, docker-compose.yml, .dockerignore
- `use_github_actions=no` removes .github/
- `use_pre_commit=no` removes .pre-commit-config.yaml
- `cli_framework=none` removes src/package_name/cli.py
- `include_example_code=no` removes src/package_name/core/example.py

### AI Configuration (when use_claude_agents=yes)
- `CLAUDE.md` - Project-specific instructions auto-loaded by Claude Code
- `.claude/skills/` - Workflow skills (review, new-feature, fix-bug)
- `docs/adrs/` - Architecture Decision Records
