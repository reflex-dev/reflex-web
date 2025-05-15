---
title: Wrapping React - Step by Step
---

# First step

In this section, we will go through the process of wrapping a React component step by step.

## Step 1: Create a new component

When wrapping a React component, the first step is to create a new component in your Reflex app. This is done by creating a new class that inherits from `rx.Component` or `rx.NoSSRComponent`.

This is when we will define the most important attributes of the component:
1. **library**: The name of the npm package that contains the component.
2. **tag**: The name of the component to import from the package.
3. **alias**: (Optional) The name of the alias to use for the component. This is useful if multiple component from different package have a name in common. If `alias` is not specified, `tag` will be used.
4. **lib_dependencies**: Any additional libraries needed to use the component.
5. **is_default**: (Optional) If the component is a default export from the module, set this to `True`. Default is `False`.

```md alert warning
# When setting the `library` attribute, it is recommended to included a pinned version of the package. Package will only change when you intentionally update the version, avoid unexpected breaking changes.
```

```python
class MyBaseComponent(rx.Component):
    """MyBaseComponent."""

    # The name of the npm package.
    library = "my-library@x.y.z"

    # The name of the component to use from the package.
    tag = "MyComponent"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = ["package-deps@x.y.z"]

    # The name of the alias to use for the component.
    alias = "MyComponentAlias"

    # If the component is a default export from the module, set this to True.
    is_default = True/False
```

## Step 2: Wrapping the Props

When wrapping a React component, you want to define the props that will be accepted by the component.
This is done by defining the props and annotating them with a `rx.Var`.

Broadly, there are three kinds of props you can encounter when wrapping a React component:
1. **Simple Props**: These are props that are passed directly to the component. They can be of any type, including strings, numbers, booleans, and even lists or dictionaries.
2. **Callback Props**: These are props that expect to receive a function. That function will usually be called by the component as a callback. (This is different from event handlers.)
3. **Component Props**: These are props that expect to receive a components themselves. They can be used to create more complex components by composing them together.
4. **Event Handlers**: These are props that expect to receive a function that will be called when an event occurs. They are defined as `rx.EventHandler` with a signature function to define the spec of the event.

### Simple Props

Simple props are the most common type of props you will encounter when wrapping a React component. They are passed directly to the component and can be of any type (but most commonly strings, numbers, booleans, and structures).

```python
class CustomReactType(TypedDict):
    """Custom React type."""

    # Define the structure of the custom type.
    prop1: str
    prop2: int
    prop3: bool

class SimplePropsComponent(MyBaseComponent):
    """MyComponent."""

    # Type the props according the component documentation.
    # props annotated as `string`
    prop1: rx.Var[str]
    # props annotated as `number`
    prop2: rx.Var[int]
    # props annotated as `boolean`
    prop3: rx.Var[bool]
    # props annotated as `string[]`
    prop4: rx.Var[list[str]]
    # props annotated as `CustomReactType`
    props5: rx.Var[CustomReactType]
```

### Callback Props

Callback props are used to handle events or to pass data back to the parent component. They are defined as `rx.Var` with a type of `FunctionVar` or `Callable`.

```python
from typing import Callable
from reflex.vars.function import FunctionVar

class CallbackPropsComponent(MyBaseComponent):
    """MyComponent."""

    # A callback prop that takes a single argument.
    callback_props: rx.Var[Callable]
```

### Component Props
Some components will occasionally accept other components as props, usually annotated as `ReactNode`. In Reflex, these are defined as `rx.Component`.

```python
class ComponentPropsComponent(MyBaseComponent):
    """MyComponent."""

    # A prop that takes a component as an argument.
    component_props: rx.Var[rx.Component]
```

### Event Handlers
Event handlers are props that expect to receive a function that will be called when an event occurs. They are defined as `rx.EventHandler` with a signature function to define the spec of the event.

