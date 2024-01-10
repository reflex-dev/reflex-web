---
components:
    - rx.radix.themes.AlertDialogTrigger
---

```python exec
import reflex as rx
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

An `alertdialog` is made up of several sub-components. The most important is the `alertdialog_root`, which contains all the parts of the dialog. 

The `alertdialog_trigger` wraps the control that will open the dialog. 

The `alertdialog_content` contains the content of the dialog. It is based on the `div` element. The `alertdialog_title` is an accessible title that is announced when the dialog is opened. This part is based on the `heading` component with a pre-defined font size and leading trim on top. 

The `alertdialog_description` is an optional accessible description that is announced when the dialog is opened. This part is based on the `text` component with a pre-defined font size. 

The `alertdialog_cancel` wraps the control that will close the dialog. This should be distinguished visually from the `alertdialog_action` wrapped control. 

The `alertdialog_action` wraps the control that will close the dialog. This should be distinguished visually from the `alertdialog_cancel` wrapped control.




Use the `inset` component to align content flush with the sides of the dialog.


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



## Examples using all the event handlers

The `on_open_change` event handler is called when the `open` state of the dialog changes. It is an event handler of the `alertdialog_root`. The controlled `open` state of the dialog prop must be used in conjunction with the `on_open_change` event handler.

```python demo
alertdialog_root(
    alertdialog_trigger(
        button("Revoke access", color_scheme="red"),
    ),
    alertdialog_content(
        alertdialog_title("Revoke access"),
        flex(
            alertdialog_action(
                button("Revoke access", color_scheme="red", variant="solid"),
            ),
        ),
    ),
    on_open_change=rx.window_alert("You just used the on_open_change event handler"),
)

```


The `on_escape_key_down` event handler is called when the escape keyboard key is down. It is an event handler of the `alertdialog_content`.

```python demo
alertdialog_root(
    alertdialog_trigger(
        button("Revoke access", color_scheme="red"),
    ),
    alertdialog_content(
        alertdialog_title("Revoke access"),
        flex(
            alertdialog_action(
                button("Revoke access", color_scheme="red", variant="solid"),
            ),
        ),
        on_escape_key_down=rx.window_alert("Escape Key Down"),
    ),
)

```