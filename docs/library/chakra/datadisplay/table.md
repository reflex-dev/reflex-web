```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
```

# Table

Tables are used to organize and display data efficiently.
The table component differs from the `data_table`` component in that it is not meant to display large amounts of data.
It is meant to display data in a more organized way.

Tables can be created with a shorthand syntax or by explicitly creating the table components.
The shorthand syntax is great for simple tables, but if you need more control over the table you can use the explicit syntax.

Let's start with the shorthand syntax.
The shorthand syntax has `headers`, `rows`, and `footers` props.

```python demo
rx.table_container(
    rx.table(
        headers=["Name", "Age", "Location"],
        rows=[
            ("John", 30, "New York"),
            ("Jane", 31, "San Francisco"),
            ("Joe", 32, "Los Angeles")
        ],
        footers=["Footer 1", "Footer 2", "Footer 3"],
        variant='striped'
    )
)
```

Let's create a simple table explicitly. In this example we will make a table with 2 columns: `Name` and `Age`.

```python demo
rx.table(
    rx.thead(
        rx.tr(
            rx.th("Name"),
            rx.th("Age"),
        )
    ),
    rx.tbody(
        rx.tr(
            rx.td("John"),
            rx.td(30),
        )
    ),
)
```

In the examples we will be using this data to display in a table.

```python exec
columns = ["Name", "Age", "Location"]
data = [
    ["John", 30, "New York"],
    ["Jane", 25, "San Francisco"],
]
footer = ["Footer 1", "Footer 2", "Footer 3"]
```

```python
columns = ["Name", "Age", "Location"]
data = [
    ["John", 30, "New York"],
    ["Jane", 25, "San Francisco"],
]
footer = ["Footer 1", "Footer 2", "Footer 3"]
```

Now lets create a table with the data we created.

```python eval
rx.center(
    rx.table_container(
        rx.table(
            rx.table_caption("Example Table"),
            rx.thead(
                rx.tr(
                    *[rx.th(column) for column in columns]
                )
            ),
            rx.tbody(
                *[rx.tr(*[rx.td(item) for item in row]) for row in data]
            ),
            rx.tfoot(
                rx.tr(
                    *[rx.th(item) for item in footer]
                )
            ),
        )
    )
)
```

Tables can also be styled with the variant and color_scheme arguments.

```python demo
rx.table_container(
    rx.table(
        rx.thead(
        rx.tr(
            rx.th("Name"),
            rx.th("Age"),
            rx.th("Location"),
            )
        ),
        rx.tbody(
            rx.tr(
                rx.td("John"),
                rx.td(30),
                rx.td("New York"),
            ),
            rx.tr(
                rx.td("Jane"), 
                rx.td(31),
                rx.td("San Francisco"),
            ),
            rx.tr(
                rx.td("Joe"),
                rx.td(32),
                rx.td("Los Angeles"),
            )
        ),
        variant='striped',
        color_scheme='teal'
    )
)
```
