# Basic Flow Example

This example demonstrates a simple flow diagram with three nodes and two edges, showing how nodes can be connected and how edges can be animated.

### Nodes

- Input Node – starting point
- Default Node – standard content node
- Output Node – endpoint of the flow

### Edges

- Input → Default (animated)
- Default → Output

### Interactivity

- Nodes can be moved
- Edges update dynamically
- Users can drag from handles to create new edges
- Zoom, pan, and mini-map controls are available

### Visual Layout

- Flow fits viewport automatically
- Background grid for orientation
- Light and dark color modes supported

### Example Flow

```python demo exec
import reflex as rx
import reflex_enterprise as rxe
from reflex_enterprise.components.flow.types import Node, Edge

# Common style for all nodes
node_style = {
    "backgroundColor": "#ffcc00",
    "color": "#000000",
    "padding": "10px",
    "borderRadius": "5px"
}

class FlowState(rx.State):
    nodes: list[Node] = [
        {
            "id": "1",
            "type": "input",
            "position": {"x": 100, "y": 100},
            "data": {"label": "Input Node"},
            "style": node_style
        },
        {
            "id": "2",
            "type": "default",
            "position": {"x": 300, "y": 200},
            "data": {"label": "Default Node"},
            "style": node_style
        },
        {
            "id": "3",
            "type": "output",
            "position": {"x": 500, "y": 100},
            "data": {"label": "Output Node"},
            "style": node_style
        },
    ]

    edges: list[Edge] = [
        {"id": "e1-2", "source": "1", "target": "2", "animated": True},
        {"id": "e2-3", "source": "2", "target": "3"},
    ]


    @rx.event
    def set_nodes(self, nodes: list[Node]):
        self.nodes = nodes

    @rx.event
    def set_edges(self, edges: list[Edge]):
        self.edges = edges


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

            # Visual settings
            fit_view=True,
            attribution_position="bottom-right",
        ),
        height="100vh",
        width="100vw",
    )
```
