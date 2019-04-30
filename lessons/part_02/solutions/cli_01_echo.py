#!/usr/bin/env python

import click


@click.option("--red", is_flag=True)
@click.command()
def cli(red):
    click.echo("Printing...", err=True)
    if red:
        color = "red"
    else:
        color = None
    click.secho("Hello!", fg=color)


if __name__ == "__main__":
    cli()
