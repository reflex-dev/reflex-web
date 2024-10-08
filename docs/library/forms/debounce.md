---
components:
    - rx.debounce_input
---

```python exec
import reflex as rx
```

# Debounce

Reflex is a backend-centric framework, which can create negative performance impacts for apps that need to provide interactive feedback to the user in real time. For example, if a search bar sends a request to the backend on every keystroke, it may result in a laggy UI. This is because the backend is doing a lot of work to process each keystroke, and the frontend is waiting for the backend to respond before updating the UI.

Using the `rx.debounce_input`  component allows the frontend to remain responsive while receiving user input and sends the value to the backend after some delay, on blur, or when `Enter` is pressed.

"Typically, this component is used to wrap a child `rx.input` or `rx.text_area`, however, most child components that accept the `value` prop and `on_change` event handler can be used with `rx.debounce_input`."

This example only sends the final radio state to the backend after a 1 second delay.

```python demo exec
class DebounceRadioState(rx.State):
    text: bool = "no selection"

def debounce_checkbox_example():
    return rx.vstack(
        rx.badge(DebounceRadioState.text, color_scheme="green"),
        rx.debounce_input(
            rx.radio(
                ["1", "2", "3"],
                on_change=DebounceRadioState.set_text,
            ),
            debounce_timeout=1000,
        ),

    )
```
