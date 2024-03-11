---
components:
    - rx.progress.root
    - rx.progress.indicator
---

```python exec
import reflex as rx
```

# Progress

Progress is used to display the progress status for a task that takes a long time or consists of several steps.

## Basic Example

`rx.progress.root` exposes the `width`, `height`, and `radius` props.

`rx.progress.indicator` accepts the `value` prop to set the progress value with
the `max` prop specifying the value at which the progress is considered
complete. Max should always be specified, because it defaults to `0`.

The color of the bar may be set to a radix color via the `color_scheme` prop.
Alternatively, the `background` or `background_color` can be specified with any
valid CSS background.

```python demo
rx.vstack(
    rx.progress.root(
        rx.progress.indicator(value=30, max=100, color_scheme="tomato"),
        radius="none",
        height="10px",
    ),
    rx.progress.root(
        rx.progress.indicator(value=50, max=100, color_scheme="amber"),
        radius="medium",
        height="15px",
    ),
    rx.progress.root(
        rx.progress.indicator(value=80, max=100, color_scheme="green"),
        radius="full",
        height="20px",
    ),
    gap="1em",
    min_width=["10em", "20em"],
)
```

For a dynamic progress, you can assign a state variable to the `value` prop instead of a constant value.

```python demo exec
import asyncio

class ProgressState2(rx.State):
    value: int = 0

    @rx.background
    async def start_progress(self):
        async with self:
            self.value = 0
        while self.value < 100:
            await asyncio.sleep(0.1)
            async with self:
                self.value += 1


def live_progress():
    return rx.hstack(
        rx.progress.root(
            rx.progress.indicator(
                value=ProgressState2.value,
                max=100,
                background="linear-gradient(90deg, rgba(131,58,180,1) 0%, rgba(253,29,29,1) 50%, rgba(252,176,69,1) 100%)",
            ), 
        ),
        rx.button("Start", on_click=ProgressState2.start_progress),
        width="10em"
    )
```
