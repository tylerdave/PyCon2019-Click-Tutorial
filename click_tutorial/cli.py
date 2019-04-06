# -*- coding: utf-8 -*-

"""Console script for click_tutorial."""
import sys
import click


@click.group()
def main(args=None):
    """Click tutorial runner."""

@main.command()
def verify():
    """Verify that your environment is set up correctly."""
    click.echo("All good!")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
