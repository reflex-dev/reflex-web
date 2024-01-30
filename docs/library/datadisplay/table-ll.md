---
components:
    - rx.radix.themes.TableRoot
    - rx.radix.themes.TableHeader
    - rx.radix.themes.TableRow
    - rx.radix.themes.TableColumnHeaderCell
    - rx.radix.themes.TableBody
    - rx.radix.themes.TableCell
    - rx.radix.themes.TableRowHeaderCell
    
---


```python exec
import reflex as rx
import reflex.components.radix.themes as rdxt
```

# Table


A semantic table for presenting tabular data.


## Basic Example

```python demo
rdxt.table_root(
    rdxt.table_header(
        rdxt.table_row(
            rdxt.table_column_header_cell("Full name"),
            rdxt.table_column_header_cell("Email"),
            rdxt.table_column_header_cell("Group"),
        ),
    ),
    rdxt.table_body(
        rdxt.table_row(
            rdxt.table_row_header_cell("Danilo Sousa"),
            rdxt.table_cell("danilo@example.com"),
            rdxt.table_cell("Developer"),
        ),
        rdxt.table_row(
            rdxt.table_row_header_cell("Zahra Ambessa"),
            rdxt.table_cell("zahra@example.com"),
            rdxt.table_cell("Admin"),
        ),rdxt.table_row(
            rdxt.table_row_header_cell("Jasper Eriksson"),
            rdxt.table_cell("jasper@example.com"),
            rdxt.table_cell("Developer"),
        ),
    ),
)
```




## Real World Example

```python demo
rdxt.flex(
    rdxt.heading("Your Team"),
    rdxt.text("Invite and manage your team members"),
    rdxt.flex(
        rdxt.textfield_input(placeholder="Email Address"),
        rdxt.button("Invite"),
        justify="center",
        gap="2",
    ),
    rdxt.table_root(
        rdxt.table_body(
            rdxt.table_row(
                rdxt.table_cell(rdxt.avatar(fallback="DS")),
                rdxt.table_row_header_cell(rdxt.link("Danilo Sousa")),
                rdxt.table_cell("danilo@example.com"),
                rdxt.table_cell("Developer"),
                align="center",
            ),
            rdxt.table_row(
                rdxt.table_cell(rdxt.avatar(fallback="ZA")),
                rdxt.table_row_header_cell(rdxt.link("Zahra Ambessa")),
                rdxt.table_cell("zahra@example.com"),
                rdxt.table_cell("Admin"),
                align="center",
            ),
            rdxt.table_row(
                rdxt.table_cell(rdxt.avatar(fallback="JE")),
                rdxt.table_row_header_cell(rdxt.link("Jasper Eriksson")),
                rdxt.table_cell("jasper@example.com"),
                rdxt.table_cell("Developer"),
                align="center",
            ),
        ),
    ),
    direction="column",
    gap="2",
)
```