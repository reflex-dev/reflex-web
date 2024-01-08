# Form Control

Form control provides context such as filled/focused/error/required for form inputs.

```python demo
rx.form_control(
    rx.form_label("First Name", html_for="email"),
    rx.checkbox("Example"),
    rx.form_helper_text("This is a help text"),
    is_required=True,
)
```

The example below shows a form error when then name length is 3 or less.

```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from

class FormErrorState(rx.State):
    name: str

    @rx.var
    def is_error(self) -> bool:
         return len(self.name) <= 3

def form_state_example():
    return rx.vstack(
        rx.form_control(
            rx.input(placeholder="name", on_blur=FormErrorState.set_name),
            rx.cond(
                FormErrorState.is_error,
                rx.form_error_message("Name should be more than four characters"),
                rx.form_helper_text("Enter name"),
            ),
            is_invalid=FormErrorState.is_error,
            is_required=True,
        )
    )
```

```python eval
docdemo_from(FormErrorState, component=form_state_example)
```