---
components:
    - rx.radix.themes.TableRoot
    - rx.radix.themes.TableHeader
    - rx.radix.themes.TableRow
    - rx.radix.themes.TableColumnHeaderCell
    - rx.radix.themes.TableBody
    - rx.radix.themes.TableCell
    - rx.radix.themes.TableRowHeaderCell
   
only_low_level:
    - True

TableRoot: |
    lambda **props: rx.radix.themes.table_root(
            rx.radix.themes.table_header(
                rx.radix.themes.table_row(
                    rx.radix.themes.table_column_header_cell("Full Name"),
                    rx.radix.themes.table_column_header_cell("Email"),
                    rx.radix.themes.table_column_header_cell("Group"),
                ),
            ),
            rx.radix.themes.table_body(
                rx.radix.themes.table_row(
                    rx.radix.themes.table_row_header_cell("Danilo Rosa"),
                    rx.radix.themes.table_cell("danilo@example.com"),
                    rx.radix.themes.table_cell("Developer"),
                ),
                rx.radix.themes.table_row(
                    rx.radix.themes.table_row_header_cell("Zahra Ambessa"),
                    rx.radix.themes.table_cell("zahra@example.com"),
                    rx.radix.themes.table_cell("Admin"),
                ),
            ),
            width="80%",
            **props,
        )

TableRow: |
    lambda **props: rx.radix.themes.table_root(
            rx.radix.themes.table_header(
                rx.radix.themes.table_row(
                    rx.radix.themes.table_column_header_cell("Full Name"),
                    rx.radix.themes.table_column_header_cell("Email"),
                    rx.radix.themes.table_column_header_cell("Group"),
                    **props,
                ),
            ),
            rx.radix.themes.table_body(
                rx.radix.themes.table_row(
                    rx.radix.themes.table_row_header_cell("Danilo Rosa"),
                    rx.radix.themes.table_cell(rx.radix.themes.text("danilo@example.com", as_="p"), rx.radix.themes.text("danilo@yahoo.com", as_="p"), rx.radix.themes.text("danilo@gmail.com", as_="p"),),
                    rx.radix.themes.table_cell("Developer"),
                    **props,
                ),
                rx.radix.themes.table_row(
                    rx.radix.themes.table_row_header_cell("Zahra Ambessa"),
                    rx.radix.themes.table_cell("zahra@example.com"),
                    rx.radix.themes.table_cell("Admin"),
                    **props,
                ),
            ),
            width="80%",
        )

TableColumnHeaderCell: |
    lambda **props: rx.radix.themes.table_root(
            rx.radix.themes.table_header(
                rx.radix.themes.table_row(
                    rx.radix.themes.table_column_header_cell("Full Name", **props,),
                    rx.radix.themes.table_column_header_cell("Email", **props,),
                    rx.radix.themes.table_column_header_cell("Group", **props,),
                ),
            ),
            rx.radix.themes.table_body(
                rx.radix.themes.table_row(
                    rx.radix.themes.table_row_header_cell("Danilo Rosa"),
                    rx.radix.themes.table_cell("danilo@example.com"),
                    rx.radix.themes.table_cell("Developer"),
                ),
                rx.radix.themes.table_row(
                    rx.radix.themes.table_row_header_cell("Zahra Ambessa"),
                    rx.radix.themes.table_cell("zahra@example.com"),
                    rx.radix.themes.table_cell("Admin"),
                ),
            ),
            width="80%",
        )
    
TableCell: |
    lambda **props: rx.radix.themes.table_root(
            rx.radix.themes.table_header(
                rx.radix.themes.table_row(
                    rx.radix.themes.table_column_header_cell("Full Name"),
                    rx.radix.themes.table_column_header_cell("Email"),
                    rx.radix.themes.table_column_header_cell("Group"),
                ),
            ),
            rx.radix.themes.table_body(
                rx.radix.themes.table_row(
                    rx.radix.themes.table_row_header_cell("Danilo Rosa"),
                    rx.radix.themes.table_cell("danilo@example.com", **props,),
                    rx.radix.themes.table_cell("Developer", **props,),
                ),
                rx.radix.themes.table_row(
                    rx.radix.themes.table_row_header_cell("Zahra Ambessa"),
                    rx.radix.themes.table_cell("zahra@example.com", **props,),
                    rx.radix.themes.table_cell("Admin", **props,),
                ),
            ),
            width="80%",
        )

TableRowHeaderCell: |
    lambda **props: rx.radix.themes.table_root(
            rx.radix.themes.table_header(
                rx.radix.themes.table_row(
                    rx.radix.themes.table_column_header_cell("Full Name"),
                    rx.radix.themes.table_column_header_cell("Email"),
                    rx.radix.themes.table_column_header_cell("Group"),
                ),
            ),
            rx.radix.themes.table_body(
                rx.radix.themes.table_row(
                    rx.radix.themes.table_row_header_cell("Danilo Rosa", **props,),
                    rx.radix.themes.table_cell("danilo@example.com"),
                    rx.radix.themes.table_cell("Developer"),
                ),
                rx.radix.themes.table_row(
                    rx.radix.themes.table_row_header_cell("Zahra Ambessa", **props,),
                    rx.radix.themes.table_cell("zahra@example.com"),
                    rx.radix.themes.table_cell("Admin"),
                ),
            ),
            width="80%",
        )
---

# Check Out Low Level Docs! High Level API Coming Soon.
