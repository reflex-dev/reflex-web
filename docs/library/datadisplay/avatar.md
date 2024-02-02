---
components:
    - rx.radix.themes.Avatar

prototype: |
    lambda **props: rx.radix.themes.avatar(src="/logo.jpg", **props)
---
# Avatar

```python exec
import reflex.components.radix.themes as rdxt
from pcweb.templates.docpage import style_grid
```

The Avatar component is used to represent a user, and display their profile pictures or fallback texts such as initials.

## Basic Example

To create an avatar component with an image, pass the image URL as the `src` prop.

```python demo
rdxt.avatar(src="/logo.jpg")
```

To display a text such as initials, set the `fallback` prop without passing the `src` prop.

```python demo
rdxt.avatar(fallback="RX")
```

## Styling

```python eval
style_grid(component_used=rdxt.avatar, component_used_str="rdxt.avatar", variants=["solid", "soft"], fallback="RX")
```

### Size

The `size` prop controls the size and spacing of the avatar. The acceptable size is from `"1"` to `"9"`, with `"3"` being the default.

```python demo
rdxt.flex(
    rdxt.avatar(src="/logo.jpg", fallback="RX", size="1"),
    rdxt.avatar(src="/logo.jpg", fallback="RX", size="2"),
    rdxt.avatar(src="/logo.jpg", fallback="RX", size="3"),
    rdxt.avatar(src="/logo.jpg", fallback="RX"),
    rdxt.avatar(src="/logo.jpg", fallback="RX", size="4"),
    rdxt.avatar(src="/logo.jpg", fallback="RX", size="5"),
    rdxt.avatar(src="/logo.jpg", fallback="RX", size="6"),
    rdxt.avatar(src="/logo.jpg", fallback="RX", size="7"),
    rdxt.avatar(src="/logo.jpg", fallback="RX", size="8"),
    gap="1",
)
```

### Variant

The `variant` prop controls the visual style of the avatar fallback text. The variant can be `"solid"` or `"soft"`. The default is `"soft"`.

```python demo
rdxt.flex(
    rdxt.avatar(fallback="RX", variant="solid"),
    rdxt.avatar(fallback="RX", variant="soft"),
    rdxt.avatar(fallback="RX"),
    gap="2",
)
```

### Color Scheme

The `color_scheme` prop sets a specific color to the fallback text, ignoring the global theme.

```python demo
rdxt.flex(
    rdxt.avatar(fallback="RX", color_scheme="indigo"),
    rdxt.avatar(fallback="RX", color_scheme="cyan"),
    rdxt.avatar(fallback="RX", color_scheme="orange"),
    rdxt.avatar(fallback="RX", color_scheme="crimson"),
    gap="2",
)
```

### High Contrast

The `high_contrast` prop increases color contrast of the fallback text with the background.

```python demo
rdxt.grid(
    rdxt.avatar(fallback="RX", variant="solid"),
    rdxt.avatar(fallback="RX", variant="solid", high_contrast=True),
    rdxt.avatar(fallback="RX", variant="soft"),
    rdxt.avatar(fallback="RX", variant="soft", high_contrast=True),
    rows="2",
    gap="2",
    flow="column",
)
```

### Radius

The `radius` prop sets specific radius value, ignoring the global theme. It can take values `"none" | "small" | "medium" | "large" | "full"`.

```python demo
rdxt.grid(
    rdxt.avatar(src="/logo.jpg", fallback="RX", radius="none"),
    rdxt.avatar(fallback="RX", radius="none"),
    rdxt.avatar(src="/logo.jpg", fallback="RX", radius="small"),
    rdxt.avatar(fallback="RX", radius="small"),
    rdxt.avatar(src="/logo.jpg", fallback="RX", radius="medium"),
    rdxt.avatar(fallback="RX", radius="medium"),
    rdxt.avatar(src="/logo.jpg", fallback="RX", radius="large"),
    rdxt.avatar(fallback="RX", radius="large"),
    rdxt.avatar(src="/logo.jpg", fallback="RX", radius="full"),
    rdxt.avatar(fallback="RX", radius="full"),
    rows="2",
    gap="2",
    flow="column",
)
```

### Fallback

The `fallback` prop indicates the rendered text when the `src` cannot be loaded.

```python demo
rdxt.flex(
    rdxt.avatar(fallback="RX"),
    rdxt.avatar(fallback="PC"),
    gap="2",
)
```

## Final Example

As part of a user profile page, the Avatar component is used to display the user's profile picture, with the fallback text showing the user's initials. Text components displays the user's full name and username handle and a Button component shows the edit profile button.

```python demo
rdxt.flex(
    rdxt.avatar(src="/logo.jpg", fallback="RU", size="9"),
    rdxt.text("Reflex User", weight="bold", size="4"),
    rdxt.text("@reflexuser", color_scheme="gray"),
    rdxt.button("Edit Profile", color_scheme="indigo", variant="solid"),
    direction="column",
    gap="1",
)
```
