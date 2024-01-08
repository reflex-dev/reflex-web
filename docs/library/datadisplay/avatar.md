---
components:
    - rx.radix.themes.Avatar
---
# Avatar

```python exec
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
from pcweb.templates.docpage import style_grid
```

The Avatar component is used to represent a user, and display their profile pictures or fallback texts such as initials.

## Basic Example

To create an avatar component with an image, we pass the image URL as the `src` prop.

```python demo
avatar(src="/logo.jpg")
```

If we only want to display a text such as initials, we can set it as the `fallback` prop without passing the `src` prop.

```python demo
avatar(fallback="RX")
```

## Styling

```python eval
style_grid(component_used=avatar, component_used_str="avatar", variants=["solid", "soft"], fallback="RX")
```

### Size

We use the size prop to control the size of the avatar. The acceptable size is from `"1"` to `"9"`, with `"3"` being the default.

```python demo
flex(
    avatar(src="/logo.jpg", fallback="RX", size="1"),
    avatar(src="/logo.jpg", fallback="RX", size="2"),
    avatar(src="/logo.jpg", fallback="RX", size="3"),
    avatar(src="/logo.jpg", fallback="RX"),
    avatar(src="/logo.jpg", fallback="RX", size="4"),
    avatar(src="/logo.jpg", fallback="RX", size="5"),
    avatar(src="/logo.jpg", fallback="RX", size="6"),
    avatar(src="/logo.jpg", fallback="RX", size="7"),
    avatar(src="/logo.jpg", fallback="RX", size="8"),
    gap="1",
)
```

### Variant

We use the variant prop to control the visual style of the avatar fallback text. The variant prop can be `"solid"` or `"soft"`. The default is `"soft"`.

```python demo
flex(
    avatar(fallback="RX", variant="solid"),
    avatar(fallback="RX", variant="soft"),
    avatar(fallback="RX"),
    gap="2",
)
```

### Color Scheme

We use the `color_scheme` prop to assign a specific color to the fallback text, ignoring the global theme.

```python demo
flex(
    avatar(fallback="RX", color_scheme="indigo"),
    avatar(fallback="RX", color_scheme="cyan"),
    avatar(fallback="RX", color_scheme="orange"),
    avatar(fallback="RX", color_scheme="crimson"),
    gap="2",
)
```

### High Contrast

We use the highContrast prop to increase color contrast of the fallback text with the background.

```python demo
grid(
    avatar(fallback="RX", variant="solid"),
    avatar(fallback="RX", variant="solid", high_contrast=True),
    avatar(fallback="RX", variant="soft"),
    avatar(fallback="RX", variant="soft", high_contrast=True),
    rows="2",
    gap="2",
    flow="column",
)
```

### Radius

We use the radius prop to assign a specific radius value, ignoring the global theme.

```python demo
grid(
    avatar(src="/logo.jpg", fallback="RX", radius="none"),
    avatar(fallback="RX", radius="none"),
    avatar(src="/logo.jpg", fallback="RX", radius="small"),
    avatar(fallback="RX", radius="small"),
    avatar(src="/logo.jpg", fallback="RX", radius="medium"),
    avatar(fallback="RX", radius="medium"),
    avatar(src="/logo.jpg", fallback="RX", radius="large"),
    avatar(fallback="RX", radius="large"),
    avatar(src="/logo.jpg", fallback="RX", radius="full"),
    avatar(fallback="RX", radius="full"),
    rows="2",
    gap="2",
    flow="column",
)
```

### Fallback

We use the fallback prop to modify the rendered fallback text.

```python demo
flex(
    avatar(fallback="RX"),
    avatar(fallback="PC"),
    gap="2",
)
```

## Final Example

In the following example, we use the Avatar component to build part of a user profile page. The Avatar component is used to display the user's profile picture, and the fallback text is the user's initials. We use the Text components to display the user's full name and username handle. We use the Button component to display the edit profile button.

```python demo
flex(
    avatar(src="/logo.jpg", fallback="RU", size="9"),
    text("Reflex User", weight="bold", size="4"),
    text("@reflexuser", color_scheme="gray"),
    button("Edit Profile", color_scheme="indigo", variant="solid"),
    direction="column",
    gap="1",
)
```
