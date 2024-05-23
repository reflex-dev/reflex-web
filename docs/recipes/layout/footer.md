```python exec
import reflex as rx

def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading("PRODUCTS", size="4", weight="bold", as_="h3"),
        footer_item("Web Design", "/#"),
        footer_item("Web Development", "/#"),
        footer_item("E-commerce Platforms", "/#"),
        footer_item("Content Management Systems", "/#"),
        footer_item("Mobile Apps", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading("RESOURCES", size="4", weight="bold", as_="h3"),
        footer_item("Blog", "/#"),
        footer_item("Case Studies", "/#"),
        footer_item("Whitepapers", "/#"),
        footer_item("Webinars", "/#"),
        footer_item("E-books", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )

def footer_items_3() -> rx.Component:
    return rx.flex(
        rx.heading("ABOUT US", size="4", weight="bold", as_="h3"),
        footer_item("Our Team", "/#"),
        footer_item("Careers", "/#"),
        footer_item("Contact Us", "/#"),
        footer_item("Privacy Policy", "/#"),
        footer_item("Terms of Service", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )

def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="2",
        justify="end",
        width="100%"
    )

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)
```

# Footer Bar

A footer bar is a common UI element located at the bottom of a webpage. It typically contains information about the website, such as contact details and links to other pages or sections of the site.

## Basic Footer

```python exec
def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.image(src="/favicon.ico", width="2.25em", height="auto", border_radius="50%"),
                        rx.heading("Reflex", size="7", weight="bold"),
                        align_items="center"
                    ),
                    rx.text("© 2024 Reflex, Inc", size="3", white_space="nowrap", weight="medium"),
                    spacing="4",
                    align_items=["center", "center", "start"]
                ),
                footer_items_1(),
                footer_items_2(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%"
            ),
            rx.divider(margin="0"),
            rx.hstack(
                rx.hstack(
                    footer_item("Privacy Policy", "/#"),
                    footer_item("Terms of Service", "/#"),
                    spacing="4",
                    align="center",
                    width="100%",
                ),
                socials(),
                justify="between",
                width="100%"
            ),
            spacing="6",
            width="100%"
        ),
        width="100%"
    )
```

```python demo box
footer()
```

```python
def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.image(src="/favicon.ico", width="2.25em", height="auto", border_radius="50%"),
                        rx.heading("Reflex", size="7", weight="bold"),
                        align_items="center"
                    ),
                    rx.text("© 2024 Reflex, Inc", size="3", white_space="nowrap", weight="medium"),
                    spacing="4",
                    align_items=["center", "center", "start"]
                ),
                footer_1_items_1(),
                footer_1_items_2(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%"
            ),
            rx.divider(),
            rx.hstack(
                rx.hstack(
                    footer_1_item("Privacy Policy", "/#"),
                    footer_1_item("Terms of Service", "/#"),
                    spacing="4",
                    align="center",
                    width="100%"
                ),
                socials(),
                justify="between",
                width="100%"
            ),
            spacing="6",
            width="100%",
        ),
        width="100%"
    )

def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading("PRODUCTS", size="4", weight="bold", as_="h3"),
        footer_item("Web Design", "/#"),
        footer_item("Web Development", "/#"),
        footer_item("E-commerce Platforms", "/#"),
        footer_item("Content Management Systems", "/#"),
        footer_item("Mobile Apps", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading("RESOURCES", size="4", weight="bold", as_="h3"),
        footer_item("Blog", "/#"),
        footer_item("Case Studies", "/#"),
        footer_item("Whitepapers", "/#"),
        footer_item("Webinars", "/#"),
        footer_item("E-books", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )

def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="2",
        justify="end",
        width="100%"
    )

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)
```

## Footer with newsletter form

```python exec
def footer_newsletter() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                footer_items_1(),
                footer_items_2(),
                rx.vstack(
                    rx.text("JOIN OUR NEWSLETTER", size="4", weight="bold"),
                    rx.hstack(
                        rx.input(placeholder="Your email address", type="email", size="3"),
                        rx.button("Subscribe", rx.icon("arrow-right"), size="3"),
                        justify="center",
                        width="100%"
                    ),
                    align_items=["center", "center", "start"],
                    justify="center",
                    height="100%"
                ),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%"
            ),
            rx.divider(margin="0"),
            rx.hstack(
                rx.hstack(
                    rx.image(src="/favicon.ico", width="2em", height="auto", border_radius="50%"),
                    rx.text("© 2024 Reflex, Inc", size="3", white_space="nowrap", weight="medium"),
                    spacing="2",
                    align="center",
                    width="100%"
                ),
                socials(),
                justify="between",
                width="100%"
            ),
            spacing="6",
            width="100%"
        ),
        width="100%"
    )
```

