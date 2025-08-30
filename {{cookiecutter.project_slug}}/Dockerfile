{%- if cookiecutter.use_docker == 'yes' %}
# Use Python {{ cookiecutter.python_version }} slim image
FROM python:{{ cookiecutter.python_version }}-slim

# Set working directory
WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml ./
COPY README.md ./

# Copy source code
COPY src/ ./src/

# Install the package
RUN uv pip install --system -e .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

{%- if cookiecutter.cli_framework != 'none' %}
# Set the entrypoint to the CLI
ENTRYPOINT ["{{ cookiecutter.project_slug }}"]
{%- else %}
# Default command
CMD ["python", "-m", "{{ cookiecutter.package_name }}"]
{%- endif %}
{%- endif %}