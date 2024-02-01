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

A popover displays content, triggered by a button.

The `popover_root` contains all the parts of a popover.

The `popover_trigger` contains the button that toggles the popover.

The `popover_content` is the component that pops out when the popover is open.

The `popover_close` is the button that closes an open popover.

## Basic Example

```python demo
popover_root(
    popover_trigger(
        button("Popover"),
    ),
    popover_content(
        flex(
            text("Simple Example"),
            popover_close(
                button("Close"),
            ),
            direction="column",
            gap="3",
        ),
    ),
)
```

## Examples in Context


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

