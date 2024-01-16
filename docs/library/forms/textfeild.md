---
components:
    - rx.radix.themes.TextFieldRoot
    - rx.radix.themes.TextFieldInput
    - rx.radix.themes.TextFieldSlot
---

```python exec
import reflex as rx
import reflex.components.radix.themes as rdxt
```

# TextField

A text field is an input field that users can type into. This component uses Radix's [text field](https://radix-ui.com/primitives/docs/components/text-field) component.

## Basic Example

```python demo
rdxt.textfield_root(
    rdxt.textfield_input(
        placeholder="Enter your name",
    ),
    rdxt.textfield_slot(
        rdxt.icon(tag="magnifying_glass"),
    ),
)
```

## Styling

### Sizes

The `size` prop changes the size of the text field. The default size is `2`.

```python demo
rx.vstack(
    rdxt.textfield_root(
        rdxt.textfield_input(
            placeholder="Small",
        ),
        rdxt.textfield_slot(
            rdxt.icon(tag="magnifying_glass"),
        ),
        size="1",
    ),
    rdxt.textfield_root(
        rdxt.textfield_input(
            placeholder="Medium",
        ),
        rdxt.textfield_slot(
            rdxt.icon(tag="magnifying_glass"),
        ),
        size="2",
    ),
    rdxt.textfield_root(
        rdxt.textfield_input(
            placeholder="Large",
        ),
        rdxt.textfield_slot(
            rdxt.icon(tag="magnifying_glass"),
        ),
        size="3",
    ),
)
```

### Variants

The `variant` prop changes the appearance of the text field. The default variant is `classic`.

```python demo
rx.vstack(
    rdxt.textfield_root(
        rdxt.textfield_input(
            placeholder="Classic",
        ),
        rdxt.textfield_slot(
            rdxt.icon(tag="magnifying_glass"),
        ),
        variant="classic",
    ),
    rdxt.textfield_root(
        rdxt.textfield_input(
            placeholder="Surface",
        ),
        rdxt.textfield_slot(
            rdxt.icon(tag="magnifying_glass"),
        ),
        variant="surface",
    ),
    rdxt.textfield_root(
        rdxt.textfield_input(
            placeholder="Soft",
        ),
        rdxt.textfield_slot(
            rdxt.icon(tag="magnifying_glass"),
        ),
        variant="soft",
    ),
)
```

### Color Scheme

The `color_scheme` prop changes the color scheme of the text field. The default color scheme is `gray`.

```python demo
rx.vstack(
    rdxt.textfield_root(
        rdxt.textfield_input(
            placeholder="Gray",
        ),
        rdxt.textfield_slot(
            rdxt.icon(tag="magnifying_glass"),
        ),
        color_scheme="grass",
    ),
    rdxt.textfield_root(
        rdxt.textfield_input(
            placeholder="Red",
        ),
        rdxt.textfield_slot(
            rdxt.icon(tag="magnifying_glass"),
        ),
        color_scheme="red",
    ),
    rdxt.textfield_root(
        rdxt.textfield_input(
            placeholder="Orange",
        ),
        rdxt.textfield_slot(
            rdxt.icon(tag="magnifying_glass"),
        ),
        color_scheme="orange",
    ),
)
```