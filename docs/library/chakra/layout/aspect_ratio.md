```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo
```

Preserve the ratio of the components contained within a region.

```python exec
image_example = rx.box(element="iframe", src="https://bit.ly/naruto-sage", border_color="red")
```

```python eval
docdemo("""(rx.box(element="iframe", src="https://bit.ly/naruto-sage", border_color="red")
)""")
```

```python eval
docdemo("""rx.aspect_ratio(image_example, ratio=4/3)""", comp=rx.aspect_ratio(image_example, ratio=4/3))
```

