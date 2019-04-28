#!/usr/bin/env python

import click


@click.group()
@click.option('--verbose', is_flag=True)
@click.pass_context
def cli(ctx, verbose):
    """Displays greetings."""
    ctx.ensure_object(dict)
    ctx.obj['VERBOSE'] = verbose

@cli.command()
@click.pass_context
def hello(ctx):
    verbose = ctx.obj.get('VERBOSE')
    if verbose:
        click.echo('VERBOSE is on', err=True)
    click.echo("Hello!")

@cli.command()
@click.pass_obj
def goodbye(obj):
    verbose = obj.get('VERBOSE')
    if verbose:
        click.echo('VERBOSE is on', err=True)
    click.echo("Goodbye!")


if __name__ == "__main__":
    cli()
