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

### Accessing Individual Var Values

In addition to accessing entire state instances, you can also retrieve the value of individual `Var` objects using the `get_var_value` method. This is useful when you need to access specific state variables without loading the entire state.

The `get_var_value` method is available on all state instances and can be used to:

- Access values from the current state
- Access values from other states
- Access values from literal vars
- Use in computed vars to access dynamic data

This method is an `async` method and must be `await`ed when used.

#### Basic Usage

```python
# Access a var value from the current state
value = await self.get_var_value(self.my_var)

# Access a var value from a state class
value = await self.get_var_value(OtherState.some_var)

# Access a literal var value
value = await self.get_var_value(rx.Var.create([1, 2, 3]))
```

#### Examples

##### Accessing Variables from the Same State

You can use `get_var_value` to retrieve the current value of a variable within the same state:

```python demo exec
class SameStateExample(rx.State):
    count: int = 0
    
    @rx.event
    async def increment(self):
        self.count += 1
        # Get the current value of count
        current = await self.get_var_value(SameStateExample.count)
        return rx.window_alert(f"Count is now: {current}")

def same_state_example():
    return rx.vstack(
        rx.heading(f"Count: {SameStateExample.count}"),
        rx.button("Increment", on_click=SameStateExample.increment),
        width="100%",
        align="center",
        spacing="4",
    )
```

##### Accessing Variables from Other States

One of the primary use cases for `get_var_value` is retrieving values from other states:

```python demo exec
class ConfigState(rx.State):
    theme: str = "light"
    
class UIState(rx.State):
    message: str = ""
    
    @rx.event
    async def show_theme(self):
        # Get the value from another state
        current_theme = await self.get_var_value(ConfigState.theme)
        self.message = f"Current theme is: {current_theme}"

def other_state_example():
    return rx.vstack(
        rx.heading("Theme Example"),
        rx.hstack(
            rx.text("Theme: "),
            rx.select(
                ["light", "dark", "system"],
                value=ConfigState.theme,
                on_change=ConfigState.set_theme,
            ),
        ),
        rx.button("Show Current Theme", on_click=UIState.show_theme),
        rx.text(UIState.message),
        width="100%",
        align="center",
        spacing="4",
    )
```

##### Using in Computed Vars

`get_var_value` is particularly useful in computed vars when you need to access data that might change:

```python demo exec
class DataState(rx.State):
    items: list[dict] = [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"},
    ]
    
class DisplayState(rx.State):
    selected_id: str = "1"
    
    @rx.var
    async def selected_item(self) -> dict:
        """Get the selected item from the DataState."""
        items = await self.get_var_value(DataState.items)
        selected_id = int(self.selected_id)
        selected = next((item for item in items if item["id"] == selected_id), None)
        return selected or {}

def computed_var_example():
    return rx.vstack(
        rx.heading("Item Selector"),
        rx.select(
            ["1", "2", "3"],
            value=DisplayState.selected_id,
            on_change=DisplayState.set_selected_id,
        ),
        rx.divider(),
        rx.heading("Selected Item", size="4"),
        rx.text(f"Name: {DisplayState.selected_item.get('name', '')}"),
        width="100%",
        align="center",
        spacing="4",
    )
```

#### Error Handling

If you attempt to get a value from a `Var` that doesn't have a literal value or is not associated with any state, `get_var_value` will raise an `UnretrievableVarValueError`.

```python
try:
    # This will raise an UnretrievableVarValueError if the var is not retrievable
    value = await self.get_var_value(rx.Var("undefined"))
except Exception as e:
    print("Error:", e)
```

#### Benefits

- **Flexibility**: Easily access values from any state in your application
- **Real-time Values**: Get the current value of a variable at the exact moment it's needed
- **Dynamic Interactions**: Create more complex interactions between different parts of your app
- **Cleaner Code**: Avoid passing data through multiple layers of components

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
