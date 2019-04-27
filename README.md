PyCon2019 Click Tutorial
========================

[![TravisCI build status](https://travis-ci.org/tylerdave/PyCon2019-Click-Tutorial.svg?branch=master)](https://travis-ci.org/tylerdave/PyCon2019-Click-Tutorial)
[![Appveyor build status](https://ci.appveyor.com/api/projects/status/3f5kpm416lb46bjo/branch/master?svg=true)](https://ci.appveyor.com/project/tylerdave/pycon2019-click-tutorial/branch/master)

PyCon 2019 Tutorial: Writing Command Line Applications that Click

## Setup

### Prerequisites

* Python 3.5+ installed. [Python Installation Guide](https://docs.python-guide.org/starting/installation/#python-3-installation-guides)
* `virtualenv` & `pip` (Should be installed if you follow the guide above)
* Git. [Git installation instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Optional: `pipenv` or `virtualenvwrapper`
  
### Installation

This repo is a Python package. You will create a virtualenv and install the package which will install its dependencies and make new commands available.

* Open a terminal / command prompt.
  * Recommended on Windows: [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/getting-started/getting-started-with-windows-powershell?view=powershell-6) or [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
* Clone this repo:<br> `git clone https://github.com/tylerdave/PyCon2019-Click-Tutorial.git`
  * If you'd like to save a remote copy of your changes, create a new empty repo at your source code hosting service of choice and add it as a git remote:<br> `git remote add personal $NEW_REPO_URL`
* `cd` to the root of the cloned repo: <br>`cd PyCon2019-Click-Tutorial`
* Create and activate a virtualenv using your favorite method and then install the package:
  * **Recommended:** using `pipenv` ([installation instructions](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)):
    * `pipenv --python python3`
    * `pipenv shell`
    * `pipenv install`
  * If using `virtualenvwrapper`:
    * `mkvirtualenv --python python3 click-tutorial`
    * `workon click-tutorial`
    * `pip install -e .`
  * Manually:
    * `python3 -m venv env`
    * On Mac/Linux: `source env/bin/activate`
    * On Windows: `.\env\Scripts\activate`
    * `pip install -e .`
* Verify installation:<br>`pycon verify`



