---
components:
  - rx.radix.themes.Section
---

```python exec
import reflex.components.radix.themes as rdxt
```

# Section

Denotes a section of page content, providing vertical padding by default.

Primarily this is a semantic component that is used to group related textual content.

## Basic Example

```python demo
rdxt.box(
    rdxt.section(
        rdxt.heading("First"),
        rdxt.text("This is the first content section"),
        px="3",
        background_color="var(--gray-2)",
    ),
    rdxt.section(
        rdxt.heading("Second"),
        rdxt.text("This is the second content section"),
        px="2",
        background_color="var(--gray-2)",
    ),
    width="100%",
)
```