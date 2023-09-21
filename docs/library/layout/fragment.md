---
import reflex as rx
from pcweb import constants
from pcweb.templates.docpage import docdemo

fragment_example = """rx.fragment(
    rx.text("Component1"), 
    rx.text("Component2")
)"""

---

A Fragment is a Component that allow you to group multiple Components without a wrapper node.

Refer to the React docs at [React/Fragment]({constants.FRAGMENT_COMPONENT_INFO_URL}) for more information on its use-case.

```reflex
docdemo(fragment_example)
```

