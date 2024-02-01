---
components:
    - rx.radix.avatar
---
# Avatar

```python exec
import reflex as rx
rdx = rx.radix
from pcweb.templates.docpage import style_grid
```

The Avatar component is used to represent a user, and display their profile pictures or fallback texts such as initials.

## Basic Example

To create an avatar component with an image, pass the image URL as the `src` prop.

```python demo
rdx.avatar(src="/logo.jpg")
```

To display a text such as initials, set the `fallback` prop without passing the `src` prop.

```python demo
rdx.avatar(fallback="RX")
```

## Styling

```python eval
style_grid(component_used=rdx.avatar, component_used_str="rdx.avatar", variants=["solid", "soft"], fallback="RX")
```

### Size

The `size` prop controls the size and spacing of the avatar. The acceptable size is from `"1"` to `"9"`, with `"3"` being the default.

```python demo
rdx.flex(
    rdx.avatar(src="/logo.jpg", fallback="RX", size="1"),
    rdx.avatar(src="/logo.jpg", fallback="RX", size="2"),
    rdx.avatar(src="/logo.jpg", fallback="RX", size="3"),
    rdx.avatar(src="/logo.jpg", fallback="RX"),
    rdx.avatar(src="/logo.jpg", fallback="RX", size="4"),
    rdx.avatar(src="/logo.jpg", fallback="RX", size="5"),
    rdx.avatar(src="/logo.jpg", fallback="RX", size="6"),
    rdx.avatar(src="/logo.jpg", fallback="RX", size="7"),
    rdx.avatar(src="/logo.jpg", fallback="RX", size="8"),
    gap="1",
)
```

### Variant

The `variant` prop controls the visual style of the avatar fallback text. The variant can be `"solid"` or `"soft"`. The default is `"soft"`.

```python demo
rdx.flex(
    rdx.avatar(fallback="RX", variant="solid"),
    rdx.avatar(fallback="RX", variant="soft"),
    rdx.avatar(fallback="RX"),
    gap="2",
)
```

### Color Scheme

The `color_scheme` prop sets a specific color to the fallback text, ignoring the global theme.

```python demo
rdx.flex(
    rdx.avatar(fallback="RX", color_scheme="indigo"),
    rdx.avatar(fallback="RX", color_scheme="cyan"),
    rdx.avatar(fallback="RX", color_scheme="orange"),
    rdx.avatar(fallback="RX", color_scheme="crimson"),
    gap="2",
)
```

### High Contrast

The `high_contrast` prop increases color contrast of the fallback text with the background.

```python demo
rdx.grid(
    rdx.avatar(fallback="RX", variant="solid"),
    rdx.avatar(fallback="RX", variant="solid", high_contrast=True),
    rdx.avatar(fallback="RX", variant="soft"),
    rdx.avatar(fallback="RX", variant="soft", high_contrast=True),
    rows="2",
    gap="2",
    flow="column",
)
```

### Radius

The `radius` prop sets specific radius value, ignoring the global theme. It can take values `"none" | "small" | "medium" | "large" | "full"`.

```python demo
rdx.grid(
    rdx.avatar(src="/logo.jpg", fallback="RX", radius="none"),
    rdx.avatar(fallback="RX", radius="none"),
    rdx.avatar(src="/logo.jpg", fallback="RX", radius="small"),
    rdx.avatar(fallback="RX", radius="small"),
    rdx.avatar(src="/logo.jpg", fallback="RX", radius="medium"),
    rdx.avatar(fallback="RX", radius="medium"),
    rdx.avatar(src="/logo.jpg", fallback="RX", radius="large"),
    rdx.avatar(fallback="RX", radius="large"),
    rdx.avatar(src="/logo.jpg", fallback="RX", radius="full"),
    rdx.avatar(fallback="RX", radius="full"),
    rows="2",
    gap="2",
    flow="column",
)
```

### Fallback

The `fallback` prop indicates the rendered text when the `src` cannot be loaded.

```python demo
rdx.flex(
    rdx.avatar(fallback="RX"),
    rdx.avatar(fallback="PC"),
    gap="2",
)
```

## Final Example

As part of a user profile page, the Avatar component is used to display the user's profile picture, with the fallback text showing the user's initials. Text components displays the user's full name and username handle and a Button component shows the edit profile button.

```python demo
rdx.flex(
    rdx.avatar(src="/logo.jpg", fallback="RU", size="9"),
    rdx.text("Reflex User", weight="bold", size="4"),
    rdx.text("@reflexuser", color_scheme="gray"),
    rdx.button("Edit Profile", color_scheme="indigo", variant="solid"),
    direction="column",
    gap="1",
)
```
