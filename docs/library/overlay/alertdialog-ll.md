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