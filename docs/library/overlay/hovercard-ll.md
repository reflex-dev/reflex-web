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

# Hovercard


The `hovercard_root` contains all the parts of a hover card.

The `hovercard_trigger` wraps the link that will open the hover card.

The `hovercard_content` contains the content of the open hover card.


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


## Events when the Hovercard opens or closes

The `on_open_change` event is called when the `open` state of the hovercard changes. It is used in conjunction with the `open` prop, which is passed to the event handler.

```python demo exec
class HovercardState(rx.State):
    num_opens: int = 0
    opened: bool = False

    def count_opens(self, value: bool):
        self.opened = value
        self.num_opens += 1


def hovercard_example():
    return flex(
        heading(f"Number of times hovercard opened or closed: {HovercardState.num_opens}"),
        heading(f"Hovercard open: {HovercardState.opened}"),
        rx.text(
            "Hover over the text to see the tooltip. ",
            hovercard_root(
                hovercard_trigger(
                    link("Hover over me", color_scheme="blue", underline="always"),
                ),
                hovercard_content(
                    text("This is the tooltip content."),
                ),
                on_open_change=HovercardState.count_opens,
            ),
        ),
        direction="column",
        gap="3",
    )
```