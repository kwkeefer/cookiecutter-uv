# Architecture Decisions for {{ cookiecutter.project_name }}

## ADR-001: Use src Layout for Python Package

**Status**: Accepted  
**Date**: {% now 'local', '%Y-%m-%d' %}  

### Context
Need to organize Python package structure in a way that prevents accidental imports of development code and ensures proper testing isolation.

### Decision
Use `src/` layout where all package code lives under `src/{{ cookiecutter.package_name }}/`.

### Consequences
- ✅ Prevents importing from the development directory
- ✅ Clear separation between source and tests
- ✅ Better compatibility with modern Python tooling
- ⚠️ Requires explicit PYTHONPATH configuration in some IDEs

---

## ADR-002: Mirror Test Structure to Source

**Status**: Accepted  
**Date**: {% now 'local', '%Y-%m-%d' %}  

### Context
Tests need to be organized in a way that makes it easy to find the tests for any given module.

### Decision
Mirror the source structure in tests/ directory rather than separating by test type (unit/integration).

### Consequences
- ✅ Easy to locate tests for any module
- ✅ Natural organization as project grows
- ✅ Can still use markers for test categorization
- ⚠️ Integration tests mixed with unit tests in same directories

---

## ADR-003: Use uv for Dependency Management

**Status**: Accepted  
**Date**: {% now 'local', '%Y-%m-%d' %}  

### Context
Need a fast, reliable Python package manager that supports modern workflows.

### Decision
Use uv instead of pip/poetry/pipenv for all dependency management.

### Consequences
- ✅ Extremely fast dependency resolution
- ✅ Built-in virtual environment management  
- ✅ Compatible with pip requirements
- ⚠️ Newer tool with smaller ecosystem

---

## ADR-004: Makefile as Primary Developer Interface

**Status**: Accepted  
**Date**: {% now 'local', '%Y-%m-%d' %}  

### Context
Developers need a consistent interface for common tasks regardless of their familiarity with Python tooling.

### Decision
Provide a Makefile with all common development tasks.

### Consequences
- ✅ Universal interface across different environments
- ✅ Self-documenting with help target
- ✅ Composable commands
- ⚠️ Requires make to be installed (usually available)

---

{%- if cookiecutter.cli_framework != 'none' %}

## ADR-005: {{ cookiecutter.cli_framework|title }} for CLI Framework

**Status**: Accepted  
**Date**: {% now 'local', '%Y-%m-%d' %}  

### Context
Project requires a command-line interface for user interaction.

### Decision
Use {{ cookiecutter.cli_framework }} as the CLI framework.

### Consequences
{%- if cookiecutter.cli_framework == 'click' %}
- ✅ Mature, feature-rich framework
- ✅ Excellent documentation and community
- ✅ Decorator-based API
- ⚠️ Additional dependency
{%- elif cookiecutter.cli_framework == 'typer' %}
- ✅ Modern, type-hint based
- ✅ Automatic help generation
- ✅ Rich terminal output support
- ⚠️ Newer framework
{%- elif cookiecutter.cli_framework == 'argparse' %}
- ✅ Standard library, no dependencies
- ✅ Well-documented
- ⚠️ More verbose than alternatives
- ⚠️ Less feature-rich
{%- endif %}

---
{%- endif %}

## ADR-006: Module Organization

**Status**: Proposed  
**Date**: {% now 'local', '%Y-%m-%d' %}  

### Context
Need clear boundaries between different aspects of the application.

### Decision
Organize code into four main modules:
- `core/` - Business logic and domain models
- `api/` - External interfaces (REST, GraphQL, etc.)
- `db/` - Database models and queries
- `utils/` - Shared utilities and helpers

### Consequences
- ✅ Clear separation of concerns
- ✅ Easy to understand project structure
- ✅ Prevents circular dependencies
- ⚠️ May need adjustment based on project needs

---

## ADR-007: Configuration Management

**Status**: Proposed  
**Date**: {% now 'local', '%Y-%m-%d' %}  

### Context
Need a way to manage configuration across different environments.

### Decision
- Use environment variables for secrets
- Use `config/` directory for non-secret configuration
- Support `.env` files for local development

### Consequences
- ✅ Secrets never in version control
- ✅ Easy deployment configuration
- ✅ Local development convenience
- ⚠️ Need to document all environment variables

---

## ADR-008: Error Handling Strategy

**Status**: Proposed  
**Date**: {% now 'local', '%Y-%m-%d' %}  

### Context
Need consistent error handling across the application.

### Decision
- Use custom exception classes for domain errors
- Let unexpected exceptions bubble up
- Log errors with appropriate context
- Return meaningful error messages to users

### Consequences
- ✅ Predictable error handling
- ✅ Good debugging information
- ✅ Clean error messages for users
- ⚠️ Requires discipline to maintain

---

## ADR Template

## ADR-XXX: [Decision Title]

**Status**: [Proposed|Accepted|Deprecated|Superseded]  
**Date**: YYYY-MM-DD  

### Context
[Describe the issue motivating this decision]

### Decision
[Describe the decision and rationale]

### Consequences
- ✅ [Positive consequence]
- ⚠️ [Neutral or trade-off]
- ❌ [Negative consequence]

### Alternatives Considered
- [Alternative 1]: [Why not chosen]
- [Alternative 2]: [Why not chosen]