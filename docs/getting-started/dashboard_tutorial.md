```python exec
import reflex as rx
from pcweb.pages import docs
```

# Tutorial: Data Dashboard

During this tutorial you will build a small data dashboard, where you can input data and it will be rendered in table and a graph. This tutorial does not assume any existing Reflex knowledge, but we do recommend checking out the quick [Basics Guide]({docs.getting_started.basics.path}) first. The techniques you’ll learn in the tutorial are fundamental to building any Reflex app, and fully understanding it will give you a deep understanding of Reflex.


This tutorial is divided into ...


### What are you building?

In this tutorial, you are building an interactive data dashboard with Reflex.

You can see what it will look like when you're finished here:


!!!! ADD CODE HERE in a scrollbars !!!!



## Setup for the tutorial

Send to installation page (maybe add the commands here as well)
cd dashboard tutorial
virtual env then activate and pip install reflex
reflex init 0
end with Reflex run command to start the app and make sure set up all worked


## Overview

Now that you’re set up, let’s get an overview of Reflex!

### Inspecting the starter code

Within our `dashboard_tutorial` folder we just `cd` into, there is a `rxconfig.py` file that contains the configuration for our Reflex app. This file is where you can set the title of your app, the theme, and other configurations.

There is also an `assets` folder where static files such as images and stylesheets can be placed to be referenced within your app.

Most importantly there is a folder also called `dashboard_tutorial` which contains all the code for your app. Inside of this folder there is a file named `dashboard_tutorial.py`. To begin this tutorial we will delete all the code in this file so that we can start from scratch and explain every step as we go.

The first thing we need to do is import `reflex`. Once we have done this we must create a component, which is a a piece of reusable code that represents a part of a user interface. Components are used to render, manage, and update the UI elements in your application. 

Let's look at the example below. Here we have a function called `index` that returns a `text` component (an in-built Reflex UI component) that displays the text "Hello World!".

Next we define our app and add the component we just defined (`index`) to a page. The definition of the app and adding a component to a page are required for every Reflex app.

```python
import reflex as rx


def index() -> rx.Component:
    return rx.text("Hello World!")

app = rx.App()
app.add_page(index)
```

This code will render a page with the text "Hello World!" when you run your app like below:

```python eval
rx.text("Hello World!")
```

```md alert info
For the rest of the tutorial the `app=rx.App()` and `app.add_page` will be implied and not shown in the code snippets.
```

### Creating a table

Let's create a new component that will render a table. We will use the `table` component to do this. The `table` component has a `root`, which takes in a `header` and a `body`, which in turn take in `row` components. The `row` component takes in `cell` components which are the actual data that will be displayed in the table.

```python eval
rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.table.row(
                rx.table.cell("Danilo Sousa"),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Male"),
            ),
            rx.table.row(
                rx.table.cell("Zahra Ambessa"),
                rx.table.cell("zahra@example.com"),
                rx.table.cell("Female"),
            ),
        ),
    )
```

```python
def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.table.row(
                rx.table.cell("Danilo Sousa"),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Male"),
            ),
            rx.table.row(
                rx.table.cell("Zahra Ambessa"),
                rx.table.cell("zahra@example.com"),
                rx.table.cell("Female"),
            ),
        ),
    )
```

Components in Reflex have `props`, which can be used to customize the component and are passed in as keyword arguments to the component function. 

The `rx.table.root` component has for example the `variant` and `size` props, which customize the table as seen below.

```python eval
rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.table.row(
                rx.table.cell("Danilo Sousa"),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Male"),
            ),
            rx.table.row(
                rx.table.cell("Zahra Ambessa"),
                rx.table.cell("zahra@example.com"),
                rx.table.cell("Female"),
            ),
        ),
        variant="surface",
        size="3",
    )
```

```python
def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.table.row(
                rx.table.cell("Danilo Sousa"),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Male"),
            ),
            rx.table.row(
                rx.table.cell("Zahra Ambessa"),
                rx.table.cell("zahra@example.com"),
                rx.table.cell("Female"),
            ),
        ),
        variant="surface",
        size="3",
    )
```

## Showing dynamic data (State)

Up until this point all the data we are showing in the app is static. This is not very useful for a data dashboard. We need to be able to show dynamic data that can be added to and updated.

This is where `State` comes in. `State` is a Python class that stores variables that can change when the app is running, as well as the functions that can change those variables.

To define a state class, subclass `rx.State` and define fields that store the state of your app. The state variables (vars) should have a type annotation, and can be initialized with a default value. Check out the [basics]({docs.getting_started.basics.path}) section for a simple example of how state works.


In the example below we define a `State` class called `State` that has a variable called `users` that is a list of lists. Each list in the `users` list represents a user and contains their name, email and gender.

```python
class State(rx.State):
    users: list[list] = [
        ["Danilo Sousa", "danilo@example.com", "Male"],
        ["Zahra Ambessa", "zahra@example.com", "Female"],
    ]
```

To iterate over a state var that is a list, we use the [`rx.foreach`]({docs.components.rendering_iterables.path}) function to render a list of components. The `rx.foreach` component takes an `iterable` (list, tuple or dict) and a `function` that renders each item in the `iterable`.

Here the render function is `show_user` which takes in a single user and returns a `table.row` component that displays the users name, email and gender.

```python exec
class State1(rx.State):
    users: list[list] = [
        ["Danilo Sousa", "danilo@example.com", "Male"],
        ["Zahra Ambessa", "zahra@example.com", "Female"],
    ]

def show_user1(person: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(person[0]),
        rx.table.cell(person[1]),
        rx.table.cell(person[2]),
    )
```

