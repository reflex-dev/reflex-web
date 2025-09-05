# Nodes

Nodes are the fundamental building blocks of a flow. This page explains how to define and customize nodes.

## The `Node` Type

A node is represented by a `TypedDict` with the following fields:

- `id`: `str` - Unique id of a node.
- `position`: `XYPosition` - Position of a node on the pane.
- `data`: `dict[str, Any]` - Arbitrary data passed to a node.
- `type`: `str | NodeType` - Type of node defined in `node_types`.
- `sourcePosition`: `Position` - Controls source position.
- `targetPosition`: `Position` - Controls target position.
- `hidden`: `bool` - Whether or not the node should be visible on the canvas.
- `selected`: `bool` - Whether or not the node is currently selected.
- `dragging`: `bool` - Whether or not the node is currently being dragged.
- `draggable`: `bool` - Whether or not the node is able to be dragged.
- `selectable`: `bool` - Whether or not the node can be selected.
- `connectable`: `bool` - Whether or not the node can be connected.
- `deletable`: `bool` - Whether or not the node can be deleted.
- `dragHandle`: `str` - A class name that can be applied to elements inside the node that allows those elements to act as drag handles.
- `width`: `float` - The width of the node.
- `height`: `float` - The height of the node.
- `parentId`: `str` - Parent node id, used for creating sub-flows.
- `style`: `Any` - Custom styles for the node.
- `className`: `str` - A class name for the node.

## Custom Nodes

You can create custom nodes by passing a dictionary of `node_types` to the `rxe.flow` component. The keys of the dictionary are the names of your custom node types, and the values are the components that render them.

Here is an example of a custom node that displays a color picker, based on the `custom_node.py` demo:

```python
import reflex as rx
import reflex_enterprise as rxe
from reflex_enterprise.components.flow.types import Node
from typing import Any

class CustomNodeState(rx.State):
    nodes: list[Node] = [
        {
            "id": "2",
            "type": "selectorNode",
            "data": {
                "color": "#c9f1dd",
            },
            "position": {"x": 300, "y": 50},
        },
    ]
    # ... other state variables and event handlers

@rx.memo
def color_selector_node(data: rx.Var[dict[str, Any]], isConnectable: rx.Var[bool]):
    data = data.to(dict)
    return rx.fragment(
        rxe.flow.handle(
            type="target",
            position="left",
            is_connectable=isConnectable,
        ),
        rx.el.div(
            "Custom Color Picker Node: ",
            rx.el.strong(data["color"]),
        ),
        rx.el.input(
            class_name="nodrag",
            type="color",
            on_change=CustomNodeState.on_change_color,
            default_value=data["color"],
        ),
        rxe.flow.handle(
            type="source",
            position="right",
            is_connectable=isConnectable,
        ),
    )

def custom_node_example():
    return rxe.flow(
        # ... other props
        nodes=CustomNodeState.nodes,
        node_types={
            "selectorNode": rx.vars.function.ArgsFunctionOperation.create(
                (
                    rx.vars.function.DestructuredArg(
                        fields=("data", "isConnectable")
                    ),
                ),
                color_selector_node(
                    data=rx.Var("data"), isConnectable=rx.Var("isConnectable")
                ),
            )
        },
    )

```

In this example:

1.  We define a component `color_selector_node` that will render our custom node.
2.  This component receives `data` and `isConnectable` as props.
3.  We use `rxe.flow.handle` to define the connection points for the node.
4.  We pass our custom node component to the `node_types` prop of `rxe.flow`.
5.  We set the `type` of a node to `"selectorNode"` to use our custom component.
