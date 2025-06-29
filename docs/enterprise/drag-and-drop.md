---
title: Drag and Drop
---

# Drag and Drop

## Draggable Item

```python
import reflex as rx
```

```python
rx.callout(
    "To avoid compilation error, always decorate the function defining the `rxe.dnd.draggable` component with `@rx.memo`",
    icon="triangle_alert",
    color_scheme="orange",
)
```

Using `rxe.dnd.draggable` you can create a draggable item, which can be moved around the screen.

## Drop Target

Using `rxe.dnd.drop_target` you can create a drop target, which can accept draggable items.

### Simple Example

Define a draggable item and a drop target:

```python
import reflex as rx
import reflex_enterprise as rxe

@rx.memo
def draggable_item():
    return rxe.dnd.draggable(
        rx.box("Drag me!", bg="blue", color="white", p=4),
        id="draggable-item",
    )
```

## Provider

For drag and drop to work, your app need to be wrapped with the `rxe.dnd.provider` component. By default, `draggable` and `drop_target` will add the `rxe.dnd.provider` automatically to the app wrapping components tree.
