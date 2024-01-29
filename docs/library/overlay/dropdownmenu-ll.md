---
components:
    - rx.radix.themes.DropdownMenuRoot
    - rx.radix.themes.DropdownMenuContent
    - rx.radix.themes.DropdownMenuTrigger
    - rx.radix.themes.DropdownMenuItem
    - rx.radix.themes.DropdownMenuSeparator
    - rx.radix.themes.DropdownMenuSubContent
---


```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```


# Dropdown Menu

A Dropdown Menu is a menu that offers a list of options that a user can select from. They are typically positioned near a button that will control their appearance and disappearance.

A Dropdown Menu is composed of a `dropdownmenu_root`, a `dropdownmenu_trigger` and a `dropdownmenu_content`. The `dropdownmenu_trigger` is the element that the user interacts with to open the menu. It wraps the element that will open the dropdown menu. The `dropdownmenu_content` is the component that pops out when the dropdown menu is open.

The `dropdownmenu_item` contains the actual dropdown menu items and sits under the `dropdownmenu_content`. The `shortcut` prop is an optional shortcut command displayed next to the item text.

The `dropdownmenu_sub` contains all the parts of a submenu. There is a `dropdownmenu_sub_trigger`, which is an item that opens a submenu. It must be rendered inside a `dropdownmenu_sub` component. The `dropdownmenu_sub_component` is the component that pops out when a submenu is open. It must also be rendered inside a `dropdownmenu_sub` component. 

The `dropdownmenu_separator` is used to visually separate items in a dropdown menu.

```python demo
dropdownmenu_root(
    dropdownmenu_trigger(
        button("Options", variant="soft"),
    ),
    dropdownmenu_content(
        dropdownmenu_item("Edit", shortcut="⌘ E"),
        dropdownmenu_item("Duplicate", shortcut="⌘ D"),
        dropdownmenu_separator(),
        dropdownmenu_item("Archive", shortcut="⌘ N"),
        dropdownmenu_sub(
            dropdownmenu_sub_trigger("More"),
            dropdownmenu_sub_content(
                dropdownmenu_item("Move to project…"),
                dropdownmenu_item("Move to folder…"),
                dropdownmenu_separator(),
                dropdownmenu_item("Advanced options…"),
            ),
        ),
        dropdownmenu_separator(),
        dropdownmenu_item("Share"),
        dropdownmenu_item("Add to favorites"),
        dropdownmenu_separator(),
        dropdownmenu_item("Delete", shortcut="⌘ ⌫", color="red"),
    ),
)
```

# Size

```python demo
flex(
    dropdownmenu_root(
        dropdownmenu_trigger(
            button("Options", variant="soft", size="2"),
        ),
        dropdownmenu_content(
            dropdownmenu_item("Edit", shortcut="⌘ E"),
            dropdownmenu_item("Duplicate", shortcut="⌘ D"),
            dropdownmenu_separator(),
            dropdownmenu_item("Archive", shortcut="⌘ N"),
            dropdownmenu_separator(),
            dropdownmenu_item("Delete", shortcut="⌘ ⌫", color="red"),
            size="2",
        ),
    ),
    dropdownmenu_root(
        dropdownmenu_trigger(
            button("Options", variant="soft", size="1"),
        ),
        dropdownmenu_content(
            dropdownmenu_item("Edit", shortcut="⌘ E"),
            dropdownmenu_item("Duplicate", shortcut="⌘ D"),
            dropdownmenu_separator(),
            dropdownmenu_item("Archive", shortcut="⌘ N"),
            dropdownmenu_separator(),
            dropdownmenu_item("Delete", shortcut="⌘ ⌫", color="red"),
            size="1",
        ),
    ),
    gap="3", 
    align="center",
)
```



## Events when the Dropdown Menu opens or closes

The `on_open_change` event, from the `dropdownmenu_root`, is called when the `open` state of the dropdown menu changes. It is used in conjunction with the `open` prop, which is passed to the event handler.


```python demo exec
class DropdownMenuState(rx.State):
    num_opens: int = 0
    opened: bool = False

    def count_opens(self, value: bool):
        self.opened = value
        self.num_opens += 1


def dropdownmenu_example():
    return flex(
        heading(f"Number of times Dropdown Menu opened or closed: {DropdownMenuState.num_opens}"),
        heading(f"Dropdown Menu open: {DropdownMenuState.opened}"),
        dropdownmenu_root(
            dropdownmenu_trigger(
                button("Options", variant="soft", size="2"),
            ),
            dropdownmenu_content(
                dropdownmenu_item("Edit", shortcut="⌘ E"),
                dropdownmenu_item("Duplicate", shortcut="⌘ D"),
                dropdownmenu_separator(),
                dropdownmenu_item("Archive", shortcut="⌘ N"),
                dropdownmenu_separator(),
                dropdownmenu_item("Delete", shortcut="⌘ ⌫", color="red"),
            ),
            on_open_change=DropdownMenuState.count_opens,
        ),
        direction="column",
        gap="3",
    )
```

