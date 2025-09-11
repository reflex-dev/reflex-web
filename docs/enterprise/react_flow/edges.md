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
