---
components:
    - rx.radix.themes.Checkbox
---

```python exec
import reflex as rx
import reflex.components.radix.themes as rdxt
```


# Checkbox

Checkboxes allow users to select one or more items from a set. This component uses Radix's [checkbox](https://radix-ui.com/primitives/docs/components/checkbox) component.

## Basic Example

```python demo
rdxt.text(
  rdxt.flex(
    rdxt.checkbox(default_checked=True),
    "Agree to Terms and Conditions", 
    gap="2",
  ),
  as_="label",
  size="2",
)
```

## Props

### Disabled

The `disabled` prop disables the button, by default it is `False`.

```python demo
rx.hstack(
    rdxt.checkbox(),
    rdxt.checkbox(disabled=True),
)
```

## Triggers

### OnCheckedChange

The `on_change` trigger is called when the checkbox is clicked.

```python demo
rdxt.checkbox(default_checked=True, on_checked_change=rx.window_alert("Checked!"))
```


## Real World Example


```python demo
rdxt.flex(
   rdxt.heading("Terms and Conditions"),
   rdxt.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed neque elit, tristique placerat feugiat ac, facilisis vitae arcu. Proin eget egestas augue. Praesent ut sem nec arcu 'pellentesque aliquet. Duis dapibus diam vel metus tempus vulputate.",
   ),
   rdxt.text(
      rdxt.flex(
        rdxt.checkbox(default_checked=True, color_scheme="indigo"),
        "I certify that I have read and agree to the terms and conditions for this reservation.", 
        gap="2",
      ),
      as_="label",
      size="2",
    ),
    rdxt.button("Book Reservation", color_scheme="indigo", width="100%"),
    direction="column",
    align_items="start",
    border="1px solid #e2e8f0",
    background_color="#f7fafc",
    border_radius="15px",
    gap="3",
    p="3",
)
```