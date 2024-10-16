---
components:
    - rx.alert_dialog.root
    - rx.alert_dialog.content
    - rx.alert_dialog.trigger
    - rx.alert_dialog.title
    - rx.alert_dialog.description
    - rx.alert_dialog.action
    - rx.alert_dialog.cancel

only_low_level:
    - True

AlertDialogRoot: |
    lambda **props: rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Revoke access"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title("Revoke access"),
            rx.alert_dialog.description(
                "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button("Cancel"),
                ),
                rx.alert_dialog.action(
                    rx.button("Revoke access"),
                ),
                spacing="3",
            ),
        ),
        **props
    )

AlertDialogContent: |
    lambda **props: rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Revoke access"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title("Revoke access"),
            rx.alert_dialog.description(
                "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button("Cancel"),
                ),
                rx.alert_dialog.action(
                    rx.button("Revoke access"),
                ),
                spacing="3",
            ),
            **props
        ),
    )
---


```python exec
import reflex as rx
```

# Alert Dialog

An alert dialog is a modal confirmation dialog that interrupts the user and expects a response.

The `alert_dialog.root` contains all the parts of the dialog.

The `alert_dialog.trigger` wraps the control that will open the dialog.

The `alert_dialog.content` contains the content of the dialog.

The `alert_dialog.title` is the title that is announced when the dialog is opened.

The `alert_dialog.description` is an optional description that is announced when the dialog is opened.

The `alert_dialog.action` wraps the control that will close the dialog. This should be distinguished visually from the `alert_dialog.cancel` control.

The `alert_dialog.cancel` wraps the control that will close the dialog. This should be distinguished visually from the `alert_dialog.action` control.

## Basic Example

```python demo
rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button("Revoke access"),
    ),
    rx.alert_dialog.content(
        rx.alert_dialog.title("Revoke access"),
        rx.alert_dialog.description(
            "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
        ),
        rx.flex(
            rx.alert_dialog.cancel(
                rx.button("Cancel"),
            ),
            rx.alert_dialog.action(
                rx.button("Revoke access"),
            ),
            spacing="3",
        ),
    ),
)
```

This example has a different color scheme and the `cancel` and `action` buttons are right aligned.

```python demo
rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button("Revoke access", color_scheme="red"),
    ),
    rx.alert_dialog.content(
        rx.alert_dialog.title("Revoke access"),
        rx.alert_dialog.description(
            "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
            size="2",
        ),
        rx.flex(
            rx.alert_dialog.cancel(
                rx.button("Cancel", variant="soft", color_scheme="gray"),
            ),
            rx.alert_dialog.action(
                rx.button("Revoke access", color_scheme="red", variant="solid"),
            ),
            spacing="3",
            margin_top="16px",
            justify="end",
        ),
        style={"max_width": 450},
    ),
)
```

Use the `inset` component to align content flush with the sides of the dialog.

```python demo
rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button("Delete Users", color_scheme="red"),
    ),
    rx.alert_dialog.content(
        rx.alert_dialog.title("Delete Users"),
        rx.alert_dialog.description(
            "Are you sure you want to delete these users? This action is permanent and cannot be undone.",
            size="2",
        ),
        rx.inset(
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Full Name"),
                        rx.table.column_header_cell("Email"),
                        rx.table.column_header_cell("Group"),
                    ),
                ),
                rx.table.body(
                    rx.table.row(
                        rx.table.row_header_cell("Danilo Rosa"),
                        rx.table.cell("danilo@example.com"),
                        rx.table.cell("Developer"),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("Zahra Ambessa"),
                        rx.table.cell("zahra@example.com"),
                        rx.table.cell("Admin"),
                    ),
                ),
            ),
            side="x",
            margin_top="24px",
            margin_bottom="24px",
        ),
        rx.flex(
            rx.alert_dialog.cancel(
                rx.button("Cancel", variant="soft", color_scheme="gray"),
            ),
            rx.alert_dialog.action(
                rx.button("Delete users", color_scheme="red"),
            ),
            spacing="3",
            justify="end",
        ),
        style={"max_width": 500},
    ),
)
```

## Events when the Alert Dialog opens or closes

The `on_open_change` event is called when the `open` state of the dialog changes. It is used in conjunction with the `open` prop.

```python demo exec
class AlertDialogState(rx.State):
    num_opens: int = 0
    opened: bool = False

    def count_opens(self, value: bool):
        self.opened = value
        self.num_opens += 1


def alert_dialog():
    return rx.flex(
        rx.heading(f"Number of times alert dialog opened or closed: {AlertDialogState.num_opens}"),
        rx.heading(f"Alert Dialog open: {AlertDialogState.opened}"),
        rx.alert_dialog.root(
            rx.alert_dialog.trigger(
                rx.button("Revoke access", color_scheme="red"),
            ),
            rx.alert_dialog.content(
                rx.alert_dialog.title("Revoke access"),
                rx.alert_dialog.description(
                    "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
                    size="2",
                ),
                rx.flex(
                    rx.alert_dialog.cancel(
                        rx.button("Cancel", variant="soft", color_scheme="gray"),
                    ),
                    rx.alert_dialog.action(
                        rx.button("Revoke access", color_scheme="red", variant="solid"),
                    ),
                    spacing="3",
                    margin_top="16px",
                    justify="end",
                ),
                style={"max_width": 450},
            ),
            on_open_change=AlertDialogState.count_opens,
        ),
        direction="column",
        spacing="3",
    )
```


## Controlling Alert Dialog with State

This example shows how to control whether the dialog is open or not with state. This is an easy way to show the dialog without needing to use the `rx.alert_dialog.trigger`.

`rx.alert_dialog.root` has a prop `open` that can be set to a boolean value to control whether the dialog is open or not.

We toggle this `open` prop with a button oustide of the dialog and the `rx.alert_dialog.cancel` and `rx.alert_dialog.action` buttons inside the dialog.


```python demo exec
class AlertDialogState2(rx.State):
    opened: bool = False

    def dialog_open(self):
        self.opened = ~self.opened


def alert_dialog2():
    return rx.box(
            rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title("Revoke access"),
            rx.alert_dialog.description(
                "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button("Cancel", on_click=AlertDialogState2.dialog_open),
                ),
                rx.alert_dialog.action(
                    rx.button("Revoke access", on_click=AlertDialogState2.dialog_open),
                ),
                spacing="3",
            ),
        ),
        open=AlertDialogState2.opened,
    ),
    rx.button("Button to Open the Dialog", on_click=AlertDialogState2.dialog_open),
)
```