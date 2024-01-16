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
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```

# Table


A semantic table for presenting tabular data.


## Basic Example

```python demo
table_root(
    table_header(
        table_row(
            table_column_header_cell("Full name"),
            table_column_header_cell("Email"),
            table_column_header_cell("Group"),
        ),
    ),
    table_body(
        table_row(
            table_row_header_cell("Danilo Sousa"),
            table_cell("danilo@example.com"),
            table_cell("Developer"),
        ),
        table_row(
            table_row_header_cell("Zahra Ambessa"),
            table_cell("zahra@example.com"),
            table_cell("Admin"),
        ),table_row(
            table_row_header_cell("Jasper Eriksson"),
            table_cell("jasper@example.com"),
            table_cell("Developer"),
        ),
    ),
)
```




## Real World Example

```python demo
rx.vstack(
    heading("Your Team"),
    text("Invite and manage your team members"),
    rx.hstack(
        textfield_root(
            textfield_input(placeholder="Email Address"),
        ),
        button("Invite"),
    ),

    table_root(
        table_body(
            table_row(
                table_cell(avatar(fallback="DS")),
                table_row_header_cell(link("Danilo Sousa")),
                table_cell("danilo@example.com"),
                table_cell("Developer"),
                align="center",
            ),
            table_row(
                table_cell(avatar(fallback="ZA")),
                table_row_header_cell(link("Zahra Ambessa")),
                table_cell("zahra@example.com"),
                table_cell("Admin"),
                align="center",
            ),
            table_row(
                table_cell(avatar(fallback="JE")),
                table_row_header_cell(link("Jasper Eriksson")),
                table_cell("jasper@example.com"),
                table_cell("Developer"),
                align="center",
            ),
        ),
    ),
)
```