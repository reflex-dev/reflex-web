---
title: JSON Input
---

# JSON Input

`rxe.mantine.json_input` is a component that allows you to input JSON data in a user-friendly way. It provides validation and formatting features to ensure that the JSON data is correctly structured.

## Example

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class JsonInputState(rx.State):
    json_data: str = ''

def json_input_example():
    return rxe.mantine.json_input(
        id="json-input",
        value=JsonInputState.json_data,
        placeholder="Enter JSON data",
        label="JSON Input",
        description="Please enter valid JSON data.",
        required=True,
        size="md",
        format_on_blur=True,
        on_change=lambda value: JsonInputState.setvar("json_data", value),
        width="300px",
    )
```