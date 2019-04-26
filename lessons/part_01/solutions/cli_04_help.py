#!/usr/bin/env python

import click


@click.argument("names", nargs=-1)
@click.option("--greeting", "-g", default="Hello", help="The greeting to display.")
@click.option("--question/--no-question", help="Make the greeting a question.")
@click.command(name="greet")
def cli(names, greeting, question):
    """Displays a greeting."""
    if question:
        punctuation = "?"
    else:
        punctuation = "!"
    for name in names:
        print("{}, {}{}".format(greeting, name, punctuation))


if __name__ == "__main__":
    cli()
