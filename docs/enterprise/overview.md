# Reflex Enterprise

```python exec
import reflex as rx
```

Reflex Enterprise is a package containing paid features built on top of Reflex.

See complete docs at [Enterprise Docs](https://enterprise.reflex.dev)

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

