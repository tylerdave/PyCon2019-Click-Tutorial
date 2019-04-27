#!/usr/bin/env python

import click


@click.command()
@click.argument("names", nargs=-1)
def cli(names):
    for name in names:
        print("Hello, {}!".format(name))


if __name__ == "__main__":
    cli()
