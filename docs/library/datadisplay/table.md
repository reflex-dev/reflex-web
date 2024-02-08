---
components:
    - rx.table.root
    - rx.table.header
    - rx.table.row
    - rx.table.column_header_cell
    - rx.table.body
    - rx.table.cell
    - rx.table.row_header_cell
   
only_low_level:
    - True

TableRoot: |
    lambda **props: rx.radix.themes.table.root(
            rx.radix.themes.table.header(
                rx.radix.themes.table.row(
                    rx.radix.themes.table.column_header_cell("Full Name"),
                    rx.radix.themes.table.column_header_cell("Email"),
                    rx.radix.themes.table.column_header_cell("Group"),
                ),
            ),
            rx.radix.themes.table.body(
                rx.radix.themes.table.row(
                    rx.radix.themes.table.row_header_cell("Danilo Rosa"),
                    rx.radix.themes.table.cell("danilo@example.com"),
                    rx.radix.themes.table.cell("Developer"),
                ),
                rx.radix.themes.table.row(
                    rx.radix.themes.table.row_header_cell("Zahra Ambessa"),
                    rx.radix.themes.table.cell("zahra@example.com"),
                    rx.radix.themes.table.cell("Admin"),
                ),
            ),
            width="80%",
            **props,
        )

TableRow: |
    lambda **props: rx.radix.themes.table.root(
            rx.radix.themes.table.header(
                rx.radix.themes.table.row(
                    rx.radix.themes.table.column_header_cell("Full Name"),
                    rx.radix.themes.table.column_header_cell("Email"),
                    rx.radix.themes.table.column_header_cell("Group"),
                    **props,
                ),
            ),
            rx.radix.themes.table.body(
                rx.radix.themes.table.row(
                    rx.radix.themes.table.row_header_cell("Danilo Rosa"),
                    rx.radix.themes.table.cell(rx.radix.themes.text("danilo@example.com", as_="p"), rx.radix.themes.text("danilo@yahoo.com", as_="p"), rx.radix.themes.text("danilo@gmail.com", as_="p"),),
                    rx.radix.themes.table.cell("Developer"),
                    **props,
                ),
                rx.radix.themes.table.row(
                    rx.radix.themes.table.row_header_cell("Zahra Ambessa"),
                    rx.radix.themes.table.cell("zahra@example.com"),
                    rx.radix.themes.table.cell("Admin"),
                    **props,
                ),
            ),
            width="80%",
        )

TableColumnHeaderCell: |
    lambda **props: rx.radix.themes.table.root(
            rx.radix.themes.table.header(
                rx.radix.themes.table.row(
                    rx.radix.themes.table.column_header_cell("Full Name", **props,),
                    rx.radix.themes.table.column_header_cell("Email", **props,),
                    rx.radix.themes.table.column_header_cell("Group", **props,),
                ),
            ),
            rx.radix.themes.table.body(
                rx.radix.themes.table.row(
                    rx.radix.themes.table.row_header_cell("Danilo Rosa"),
                    rx.radix.themes.table.cell("danilo@example.com"),
                    rx.radix.themes.table.cell("Developer"),
                ),
                rx.radix.themes.table.row(
                    rx.radix.themes.table.row_header_cell("Zahra Ambessa"),
                    rx.radix.themes.table.cell("zahra@example.com"),
                    rx.radix.themes.table.cell("Admin"),
                ),
            ),
            width="80%",
        )
    
TableCell: |
    lambda **props: rx.radix.themes.table.root(
            rx.radix.themes.table.header(
                rx.radix.themes.table.row(
                    rx.radix.themes.table.column_header_cell("Full Name"),
                    rx.radix.themes.table.column_header_cell("Email"),
                    rx.radix.themes.table.column_header_cell("Group"),
                ),
            ),
            rx.radix.themes.table.body(
                rx.radix.themes.table.row(
                    rx.radix.themes.table.row_header_cell("Danilo Rosa"),
                    rx.radix.themes.table.cell("danilo@example.com", **props,),
                    rx.radix.themes.table.cell("Developer", **props,),
                ),
                rx.radix.themes.table.row(
                    rx.radix.themes.table.row_header_cell("Zahra Ambessa"),
                    rx.radix.themes.table.cell("zahra@example.com", **props,),
                    rx.radix.themes.table.cell("Admin", **props,),
                ),
            ),
            width="80%",
        )

TableRowHeaderCell: |
    lambda **props: rx.radix.themes.table.root(
            rx.radix.themes.table.header(
                rx.radix.themes.table.row(
                    rx.radix.themes.table.column_header_cell("Full Name"),
                    rx.radix.themes.table.column_header_cell("Email"),
                    rx.radix.themes.table.column_header_cell("Group"),
                ),
            ),
            rx.radix.themes.table.body(
                rx.radix.themes.table.row(
                    rx.radix.themes.table.row_header_cell("Danilo Rosa", **props,),
                    rx.radix.themes.table.cell("danilo@example.com"),
                    rx.radix.themes.table.cell("Developer"),
                ),
                rx.radix.themes.table.row(
                    rx.radix.themes.table.row_header_cell("Zahra Ambessa", **props,),
                    rx.radix.themes.table.cell("zahra@example.com"),
                    rx.radix.themes.table.cell("Admin"),
                ),
            ),
            width="80%",
        )
---

# Check Out Low Level Docs! High Level API Coming Soon.
