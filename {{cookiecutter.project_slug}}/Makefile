.PHONY: help dev install test test-unit test-integration test-cov lint format typecheck clean build run

PYTHON := python{{ cookiecutter.python_version }}
PACKAGE := {{ cookiecutter.package_name }}
SRC_DIR := src/$(PACKAGE)
TEST_DIR := tests

help: ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

dev: ## Set up development environment
	uv sync --all-extras
{%- if cookiecutter.use_pre_commit == 'yes' %}
	uv run pre-commit install
{%- endif %}
	@echo "Development environment ready!"

install: ## Install the package in production mode
	uv sync

test: ## Run all tests
	uv run pytest $(TEST_DIR) -v

test-unit: ## Run unit tests only
	uv run pytest $(TEST_DIR) -v -m unit

test-integration: ## Run integration tests only
	uv run pytest $(TEST_DIR) -v -m integration

test-cov: ## Run tests with coverage report
	uv run pytest $(TEST_DIR) --cov=$(PACKAGE) --cov-report=term-missing --cov-report=html

lint: ## Run linting checks
	uv run ruff check $(SRC_DIR) $(TEST_DIR)

format: ## Format code with ruff
	uv run ruff format $(SRC_DIR) $(TEST_DIR)
	uv run ruff check --fix $(SRC_DIR) $(TEST_DIR)

typecheck: ## Run type checking with mypy
	uv run mypy $(SRC_DIR)

clean: ## Clean up generated files
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean ## Build distribution packages
	uv build

{%- if cookiecutter.cli_framework != 'none' %}

run: ## Run the CLI application
	uv run {{ cookiecutter.project_slug }}
{%- endif %}

{%- if cookiecutter.use_docker == 'yes' %}

docker-build: ## Build Docker image
	docker build -t {{ cookiecutter.project_slug }}:latest .

docker-run: ## Run Docker container
	docker run --rm -it {{ cookiecutter.project_slug }}:latest

docker-compose-up: ## Start services with docker-compose
	docker-compose up -d

docker-compose-down: ## Stop services with docker-compose
	docker-compose down
{%- endif %}