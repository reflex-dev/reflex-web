```python exec
from pcweb import constants
import reflex as rx
app_name = "my_app_name"
default_url = "http://localhost:3000"
```

# Installation

## Prerequisites

Reflex requires Python 3.7+ to get started.

For Windows users, we recommend using Windows Subsystem for Linux (WSL) for optimal performance.

For macOS users with Apple M1 or M2 chips, you may need to install Rosetta 2 to run Reflex. 
This can be done with the following command:
    
`/usr/sbin/softwareupdate --install-rosetta --agree-to-license`


```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title("Error ", rx.code("command not found: reflex"),),
        rx.alert_description(
            "If you install Reflex with no virtual environment and get this error it means your PATH cannot find the reflex package. A virtual environment should solve this problem.",
        ),
    ),
    status="warning",
)
```


## Virtual Environment (Recommended)

We recommend creating a virtual environment for your project.

Below are some tools you can use to manage environments:

- [venv]({constants.VENV_URL})
- [poetry]({constants.POETRY_URL})
- [conda]({constants.CONDA_URL})

```python eval
rx.box(height=8)
```



## Installing on macOS/Linux

Reflex's recommended package manager and environment manager for macOS and Linux are [pip]({constants.PIP_URL}) and [venv]({constants.VENV_URL}), respectively. `venv` is a part of [The Python Standard Library]({constants.PYTHON_STANDARD_LIBRARY}) and comes bundled with your installation of Python. See instructions on how to install and use `pip` below.


### Install pip

Install `pip`. More details about installing pip can be found in [pip's documentation]({constants.PIP_DOCS}).

On a macOS:

```bash
python -m ensurepip --upgrade
```

```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title("Error ", rx.code("command not found: python"),),
        rx.alert_description(
            "On mac sometimes you need to write python3 instead of python",
        ),
    ),
    status="warning",
)
```

```python eval
rx.box(height=2)
```

On Ubuntu with Python 3:

```bash
sudo apt-get install python3-pip
```

For other Linux distributions, see [How to install PIP for Python]({constants.HOW_TO_INSTALL_PIP}).




### Create a new environment with Reflex

1. Create a new project folder and navigate to it. Replace `{app_name}` with your project name:

```bash
mkdir {app_name}
cd {app_name}
```

2. Create a new virtual environment in that folder and activate that environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

When you run the command above, a directory called .venv will appear in the folder {app_name} (this is a hidden folder). This directory is where your virtual environment and its dependencies are installed.



3. Reflex is available as a [pip](constants.PIP_URL) package. Install Reflex in your environment:

```bash
pip install reflex
```

4. Installing Reflex also installs the `reflex` command line tool. Test that the install was successful by running:

```bash
reflex init
```

This initializes a template app in your new directory.

When you're done using this environment, type `deactivate` to return to your normal shell.





```python eval
rx.box(height=8)
```

## Installing on Windows

Reflex's recommended environment manager on Windows is [Anaconda Navigator]({constants.ANACONDA_URL}).


### Install Anaconda

If you don't have Anaconda install yet, follow the steps provided on the [Anaconda installation page]({constants.ANACONDA_INSTALLATION}).


### Create a new environment with Reflex

Next you'll need to set up your environment.

 1. Follow the steps provided by Anaconda to [set up and manage your environment]({constants.ANACONDA_SETUP_ENVIRONMENT}) using the Anaconda Navigator.

 2. Select the "▶" icon next to your new environment. Then select "Open terminal".

 3. In the terminal that appears, type:
    ```bash
    pip install reflex
    ```
    Installing Reflex also installs the `reflex` command line tool. 
  
 4. Test that the install was successful by running:
    ```bash
    reflex init
    ```
    This initializes a template app in your new directory.



```python eval
rx.box(height=8)
```



## Run the App

You can run this app in development mode:

```bash
$ reflex run
```

You should see your app running at [http://localhost:3000](http://localhost:3000).


## Fast Refresh

Reflex has fast refreshes when running in development mode. You can modify the source code in `{app_name}/{app_name}.py` and see your changes in the browser instantly when you save your code.

## Debugging

You can debug your app by setting the `--loglevel` flag on any reflex command.

```bash
$ reflex run --loglevel debug
```
