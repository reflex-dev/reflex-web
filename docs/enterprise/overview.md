# Reflex Enterprise

```python exec
import reflex as rx
```

Reflex Enterprise is a package containing premium features built on top of Reflex designed to help you build enterprise-grade applications faster.

See complete docs at [Enterprise Docs](https://enterprise.reflex.dev)

## Features

So far the enterprise package contains the following features:

- AgGrid and AgCharts
- Single Port Proxy

More features will be added in the future. If you have any feature requests, please [open an issue](https://github.com/reflex-dev/reflex/issues/new/choose).

## Installation of reflex_enterprise.

```bash
pip install reflex-enterprise
```

## Usage of reflex_enterprise.

Using `rxe.App` as your `app` is required to use any of the components provided by the enterprise package, as well as config options provided by `rxe.Config`.

### In the main file

Instead of the usual `rx.App()` to create your app, use the following:
```python
import reflex_enterprise as rxe
rxe.App()
```

### In rxconfig.py
```python
import reflex_enterprise as rxe
config = rxe.Config(
    app_name="MyApp",
    ... # you can pass all rx.Config arguments as well as the one specific to rxe.Config
)
```

## Pricing

Unlike the open source `reflex` package, the `reflex-enterprise` package is free to use for all users but requires a paid tier to remove [branding](https://enterprise.reflex.dev/built-with-reflex/).