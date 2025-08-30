# ADR-005: {{ cookiecutter.cli_framework|title }} for CLI Framework

**Status**: Accepted  
**Date**: {% now 'local', '%Y-%m-%d' %}  

{%- if cookiecutter.cli_framework != 'none' %}
## Context
Project requires a command-line interface for user interaction.

## Decision
Use {{ cookiecutter.cli_framework }} as the CLI framework.

## Consequences
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
{%- else %}
## Context
This project does not require a CLI interface.

## Decision
No CLI framework selected.
{%- endif %}