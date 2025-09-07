# Cookiecutter Python uv

Modern Python project template using [uv](https://github.com/astral-sh/uv) with src layout and comprehensive tooling.

## Features

✨ **Modern Python Setup**
- Python 3.8+ support with configurable version
- src layout for better package organization
- Test structure that mirrors source code
- uv for fast, reliable dependency management

🛠️ **Development Tools**
- Comprehensive Makefile for common tasks
- Pre-configured pytest with markers for unit/integration tests
- Ruff for fast linting and formatting
- mypy for static type checking
- Coverage reporting

📦 **Optional Features**
- CLI framework options (Click, Typer, Argparse, or none)
- Docker support with multi-stage builds
- GitHub Actions CI/CD pipeline
- Pre-commit hooks for code quality
- Example code to get started quickly

## Quick Start

### Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) (for uvx command)

### Installation & Usage

The easiest way to use this template is with `uvx` (no installation required):

```bash
# Generate a new project directly with uvx
uvx cookiecutter https://github.com/kwkeefer/cookiecutter-uv

# Or if you've cloned the repository locally
uvx cookiecutter /path/to/cookiecutter-uv
```

Alternative installation methods:

```bash
# Traditional pip install
pip install cookiecutter
cookiecutter https://github.com/kwkeefer/cookiecutter-uv

# Or with uv tool install (permanent installation)
uv tool install cookiecutter
cookiecutter https://github.com/kwkeefer/cookiecutter-uv
```

You'll be prompted to enter values for your project:

```
full_name [Your Name]: Jane Doe
email [your.email@example.com]: jane@example.com
github_username [yourusername]: janedoe
project_name [My Python Project]: Awesome Tool
project_slug [awesome_tool]: 
package_name [awesome_tool]: 
project_short_description [A short description of the project]: A tool that does awesome things
version [0.1.0]: 
python_version [3.12]: 
Select use_docker:
1 - yes
2 - no
Choose from 1, 2 [1]: 1
Select use_github_actions:
1 - yes
2 - no
Choose from 1, 2 [1]: 1
Select use_pre_commit:
1 - yes
2 - no
Choose from 1, 2 [1]: 1
Select cli_framework:
1 - none
2 - click
3 - typer
4 - argparse
Choose from 1, 2, 3, 4 [1]: 2
Select include_example_code:
1 - yes
2 - no
Choose from 1, 2 [1]: 1
Select use_claude_agents:
1 - yes
2 - no
Choose from 1, 2 [1]: 1
Select open_source_license:
1 - MIT
2 - Apache-2.0
3 - GPL-3.0
4 - BSD-3-Clause
5 - Proprietary
Choose from 1, 2, 3, 4, 5 [1]: 1
```

After generation:

```bash
cd awesome_tool
make dev  # Set up development environment
make test # Run tests
```

## Project Structure

The generated project will have the following structure:

```
project-name/
├── src/
│   └── package_name/
│       ├── __init__.py
│       ├── cli.py           # If CLI framework selected
│       ├── core/            # Core business logic
│       │   ├── __init__.py
│       │   └── example.py   # If include_example_code
│       ├── api/             # API interfaces
│       │   └── __init__.py
│       ├── db/              # Database modules
│       │   └── __init__.py
│       └── utils/           # Utility functions
│           └── __init__.py
├── tests/                   # Test suite mirroring src
│   ├── __init__.py
│   ├── conftest.py         # Shared fixtures
│   ├── core/
│   │   └── test_example.py
│   ├── api/
│   ├── db/
│   └── utils/
├── docs/                    # Documentation
├── config/                  # Configuration files
├── scripts/                 # Utility scripts
├── .github/
│   └── workflows/
│       └── ci.yml          # If use_github_actions
├── Dockerfile              # If use_docker
├── docker-compose.yml      # If use_docker
├── pyproject.toml          # Project configuration
├── Makefile                # Development commands
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
└── .pre-commit-config.yaml # If use_pre_commit
```

## Available Make Commands

The generated project includes a comprehensive Makefile:

- `make help` - Show all available commands
- `make dev` - Set up development environment
- `make test` - Run all tests
- `make test-unit` - Run unit tests only
- `make test-integration` - Run integration tests only
- `make test-cov` - Run tests with coverage
- `make lint` - Run linting checks
- `make format` - Format code
- `make typecheck` - Run type checking
- `make build` - Build distribution packages
- `make clean` - Clean generated files
- `make run` - Run the CLI (if CLI framework selected)
- `make docker-build` - Build Docker image (if Docker selected)
- `make docker-run` - Run Docker container (if Docker selected)

## Configuration Options

**CLI Frameworks**: none, click, typer, argparse
**Optional Features**: Docker, GitHub Actions, Pre-commit, Example Code, Claude Agents  
**License Options**: MIT, Apache-2.0, GPL-3.0, BSD-3-Clause, Proprietary

## AI Assistant Features

When `use_claude_agents` is enabled:
- `.ai/` directory with project context and architecture decisions
- `.claude/agents/` with specialized development agents
- Update script: `python scripts/update_ai_config.py`

## License

MIT