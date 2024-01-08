```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
```

# Spinner

Spinners provide a visual cue that an event is either processing, awaiting a course of change or a result.

```python demo
rx.hstack(
    rx.spinner(color="red", size="xs"),
    rx.spinner(color="orange", size="sm"),
    rx.spinner(color="green", size="md"),
    rx.spinner(color="blue", size="lg"),
    rx.spinner(color="purple", size="xl"),
)
```

Along with the color you can style further with props such as speed, empty color, and thickness.

```python demo
rx.hstack(
    rx.spinner(color="lightgreen", thickness=1, speed="1s", size="xl"),
    rx.spinner(color="lightgreen", thickness=5, speed="1.5s", size="xl"),
    rx.spinner(
        color="lightgreen",
        thickness=10,
        speed="2s",
        empty_color="red",
        size="xl",
    ),
)
```