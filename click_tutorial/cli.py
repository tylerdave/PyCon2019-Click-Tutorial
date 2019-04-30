#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import click

from click_tutorial.checks import ALL_CHECKS


@click.group(name="pycon")
def main(args=None):
    """PyCon Tutorial."""


@main.command()
def hello():
    """Say hello."""
    click.echo("Hello!")


@main.command()
def verify():
    """Verify that your environment is set up correctly."""
    any_failures = False
    for check_name, check_func in ALL_CHECKS.items():
        try:
            result = check_func()
            if result:
                click.secho("{:>20}: {}".format(check_name, result), fg="green")
            else:
                click.secho("{:>20}: {}".format(check_name, result), fg="red")
                any_failures = True
        except Exception as err:
            click.secho("{:>20}: ".format(check_name), fg="red", nl=False)
            click.secho(message=str(err), fg="red", bg="yellow")
            any_failures = True
    if any_failures:
        click.secho("\nVerification failed. Please see setup instructions.", fg="red")
    else:
        click.secho(
            "\nVerification successful! Your system will be albe to run the tutorial!",
            fg="blue",
        )


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
