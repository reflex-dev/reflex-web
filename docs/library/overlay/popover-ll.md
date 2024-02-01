---
components:
    - rx.radix.popover.root
    - rx.radix.popover.content
    - rx.radix.popover.trigger
    - rx.radix.popover.close
---

```python exec
import reflex as rx
rdx = rx.radix
```

# Popover

```python demo

rdx.popover.root(
    rdx.popover.trigger(
        rdx.button("Comment", variant="soft"),
    ),
    rdx.popover.content(
        rdx.flex(
            rdx.avatar(
                "2",
                fallback="RX",
                radius="full"
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
                    rdx.popover.close(
                        rdx.button("Comment", size="1")
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
rdx.popover.root(
    rdx.popover.trigger(
        rdx.button("Feedback", variant="classic"),
    ),
    rdx.popover.content(
        rdx.inset(
            side="top",
            background="url('https://source.unsplash.com/random/800x600') center/cover",
            height="100px",
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
                rdx.popover.close(
                    rdx.button("Comment", size="1")
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

