# Cookiecutter Python uv

A modern Python project template using [uv](https://github.com/astral-sh/uv) for dependency management, following 2024 best practices with src layout and comprehensive development tooling.

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
- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [uv](https://github.com/astral-sh/uv) (recommended, will be prompted to install if missing)

### Installation

```bash
# Install cookiecutter if you haven't already
pip install cookiecutter

# Or with uv
uv pip install cookiecutter
```

### Usage

Generate a new project:

```bash
cookiecutter https://github.com/yourusername/cookiecutter-uv
```

Or use it locally:

```bash
cookiecutter /path/to/cookiecutter-uv
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

### CLI Frameworks

- **none**: No CLI framework
- **click**: Feature-rich CLI framework
- **typer**: Modern CLI framework with type hints
- **argparse**: Built-in Python argument parser

### Optional Features

- **Docker**: Includes Dockerfile and docker-compose.yml
- **GitHub Actions**: CI/CD pipeline for testing and building
- **Pre-commit**: Git hooks for code quality checks
- **Example Code**: Sample modules and tests to get started

### License Options

- MIT
- Apache-2.0
- GPL-3.0
- BSD-3-Clause
- Proprietary

## Development

To contribute to this cookiecutter template:

```bash
git clone https://github.com/yourusername/cookiecutter-uv
cd cookiecutter-uv

# Test the template
cookiecutter . --no-input
cd my_python_project
make dev
make test
```

## Testing Different Configurations

You can test the template with different configurations:

```bash
# Minimal setup
cookiecutter . --no-input \
    use_docker=no \
    use_github_actions=no \
    use_pre_commit=no \
    cli_framework=none \
    include_example_code=no

# Full featured
cookiecutter . --no-input \
    use_docker=yes \
    use_github_actions=yes \
    use_pre_commit=yes \
    cli_framework=typer \
    include_example_code=yes
```

## License

This cookiecutter template is released under the MIT License.

## Acknowledgments

- [uv](https://github.com/astral-sh/uv) for blazing fast Python package management
- [cookiecutter](https://github.com/cookiecutter/cookiecutter) for project templating
- The Python community for best practices and standards

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch
3. Test the template with various configurations
4. Commit your changes
5. Push to the branch
6. Open a Pull Request