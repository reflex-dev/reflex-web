---
components:
    - rx.radix.themes.PopoverRoot
    - rx.radix.themes.PopoverContent
    - rx.radix.themes.PopoverTrigger
    - rx.radix.themes.PopoverClose
---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```

# Popover

```python demo

popover_root(
    popover_trigger(
        button("Comment", variant="soft"),
    ),
    popover_content(
        flex(
            avatar(
                "2",
                fallback="RX",
                radius="full"
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
                    popover_close(
                        button("Comment", size="1")
                    ),
                    gap="3",
                    margin_top="12px",
                    justify="between",
                ),
                flex_grow="1",
            ),
            gap="3"
        ),
        style={"width": 360},
    )
)
```

```python demo
popover_root(
    popover_trigger(
        button("Feedback", variant="classic"),
    ),
    popover_content(
        inset(
            side="top",
            background="url('https://source.unsplash.com/random/800x600') center/cover",
            height="100px",
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
                popover_close(
                    button("Comment", size="1")
                ),
                gap="3",
                margin_top="12px",
                justify="between",
            ),
            padding_top="12px",
        ),
        style={"width": 360},
    )
)
```

