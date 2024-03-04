# Python Package Index

```python exec
import reflex as rx
```

In order to publish a Python package, an account with the package index is required. As of **0.4.3**, Reflex only supports publishing to PyPI and TestPyPI. PyPI is short for **Python Package Index**, the official third-party software repository for Python. TestPyPI is a separate instance of index that allows users to test the distribution and installation of the package before publishing it to the real index.

## PyPI

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

## TestPyPI

TestPyPI has the same look and feel as PyPI.
