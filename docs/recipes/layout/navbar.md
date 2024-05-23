```python exec
import reflex as rx
```

# Navigation Bar

A navigation bar, also known as a navbar, is a common UI element found at the top of a webpage or application.
It typically provides links or buttons to the main sections of a website or application, allowing users to easily navigate and access the different pages.

Navigation bars are useful for web apps because they provide a consistent and intuitive way for users to navigate through the app.
Having a clear and consistent navigation structure can greatly improve the user experience by making it easy for users to find the information they need and access the different features of the app.

## Basic Navbar

In this recipe, we will create a navbar component that can be used to create a navigation bar for a web app.
The navbar will be a simple horizontal bar that contains a logo and a list of links to the different pages of the app.

The navbar will be created using the `rx.hstack` component, which is used to create a horizontal layout.
Since we want the navbar to be fixed to the top of the page, we set the `position` prop to `fixed` and the `top` prop to `0px`.
We also set the `z_index` prop to `5` to make sure the navbar is always on top of the screen and above the other components on the page.

```python exec
import reflex as rx


def navbar():
	return rx.hstack(
		rx.hstack(
			rx.image(src="/favicon.ico", width="2em"),
			rx.heading("My App", font_size="2em"),
		),
		rx.spacer(),
		rx.menu.root(
			rx.menu.trigger(
				rx.button("Menu"),
			),
			rx.menu.content(
				rx.menu.item("item 1"),
				rx.menu.separator(),
				rx.menu.item("Item 2"),

				rx.menu.item("Item 3"),
				width="10rem"
			),

		),
		background_color="lightgray",
		padding="1em",
		height="4em",
		width="100%",
		#z_index="5",
	)
```

```python demo box
navbar()
```

```python
def navbar():
	return rx.hstack(
		rx.hstack(
			rx.image(src="/favicon.ico", width="2em"),
			rx.heading("My App", font_size="2em"),
		),
		rx.spacer(),
		rx.menu.root(
			rx.menu.trigger(
				rx.button("Menu"),
			),
			rx.menu.content(
				rx.menu.item("item 1"),
				rx.menu.separator(),
				rx.menu.item("Item 2"),

				rx.menu.item("Item 3"),
				width="10rem"
			),

		),
		position="fixed",
		top="0px",
		background_color="lightgray",
		padding="1em",
		height="4em",
		width="100%",
		z_index="5",
	)
```

## Adding Main Content

Now that we have a navbar, we can add some content to the page.

We wrap both the navbar and the main content in a `rx.fragment` component so that they are rendered together as a single page.
We add some padding to the top of the main content so that it is not hidden behind the navbar.
You can adjust the amount of padding to suit your needs.

```python demo exec
def content():
	return rx.box(
		rx.heading("Welcome to My App"),
		rx.text("This is the main content of the page."),
	)

def index():
	return rx.fragment(
		navbar(),
		rx.container(
			content(),
			padding_top="6em",
			max_width="60em",
		),
	)
```

Here is the full code for a basic navbar with main content:

```python
import reflex as rx

def content():
	return rx.box(
		rx.heading("Welcome to My App"),
		rx.text("This is the main content of the page."),
	)

def navbar():
	return rx.hstack(
		rx.hstack(
			rx.image(src="/favicon.ico", width="2em"),
			rx.heading("My App", font_size="2em"),
		),
		rx.spacer(),
		rx.menu.root(
			rx.menu.trigger(
				rx.button("Menu"),
			),
			rx.menu.content(
				rx.menu.item("item 1"),
				rx.menu.separator(),
				rx.menu.item("Item 2"),

				rx.menu.item("Item 3"),
			),

		),
		position="fixed",
		top="0px",
		background_color="lightgray",
		padding="1em",
		height="4em",
		width="100%",
		z_index="5",
	)


def index():
	return rx.fragment(
		navbar(),
		rx.container(
			content(),
			padding_top="6em",
			max_width="60em",
		),
	)


app = rx.App()
app.add_page(index)
```

## Navbar with navigation links

```python exec
def navbar_links() -> rx.Component:
	return rx.el.nav(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					rx.link(rx.text("Home", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("About", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("Pricing", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("Contact", size="4", weight="medium"), href="/#"),
					justify="end",
					spacing="5"
				),
				justify="between",
				align_items="center"
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
					justify="end"
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		# position="fixed",
		# top="0px",
		# z_index="5",
		width="100%"
	)
```

```python demo box
navbar_links()
```

```python
def navbar_links() -> rx.Component:
	return rx.el.nav(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					rx.link(rx.text("Home", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("About", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("Pricing", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("Contact", size="4", weight="medium"), href="/#"),
					justify="end",
					spacing="5"
				),
				justify="between",
				align_items="center"
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
					justify="end"
				),
				justify="between",
				align_items="center"
			),
		),
		position="fixed",
		top="0px",
		z_index="5",
		bg=rx.color("accent", 3),
		padding="1em",
		width="100%"
	)
```

## Navbar with dropdown

