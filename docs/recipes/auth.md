# Auth Recipes


```python exec
import reflex as rx
```

## Basic Auth

```python demo
rx.el.nav(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(src="/favicon.ico", width="2.25em",
                             height="auto", border_radius="50%"),
                    rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
                rx.hstack(
                    rx.link(rx.text("Home", size="4", weight="medium"), href="/#"),
                    rx.link(rx.text("About", size="4", weight="medium"), href="/#"),
                    rx.link(rx.text("Pricing", size="4", weight="medium"), href="/#"),
                    rx.link(rx.text("Contact", size="4", weight="medium"), href="/#"),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(src="/favicon.ico", width="2em",
                             height="auto", border_radius="50%"),
                    rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 4),
        padding="1em",
        width="100%",
        max_width="84rem",
    )
```

