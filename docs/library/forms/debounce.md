```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from, demo_box_style
```

# Debounce

Reflex is a backend-centric framework, which can create negative performance impacts for apps taht need to provide interactive feedback to the user in real time. For example, if you have a search bar that sends a request to the backend on every keystroke, you will likely experience a laggy UI. This is because the backend is doing a lot of work to process each keystroke, and the frontend is waiting for the backend to respond before updating the UI.

Using the `rx.debounce_input`  component allows the frontend to remain responsive while receiving user input and send the value to the backend after some delay, on blur, or when `Enter` is pressed.

"Typically, this component is used to wrap a child `rx.input` or `rx.text_area`, however, most child components that accept the `value` prop and `on_change` event handler can be used with `rx.debounce_input`."

This example only sends the final checkbox state to the backend after a 1 second delay.

```python exec
class DebounceCheckboxState(rx.State):
    checked: bool = False

def debounce_checkbox_example():
    return rx.hstack(
        rx.cond(
            DebounceCheckboxState.checked,
            rx.text("Checked", color="green"),
            rx.text("Unchecked", color="red"),
        ),
        rx.debounce_input(
            rx.checkbox(
                on_change=DebounceCheckboxState.set_checked,
            ),
            debounce_timeout=1000,
        ),
    )
```

```python eval
docdemo_from(DebounceCheckboxState, component=debounce_checkbox_example)
```