#!/usr/bin/env python

import click

@click.argument('names', nargs=-1)
@click.command()
def cli(names):
    for name in names:
        print("Hello, {}!".format(name))

if __name__ == "__main__":
    cli()
