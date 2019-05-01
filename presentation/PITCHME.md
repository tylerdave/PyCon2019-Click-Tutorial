Writing Command Line Applications that Click
============================================

Instructions: http://bit.ly/pycon-click

dave@forgac.com - @tylerdave

---

Welcome to Cleveland!
=====================

# 🐍&nbsp;&nbsp;🎸&nbsp;&nbsp;🤘

---


The Goal
--------

Learn to write "well-behaved" command line applications in Python using `click`.

+++

> Well behaved?

Note:
Let's talk about what makes a command line well behaved

+++

The Unix Philosophy
-------------------

- Write programs that do one thing and do it well.
- Write programs that work together.
- Write programs to handle text streams,<br> because that is a universal interface.

Note: 
The Unix Philosophy is a set of guiding principals that influence how programs are written and are the key to these OS's power and flexibility.


+++

Do one thing
------------

Note:
A program should be self-contained and single-purposed.
This allows it to be a well-tested understandable unit.

+++

Work together
-------------

Note:
Programs should work together using standard interfaces. 
On POSIX systems this means stdin / stdout


+++

Handle text streams
-------------------

Note:
Programs should be able to read and emit text streams in order to work together.
This is what allows you to do things like run a program, using grep to filter the output, and then use less to page that output.

---

> Why?

Note:
If you make your programs work in this way you can allow users of your programs to take advantage of the rich ecosystem in ways you might not even expect.

+++

Why write CLIs?
---------------

Note:
Alternatives to CLIs are graphical programs and web interfaces.
Command line interfaces are great for repetitive tasks especially where you may want to automate them.
They're also useful as management interfaces for bigger applications.
Django's manage.py is an example of this.

+++

Why Python? 🐍
-------------

Note:
Python has a rich ecosystem of packages that do just about anything you'd want to do with a computer, from data science, to image manipulation.
Many service providers also have Python SDKs so you can use Python CLIs to drive interactions with them.
Python also makes sense when you're building a management interface for an existing Python application or service.
There are times that Python may not be best: If you need to distribute a binary, or need something very fast another language might make more sense.
If you are only calling other programs and don't have complex options then a shell script probably makes more sense

+++

Why `click`?
------------

https://click.palletsprojects.com/why/

Note:
Click is one of many CLI libraries for Python
The reasons I use it are that it encourages POSIX conventions, supports file input and output, and supports composing nested subcommands. 
It also has some nice utility features like input validation, color support, confirmation prompts, and progress bars.

---

Well Behaved CLIs
=================

+++

Arguments & Options
-------------------

```text
# Arguments:
exmaple argumentA argumentB

# Options:
example --count 3

# Option flags:
exmaple --verbose

# Arguments and Options:
example --verbose --count3 argumentA argumentB
```


+++

`stdin`/`stdout`/`stderr`
-------------------------

```text
# Read stdin:
echo "input text" | example

# Write stdout:
example > outfile.txt

# Write stdout w/ stderr:
example > outfile.txt
INFO: Generating output

# Redirect both:
example > outfile.txt 2> errfile.txt
```

+++

Exit code
---------

```text
if ! [ -x "$(example argumentA)" ]; then
  echo 'Error: running example failed.' >&2
  exit 1
fi
```

+++

`Ctrl-c` / Signals
----------------

```text
INFO: Running long process...
[Ctrl-c]
INFO: Shutting down gracefully...
```

+++

Configuration
-------------

* Mac OS X:<br>
`~/Library/Application Support/Foo Bar`
* Unix:<br>
`~/.config/foo-bar`
* Windows (non-roaming):<br>
`C:\Users\<user>\AppData\Local\Foo Bar`

+++

Colors
------

```text
cat good_outfile.txt
Output should look like this.

cat bad_outfile.txt
Output \u001b[31;1mshouln't\u001b[30;1m look like this.
```

---

Click
=====

https://click.palletsprojects.com/

+++

```python
import click

@click.command()
@click.option('--count', default=1,
              help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of 
    COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
```

+++

