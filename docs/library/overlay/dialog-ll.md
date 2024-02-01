---
components:
    - rx.radix.dialog.root
    - rx.radix.dialog.trigger
    - rx.radix.dialog.title
    - rx.radix.dialog.content
    - rx.radix.dialog.description
    - rx.radix.dialog.close
---

```python exec
import reflex as rx
rdx = rx.radix
```

# Dialog

```python demo
rdx.dialog.root(
    rdx.dialog.trigger(rdx.button("Open Dialog")),
    rdx.dialog.content(
        rdx.dialog.title("Welcome to Reflex!"),
        rdx.dialog.description(
            "This is a dialog component. You can render anything you want in here.",
        ),
        rdx.dialog.close(
            rdx.button("Close Dialog", size="3"),
        ),
    ),
)
```



## give in context examples 

```python demo
rdx.dialog.root(
    rdx.dialog.trigger(
        rdx.button("Edit Profile", size="4")
    ),
    rdx.dialog.content(
        rdx.dialog.title("Edit Profile"),
        rdx.dialog.description(
            "Change your profile details and preferences.",
            size="2",
            margin_bottom="16px",
        ),
        rdx.flex(
            rdx.text("Name", as_="div", size="2", margin_bottom="4px", weight="bold"),
            rdx.text_field(default_value="Freja Johnson", placeholder="Enter your name"),
            rdx.text("Email", as_="div", size="2", margin_bottom="4px", weight="bold"),
            rdx.text_field(default_value="freja@example.com", placeholder="Enter your email"),
            direction="column",
            gap="3",
        ),
        rdx.flex(
            rdx.dialog.close(
                rdx.button("Cancel", color_scheme="gray", variant="soft"),
            ),
            rdx.dialog.close(
                rdx.button("Save"),
            ),
            gap="3",
            margin_top="16px",
            justify="end",
        ),
    ),
)
```


```python demo
rdx.dialog.root(
    rdx.dialog.trigger(rdx.button("View users", size="4")),
    rdx.dialog.content(
        rdx.dialog.title("Users"),
        rdx.dialog.description("The following users have access to this project."),

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
            rdx.dialog.close(
                rdx.button("Close", variant="soft", color_scheme="gray"),
            ),
            gap="3",
            justify="end",
        ),
    ),
)
```