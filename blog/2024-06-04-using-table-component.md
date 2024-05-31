---
author: Tom Gotsman
date: 2024-06-04
title: Using Table Component
description: Describing main uses of the Table component with a Database
image: 
---

The table component is one of the most useful components for visualizing, editing and working with data.




## Defining the customer model

A `Customer` model is defined that inherits from `rx.Model`.

```python
class Customer(rx.Model, table=True):
    """The customer model."""

    name: str
    email: str
    phone: str
    address: str
```

more to add here .....!!!!!!!!!


## Loading Data into the Table
2. loading customers from the db (State.load_entries, show_customer used in rx.foreach(State.users, show_customer))

First it is necessary to load our data from a database. The `load_entries` event handler in `State` does a database query and returns all the date in the database to the `State` variable `self.users`.

The `show_customer` function takes in a `user` and renders it in a `rx.table.row`. It generates a list of table cell elements (`rx.table.cell`) for each attribute of the `user` object, excluding the `id` attribute. It uses a list comprehension to iterate over all field names returned by `Customer.get_fields()`, dynamically accesses each field's value with `getattr(user, field)`, and creates a cell for each field. The `*` operator unpacks the resulting list, passing the individual cell elements to the `rx.table.row`.


The `content` function renders an `rx.table` component. It uses a list comprehension that passes each field in the `Customer` model to the `rx.table.column_header_cell` function unless the field is `id`. This renders out the names of the `Customer` model fields as the titles of the table columns. 

The `State.users` var is iterated through using `rx.foreach` in this code `rx.table.body(rx.foreach(State.users, show_customer))`. The `show_customer` function is used to render each item in the `State.users` var.

Lastly the `State.load_entries` event handler is called when the `rx.table` is rendered using the `on_mount` event trigger.

```python
class State(rx.State):
    """The app state."""

    users: list[Customer] = []
    current_user: Customer = Customer()

    def load_entries(self) -> list[Customer]:
        """Get all users from the database."""
        with rx.session() as session:
            query = select(Customer)
            self.users = session.exec(query).all()


def show_customer(user: Customer):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(rx.avatar(fallback="DA")),
        *[
            rx.table.cell(getattr(user, field))
            for field in Customer.get_fields()
            if field != "id"
        ],
    )

def content():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("icon"),
                *[
                    rx.table.column_header_cell(field)
                    for field in Customer.get_fields()
                    if field != "id"
                ],
            ),
        ),
        rx.table.body(rx.foreach(State.users, show_customer)),
        on_mount=State.load_entries,
    )


app = rx.App(
    theme=rx.theme(appearance="light", has_background=True, radius="large", accent_color="grass"),
    )
app.add_page(content)
```





## Adding a New Customer 
3. adding a new customer (State.handle_add_submit, State.add_customer, add_fields, add_customer)


Next let's explore how to add a user to our database and therefore to our table. We have a function `add_customer`, which is a UI element that is rendered in the `content` function defined in the section above. 

In this `add_customer` function there is a `rx.dialog` which opens when the `rx.button` "Add New Customer" is pressed. When the dialog is opened there is an `rx.form` with a list comprehension that passes each field in the `Customer` model to the `add_fields` function unless the field is `id`.

The `add_fields` function takes the field passed and sets it as the `name` in an `rx.input`. The `name` prop is needed to submit with its owning form as part of a `name/value` pair. The content typed into the `rx.input` is submitted as the `value` in that `name/value` pair when the `rx.form` is submitted.

To submit the `rx.form` with all the `name/value` pairs added, the "submit" button is pressed which runs the code `on_submit=State.handle_add_submit` running the event handler `handle_add_submit`. This event handler sets the `State` var `current_user` to equal the form data just submitted in the `rx.form`. 

Once the `rx.form` is submitted, the "Submit Customer" `rx.button` within the `rx.dialog` is pressed and `State.add_customer_to_db` event handler is called. This event handler does a database query to add the current `self.current_user`, which we just set to be the form response. Before this a check is done to see if the `email` the user has added is already an `email` in the database, and if it is then an `rx.window_alert` is thrown. 

Finally once the new user is added to the database, the `load_entries` event handler is run again which loads all the data from the database and fills the table.


```python
class State(rx.State):
    """The app state."""

    users: list[Customer] = []
    current_user: Customer = Customer()


    def handle_add_submit(self, form_data: dict):
        """Handle the form submit."""
        self.current_user = form_data

    def add_customer_to_db(self):
        """Add a customer to the database."""
        with rx.session() as session:
            if session.exec(
                select(Customer).where(Customer.email == self.current_user["email"])
            ).first():
                return rx.window_alert("User with this email already exists")
            session.add(Customer(**self.current_user))
            session.commit()
        self.load_entries()
        return rx.window_alert(f"User \{self.current_user["name"]} has been added.")


def add_fields(field):
    return rx.flex(
        rx.text(
            field,
        ),
        rx.input(
            placeholder=field,
            name=field,
        ),
        direction="column",
    )

# this function has all styling removed to keep the code simpler and shorter
def add_customer():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.flex(
                    "Add New Customer",
                    rx.icon(tag="plus", width=24, height=24),
                ),
            ),
        ),
        rx.dialog.content(
            rx.dialog.title(
                "Customer Details",
            ),
            rx.dialog.description(
                "Add your customer profile details.",
            ),
            rx.form(
                rx.flex(
                    *[
                        add_fields(field)
                        for field in Customer.get_fields()
                        if field != "id"
                    ],
                    rx.box(
                        rx.button(
                            "Submit",
                            type="submit",
                        ),
                    ),
                    direction="column",
                ),
                on_submit=State.handle_add_submit,
                reset_on_submit=True,
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancel",
                    ),
                ),
                rx.dialog.close(
                    rx.button(
                        "Submit Customer",
                        on_click=State.add_customer_to_db,
                    ),
                ),
            ),
        ),
    )
```







4. updating a customer (State.handle_update_submit, State.update_customer, State.get_user, update_fields_and_attrs, update_customer, update in show_customer)
5. deleting a customer (State.delete_customer, delete in show_customer)
6. sorting (State.sort_values, State.load_entries, rx.select in content)
6. filtering (State.filter_values, State.load_entries, rx.input in content)
7. non-string data you want to display in the UI