---
components:
    - rx.radix.stack
    - rx.radix.hstack
    - rx.radix.vstack
---

```python exec
import reflex as rx
```

# Stack

`Stack` is a layout component used to group elements together and apply a space between them.

`vstack` is used to stack elements in the vertical direction.

`vstack` is used to stack elements in the horizontal direction.

`stack` is used to stack elements in the vertical or horizontal direction.

These components are based on the `flex` component and therefore inherit all of its props.


```python demo
rx.hstack(
    rx.box(
        "Example", bg="red", border_radius="3px", width="10%"
    ),
    rx.box(
        "Example",
        bg="orange",
        border_radius="3px",
        width="10%",
    ),
    rx.box(
        "Example",
        bg="yellow",
        border_radius="3px",
        width="10%",
    ),
    rx.box(
        "Example",
        bg="lightblue",
        border_radius="3px",
        width="10%",
    ),
    rx.box(
        "Example",
        bg="lightgreen",
        border_radius="3px",
        width="60%",
    ),
    width="100%",
)
```



```python demo
rx.vstack(
    rx.box(
        "Example", bg="red", border_radius="3px", width="20%"
    ),
    rx.box(
        "Example",
        bg="orange",
        border_radius="3px",
        width="40%",
    ),
    rx.box(
        "Example",
        bg="yellow",
        border_radius="3px",
        width="60%",
    ),
    rx.box(
        "Example",
        bg="lightblue",
        border_radius="3px",
        width="80%",
    ),
    rx.box(
        "Example",
        bg="lightgreen",
        border_radius="3px",
        width="100%",
    ),
    width="100%",
)
```