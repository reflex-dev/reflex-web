---
components:
    - rx.radix.popover.root
    - rx.radix.popover.content
    - rx.radix.popover.trigger
    - rx.radix.popover.close

only_low_level:
    - True

PopoverRoot: |
    lambda **props: rx.radix.themes.popover.root(
        rx.radix.themes.popover.trigger(
            rx.radix.themes.button("Popover"),
        ),
        rx.radix.themes.popover.content(
            rx.radix.themes.flex(
                rx.radix.themes.text("Simple Example"),
                rx.radix.themes.popover.close(
                    rx.radix.themes.button("Close"),
                ),
                direction="column",
                gap="3",
            ),
        ),
        **props
    )

PopoverContent: |
    lambda **props: rx.radix.themes.popover.root(
        rx.radix.themes.popover.trigger(
            rx.radix.themes.button("Popover"),
        ),
        rx.radix.themes.popover.content(
            rx.radix.themes.flex(
                rx.radix.themes.text("Simple Example"),
                rx.radix.themes.popover.close(
                    rx.radix.themes.button("Close"),
                ),
                direction="column",
                gap="3",
            ),
            **props
        ),
    )
---


# Check Out Low Level Docs! High Level API Coming Soon.

