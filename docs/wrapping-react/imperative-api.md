# Creating Imperative APIs with JSAPIVar (reflex-enterprise)

## Introduction

React and Reflex primarily use a declarative programming model, where UI is defined as a function of state. However, many JavaScript libraries provide imperative APIs that allow direct manipulation of components through method calls. While the declarative approach is excellent for most UI scenarios, sometimes you need to trigger specific actions imperatively, such as programmatically focusing an input field, scrolling an element into view, or triggering an animation.

### Why Use Imperative APIs?

1. **Direct Control**: Some operations are more naturally expressed as commands rather than state changes.
   
2. **Complex Interactions**: Certain complex interactions are difficult to model purely through state and props.
   
3. **Performance Optimization**: For operations that would require complex state propagation, direct imperative calls can be more efficient.
   
4. **Library Integration**: Many third-party JavaScript libraries are designed with imperative APIs, and providing a similar interface makes your wrapper more intuitive to users familiar with the original library.

### Use Cases

Imperative APIs are particularly valuable when wrapping complex interactive components such as:

- **Maps**: Pan, zoom, fly to location, add/remove layers
- **Charts and Visualizations**: Update data, trigger animations, export
- **Media Players**: Play, pause, seek, change playback rate
- **Complex Forms**: Focus fields, validate, reset, submit
- **Modals and Dialogs**: Open, close, position
- **Canvas and WebGL**: Draw, clear, animate

### Benefits of JSAPIVar

Reflex Enterprise provides `JSAPIVar` as a specialized tool for creating imperative APIs that bridge your Python code with JavaScript libraries. Using `JSAPIVar`, you can:

- Create type-safe Python methods that map to JavaScript method calls
- Maintain a clean separation between declarative props and imperative methods
- Provide a familiar and intuitive API for developers used to the original library
- Integrate smoothly with Reflex's event system

In the following sections, we'll explore how to implement your own imperative APIs using `JSAPIVar`, with examples and best practices for different types of components.

## Understanding JSAPIVar

Before diving into implementation, it's important to understand what `JSAPIVar` is and how it works within the Reflex ecosystem.

### What is JSAPIVar?

`JSAPIVar` is a specialized variable type in Reflex Enterprise that extends the base `Var` class. It's designed specifically for representing JavaScript API objects that expose methods for imperative interactions. Unlike regular `Var` instances that typically represent state or props, a `JSAPIVar` represents a JavaScript object with methods that can be invoked.

When you create a `JSAPIVar`, you're effectively creating a reference to a JavaScript object that lives in the client's browser. The methods you call on this object will be translated into JavaScript method calls on the client side.

Here's a simple example showing how to use JSAPIVar to access a JavaScript object's methods:

```python
# Create a JSAPIVar that points to a JavaScript object
my_api_var = JSAPIVar("document.getElementById('my-element')")  # JavaScript expression to access the object

# Call methods on the JavaScript object
# Python snake_case is automatically converted to JavaScript camelCase
result = my_api_var.get_bounding_client_rect()  # Calls getBoundingClientRect() in JS

# Pass parameters to methods
my_api_var.set_attribute("aria-label", "Example")  # Calls setAttribute() in JS
```

For a more structured approach, you can wrap JSAPIVar in a class:

```python
@dataclass
class ElementAPI:
    """Wrapper for DOM element API methods."""
    
    def __init__(self, element_id: str):
        self.element_id = element_id
    
    @property
    def _api(self) -> JSAPIVar:
        return JSAPIVar(f"document.getElementById('{self.element_id}')")
    
    def focus(self) -> rx.event.EventSpec:
        """Focus the element."""
        return rx.event.run_script(self._api.focus())
    
    def scroll_into_view(self, behavior: str = "smooth") -> rx.event.EventSpec:
        """Scroll the element into view."""
        return rx.event.run_script(
            self._api.scroll_into_view({"behavior": behavior})
        )

# Create and use the API
element_api = ElementAPI("my-input")

# Include this button where you want in your page
rx.button("Focus Input", on_click=element_api.focus())
```

This pattern allows you to call JavaScript methods directly from Python in a type-safe and intuitive way, with automatic conversion between snake_case and camelCase.

### How JSAPIVar Works

Under the hood, `JSAPIVar` operates by:

1. **Reference Creation**: It maintains a reference to a JavaScript object in the client's browser (often through a ref system)
2. **Method Proxying**: It provides a way to call methods on that object from Python
3. **Event Translation**: It converts method calls into Reflex events that can be executed on the client

When you call a method on a `JSAPIVar` instance, you're not actually executing JavaScript code directly. Instead, you're creating a Reflex event that, when processed, will execute the corresponding JavaScript method on the client.

