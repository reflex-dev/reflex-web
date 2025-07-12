---
title: JSON Input
---

# JSON Input

`rxe.mantine.json_input` - Input and validate JSON data with automatic formatting and syntax validation.

## Basic Usage

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class JsonState(rx.State):
    data: str = ""

def basic_json_input():
    return rxe.mantine.json_input(
        value=JsonState.data,
        on_change=JsonState.setvar("data"),
        placeholder='{"key": "value"}',
    )
```

## With Formatting

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class FormattedJsonState(rx.State):
    data: str = '{"name": "John", "age": 30}'

def formatted_json_input():
    return rxe.mantine.json_input(
        value=FormattedJsonState.data,
        on_change=FormattedJsonState.setvar("data"),
        format_on_blur=True,
        placeholder="JSON will be formatted on blur",
    )
```

## With Validation

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe
import json

class ValidatedJsonState(rx.State):
    data: str = ""
    error: str = ""

    @rx.event
    def validate(self, value: str):
        self.data = value
        try:
            json.loads(value) if value else {}
            self.error = ""
        except json.JSONDecodeError as e:
            self.error = f"Invalid JSON: {str(e)}"

def validated_json_input():
    return rxe.mantine.json_input(
        value=ValidatedJsonState.data,
        on_change=ValidatedJsonState.validate,
        error=ValidatedJsonState.error,
        placeholder="Enter valid JSON",
    )
```

## Required Field

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class RequiredJsonState(rx.State):
    data: str = ""

def required_json_input():
    return rxe.mantine.json_input(
        value=RequiredJsonState.data,
        on_change=RequiredJsonState.setvar("data"),
        required=True,
        label="Configuration",
        placeholder="Required JSON field",
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
            ("value", "str", "JSON string value"),
            ("on_change", "EventHandler", "Called when value changes"),
            ("placeholder", "str", "Placeholder text"),
            ("format_on_blur", "bool", "Auto-format JSON on blur"),
            ("required", "bool", "Mark as required field"),
            ("disabled", "bool", "Disable the input"),
            ("error", "str", "Error message to display"),
            ("label", "str", "Label text"),
            ("description", "str", "Description text"),
            ("size", "str", "Input size (xs, sm, md, lg, xl)"),
        ]
    ]),
    variant="ghost",
    size="2",
    width="100%",
    max_width="800px",
)
```
