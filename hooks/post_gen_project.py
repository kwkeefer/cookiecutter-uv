#!/usr/bin/env python
"""Post-generation hooks for the cookiecutter template."""

import os
import shutil
import subprocess
import sys
from pathlib import Path


def remove_file(filepath):
    """Remove a file if it exists."""
    path = Path(filepath)
    if path.exists():
        path.unlink()
        print(f"Removed: {filepath}")


def remove_dir(dirpath):
    """Remove a directory if it exists."""
    path = Path(dirpath)
    if path.exists():
        shutil.rmtree(path)
        print(f"Removed directory: {dirpath}")


def run_command(cmd, description):
    """Run a shell command."""
    print(f"\n{description}...")
    try:
        subprocess.run(cmd, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Warning: {description} failed: {e}")
        return False


def main():
    """Execute post-generation tasks."""
    print("\n" + "="*60)
    print("Setting up your new Python project...")
    print("="*60)
    
    # Clean up files based on user choices
    if '{{ cookiecutter.use_docker }}' == 'no':
        remove_file('Dockerfile')
        remove_file('docker-compose.yml')
        remove_file('.dockerignore')
    
    if '{{ cookiecutter.use_github_actions }}' == 'no':
        remove_dir('.github')
    
    if '{{ cookiecutter.use_pre_commit }}' == 'no':
        remove_file('.pre-commit-config.yaml')
    
    if '{{ cookiecutter.cli_framework }}' == 'none':
        remove_file('src/{{ cookiecutter.package_name }}/cli.py')
    
    if '{{ cookiecutter.include_example_code }}' == 'no':
        remove_file('src/{{ cookiecutter.package_name }}/core/example.py')
    
    # Initialize git repository
    if not Path('.git').exists():
        run_command('git init', 'Initializing git repository')
        run_command('git add .', 'Adding files to git')
        run_command('git commit -m "Initial commit from cookiecutter-python-uv"', 'Creating initial commit')
    
    # Check if uv is available
    if shutil.which('uv'):
        # Initialize uv project
        if not Path('uv.lock').exists():
            run_command('uv sync --all-extras', 'Installing dependencies with uv')
        
        # Install pre-commit hooks if selected
        if '{{ cookiecutter.use_pre_commit }}' == 'yes':
            run_command('uv run pre-commit install', 'Installing pre-commit hooks')
    else:
        print("\n" + "!"*60)
        print("WARNING: uv is not installed!")
        print("Please install uv to manage dependencies:")
        print("  curl -LsSf https://astral.sh/uv/install.sh | sh")
        print("  or")
        print("  pip install uv")
        print("!"*60)
    
    print("\n" + "="*60)
    print("✨ Your project is ready!")
    print("="*60)
    print("\nNext steps:")
    print("1. cd {{ cookiecutter.project_slug }}")
    if not shutil.which('uv'):
        print("2. Install uv (see warning above)")
        print("3. make dev  # Set up development environment")
    else:
        print("2. make dev  # Set up development environment")
    print("3. make test # Run tests")
    print("\nSee README.md for more information.")
    print("\nHappy coding! 🚀")


if __name__ == '__main__':
    main()