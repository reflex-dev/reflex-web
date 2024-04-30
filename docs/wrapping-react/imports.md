```python exec
import reflex as rx
from typing import Any
```

```python exec
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str]
    on_change: rx.EventHandler[lambda event: [event]]

color_picker = ColorPicker.create


class ColorPickerState(rx.State):
    color: str = "#db114b"
```

# Full Guide

Let's walk step by step through how to wrap a React component in Reflex, using the color picker as our primary example.

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

In this guide we are wrapping the `HexPicker` component from the [react-colorful](https://www.npmjs.com/package/react-colorful) library. We will cover local components on the next page.

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

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[str]
    is_default = True
    lib_dependencies: list[str] = ["@splinetool/runtime"]  # Specify extra npm packages to install.
```

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
    alias = "OtherHexColorPicker"
    color: rx.Var[str]
    on_change: rx.EventHandler[lambda e0: [e0]]
```

## Custom Code

Sometimes you may need to add custom code to your component. This could be anything from adding custom constants, to adding custom imports, or even adding custom functions. Custom code will be inserted _outside_ of the react component function.

```javascript
import React from "react";
// Other imports...
...

// Custom code
const customCode = "const customCode = 'customCode';";
```

To add custom code to your component you can use the `get_custom_code` method in your component class.

```python
from reflex.components.component import NoSSRComponent

class PlotlyLib(NoSSRComponent):
    """A component that wraps a plotly lib."""

    library = "react-plotly.js@2.6.0"

    lib_dependencies: List[str] = ["plotly.js@2.22.0"]

    def _get_custom_code(self) -> str:
        return "const customCode = 'customCode';"
```
