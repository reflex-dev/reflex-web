---
components:
    - rx.radix.themes.HighLevelCheckbox
    - rx.radix.themes.Checkbox
---

```python exec
import reflex as rx
import reflex.components.radix.themes as rdxt
```


# High Level Checkbox

Checkboxes allow users to select one or more items from a set.

## Basic example

```python demo
rdxt.checkbox_hl()
```

The `checkbox` component takes a `text` prop, which is the text label associated with the checkbox.

The `default_checked` prop defines whether the `checkbox` is checked by default. 

The `gap` prop determines the space between the `checkbox` and the `text` label.

```python demo
rdxt.checkbox_hl("Agree to Terms and Conditios", default_checked=True, gap="2")

```

The `size` prop determines the size of the `checkbox` and the associated `text` label.

```python demo
rdxt.checkbox_hl("Agree to Terms and Conditios", size="3")
```


### Disabled

The `disabled` prop disables the `checkbox`, by default it is `False`. A disabled `checkbox` does not respond to user interactions such as click and cannot be focused.

```python demo
rx.hstack(
    rdxt.checkbox_hl(),
    rdxt.checkbox_hl(disabled=True),
)
```

## Triggers

### OnCheckedChange

The `on_change` trigger is called when the `checkbox` is clicked.

```python demo
rdxt.checkbox_hl("Agree to Terms and Conditios", default_checked=True, on_checked_change=rx.window_alert("Checked!"))
```


The `checkbox` can also take other styling props such as `color_scheme` and `variant`. 

```python demo
rdxt.checkbox_hl("Agree to Terms and Conditios", size="3", color_scheme="red", variant="soft")
```


## Real World Example


```python demo
rdxt.flex(
    rdxt.heading("Terms and Conditions"),
    rdxt.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed neque elit, tristique placerat feugiat ac, facilisis vitae arcu. Proin eget egestas augue. Praesent ut  sem nec arcu 'pellentesque aliquet. Duis dapibus diam vel metus tempus vulputate.",
    ),
    rdxt.checkbox_hl("I certify that I have read and agree to the terms and conditions for this reservation.", gap="2", size="2", default_checked=True, color_scheme="indigo"),
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

The `disabled` prop disables the `checkbox`, by default it is `False`. A disabled `checkbox` does not respond to user interactions such as click and cannot be focused.

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