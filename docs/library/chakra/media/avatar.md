---
components:
    - rx.chakra.Avatar
    - rx.chakra.AvatarBadge
    - rx.chakra.AvatarGroup
---

```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
```

# Avatar

The Avatar component is used to represent a user, and displays the profile picture, initials or fallback icon.

```python demo
rx.hstack(
    rx.avatar(size="sm"),
    rx.avatar(name="Barack Obama", size="md"),
    rx.avatar(name="Donald Trump", size="lg"),
    rx.avatar(name="Joe Biden", size="xl"),
)
```

Avatar components can be grouped into avatar groups for easier display.

```python demo
rx.avatar_group(
    rx.avatar(name="Barack Obama"),
    rx.avatar(name="Donald Trump"),
    rx.avatar(name="Joe Biden"),
)
```

Badges can also be applied to show elements about the avatar such as activity.

```python demo
rx.avatar_group(
    rx.avatar(
        rx.avatar_badge(
            box_size="1.25em", bg="green.500", border_color="green.500"
        ),
        name="Barack Obama",
    ),
    rx.avatar(
        rx.avatar_badge(
            box_size="1.25em", bg="yellow.500", border_color="red.500"
        ),
        name="Donald Trump",
    ),
)
```

If there are too many avatar to display a limit can be set using the `max_` prop.

```python demo
rx.avatar_group(
    *([rx.avatar(name="Barack Obama")] * 5),
    size="md",
    max_=3,
)
```

