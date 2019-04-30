#!/usr/bin/env python

import click


@click.group()
def cli():
    """Displays greetings."""


@cli.command()
def hello():
    click.echo("Hello!")


if __name__ == "__main__":
    cli()
