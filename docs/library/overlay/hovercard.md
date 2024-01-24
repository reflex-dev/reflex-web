---
components:
    - rx.radix.themes.HoverCardRoot
    - rx.radix.themes.HoverCardContent
    - rx.radix.themes.HoverCardTrigger
---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```

```python demo
rx.text(
    "Hover over the text to see the tooltip. ",
    hovercard_root(
        hovercard_trigger(
            link("Hover over me", color_scheme="blue", underline="always"),
        ),
        hovercard_content(
            text("This is the tooltip content."),
        ),
    ),
)
```

```python demo
rx.text(
    "Hover over the text to see the tooltip. ",
    hovercard_root(
        hovercard_trigger(
            link("Hover over me", color_scheme="blue", underline="always"),
        ),
        hovercard_content(
            grid(
                inset(
                    side="left",
                    pr="current",
                    background="url('https://source.unsplash.com/random/800x600') center/cover",
                    height="full",
                ),
                box(
                    textarea(placeholder="Write a comment…", style={"height": 80}),
                    flex(
                        flex(
                            text(
                                checkbox(),
                                text("Send to group"),
                                as_="label",
                                size="2",
                            ),
                            align="center",
                            gap="2",
                            as_child=True,
                        ),
                        gap="3",
                        margin_top="12px",
                        justify="between",
                    ),
                    padding_left="12px",
                ),
                columns="120px 1fr",
            ),
            style={"width": 360},
        ),
    ),
)
```
