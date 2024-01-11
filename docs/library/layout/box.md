---
components:
  - rx.radix.themes.Box
---

```python exec
import reflex.components.radix.themes as rdxt
```

# Box

Box is a generic container component that can be used to group other components.

By default, the Box component is based on the `div` and rendered as a block element. It's primary use is for applying styles.

## Common Layout Props

Like all other layout components, `Box` provides shorthand props for
setting the padding (`p`) and margin (`m`) using the radix `"1"` - `"9"` scale.

Horizontal (`x`), Vertical (`y`), Top (`t`), Bottom (`b`), Left (`l`), and Right (`r`)
modifiers may be appended to `p` or `m` props to set specific padding or margin values for
the component.

The `grow` and `shrink` props accept either `"0"` or `"1"` and control
whether the box should expand to fill the parent container, or whether it
should take up the smallest amount of space possible. These props are useful
when creating flexible responsive layouts.

## Basic Example

```python demo
rdxt.box(
    rdxt.box("CSS color", background_color="yellow", border_radius="2px", width="20%", m="1", p="1"),
    rdxt.box("CSS color", background_color="orange", border_radius="5px", width="40%", m="2", p="2"),
    rdxt.box("Radix Color", background_color="var(--tomato-3)", border_radius="5px", width="60%", m="3", p="3"),
    rdxt.box("Radix Color", background_color="var(--plum-3)", border_radius="10px", width="80%", m="4", p="4"),
    rdxt.box("Radix Theme Color", background_color="var(--accent-2)", radius="full", width="100%", m="5", p="5"),
    grow="1",
    text_align="center",
)
```

## Background

To set a background [image](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_images) or
[gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_images/Using_CSS_gradients),
use the [`background` CSS prop](https://developer.mozilla.org/en-US/docs/Web/CSS/background).

```python demo
rdxt.flex(
    rdxt.box(background="linear-gradient(45deg, var(--tomato-9), var(--plum-9))", width="20%", height="100%"),
    rdxt.box(background="linear-gradient(red, yellow, blue, orange)", width="20%", height="100%"),
    rdxt.box(background="radial-gradient(at 0% 30%, red 10px, yellow 30%, #1e90ff 50%)", width="20%", height="100%"),
    rdxt.box(background="center/cover url('/reflex_banner.png')", width="20%", height="100%"),
    gap="2",
    width="100%",
    height="10vh",
)
```