```python demo box
footer_newsletter()
```

```python
def footer_newsletter() -> rx.Component:
	return rx.el.footer(
		rx.vstack(
			rx.flex(
				footer_items_1(),
				footer_items_2(),
				rx.vstack(
					rx.text("JOIN OUR NEWSLETTER", size="4",
							weight="bold"),
					rx.hstack(
						rx.input(placeholder="Your email address", type="email", size="3"),
						rx.button("Subscribe", rx.icon("arrow-right"), size="3"),
						justify="center",
						width="100%"
					),
					align_items=["center", "center", "start"],
					justify="center",
					height="100%"
				),
				justify="between",
				spacing="6",
				flex_direction=["column", "column", "row"],
				width="100%"
			),
			rx.divider(),
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2em", height="auto", border_radius="50%"),
					rx.text("© 2024 Reflex, Inc", size="3", white_space="nowrap", weight="medium"),
					spacing="2",
					align="center",
					width="100%"
				),
				socials(),
				justify="between",
				width="100%"
			),
			spacing="6",
			width="100%"
		),
		width="100%"
	)

def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading("PRODUCTS", size="4", weight="bold", as_="h3"),
        footer_item("Web Design", "/#"),
        footer_item("Web Development", "/#"),
        footer_item("E-commerce Platforms", "/#"),
        footer_item("Content Management Systems", "/#"),
        footer_item("Mobile Apps", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading("RESOURCES", size="4", weight="bold", as_="h3"),
        footer_item("Blog", "/#"),
        footer_item("Case Studies", "/#"),
        footer_item("Whitepapers", "/#"),
        footer_item("Webinars", "/#"),
        footer_item("E-books", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )

def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="2",
        justify="end",
        width="100%"
    )

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)
```

## Footer with three columns

```python exec
def footer_three_columns() -> rx.Component:
	return rx.el.footer(
        rx.vstack(
            rx.flex(
                footer_items_1(),
                footer_items_2(),
                footer_items_3(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%"
            ),
            rx.divider(margin="0"),
            rx.hstack(
                rx.hstack(
                    rx.image(src="/favicon.ico", width="2em",
                             height="auto", border_radius="50%"),
                    rx.text("© 2024 Reflex, Inc", size="3",
                            white_space="nowrap", weight="medium"),
                    spacing="2",
                    align="center",
                    width="100%"
                ),
                socials(),
                justify="between",
                width="100%"
            ),
            spacing="6",
            width="100%"
        ),
        width="100%"
    )
```

```python demo box
footer_three_columns()
```

```python
def footer_three_columns() -> rx.Component:
	return rx.el.footer(
        rx.vstack(
            rx.flex(
                footer_items_1(),
                footer_items_2(),
                footer_items_3(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%"
            ),
            rx.divider(),
            rx.hstack(
                rx.hstack(
                    rx.image(src="/favicon.ico", width="2em",
                             height="auto", border_radius="50%"),
                    rx.text("© 2024 Reflex, Inc", size="3",
                            white_space="nowrap", weight="medium"),
                    spacing="2",
                    align="center",
                    width="100%"
                ),
                socials(),
                justify="between",
                width="100%"
            ),
            spacing="6",
            width="100%"
        ),
        width="100%"
    )

def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading("PRODUCTS", size="4", weight="bold", as_="h3"),
        footer_item("Web Design", "/#"),
        footer_item("Web Development", "/#"),
        footer_item("E-commerce Platforms", "/#"),
        footer_item("Content Management Systems", "/#"),
        footer_item("Mobile Apps", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading("RESOURCES", size="4", weight="bold", as_="h3"),
        footer_item("Blog", "/#"),
        footer_item("Case Studies", "/#"),
        footer_item("Whitepapers", "/#"),
        footer_item("Webinars", "/#"),
        footer_item("E-books", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )

def footer_items_3() -> rx.Component:
    return rx.flex(
        rx.heading("ABOUT US", size="4", weight="bold", as_="h3"),
        footer_item("Our Team", "/#"),
        footer_item("Careers", "/#"),
        footer_item("Contact Us", "/#"),
        footer_item("Privacy Policy", "/#"),
        footer_item("Terms of Service", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )

def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="2",
        justify="end",
        width="100%"
    )

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)
```