```python
from reflex.vars.event_handler import EventHandler
from reflex.vars.function import FunctionVar
from reflex.vars.object import ObjectVar

class InputEventType(TypedDict):
    """Input event type."""

    # Define the structure of the input event.
    foo: str
    bar: int


def custom_spec(event: ObjectVar[InputEventType]) -> tuple[str, int]:
    """Custom event spec."""
    return (
        event.foo.to(str),
        event.bar.to(int),
    )

class EventHandlerComponent(MyBaseComponent):
    """MyComponent."""

    # An event handler that take no argument.
    on_event: rx.EventHandler[rx.event.no_args_event_spec]

    # An event handler that takes a single string argument.
    on_event_with_arg: rx.EventHandler[rx.event.passthrough_event_spec(str)]

    # An event handler specialized for input events, accessing event.target.value from the event.
    on_input_change: rx.EventHandler[rx.event.input_event]

    # An event handler specialized for key events, accessing event.key from the event and provided modifiers (ctrl, alt, shift, meta).
    on_key_down: rx.EventHandler[rx.event.key_event]

    # An event handler that takes a custom spec.
    on_custom_event: rx.EventHandler[custom_spec]
```

```md alert info
# Custom event specs have a few use case where they are particularly useful. If the event returns non-serializable data, you can filter them out so the event can be sent to the backend. You can also use them to transform the data before sending it to the backend.
```

## Step 3: Define custom code and hooks
When wrapping a React component, you may need to define custom code or hooks that are specific to the component. This is done by defining the `add_custom_code`or `add_hooks` methods in your component class.

### Custom Code

Custom code is any JS code that need to be included in your page, but not necessarily in the component itself. This can include things like CSS styles, JS libraries, or any other code that needs to be included in the page.

```python
from reflex.vars.base import Var, VarData
from reflex.constants import Hooks

class CustomCodeComponent(MyBaseComponent):
    """MyComponent."""

    def add_custom_code(self) -> list[str]:
        """Add custom code to the component."""
        code1 = """
        console.log("Custom code1");
        """

        code2 = """
        console.log("Custom code2");
        """

        return [code1, code2]
```

### Custom Hooks
Custom hooks are any hooks that need to be included in your component. This can include things like `useEffect`, `useState`, or any other hooks that need to be included in the component.

- Simpke hooks can be added as strings.
- More complex hooks that need to have special import or be written in a specific order can be added as `rx.Var` with a `VarData` object to specify the position of the hook.
    - The `imports` attribute of the `VarData` object can be used to specify any imports that need to be included in the component.
    - The `position` attribute of the `VarData` object can be set to `Hooks.HookPosition.PRE_TRIGGER` or `Hooks.HookPosition.POST_TRIGGER` to specify the position of the hook in the component.

```python
from reflex.vars.base import Var, VarData
from reflex.constants import Hooks

class ComponentWithHooks(MyBaseComponent):
    """MyComponent."""

    def add_hooks(self) -> list[str| Var]:
        """Add hooks to the component."""
        hooks = []
        hooks1 = """
        useEffect(() => {
            console.log("Hook1");
        }, []);
        """
        hooks.append(hooks1)

        # A hook that need to be written before the memoized event handlers.
        hooks2 = Var(
            """
            useState(() => {
                console.log("Hook2");
            }, []);
            """,
            var_data=VarData(position=Hooks.HookPosition.PRE_TRIGGER),
        )
        hooks.append(hooks2)

        return hooks
```

## Step 4: Define styles and imports

When wrapping a React component, you may need to define styles and imports that are specific to the component. This is done by defining the `add_styles` and `add_imports` methods in your component class.

### Styles

Styles are any CSS styles that need to be included in the component. The style will be added inline to the component, so you can use any CSS styles that are valid in React.

```python
class StyledComponent(MyBaseComponent):
    """MyComponent."""

    def add_styles(self) -> list[str]:
        """Add styles to the component."""

        return rx.Style({
            "backgroundColor": "red",
            "color": "white",
            "padding": "10px",
        })
```

### Imports

You can also add imports to the component. This is useful if the component needs to import other components or libraries.
- Imports can be added as strings, or a list of strings.
- Imports can also be added as `ImportVar` objects. This is useful if the import needs to be aliased or if it needs to be installed as a dependency.

```python
from reflex.utils.imports import ImportVar

class ComponentWithImports(MyBaseComponent):
    def add_imports(self):
        """Add imports to the component."""
        return {
            "my-package1": "my-import1",
            "my-package2": ["my-import2"],
            "my-package3": ImportVar(tag="my-import3", alias="my-alias", install=False, is_default=False),
        }
```