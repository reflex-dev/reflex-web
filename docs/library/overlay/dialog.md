---
components:
    - rx.radix.themes.DialogRoot
---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```

# Dialog

```python demo
dialog_root(
    dialog_trigger(button("Open Dialog")),
    dialog_content(
        dialog_title("Welcome to Reflex!"),
        dialog_description(
            "This is a dialog component. You can render anything you want in here.",
        ),
        dialog_close(
            button("Close Dialog", size="3"),
        ),
    ),
)
```



## give in context examples 

```python demo
dialog_root(
    dialog_trigger(
        button("Edit Profile", size="4")
    ),
    dialog_content(
        dialog_title("Edit Profile"),
        dialog_description(
            "Change your profile details and preferences.",
            size="2",
            mb="4",
        ),
        flex(
            text("Name", as_="div", size="2", mb="1", weight="bold"),
            textfield_input(default_value="Freja Johnson", placeholder="Enter your name"),
            text("Email", as_="div", size="2", mb="1", weight="bold"),
            textfield_input(default_value="freja@example.com", placeholder="Enter your email"),
            direction="column",
            gap="3",
        ),
        flex(
            dialog_close(
                button("Cancel", color_scheme="gray", variant="soft"),
            ),
            dialog_close(
                button("Save"),
            ),
            gap="3",
            mt="4",
            justify="end",
        ),
    ),
)
```


```python demo
dialog_root(
    dialog_trigger(button("View users", size="4")),
    dialog_content(
        dialog_title("Users"),
        dialog_description("The following users have access to this project."),

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
            dialog_close(
                button("Close", variant="soft", color_scheme="gray"),
            ),
            gap="3",
            justify="end",
        ),
    ),
)
```