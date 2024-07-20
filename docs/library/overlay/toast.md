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

If the presets don't fit your needs, you can customize the toasts by passing to `rx.toast` or to `rx.toast.options` some kwargs.

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

The following props are available for customization:

- `description`: `str | Var`: Toast's description, renders underneath the title.
- `close_button`: `bool`: Whether to show the close button.    
- `invert`: `bool`: Dark toast in light mode and vice versa.
- `important`: `bool`: Control the sensitivity of the toast for screen readers.
- `duration`: `int`: Time in milliseconds that should elapse before automatically closing the toast.
- `position`: `LiteralPosition`: Position of the toast.
- `dismissible`: `bool`: If false, it'll prevent the user from dismissing the toast.
- `action`: `ToastAction`: Renders a primary button, clicking it will close the toast.
- `cancel`: `ToastAction`: Renders a secondary button, clicking it will close the toast.
- `id`: `str | Var`: Custom id for the toast.
- `unstyled`: `bool`: Removes the default styling, which allows for easier customization.
- `style`: `Style`: Custom style for the toast.
- `on_dismiss`: `Any`: The function gets called when either the close button is clicked, or the toast is swiped.
- `on_auto_close`: `Any`: Function that gets called when the toast disappears automatically after it's timeout (`duration` prop).
