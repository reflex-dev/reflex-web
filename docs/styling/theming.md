```python exec
import reflex as rx
```

# Theming

You can also add a dark mode toggle by adding `rx.toggle_color_mode` to an event trigger. This will change the whole app to dark mode.

Here is an example of a button that will change the app to dark mode:

```python
rx.button(
    rx.icon(tag="moon"),
    on_click=rx.toggle_color_mode,
)
```

```md alert warning
# Any custom colors you add will not be overwritten by the dark mode toggle.
```

```python eval
rx.box(height=4)
```

More theming options are coming soon!