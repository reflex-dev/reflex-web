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
    lambda **props: rx.radix.table.root(
            rx.radix.table.header(
                rx.radix.table.row(
                    rx.radix.table.column_header_cell("Full Name"),
                    rx.radix.table.column_header_cell("Email"),
                    rx.radix.table.column_header_cell("Group"),
                ),
            ),
            rx.radix.table.body(
                rx.radix.table.row(
                    rx.radix.table.row_header_cell("Danilo Rosa"),
                    rx.radix.table.cell("danilo@example.com"),
                    rx.radix.table.cell("Developer"),
                ),
                rx.radix.table.row(
                    rx.radix.table.row_header_cell("Zahra Ambessa"),
                    rx.radix.table.cell("zahra@example.com"),
                    rx.radix.table.cell("Admin"),
                ),
            ),
            width="80%",
            **props,
        )

TableRow: |
    lambda **props: rx.radix.table.root(
            rx.radix.table.header(
                rx.radix.table.row(
                    rx.radix.table.column_header_cell("Full Name"),
                    rx.radix.table.column_header_cell("Email"),
                    rx.radix.table.column_header_cell("Group"),
                    **props,
                ),
            ),
            rx.radix.table.body(
                rx.radix.table.row(
                    rx.radix.table.row_header_cell("Danilo Rosa"),
                    rx.radix.table.cell(rx.radix.text("danilo@example.com", as_="p"), rx.radix.text("danilo@yahoo.com", as_="p"), rx.radix.text("danilo@gmail.com", as_="p"),),
                    rx.radix.table.cell("Developer"),
                    **props,
                ),
                rx.radix.table.row(
                    rx.radix.table.row_header_cell("Zahra Ambessa"),
                    rx.radix.table.cell("zahra@example.com"),
                    rx.radix.table.cell("Admin"),
                    **props,
                ),
            ),
            width="80%",
        )

TableColumnHeaderCell: |
    lambda **props: rx.radix.table.root(
            rx.radix.table.header(
                rx.radix.table.row(
                    rx.radix.table.column_header_cell("Full Name", **props,),
                    rx.radix.table.column_header_cell("Email", **props,),
                    rx.radix.table.column_header_cell("Group", **props,),
                ),
            ),
            rx.radix.table.body(
                rx.radix.table.row(
                    rx.radix.table.row_header_cell("Danilo Rosa"),
                    rx.radix.table.cell("danilo@example.com"),
                    rx.radix.table.cell("Developer"),
                ),
                rx.radix.table.row(
                    rx.radix.table.row_header_cell("Zahra Ambessa"),
                    rx.radix.table.cell("zahra@example.com"),
                    rx.radix.table.cell("Admin"),
                ),
            ),
            width="80%",
        )
    
TableCell: |
    lambda **props: rx.radix.table.root(
            rx.radix.table.header(
                rx.radix.table.row(
                    rx.radix.table.column_header_cell("Full Name"),
                    rx.radix.table.column_header_cell("Email"),
                    rx.radix.table.column_header_cell("Group"),
                ),
            ),
            rx.radix.table.body(
                rx.radix.table.row(
                    rx.radix.table.row_header_cell("Danilo Rosa"),
                    rx.radix.table.cell("danilo@example.com", **props,),
                    rx.radix.table.cell("Developer", **props,),
                ),
                rx.radix.table.row(
                    rx.radix.table.row_header_cell("Zahra Ambessa"),
                    rx.radix.table.cell("zahra@example.com", **props,),
                    rx.radix.table.cell("Admin", **props,),
                ),
            ),
            width="80%",
        )

TableRowHeaderCell: |
    lambda **props: rx.radix.table.root(
            rx.radix.table.header(
                rx.radix.table.row(
                    rx.radix.table.column_header_cell("Full Name"),
                    rx.radix.table.column_header_cell("Email"),
                    rx.radix.table.column_header_cell("Group"),
                ),
            ),
            rx.radix.table.body(
                rx.radix.table.row(
                    rx.radix.table.row_header_cell("Danilo Rosa", **props,),
                    rx.radix.table.cell("danilo@example.com"),
                    rx.radix.table.cell("Developer"),
                ),
                rx.radix.table.row(
                    rx.radix.table.row_header_cell("Zahra Ambessa", **props,),
                    rx.radix.table.cell("zahra@example.com"),
                    rx.radix.table.cell("Admin"),
                ),
            ),
            width="80%",
        )
