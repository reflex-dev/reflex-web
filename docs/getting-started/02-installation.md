---
from pcweb import constants
from pcweb.templates.docpage import docalert, doccode
---

# Installation

## Prerequisites

Reflex requires Python 3.7+ to get started.

For Windows users, we recommend using Windows Subsystem for Linux (WSL) for optimal performance.

For macOS users with Apple M1 or M2 chips, you may need to install Rosetta 2 to run Reflex. 
This can be done with the following command:
    
`/usr/sbin/softwareupdate --install-rosetta --agree-to-license`

## Virtual Environment (Optional)

We recommend creating a virtual environment for your project.

Below are some tools you can use to manage environments:

- [venv](constants.VENV_URL)
- [poetry](constants.POETRY_URL)

## Installing

Reflex is available as a [pip](constants.PIP_URL) package.

```bash
pip install reflex
```

```reflex
doccode(
    "$ pip install reflex",
    language="bash"
)
```

## Create a Project

Installing Reflex also installs the `reflex` command line tool.

Test that the install was successful by creating a new project. Replace `my_app_name` with your project name:

```bash
$ mkdir my_app_name
$ cd my_app_name
$ reflex init
```

This initializes a template app in your new directory.

## Run the App

You can run this app in development mode:

```bash
$ reflex run
```

You should see your app running at [http://localhost:3000](http://localhost:3000).

## Fast Refresh

Reflex has fast refreshes when running in development mode. You can modify the source code in `my_app_name/my_app_name.py` and see your changes in the browser instantly when you save your code.

## Debugging

You can debug your app by setting the `--loglevel` flag on any reflex command.

```bash
$ reflex run --loglevel debug
```
