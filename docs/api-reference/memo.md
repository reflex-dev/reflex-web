```python exec
import reflex as rx

from pcweb.templates.docpage import docdemo, h1_comp, text_comp, docpage

def basic_example():
    class MemoState(rx.State):
        count: int = 0
        text: str = "This component is memoized and won't re-render when the counter changes."
        
        def increment(self):
            self.count += 1
    
    @rx.memo
    def memoized_component(text_content: str) -> rx.Component:
        return rx.text(text_content)
    
    return rx.vstack(
        rx.hstack(
            rx.button("Increment Counter", on_click=MemoState.increment),
            rx.text(f"Count: {MemoState.count}"),
        ),
        memoized_component(MemoState.text),
        spacing="4",
    )

def recursive_example():
    class RecursiveState(rx.State):
        depth: int = 3
        
        def increase_depth(self):
            self.depth += 1
            
        def decrease_depth(self):
            if self.depth > 0:
                self.depth -= 1
    
    @rx.memo
    def recursive_component(depth_value: int) -> rx.Component:
        return rx.cond(
            depth_value <= 0,
            rx.text("Reached bottom!"),
            rx.vstack(
                rx.text(f"Depth: {depth_value}"),
                recursive_component(depth_value - 1),
                border="1px solid #eaeaea",
                padding="1em",
                border_radius="0.5em",
            )
        )
    
    return rx.vstack(
        rx.hstack(
            rx.button("Increase Depth", on_click=RecursiveState.increase_depth),
            rx.button("Decrease Depth", on_click=RecursiveState.decrease_depth),
        ),
        recursive_component(RecursiveState.depth),
        spacing="4",
    )

def event_handler_example():
    class EventState(rx.State):
        clicked: bool = False
        
        def toggle(self):
            self.clicked = not self.clicked
    
    @rx.memo
    def memoized_with_event(handler) -> rx.Component:
        return rx.button(
            "Click Me",
            on_click=handler,
            color=rx.cond(EventState.clicked, "green", "blue"),
        )
    
    return rx.vstack(
        rx.text(f"Button clicked: {EventState.clicked}"),
        memoized_with_event(EventState.toggle),
        spacing="4",
    )
```

# Memoization with rx.memo

The `rx.memo` decorator is used to memoize components in Reflex applications. Memoization is a performance optimization technique that prevents unnecessary re-renders of components when their inputs haven't changed.

## Basic Usage

Use the `@rx.memo` decorator on component functions to memoize them:

```python
@rx.memo
def my_component(text: rx.Var[str]) -> rx.Component:
    return rx.text(text)
```

When a component is memoized, Reflex will only re-render it when its inputs (props) change. This can significantly improve performance in complex applications with many components.

```python eval
basic_example()
```

## Benefits of Memoization

- **Performance Optimization**: Prevents unnecessary re-renders when component props haven't changed
- **Reduced Computation**: Avoids expensive calculations when inputs remain the same
- **Smoother UI**: Helps maintain responsive user interfaces in complex applications

## Advanced Usage

### Recursive Components

The `rx.memo` decorator supports recursive UI elements, allowing you to create components that reference themselves:

```python eval
recursive_example()
```

### Components with Event Handlers

You can pass event handlers as arguments to memoized components:

```python eval
event_handler_example()
```

## When to Use Memoization

Memoization is most beneficial in the following scenarios:

1. **Complex Components**: When components perform expensive calculations or rendering
2. **Deeply Nested Components**: When components are deep in the component tree and re-render frequently
3. **Components with Stable Props**: When components receive props that rarely change

## Implementation Details

Under the hood, `rx.memo` works by:

1. Comparing the current props with previous props
2. Skipping the re-render if all props are the same
3. Re-rendering only when props have changed

This optimization helps maintain application performance as your Reflex app grows in complexity.
