```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
```

# List

There are three types of lists: regular lists, ordered, unordered.

The shorthand syntax used to create a list is by passing in a list of items.
These items can be components or Python primitives.

```python demo
rx.list(
    items=["Example 1", "Example 2", "Example 3"],
    spacing=".25em"
)
```

The examples below have the explicit syntax of list and list_items.
Regular lists are used to display a list of items.
They have no bullet points or numbers and stack the list items vertically.

```python demo
rx.list(
    rx.list_item("Example 1"),
    rx.list_item("Example 2"),
    rx.list_item("Example 3"),
)
```

Unordered have bullet points to display the list items.

```python demo
rx.unordered_list(
    rx.list_item("Example 1"),
    rx.list_item("Example 2"),
    rx.list_item("Example 3"),
)
```

Ordered lists have numbers to display the list items.

```python demo
rx.ordered_list(
    rx.list_item("Example 1"),
    rx.list_item("Example 2"),
    rx.list_item("Example 3"),
)
```

Lists can also be used with icons.

```python demo
rx.list(
    rx.list_item(rx.icon(tag="check_circle", color = "green"), "Allowed"),
    rx.list_item(rx.icon(tag="not_allowed", color = "red"), "Not"),
    rx.list_item(rx.icon(tag="settings", color = "grey"), "Settings"),
    spacing = ".25em"
)
```
