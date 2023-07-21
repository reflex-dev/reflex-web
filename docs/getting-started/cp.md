---
from pcweb import constants
from pcweb.templates.docpage import docalert, doccode, docheader, subheader
app_name = "app_name"
default_url = "http://localhost:3000"
---

# Installation

## Prerequisites

Reflex requires the following to get started:
* Python 3.7+
* [NodeJS 16.8.0+]({constants.NODEJS_URL})

---

## Virtual Environment (Optional)

We recommend creating a virtual environment for your project.

Below are some tools you can use to manage environments:
* [poetry]({constants.POETRY_URL})
* [pipenv]({constants.PIPENV_URL})
* [venv]({constants.VENV_URL})
* [virtualenv]({constants.VIRTUALENV_URL})
* [conda]({constants.CONDA_URL})

## Installing

Reflex is available as a [pip]({constants.PIP_URL}) package.

```bash
pip install reflex
```

## Create a Project

Installing Reflex also installs the `reflex` command line tool.

Test that the install was successful by creating a new project. Replace `app_name` with your project name.

```bash
$ mkdir app_name
$ cd app_name
$ reflex init
```

This initializes a template app in your new directory.

## Run the App

You can run this app in development mode by running:

```bash
reflex run
```

You should see your app running at [{default_url}]({default_url}).

```reflex
rx.alert(
    rx.alert_icon(),
    rx.alert_title(
        rx.markdown(
            "You can run your app on a different port with the `--frontend-port` flag. "
        ),
    ),
    status="success",
)
```

```reflex
docalert(
    "Running on Windows.",
    "We strongly advise you to use Windows Subsystem for Linux (WSL) for optimal performance"
    " when using Reflex. Due to compatibility issues with one of our dependencies, Bun,"
    " you may experience slower performance on Windows. By using WSL, you can expect to "
    "see a significant speed increase.",
    status="warning",
)
```

Reflex also starts a [FastAPI]({constants.FASTAPI_URL}) server at port `8000`.
All of your event handlers run on this server, and state changes are send to the client via websockets.

You can also debug your app by setting the `--loglevel` flag.

```bash
$ reflex run --loglevel debug
```

## Fast Refresh

Reflex has fast refresh built in when running in development mode.
You can modify the source code in `app_name/app_name.py` and see your changes in the browser instantly when you save your code.

```reflex
docalert(
    "Fast Refresh on Windows.",
    "When running on windows, the hot reload feature may not work as "
    "expected if you're running a project that resides on a different "
    "file system (eg. running your Reflex project from Windows with "
    "your project residing on the WSL file system). This is as a result "
    "of incompatibilities between the the windows file system and that of WSL."
    " It is however, recommended "
    "to run your app on the same file system your app resides.",
    status="error",
)
```

Continue reading to learn how to customize your app.
