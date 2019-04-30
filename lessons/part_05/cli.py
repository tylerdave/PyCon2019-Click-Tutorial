#!/usr/bin/env python

import click
import time


@click.group()
def cli():
    """Examples."""

@cli.command()
def editor():
    """Launch an editor."""
    message = click.edit("Prepopulated text")
    click.echo("Your message: {}".format(message))

@cli.command(name="find-app-dir")
def find_app_dir():
    """Find the appropriate application data folder."""
    click.echo(click.get_app_dir('part05'))

@cli.command()
def launch():
    """Launch applicaiton."""
    click.launch("https://click.palletsprojects.com/")


@cli.command()
@click.option("--lines", default=100)
def paging(lines):
    """Page through output."""
    data = '\n'.join(['Line %d' % num for num in range(lines)])
    click.echo_via_pager(data)


@cli.command(name="progress-bar")
@click.option('--delay', default=0.5)
@click.option('--count', default=10)
def progress_bar(count, delay):
    """Display a progress bar."""
    data = range(count)
    with click.progressbar(data) as bar:
        for number in bar:
            time.sleep(delay)


if __name__ == "__main__":
    cli()