```text
Usage: cl.py [OPTIONS]

  Simple program that greets NAME for a total of COUNT times.

Options:
  --count INTEGER  Number of greetings.
  --name TEXT      The person to greet.
  --help           Show this message and exit.
```




---

The Tutorial
=============

+++

Installation
------------

- This repo is a Python package
- Installs commands:
  - `pycon` and `tutorial`
  - Lessons: `part01`, `part02`, `part03`
  - `pytest` and `cookiecutter`
- `pycon verify` will test your environment

+++


Tutorial-Runner
---------------

```text
Usage: tutorial [OPTIONS] COMMAND [ARGS]...

  Click tutorial runner.

Options:
--help Show this message and exit.
Commands:
check	Check your work for the current lesson.
init	(Re-)Initialize the tutorial
lesson	Switch to a specific lesson
peek	Look at the solution file without overwriting
solve	Copy the solution file to the working file.
status	Show the status of your progress.
version	Display the version of this command.
```

+++

Initialize
----------

```text
tutorial init
Tutorial initialized! Time to start your first lesson!
```

+++

Show Lesson
-----------

```text
tutorial lesson

Currently working on Part 01, Lesson 01 - Hello, PyCon!

Working file: lessons/part_01/cli.py
       Tests: lessons/part_01/tests/01_hello.py
     Command: part01
Related docs: https://click.palletsprojects.com/en/7.x/quickstart/#basic-concepts-creating-a-command

Objectives:
* Learn how to use the `tutorial` command to run and check lessons.
* Make the tests for the first lesson pass by editing the working file.
```

+++

Try running the command

```text
part01
Hello.
```

```text
part01 --help
Usage: part01 [OPTIONS]

Options:
  --help  Show this message and exit.
```



+++

Check Your Work
---------------

* Runs tests
* Outputs assertion results
* Proceeds to next lesson upon success

```text
tutorial check
```

+++

Need a hint?
------------

Display a solution file that makes test pass:

```text
tutorial peek
```

+++

Solve
-----

```text
tutorial solve
This will make a backup of the working file and then copy the solution file into place.
  Working file: lessons/part_01/cli.py
   Backup file: lessons/part_01/cli.2019-04-29.12-54-03.py
 Solution file: lessons/part_01/solutions/cli_01_hello.py
Do you wish to proceed? [y/N]:
```

Then run check to advance

```text
tutorial check
```

+++

Other Commands
--------------

Check overall status:

```text
tutorial status
```

Skip to specific lesson:

```text
tutorial lesson --part 1 --lesson 1
```

```text
tutorial lesson -p1 -l1
```

---?color=#000000;

Tutorial
========

---

# Part 01:
# Command Parsing


---

## Hello, PyCon!

```python
import click

@click.command()
def cli():
    print("Hello.")
```

+++

## 01-01: Hello, PyCon!

* Learn how to use the `tutorial` command to run and check lessons.
* Make the tests for the first lesson pass by editing the working file.

---
## Arguments

```python
@click.command()
@click.argument("names", nargs=1)
def cli(name):
    print(f"Hello, {name}.")
```

+++

## 01-02: Arguments

* Make the command accept a positional NAME argument
  * accept any number of values
  * print "Hello, NAME!" on a new line for each name given
  * output nothing if no arguments are passed (noop)

---

## Options

```python
@click.command()
@click.argument("name")
@click.option("--count", "-c", default=1)
@click.option("--green", is_flag=True)
@click.option("--debug/--no-debug")
def cli(name):
    ...
```

+++

## 01-03: Options

* Add multiple options:
  * Add `--greeting` to specify greeting text
    * With a short alias: `-g`
    * Default to "Hello" if no greeting is passed
  * Add a `--question` option as a flag that doesn't take a value
    * If passed, end the greeting with "?"
    * If not passed, end the greeting with "!"
"

---

## Help Documentation

```python
@click.command()
@click.option("--count", help="Number of times to print greeting.")
def cli(count):
    """Print a greeting."""
    ...
```

+++

## 01-04: Help Documentation

* Document your script
  * Add general command usage help
  * Add help text to the `--greeting` and `--question` options
  
---

## Input Validation

