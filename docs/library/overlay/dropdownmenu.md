---
components:
    - rx.radix.dropdown_menu.root
    - rx.radix.dropdown_menu.content
    - rx.radix.dropdown_menu.trigger
    - rx.radix.dropdown_menu.item
    - rx.radix.dropdown_menu.separator
    - rx.radix.dropdown_menu.sub_content

only_low_level:
    - True

DropdownMenuRoot: |
    lambda **props: rx.dropdown_menu.root(
        rx.dropdown_menu.trigger(rx.radix.themes.button("drop down menu")),
        rx.dropdown_menu.content(
            rx.dropdown_menu.item("Edit", shortcut="⌘ E"),
            rx.dropdown_menu.item("Share"),
            rx.dropdown_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
            rx.dropdown_menu.sub(
                rx.dropdown_menu.sub_trigger("More"),
                rx.dropdown_menu.sub_content(
                    rx.dropdown_menu.item("Eradicate"),
                    rx.dropdown_menu.item("Duplicate"),
                    rx.dropdown_menu.item("Archive"),
                ),
            ),
        ),
        **props
    )

DropdownMenuContent: |
    lambda **props: rx.dropdown_menu.root(
        rx.dropdown_menu.trigger(rx.radix.themes.button("drop down menu")),
        rx.dropdown_menu.content(
            rx.dropdown_menu.item("Edit", shortcut="⌘ E"),
            rx.dropdown_menu.item("Share"),
            rx.dropdown_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
            rx.dropdown_menu.sub(
                rx.dropdown_menu.sub_trigger("More"),
                rx.dropdown_menu.sub_content(
                    rx.dropdown_menu.item("Eradicate"),
                    rx.dropdown_menu.item("Duplicate"),
                    rx.dropdown_menu.item("Archive"),
                ),
            ),
            **props,
        ),
    )

DropdownMenuItem: |
    lambda **props: rx.dropdown_menu.root(
        rx.dropdown_menu.trigger(rx.radix.themes.button("drop down menu")),
        rx.dropdown_menu.content(
            rx.dropdown_menu.item("Edit", shortcut="⌘ E", **props),
            rx.dropdown_menu.item("Share", **props),
            rx.dropdown_menu.item("Delete", shortcut="⌘ ⌫", color="red", **props),
            rx.dropdown_menu.sub(
                rx.dropdown_menu.sub_trigger("More"),
                rx.dropdown_menu.sub_content(
                    rx.dropdown_menu.item("Eradicate", **props),
                    rx.dropdown_menu.item("Duplicate", **props),
                    rx.dropdown_menu.item("Archive", **props),
                ),
            ),
        ),
    )

DropdownMenuSub: |
    lambda **props: rx.dropdown_menu.root(
        rx.dropdown_menu.trigger(rx.radix.themes.button("drop down menu")),
        rx.dropdown_menu.content(
            rx.dropdown_menu.item("Edit", shortcut="⌘ E"),
            rx.dropdown_menu.item("Share"),
            rx.dropdown_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
            rx.dropdown_menu.sub(
                rx.dropdown_menu.sub_trigger("More"),
                rx.dropdown_menu.sub_content(
                    rx.dropdown_menu.item("Eradicate"),
                    rx.dropdown_menu.item("Duplicate"),
                    rx.dropdown_menu.item("Archive"),
                ),
                **props,
            ),
        ),
    )

DropdownMenuSubTrigger: |
    lambda **props: rx.dropdown_menu.root(
        rx.dropdown_menu.trigger(rx.radix.themes.button("drop down menu")),
        rx.dropdown_menu.content(
            rx.dropdown_menu.item("Edit", shortcut="⌘ E"),
            rx.dropdown_menu.item("Share"),
            rx.dropdown_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
            rx.dropdown_menu.sub(
                rx.dropdown_menu.sub_trigger("More", **props),
                rx.dropdown_menu.sub_content(
                    rx.dropdown_menu.item("Eradicate"),
                    rx.dropdown_menu.item("Duplicate"),
                    rx.dropdown_menu.item("Archive"),
                ),
            ),
        ),
    )

DropdownMenuSubContent: |
    lambda **props: rx.dropdown_menu.root(
        rx.dropdown_menu.trigger(rx.radix.themes.button("drop down menu")),
        rx.dropdown_menu.content(
            rx.dropdown_menu.item("Edit", shortcut="⌘ E"),
            rx.dropdown_menu.item("Share"),
            rx.dropdown_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
            rx.dropdown_menu.sub(
                rx.dropdown_menu.sub_trigger("More"),
                rx.dropdown_menu.sub_content(
                    rx.dropdown_menu.item("Eradicate"),
                    rx.dropdown_menu.item("Duplicate"),
                    rx.dropdown_menu.item("Archive"),
                    **props,
                ),
            ),
        ),
    )
---


# Check Out Low Level Docs! High Level API Coming Soon.

