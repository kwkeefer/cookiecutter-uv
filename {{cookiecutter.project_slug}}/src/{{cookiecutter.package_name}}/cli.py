{%- if cookiecutter.cli_framework == 'click' %}
"""Command-line interface for {{ cookiecutter.project_name }}."""

import click
from {{ cookiecutter.package_name }} import __version__


@click.group()
@click.version_option(version=__version__, prog_name="{{ cookiecutter.project_slug }}")
def cli():
    """{{ cookiecutter.project_short_description }}"""
    pass


@cli.command()
@click.option('--name', '-n', default='World', help='Name to greet')
def hello(name: str):
    """Say hello to someone."""
    click.echo(f"Hello, {name}!")


@cli.command()
def info():
    """Show project information."""
    click.echo(f"{{ cookiecutter.project_name }} v{__version__}")
    click.echo(f"{{ cookiecutter.project_short_description }}")


def main():
    """Main entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()

{%- elif cookiecutter.cli_framework == 'typer' %}
"""Command-line interface for {{ cookiecutter.project_name }}."""

import typer
from rich.console import Console
from rich.table import Table
from typing_extensions import Annotated

from {{ cookiecutter.package_name }} import __version__

app = typer.Typer(
    name="{{ cookiecutter.project_slug }}",
    help="{{ cookiecutter.project_short_description }}",
    add_completion=False,
)
console = Console()


@app.command()
def hello(
    name: Annotated[str, typer.Option("--name", "-n", help="Name to greet")] = "World",
):
    """Say hello to someone."""
    console.print(f"[green]Hello, {name}![/green]")


@app.command()
def info():
    """Show project information."""
    table = Table(title="{{ cookiecutter.project_name }} Information")
    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    
    table.add_row("Version", __version__)
    table.add_row("Description", "{{ cookiecutter.project_short_description }}")
    table.add_row("Author", "{{ cookiecutter.full_name }}")
    
    console.print(table)


@app.command()
def version():
    """Show version information."""
    console.print(f"{{ cookiecutter.project_slug }} v{__version__}")


def main():
    """Main entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()

{%- elif cookiecutter.cli_framework == 'argparse' %}
"""Command-line interface for {{ cookiecutter.project_name }}."""

import argparse
import sys
from {{ cookiecutter.package_name }} import __version__


def create_parser():
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        prog="{{ cookiecutter.project_slug }}",
        description="{{ cookiecutter.project_short_description }}",
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Hello command
    hello_parser = subparsers.add_parser("hello", help="Say hello to someone")
    hello_parser.add_argument(
        "--name", "-n",
        default="World",
        help="Name to greet",
    )
    
    # Info command
    subparsers.add_parser("info", help="Show project information")
    
    return parser


def hello_command(args):
    """Execute hello command."""
    print(f"Hello, {args.name}!")


def info_command(args):
    """Execute info command."""
    print(f"{{ cookiecutter.project_name }} v{__version__}")
    print(f"{{ cookiecutter.project_short_description }}")
    print(f"Author: {{ cookiecutter.full_name }}")


def main():
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()
    
    if args.command == "hello":
        hello_command(args)
    elif args.command == "info":
        info_command(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
{%- endif %}