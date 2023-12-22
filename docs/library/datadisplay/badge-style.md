```python exec
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
# from reflex.components.radix.doc_functions import style_grid
```

# Styling 

blurb about the grid for this one ...




We can change the radius of the badge using the `radius` prop. It can take values `"none" | "small" | "medium" | "large" | "full"`. 

It is also possible to change the size of the badge using the `size` prop. It can take values of `"1" | "2"`.

```python demo
flex(
    badge("New", size="1", radius="none"),
    badge("New", size="1", radius="small"),
    badge("New", size="1", radius="medium"),
    badge("New", size="1", radius="large"),
    badge("New", size="1", radius="full"),
    badge("New", size="2", radius="none"),
    badge("New", size="2", radius="small"),
    badge("New", size="2", radius="medium"),
    badge("New", size="2", radius="large"),
    badge("New", size="2", radius="full"),
    gap="3",
    )
```