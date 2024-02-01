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
rdx = rx.radix
```

# ContextMenu

A ContextMenu is a popup menu that appears upon user interaction, such as a right-click or a hover.

## Basic Usage

A ContextMenu is composed of a `ContextMenuTrigger` and a `ContextMenuContent`. The `ContextMenuTrigger` is the element that the user interacts with to open the menu. The `ContextMenuContent` is the menu itself.

```python demo
rdx.context_menu.root(
    rdx.context_menu.trigger(
       rdx.button("Right click me"),
    ),
    rdx.context_menu.content(
        rdx.context_menu.item("Edit", shortcut="⌘ E"),
        rdx.context_menu.item("Duplicate", shortcut="⌘ D"),
        rdx.context_menu.separator(),
        rdx.context_menu.item("Archive", shortcut="⌘ N"),
        rdx.context_menu.sub(
            rdx.context_menu.sub_trigger("More"),
            rdx.context_menu.sub_content(
                rdx.context_menu.item("Move to project…"),
                rdx.context_menu.item("Move to folder…"),
                rdx.context_menu.separator(),
                rdx.context_menu.item("Advanced options…"),
            ),
        ),
        rdx.context_menu.separator(),
        rdx.context_menu.item("Share"),
        rdx.context_menu.item("Add to favorites"),
        rdx.context_menu.separator(),
        rdx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
    ),
)
```


```python demo
rdx.grid(
    rdx.context_menu.root(
        rdx.context_menu.trigger(
            rdx.button("Right click me"),
        ),
        rdx.context_menu.content(
            rdx.context_menu.item("Edit", shortcut="⌘ E"),
            rdx.context_menu.item("Duplicate", shortcut="⌘ D"),
            rdx.context_menu.separator(),
            rdx.context_menu.item("Archive", shortcut="⌘ N"),
            rdx.context_menu.separator(),
            rdx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red",
            ),
            size="1",
        ),
    ),
    rdx.context_menu.root(
        rdx.context_menu.trigger(
             rdx.button("Right click me"),
        ),
        rdx.context_menu.content(
            rdx.context_menu.item("Edit", shortcut="⌘ E"),
            rdx.context_menu.item("Duplicate", shortcut="⌘ D"),
            rdx.context_menu.separator(),
            rdx.context_menu.item("Archive", shortcut="⌘ N"),
            rdx.context_menu.separator(),
            rdx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"
            ),
            size="2",
        ),
    ),
    columns="2", 
    gap="3",
)
```