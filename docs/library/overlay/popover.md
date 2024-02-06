---
components:
    - rx.radix.themes.PopoverRoot
    - rx.radix.themes.PopoverContent
    - rx.radix.themes.PopoverTrigger
    - rx.radix.themes.PopoverClose

only_low_level:
    - True

PopoverRoot: |
    lambda **props: rx.radix.themes.popover_root(
        rx.radix.themes.popover_trigger(
            rx.radix.themes.button("Popover"),
        ),
        rx.radix.themes.popover_content(
            rx.radix.themes.flex(
                rx.radix.themes.text("Simple Example"),
                rx.radix.themes.popover_close(
                    rx.radix.themes.button("Close"),
                ),
                direction="column",
                gap="3",
            ),
        ),
        **props
    )

PopoverContent: |
    lambda **props: rx.radix.themes.popover_root(
        rx.radix.themes.popover_trigger(
            rx.radix.themes.button("Popover"),
        ),
        rx.radix.themes.popover_content(
            rx.radix.themes.flex(
                rx.radix.themes.text("Simple Example"),
                rx.radix.themes.popover_close(
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

