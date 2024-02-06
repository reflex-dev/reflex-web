---
components:
    - rx.radix.themes.ContextMenuRoot
    - rx.radix.themes.ContextMenuTrigger
    - rx.radix.themes.ContextMenuContent
    - rx.radix.themes.ContextMenuSub
    - rx.radix.themes.ContextMenuSubTrigger
    - rx.radix.themes.ContextMenuSubContent
    - rx.radix.themes.ContextMenuItem
    - rx.radix.themes.ContextMenuSeparator


only_low_level:
    - True

ContextMenuRoot: |
    lambda **props: rx.radix.themes.contextmenu_root(
            rx.radix.themes.contextmenu_trigger(
                rx.radix.themes.text("Context Menu (right click)")
            ),
            rx.radix.themes.contextmenu_content(
                rx.radix.themes.contextmenu_item("Copy", shortcut="⌘ C"),
                rx.radix.themes.contextmenu_item("Share"),
                rx.radix.themes.contextmenu_item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.radix.themes.contextmenu_sub(
                    rx.radix.themes.contextmenu_sub_trigger("More"),
                    rx.radix.themes.contextmenu_sub_content(
                        rx.radix.themes.contextmenu_item("Eradicate"),
                        rx.radix.themes.contextmenu_item("Duplicate"),
                        rx.radix.themes.contextmenu_item("Archive"),
                    ),
                ),
            ),
            **props
        )

ContextMenuTrigger: |
    lambda **props: rx.radix.themes.contextmenu_root(
            rx.radix.themes.contextmenu_trigger(
                rx.radix.themes.text("Context Menu (right click)"),
                **props
            ),
            rx.radix.themes.contextmenu_content(
                rx.radix.themes.contextmenu_item("Copy", shortcut="⌘ C"),
                rx.radix.themes.contextmenu_item("Share"),
                rx.radix.themes.contextmenu_item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.radix.themes.contextmenu_sub(
                    rx.radix.themes.contextmenu_sub_trigger("More"),
                    rx.radix.themes.contextmenu_sub_content(
                        rx.radix.themes.contextmenu_item("Eradicate"),
                        rx.radix.themes.contextmenu_item("Duplicate"),
                        rx.radix.themes.contextmenu_item("Archive"),
                    ),
                ),
            ),
        )

ContextMenuContent: |
    lambda **props: rx.radix.themes.contextmenu_root(
            rx.radix.themes.contextmenu_trigger(
                rx.radix.themes.text("Context Menu (right click)")
            ),
            rx.radix.themes.contextmenu_content(
                rx.radix.themes.contextmenu_item("Copy", shortcut="⌘ C"),
                rx.radix.themes.contextmenu_item("Share"),
                rx.radix.themes.contextmenu_item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.radix.themes.contextmenu_sub(
                    rx.radix.themes.contextmenu_sub_trigger("More"),
                    rx.radix.themes.contextmenu_sub_content(
                        rx.radix.themes.contextmenu_item("Eradicate"),
                        rx.radix.themes.contextmenu_item("Duplicate"),
                        rx.radix.themes.contextmenu_item("Archive"),
                    ),
                ),
                **props
            ),
        )

ContextMenuSubTrigger: |
    lambda **props: rx.radix.themes.contextmenu_root(
            rx.radix.themes.contextmenu_trigger(
                rx.radix.themes.text("Context Menu (right click)")
            ),
            rx.radix.themes.contextmenu_content(
                rx.radix.themes.contextmenu_item("Copy", shortcut="⌘ C"),
                rx.radix.themes.contextmenu_item("Share"),
                rx.radix.themes.contextmenu_item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.radix.themes.contextmenu_sub(
                    rx.radix.themes.contextmenu_sub_trigger("More", **props),
                    rx.radix.themes.contextmenu_sub_content(
                        rx.radix.themes.contextmenu_item("Eradicate"),
                        rx.radix.themes.contextmenu_item("Duplicate"),
                        rx.radix.themes.contextmenu_item("Archive"),
                    ),
                ),
            ),
        )

ContextMenuSubContent: |
    lambda **props: rx.radix.themes.contextmenu_root(
            rx.radix.themes.contextmenu_trigger(
                rx.radix.themes.text("Context Menu (right click)")
            ),
            rx.radix.themes.contextmenu_content(
                rx.radix.themes.contextmenu_item("Copy", shortcut="⌘ C"),
                rx.radix.themes.contextmenu_item("Share"),
                rx.radix.themes.contextmenu_item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.radix.themes.contextmenu_sub(
                    rx.radix.themes.contextmenu_sub_trigger("More"),
                    rx.radix.themes.contextmenu_sub_content(
                        rx.radix.themes.contextmenu_item("Eradicate"),
                        rx.radix.themes.contextmenu_item("Duplicate"),
                        rx.radix.themes.contextmenu_item("Archive"),
                        **props
                    ),
                ),
            ),
        )

ContextMenuItem: |
    lambda **props: rx.radix.themes.contextmenu_root(
            rx.radix.themes.contextmenu_trigger(
                rx.radix.themes.text("Context Menu (right click)")
            ),
            rx.radix.themes.contextmenu_content(
                rx.radix.themes.contextmenu_item("Copy", shortcut="⌘ C", **props),
                rx.radix.themes.contextmenu_item("Share", **props),
                rx.radix.themes.contextmenu_item("Delete", shortcut="⌘ ⌫", color="red", **props),
                rx.radix.themes.contextmenu_sub(
                    rx.radix.themes.contextmenu_sub_trigger("More"),
                    rx.radix.themes.contextmenu_sub_content(
                        rx.radix.themes.contextmenu_item("Eradicate", **props),
                        rx.radix.themes.contextmenu_item("Duplicate", **props),
                        rx.radix.themes.contextmenu_item("Archive", **props),
                    ),
                ),
            ),
        )
---


# Check Out Low Level Docs! High Level API Coming Soon.