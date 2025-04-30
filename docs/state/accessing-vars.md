```python exec
import reflex as rx
```

# Accessing Var Values

Reflex provides the `get_var_value` method, which allows you to retrieve the actual value of a `Var` at runtime. This is useful when you need to access state variables from other states or when dealing with computed values.

## Overview

The `get_var_value` method is available on all state instances and can be used to:

- Access values from the current state
- Access values from other states
- Access values from literal vars
- Use in computed vars to access dynamic data

This method is an `async` method and must be `await`ed when used.

## Basic Usage

```python
# Access a var value from the current state
value = await self.get_var_value(self.my_var)

# Access a var value from a state class
value = await self.get_var_value(OtherState.some_var)

# Access a literal var value
value = await self.get_var_value(rx.Var.create([1, 2, 3]))
```

## Examples

### Accessing Variables from the Same State

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

### Accessing Variables from Other States

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

### Using in Computed Vars

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

## Error Handling

If you attempt to get a value from a `Var` that doesn't have a literal value or is not associated with any state, `get_var_value` will raise an `UnretrievableVarValueError`.

```python
try:
    # This will raise an UnretrievableVarValueError if the var is not retrievable
    value = await self.get_var_value(rx.Var("undefined"))
except Exception as e:
    print("Error:", e)
```

## Benefits

- **Flexibility**: Easily access values from any state in your application
- **Real-time Values**: Get the current value of a variable at the exact moment it's needed
- **Dynamic Interactions**: Create more complex interactions between different parts of your app
- **Cleaner Code**: Avoid passing data through multiple layers of components

## Related Features

For accessing entire state instances rather than individual variables, see the `get_state` method described in the [Substates documentation](/docs/substates/overview).
