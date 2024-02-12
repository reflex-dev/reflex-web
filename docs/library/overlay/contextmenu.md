---
components:
    - rx.radix.context_menu.root
    - rx.radix.context_menu.item
    - rx.radix.context_menu.separator
    - rx.radix.context_menu.trigger
    - rx.radix.context_menu.content
    - rx.radix.context_menu.sub
    - rx.radix.context_menu.sub_trigger
    - rx.radix.context_menu.sub_content


only_low_level:
    - True

ContextMenuRoot: |
    lambda **props: rx.radix.themes.context_menu.root(
            rx.radix.themes.context_menu.trigger(
                rx.radix.themes.text("Context Menu (right click)")
            ),
            rx.radix.themes.context_menu.content(
                rx.radix.themes.context_menu.item("Copy", shortcut="⌘ C"),
                rx.radix.themes.context_menu.item("Share"),
                rx.radix.themes.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.radix.themes.context_menu.sub(
                    rx.radix.themes.context_menu.sub_trigger("More"),
                    rx.radix.themes.context_menu.sub_content(
                        rx.radix.themes.context_menu.item("Eradicate"),
                        rx.radix.themes.context_menu.item("Duplicate"),
                        rx.radix.themes.context_menu.item("Archive"),
                    ),
                ),
            ),
            **props
        )

ContextMenuTrigger: |
    lambda **props: rx.radix.themes.context_menu.root(
            rx.radix.themes.context_menu.trigger(
                rx.radix.themes.text("Context Menu (right click)"),
                **props
            ),
            rx.radix.themes.context_menu.content(
                rx.radix.themes.context_menu.item("Copy", shortcut="⌘ C"),
                rx.radix.themes.context_menu.item("Share"),
                rx.radix.themes.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.radix.themes.context_menu.sub(
                    rx.radix.themes.context_menu.sub_trigger("More"),
                    rx.radix.themes.context_menu.sub_content(
                        rx.radix.themes.context_menu.item("Eradicate"),
                        rx.radix.themes.context_menu.item("Duplicate"),
                        rx.radix.themes.context_menu.item("Archive"),
                    ),
                ),
            ),
        )

ContextMenuContent: |
    lambda **props: rx.radix.themes.context_menu.root(
            rx.radix.themes.context_menu.trigger(
                rx.radix.themes.text("Context Menu (right click)")
            ),
            rx.radix.themes.context_menu.content(
                rx.radix.themes.context_menu.item("Copy", shortcut="⌘ C"),
                rx.radix.themes.context_menu.item("Share"),
                rx.radix.themes.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.radix.themes.context_menu.sub(
                    rx.radix.themes.context_menu.sub_trigger("More"),
                    rx.radix.themes.context_menu.sub_content(
                        rx.radix.themes.context_menu.item("Eradicate"),
                        rx.radix.themes.context_menu.item("Duplicate"),
                        rx.radix.themes.context_menu.item("Archive"),
                    ),
                ),
                **props
            ),
        )

ContextMenuSubTrigger: |
    lambda **props: rx.radix.themes.context_menu.root(
            rx.radix.themes.context_menu.trigger(
                rx.radix.themes.text("Context Menu (right click)")
            ),
            rx.radix.themes.context_menu.content(
                rx.radix.themes.context_menu.item("Copy", shortcut="⌘ C"),
                rx.radix.themes.context_menu.item("Share"),
                rx.radix.themes.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.radix.themes.context_menu.sub(
                    rx.radix.themes.context_menu.sub_trigger("More", **props),
                    rx.radix.themes.context_menu.sub_content(
                        rx.radix.themes.context_menu.item("Eradicate"),
                        rx.radix.themes.context_menu.item("Duplicate"),
                        rx.radix.themes.context_menu.item("Archive"),
                    ),
                ),
            ),
        )

ContextMenuSubContent: |
    lambda **props: rx.radix.themes.context_menu.root(
            rx.radix.themes.context_menu.trigger(
                rx.radix.themes.text("Context Menu (right click)")
            ),
            rx.radix.themes.context_menu.content(
                rx.radix.themes.context_menu.item("Copy", shortcut="⌘ C"),
                rx.radix.themes.context_menu.item("Share"),
                rx.radix.themes.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.radix.themes.context_menu.sub(
                    rx.radix.themes.context_menu.sub_trigger("More"),
                    rx.radix.themes.context_menu.sub_content(
                        rx.radix.themes.context_menu.item("Eradicate"),
                        rx.radix.themes.context_menu.item("Duplicate"),
                        rx.radix.themes.context_menu.item("Archive"),
                        **props
                    ),
                ),
            ),
        )

ContextMenuItem: |
    lambda **props: rx.radix.themes.context_menu.root(
            rx.radix.themes.context_menu.trigger(
                rx.radix.themes.text("Context Menu (right click)")
            ),
            rx.radix.themes.context_menu.content(
                rx.radix.themes.context_menu.item("Copy", shortcut="⌘ C", **props),
                rx.radix.themes.context_menu.item("Share", **props),
                rx.radix.themes.context_menu.item("Delete", shortcut="⌘ ⌫", color="red", **props),
                rx.radix.themes.context_menu.sub(
                    rx.radix.themes.context_menu.sub_trigger("More"),
                    rx.radix.themes.context_menu.sub_content(
                        rx.radix.themes.context_menu.item("Eradicate", **props),
                        rx.radix.themes.context_menu.item("Duplicate", **props),
                        rx.radix.themes.context_menu.item("Archive", **props),
                    ),
                ),
            ),
        )
---


# Check Out Low Level Docs! High Level API Coming Soon.