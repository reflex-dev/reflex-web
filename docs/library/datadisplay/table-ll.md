---
components:
    - rx.radix.table.root
    - rx.radix.table.header
    - rx.radix.table.row
    - rx.radix.table.column_header_cell
    - rx.radix.table.body
    - rx.radix.table.cell
    - rx.radix.table.row_header_cell
---


```python exec
import reflex as rx
rdx = rx.radix
```

# Table


A semantic table for presenting tabular data.


## Basic Example

```python demo
rdx.table.root(
    rdx.table.header(
        rdx.table.row(
            rdx.table.column_header_cell("Full name"),
            rdx.table.column_header_cell("Email"),
            rdx.table.column_header_cell("Group"),
        ),
    ),
    rdx.table.body(
        rdx.table.row(
            rdx.table.row_header_cell("Danilo Sousa"),
            rdx.table.cell("danilo@example.com"),
            rdx.table.cell("Developer"),
        ),
        rdx.table.row(
            rdx.table.row_header_cell("Zahra Ambessa"),
            rdx.table.cell("zahra@example.com"),
            rdx.table.cell("Admin"),
        ),rdx.table.row(
            rdx.table.row_header_cell("Jasper Eriksson"),
            rdx.table.cell("jasper@example.com"),
            rdx.table.cell("Developer"),
        ),
    ),
)
```




## Real World Example

```python demo
rdx.flex(
    rdx.heading("Your Team"),
    rdx.text("Invite and manage your team members"),
    rdx.flex(
        rdx.text_field.input(placeholder="Email Address"),
        rdx.button("Invite"),
        justify="center",
        gap="2",
    ),
    rdx.table.root(
        rdx.table.body(
            rdx.table.row(
                rdx.table.cell(rdx.avatar(fallback="DS")),
                rdx.table.row_header_cell(rdx.link("Danilo Sousa")),
                rdx.table.cell("danilo@example.com"),
                rdx.table.cell("Developer"),
                align="center",
            ),
            rdx.table.row(
                rdx.table.cell(rdx.avatar(fallback="ZA")),
                rdx.table.row_header_cell(rdx.link("Zahra Ambessa")),
                rdx.table.cell("zahra@example.com"),
                rdx.table.cell("Admin"),
                align="center",
            ),
            rdx.table.row(
                rdx.table.cell(rdx.avatar(fallback="JE")),
                rdx.table.row_header_cell(rdx.link("Jasper Eriksson")),
                rdx.table.cell("jasper@example.com"),
                rdx.table.cell("Developer"),
                align="center",
            ),
        ),
    ),
    direction="column",
    gap="2",
)
```