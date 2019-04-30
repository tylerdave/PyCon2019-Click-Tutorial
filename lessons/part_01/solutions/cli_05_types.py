#!/usr/bin/env python

import click


@click.command(name="greet")
@click.argument("names", nargs=-1)
@click.option("--int-option", type=click.INT)
@click.option("--float-option", type=click.FLOAT)
@click.option("--bool-option", type=click.BOOL)
@click.option("--choice-option", type=click.Choice(["A", "B", "C"]))
@click.option("--greeting", "-g", default="Hello", help="The greeting to display.")
@click.option("--question/--no-question", help="Make the greeting a question.")
def cli(
    names, int_option, float_option, bool_option, choice_option, greeting, question
):
    """Displays a greeting."""
    if question:
        punctuation = "?"
    else:
        punctuation = "!"
    for name in names:
        print("{}, {}{}".format(greeting, name, punctuation))
    if int_option:
        print("int: {}".format(int_option))
    if float_option:
        print("float: {}".format(float_option))
    if bool_option is not None:
        print("bool: {}".format(bool_option))
    if choice_option:
        print("choice: {}".format(choice_option))


if __name__ == "__main__":
    cli()
