```python exec
import reflex as rx
from typing import Any
from pcweb.base_state import State
```
# Wrapping React


One of Reflex's most powerful features is the ability to wrap React components. This allows us to build on top of the existing React ecosystem, and leverage the vast array of existing React components and libraries.

If you want a specific component for your app but Reflex doesn't provide it, there's a good chance it's available as a React component. Search for it on [npm](https://www.npmjs.com/), and if it's there, you can use it in your Reflex app.

In this section, we'll learn how to wrap React components and use them in Reflex apps.

## Import Types


If the tag is not the default export from the module, then set `is_default = False` in the component class definition to generate an import using the curly brace syntax.

```javascript 
import \{ HexColorPicker \} from "react-colorful"
```

## Aliases

If you are wrapping another components with the same tag as a component in your project you can use aliases to differentiate between them and avoid naming conflicts.

Lets check out the code below, in this case if we needed to wrap another color picker library with the same tag we use an alias to avoid a conflict.

```python
class AnotherColorPicker(rx.Component):
    library = "some-other-colorpicker"
    tag = "HexColorPicker"
    alias = "OtherHexColorPicker"
    color: rx.Var[str]

    def get_event_triggers(self) -> dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_change": lambda e0: [e0],
        }
```

## Dynamic Imports

Some libraries you may want to wrap may require dynamic imports. This is because they they may not be compatible with Server-Side Rendering (SSR).


To handle this in Reflex all you need todo is subclass when defining your component `NoSSRComponent`


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

Sometimes you may need to add custom code to your component. This could be anything from adding custom constants, to adding custom imports, or even adding custom functions.

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

    def get_custom_code(self) -> str:
        return "const customCode = 'customCode';"
```