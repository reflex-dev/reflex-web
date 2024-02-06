---
components:
    - rx.radix.themes.DropdownMenuRoot
    - rx.radix.themes.DropdownMenuContent
    - rx.radix.themes.DropdownMenuTrigger
    - rx.radix.themes.DropdownMenuItem
    - rx.radix.themes.DropdownMenuSub
    - rx.radix.themes.DropdownMenuSubTrigger
    - rx.radix.themes.DropdownMenuSubContent
    - rx.radix.themes.DropdownMenuSeparator

only_low_level:
    - True

DropdownMenuRoot: |
    lambda **props: rx.radix.themes.dropdownmenu_root(
        rx.radix.themes.dropdownmenu_trigger(rx.radix.themes.button("drop down menu")),
        rx.radix.themes.dropdownmenu_content(
            rx.radix.themes.dropdownmenu_item("Edit", shortcut="⌘ E"),
            rx.radix.themes.dropdownmenu_item("Share"),
            rx.radix.themes.dropdownmenu_item("Delete", shortcut="⌘ ⌫", color="red"),
            rx.radix.themes.dropdownmenu_sub(
                rx.radix.themes.dropdownmenu_sub_trigger("More"),
                rx.radix.themes.dropdownmenu_sub_content(
                    rx.radix.themes.dropdownmenu_item("Eradicate"),
                    rx.radix.themes.dropdownmenu_item("Duplicate"),
                    rx.radix.themes.dropdownmenu_item("Archive"),
                ),
            ),
        ),
        **props
    )

DropdownMenuContent: |
    lambda **props: rx.radix.themes.dropdownmenu_root(
        rx.radix.themes.dropdownmenu_trigger(rx.radix.themes.button("drop down menu")),
        rx.radix.themes.dropdownmenu_content(
            rx.radix.themes.dropdownmenu_item("Edit", shortcut="⌘ E"),
            rx.radix.themes.dropdownmenu_item("Share"),
            rx.radix.themes.dropdownmenu_item("Delete", shortcut="⌘ ⌫", color="red"),
            rx.radix.themes.dropdownmenu_sub(
                rx.radix.themes.dropdownmenu_sub_trigger("More"),
                rx.radix.themes.dropdownmenu_sub_content(
                    rx.radix.themes.dropdownmenu_item("Eradicate"),
                    rx.radix.themes.dropdownmenu_item("Duplicate"),
                    rx.radix.themes.dropdownmenu_item("Archive"),
                ),
            ),
            **props,
        ),
    )

DropdownMenuItem: |
    lambda **props: rx.radix.themes.dropdownmenu_root(
        rx.radix.themes.dropdownmenu_trigger(rx.radix.themes.button("drop down menu")),
        rx.radix.themes.dropdownmenu_content(
            rx.radix.themes.dropdownmenu_item("Edit", shortcut="⌘ E", **props),
            rx.radix.themes.dropdownmenu_item("Share", **props),
            rx.radix.themes.dropdownmenu_item("Delete", shortcut="⌘ ⌫", color="red", **props),
            rx.radix.themes.dropdownmenu_sub(
                rx.radix.themes.dropdownmenu_sub_trigger("More"),
                rx.radix.themes.dropdownmenu_sub_content(
                    rx.radix.themes.dropdownmenu_item("Eradicate", **props),
                    rx.radix.themes.dropdownmenu_item("Duplicate", **props),
                    rx.radix.themes.dropdownmenu_item("Archive", **props),
                ),
            ),
        ),
    )


---


# Check Out Low Level Docs! High Level API Coming Soon.

