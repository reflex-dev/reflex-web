---
from pcweb import constants, styles
from pcweb.base_state import State
from pcweb.templates.docpage import docdemo

import reflex as rx

color_picker_code = """class ColorPicker(rx.Component):
    # The NPM package name.
    library = "react-colorful@5.6.1"

    # The tag of the component in the package.
    tag = "HexColorPicker"

    # Any props that the component takes.
    color: rx.Var[str]

    def get_event_triggers(self) -> dict:
        return {
            **super().get_event_triggers(),
            "on_change": lambda value: [value],
        }

color_picker = ColorPicker.create"""

exec(color_picker_code)


state_code = """
class ColorPickerState(State):
    color: str = "#db114b"
"""
exec(state_code)
color_picker = ColorPicker.create

render_code = """
rx.box(
    rx.vstack(
        rx.heading(ColorPickerState.color),
        color_picker(on_change=ColorPickerState.set_color),
    ),
    background_color=ColorPickerState.color,
    padding="5em",
    border_radius="1em",
)
"""

def get_lines(code, start=0, end=-1):
    return "\n".join(code.split("\n")[start:end])
---

# Wrapping React

One of Reflex's most powerful features is the ability to wrap React components.
This allows us to build on top of the powerful React ecosystem, but interface with it through Python.

Most of Reflex's base components are just wrappers around the great 
[Chakra UI](https://chakra-ui.com/) React component library.
Let's take a look at how we can wrap React components in Reflex.

## Step 1: Find a Library

If you want a component for your app but Reflex doesn't provide it, there's a good chance it's available as a React component.
Search the web for an [npm](https://www.npmjs.com/) package that has the component you want.

In this example, we will wrap the
[react-colorful](https://www.npmjs.com/package/react-colorful) color picker component.

## Step 2: Wrap the Library

To wrap the component, create a subclass of `rx.Component`.

```python
{get_lines(color_picker_code, end=6)}
```

The `library` attribute is the name of the npm package.
You can specify a version number or range after the `@` symbol.

The `tag` attribute is the name of the component in the package that you want to wrap.

Reflex will automatically install the npm package when you use the component.

A component may also have many props. You can add props by declaring them as rx.Vars in the class. In this example, we have just one prop, `color`, which is the current color.

```python
{get_lines(color_picker_code, end=9)}
```

Finally, we must specify any event triggers that the component takes. This component has a single trigger to specify when the color changes.

```python
{get_lines(color_picker_code, end=16)}
```

The event triggers are a dictionary where the keys are the names of the triggers.
The value is a function that specifies how to transform the Javascript event into arguments for the event handler.

We call `super().get_event_triggers()` to add in the base event triggers such as `on_click` to the component.

We specify the `on_change` trigger to take a single argument, `value`, which is the new color, and will pass that color to the event handler.


## Step 3: Use the Component

Now we're ready to use the component! Every component has a create method. Usually you'll want to store this for easy access.

```python
{get_lines(color_picker_code, start=16, end=17)}
```

Then you can use it like any other Reflex component.

```reflex
docdemo(state_code, render_code, comp=eval(render_code))
```

That's it! We hope over time the Reflex ecosystem will grow to include many useful components. Our goal is to bring the full power of web development to Python.

## Lib Dependencies

If your component depends on non-react JS libs to work, add in the `lib_dependencies` field and the dependencies will be installed automatically.

For example, the `Plotly` component depends on the `plotly.js` library, even though the component comes from the `react-plotly.js` package. We can add the dependency like this:

```python
class PlotlyLib(rx.Component):
    """A component that wraps a plotly lib."""

    library = "react-plotly.js@^2.6.0"

    lib_dependencies: List[str] = ["plotly.js@^2.22.0"]
```

## Aliases

If you are wrapping another components with the same tag as a component in your project you can use aliases to differentiate between them and avoid naming conflicts.

For example, if we needed to wrap another color picker library with the same tag we use an alias to avoid a conflict.

```python
class AnotherColorPicker(rx.Component):
    library = "some-other-colorpicker"

    # This would conflict with the other color picker without an alias.
    tag = "HexColorPicker"

    color: rx.Var[str]

    def get_event_triggers(self) -> dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_change": lambda color: [color],
        }

    @classmethod
    def get_alias(cls) -> str:
        return "OtherHexColorPicker"
```

## Local Components

You can also wrap components that are defined locally in your project. This is useful if you want to wrap a component that you have created yourself.

Store your local component within the `assets/` directory. In this example, we will create a local component in `./assets/welcome.js`.

```javascript
// assets/welcome.js
export function Welcome(props) {
    return <h1>Hello, {props.name}</h1>;
}
```

Then you can wrap the component like this:

```python
class Welcome(rx.Component):
    library = "../public/welcome.js"
    tag = "Welcome"

    name: rx.Var[str]


welcome = Welcome.create
```

(Note that the contents of assets are compiled to `.web/public` directory.)

The local wrapped component can now be used like any other Reflex component.

```python
def index():
    return rx.vstack(welcome(name="Reflex"))
```

## Import Types

If the tag is the default export from the module, then set `is_default = True` in the component class definition to generate an import using the curly brace syntax.

By default, the import will use the `import { Tag } from "library"` syntax.

```python
class Markdown(Component):
    """A markdown component."""

    library = "react-markdown@^8.0.7"

    tag = "ReactMarkdown"

    is_default = True
```

```python
import ReactMarkdown from "react-markdown"
```

## Client-Side Only

For components that do not work properly during server-side rendering, use the `_get_custom_code` method to emit a dynamic loader.

```python
class ReactPlayerComponent(rx.Component):
    library = "react-player"
    tag = "ReactPlayer"

    def _get_imports(self) -> Optional[imports.ImportDict]:
        return {}

    def _get_custom_code(self) -> Optional[str]:
        return """
import dynamic from "next/dynamic";
const ReactPlayer = dynamic(() => import("react-player/lazy"), { ssr: false });
"""
```

The strategy of emitting custom code can be used to surpass any current limitations of the Reflex component compiler.
