```python exec
from pcweb.base_state import State
from pcweb.pages.docs.styling.overview import styling_overview
from pcweb.templates.docpage import docdemo
import reflex as rx
import inspect
```

# Style Props

In addition to component-specific props, most built-in components support a full range of style props. You can use any CSS property to style a component.

```python exec
def button():
    return rx.button(
    "Fancy Button",
    border_radius="1em",
    box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
    background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
    box_sizing="border-box",
    color="white",
    opacity="0.6",
    _hover={
        "opacity": 1,
    }
)
```

```python eval
docdemo(inspect.getsource(button).replace("def button():", "").replace("return", ""),
    comp=button()
)
```

See the [styling docs]({styling_overview.path}) to learn more about customizing the appearance of your app.
