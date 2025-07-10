---
title: Tree
---

# Tree

`rxe.mantine.tree` - Display hierarchical data with expand/collapse functionality.

```md alert warning
# Maximum 5 levels of depth supported due to technical limitations.
```

## Basic Usage

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def basic_tree():
    return rxe.mantine.tree(
        data=[
            {
                "value": "root",
                "label": "Root Node",
                "children": [
                    {"value": "child1", "label": "Child 1"},
                    {"value": "child2", "label": "Child 2"},
                ],
            }
        ],
    )
```

## File System Structure

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def file_tree():
    return rxe.mantine.tree(
        data=[
            {
                "value": "src",
                "label": "📁 src",
                "children": [
                    {
                        "value": "components",
                        "label": "📁 components",
                        "children": [
                            {"value": "header.py", "label": "🐍 header.py"},
                            {"value": "footer.py", "label": "🐍 footer.py"},
                        ]
                    },
                    {"value": "main.py", "label": "🐍 main.py"},
                ]
            }
        ],
        level_offset=20,
    )
```

## With State Management

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class TreeState(rx.State):
    selected: list[str] = []
    
    @rx.event
    def handle_select(self, value: str):
        if value in self.selected:
            self.selected.remove(value)
        else:
            self.selected.append(value)

def interactive_tree():
    return rx.vstack(
        rxe.mantine.tree(
            data=[
                {
                    "value": "docs",
                    "label": "Documents",
                    "children": [
                        {"value": "report1", "label": "Report 1.pdf"},
                        {"value": "report2", "label": "Report 2.pdf"},
                    ]
                }
            ],
        ),
        rx.text(f"Selected: {TreeState.selected}"),
        spacing="4",
    )
```

## Dynamic Loading

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class DynamicTreeState(rx.State):
    data: list = []
    loading: bool = False

    @rx.event
    def load_data(self):
        self.loading = True
        yield rx.sleep(1)
        self.data = [
            {
                "value": "project",
                "label": "Project Files",
                "children": [
                    {"value": "config.json", "label": "config.json"},
                    {"value": "readme.md", "label": "README.md"},
                ]
            }
        ]
        self.loading = False

def dynamic_tree():
    return rx.vstack(
        rx.button(
            "Load Tree Data",
            on_click=DynamicTreeState.load_data,
            loading=DynamicTreeState.loading,
        ),
        rx.cond(
            DynamicTreeState.data.length() > 0,
            rxe.mantine.tree(data=DynamicTreeState.data),
            rx.text("Click to load tree data"),
        ),
        spacing="4",
    )
```

## Maximum Depth

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def max_depth_tree():
    return rxe.mantine.tree(
        data=[
            {
                "value": "l1",
                "label": "Level 1",
                "children": [
                    {
                        "value": "l2",
                        "label": "Level 2",
                        "children": [
                            {
                                "value": "l3",
                                "label": "Level 3",
                                "children": [
                                    {
                                        "value": "l4",
                                        "label": "Level 4",
                                        "children": [
                                            {"value": "l5", "label": "Level 5 (Max)"}
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        level_offset=24,
    )
```

## API Reference

### Props

```python demo-only
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell(rx.text("Prop", size="1", weight="bold", color=rx.color("slate", 11))),
            rx.table.column_header_cell(rx.text("Type", size="1", weight="bold", color=rx.color("slate", 11))),
            rx.table.column_header_cell(rx.text("Description", size="1", weight="bold", color=rx.color("slate", 11))),
            align="center"
        )
    ),
    rx.table.body(*[
        rx.table.row(
            rx.table.cell(rx.text(prop, class_name="text-sm")),
            rx.table.cell(rx.text(type_, class_name="text-sm")),
            rx.table.cell(rx.text(description, size="1", weight="regular")),
            align="center"
        ) for prop, type_, description in [
            ("data", "list[dict]", "Tree data structure"),
            ("level_offset", "int", "Indentation per level (px)"),
        ]
    ]),
    variant="ghost",
    size="2",
    width="100%",
    max_width="800px",
)
```

### Data Structure

```python
data = [
    {
        "value": "unique-id",     # Required: unique identifier
        "label": "Display Text",  # Required: text to show
        "children": [             # Optional: nested items
            # ... more nodes
        ]
    }
]
```
