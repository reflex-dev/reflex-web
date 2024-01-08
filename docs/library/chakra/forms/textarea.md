```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
```

# Textarea

The TextArea component allows you to easily create multi-line text inputs.

```python exec
class TextareaState(rx.State):
    text: str = "Hello World!"

def textarea_example():
    return rx.vstack(
        rx.heading(TextareaState.text),
        rx.text_area(value=TextareaState.text, on_change=TextareaState.set_text)
    )
```

```python eval
docdemo_from(TextareaState, component=textarea_example)
```

Alternatively, you can use the `on_blur` event handler to only update the state when the user clicks away.

Similar to the Input component, the TextArea is also implemented using debounced input when it is fully controlled.
You can tune the debounce delay by setting the `debounce_timeout` prop.
You can find examples of how it is used in the [DebouncedInput]("/docs/library/forms/debounceinput") component.