```python
@click.command()
@click.option("--example", default=1)
@click.option("--another", type=int)
@click.option("--color", type=click.Choice("red", "green", "blue"))
def cli(example, another, color):
    ...
```

+++

## 01-05: Input Validation

* Add new options to learn how type validation works
  * Output "int: {VALUE}" if `--int-option` 
  * Output "float: {VALUE}" if `--float-option` 
  * Output "bool: {VALUE}" if `--bool-option` 
  * Add `--choice-option`
    * Validate values are one of "A", "B", "C"
    * Output "choice: {VALUE}" if value passed

---

# Part 02:
# Input / Output

---

## Echo

```python
@click.command()
def cli():
    click.echo("I'm about to print...", err=True)
    
    click.echo("Hello!")
    
    click.echo(click.style("Green text!", fg="green"))
    # equivalent:
    click.secho("Green text!", fg="green")
```

+++

## 02-01: Echo

* Customize output destination and formatting
  * Make "Hello!" print to stdout
  * Make "Printing..." print to stderr
  * Add a `--red` option that makes output text red when passed

---

## File I/O

```python
@click.command()
@click.argument("infile", type=click.File("r"), default="-")
def cli(infile):
    text = infile.read()
```

+++

## 02-02: File I/O

* Read from and write to files or stdin/stdout depending on arguments
  * Read the input source and write the contents to the output
  * Accept an input file argument, reading from stdin by default (using `-` arg)
  * Accept an output file argument, writing to stdout by default (using `-` arg)
  * Find the length of the input data and print a message to stderr

---
# Part 03:
# Nested Commands

---

## Command Groups

```python
@click.group()
def example_command():
    """I'm an example command."""

@example_command.command()
def example_subcommand():
    """Says hi."""
    click.echo("Hello, world!")
```

+++

## 03-01: Command Groups

* Make a command that has subcommands
  * Add `hello` subcommand that prints "Hello!"
  * See that trying to run nonexistent subcommands results in an error

---

## Sharing Contexts

```python
@click.group()
@click.pass_context
def example_command(ctx):
    ctx.obj = {"setting": "value"}

@example_command.command()
@click.pass_context
def example_subcommand(ctx):
    sttings = ctx.obj
    click.echo(settings.get("setting"))

@example_command.command()
@click.pass_obj
def another_subcommand(obj):
    click.echo(obj.get("setting"))
```

+++

## 03-02: Sharing Contexts 

* Learn how parameters are handled by the group and by subcommands
  * Pass `--verbose` group option to `hello` subcommand via `pass_context`
  * Add a new `goodbye` subcommand
  * Pass `--verbose` group option to `goodbye` via `pass_obj`

---


# Part 04:
# Projects & Packaging

---

## 04-01: Create a Project

* Use `cookiecutter` to create a new project
* Follow the prompts to enable the CLI

+++

## 04-01: Cookiecutter Example

```text
full_name [Audrey Roy Greenfeld]: Dave Forgac
email [audreyr@example.com]: tylerdave@tylerdave.com
github_username [audreyr]: tylerdave
project_name [Python Boilerplate]: Example CLI
project_slug [example_cli]:
project_short_description [Python Boilerplate.]: An example CLI project
pypi_username [tylerdave]: tylerdave
version [0.1.0]: 0.0.1
use_pytest [n]: y
use_pypi_deployment_with_travis [y]: n
Select command_line_interface:
1 - Click
2 - No command-line interface
Choose from 1, 2 (1, 2) [1]: 1
```

---

## 04-02: Package Layout

* Explore package layout
* `setup.py`
* `setup.cfg`
* $PACKAGE_NAME/`cli.py`

---

## 04-03: Development

* Create a virtualenv
* Install the package in editable mode
* See changes reflected

---

## 04-04: Testing

* Update tests to match CLI output 

---

## 04-05: Build & Publish

* Build distribution files
* See how to publish on PyPI

---

# Part 05:
# Extras

---

## Examples

* Pagination
* Progress Bars
* Pagination
* Launch Editor
* Handle `ctrl-c`

---

Thank You!
==========

Feedback / Questions?
---------------------

dave@forgac.com

@tylerdave
