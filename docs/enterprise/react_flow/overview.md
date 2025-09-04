# React Flow

The `rxe.flow` component is a powerful tool for creating interactive, node-based UIs, diagrams, and editors. It is built on top of [React Flow](https://reactflow.dev/) and provides a Reflex-native way to build complex flow-based applications.

## Getting Started

To use the Flow component, you need to wrap your application with a `rxe.flow.provider` and then use the `rxe.flow` component. Here is a basic example:

```python
import reflex as rx
import reflex_enterprise as rxe
from reflex_enterprise.components.flow.types import Node, Edge

class FlowState(rx.State):
    nodes: list[Node] = [
        {
            "id": "1",
            "type": "input",
            "position": {"x": 100, "y": 100},
            "data": {"label": "Input Node"}
        },
        {
            "id": "2",
            "type": "default",
            "position": {"x": 300, "y": 200},
            "data": {"label": "Default Node"}
        },
        {
            "id": "3",
            "type": "output",
            "position": {"x": 500, "y": 100},
            "data": {"label": "Output Node"}
        },
    ]

    edges: list[Edge] = [
        {"id": "e1-2", "source": "1", "target": "2", "animated": True},
        {"id": "e2-3", "source": "2", "target": "3"},
    ]

    @rx.event
    def on_nodes_change(self, changes: list[dict]):
        self.nodes = rxe.flow.util.apply_node_changes(self.nodes, changes)

    @rx.event
    def on_edges_change(self, changes: list[dict]):
        self.edges = rxe.flow.util.apply_edge_changes(self.edges, changes)

    @rx.event
    def on_connect(self, connection: dict):
        self.edges = rxe.flow.util.add_edge(connection, self.edges)

def flow_example():
    return rx.box(
        rxe.flow(
            # Core flow components
            rxe.flow.controls(),  # Zoom and pan controls
            rxe.flow.background(),  # Grid background
            rxe.flow.mini_map(),  # Mini map for navigation

            # Flow configuration
            nodes=FlowState.nodes,
            edges=FlowState.edges,
            on_nodes_change=lambda node_changes: FlowState.set_nodes(
                rxe.flow.util.apply_node_changes(FlowState.nodes, node_changes)
            ),
            on_edges_change=lambda edge_changes: FlowState.set_edges(
                rxe.flow.util.apply_edge_changes(FlowState.edges, edge_changes)
            ),
            fit_view=True,

            # Visual settings
            color_mode="light",
            attribution_position="bottom-right",
        ),
        height="100vh",
        width="100vw",
    )
```


```python exec
import reflex as rx
from reflex_image_zoom import image_zoom

def render_image():
    return rx.el.div(
        image_zoom(
            rx.image(
                src="/enterprise/flow-simple.gif",
                class_name="p-2 rounded-md h-auto",
                border=f"0.81px solid {rx.color('slate', 5)}",
            ),
            class_name="rounded-md overflow-hidden",
        ),
        class_name="w-full flex flex-col rounded-md cursor-pointer",
    )
```

```python eval

rx.el.div(render_image(), class_name="py-4")

```

This example creates a simple flow with two nodes and one edge. The `on_nodes_change`, `on_edges_change`, and `on_connect` event handlers are used to keep the state updated when the user interacts with the flow.
