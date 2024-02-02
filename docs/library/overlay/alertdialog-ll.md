---
components:
    - rx.radix.alert_dialog.root
    - rx.radix.alert_dialog.content
    - rx.radix.alert_dialog.trigger
    - rx.radix.alert_dialog.title
    - rx.radix.alert_dialog.description
    - rx.radix.alert_dialog.action
    - rx.radix.alert_dialog.cancel
---

```python exec
import reflex as rx
rdx = rx.radix
```


# Alert Dialog

An alert dialog is a modal confirmation dialog that interrupts the user and expects a response.

The `alertdialog_root` contains all the parts of the dialog.

The `alertdialog_trigger` wraps the control that will open the dialog.

The `alertdialog_content` contains the content of the dialog.

The `alertdialog_title` is the title that is announced when the dialog is opened.

The `alertdialog_description` is an optional description that is announced when the dialog is opened.

The `alertdialog_action` wraps the control that will close the dialog. This should be distinguished visually from the `alertdialog_cancel` control.

The `alertdialog_cancel` wraps the control that will close the dialog. This should be distinguished visually from the `alertdialog_action` control.


## Basic Example

```python demo
alertdialog_root(
    alertdialog_trigger(
        button("Revoke access"),
    ),
    alertdialog_content(
        alertdialog_title("Revoke access"),
        alertdialog_description(
            "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
        ),
        flex(
            alertdialog_cancel(
                button("Cancel"),
            ),
            alertdialog_action(
                button("Revoke access"),
            ),
            gap="3",
        ),
    ),
)
```





```python demo
rdx.alert_dialog.root(
    rdx.alert_dialog.trigger(
        rdx.button("Revoke access", color_scheme="red"),
    ),
    rdx.alert_dialog.content(
        rdx.alert_dialog.title("Revoke access"),
        rdx.alert_dialog.description(
            "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
            size="2",
        ),
        rdx.flex(
            rdx.alert_dialog.cancel(
                rdx.button("Cancel", variant="soft", color_scheme="gray"),
            ),
            rdx.alert_dialog.action(
                rdx.button("Revoke access", color_scheme="red", variant="solid"),
            ),
            gap="3",
            margin_top="16px",
            justify="end",
        ),
        style={"max_width": 450},
    ),
)
```

Use the `inset` component to align content flush with the sides of the dialog.


```python demo
rdx.alert_dialog.root(
    rdx.alert_dialog.trigger(
        rdx.button("Delete Users", color_scheme="red"),
    ),
    rdx.alert_dialog.content(
        rdx.alert_dialog.title("Delete Users"),
        rdx.alert_dialog.description(
            "Are you sure you want to delete these users? This action is permanent and cannot be undone.",
            size="2",
        ),
        rdx.inset(
            rdx.table.root(
                rdx.table.header(
                    rdx.table.row(
                        rdx.table.column_header_cell("Full Name"),
                        rdx.table.column_header_cell("Email"),
                        rdx.table.column_header_cell("Group"),
                    ),
                ),
                rdx.table.body(
                    rdx.table.row(
                        rdx.table.row_header_cell("Danilo Rosa"),
                        rdx.table.cell("danilo@example.com"),
                        rdx.table.cell("Developer"),
                    ),
                    rdx.table.row(
                        rdx.table.row_header_cell("Zahra Ambessa"),
                        rdx.table.cell("zahra@example.com"),
                        rdx.table.cell("Admin"),
                    ),
                ),
            ),
            side="x",
            margin_top="24px",
            margin_bottom="24px",
        ),
        rdx.flex(
            rdx.alert_dialog.cancel(
                rdx.button("Cancel", variant="soft", color_scheme="gray"),
            ),
            rdx.alert_dialog.action(
                rdx.button("Delete users", color_scheme="red"),
            ),
            gap="3",
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
    return flex(
        heading(f"Number of times alert dialog opened or closed: {AlertDialogState.num_opens}"),
        heading(f"Alert Dialog open: {AlertDialogState.opened}"),
        alertdialog_root(
            alertdialog_trigger(
                button("Revoke access", color_scheme="red"),
            ),
            alertdialog_content(
                alertdialog_title("Revoke access"),
                alertdialog_description(
                    "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
                    size="2",
                ),
                flex(
                    alertdialog_cancel(
                        button("Cancel", variant="soft", color_scheme="gray"),
                    ),
                    alertdialog_action(
                        button("Revoke access", color_scheme="red", variant="solid"),
                    ),
                    gap="3",
                    margin_top="16px",
                    justify="end",
                ),
                style={"max_width": 450},
            ),
            on_open_change=AlertDialogState.count_opens,
        ),
        direction="column",
        gap="3",
    )
```



## Changing the size

The `size` of `alertdialog` can be changed. The `alertdialog` on the right hand side has no `size` props set. The one on the left hand side has `size` set to `1` for all subcomponents including `alertdialog_trigger`, `alertdialog_content`, `alertdialog_title`, `alertdialog_description`, `alertdialog_cancel` and `alertdialog_action`. The `size` prop can take any value of `1, 2, 3, 4`.

```python demo
flex(
    alertdialog_root(
        alertdialog_trigger(
            button("Revoke access", color_scheme="red"),
            size="1",
        ),
        alertdialog_content(
            alertdialog_title("Revoke access", size="1",),
            alertdialog_description(
                "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
                size="1",
            ),
            flex(
                alertdialog_cancel(
                    button("Cancel", variant="soft", color_scheme="gray"),
                    size="1",
                ),
                alertdialog_action(
                    button("Revoke access", color_scheme="red", variant="solid"),
                    size="1",
                ),
                gap="3",
                margin_top="16px",
                justify="end",
            ),
            style={"max_width": 450},
            size="1",
        ),
    ),
    alertdialog_root(
        alertdialog_trigger(
            button("Revoke access", color_scheme="red"),
        ),
        alertdialog_content(
            alertdialog_title("Revoke access"),
            alertdialog_description(
                "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
            ),
            flex(
                alertdialog_cancel(
                    button("Cancel", variant="soft", color_scheme="gray"),
                ),
                alertdialog_action(
                    button("Revoke access", color_scheme="red", variant="solid"),
                ),
                gap="3",
                margin_top="16px",
                justify="end",
            ),
            style={"max_width": 450},
        ),
    ),
    gap="3",
)
```