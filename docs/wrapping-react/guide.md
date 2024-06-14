```python exec
import reflex as rx
from typing import Any

from pcweb.pages.docs import events, api_reference
```

```python exec
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str]
    on_change: rx.EventHandler[lambda color: [color]]

color_picker = ColorPicker.create


class ColorPickerState(rx.State):
    color: str = "#db114b"
```

# Full Guide

Let's walk step by step through how to wrap a React component in Reflex, using the color picker as our primary example. You can also see the full [API reference]({api_reference.component.path}).

```python eval
rx.box(
    rx.vstack(
        rx.heading(ColorPickerState.color, color="white"),
        color_picker(
            on_change=ColorPickerState.set_color
        ),
    ),
    background_color=ColorPickerState.color,
    padding="5em",
    border_radius="1em",
    margin_bottom="1em",
)
```

## Find The Component

There are two ways to find a component to wrap:
1. Write the component yourself locally.
2. Find a well-maintained React library on [npm](https://www.npmjs.com/) that contains the component you need.

In both cases, the process of wrapping the component is the same except for the `library` field.

In this guide we are wrapping the `HexColorPicker` component from the [react-colorful](https://www.npmjs.com/package/react-colorful) library.

## Define the Component

The first step to wrapping any React component is to subclass `rx.Component`.

```python
class ColorPicker(rx.Component):
    """A color picker component."""
```

## Set the Library and Tag

The library is just the name of the `npm` package, and the tag is the name of the React component from the package that you want to wrap. Some packages have multiple components, and you can wrap each one as a separate Reflex component.

You can generally find the library and tag by looking at the import statement in the React code.

```javascript
import \{ HexColorPicker } from "react-colorful"
```

In this case, the library is `react-colorful` and the tag is `HexColorPicker`.


```python
class ColorPicker(rx.Component):
    """Color picker component."""

    library = "react-colorful"
    tag = "HexColorPicker"
```

When you create your component, Reflex will automatically install the library for you.

### Local Components

You can also wrap components that you have written yourself. Local components should be stored in your `assets` directory. For example, you could define a basic `Hello` component like this:

```javascript
// assets/hello.js
import React from 'react';

export function Hello() {
  return (
    <div>
      <h1>Hello!</h1>
    </div>
  )
}
```

Then specify the library as following (note: we use the `public` directory here instead of `assets` as this is the directory that is served by the web server):

```python
import reflex as rx

class Hello(rx.Component):
    # Use an absolute path starting with /public
    library = "/public/hello"

    # Define everything else as normal.
    tag = "Hello"
```

### Local Packages

If the component is part of a local package, available on Github, or
downloadable via a web URL, it can also be wrapped in Reflex. Specify the path
or URL after an `@` following the package name.

Any local paths are relative to the `.web` folder, so you can use `../` prefix
to reference the Reflex project root.

Some examples of valid specifiers for a package called 
[`@masenf/hello-react`](https://github.com/masenf/hello-react) are:

* GitHub: `@masenf/hello-react@github:masenf/hello-react`
* URL: `@masenf/hello-react@https://github.com/masenf/hello-react/archive/refs/heads/main.tar.gz`
* Local Archive: `@masenf/hello-react@../hello-react.tgz`
* Local Directory: `@masenf/hello-react@../hello-react`

It is important that the package name matches the name in `package.json` so
Reflex can generate the correct import statement in the generated javascript
code.

These package specifiers can be used for `library` or `lib_dependencies`.

```python demo exec
class GithubComponent(rx.Component):
    library = "@masenf/hello-react@github:masenf/hello-react"
    tag = "Counter"

def github_component_example():
    return GithubComponent.create()
```

Although more complicated, this approach is useful when the local components
have additional dependencies or build steps required to prepare the component
for use.

Some important notes regarding this approach:

* The repo or archive must contain a `package.json` file.
* `prepare` or `build` scripts will NOT be executed. The distribution archive,
  directory, or repo must already contain the built javascript files (this is common).

### Import Types

Sometimes the component is a default export from the module (meaning it doesn't require curly braces in the import statement).

```javascript
import Spline from '@splinetool/react-spline';
```

In these cases you must set `is_default = True` in your component class, as we did in the Spline example in the overview section:

```python
class Spline(rx.Component):
    """Spline component."""
 
    library = "@splinetool/react-spline"
    tag = "Spline"
    is_default = True  # Needed for default imports
```

### Library Dependencies

By default Reflex will install the library you have specified in the library property. However, sometimes you may need to install other libraries to use a component. In this case you can use the `lib_dependencies` property to specify other libraries to install.

As seen in the Spline example in the overview section, we need to import the `@splinetool/runtime` library to use the `Spline` component. We can specify this in our component class like this:

```python
class Spline(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"  # This is installed by default
    lib_dependencies: list[str] = ["@splinetool/runtime@1.5.5"]  # Specify extra npm packages to install.
```

### Versions

You can specify the version of the library you want to install by appending `@` and the version number to the library name.

```python
class Spline(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline@1.0.0"
```

This is recommended to ensure that your app works consistently across different environments.

### Dynamic Imports

Some libraries you may want to wrap may require dynamic imports. This is because they they may not be compatible with Server-Side Rendering (SSR).

To handle this in Reflex, subclass `NoSSRComponent` when defining your component.

Often times when you see an import something like this:

```javascript
import dynamic from 'next/dynamic';

const MyLibraryComponent = dynamic(() => import('./MyLibraryComponent'), {
  ssr: false
});
```

You can wrap it in Reflex like this, here we are wrapping the `react-plotly.js` library which requires dynamic imports:

```python
from reflex.components.component import NoSSRComponent

class PlotlyLib(NoSSRComponent):
    """A component that wraps a plotly lib."""

    library = "react-plotly.js@2.6.0"

    lib_dependencies: List[str] = ["plotly.js@2.22.0"]
```

### Additional Imports

Sometimes you may need to import additional files or stylesheets to use a component. You can do this by overriding the `add_imports` method in your component class. The method returns a dictionary where the key is the library and the values are a list of imports.

```python
class ReactFlowLib(Component):
    """A component that wraps a react flow lib."""

    library = "reactflow"

    def add_imports(self):
        return {
            "": ['reactflow/dist/style.css']
        }
```

You can use the empty string as the key to import files that are not part of a library.

### Aliases

If you are wrapping another component with the same tag as a component in your project you can use aliases to differentiate between them and avoid naming conflicts.

Lets check out the code below, in this case if we needed to wrap another color picker library with the same tag we use an alias to avoid a conflict.

```python
class AnotherColorPicker(rx.Component):
    library = "some-other-colorpicker"
    tag = "HexColorPicker"
    alias = "OtherHexColorPicker" # This can now coexist with the original HexColorPicker
```

## Custom Code

Sometimes you may need to add custom code to your component, such as definining constants and functions used. Custom code will be inserted _outside_ of the react component function.

```javascript
import React from "react";
// Other imports...
...

// Custom code
const customCode = "const customCode = 'customCode';";
```

To add custom code to your component you can use the `add_custom_code` method in your component class.

```python
from reflex.components.component import NoSSRComponent

class PlotlyLib(NoSSRComponent):
    """A component that wraps a plotly lib."""

    library = "react-plotly.js@2.6.0"

    lib_dependencies: List[str] = ["plotly.js@2.22.0"]

    def add_custom_code(self) -> str:
        return "const customCode = 'customCode';"
```

## Props

Props are the variables that you can pass to the component. In the case of our color picker, we have a single prop `color`. Props are defined using `rx.Var` with the type of the prop. Specifying the type helps the compiler catch errors and provides better intellisense.

```python
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"

    # Define all props using rx.Var
    color: rx.Var[str]

color_picker = ColorPicker.create
```

Then when you create the component, you can pass in the props as keyword arguments.

```python demo
color_picker(color="#db114b")
```

### Default Value

You can set a default value for the prop by assigning it in the class definition.

```python
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"

    # Set a default value for the color prop
    color: rx.Var[str] = "#db114b" 
```

## Serializers

Vars can be any type that can be serialized to JSON. This includes primitive types like strings, numbers, and booleans, as well as more complex types like lists, dictionaries, and dataframes.

In case you need to serialize a more complex type, you can use the `serializer` decorator to convert the type to a primitive type that can be stored in the state. Just define a method that takes the complex type as an argument and returns a primitive type. We use type annotations to determine the type that you want to serialize.

For example, the Plotly component serializes a plotly figure into a JSON string that can be stored in the state.

```python
import json
import reflex as rx
from plotly.graph_objects import Figure
from plotly.io import to_json

# Use the serializer decorator to convert the figure to a JSON string.
# Specify the type of the argument as an annotation.
@rx.serializer
def serialize_figure(figure: Figure) -> list:
    # Use Plotly's to_json method to convert the figure to a JSON string.
    return json.loads(str(to_json(figure)))["data"]
```

We can then define a var of this type as a prop in our component.

```python
import reflex as rx
from plotly.graph_objects import Figure

class Plotly(rx.Component):
    """Display a plotly graph."""
    library = "react-plotly.js@2.6.0"
    lib_dependencies: List[str] = ["plotly.js@2.22.0"]

    tag = "Plot"

    is_default = True

    # Since a serialize is defined now, we can use the Figure type directly.
    data: Var[Figure]
```

## Event Handlers

Recall that [event handlers]({events.events_overview.path}) are ways that components can handle user interactions. In the case of the color picker, we have a single event trigger `on_change` that triggers when the color changes. The event trigger takes a single argument `color` which is the new color.

```python
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str]
    on_change: rx.EventHandler[lambda color: [color]]
```

We can then bind this event trigger to an event handler in our state that takes the color as an argument.

```python
class ColorPickerState(rx.State):
    color: str = "#db114b"

    def set_color(self, color: str):
        self.color = color

def index():
    return color_picker(
        color=ColorPickerState.color,
        # Set the event handler.
        on_change=ColorPickerState.set_color
    )
```

## Assets

_Experimental feature added in v0.5.3_.

If a wrapped component depends on assets such as images, scripts, or
stylesheets, these can kept adjacent to the component code and
included in the final build using the `rx._x.asset` function.

`rx._x.asset` returns a relative path that references the asset in the compiled
output. The target files are copied into a subdirectory of `assets/external`
based on the module where they are initially used. This allows third-party
components to have external assets with the same name without conflicting
with each other.

For example, if there is an SVG file named `wave.svg` in the same directory as
this component, it can be rendered using `rx.image` and `rx._x.asset`.

```python
class Hello(rx.Component):
    @classmethod
    def create(cls, *children, **props) -> rx.Component:
        props.setdefault("align", "center")
        return rx.hstack(
            rx.image(src=rx._x.asset("wave.svg"), width="50px", height="50px"),
            rx.heading("Hello ", *children),
            **props
        )
```
