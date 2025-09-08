# Edges

Edges connect nodes together in a flow. This page explains how to define, customize, and interact with edges in Reflex Flow.

## The `Edge` Type

An edge is represented as a Python dictionary with the following fields:

- `id` (`str`) – Unique identifier for the edge.
- `source` (`str`) – ID of the source node.
- `target` (`str`) – ID of the target node.
- `type` (`str`) – Edge type defined in `edge_types`.
- `sourceHandle` (`str | None`) – Optional source handle ID.
- `targetHandle` (`str | None`) – Optional target handle ID.
- `animated` (`bool`) – Whether the edge should animate.
- `hidden` (`bool`) – Whether the edge is hidden.
- `deletable` (`bool`) – Whether the edge can be removed.
- `selectable` (`bool`) – Whether the edge can be selected.
- `data` (`dict`) – Arbitrary metadata.
- `label` (`Any`) – Label rendered along the edge.
- `style` (`dict`) – Custom styles.
- `className` (`str`) – CSS class for the edge.

## Basic Edge Types

Reflex Flow comes with several built-in edge types:

### Default Edge Types

```python
edges: list[Edge] = [
    {"id": "e1", "source": "1", "target": "2", "type": "default"},
    {"id": "e2", "source": "2", "target": "3", "type": "straight"},
    {"id": "e3", "source": "3", "target": "4", "type": "step"},
    {"id": "e4", "source": "4", "target": "5", "type": "smoothstep"},
    {"id": "e5", "source": "5", "target": "6", "type": "bezier"},
]
```

- **default** – Standard curved edge
- **straight** – Direct line between nodes
- **step** – Right-angled path with steps
- **smoothstep** – Smooth right-angled path
- **bezier** – Curved bezier path

## Edge Styling

### Basic Styling

Add visual styling to edges using the `style` property:

```python
edges: list[Edge] = [
    {
        "id": "styled-edge",
        "source": "1",
        "target": "2",
        "style": {
            "stroke": "#ff6b6b",
            "strokeWidth": 3,
        }
    }
]
```

### Animated Edges

Make edges animate with flowing dots:

```python
edges: list[Edge] = [
    {
        "id": "animated-edge",
        "source": "1",
        "target": "2",
        "animated": True,
        "style": {"stroke": "#4dabf7"}
    }
]
```

### Edge Labels

Add text labels to edges:

```python
edges: list[Edge] = [
    {
        "id": "labeled-edge",
        "source": "1",
        "target": "2",
        "label": "Connection",
        "style": {"stroke": "#51cf66"}
    }
]
```

## Custom Edges

For advanced use cases, you can create custom edge components that render additional controls or styling.

Here's a complete example showing various edge types and interactions:

```python
import reflex as rx
import reflex_enterprise as rxe
from reflex_enterprise.components.flow.types import Node, Edge

class EdgeExampleState(rx.State):
    nodes: list[Node] = [
        {"id": "1", "type": "input", "position": {"x": 100, "y": 50}, "data": {"label": "Input"}},
        {"id": "2", "type": "default", "position": {"x": 300, "y": 150}, "data": {"label": "Process"}},
        {"id": "3", "type": "output", "position": {"x": 500, "y": 50}, "data": {"label": "Output"}},
        {"id": "4", "type": "default", "position": {"x": 300, "y": 300}, "data": {"label": "Branch"}},
    ]

    edges: list[Edge] = [
        {
            "id": "e1-2",
            "source": "1",
            "target": "2",
            "type": "bezier",
            "animated": True,
            "label": "Input Flow"
        },
        {
            "id": "e2-3",
            "source": "2",
            "target": "3",
            "type": "straight",
            "style": {"stroke": "#ff6b6b", "strokeWidth": 3}
        },
        {
            "id": "e2-4",
            "source": "2",
            "target": "4",
            "type": "step",
            "label": "Branch",
            "style": {"stroke": "#4dabf7"}
        },
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

def edge_example_flow():
    return rx.box(
        rxe.flow(
            rxe.flow.controls(),
            rxe.flow.background(),
            rxe.flow.mini_map(),

            nodes=EdgeExampleState.nodes,
            edges=EdgeExampleState.edges,

            on_nodes_change=lambda node_changes: EdgeExampleState.set_nodes(
                rxe.flow.util.apply_node_changes(EdgeExampleState.nodes, node_changes)
            ),
            on_edges_change=lambda edge_changes: EdgeExampleState.set_edges(
                rxe.flow.util.apply_edge_changes(EdgeExampleState.edges, edge_changes)
            ),
            on_connect=lambda connection: EdgeExampleState.set_edges(
                rxe.flow.util.add_edge(connection, EdgeExampleState.edges)
            ),

            fit_view=True,
            color_mode="light",
        ),
        height="100vh",
        width="100vw",
    )
```

This example demonstrates:
- Multiple edge types (bezier, straight, step)
- Animated edges
- Styled edges with custom colors
- Edge labels
- Interactive edge creation and modification
