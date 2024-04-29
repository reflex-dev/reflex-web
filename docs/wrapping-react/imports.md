```python exec
import reflex as rx
from typing import Any
```

```python exec
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str]
    on_change: rx.EventHandler[lambda e0: [e0]]

color_picker = ColorPicker.create


class ColorPickerState(rx.State):
    color: str = "#db114b"
```

# Full Guide

Let's walk step by step through how to wrap a React component in Reflex by wrapping a color picker component.

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

Before deciding to extend Reflex by wrapping a component, check to see if there is a corresponding, well-maintained React library. Search for your library on [npm](https://www.npmjs.com/), and if it's there, you can use it in your Reflex app. Make sure to include `react` in your search query to find React components.

In this example we are wrapping the `HexPicker` component from the [react-colorful](https://www.npmjs.com/package/react-colorful) library.

## Define the Component

The first step to wrapping any React component is to subclass `rx.Component`.

```python
class ColorPicker(rx.Component):
    """A color picker component."""
```

## Set the Library and Tag

When wrapping a React component, the first tings to determine are the library and the tag.

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

Sometimes the component is a default export from the module. For example in the `react-spline` library the `Spline` component is the default export, since there are no curly braces around the import.

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
    scene: Var[str] = "https://prod.spline.design/Br2ec3WwuRGxEuij/scene.splinecode"
    is_default = True
    lib_dependencies: list[str] = ["@splinetool/runtime"]  # Specify extra npm packages to install.
```

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

### Dynamic Imports

Some libraries you may want to wrap may require dynamic imports. This is because they they may not be compatible with Server-Side Rendering (SSR).

To handle this in Reflex all you need to do is subclass `NoSSRComponent` when defining your component.

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
