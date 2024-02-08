---
components:
    - rx.radix.hover_card.root
    - rx.radix.hover_card.content
    - rx.radix.hover_card.trigger

only_low_level:
    - True

HoverCardRoot: |
    lambda **props: rx.radix.themes.hover_card.root(
        rx.radix.themes.hover_card.trigger(
            rx.radix.themes.link("Hover over me"),
        ),
        rx.radix.themes.hover_card.content(
            rx.radix.themes.text("This is the tooltip content."),
        ),
        **props
    )

HoverCardContent: |
    lambda **props: rx.radix.themes.hover_card.root(
        rx.radix.themes.hover_card.trigger(
            rx.radix.themes.link("Hover over me"),
        ),
        rx.radix.themes.hover_card.content(
            rx.radix.themes.text("This is the tooltip content."),
            **props
        ),
    )
---

# Check Out Low Level Docs! High Level API Coming Soon.


