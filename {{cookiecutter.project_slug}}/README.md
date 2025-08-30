# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Features

- Modern Python {{ cookiecutter.python_version }} project with src layout
- Dependency management with [uv](https://github.com/astral-sh/uv)
- Testing with pytest
- Code formatting with ruff
- Type checking with mypy
{%- if cookiecutter.cli_framework != 'none' %}
- CLI interface with {{ cookiecutter.cli_framework }}
{%- endif %}
{%- if cookiecutter.use_docker == 'yes' %}
- Docker support for containerization
{%- endif %}
{%- if cookiecutter.use_github_actions == 'yes' %}
- GitHub Actions for CI/CD
{%- endif %}
{%- if cookiecutter.use_pre_commit == 'yes' %}
- Pre-commit hooks for code quality
{%- endif %}

## Installation

### For Development

```bash
# Clone the repository
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}

# Set up development environment
make dev
```

### For Production

```bash
# Install with uv
uv pip install {{ cookiecutter.project_slug }}

# Or install from source
make install
```

## Usage

{%- if cookiecutter.cli_framework != 'none' %}

### Command Line Interface

```bash
# Run the CLI
{{ cookiecutter.project_slug }} --help

# Or using make
make run
```
{%- endif %}

### As a Library

```python
from {{ cookiecutter.package_name }} import __version__
{%- if cookiecutter.include_example_code == 'yes' %}
from {{ cookiecutter.package_name }}.core.example import process_data

# Example usage
data = {"key": "value"}
result = process_data(data)
print(result)
{%- endif %}
```

## Development

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run only unit tests
make test-unit

# Run only integration tests
make test-integration
```

### Code Quality

```bash
# Run linting
make lint

# Format code
make format

# Type checking
make typecheck
```

### Building

```bash
# Build distribution packages
make build
```

{%- if cookiecutter.use_docker == 'yes' %}

### Docker

```bash
# Build Docker image
make docker-build

# Run Docker container
make docker-run

# Using docker-compose
make docker-compose-up
make docker-compose-down
```
{%- endif %}

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/
│   └── {{ cookiecutter.package_name }}/
│       ├── __init__.py
│       ├── core/           # Core business logic
│       ├── api/            # API interfaces
│       ├── db/             # Database models and queries
│       └── utils/          # Utility functions
├── tests/                  # Test suite (mirrors src structure)
│   ├── conftest.py
│   ├── core/
│   ├── api/
│   ├── db/
│   └── utils/
├── docs/                   # Documentation
├── config/                 # Configuration files
├── scripts/                # Utility scripts
├── pyproject.toml          # Project configuration
├── Makefile                # Development commands
└── README.md               # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

{%- if cookiecutter.open_source_license != 'Proprietary' %}
This project is licensed under the {{ cookiecutter.open_source_license }} License - see the LICENSE file for details.
{%- else %}
This project is proprietary software. All rights reserved.
{%- endif %}

## Author

{{ cookiecutter.full_name }} - {{ cookiecutter.email }}

## Acknowledgments

- Built with [cookiecutter-python-uv](https://github.com/yourusername/cookiecutter-python-uv)
- Package management by [uv](https://github.com/astral-sh/uv)