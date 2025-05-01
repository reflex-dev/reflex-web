```python exec
import reflex as rx
from pcweb.pages.docs import styling
```

# Memo

The `memo` decorator is used to optimize component rendering by memoizing components that don't need to be re-rendered. This is particularly useful for expensive components that depend on specific props and don't need to be re-rendered when other state changes in your application.

## Requirements

When using `rx.memo`, you must follow these requirements:

1. **Type all arguments**: All arguments to a memoized component must have type annotations.
2. **Use keyword arguments**: When calling a memoized component, you must use keyword arguments (not positional arguments).

## Basic Usage

When you wrap a component function with `@rx.memo`, the component will only re-render when its props change. This helps improve performance by preventing unnecessary re-renders.

```python
class DemoState(rx.State):
    count: int = 0
    
    def increment(self):
        self.count += 1

@rx.memo
def expensive_component(label: str) -> rx.Component:
    return rx.vstack(
        rx.heading(label, size="lg"),
        rx.text("This component only re-renders when props change!"),
        rx.divider(),
    )

def index():
    return rx.vstack(
        rx.heading("Memo Example"),
        rx.text(f"Count: {DemoState.count}"),
        rx.button("Increment", on_click=DemoState.increment),
        rx.divider(),
        expensive_component(label="Memoized Component"),  # Must use keyword arguments
        spacing="4",
        padding="4",
        border_radius="md",
        border="1px solid #eaeaea",
    )
```

In this example, the `expensive_component` will only re-render when the `label` prop changes, not when the `count` state changes.

## With Event Handlers

You can also use `rx.memo` with components that have event handlers:

```python
class ButtonState(rx.State):
    clicks: int = 0
    
    def increment(self):
        self.clicks += 1

@rx.memo
def my_button(text: str, on_click: rx.EventHandler) -> rx.Component:
    return rx.button(text, on_click=on_click)

def index():
    return rx.vstack(
        rx.text(f"Clicks: {ButtonState.clicks}"),
        my_button(
            text="Click me", 
            on_click=ButtonState.increment
        ),
        spacing="4",
    )
```

## With State Variables

When used with state variables, memoized components will only re-render when the specific state variables they depend on change:

```python
class AppState(rx.State):
    name: str = "World"
    count: int = 0
    
    def increment(self):
        self.count += 1
        
    def set_name(self, name: str):
        self.name = name

@rx.memo
def greeting(name: str) -> rx.Component:
    return rx.heading(f"Hello, {name}!")

def index():
    return rx.vstack(
        greeting(name=AppState.name),  # Must use keyword arguments
        rx.text(f"Count: {AppState.count}"),
        rx.button("Increment Count", on_click=AppState.increment),
        rx.input(
            placeholder="Enter your name", 
            on_change=AppState.set_name,
            value=AppState.name,
        ),
        spacing="4",
    )
```

## Advanced Event Handler Example

You can also pass arguments to event handlers in memoized components:

```python
class MessageState(rx.State):
    message: str = ""
    
    def set_message(self, text: str):
        self.message = text

@rx.memo
def action_buttons(on_action: rx.EventHandler[rx.event.passthrough_event_spec(str)]) -> rx.Component:
    return rx.hstack(
        rx.button("Save", on_click=on_action("Saved!")),
        rx.button("Delete", on_click=on_action("Deleted!")),
        rx.button("Cancel", on_click=on_action("Cancelled!")),
        spacing="2",
    )

def index():
    return rx.vstack(
        rx.text(f"Status: {MessageState.message}"),
        action_buttons(on_action=MessageState.set_message),
        spacing="4",
    )
```

## Performance Considerations

Use `rx.memo` for:
- Components with expensive rendering logic
- Components that render the same result given the same props
- Components that re-render too often due to parent component updates

Avoid using `rx.memo` for:
- Simple components where the memoization overhead might exceed the performance gain
- Components that almost always receive different props on re-render
