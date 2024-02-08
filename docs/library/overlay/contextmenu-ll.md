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
---


```python exec
import reflex as rx
```

# ContextMenu

A Context Menu is a popup menu that appears upon user interaction, such as a right-click or a hover.

## Basic Usage

A Context Menu is composed of a `contextmenu_root`, a `contextmenu_trigger` and a `contextmenu_content`. The `context_menu_root` contains all the parts of a context menu. The `contextmenu_trigger` is the element that the user interacts with to open the menu. It wraps the element that will open the context menu. The `contextmenu_content` is the component that pops out when the context menu is open.

The `contextmenu_item` contains the actual context menu items and sits under the `contextmenu_content`. 

The `contextmenu_sub` contains all the parts of a submenu. There is a `contextmenu_sub_trigger`, which is an item that opens a submenu. It must be rendered inside a `contextmenu_sub` component. The `contextmenu_sub_component` is the component that pops out when a submenu is open. It must also be rendered inside a `contextmenu_sub` component. 

The `contextmenu_separator` is used to visually separate items in a context menu.


```python demo
rx.context_menu.root(
    rx.context_menu.trigger(
       rx.button("Right click me"),
    ),
    rx.context_menu.content(
        rx.context_menu.item("Edit", shortcut="⌘ E"),
        rx.context_menu.item("Duplicate", shortcut="⌘ D"),
        rx.context_menu.separator(),
        rx.context_menu.item("Archive", shortcut="⌘ N"),
        rx.context_menu.sub(
            rx.context_menu.sub_trigger("More"),
            rx.context_menu.sub_content(
                rx.context_menu.item("Move to project…"),
                rx.context_menu.item("Move to folder…"),
                rx.context_menu.separator(),
                rx.context_menu.item("Advanced options…"),
            ),
        ),
        rx.context_menu.separator(),
        rx.context_menu.item("Share"),
        rx.context_menu.item("Add to favorites"),
        rx.context_menu.separator(),
        rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
    ),
)
```


```python demo
rx.grid(
    rx.context_menu.root(
        rx.context_menu.trigger(
            rx.button("Right click me"),
        ),
        rx.context_menu.content(
            rx.context_menu.item("Edit", shortcut="⌘ E"),
            rx.context_menu.item("Duplicate", shortcut="⌘ D"),
            rx.context_menu.separator(),
            rx.context_menu.item("Archive", shortcut="⌘ N"),
            rx.context_menu.separator(),
            rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red",
            ),
            size="1",
        ),
    ),
    rx.context_menu.root(
        rx.context_menu.trigger(
             rx.button("Right click me"),
        ),
        rx.context_menu.content(
            rx.context_menu.item("Edit", shortcut="⌘ E"),
            rx.context_menu.item("Duplicate", shortcut="⌘ D"),
            rx.context_menu.separator(),
            rx.context_menu.item("Archive", shortcut="⌘ N"),
            rx.context_menu.separator(),
            rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"
            ),
            size="2",
        ),
    ),
    columns="2", 
    gap="3",
)
```