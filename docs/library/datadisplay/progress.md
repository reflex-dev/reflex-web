---
components:
    - rx.progress
    - rx.vstack
    # - rx.progress.ndicator

Progress: |
    lambda **props: rx.progress(value=50, **props)
---

```python exec
import reflex as rx
```

# Progress

Progress is used to display the progress status for a task that takes a long time or consists of several steps.

## Basic Example

`rx.progress` expects the `value` prop to set the progress value.

```python demo
rx.vstack(
    rx.progress(value=0),
    rx.progress(value=50),
    rx.progress(value=100),
    gap="1em",
    width=["20em"],
)
```

For a dynamic progress, you can assign a state variable to the `value` prop instead of a constant value.

```python demo exec
import asyncio

class ProgressState(rx.State):
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
        rx.progress(value=ProgressState.value), 
        rx.button("Start", on_click=ProgressState.start_progress),
        width="10em"
    )
```

## More Examples

### Progress with different sizes and variants
```python demo exec
rx.vstack(
    rx.progress(value=30, size="1", variant="classic"),
    rx.progress(value=50, size="2", variant="surface"),
    rx.progress(value=70, size="3", variant="soft"),
    gap="1em",
)
```


### Progress with different color schemes and high contrast
```python demo
rx.vstack(
    rx.progress(value=40, color_scheme="blue", high_contrast=False),
    rx.progress(value=60, color_scheme="green", high_contrast=True),
    rx.progress(value=80, color_scheme="red", high_contrast=False),
    gap="1em",
)
```

### Progress with custom radius
```python demo
rx.vstack(
    rx.progress(value=20, radius="none"),
    rx.progress(value=40, radius="small"),
    rx.progress(value=60, radius="medium"),
    rx.progress(value=80, radius="large"),
    rx.progress(value=100, radius="full"),
    gap="1em",
)
```

### Indeterminate progress with custom duration
```python demo
rx.vstack(
    rx.progress(duration="10s"),
    rx.progress(duration="20s"),
    rx.progress(duration="30s"),
    gap="1em",
)
```


### Combining multiple props
```python demo
rx.vstack(
    rx.progress(value=25, size="1", variant="classic", color_scheme="purple", high_contrast=True radius="small"),
    rx.progress(value=50, size="2", variant="surface", color_scheme="teal", high_contrast=False, radius="medium"),
    rx.progress(value=75, size="3", variant="soft", color_scheme="yellow", high_contrast=True, radius="large"),
    gap="1em",
)
```