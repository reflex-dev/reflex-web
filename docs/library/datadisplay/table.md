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
from pcweb.models import Customer
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
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Full name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Group"),
            ),
        ),
        rx.table.body(rx.foreach(TableForEachState.people, show_person)),
    )
```


It is also possible to define a `class` such as `Person` below and then iterate through this data structure, as a `list[Person]`.

```python
class Person(rx.Base):
    full_name: str
    email: str
    group: str
```



## Sorting and Filtering (Searching)


In this example we sort and filter the data. 

The state variable `_people` is set to be a backend-only variable. This is done incase the variable is very large in order to reduce network traffic and improve performance. (link to https://reflex.dev/docs/vars/base-vars/#backend-only-vars)

For sorting the `rx.select` component is used. The data is sorted based on the attributes of the `Person` class. When a `select` item is selected, as the `on_change` event trigger is hooked up to the `set_sort_value` event handler, the data is sorted based on the state variable `sort_value` attribute selected. (Every base var has a built-in event handler to set it's value for convenience, called `set_VARNAME`. link to https://reflex.dev/docs/events/setters/) 

For filtering the `rx.input` component is used. The data is filtered based on the search query entered into the `rx.input` component. When a search query is entered, as the `on_change` event trigger is hooked up to the `set_search_value` event handler, the data is filtered based on if the state variable `search_value` is present in any of the data in that specific `Person`.

`current_people` is a `rx.cached_var` (link to https://reflex.dev/docs/vars/computed-vars/#cached-vars). It is a var that is only recomputed when the other state vars it depends on change. This is to ensure that the `People` shown in the table are always up to date whenever they are searched or sorted.


```python demo exec

class Person(rx.Base):
    full_name: str
    email: str
    group: str


class TableSortingState(rx.State):
    
    _people: list[Person] = [
        Person(full_name="Danilo Sousa", email="danilo@example.com", group="Developer"),
        Person(full_name="Zahra Ambessa", email="zahra@example.com", group="Admin"),
        Person(full_name="Jasper Eriks", email="zjasper@example.com", group="B-Developer"),
    ]

    sort_value = ""
    search_value = ""

    @rx.cached_var
    def current_people(self) -> list[Person]:
        people = self._people

        if self.sort_value != "":
            people = sorted(
                people, key=lambda user: getattr(user, self.sort_value).lower()
            )

        if self.search_value != "":
            people = [
                person for person in people
                if any(
                    self.search_value in getattr(person, attr).lower()
                    for attr in ['full_name', 'email', 'group']
                )
            ]
        return people


def show_person(person: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(person.full_name),
        rx.table.cell(person.email),
        rx.table.cell(person.group),
    )

def sorting_table_example():
    return rx.vstack(
        rx.select(
            ["full_name", "email", "group"],
            placeholder="Sort By: full_name",
            on_change=TableSortingState.set_sort_value,
        ),
        rx.input(
            placeholder="Search here...",
            on_change=TableSortingState.set_search_value,
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Full name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Group"),
                ),
            ),
            rx.table.body(rx.foreach(TableSortingState.current_people, show_person)),
        ),
    )
```








# Database 

The more common use case for building an `rx.table` is to use data from a database.

The code below shows how to load data from a database and place it in an `rx.table`.


## Loading data into table

```python
class Customer(rx.Model, table=True):
    """The customer model."""

    name: str
    email: str
    phone: str
    address: str
```


```python demo exec
from sqlmodel import select

class DatabaseTableState(rx.State):

    users: list[Customer] = []

    def load_entries(self) -> list[Customer]:
        """Get all users from the database."""
        with rx.session() as session:
            self.users = session.exec(select(Customer)).all()


def show_customer(user: Customer):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.phone),
        rx.table.cell(user.address),
    )

def loading_data_table_example():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Phone"),
                rx.table.column_header_cell("Address"),
            ),
        ),
        rx.table.body(rx.foreach(DatabaseTableState.users, show_customer)),
        on_mount=DatabaseTableState.load_entries,
    )

```


If you want to load the data when the page in the app loads you can set `on_load` in `app.add_page()` to equal this event handler, like `app.add_page(page_name, on_load=State.load_entries)`.



## Sorting and Filtering (Searching)


```python
class Customer(rx.Model, table=True):
    """The customer model."""

    name: str
    email: str
    phone: str
    address: str
```


```python demo exec
from sqlmodel import select, asc, or_


class DatabaseTableState2(rx.State):

    users: list[Customer] = []

    sort_value = ""
    search_value = ""

    def load_entries(self) -> list[Customer]:
        """Get all users from the database."""
        with rx.session() as session:
            query = select(Customer)

            if self.search_value != "":
                search_value = f"%{self.search_value.lower()}%"
                query = query.where(
                    or_(
                        Customer.name.ilike(search_value),
                        Customer.email.ilike(search_value),
                        Customer.phone.ilike(search_value),
                        Customer.address.ilike(search_value),
                    )
                )

            if self.sort_value != "":
                sort_column = getattr(Customer, self.sort_value)
                order = asc(sort_column)
                query = query.order_by(order)

            self.users = session.exec(query).all()

        

    def sort_values(self, sort_value):
        self.sort_value = sort_value
        self.load_entries()

    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_entries()

def show_customer(user: Customer):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.phone),
        rx.table.cell(user.address),
    )


def loading_data_table_example2():
    return rx.vstack(
        rx.select(
            ["name", "email", "phone", "address"],
            placeholder="Sort By: Name",
            on_change= lambda value: DatabaseTableState2.sort_values(value),
        ),
        rx.input(
            placeholder="Search here...",
            on_change= lambda value: DatabaseTableState2.filter_values(value),
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Phone"),
                    rx.table.column_header_cell("Address"),
                ),
            ),
            rx.table.body(rx.foreach(DatabaseTableState2.users, show_customer)),
            on_mount=DatabaseTableState2.load_entries,
        ),
    )

```
















The real power of the `rx.table` comes where you are able to visualise, add and edit data live in your app. Check out these apps and code to see how this is done: https://customer-data-app.reflex.run and ...


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