```python exec
def navbar_dropdown() -> rx.Component:
	return rx.el.nav(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					rx.link(rx.text("Home", size="4", weight="medium"), href="/#"),
					rx.menu.root(
						rx.menu.trigger(
							rx.button(rx.text("Services", size="4", weight="medium"), rx.icon(
								"chevron-down"), weight="medium", variant="ghost", size="3"),
						),
						rx.menu.content(
							rx.menu.item("Service 1"),
							rx.menu.item("Service 2"),
							rx.menu.item("Service 3"),
						),
					),
					rx.link(rx.text("Pricing", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("Contact", size="4", weight="medium"), href="/#"),
					justify="end",
					spacing="5"
				),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.menu.root(
					rx.menu.trigger(rx.icon("menu", size=30)),
					rx.menu.content(
						rx.menu.item("Home"),
						rx.menu.sub(
							rx.menu.sub_trigger("Services"),
							rx.menu.sub_content(
								rx.menu.item("Service 1"),
								rx.menu.item("Service 2"),
								rx.menu.item("Service 3"),
							),
						),
						rx.menu.item("About"),
						rx.menu.item("Pricing"),
						rx.menu.item("Contact"),
					),
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		# position="fixed",
		# top="0px",
		# z_index="5",
		width="100%"
	)
```

```python demo box
navbar_dropdown()
```

```python
def navbar_dropdown() -> rx.Component:
	return rx.el.nav(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					rx.link(rx.text("Home", size="4", weight="medium"), href="/#"),
					rx.menu.root(
						rx.menu.trigger(rx.icon("menu", size=30)),
						rx.menu.content(
							rx.menu.item("Home"),
							rx.menu.sub(
								rx.menu.sub_trigger("Services"),
								rx.menu.sub_content(
									rx.menu.item("Service 1"),
									rx.menu.item("Service 2"),
									rx.menu.item("Service 3"),
								),
							),
							rx.menu.item("About"),
							rx.menu.item("Pricing"),
							rx.menu.item("Contact"),
						),
						justify="end",
					),
					rx.link(rx.text("Pricing", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("Contact", size="4", weight="medium"), href="/#"),
					justify="end",
					spacing="5"
				),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.menu.root(
					rx.menu.trigger(rx.icon("menu", size=30)),
					rx.menu.content(
						rx.menu.item("Home"),
						rx.menu.sub(
							rx.menu.sub_trigger("Services"),
							rx.menu.sub_content(
								rx.menu.item("Service 1"),
								rx.menu.item("Service 2"),
								rx.menu.item("Service 3"),
							),
						),
						rx.menu.item("About"),
						rx.menu.item("Pricing"),
						rx.menu.item("Contact"),
					),
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		position="fixed",
		top="0px",
		z_index="5",
		width="100%"
	)
```

## Navbar with search bar

```python exec
def navbar_searchbar() -> rx.Component:
	return rx.el.nav(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.input(
					rx.input.slot(rx.icon("search")),
					placeholder="Search...",
					type="search", size="2",
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.input(
					rx.input.slot(rx.icon("search")),
					placeholder="Search...",
					type="search", size="2",
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		# position="fixed",
		# top="0px",
		# z_index="5",
		width="100%"
	)
```

```python demo box
navbar_searchbar()
```

```python
def navbar_searchbar() -> rx.Component:
	return rx.el.nav(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.input(
					rx.input.slot(rx.icon("search")),
					placeholder="Search...",
					type="search", size="2",
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.input(
					rx.input.slot(rx.icon("search")),
					placeholder="Search...",
					type="search", size="2",
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		position="fixed",
		top="0px",
		z_index="5",
		width="100%"
	)
```

## Navbar with icons

```python exec
def navbar_icons_item(text: str, url: str, icon: str) -> rx.Component:
	return rx.link(rx.hstack(rx.icon(icon), rx.text(text, size="4", weight="medium")), href=url)

def navbar_icons_menu_item(text: str, icon: str, url: str) -> rx.Component:
	return rx.link(rx.hstack(rx.icon(icon, size=16), rx.text(text, size="3", weight="medium")), href=url)

def navbar_icons() -> rx.Component:
	return rx.el.nav(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					navbar_icons_item("Home", "/#", "home"),
					navbar_icons_item("Pricing", "/#", "coins"),
					navbar_icons_item("Contact", "/#", "mail"),
					navbar_icons_item("Services", "/#", "layers"),
					spacing="6",
				),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.menu.root(
					rx.menu.trigger(rx.icon("menu", size=30)),
					rx.menu.content(
						navbar_icons_menu_item("Home", "home", "/#"),
						navbar_icons_menu_item("Pricing", "coins", "/#"),
						navbar_icons_menu_item("Contact", "mail", "/#"),
						navbar_icons_menu_item("Services", "layers", "/#"),
					),
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		# position="fixed",
		# top="0px",
		# z_index="5",
		width="100%"
	)
```

```python demo box
navbar_icons()
```

