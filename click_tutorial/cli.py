import sys
import click

from click_tutorial.checks import ALL_CHECKS
from click_tutorial import state


@click.group()
def tutorial(args=None):
    """Click tutorial runner."""


@tutorial.command()
def hint():
    """Get a hint for the current lesson."""
    click.echo("Hints coming soon!")


@tutorial.command()
@click.option(
    "--reinitialize",
    "-r",
    is_flag=True,
    help="Clear progress and reinitialize tutorial.",
)
def init(reinitialize):
    """(Re-)Initialize the tutorial"""
    if state.is_initialized() and reinitialize is not True:
        click.confirm(
            "Already initialized. Do you want to clear progress and start over?",
            abort=True,
        )
    state.initialize()
    click.echo("Tutorial initialized! Time to start your first lesson!")


@tutorial.command()
def status():
    """Show the status of your progress."""
    click.echo("OK")


@tutorial.command()
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
            "\nVerification successful! You're ready to run the tutorial!", fg="blue"
        )


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
