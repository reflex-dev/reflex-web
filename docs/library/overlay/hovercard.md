---
components:
    - rx.radix.themes.HoverCardRoot
    - rx.radix.themes.HoverCardContent
    - rx.radix.themes.HoverCardTrigger

only_low_level:
    - True

HoverCardRoot: |
    lambda **props: rx.radix.themes.hovercard_root(
        rx.radix.themes.hovercard_trigger(
            rx.radix.themes.link("Hover over me"),
        ),
        rx.radix.themes.hovercard_content(
            rx.radix.themes.text("This is the tooltip content."),
        ),
        **props
    )

HoverCardContent: |
    lambda **props: rx.radix.themes.hovercard_root(
        rx.radix.themes.hovercard_trigger(
            rx.radix.themes.link("Hover over me"),
        ),
        rx.radix.themes.hovercard_content(
            rx.radix.themes.text("This is the tooltip content."),
            **props
        ),
    )
---

# Check Out Low Level Docs! High Level API Coming Soon.


