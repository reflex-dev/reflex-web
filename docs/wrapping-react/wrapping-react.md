```python exec
import reflex as rx
from typing import Any
from pcweb.base_state import State
```
# Wrapping React Overview


One of Reflex's most powerful features is the ability to wrap React components. This allows us to build on top of the existing React ecosystem, and leverage the vast array of existing React components and libraries.

If you want a specific component for your app but Reflex doesn't provide it, there's a good chance it's available as a React component. Search for it on [npm](https://www.npmjs.com/), and if it's there, you can use it in your Reflex app.

In this section, we'll go over how to wrap React components on a high level. In the subsequent sections, we'll go over the details of how to wrap more complex components.

## ColorPicker Example

Lets take a color picker example. We'll use the [react-colorful](https://www.npmjs.com/package/react-colorful) component, which is a simple color picker component.

```javascript
import \{ HexColorPicker \} from "react-colorful";

const YourComponent = () => \\{
  const [color, setColor] = useState("#aabbcc");
  return <HexColorPicker color=\{color\} onChange=\{setColor\} />;
\};
```

## Wrapping React Components

The two most important props are `library`, which is the name of the npm package, and `tag`, which is the name of the React component.

Reflex will automatically install the library specified in your code if needed.

```python
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
```

A component may also have many props. You can add props by declaring them as rx.Vars in the class. In this example, we have just one prop, value, which is the current color.

Finally, we must specify any event triggers that the component takes. This component has a single trigger to specify when the color changes.

```python
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str]

    def get_event_triggers(self) -> dict[str, Any]:
        return \{
            **super().get_event_triggers(),
            "on_change": lambda e0: [e0],
        \}
```

## Using the Component

Now we're ready to use the component! Every component has a create method. Usually you'll want to store this for easy access.

```python
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str]

    def get_event_triggers(self) -> dict[str, Any]:
        return \{
            **super().get_event_triggers(),
            "on_change": lambda e0: [e0],
        \}

color_picker = ColorPicker.create

class ColorPickerState(rx.State):
    color: str = "#db114b"

def index():
    return rx.box(
        rx.vstack(
            rx.heading(ColorPickerState.color, color="white"),
            color_picker(
                on_change=ColorPickerState.set_color
            ),
        ),
        background_color=ColorPickerState.color,
        padding="5em",
        border_radius="1em",
    )

```

```python exec
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str]

    def get_event_triggers(self) -> dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_change": lambda e0: [e0],
        }

color_picker = ColorPicker.create


class ColorPickerState(State):
    color: str = "#db114b"
```

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
    )
```

