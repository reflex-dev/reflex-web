---
title: Tree
---

# Tree component

`rxe.mantine.tree` is a component for displaying hierarchical data in a tree structure. It allows users to expand and collapse nodes, making it easy to navigate through large datasets.

```python
import reflex as rx

def warning_callout():
    return rx.callout(
        "Due to some technical limitations (pydantic), the tree component only supports 5 levels of depths for the `data` props.",
        icon="triangle_alert",
        color_scheme="orange",
        size="1",
    )
```

```python
warning_callout()
```

```python
import reflex as rx
import reflex_enterprise as rxe

def tree_example():
    # return rx.text("Placeholder for tree example")
    return rxe.mantine.tree(
        data=[
            dict(
                value="0",
                label="Root",
                children=[
                    dict(value="0-1", label="Child 1"),
                    dict(value="0-2", label="Child 2"),
                ],
            )
        ],
    )
```