### The Connection to Reflex's Event System

`JSAPIVar` integrates with Reflex's event system, which is how it enables Python code to trigger JavaScript actions. When you call a method on a `JSAPIVar`:

1. The method call is converted to a special type of event
2. This event contains the method name and arguments
3. When the event is processed on the client, it evaluate the referenced Javascript expression that was passed to the `JSAPIVar`
4. It then calls the specified method with the provided arguments

This architecture allows for a clean separation between your Python component definitions and the JavaScript methods they need to invoke, while still providing a cohesive developer experience.

### Relationship with Component References

In most implementations, `JSAPIVar` works in conjunction with React refs, which provide references to DOM elements or component instances. Your component typically needs a mechanism to:

1. Create and store refs for components
2. Make these refs accessible to your API wrapper
3. Use these refs to access the underlying JavaScript objects

This often involves:

- A unique ID for each component instance
- A way to reference the component by this ID
- Methods that map to the JavaScript API

## Step-by-Step Implementation Guide

Let's walk through creating an imperative API for DOM elements using the ElementAPI example from above. This will demonstrate the core patterns that can be applied to any JavaScript library or component.

### 1. Define Your API Wrapper Class

Start by creating a class that will serve as the main API interface for your users:

```python
@dataclass
class ElementAPI:
    """Wrapper for DOM element API methods."""
    
    # Store the ID to reference the element
    element_id: str
```

### 2. Create a JSAPIVar Reference

Add a method or property to access the JavaScript object through JSAPIVar:

```python
@property
def _api(self) -> JSAPIVar:
    """Get the JavaScript API object."""
    return JSAPIVar(
        f"document.getElementById('{self.element_id}')"
    )
```

### 3. Implement API Methods

Add methods that wrap the JavaScript functions you want to expose:

```python
def focus(self) -> rx.event.EventSpec:
    """Focus the element."""
    return rx.event.run_script(self._api.focus())

def scroll_into_view(self, behavior: str = "smooth") -> rx.event.EventSpec:
    """Scroll the element into view."""
    return rx.event.run_script(
        self._api.scroll_into_view({"behavior": behavior})
    )

def set_attribute(self, name: str, value: str) -> rx.event.EventSpec:
    """Set an attribute on the element."""
    return rx.event.run_script(
        self._api.set_attribute(name, value)
    )
```

### 4. Create a Factory Method (Optional)

For convenience, you might add a class method to create instances:

```python
@classmethod
def create(cls, element_id: str) -> "ElementAPI":
    """Create a new ElementAPI instance."""
    return cls(element_id=element_id)
```

### 5. Use the API in Your Components

Now you can use the API in your Reflex components:

```python
def index() -> rx.Component:
    # Create an API instance for a specific element
    input_api = ElementAPI.create("my-input")
    
    return rx.box(
        rx.input(id="my-input", placeholder="Type here..."),
        rx.hstack(
            rx.button("Focus Input", on_click=input_api.focus()),
            rx.button("Scroll to Input", on_click=input_api.scroll_into_view()),
        ),
    )
```

### Key Implementation Considerations

When implementing your own API wrapper:

1. **Naming Conventions**: Remember that snake_case method names in Python are automatically converted to camelCase in JavaScript.

2. **Type Safety**: Consider adding proper type annotations to your API methods for better IDE support and documentation.

3. **Error Handling**: JavaScript errors don't automatically propagate back to Python, so consider adding error handling in your component.

4. **Performance**: API calls create events - avoid creating them in render methods or frequently called code paths.

This pattern can be adapted for any JavaScript library or component, from simple DOM manipulations to complex third-party libraries.

## Best Practices

When creating imperative APIs with JSAPIVar, follow these best practices to ensure your code is maintainable, efficient, and user-friendly.

### Type Safety

1. **Use Proper Annotations**: Add appropriate type hints to your API methods. This improves IDE support and makes your API easier to use.

2. **Document Method Parameters**: Include docstrings that explain the parameters, especially when they match JavaScript counterparts.

3. **Return Types**: Specify return types accurately, typically `rx.event.EventSpec` for event handlers.

### API Design

1. **Match Library Conventions**: Try to match the naming and structure of the original JavaScript library to make your API intuitive for users familiar with it.

2. **Group Related Methods**: Organize methods logically by functionality to make your API discoverable.

3. **Provide Defaults**: Add sensible defaults for parameters where appropriate to make common cases simple.

4. **Consistent Naming**: Use consistent naming conventions across your API. The automatic snake_case to camelCase conversion helps maintain this consistency.

By following these practices, you can create imperative APIs that are both powerful and user-friendly, bridging the gap between Reflex's declarative model and the imperative nature of many JavaScript libraries.