---
components:
    - rx.context_menu.root
    - rx.context_menu.item
    - rx.context_menu.separator
    - rx.context_menu.trigger
    - rx.context_menu.content
    - rx.context_menu.sub
    - rx.context_menu.sub_trigger
    - rx.context_menu.sub_content


only_low_level:
    - True

ContextMenuRoot: |
    lambda **props: rx.context_menu.root(
            rx.context_menu.trigger(
                rx.text("Context Menu (right click)")
            ),
            rx.context_menu.content(
                rx.context_menu.item("Copy", shortcut="⌘ C"),
                rx.context_menu.item("Share"),
                rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.context_menu.sub(
                    rx.context_menu.sub_trigger("More"),
                    rx.context_menu.sub_content(
                        rx.context_menu.item("Eradicate"),
                        rx.context_menu.item("Duplicate"),
                        rx.context_menu.item("Archive"),
                    ),
                ),
            ),
            **props
        )

ContextMenuTrigger: |
    lambda **props: rx.context_menu.root(
            rx.context_menu.trigger(
                rx.text("Context Menu (right click)"),
                **props
            ),
            rx.context_menu.content(
                rx.context_menu.item("Copy", shortcut="⌘ C"),
                rx.context_menu.item("Share"),
                rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.context_menu.sub(
                    rx.context_menu.sub_trigger("More"),
                    rx.context_menu.sub_content(
                        rx.context_menu.item("Eradicate"),
                        rx.context_menu.item("Duplicate"),
                        rx.context_menu.item("Archive"),
                    ),
                ),
            ),
        )

ContextMenuContent: |
    lambda **props: rx.context_menu.root(
            rx.context_menu.trigger(
                rx.text("Context Menu (right click)")
            ),
            rx.context_menu.content(
                rx.context_menu.item("Copy", shortcut="⌘ C"),
                rx.context_menu.item("Share"),
                rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.context_menu.sub(
                    rx.context_menu.sub_trigger("More"),
                    rx.context_menu.sub_content(
                        rx.context_menu.item("Eradicate"),
                        rx.context_menu.item("Duplicate"),
                        rx.context_menu.item("Archive"),
                    ),
                ),
                **props
            ),
        )

ContextMenuSubTrigger: |
    lambda **props: rx.context_menu.root(
            rx.context_menu.trigger(
                rx.text("Context Menu (right click)")
            ),
            rx.context_menu.content(
                rx.context_menu.item("Copy", shortcut="⌘ C"),
                rx.context_menu.item("Share"),
                rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.context_menu.sub(
                    rx.context_menu.sub_trigger("More", **props),
                    rx.context_menu.sub_content(
                        rx.context_menu.item("Eradicate"),
                        rx.context_menu.item("Duplicate"),
                        rx.context_menu.item("Archive"),
                    ),
                ),
            ),
        )

ContextMenuSubContent: |
    lambda **props: rx.context_menu.root(
            rx.context_menu.trigger(
                rx.text("Context Menu (right click)")
            ),
            rx.context_menu.content(
                rx.context_menu.item("Copy", shortcut="⌘ C"),
                rx.context_menu.item("Share"),
                rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
                rx.context_menu.sub(
                    rx.context_menu.sub_trigger("More"),
                    rx.context_menu.sub_content(
                        rx.context_menu.item("Eradicate"),
                        rx.context_menu.item("Duplicate"),
                        rx.context_menu.item("Archive"),
                        **props
                    ),
                ),
            ),
        )

ContextMenuItem: |
    lambda **props: rx.context_menu.root(
            rx.context_menu.trigger(
                rx.text("Context Menu (right click)")
            ),
            rx.context_menu.content(
                rx.context_menu.item("Copy", shortcut="⌘ C", **props),
                rx.context_menu.item("Share", **props),
                rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red", **props),
                rx.context_menu.sub(
                    rx.context_menu.sub_trigger("More"),
                    rx.context_menu.sub_content(
                        rx.context_menu.item("Eradicate", **props),
                        rx.context_menu.item("Duplicate", **props),
                        rx.context_menu.item("Archive", **props),
                    ),
                ),
            ),
        )
---


```python exec
import reflex as rx
```

# Context Menu

A Context Menu is a popup menu that appears upon user interaction, such as a right-click or a hover.

## Basic Usage

A Context Menu is composed of a `context_menu.root`, a `context_menu.trigger` and a `context_menu.content`. The `context_menu_root` contains all the parts of a context menu. The `context_menu.trigger` is the element that the user interacts with to open the menu. It wraps the element that will open the context menu. The `context_menu.content` is the component that pops out when the context menu is open.

The `context_menu.item` contains the actual context menu items and sits under the `context_menu.content`.

The `context_menu.sub` contains all the parts of a submenu. There is a `context_menu.sub_trigger`, which is an item that opens a submenu. It must be rendered inside a `context_menu.sub` component. The `context_menu.sub_content` is the component that pops out when a submenu is open. It must also be rendered inside a `context_menu.sub` component.

The `context_menu.separator` is used to visually separate items in a context menu.

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
    spacing="3",
)
```
