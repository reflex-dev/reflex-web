---
components:
  - rx.radix.container
---

```python exec
import reflex as rx
rdx = rx.radix
```

# Container

Constrains the maximum width of page content, while keeping flexible margins
for responsive layouts.

A Container is generally used to wrap the main content for a page.

## Basic Example

```python demo
rdx.box(
    rdx.container(
        rdx.card("This content is constrained to a max width of 448px.", width="100%"),
        size="1",
    ),
    rdx.container(
        rdx.card("This content is constrained to a max width of 688px.", width="100%"),
        size="2",
    ),
    rdx.container(
        rdx.card("This content is constrained to a max width of 880px.", width="100%"),
        size="3",
    ),
    rdx.container(
        rdx.card("This content is constrained to a max width of 1136px.", width="100%"),
        size="4",
    ),
    background_color="var(--gray-3)",
    width="100%",
)
```