```python exec
import reflex as rx
from typing import Any
```

# Substates

Substates allow you to break up your state into multiple classes to make it more manageable. This is useful as your app
grows, as it allows you to think about each page as a separate entity. Substates also allow you to share common state
resources, such as variables or event handlers.

When a particular state class becomes too large, breaking it up into several substates can bring performance
benefits by only loading parts of the state that are used to handle a certain event.

## Multiple States

One common pattern is to create a substate for each page in your app.
This allows you to think about each page as a separate entity, and makes it easier to manage your code as your app grows.

To create a substate, simply inherit from `rx.State` multiple times:

```python
# index.py
import reflex as rx

class IndexState(rx.State):
    """Define your main state here."""
    data: str = "Hello World"


@rx.page()
def index():
    return rx.box(rx.text(IndexState.data)

# signup.py
import reflex as rx


class SignupState(rx.State):
    """Define your signup state here."""
    username: str = ""
    password: str = ""

    def signup(self):
        ...


@rx.page()
def signup_page():
    return rx.box(
        rx.input(value=SignupState.username),
        rx.input(value=SignupState.password),
    )

# login.py
import reflex as rx

class LoginState(rx.State):
    """Define your login state here."""
    username: str = ""
    password: str = ""

    def login(self):
        ...

@rx.page()
def login_page():
    return rx.box(
        rx.input(value=LoginState.username),
        rx.input(value=LoginState.password),
    )
```

Separating the states is purely a matter of organization. You can still access the state from other pages by importing the state class.

```python
# index.py

import reflex as rx

from signup import SignupState

...

def index():
    return rx.box(
        rx.text(IndexState.data),
        rx.input(value=SignupState.username),
        rx.input(value=SignupState.password),
    )
```

## State Inheritance

A substate can also inherit from another substate other than `rx.State`, allowing you to create a hierarchy of states.

For example, you can create a base state that defines variables and event handlers that are common to all pages in your app, such as the current logged in user.

```python
class BaseState(rx.State):
    """Define your base state here."""

    current_user: str = ""

    def logout(self):
        self.current_user = ""


class LoginState(BaseState):
    """Define your login state here."""

    username: str = ""
    password: str = ""

    def login(self, username, password):
        # authenticate
        authenticate(...)

        # Set the var on the parent state.
        self.current_user = username
```

You can access the parent state properties from a child substate automatically.

## Accessing Arbitrary States

An event handler in a particular state can access and modify vars in another state instance by calling
the `get_state` async method and passing the desired state class. If the requested state is not already loaded,
it will be loaded and deserialized on demand.

In the following example, the `GreeterState` accesses the `SettingsState` to get the `salutation` and uses it
to update the `message` var.

Notably, the widget that sets the salutation does NOT have to load the `GreeterState` when handling the
input `on_change` event, which improves performance.

```python demo exec
class SettingsState(rx.State):
     salutation: str = "Hello"


def set_salutation_popover():
    return rx.popover.root(
        rx.popover.trigger(
            rx.icon_button(rx.icon("settings")),
        ),
        rx.popover.content(
            rx.input(
                value=SettingsState.salutation,
                on_change=SettingsState.set_salutation
            ),
        ),
    )


class GreeterState(rx.State):
    message: str = ""

    @rx.event
    async def handle_submit(self, form_data: dict[str, Any]):
        settings = await self.get_state(SettingsState)
        self.message = f"{settings.salutation} {form_data['name']}"


def index():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(placeholder="Name", id="name"),
                    set_salutation_popover(),
                ),
                rx.button("Submit"),
            ),
            reset_on_submit=True,
            on_submit=GreeterState.handle_submit,
        ),
        rx.text(GreeterState.message),
    )
```

## Performance Implications

When an event handler is called, Reflex will load the data not only for the substate containing
the event handler, but also all of its substates and parent states as well.
If a state has a large number of substates or contains a large amount of data, it can slow down processing
of events associated with that state.

For optimal performance, keep a flat structure with most substate classes directly inheriting from `rx.State`.
Only inherit from another state when the parent holds data that is commonly used by the substate.
Implementing different parts of the app with separate, unconnected states ensures that only the necessary
data is loaded for processing events for a particular page or component.

Avoid defining computed vars inside a state that contains a large amount of data, as
states with computed vars are always loaded to ensure the values are recalculated.
When using computed vars, it better to define them in a state that directly inherits from `rx.State` and
does not have other states inheriting from it, to avoid loading unnecessary data.
