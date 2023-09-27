---
import reflex as rx
from pcweb.templates.docpage import docdemo

image_example = (
    """rx.box(element="iframe", src="https://bit.ly/naruto-sage", border_color="red")"""
)

aspect_ratio_example = f"""rx.aspect_ratio({image_example}, ratio=4/3)"""

---

Preserve the ratio of the components contained within a region.

```reflex
docdemo(image_example)
```

```reflex
docdemo(aspect_ratio_example)
```

