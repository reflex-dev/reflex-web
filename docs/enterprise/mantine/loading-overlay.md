---
title: Loading Overlay
---

# Loading Overlay

`rxe.mantine.loading_overlay` - Display loading state over content to prevent interaction during async operations.

## Basic Usage

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class LoadingState(rx.State):
    loading: bool = False

    @rx.event
    def toggle(self):
        self.loading = not self.loading

def basic_loading_overlay():
    return rx.vstack(
        rxe.mantine.loading_overlay(
            rx.box(
                "Content behind overlay",
                padding="40px",
                border="1px solid #ccc",
                border_radius="8px",
            ),
            visible=LoadingState.loading,
        ),
        rx.button("Toggle Loading", on_click=LoadingState.toggle),
        spacing="4",
    )
```

## Async Operations

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class AsyncState(rx.State):
    loading: bool = False
    data: str = "No data"

    @rx.event
    async def load_data(self):
        self.loading = True
        await rx.sleep(2)
        self.data = "Data loaded!"
        self.loading = False

def async_loading_overlay():
    return rx.vstack(
        rxe.mantine.loading_overlay(
            rx.box(
                rx.text(AsyncState.data),
                padding="40px",
                border="1px solid #e0e0e0",
                border_radius="8px",
            ),
            visible=AsyncState.loading,
            loader_props={"size": "lg"},
        ),
        rx.button("Load Data", on_click=AsyncState.load_data),
        spacing="4",
    )
```

## Custom Loader

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class CustomLoaderState(rx.State):
    loading: bool = False

    @rx.event
    def toggle(self):
        self.loading = not self.loading

def custom_loader_overlay():
    return rx.vstack(
        rxe.mantine.loading_overlay(
            rx.box(
                "Custom loader styling",
                padding="40px",
                border="1px solid #e0e0e0",
                border_radius="8px",
            ),
            visible=CustomLoaderState.loading,
            loader_props={"size": "xl", "color": "red"},
            overlay_props={"radius": "md", "blur": 3},
        ),
        rx.button("Toggle Custom Loading", on_click=CustomLoaderState.toggle),
        spacing="4",
    )
```

## Form Submission

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class FormState(rx.State):
    submitting: bool = False
    submitted: bool = False

    @rx.event
    async def submit(self):
        self.submitting = True
        await rx.sleep(1.5)
        self.submitting = False
        self.submitted = True

    @rx.event
    def reset_form(self):
        self.submitted = False

def form_loading_overlay():
    return rxe.mantine.loading_overlay(
        rx.box(
            rx.cond(
                FormState.submitted,
                rx.vstack(
                    rx.text("✅ Success!"),
                    rx.button("Reset", on_click=FormState.reset_form),
                    spacing="3",
                ),
                rx.vstack(
                    rx.text("Submit Form"),
                    rx.button("Submit", on_click=FormState.submit),
                    spacing="3",
                ),
            ),
            padding="40px",
            border="1px solid #e0e0e0",
            border_radius="8px",
        ),
        visible=FormState.submitting,
    )
```

## Multiple Overlays

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class MultiState(rx.State):
    loading1: bool = False
    loading2: bool = False

    @rx.event
    async def load1(self):
        self.loading1 = True
        await rx.sleep(1)
        self.loading1 = False

    @rx.event
    async def load2(self):
        self.loading2 = True
        await rx.sleep(1.5)
        self.loading2 = False

def multi_loading_overlay():
    return rx.hstack(
        rxe.mantine.loading_overlay(
            rx.box(
                rx.vstack(
                    rx.text("Section 1"),
                    rx.button("Load", on_click=MultiState.load1, size="2"),
                    spacing="2",
                ),
                padding="20px",
                border="1px solid #e0e0e0",
                border_radius="8px",
            ),
            visible=MultiState.loading1,
        ),
        rxe.mantine.loading_overlay(
            rx.box(
                rx.vstack(
                    rx.text("Section 2"),
                    rx.button("Load", on_click=MultiState.load2, size="2"),
                    spacing="2",
                ),
                padding="20px",
                border="1px solid #e0e0e0",
                border_radius="8px",
            ),
            visible=MultiState.loading2,
        ),
        spacing="4",
    )
```

## API Reference

### Props

| Prop | Type | Description |
|------|------|-------------|
| `visible` | `bool` | Show/hide the overlay |
| `loader_props` | `dict` | Loader configuration (size, color) |
| `overlay_props` | `dict` | Overlay styling (radius, blur) |
| `z_index` | `int` | Stacking order |

### Loader Props

| Prop | Type | Options |
|------|------|---------|
| `size` | `str` | `xs`, `sm`, `md`, `lg`, `xl` |
| `color` | `str` | Any valid color |

### Overlay Props

| Prop | Type | Description |
|------|------|-------------|
| `radius` | `str` | Border radius |
| `blur` | `int` | Blur amount |
