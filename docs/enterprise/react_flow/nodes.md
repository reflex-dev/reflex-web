# Nodes

Nodes are the fundamental building blocks of a flow. This page explains how to define and customize nodes in Reflex Flow.

## The **Node** Type

A node is represented as a Python dictionary with the following fields:

- `id` (`str`) – Unique identifier for the node.
- `position` (`dict`) – Position of the node with `x` and `y` coordinates.
- `data` (`dict`) – Arbitrary data passed to the node component.
- `type` (`str`) – Node type defined in `node_types`.
- `sourcePosition` (`str`) – Controls source handle position ("top", "right", "bottom", "left").
- `targetPosition` (`str`) – Controls target handle position ("top", "right", "bottom", "left").
- `hidden` (`bool`) – Whether the node is visible on the canvas.
- `selected` (`bool`) – Whether the node is currently selected.
- `draggable` (`bool`) – Whether the node can be dragged.
- `selectable` (`bool`) – Whether the node can be selected.
- `connectable` (`bool`) – Whether the node can be connected to other nodes.
- `deletable` (`bool`) – Whether the node can be deleted.
- `width` (`float`) – Width of the node.
- `height` (`float`) – Height of the node.
- `parentId` (`str`) – Parent node ID for creating sub-flows.
- `style` (`dict`) – Custom styles for the node.
- `className` (`str`) – CSS class name for the node.

## Built-in Node Types

Reflex Flow includes several built-in node types:

```python
nodes: list[Node] = [
    {"id": "1", "type": "input", "position": {"x": 100, "y": 100}, "data": {"label": "Start"}},
    {"id": "2", "type": "default", "position": {"x": 300, "y": 100}, "data": {"label": "Process"}},
    {"id": "3", "type": "output", "position": {"x": 500, "y": 100}, "data": {"label": "End"}},
]
```

- **input** – Entry point with only source handles
- **default** – Standard node with both source and target handles
- **output** – Exit point with only target handles

## Basic Node Configuration

### Node Positioning

```python
node = {
    "id": "positioned-node",
    "type": "default",
    "position": {"x": 250, "y": 150},
    "data": {"label": "Positioned Node"}
}
```

### Node Styling

```python
styled_node = {
    "id": "styled-node",
    "type": "default",
    "position": {"x": 100, "y": 200},
    "data": {"label": "Custom Style"},
    "style": {
        "background": "#ff6b6b",
        "color": "white",
        "border": "2px solid #ff5252",
        "borderRadius": "8px",
        "padding": "10px"
    }
}
```

### Handle Positioning

```python
node_with_handles = {
    "id": "handle-node",
    "type": "default",
    "position": {"x": 300, "y": 300},
    "data": {"label": "Custom Handles"},
    "sourcePosition": "right",
    "targetPosition": "left"
}
```
