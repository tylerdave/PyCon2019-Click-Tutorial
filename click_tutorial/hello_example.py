#!/usr/bin/env python

import click
import time


@click.group()
def cli():
    """Command group."""


@cli.command()
@click.argument("name")
@click.option("--color", default="green", type=click.Choice(["red", "black", "green"]))
@click.option(
    "--count", "-c", type=int, default=1, help="number of times to print message"
)
def hello(name, color, count):
    """A command that says hello."""
    click.echo("color: {}".format(color), err=True)
    for i in range(count):
        click.secho("Hello, {}!".format(name), fg=color)

    items = range(100)
    with click.progressbar(items) as bar:
        for item in bar:
            time.sleep(0.03)


if __name__ == "__main__":
    cli()
