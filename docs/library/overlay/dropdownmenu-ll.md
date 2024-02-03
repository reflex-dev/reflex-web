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


# Dropdown Menu

A Dropdown Menu is a menu that offers a list of options that a user can select from. They are typically positioned near a button that will control their appearance and disappearance.

A Dropdown Menu is composed of a `dropdown_menu.root`, a `dropdown_menu.trigger` and a `dropdown_menu.content`. The `dropdown_menu.trigger` is the element that the user interacts with to open the menu. It wraps the element that will open the dropdown menu. The `dropdown_menu.content` is the component that pops out when the dropdown menu is open.

The `dropdown_menu.item` contains the actual dropdown menu items and sits under the `dropdown_menu.content`. The `shortcut` prop is an optional shortcut command displayed next to the item text.

The `dropdown_menu.sub` contains all the parts of a submenu. There is a `dropdown_menu.sub_trigger`, which is an item that opens a submenu. It must be rendered inside a `dropdown_menu.sub` component. The `dropdown_menu.sub_component` is the component that pops out when a submenu is open. It must also be rendered inside a `dropdown_menu.sub` component. 

The `dropdown_menu.separator` is used to visually separate items in a dropdown menu.

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



## Events when the Dropdown Menu opens or closes

The `on_open_change` event, from the `dropdown_menu.root`, is called when the `open` state of the dropdown menu changes. It is used in conjunction with the `open` prop, which is passed to the event handler.


```python demo exec
class DropdownMenuState(rx.State):
    num_opens: int = 0
    opened: bool = False

    def count_opens(self, value: bool):
        self.opened = value
        self.num_opens += 1


def dropdown_menu_example():
    return rx.flex(
        rx.heading(f"Number of times Dropdown Menu opened or closed: {DropdownMenuState.num_opens}"),
        rx.heading(f"Dropdown Menu open: {DropdownMenuState.opened}"),
        rx.dropdown_menu.root(
            rx.dropdown_menu.trigger(
                rx.button("Options", variant="soft", size="2"),
            ),
            rx.dropdown_menu.content(
                rx.dropdown_menu.item("Edit", shortcut="⌘ E"),
                rx.dropdown_menu.item("Duplicate", shortcut="⌘ D"),
                rx.dropdown_menu.separator(),
                rx.dropdown_menu.item("Archive", shortcut="⌘ N"),
                rx.dropdown_menu.separator(),
                rx.dropdown_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
            ),
            on_open_change=DropdownMenuState.count_opens,
        ),
        direction="column",
        gap="3",
    )
```

