# Edges

Edges connect nodes together. This page explains how to define and customize edges.

## The `Edge` Type

An edge is represented by a `TypedDict` with the following fields:

- `id`: `str` - Unique id of an edge.
- `source`: `str` - Id of source node.
- `target`: `str` - Id of target node.
- `type`: `EdgeType | str` - Type of edge defined in `edge_types`.
- `sourceHandle`: `str | None` - Id of source handle.
- `targetHandle`: `str | None` - Id of target handle.
- `animated`: `bool` - Whether the edge should be animated.
- `hidden`: `bool` - Whether the edge should be hidden.
- `deletable`: `bool` - Whether the edge can be deleted.
- `selectable`: `bool` - Whether the edge can be selected.
- `data`: `dict[str, Any]` - Arbitrary data passed to an edge.
- `label`: `Any` - The label to render along the edge.
- `style`: `Any` - Custom styles for the edge.
- `className`: `str` - A class name for the edge.

## Custom Edges

You can create custom edges by passing a dictionary of `edge_types` to the `rxe.flow` component. The keys of the dictionary are the names of your custom edge types, and the values are the components that render them.

Here is an example of a custom edge with a button to delete it, based on the `overview.py` demo:

```python
import reflex as rx
import reflex_enterprise as rxe
from reflex_enterprise.components.flow.types import Edge, Position

@rx.memo
def button_edge(
    id: rx.Var[str],
    sourceX: rx.Var[float],
    sourceY: rx.Var[float],
    targetX: rx.Var[float],
    targetY: rx.Var[float],
    sourcePosition: rx.Var[Position],
    targetPosition: rx.Var[Position],
    markerEnd: rx.Var[str],
):
    bezier_path = rxe.components.flow.util.get_bezier_path(
        source_x=sourceX,
        source_y=sourceY,
        target_x=targetX,
        target_y=targetY,
        source_position=sourcePosition,
        target_position=targetPosition,
    )
    return rx.fragment(
        rxe.flow.base_edge(path=bezier_path.path, markerEnd=markerEnd),
        rxe.flow.edge_label_renderer(
            rx.el.div(
                rx.el.button(
                    "×",
                    class_name="button-edge__button",
                    on_click=rx.run_script(
                        rxe.flow.api.set_edges(
                            rx.vars.FunctionStringVar.create(
                                "Array.prototype.filter.call"
                            ).call(
                                rxe.flow.api.get_edges(),
                                rx.Var(f"((edge) => edge.id !== {id})"),
                            ),
                        )
                    ),
                ),
                class_name="button-edge__label nodrag nopan",
                transform=f"translate(-50%, -50%) translate({bezier_path.label_x}px,{bezier_path.label_y}px)",
            )
        ),
    )

def custom_edge_example():
    return rxe.flow(
        # ... other props
        edge_types={
            "button": rx.vars.function.ArgsFunctionOperation.create(
                (
                    rx.vars.function.DestructuredArg(
                        fields=(
                            "id",
                            "sourceX",
                            "sourceY",
                            "targetX",
                            "targetY",
                            "sourcePosition",
                            "targetPosition",
                            "markerEnd",
                        ),
                    ),
                ),
                button_edge(
                    id=rx.Var("id"),
                    sourceX=rx.Var("sourceX"),
                    sourceY=rx.Var("sourceY"),
                    targetX=rx.Var("targetX"),
                    targetY=rx.Var("targetY"),
                    sourcePosition=rx.Var("sourcePosition"),
                    targetPosition=rx.Var("targetPosition"),
                    markerEnd=rx.Var("markerEnd"),
                ),
            )
        },
    )
```

In this example:

1.  We define a component `button_edge` that will render our custom edge.
2.  This component receives props like `id`, `sourceX`, `sourceY`, etc. which describe the edge's geometry.
3.  We use `rxe.flow.util.get_bezier_path` to calculate the SVG path for the edge.
4.  We use `rxe.flow.base_edge` to render the path, and `rxe.flow.edge_label_renderer` to render a custom label (in this case, a button).
5.  The button's `on_click` handler uses `rxe.flow.api.set_edges` to remove the edge from the flow.
6.  We pass our custom edge component to the `edge_types` prop of `rxe.flow`.
