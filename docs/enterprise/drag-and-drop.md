---
title: Drag and Drop
---

# Drag and Drop

## Draggable Item

```md alert
# To avoid compilation error, always decorate the function defining the `rxe.dnd.draggable` component with `@rx.memo`
```

Using `rxe.dnd.draggable` you can create a draggable item, which can be moved around the screen.

## Drop Target

Using `rxe.dnd.drop_target` you can create a drop target, which can accept draggable items.

### Simple Example

Define a draggable item and a drop target:

```python
import reflex_enterprise as rxe

@rx.memo
def draggable_item():
    return rxe.dnd.draggable(
        rxe.box("Drag me!"),
        id="draggable-item",
    )
```

## Provider

For drag and drop to work, your app need to be wrapped with the `rxe.dnd.provider` component. By default, `draggable` and `drop_target` will add the `rxe.dnd.provider` automatically to the app wrapping components tree.
