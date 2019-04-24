#!/usr/bin/env python

import click

@click.argument('name', nargs=-1)
@click.command()
def cli(name):
    print("Hello, {}!".format(name))

if __name__ == "__main__":
    cli()
