```python exec
from pcweb.pages.docs import components
from pcweb.pages.docs.library import library
from pcweb.pages.docs.custom_components import custom_components
from pcweb.pages import docs
import reflex as rx
```

# Reflex Basics

This page gives an introduction to the most common concepts that you will use to build Reflex apps.

```md section
# You will learn how to:
* Create and nest components
* Customize and style components
* Distinguishes between compile-time and runtime
* Define state that changes over time
* Respond to user input and update the screen
* Render conditions and lists
* Create pages and navigate between them
```

Import the reflex library to get started.

```python
import reflex as rx
```

## Creating and nesting components

[Components]({docs.ui.overview.path}) are the building blocks for your app's user interface (UI). They are the visual elements that make up your app, like buttons, text, and images. Reflex has a wide selection of [built-in components]({library.path}) to get you started quickly.

Components are created using functions that return a component object.

```python demo exec
def my_button():
    return rx.button("Click Me")
```

Components can be nested inside each other to create complex UIs.

```python demo exec
def my_page():
    return rx.box(
        rx.text("This is a page"),
        # Reference components defined in other functions.
        my_button()
    )
```

You can also use any base HTML element through the `rx.el` namespace.

```python demo exec
def my_div():
    return rx.el.div(
        rx.el.p("Use base html!"),
    )
```

If you need a component not provided by Reflex, you can check the [3rd party ecosystem]({custom_components.path}) or [wrap your own React component]({docs.wrapping_react.guide.path}).


## Customizing and styling components

Components can be customized using [props]({docs.components.props.path}), which are passed in as keyword arguments to the component function.

Each component has props that are specific to that component. Check the docs for the component you are using to see what props are available.

```python demo exec
def half_filled_progress():
    return rx.progress(value=50)
```

In addition to component-specific props, components can also be styled using CSS properties passed as props.

```python demo exec
def round_button():
    return rx.button("Click Me", border_radius="15px", font_size="18px")
```

See the [styling guide]({docs.styling.overview.path}) for more information on how to style components

## Making components interactive

Apps often need to respond to user input or update the screen based on some event. Reflex handles this through [state]({docs.state.overview.path}), which is a Python class that stores variables that can change when the app is running, as well as the functions that can change those variables.

To define a state class, subclass `rx.State` and define fields that store the state of your app. The state vars should have a type annotation, and can be initialized with a default value.

```python
class MyState(rx.State):
    count: int = 0
```

## Referencing state in components

To reference a state var in a component, you can pass it as either a prop or a child of the component.

```python demo exec
class MyState(rx.State):
    count: int = 0

def counter():
    return rx.hstack(
        rx.heading("Count: "),
        # Reference the state var in the component
        rx.heading(MyState.count),
    )
```

Vars can be referenced in multiple components, and will automatically update when the state changes.


## Compile-time vs. runtime

Before we dive into state, it's important to understand the difference between compile-time and runtime in Reflex. 

When you run your app, Reflex compiles your components into Javascript code that runs in the browser. What this means importantly is ha you cannot use arbitrary Python operations and funcions when referencing state in components.

```python
def count_if_even():
    return rx.box(
        rx.heading("Count: "),
        # This will raise a compile error, as MyState.count is a var and not known a compile time.
        rx.text(MyState.count if MyState.count % 2 == 0 else "Odd"),
    )
```

## Conditional rendering

As mentioned above, you cannot use Python `if/else` statements with state vars in components. Instead, use the `rx.cond` function to conditionally render components.

```python demo exec
class LoginState(rx.State):
    logged_in: bool = False

    def toggle_login(self):
        self.logged_in = not self.logged_in

def count_if_even():
    return rx.box(
        rx.cond(
            LoginState.logged_in,
            rx.heading("Logged In"),
            rx.heading("Not Logged In"),
        ),
        rx.button("Toggle Login", on_click=LoginState.toggle_login)
    )
```


