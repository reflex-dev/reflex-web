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
            "If you install Reflex with no virtual environment and get this error it means your PATH cannot find the reflex package. A virtual environment should solve this problem, or you can try running ", rx.code("python3 -m"), " before the reflex command.",
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
rx.box(height=6)
```



## Installing on macOS/Linux

Reflex's recommended environment manager for macOS and Linux is [venv]({constants.VENV_URL}). `venv` is a part of [The Python Standard Library]({constants.PYTHON_STANDARD_LIBRARY}) and comes bundled with your installation of Python. 


On Ubuntu with Python 3 we must run the command:

```bash
$ sudo apt-get install python3-pip python3-venv
```


### Create a new environment with Reflex

1. Create a new project folder and navigate to it. Replace `{app_name}` with your project name:

```bash
$ mkdir {app_name}
$ cd {app_name}
```

2. Create a new virtual environment in that folder and activate that environment:

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

When you run the command above, a directory called .venv will appear in the folder {app_name} (this is a hidden folder). This directory is where your virtual environment and its dependencies are installed.



3. Reflex is available as a [pip](constants.PIP_URL) package. Install Reflex in your environment:

```bash
$ pip install reflex
```

4. Installing Reflex also installs the `reflex` command line tool. Test that the install was successful by running:

```bash
$ reflex init
```

This initializes a template app in your new directory.


5. Run the demo app to get an idea of what you can build with Reflex:

```bash
$ reflex demo
```


When you're done using this environment, type `deactivate` to return to your normal shell.




```python eval
rx.box(height=8)
```




## Installing on Windows

Reflex's recommended environment manager for Windows is [venv]({constants.VENV_URL}). `venv` is a part of [The Python Standard Library]({constants.PYTHON_STANDARD_LIBRARY}) and comes bundled with your installation of Python. 



### Create a new environment with Reflex

1. Create a new project folder and navigate to it. Replace `{app_name}` with your project name:

```bash
> mkdir {app_name}
> cd {app_name}
```

2. Create a new virtual environment in that folder and activate that environment:

```bash
> py -3 -m venv .venv
> .venv\\Scripts\\activate
```

When you run the command above, a directory called .venv will appear in the folder {app_name} (this is a hidden folder). This directory is where your virtual environment and its dependencies are installed.


3. Reflex is available as a [pip](constants.PIP_URL) package. Install Reflex in your environment:

```bash
> pip install reflex
```

4. Installing Reflex also installs the `reflex` command line tool. Test that the install was successful by running:

```bash
> reflex init
```

This initializes a template app in your new directory.


5. Run the demo app to get an idea of what you can build with Reflex:

```bash
$ reflex demo
```


When you're done using this environment, type `deactivate` to return to your normal shell.



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
