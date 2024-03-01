# Custom Components Overview

```python exec
import reflex as rx
```

Reflex users create many components of their own: ready to use high level components, or nicely wrapped React components. With **Custom Components**, the community can easily share these components now. Release **0.4.3** introduces a series of `reflex component` commands that help developers wrap react components, test, and publish them as python packages.

## Prerequisites for Publishing

In order to publish a Python package, an account with the package index is required. As of **0.4.3**, Reflex only supports publishing to PyPI and TestPyPI. PyPI is short for **Python Package Index**, the official third-party software repository for Python. TestPyPI is a separate instance of index that allows users to test the distribution and installation of the package before publishing it to the real index.

### PyPI

It is straightforward to create accounts and API tokens with PyPI. There is official help on the [PyPI website](https://pypi.org/help/). For a quick reference here, go to the top right corner of the PyPI website and look for the button to register and fill out personal information.

```python eval
rx.center(
  rx.image(src="/custom_components/pypi_register.png", width="400px", border_radius="15px", border="1px solid"),
)
```

A user can use username and password to authenticate with PyPI when publishing. Reflex does not store your PyPI credentials. If an API token is preferred, it can be generated in the account settings.

```python eval
rx.center(
  rx.image(src="/custom_components/pypi_account_settings.png", width="400px", border_radius="15px", border="1px solid"),
)
```

Scroll down to the API tokens section and click on the "Add API token" button. Fill out the form and click "Generate API token".

```python eval
rx.center(
  rx.image(src="/custom_components/pypi_api_tokens.png", width="700px", border_radius="15px", border="1px solid"),
)
```

### TestPyPI

TestPyPI has the same look and feel as PyPI.

## Quick Start

First create a new folder for your custom component project, for example `color_picker`. The package name will be `reflex-color-picker`. The prefix `reflex-` is intentionally added for all custom components for easy search on PyPI. If you prefer a particular name for the package, you can either change it manually in the `pyproject.toml` file or add the `--library-name` option in the `reflex component init` command initially.

Run `reflex component init`, and a set of files and folders will be created in the `color_picker` folder. The `pyproject.toml` file is the configuration file for the project. The `custom_components` folder is where the custom component implementation is. The `color_picker_demo` folder is a demo Reflex app that uses the custom component. If this is the first time of creating python packages, it is encouraged to browse through all the files (there are not that many) to understand the structure of the project.

```python eval
rx.code_block("""
color_picker/
├── pyproject.toml
├── README.md
├── custom_components/
│   └── reflex_color_picker/
│       ├── color_picker.py
│       └── __init__.py
└── color_picker_demo/
    └── assets/
        color_picker_demo/
        requirements.txt
        rxconfig.py
""",
  language="bash",
)
```

After finishing the custom component implementation, the user is encouraged to fully test it before publishing. The generated Reflex demo app `color_picker_demo` is a good place to start. It is a regular Reflex app prefilled with imports and usage of this component. During the init, the `custom_component` folder is installed locally in editable mode, so a developer can incrementally develop and test with ease. The changes in component implementation are automatically reflected in the demo app.

Run `reflex component build` to build. The end result is a `dist` folder containing the distribution files. The user does not need to do anything manually with these distribution files.

Once ready to publish, execute `reflex component publish` with the credentials in the command options (either `--username` and `--password` together or `--token`). The same version of the package can only be published once. If already exists, the publish ends in error. The user can go to the `pyproject.toml` file and update the version number as desired. After the publish command finishes successfully, the package is uploaded to PyPI. 🎉
