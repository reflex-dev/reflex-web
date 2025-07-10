---
title: MultiSelect
---

# MultiSelect

`rxe.mantine.multi_select` - Select multiple options from a list with validation and search capabilities.

## Basic Usage

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class MultiSelectState(rx.State):
    selected: list[str] = []

def basic_multi_select():
    return rxe.mantine.multi_select(
        data=["React", "Vue", "Angular", "Svelte"],
        value=MultiSelectState.selected,
        on_change=MultiSelectState.setvar("selected"),
        placeholder="Select frameworks",
    )
```

## With Search

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class SearchableState(rx.State):
    selected: list[str] = []

def searchable_multi_select():
    return rxe.mantine.multi_select(
        data=["Python", "JavaScript", "TypeScript", "Java", "C++", "Go", "Rust"],
        value=SearchableState.selected,
        on_change=SearchableState.setvar("selected"),
        searchable=True,
        placeholder="Search languages",
    )
```

## With Validation

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class ValidatedState(rx.State):
    selected: list[str] = []
    error: str = ""

    @rx.event
    def validate(self, values: list[str]):
        self.selected = values
        if len(values) > 3:
            self.error = "Max 3 selections"
        else:
            self.error = ""

def validated_multi_select():
    return rxe.mantine.multi_select(
        data=["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"],
        value=ValidatedState.selected,
        on_change=ValidatedState.validate,
        error=ValidatedState.error,
        placeholder="Select up to 3",
    )
```

## Clearable

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class ClearableState(rx.State):
    selected: list[str] = ["Pre-selected"]

def clearable_multi_select():
    return rxe.mantine.multi_select(
        data=["Pre-selected", "Option 1", "Option 2", "Option 3"],
        value=ClearableState.selected,
        on_change=ClearableState.setvar("selected"),
        clearable=True,
        placeholder="Clearable selection",
    )
```

## Max Values

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class MaxValuesState(rx.State):
    selected: list[str] = []

def max_values_multi_select():
    return rxe.mantine.multi_select(
        data=["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"],
        value=MaxValuesState.selected,
        on_change=MaxValuesState.setvar("selected"),
        max_values=2,
        placeholder="Max 2 selections",
    )
```

## API Reference

### Props

| Prop | Type | Description |
|------|------|-------------|
| `data` | `list[str]` | Options to display |
| `value` | `list[str]` | Selected values |
| `on_change` | `EventHandler` | Called when selection changes |
| `placeholder` | `str` | Placeholder text |
| `searchable` | `bool` | Enable search functionality |
| `clearable` | `bool` | Show clear button |
| `max_values` | `int` | Maximum selections allowed |
| `disabled` | `bool` | Disable the component |
| `error` | `str` | Error message to display |
| `label` | `str` | Label text |
| `description` | `str` | Description text |
