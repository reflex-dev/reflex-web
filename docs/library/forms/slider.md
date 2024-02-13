---
components:
    - rx.radix.slider

Slider: |
    lambda **props: rx.radix.themes.slider(default_value=[40], width="100%", height="50%", **props)

---


```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
from pcweb.templates.docpage import style_grid
```


# Slider

Provides user selection from a range of values.

## Basic Example

```python demo
slider(default_value=[40], width="100%")
```


### Setting slider defaults

We can set the `min` and `max` values for the range of the slider. The defaults for `min` and `max` are 0 and 100. 

The stepping interval can also be adjusted by using the `step` prop. It defaults to 1.

The `on_value_commit` event is called when the value changes at the end of an interaction. Useful when you only need to capture a final value e.g. to update a backend service.

```python demo exec
class SliderVariationState(rx.State):
    value: int = 50

    def set_end(self, value: int):
        self.value = value

def slider_max_min_step():
    return rx.vstack(
        heading(SliderVariationState.value),
        text("Min=20 Max=240"),
        slider(default_value=[40], min=20, max=240, width="100%", on_value_commit=SliderVariationState.set_end),
        text("Step=5"),
        slider(default_value=[40], step=5, width="100%", on_value_commit=SliderVariationState.set_end),
        text("Step=0.5"),
        slider(default_value=[40], step=0.5, width="100%", on_value_commit=SliderVariationState.set_end),
        width="100%",
    )
```


### Disabling

When the `disabled` prop is set to `True`, it prevents the user from interacting with the slider.

```python demo
slider(default_value=[40], width="100%", disabled=True)
```


### Control the value

The `default_value` is the value of the slider when initially rendered. It must be passed as a `List[float]`. You can pass in more than one `float` value and this renders multiple thumbs to drag. Providing multiple values creates a range slider.


```python demo
slider(default_value=[40, 60], width="100%")
```


The `on_change` event is called when the `value` of the slider changes. 


```python demo exec
class SliderVariationState2(rx.State):
    value: int = 50

    def set_end(self, value: int):
        self.value = value


def slider_on_change():
    return rx.vstack(
        heading(SliderVariationState2.value),
        slider(default_value=[40], width="100%", on_change=SliderVariationState2.set_end),
        width="100%",
    )
```




### Submitting a form using slider

The `name` of the slider. Submitted with its owning form as part of a name/value pair.


```python demo exec
class FormSliderState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_example2():
    return rx.vstack(
        rx.form.root(
            rx.vstack(
                slider(default_value=[40], width="100%", name="slider"),
                rx.button("Submit", type_="submit"),
                width="100%",
            ),
            on_submit=FormSliderState.handle_submit,
            reset_on_submit=True,
            width="100%",
        ),
        rx.chakra.divider(),
        rx.heading("Results"),
        rx.text(FormSliderState.form_data.to_string()),
        width="100%",
    )
```



### Orientation

Use the `orientation` prop to change the orientation of the slider.

```python demo
slider(default_value=[40], width="100%", orientation="horizontal")
```

```python demo
slider(default_value=[40], height="4em", orientation="vertical")
```






## Styling

```python eval
style_grid(component_used=slider, component_used_str="slider", variants=["classic", "surface", "soft"], disabled=True, default_value=[40], width="100%",)
```

### size

```python demo
flex(
    slider(default_value=[25], size="1"),
    slider(default_value=[25], size="2"),
    slider(default_value=[25], size="3"),
    direction="column",
    spacing="4",
    width="100%",
)
```



### high contrast

```python demo
flex(
    slider(default_value=[25]),
    slider(default_value=[25], high_contrast=True),
    direction="column",
    spacing="4",
    width="100%",
)
```


### radius

```python demo
flex(
    slider(default_value=[25], radius="none"),
    slider(default_value=[25], radius="small"),
    slider(default_value=[25], radius="full"),
    direction="column",
    spacing="4",
    width="100%",
)
```



## Real World Example

