---
components:
    - rx.radix.themes.ContextMenuRoot
    - rx.radix.themes.ContextMenuItem
    - rx.radix.themes.ContextMenuSeparator
    - rx.radix.themes.ContextMenuTrigger
    - rx.radix.themes.ContextMenuContent
    - rx.radix.themes.ContextMenuSub
    - rx.radix.themes.ContextMenuSubTrigger
    - rx.radix.themes.ContextMenuSubContent
---


```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```

# ContextMenu

A Context Menu is a popup menu that appears upon user interaction, such as a right-click or a hover.

## Basic Usage

A Context Menu is composed of a `contextmenu_root`, a `contextmenu_trigger` and a `contextmenu_content`. The `context_menu_root` contains all the parts of a context menu. The `contextmenu_trigger` is the element that the user interacts with to open the menu. It wraps the element that will open the context menu. The `contextmenu_content` is the component that pops out when the context menu is open.

The `contextmenu_item` contains the actual context menu items and sits under the `contextmenu_content`. 

The `contextmenu_sub` contains all the parts of a submenu. There is a `contextmenu_sub_trigger`, which is an item that opens a submenu. It must be rendered inside a `contextmenu_sub` component. The `contextmenu_sub_component` is the component that pops out when a submenu is open. It must also be rendered inside a `contextmenu_sub` component. 

The `contextmenu_separator` is used to visually separate items in a context menu.


```python demo
contextmenu_root(
    contextmenu_trigger(
       button("Right click me"),
    ),
    contextmenu_content(
        contextmenu_item("Edit", shortcut="⌘ E"),
        contextmenu_item("Duplicate", shortcut="⌘ D"),
        contextmenu_separator(),
        contextmenu_item("Archive", shortcut="⌘ N"),
        contextmenu_sub(
            contextmenu_sub_trigger("More"),
            contextmenu_sub_content(
                contextmenu_item("Move to project…"),
                contextmenu_item("Move to folder…"),
                contextmenu_separator(),
                contextmenu_item("Advanced options…"),
            ),
        ),
        contextmenu_separator(),
        contextmenu_item("Share"),
        contextmenu_item("Add to favorites"),
        contextmenu_separator(),
        contextmenu_item("Delete", shortcut="⌘ ⌫", color="red"),
    ),
)
```


```python demo
grid(
    contextmenu_root(
        contextmenu_trigger(
            button("Right click me"),
        ),
        contextmenu_content(
            contextmenu_item("Edit", shortcut="⌘ E"),
            contextmenu_item("Duplicate", shortcut="⌘ D"),
            contextmenu_separator(),
            contextmenu_item("Archive", shortcut="⌘ N"),
            contextmenu_separator(),
            contextmenu_item("Delete", shortcut="⌘ ⌫", color="red",
            ),
            size="1",
        ),
    ),
    contextmenu_root(
        contextmenu_trigger(
             button("Right click me"),
        ),
        contextmenu_content(
            contextmenu_item("Edit", shortcut="⌘ E"),
            contextmenu_item("Duplicate", shortcut="⌘ D"),
            contextmenu_separator(),
            contextmenu_item("Archive", shortcut="⌘ N"),
            contextmenu_separator(),
            contextmenu_item("Delete", shortcut="⌘ ⌫", color="red"
            ),
            size="2",
        ),
    ),
    columns="2", 
    gap="3",
)
```