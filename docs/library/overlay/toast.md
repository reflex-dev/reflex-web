---
components:
    - rx.toast.provider
---

```python exec
import reflex as rx
```

# Toast

A `rx.toast` is a non-blocking notification that disappears after a certain amount of time. It is often used to show a message to the user without interrupting their workflow.

Using the `rx.toast` function require to have a toast provider in your app.

## Toast Provider

`rx.toast.provider` is a component that provides a context for displaying toasts. It should be placed at the root of your app.

```md alert warning
In most case you will not need to include this component directly, as it is already included in `rx.app` as the `overlay_component` for displaying connections errors.
```

## Usage

You can use `rx.toast` as an event handler for any component that triggers an action.

```python
rx.button("Show Toast", on_click=rx.toast("Hello, World!"))
```

## Interaction

If you want to interact with a toast, a few props are available to customize the behavior.

By passing a `ToastAction` to the `action` or `cancel` prop, you can trigger an action when the toast is clicked or when it is closed.

```python demo
rx.button("Show Toast", on_click=rx.toast("Hello, World!", timeout=5000, close_on_click=True))
```

### Presets

`rx.toast` has some presets that you can use to show different types of toasts.

```python demo
rx.vstack(
    rx.button("Success", on_click=rx.toast.success("Success!")),
    rx.button("Error", on_click=rx.toast.error("Error!")),
    rx.button("Warning", on_click=rx.toast.warning("Warning!")),
    rx.button("Info", on_click=rx.toast.info("Info!")),
)
```

### Customization

If the presets don't fit your needs, you can customize the toast by passing to `rx.toast` some kwargs.

```python demo
rx.button(
    "Custom", 
    on_click=rx.toast(
        "Custom Toast!",
        position="top-right",
        border_radius="0.5em",
        style={"background-color": "green", "color": "white", "border": "1px solid green"}
    )
)
```