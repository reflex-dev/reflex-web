---
components:
    - rx.radix.themes.Link
---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```

# Link

Links are accessible elements used primarily for navigation. Use the `href` prop to specify the location for the link to navigate to.

```python demo
link("Reflex Home Page.", href="https://reflex.dev")
```


You can also provide local links to other pages in your project without writing the full url.


```python demo
link("Example", href="/docs/library",)
```

The `link` component can be used to wrap other components to make them link to other pages.


```python demo
link(button("Example"), href="https://reflex.dev")
```

You can also create anchors to link to specific parts of a page using the `id` prop.

```python demo
box("Example", id="example")
```

To reference an anchor, you can use the `href` prop of the `link` component. The `href` should be in the format of the page you want to link to followed by a # and the id of the anchor.


```python demo
link("Example", href="/docs/library/typography/link#example")
```