---


```python exec
import reflex as rx
from pcweb.models import Customer
from pcweb.pages.docs import vars, events, database, library, components
```

# Table

A semantic table for presenting tabular data.

If you just want to [represent static data]({library.datadisplay.datatable.path}) then the [`rx.data_table`]({library.datadisplay.datatable.path}) might be a better fit for your use case as it comes with in-built pagination, search and sorting.

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


## Showing State data (using foreach)

Many times there is a need for the data we represent in our table to be dynamic. Dynamic data must be in `State`. Later we will show an example of how to access data from a database and how to load data from a source file.

In this example there is a `people` data structure in `State` that is [iterated through using `rx.foreach`]({components.rendering_iterables.path}).

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

The state variable `_people` is set to be a [backend-only variable]({vars.base_vars.path}). This is done incase the variable is very large in order to reduce network traffic and improve performance.

For sorting the `rx.select` component is used. The data is sorted based on the attributes of the `Person` class. When a `select` item is selected, as the `on_change` event trigger is hooked up to the `set_sort_value` event handler, the data is sorted based on the state variable `sort_value` attribute selected. (Every base var has a [built-in event handler to set]({events.setters.path}) it's value for convenience, called `set_VARNAME`.)

For filtering the `rx.input` component is used. The data is filtered based on the search query entered into the `rx.input` component. When a search query is entered, as the `on_change` event trigger is hooked up to the `set_search_value` event handler, the data is filtered based on if the state variable `search_value` is present in any of the data in that specific `Person`.

`current_people` is an [`rx.cached_var`]({vars.computed_vars.path}). It is a var that is only recomputed when the other state vars it depends on change. This is to ensure that the `People` shown in the table are always up to date whenever they are searched or sorted.


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

A `Customer` [model]({database.tables.path}) is defined that inherits from `rx.Model`.

The `load_entries` event handler executes a [query]({database.queries.path}) that is used to request information from a database table. This `load_entries` event handler is called on the `on_mount` event trigger of the `rx.table.root`. 

If you want to load the data when the page in the app loads you can set `on_load` in `app.add_page()` to equal this event handler, like `app.add_page(page_name, on_load=State.load_entries)`.


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



## Filtering (Searching) and Sorting

In this example we sort and filter the data.

For sorting the `rx.select` component is used. The data is sorted based on the attributes of the `Customer` class. When a select item is selected, as the `on_change` event trigger is hooked up to the `sort_values` event handler, the data is sorted based on the state variable `sort_value` attribute selected. 

The sorting query gets the `sort_column` based on the state variable `sort_value`, it gets the order using the `asc` function from sql and finally uses the `order_by` function.

For filtering the `rx.input` component is used. The data is filtered based on the search query entered into the `rx.input` component. When a search query is entered, as the `on_change` event trigger is hooked up to the `filter_values` event handler, the data is filtered based on if the state variable `search_value` is present in any of the data in that specific `Customer`. 

The `%` character before and after `search_value` makes it a wildcard pattern that matches any sequence of characters before or after the `search_value`. `query.where(...)` modifies the existing query to include a filtering condition. The `or_` operator is a logical OR operator that combines multiple conditions. The query will return results that match any of these conditions. `Customer.name.ilike(search_value)` checks if the `name` column of the `Customer` table matches the `search_value` pattern in a case-insensitive manner (`ilike` stands for "case-insensitive like").



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




## Pagination


Pagination is an important part of database management, especially when working with large datasets. It helps in enabling efficient data retrieval by breaking down results into manageable loads.

The purpose of this code is to retrieve a specific subset of rows from the `Customer` table based on the specified pagination parameters `offset` and `limit`.

`query.offset(self.offset)` modifies the query to skip a certain number of rows before returning the results. The number of rows to skip is specified by `self.offset`.

`query.limit(self.limit)` modifies the query to limit the number of rows returned. The maximum number of rows to return is specified by `self.limit`.



```python demo exec
from sqlmodel import select, func


class DatabaseTableState3(rx.State):

    users: list[Customer] = []
    
    total_items: int
    offset: int = 0
    limit: int = 3

    @rx.cached_var
    def page_number(self) -> int:
        return (
            (self.offset // self.limit)
            + 1
            + (1 if self.offset % self.limit else 0)
        )

    @rx.cached_var
    def total_pages(self) -> int:
        return self.total_items // self.limit + (
            1 if self.total_items % self.limit else 0
        )

    def prev_page(self):
        self.offset = max(self.offset - self.limit, 0)
        self.load_entries()

    def next_page(self):
        if self.offset + self.limit < self.total_items:
            self.offset += self.limit
        self.load_entries()

    def _get_total_items(self, session):
        """Return the total number of items in the Customer table."""
        self.total_items = session.exec(select(func.count(Customer.id))).one()


    def load_entries(self) -> list[Customer]:
        """Get all users from the database."""
        with rx.session() as session:
            query = select(Customer)

            # Apply pagination
            query = query.offset(self.offset).limit(self.limit)

            self.users = session.exec(query).all()
            self._get_total_items(session)
        

def show_customer(user: Customer):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.phone),
        rx.table.cell(user.address),
    )


def loading_data_table_example3():
    return rx.vstack(
        rx.hstack(
            rx.button(
                "Prev",
                on_click=DatabaseTableState3.prev_page,
            ),
            rx.text(
                f"Page {DatabaseTableState3.page_number} / {DatabaseTableState3.total_pages}"
            ),
            rx.button(
                "Next",
                on_click=DatabaseTableState3.next_page,
            ),
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
            rx.table.body(rx.foreach(DatabaseTableState3.users, show_customer)),
            on_mount=DatabaseTableState3.load_entries,
        ),
    )

```

## More advanced examples

The real power of the `rx.table` comes where you are able to visualise, add and edit data live in your app. Check out these apps and code to see how this is done: app: https://customer-data-app.reflex.run code: https://github.com/reflex-dev/reflex-examples/tree/main/customer_data_app and code: https://github.com/reflex-dev/data-viewer. 









# Download 

Most users will want to download their data after they have got the subset that they would like in their table. 

In this example there are buttons to download the data as a `json` and as a `csv`.

For the `json` download the `rx.download` is in the frontend code attached to the `on_click` event trigger for the button. This works because if the `Var` is not already a string, it will be converted to a string using `JSON.stringify`.

For the `csv` download the `rx.download` is in the backend code as an event_handler `download_csv_data`. There is also a helper function `_convert_to_csv` that converts the data in `self.users` to `csv` format.


```python demo exec
import io
import csv
from sqlmodel import select

class TableDownloadState(rx.State):

    users: list[Customer] = []

    def load_entries(self) -> list[Customer]:
        """Get all users from the database."""
        with rx.session() as session:
            self.users = session.exec(select(Customer)).all()


    def _convert_to_csv(self) -> str:
        """Convert the users data to CSV format."""
        
        # Make sure to load the entries first
        if not self.users:
            self.load_entries()

        # Define the CSV file header based on the Customer model's attributes
        fieldnames = list(Customer.__fields__)

        # Create a string buffer to hold the CSV data
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        for user in self.users:
            writer.writerow(user.dict())

        # Get the CSV data as a string
        csv_data = output.getvalue()
        output.close()
        return csv_data


    def download_csv_data(self):
        csv_data = self._convert_to_csv()
        return rx.download(
            data=csv_data,
            filename="data.csv",
        )


def show_customer(user: Customer):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.phone),
        rx.table.cell(user.address),
    )

def download_data_table_example():
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Phone"),
                    rx.table.column_header_cell("Address"),
                ),
            ),
            rx.table.body(rx.foreach(TableDownloadState.users, show_customer)),
            on_mount=TableDownloadState.load_entries,
        ),
        rx.hstack(
            rx.button(
                "Download as JSON",
                on_click=rx.download(
                    data=TableDownloadState.users,
                    filename="data.json",
                ),
            ),
            rx.button(
                "Download as CSV",
                on_click=TableDownloadState.download_csv_data,
            ),
            spacing="7",
        ),
        spacing="5",
    )

```


# Real World Example UI

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
