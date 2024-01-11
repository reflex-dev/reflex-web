---
components:
    - rx.chakra.Drawer
    - rx.chakra.DrawerOverlay
    - rx.chakra.DrawerContent
    - rx.chakra.DrawerHeader
    - rx.chakra.DrawerBody
    - rx.chakra.DrawerFooter
---

```python exec
import reflex as rx
```

# Drawer

The Drawer component is a panel that slides out from the edge of the screen.
It can be useful when you need users to complete a task or view some details without leaving the current page.

```python demo exec
class DrawerState(rx.State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)

def drawer_example():
    return rx.vstack(
        rx.button("Show Right Drawer", on_click=DrawerState.right),
        rx.drawer(
            rx.drawer_overlay(
                rx.drawer_content(
                    rx.drawer_header("Confirm"),
                    rx.drawer_body("Do you want to confirm example?"),
                    rx.drawer_footer(
                        rx.button("Close", on_click=DrawerState.right)
                    ),
                    bg = "rgba(0, 0, 0, 0.3)"
                )
            ),
            is_open=DrawerState.show_right,
        )
    )
```

Drawer can display from the top, bottom, left, or right.
By defualt it displays to the right as seen above

```python demo
rx.vstack(
    rx.button("Show Top Drawer", on_click=DrawerState.top),
    rx.drawer(
        rx.drawer_overlay(
            rx.drawer_content(
                rx.drawer_header("Confirm"),
                rx.drawer_body("Do you want to confirm example?"),
                rx.drawer_footer(
                    rx.button("Close", on_click=DrawerState.top)
                ),
            )
        ),
        placement="top",
        is_open=DrawerState.show_top,
    )
)
```