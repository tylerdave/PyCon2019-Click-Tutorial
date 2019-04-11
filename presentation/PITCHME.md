Writing Command Line Applications that Click
============================================

Instructions: http://bit.ly/pycon-click

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

Why?
====

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

The Tutorial
=============

+++

Installation
------------

- This repo is a Python package
- Installs `tutorial` command
- `tutorial verify` will test your environment
- For initial lessons:
  - Work in `./click_tutorial/hello.py`
  - Which is installed as `hello` command

+++

Lessons
-------

+++

Tests
-----

+++

Hints
-----

+++

Solutions
---------

+++

Need help?
----------

---?color=#000000;

Tutorial
========

---

Lesson: Hello, PyCon!
-----------------------

---

Lesson: `stdout`/`stderr`
-------------------------

---

Lesson: Arguments
-------------------

---

Lesson: Options
-----------------

---

Lesson: Input Validation
------------------------

---

Lesson: Subcommands
-------------------

---

Lesson: Prompts
---------------

---

Lesson: Package Layout
----------------------

---

Lesson: Packaging & Installing
------------------------------

---

Lesson: Reading from files
--------------------------

---

Lesson: Reading from `stdin`
----------------------------

---

Lesson: Documentation
---------------------

---

Lesson: Testing
---------------

---

Lesson: Exceptions
------------------

---

Lesson: Colors
--------------

---

Lesson: Pagination
------------------

---

Lesson: Auto-completion
-----------------------

---

Lesson: Progress Bars
---------------------

