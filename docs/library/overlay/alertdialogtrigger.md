```python exec
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```


# Alert Dialog


```python demo
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
            mt="4",
            justify="end",
        ),
        style={"max_width": 450},
    ),
)

```

An `alertdialog` is made up of several sub-components. The most important is the `alertdialog_root`, which contains all the parts of the dialog. The `alertdialog_trigger` wraps the control that will open the dialog.


```python demo
alertdialog_root(
    alertdialog_trigger(
        button("Delete Users", color_scheme="red"),
    ),
    alertdialog_content(
        alertdialog_title("Delete Users"),
        alertdialog_description(
            "Are you sure you want to delete these users? This action is permanent and cannot be undone.",
            size="2",
        ),
        inset(
            table_root(
                table_header(
                    table_row(
                        table_column_header_cell("Full Name"),
                        table_column_header_cell("Email"),
                        table_column_header_cell("Group"),
                    ),
                ),
                table_body(
                    table_row(
                        table_row_header_cell("Danilo Rosa"),
                        table_cell("danilo@example.com"),
                        table_cell("Developer"),
                    ),
                    table_row(
                        table_row_header_cell("Zahra Ambessa"),
                        table_cell("zahra@example.com"),
                        table_cell("Admin"),
                    ),
                ),
            ),
            side="x",
            my="5",
        ),

        flex(

            alertdialog_cancel(
                button("Cancel", variant="soft", color_scheme="gray"),
            ),
            alertdialog_action(
                button("Delete users", color_scheme="red"),
            ),
            gap="3",
            justify="end",
        ),
        style={"max_width": 500},
    ),
)
```