```python
def navbar_icons() -> rx.Component:
	return rx.el.nav(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					navbar_icons_item("Home", "/#", "home"),
					navbar_icons_item("Pricing", "/#", "coins"),
					navbar_icons_item("Contact", "/#", "mail"),
					navbar_icons_item("Services", "/#", "layers"),
					spacing="6",
				),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.menu.root(
					rx.menu.trigger(rx.icon("menu", size=30)),
					rx.menu.content(
						navbar_icons_menu_item("Home", "home", "/#"),
						navbar_icons_menu_item("Pricing", "coins", "/#"),
						navbar_icons_menu_item("Contact", "mail", "/#"),
						navbar_icons_menu_item("Services", "layers", "/#"),
					),
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		position="fixed",
		top="0px",
		z_index="5",
		width="100%"
	)

def navbar_icons_item(text: str, url: str, icon: str) -> rx.Component:
	return rx.link(rx.hstack(rx.icon(icon), rx.text(text, size="4", weight="medium")), href=url)

def navbar_icons_menu_item(text: str, icon: str, url: str) -> rx.Component:
	return rx.link(rx.hstack(rx.icon(icon, size=16), rx.text(text, size="3", weight="medium")), href=url)
```

## Navbar with buttons

```python exec
def navbar_buttons() -> rx.Component:
	return rx.el.nav(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					rx.link(rx.text("Home", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("About", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("Pricing", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("Contact", size="4", weight="medium"), href="/#"),
					spacing="5",
				),
				rx.hstack(
					rx.button("Sign Up", size="3", variant="outline"),
					rx.button("Log In", size="3"),
					spacing="4",
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.menu.root(
					rx.menu.trigger(rx.icon("menu", size=30)),
					rx.menu.content(
						rx.menu.item("Home"),
						rx.menu.item("About"),
						rx.menu.item("Pricing"),
						rx.menu.item("Contact"),
						rx.menu.separator(),
						rx.menu.item("Log in"),
						rx.menu.item("Sign up"),
					),
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		# position="fixed",
		# top="0px",
		# z_index="5",
		width="100%"
	)
```

```python demo box
navbar_buttons()
```

```python
def navbar_buttons() -> rx.Component:
	return rx.el.nav(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					rx.link(rx.text("Home", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("About", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("Pricing", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("Contact", size="4", weight="medium"), href="/#"),
					spacing="5",
				),
				rx.hstack(
					rx.button("Sign Up", size="3", variant="outline"),
					rx.button("Log In", size="3"),
					spacing="4",
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.menu.root(
					rx.menu.trigger(rx.icon("menu", size=30)),
					rx.menu.content(
						rx.menu.item("Home"),
						rx.menu.item("About"),
						rx.menu.item("Pricing"),
						rx.menu.item("Contact"),
						rx.menu.separator(),
						rx.menu.item("Log in"),
						rx.menu.item("Sign up"),
					),
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		position="fixed",
		top="0px",
		z_index="5",
		width="100%"
	)
```

## Navbar with user profile

```python exec
def navbar_user() -> rx.Component:
	return rx.el.nav(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					rx.link(rx.text("Home", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("About", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("Pricing", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("Contact", size="4", weight="medium"), href="/#"),
					spacing="5",
				),
				rx.menu.root(
                    rx.menu.trigger(rx.icon_button(
                        rx.icon("user"), size="2", radius="full")),
                    rx.menu.content(
                        rx.menu.item("Settings"),
                        rx.menu.item("Earnings"),
                        rx.menu.separator(),
                        rx.menu.item("Log out"),
                    ),
                    justify="end",
                ),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.menu.root(
					rx.menu.trigger(rx.icon_button(
                        rx.icon("user"), size="2", radius="full")),
                    rx.menu.content(
                        rx.menu.item("Settings"),
                        rx.menu.item("Earnings"),
                        rx.menu.separator(),
                        rx.menu.item("Log out"),
                    ),
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		# position="fixed",
		# top="0px",
		# z_index="5",
		width="100%"
	)
```

```python demo box
navbar_user()
```

```python
def navbar_user() -> rx.Component:
	return rx.el.nav(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					rx.link(rx.text("Home", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("About", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("Pricing", size="4", weight="medium"), href="/#"),
					rx.link(rx.text("Contact", size="4", weight="medium"), href="/#"),
					spacing="5",
				),
				rx.menu.root(
                    rx.menu.trigger(rx.icon_button(
                        rx.icon("user"), size="2", radius="full")),
                    rx.menu.content(
                        rx.menu.item("Settings"),
                        rx.menu.item("Earnings"),
                        rx.menu.separator(),
                        rx.menu.item("Log out"),
                    ),
                    justify="end",
                ),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2em", height="auto", border_radius="50%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.menu.root(
					rx.menu.trigger(rx.icon_button(
                        rx.icon("user"), size="2", radius="full")),
                    rx.menu.content(
                        rx.menu.item("Settings"),
                        rx.menu.item("Earnings"),
                        rx.menu.separator(),
                        rx.menu.item("Log out"),
                    ),
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		position="fixed",
		top="0px",
		z_index="5",
		width="100%"
	)
```