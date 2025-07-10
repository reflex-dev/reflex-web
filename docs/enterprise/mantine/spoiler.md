---
title: Spoiler
---

# Spoiler

`rxe.mantine.spoiler` - Hide/reveal content with customizable height and labels.

## Basic Usage

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def basic_spoiler():
    return rxe.mantine.spoiler(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        max_height=100,
        show_label="Show more",
        hide_label="Show less",
    )
```

## Custom Height

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def custom_height_spoiler():
    return rxe.mantine.spoiler(
        rx.vstack(
            rx.text("This is a longer content section that will be hidden."),
            rx.text("It contains multiple paragraphs and elements."),
            rx.text("The spoiler will show only the first 50px by default."),
            rx.text("Click to reveal the rest of the content."),
            spacing="3",
        ),
        max_height=50,
        show_label="Expand",
        hide_label="Collapse",
    )
```

## With Rich Content

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def rich_content_spoiler():
    return rxe.mantine.spoiler(
        rx.vstack(
            rx.heading("Hidden Section", size="4"),
            rx.text("This spoiler contains rich content including:"),
            rx.unordered_list(
                rx.list_item("Headings and text"),
                rx.list_item("Lists and buttons"),
                rx.list_item("Any Reflex components"),
            ),
            rx.button("Hidden Button", variant="outline"),
            spacing="3",
        ),
        max_height=80,
        show_label="Show details",
        hide_label="Hide details",
    )
```

## No Animation

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

def no_animation_spoiler():
    return rxe.mantine.spoiler(
        "This spoiler reveals content instantly without animation. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        max_height=60,
        show_label="Show instantly",
        hide_label="Hide instantly",
        transition_duration=0,
    )
```

## API Reference

### Props

| Prop | Type | Description |
|------|------|-------------|
| `max_height` | `int` | Maximum height before content is hidden |
| `show_label` | `str` | Text for expand button |
| `hide_label` | `str` | Text for collapse button |
| `transition_duration` | `int` | Animation duration in ms |
