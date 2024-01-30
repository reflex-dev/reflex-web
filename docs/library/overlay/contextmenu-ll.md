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

A ContextMenu is a popup menu that appears upon user interaction, such as a right-click or a hover.

## Basic Usage

A ContextMenu is composed of a `ContextMenuTrigger` and a `ContextMenuContent`. The `ContextMenuTrigger` is the element that the user interacts with to open the menu. The `ContextMenuContent` is the menu itself.

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