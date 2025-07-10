---
title: TagsInput
---

# TagsInput

`rxe.mantine.tags_input` - Add and manage tags with validation and suggestions.

```md alert info
# Props use snake_case format (e.g., `max_length` instead of `maxLength`).
```

## Basic Usage

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class TagsState(rx.State):
    tags: list[str] = []

def basic_tags_input():
    return rxe.mantine.tags_input(
        value=TagsState.tags,
        on_change=TagsState.setvar("tags"),
        placeholder="Press Enter to add tags",
    )
```

## With Initial Values

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class InitialTagsState(rx.State):
    tags: list[str] = ["Python", "JavaScript"]

def initial_tags_input():
    return rxe.mantine.tags_input(
        value=InitialTagsState.tags,
        on_change=InitialTagsState.setvar("tags"),
        placeholder="Add more tags",
    )
```

## With Validation

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class ValidatedTagsState(rx.State):
    tags: list[str] = []
    error: str = ""

    @rx.event
    def validate(self, tags: list[str]):
        self.tags = tags
        if len(tags) > 5:
            self.error = "Maximum 5 tags allowed"
        else:
            self.error = ""

def validated_tags_input():
    return rxe.mantine.tags_input(
        value=ValidatedTagsState.tags,
        on_change=ValidatedTagsState.validate,
        error=ValidatedTagsState.error,
        placeholder="Max 5 tags",
    )
```

## With Suggestions

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class SuggestedTagsState(rx.State):
    tags: list[str] = []
    suggestions: list[str] = ["react", "vue", "angular", "svelte"]

    @rx.event
    def add_suggestion(self, tag: str):
        if tag not in self.tags:
            self.tags = self.tags + [tag]

def suggested_tags_input():
    return rx.vstack(
        rxe.mantine.tags_input(
            value=SuggestedTagsState.tags,
            on_change=SuggestedTagsState.setvar("tags"),
            placeholder="Type or click suggestions",
        ),
        rx.flex(
            rx.foreach(
                SuggestedTagsState.suggestions,
                lambda tag: rx.button(
                    tag,
                    on_click=lambda: SuggestedTagsState.add_suggestion(tag),
                    size="2",
                    variant="outline",
                )
            ),
            wrap="wrap",
            gap="2",
        ),
        spacing="4",
    )
```

## Styled

```python demo exec toggle
import reflex as rx
import reflex_enterprise as rxe

class StyledTagsState(rx.State):
    tags: list[str] = ["Design", "Development"]

def styled_tags_input():
    return rxe.mantine.tags_input(
        value=StyledTagsState.tags,
        on_change=StyledTagsState.setvar("tags"),
        placeholder="Add skills",
        size="lg",
        radius="xl",
        label="Skills",
        description="Add your professional skills",
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
            ("value", "list[str]", "Current tags"),
            ("on_change", "EventHandler", "Called when tags change"),
            ("placeholder", "str", "Placeholder text"),
            ("disabled", "bool", "Disable the input"),
            ("error", "str", "Error message to display"),
            ("label", "str", "Label text"),
            ("description", "str", "Description text"),
            ("size", "str", "Input size (xs, sm, md, lg, xl)"),
            ("radius", "str", "Border radius (xs, sm, md, lg, xl)"),
        ]
    ]),
    variant="ghost",
    size="2",
    width="100%",
    max_width="800px",
)
```
