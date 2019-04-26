#!/usr/bin/env python

import click


@click.command()
@click.argument("infile", type=click.File("r"), default="-")
@click.argument("outfile", type=click.File("w"), default="-")
def cli(infile, outfile):
    text = infile.read()
    click.echo("Input length: {}".format(len(text)), err=True)
    click.echo(text, file=outfile, nl=False)


if __name__ == "__main__":
    cli()
