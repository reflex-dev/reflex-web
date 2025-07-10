---
title: Combobox
---

```python exec
import reflex as rx
import reflex_enterprise as rxe
from pcweb.pages.docs import enterprise
```

# Combobox

`rxe.mantine.combobox` - Flexible dropdown with custom target, dropdown, and options structure.

```md alert info
# The examples below use `rx.select` as a working alternative that provides similar functionality.
```

## Basic Usage

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def basic_combobox():
    return rx.select(
        ["Option 1", "Option 2", "Option 3"],
        placeholder="Select option",
    )
```

## With State

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class ComboState(rx.State):
    selected: str = ""

def stateful_combobox():
    return rx.select(
        ["Apple", "Banana", "Cherry"],
        value=ComboState.selected,
        on_change=ComboState.setvar("selected"),
        placeholder="Select fruit",
    )
```

## Searchable

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class SearchState(rx.State):
    selected: str = ""

def searchable_combobox():
    return rx.select(
        ["JavaScript", "Python", "TypeScript", "Java"],
        value=SearchState.selected,
        on_change=SearchState.setvar("selected"),
        placeholder="Search languages",
    )
```

## Clearable

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class ClearableState(rx.State):
    selected: str = "Pre-selected"

def clearable_combobox():
    return rx.select(
        ["Pre-selected", "Option 1", "Option 2"],
        value=ClearableState.selected,
        on_change=ClearableState.setvar("selected"),
        placeholder="Clearable selection",
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
            ("data", "list[str]", "Options to display"),
            ("value", "str", "Selected value"),
            ("on_change", "EventHandler", "Called when selection changes"),
            ("placeholder", "str", "Placeholder text"),
            ("searchable", "bool", "Enable search functionality"),
            ("clearable", "bool", "Show clear button"),
            ("disabled", "bool", "Disable the component"),
            ("error", "str", "Error message to display"),
            ("label", "str", "Label text"),
            ("description", "str", "Description text"),
        ]
    ]),
    variant="ghost",
    size="2",
    width="100%",
    max_width="800px",
)
```

