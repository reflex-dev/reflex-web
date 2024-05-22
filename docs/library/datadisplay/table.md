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


```python exec
import reflex as rx
```

# Table

A semantic table for presenting tabular data.


## Basic Example

```python demo
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Full name"),
            rx.table.column_header_cell("Email"),
            rx.table.column_header_cell("Group"),
        ),
    ),
    rx.table.body(
        rx.table.row(
            rx.table.row_header_cell("Danilo Sousa"),
            rx.table.cell("danilo@example.com"),
            rx.table.cell("Developer"),
        ),
        rx.table.row(
            rx.table.row_header_cell("Zahra Ambessa"),
            rx.table.cell("zahra@example.com"),
            rx.table.cell("Admin"),
        ),rx.table.row(
            rx.table.row_header_cell("Jasper Eriks"),
            rx.table.cell("jasper@example.com"),
            rx.table.cell("Developer"),
        ),
    ),
)
```

If you just want to represent static data then the `rx.datatable` (give link here) might be a better fit for your use case as it comes with in-built pagination, search and sorting.


## Showing State data (using foreach)

Many times there is a need for the data we represent in our table to be dynamic. Dynamic data must be in `State`. Later we will show an example of how to access data from a database and how to load data from a source file.

In this example there is a `people` data structure in `State` that is iterated through using `rx.foreach` (link to foreach docs). 

```python demo exec
class TableForEachState(rx.State):
    people: list[list] = [
        ["Danilo Sousa", "danilo@example.com", "Developer"], 
        ["Zahra Ambessa", "zahra@example.com", "Admin"], 
        ["Jasper Eriks", "jasper@example.com", "Developer"],
    ]

def show_person(person: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(person[0]),
        rx.table.cell(person[1]),
        rx.table.cell(person[2]),
    )

def foreach_table_example():
    return rx.hstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Full name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Group"),
                ),
            ),
            rx.table.body(rx.foreach(TableForEachState.people, show_person)),
        ),
    )
```


It is also possible to define a `class` such as `People` below and then iterate through this data structure, as a `list[People]`.

```python
class People(rx.Base):
    full_name: str
    email: str
    group: str
```








## Real World Example

```python demo
rx.flex(
    rx.heading("Your Team"),
    rx.text("Invite and manage your team members"),
    rx.flex(
        rx.input(placeholder="Email Address"),
        rx.button("Invite"),
        justify="center",
        spacing="2",
    ),
    rx.table.root(
        rx.table.body(
            rx.table.row(
                rx.table.cell(rx.avatar(fallback="DS")),
                rx.table.row_header_cell(rx.link("Danilo Sousa")),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Developer"),
                align="center",
            ),
            rx.table.row(
                rx.table.cell(rx.avatar(fallback="ZA")),
                rx.table.row_header_cell(rx.link("Zahra Ambessa")),
                rx.table.cell("zahra@example.com"),
                rx.table.cell("Admin"),
                align="center",
            ),
            rx.table.row(
                rx.table.cell(rx.avatar(fallback="JE")),
                rx.table.row_header_cell(rx.link("Jasper Eriksson")),
                rx.table.cell("jasper@example.com"),
                rx.table.cell("Developer"),
                align="center",
            ),
        ),
    ),
    direction="column",
    spacing="2",
)
```
