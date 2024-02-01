---
components:
    - rx.radix.dropdown_menu.root
    - rx.radix.dropdown_menu.content
    - rx.radix.dropdown_menu.trigger
    - rx.radix.dropdown_menu.item
    - rx.radix.dropdown_menu.separator
    - rx.radix.dropdown_menu.sub_content
---


```python exec
import reflex as rx
rdx = rx.radix
```


# DropdownMenu

A dropdown menu is a menu that offers a list of options that a user can select from. They are typically positioned near a button that will control their appearance and disappearance.

```python demo
rdx.dropdown_menu.root(
    rdx.dropdown_menu.trigger(
        rdx.button("Options", variant="soft"),
    ),
    rdx.dropdown_menu.content(
        rdx.dropdown_menu.item("Edit", shortcut="⌘ E"),
        rdx.dropdown_menu.item("Duplicate", shortcut="⌘ D"),
        rdx.dropdown_menu.separator(),
        rdx.dropdown_menu.item("Archive", shortcut="⌘ N"),
        rdx.dropdown_menu.sub(
            rdx.dropdown_menu.sub_trigger("More"),
            rdx.dropdown_menu.sub_content(
                rdx.dropdown_menu.item("Move to project…"),
                rdx.dropdown_menu.item("Move to folder…"),
                rdx.dropdown_menu.separator(),
                rdx.dropdown_menu.item("Advanced options…"),
            ),
        ),
        rdx.dropdown_menu.separator(),
        rdx.dropdown_menu.item("Share"),
        rdx.dropdown_menu.item("Add to favorites"),
        rdx.dropdown_menu.separator(),
        rdx.dropdown_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
    ),
)
```

# Size

```python demo
rdx.flex(
    rdx.dropdown_menu.root(
        rdx.dropdown_menu.trigger(
            rdx.button("Options", variant="soft", size="2"),
        ),
        rdx.dropdown_menu.content(
            rdx.dropdown_menu.item("Edit", shortcut="⌘ E"),
            rdx.dropdown_menu.item("Duplicate", shortcut="⌘ D"),
            rdx.dropdown_menu.separator(),
            rdx.dropdown_menu.item("Archive", shortcut="⌘ N"),
            rdx.dropdown_menu.separator(),
            rdx.dropdown_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
            size="2",
        ),
    ),
    rdx.dropdown_menu.root(
        rdx.dropdown_menu.trigger(
            rdx.button("Options", variant="soft", size="1"),
        ),
        rdx.dropdown_menu.content(
            rdx.dropdown_menu.item("Edit", shortcut="⌘ E"),
            rdx.dropdown_menu.item("Duplicate", shortcut="⌘ D"),
            rdx.dropdown_menu.separator(),
            rdx.dropdown_menu.item("Archive", shortcut="⌘ N"),
            rdx.dropdown_menu.separator(),
            rdx.dropdown_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
            size="1",
        ),
    ),
    gap="3", 
    align="center",
)
```