```python eval
rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State1.users, show_user1
            ),
        ),
        variant="surface",
        size="3",
)
```


```python
class State(rx.State):
    users: list[list] = [
        ["Danilo Sousa", "danilo@example.com", "Male"],
        ["Zahra Ambessa", "zahra@example.com", "Female"],
    ]

def show_user(person: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(person[0]),
        rx.table.cell(person[1]),
        rx.table.cell(person[2]),
    )

def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State.users, show_user
            ),
        ),
        variant="surface",
        size="3",
)
```

As you can see the output above looks the same as before, except now the data is no longer static and can change with user input to the app.

### Using a proper class structure for our data

So far our data has been defined in a list of lists, where the data is accessed by index i.e. `user[0]`, `user[1]`. This is not very maintainable as our app gets bigger. 

A better way to structure our data in Reflex is to use a class to represent a user. This way we can access the data using attributes i.e. `user.name`, `user.email`.

In Reflex when we create these classes to showcase our data, the class must inherit from `rx.Base`.

The `show_user` render function is also updated to access the data by named attributes, instead of indexing.

```python exec
class User(rx.Base):
    """The user model."""

    name: str
    email: str
    gender: str


class State2(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female"),
    ]

def show_user2(user: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )
```

```python eval
rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State2.users, show_user2
            ),
        ),
        variant="surface",
        size="3",
)
```


```python
class User(rx.Base):
    """The user model."""

    name: str
    email: str
    gender: str


class State(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female"),
    ]

def show_user(user: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )

def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State.users, show_user
            ),
        ),
        variant="surface",
        size="3",
)
```


Next let's add a form to the app so we can add new users to the table.


## Simple form to add data 

We build a form using `rx.form`, whick takes several components such as `rx.input` and `rx.select`, which represent the form fields that allow you to add information to submit with the form. Check out here for other form components !!!!!

The `rx.input` component takes in several props. The `placeholder` prop is the text that is displayed in the input field when it is empty. The `name` prop is the name of the input field, which gets passed through in the dictionary when the form is submitted. The `required` prop is a boolean that determines if the input field is required.

The `rx.select` component takes in a list of options that are displayed in the dropdown. The other props used here are identical to the `rx.input` component.

```python demo
rx.form(
    rx.input(
        placeholder="User Name", name="name", required=True
    ),
    rx.input(
        placeholder="user@reflex.dev",
        name="email",
    ),
    rx.select(
        ["male", "female"],
        placeholder="male",
        name="gender",
    ),
)
```

This form is all very compact as you can see from the example, so we need to add some styling to make it look better. We can do this by adding a `vstack` component around the form fields. The `vstack` component stacks the form fields vertically. Check out the [layout] docs !!!! for more information on how to layout your app.


```python demo
rx.form(
    rx.vstack(
        rx.input(
            placeholder="User Name", name="name", required=True
        ),
        rx.input(
            placeholder="user@reflex.dev",
            name="email",
        ),
        rx.select(
            ["male", "female"],
            placeholder="male",
            name="gender",
        ),
    ),
)
```

Now you have probably realised that we have all the form fields, but we have no way to submit the form. We can add a submit button to the form by adding a `rx.button` component to the `vstack` component. The `rx.button` component takes in the text that is displayed on the button and the `type` prop which is the type of button. The `type` prop is set to `submit` so that the form is submitted when the button is clicked. 

In addition to this we need a way to update the `users` state variable when the form is submitted. All state changes are handled through functions in the state class, called [event handlers]({docs.events.events_overview.path}).

Components have special props called event triggers, such as `on_submit`, that can be used to make components interactive. Event triggers connect components to event handlers, which update the state.

The `on_submit` event trigger of `rx.form` is hooked up to the `add_user` event handler that is defined in the `State` class. The `add_user` event handler takes in the form data as a dictionary and appends it to the `users` state variable.


```python
class State(rx.State):
    
    ...

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))


def form():
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="User Name", name="name", required=True
            ),
            rx.input(
                placeholder="user@reflex.dev",
                name="email",
            ),
            rx.select(
                ["male", "female"],
                placeholder="male",
                name="gender",
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=State.add_user,
        reset_on_submit=True,
    )
```

Finally we must add the new `form()` component we have defined to the `index()` function so that the form is rendered on the page.

Below is the full code for the app so far. If you try this form out you will see that you can add new users to the table by filling out the form and clicking the submit button and the form data will appear as a toast on the screen.


```python exec
class State3(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female"),
    ]

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))
        

        return rx.toast.info(
            f"User has been added: {form_data}.",
            position="bottom-right",
        )

def show_user(user: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )

def form():
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="User Name", name="name", required=True
            ),
            rx.input(
                placeholder="user@reflex.dev",
                name="email",
            ),
            rx.select(
                ["male", "female"],
                placeholder="male",
                name="gender",
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=State3.add_user,
        reset_on_submit=True,
    )
```

```python eval
rx.vstack(
    form(),
    rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State3.users, show_user
            ),
        ),
        variant="surface",
        size="3",
    ),
)
```

```python
class State(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female"),
    ]

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))


def show_user(user: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )

def form():
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="User Name", name="name", required=True
            ),
            rx.input(
                placeholder="user@reflex.dev",
                name="email",
            ),
            rx.select(
                ["male", "female"],
                placeholder="male",
                name="gender",
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=State.add_user,
        reset_on_submit=True,
    )

def index() -> rx.Component:
    return rx.vstack(
        form(),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Gender"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    State.users, show_user
                ),
            ),
            variant="surface",
            size="3",
        ),
    )
```


## putting form in overlay