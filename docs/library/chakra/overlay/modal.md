---
components:
    - rx.chakra.Modal
    - rx.chakra.ModalOverlay
    - rx.chakra.ModalContent
    - rx.chakra.ModalHeader
    - rx.chakra.ModalBody
    - rx.chakra.ModalFooter
---

```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
```

# Modal

A modal dialog is a window overlaid on either the primary window or another dialog window.
Content behind a modal dialog is inert, meaning that users cannot interact with it.


```python exec
class ModalState(rx.State):
    show: bool = False

    def change(self):
        self.show = not (self.show)


def modal_example():
    return rx.vstack(
    rx.button("Confirm", on_click=ModalState.change),
    rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.modal_header("Confirm"),
                rx.modal_body("Do you want to confirm example?"),
                rx.modal_footer(rx.button("Close", on_click=ModalState.change)),
            )
        ),
        is_open=ModalState.show,
    ),
)
```

```python eval
docdemo_from(ModalState, component=modal_example)
```