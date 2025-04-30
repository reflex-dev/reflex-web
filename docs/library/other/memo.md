```python exec
import reflex as rx
from pcweb.pages.docs import styling
```

# Memo

The `memo` decorator is used to optimize component rendering by memoizing components that don't need to be re-rendered. This is particularly useful for expensive components that depend on specific props and don't need to be re-rendered when other state changes in your application.

## Basic Usage

When you wrap a component function with `@rx.memo`, the component will only re-render when its props change. This helps improve performance by preventing unnecessary re-renders.

```python
@rx.memo
def expensive_component(label):
    return rx.vstack(
        rx.heading(label, size="lg"),
        rx.text("This component only re-renders when props change!"),
        rx.divider(),
    )

def index():
    return rx.vstack(
        rx.heading("Memo Example"),
        rx.text("Count: 0"),
        rx.button("Increment"),
        rx.divider(),
        expensive_component(label="Memoized Component"),
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
@rx.memo
def my_button(text, on_click=None):
    return rx.button(text, on_click=on_click)

def index():
    return rx.vstack(
        rx.text("Clicks: 0"),
        my_button(text="Click me"),
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
        
    def set_name(self, name):
        self.name = name

@rx.memo
def greeting(name):
    return rx.heading("Hello, " + name)

def index():
    return rx.vstack(
        greeting(name=AppState.name),
        rx.text("Count: " + str(AppState.count)),
        rx.button("Increment Count", on_click=AppState.increment),
        rx.input(
            placeholder="Enter your name", 
            on_change=AppState.set_name,
            value=AppState.name,
        ),
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
