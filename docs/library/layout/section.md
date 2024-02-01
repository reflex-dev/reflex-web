---
components:
  - rx.radix.section
---

```python exec
import reflex as rx
rdx = rx.radix
```

# Section

Denotes a section of page content, providing vertical padding by default.

Primarily this is a semantic component that is used to group related textual content.

## Basic Example

```python demo
rdx.box(
    rdx.section(
        rdx.heading("First"),
        rdx.text("This is the first content section"),
        padding_left="12px",
        padding_right="12px",
        background_color="var(--gray-2)",
    ),
    rdx.section(
        rdx.heading("Second"),
        rdx.text("This is the second content section"),
        padding_left="12px",
        padding_right="12px",
        background_color="var(--gray-2)",
    ),
    width="100%",
)
```