---
components:
    - rx.radix.hover_card.root
    - rx.radix.hover_card.content
    - rx.radix.hover_card.trigger
---

```python exec
import reflex as rx
rdx = rx.radix
```

# Hovercard

```python demo
rdx.text(
    "Hover over the text to see the tooltip. ",
    rdx.hover_card.root(
        rdx.hover_card.trigger(
            rdx.link("Hover over me", color_scheme="blue", underline="always"),
        ),
        rdx.hover_card.content(
            rdx.text("This is the tooltip content."),
        ),
    ),
)
```

```python demo
rdx.text(
    "Hover over the text to see the tooltip. ",
    rdx.hover_card.root(
        rdx.hover_card.trigger(
            rdx.link("Hover over me", color_scheme="blue", underline="always"),
        ),
        rdx.hover_card.content(
            rdx.grid(
                rdx.inset(
                    side="left",
                    pr="current",
                    background="url('https://source.unsplash.com/random/800x600') center/cover",
                    height="full",
                ),
                rdx.box(
                    rdx.text_area(placeholder="Write a comment…", style={"height": 80}),
                    rdx.flex(
                        rdx.flex(
                            rdx.text(
                                rdx.checkbox.root(),
                                rdx.text("Send to group"),
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