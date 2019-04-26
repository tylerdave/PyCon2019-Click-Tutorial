#!/usr/bin/env python

import click


@click.command()
def cli():
    print("Hello!")


if __name__ == "__main__":
    cli()
