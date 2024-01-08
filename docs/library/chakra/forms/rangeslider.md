```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
```

# RangeSlider

The range slider is used to allow users to make selections from a range of values.

```python exec
from typing import List

class RangeSliderState(rx.State):
    value: List[int] = [0, 100]


def range_slider_example():
    return rx.vstack(
        rx.heading(RangeSliderState.value),
        rx.range_slider(
            on_change_end=RangeSliderState.set_value
        ),
        width="100%",
    )
```

```python eval
docdemo_from(RangeSliderState, component=range_slider_example)
```

If you want to trigger state change on every slider movement, you can use the `on_change` event handler.
This is not recommended for performance reasons and should only be used if you need to perform an event on every slider movement.

```python demo
rx.vstack(
    rx.heading(RangeSliderState.value),
    rx.range_slider(
        on_change=RangeSliderState.set_value
    ),
    width="100%",
)
```
