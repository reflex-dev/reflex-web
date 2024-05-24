```python exec
import reflex as rx
from pcweb.templates.docpage import demo_box_style

# Custom styles for sidebar.
box_style = demo_box_style.copy()
del box_style["padding"]
del box_style["align_items"]
del box_style["justify_content"]
box_style["height"] = "650px"
box_style["position"] = "relative"

# Custom styles for sidebar mobile and tablet.
box_style_sm = demo_box_style.copy()
del box_style_sm["padding"]
del box_style_sm["align_items"]
del box_style_sm["justify_content"]

def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
	return rx.link(
		rx.hstack(
			rx.icon(icon),
			rx.text(text, size="4"),
			width="100%",
			padding_x="0.5rem",
			padding_y="0.75rem",
			align="center",
			style={
				"_hover": {
					"bg": rx.color("accent", 4),
					"color": rx.color("accent", 11),
				},
				"border-radius": "0.5em",
			},
		),
		href=href,
		underline="none",
		weight="medium",
		width="100%"
	)

def sidebar_items() -> rx.Component:
	return rx.vstack(
		sidebar_item("Dashboard", "layout-dashboard", "/#"),
		sidebar_item("Projects", "square-library", "/#"),
		sidebar_item("Analytics", "bar-chart-4", "/#"),
		sidebar_item("Messages", "mail", "/#"),
		spacing="1",
		width="100%"
	)
```

# Sidebar

Similar to a navigation bar, a sidebar is a common UI element found on the side of a webpage or application. It typically contains links to different sections of the site or app.

## Basic

```python exec
def sidebar() -> rx.Component:
	return rx.box(
		rx.desktop_only(
			rx.vstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em",
								height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"),
					align="center",
					justify="start",
					padding_x="0.5rem",
					width="100%"
				),
				sidebar_items(),
				spacing="5",
				#position="fixed",
				# left="0px",
				# top="0px",
				# z_index="5",
				padding_x="1em",
				padding_y="1.5em",
				bg=rx.color("accent", 3),
				align="start",
				height="100%",
				width="16em",
			),
			style=box_style
		),
		rx.mobile_and_tablet(
			rx.drawer.root(
				rx.drawer.trigger(rx.icon("align-justify", size=30)),
				rx.drawer.overlay(z_index="5"),
				rx.drawer.portal(
					rx.drawer.content(
						rx.vstack(
							rx.box(
								rx.drawer.close(rx.icon("x", size=30)),
								width="100%",
							),
							sidebar_items(),
							spacing="5",
							width="100%",
						),
						top="auto",
						right="auto",
						height="100%",
						width="20em",
						padding="1.5em",
						bg=rx.color("accent", 2)
					),
					width="100%",
				),
				direction="left"
			),
			padding="1em",
			style=box_style_sm
		),
	)
```

```python eval
sidebar()
```

```python
def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
	return rx.link(
		rx.hstack(
			rx.icon(icon),
			rx.text(text, size="4"),
			width="100%",
			padding_x="0.5rem",
			padding_y="0.75rem",
			align="center",
			style={
				"_hover": {
					"bg": rx.color("accent", 4),
					"color": rx.color("accent", 11),
				},
				"border-radius": "0.5em",
			},
		),
		href=href,
		underline="none",
		weight="medium",
		width="100%"
	)

def sidebar_items() -> rx.Component:
	return rx.vstack(
		sidebar_item("Dashboard", "layout-dashboard", "/#"),
		sidebar_item("Projects", "square-library", "/#"),
		sidebar_item("Analytics", "bar-chart-4", "/#"),
		sidebar_item("Messages", "mail", "/#"),
		spacing="1",
		width="100%"
	)

def sidebar() -> rx.Component:
	return rx.box(
		rx.desktop_only(
			rx.vstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em",
								height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"),
					align_items="center",
					padding_x="0.5rem"
				),
				sidebar_items(),
				spacing="5",
				position="fixed",
				left="0px",
				top="0px",
				z_index="5",
				padding_x="1em",
				padding_y="1.5em",
				bg=rx.color("accent", 3),
				align="start",
				height="100%",
				width="16em"
			),
		),
		rx.mobile_and_tablet(
			rx.drawer.root(
				rx.drawer.trigger(rx.icon("align-justify", size=30)),
				rx.drawer.overlay(z_index="5"),
				rx.drawer.portal(
					rx.drawer.content(
						rx.vstack(
							rx.drawer.close(rx.icon("x", size=30)),
							sidebar_items(),
							spacing="5",
							width="100%",
						),
						top="auto",
						right="auto",
						height="100%",
						width="20em",
						padding="1.5em",
						bg=rx.color("accent", 3)
					),
					width="100%"
				),
				direction="left"
			)
		)
	)
```

## Bottom user profile

```python exec
def sidebar_bottom_profile() -> rx.Component:
	return rx.box(
		rx.desktop_only(
			rx.vstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em",
								height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"),
					align="center",
					justify="start",
					padding_x="0.5rem",
					width="100%"
				),
				sidebar_items(),
				rx.spacer(),
				rx.vstack(
					rx.vstack(
						sidebar_item("Settings", "settings", "/#"),
						sidebar_item("Log out", "log-out", "/#"),
						spacing="1",
						width="100%"
					),
					rx.divider(),
					rx.hstack(
						rx.icon_button(rx.icon("user"), size="3", radius="full"),
						rx.vstack(
							rx.box(
								rx.text("My account", size="3", weight="bold"),
								rx.text("user@reflex.dev", size="2", weight="medium"),
								width="100%"
							),
							spacing="0",
							align="start",
							justify="start",
							width="100%"
						),
						padding_x="0.5rem",
						align="center",
						justify="start",
						width="100%",
					),
					width="100%",
					spacing="5",
				),
				spacing="5",
				#position="fixed",
				# left="0px",
				# top="0px",
				# z_index="5",
				padding_x="1em",
				padding_y="1.5em",
				bg=rx.color("accent", 3),
				align="start",
				height="100%",
				width="16em",
			),
			style=box_style
		),
		rx.mobile_and_tablet(
			rx.drawer.root(
				rx.drawer.trigger(rx.icon("align-justify", size=30)),
				rx.drawer.overlay(z_index="5"),
				rx.drawer.portal(
					rx.drawer.content(
						rx.vstack(
							rx.box(
							rx.drawer.close(rx.icon("x", size=30)),
							width="100%",
							),
							sidebar_items(),
							rx.spacer(),
							rx.vstack(
								rx.vstack(
									sidebar_item("Settings", "settings", "/#"),
									sidebar_item("Log out", "log-out", "/#"),
									width="100%",
									spacing="1",
								),
								rx.divider(margin="0"),
								rx.hstack(
									rx.icon_button(rx.icon("user"), size="3", radius="full"),
									rx.vstack(
										rx.box(
											rx.text("My account", size="3", weight="bold"),
											rx.text("user@reflex.dev", size="2", weight="medium"),
											width="100%"
										),
										spacing="0",
										justify="start",
										width="100%",
									),
									padding_x="0.5rem",
									align="center",
									justify="start",
									width="100%",
								),
								width="100%",
								spacing="5",
							),
							spacing="5",
							width="100%",
						),
						top="auto",
						right="auto",
						height="100%",
						width="20em",
						padding="1.5em",
						bg=rx.color("accent", 2)
					),
					width="100%",
				),
				direction="left"
			),
			padding="1em",
			style=box_style_sm
		),
	)
```

```python eval
sidebar_bottom_profile()
```

```python
def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
	return rx.link(
		rx.hstack(
			rx.icon(icon),
			rx.text(text, size="4"),
			width="100%",
			padding_x="0.5rem",
			padding_y="0.75rem",
			align="center",
			style={
				"_hover": {
					"bg": rx.color("accent", 4),
					"color": rx.color("accent", 11),
				},
				"border-radius": "0.5em",
			},
		),
		href=href,
		underline="none",
		weight="medium",
		width="100%"
	)

def sidebar_items() -> rx.Component:
	return rx.vstack(
		sidebar_item("Dashboard", "layout-dashboard", "/#"),
		sidebar_item("Projects", "square-library", "/#"),
		sidebar_item("Analytics", "bar-chart-4", "/#"),
		sidebar_item("Messages", "mail", "/#"),
		spacing="1",
		width="100%"
	)

def sidebar_bottom_profile() -> rx.Component:
	return rx.box(
		rx.desktop_only(
			rx.vstack(
				rx.hstack(
					rx.image(src="/favicon.ico", width="2.25em",
								height="auto", border_radius="50%"),
					rx.heading("Reflex", size="7", weight="bold"),
					align="center",
					justify="start",
					padding_x="0.5rem",
					width="100%"
				),
				sidebar_items(),
				rx.spacer(),
				rx.vstack(
					rx.vstack(
						sidebar_item("Settings", "settings", "/#"),
						sidebar_item("Log out", "log-out", "/#"),
						spacing="1",
						width="100%"
					),
					rx.divider(),
					rx.hstack(
						rx.icon_button(rx.icon("user"), size="3", radius="full"),
						rx.vstack(
							rx.text("My account", size="3", weight="bold"),
							rx.text("user@reflex.dev",
									size="2", weight="medium"),
							spacing="0",
							width="100%",
						),
						padding_x="0.5rem",
						align="center",
						width="100%",
					),
					width="100%",
					spacing="5",
				),
				spacing="5",
				position="fixed",
				left="0px",
				top="0px",
				z_index="5",
				padding_x="1em",
				padding_y="1.5em",
				bg=rx.color("accent", 3),
				align="start",
				height="100%",
				width="16em",
			)
		),
		rx.mobile_and_tablet(
			rx.drawer.root(
				rx.drawer.trigger(rx.icon("align-justify", size=30)),
				rx.drawer.overlay(z_index="5"),
				rx.drawer.portal(
					rx.drawer.content(
						rx.vstack(
							rx.drawer.close(rx.icon("x", size=30)),
							sidebar_items(),
							rx.spacer(),
							rx.vstack(
								rx.vstack(
									sidebar_item("Settings", "settings", "/#"),
									sidebar_item("Log out", "log-out", "/#"),
									width="100%",
									spacing="1",
								),
								rx.divider(),
								rx.hstack(
									rx.icon_button(rx.icon("user"), size="3", radius="full"),
									rx.vstack(
										rx.text("My account", size="3", weight="bold"),
										rx.text("user@reflex.dev", size="2", weight="medium"),
										spacing="0",
										width="100%",
									),
									padding_x="0.5rem",
									align="center",
									width="100%",
								),
								width="100%",
								spacing="5",
							),
							spacing="5",
							width="100%",
						),
						top="auto",
						right="auto",
						height="100%",
						width="20em",
						padding="1.5em",
						bg=rx.color("accent", 2)
					),
					width="100%",
				),
				direction="left"
			)
		)
	)
```

## Top user profile

```python exec
def sidebar_top_profile() -> rx.Component:
		return rx.box(
		rx.desktop_only(
			rx.vstack(
				rx.hstack(
					rx.icon_button(rx.icon("user"), size="3", radius="full"),
                    rx.vstack(
						rx.box(
							rx.text("My account", size="3", weight="bold"),
							rx.text("user@reflex.dev", size="2", weight="medium"),
							width="100%"
						),
						spacing="0",
						justify="start",
						width="100%",
					),
                    rx.spacer(),
                    rx.icon_button(rx.icon("settings"), size="2",
                                   variant="ghost", color_scheme="gray"),
                    padding_x="0.5rem",
                    align="center",
                    width="100%",
                ),
				sidebar_items(),
				rx.spacer(),
				sidebar_item("Help & Support", "life-buoy", "/#"),
				spacing="5",
				#position="fixed",
				# left="0px",
				# top="0px",
				# z_index="5",
				padding_x="1em",
				padding_y="1.5em",
				bg=rx.color("accent", 3),
				align="start",
				height="100%",
				width="16em",
			),
			style=box_style
		),
		rx.mobile_and_tablet(
			rx.drawer.root(
				rx.drawer.trigger(rx.icon("align-justify", size=30)),
				rx.drawer.overlay(z_index="5"),
				rx.drawer.portal(
					rx.drawer.content(
						rx.vstack(
							rx.box(
								rx.drawer.close(rx.icon("x", size=30)),
								width="100%",
							),
							sidebar_items(),
							rx.spacer(),
							rx.vstack(
								sidebar_item("Help & Support", "life-buoy", "/#"),
								rx.divider(margin="0"),
								rx.hstack(
									rx.icon_button(rx.icon("user"), size="3", radius="full"),
									rx.vstack(
										rx.box(
											rx.text("My account", size="3", weight="bold"),
											rx.text("user@reflex.dev", size="2", weight="medium"),
											width="100%"
										),
										spacing="0",
										justify="start",
										width="100%",
									),
									padding_x="0.5rem",
									align="center",
									justify="start",
									width="100%",
								),
								width="100%",
								spacing="5",
							),
							spacing="5",
							width="100%",
						),
						top="auto",
						right="auto",
						height="100%",
						width="20em",
						padding="1.5em",
						bg=rx.color("accent", 2)
					),
					width="100%",
				),
				direction="left"
			),
			padding="1em",
			style=box_style_sm
		),
	)
```

```python eval
sidebar_top_profile()
```

```python
def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
	return rx.link(
		rx.hstack(
			rx.icon(icon),
			rx.text(text, size="4"),
			width="100%",
			padding_x="0.5rem",
			padding_y="0.75rem",
			align="center",
			style={
				"_hover": {
					"bg": rx.color("accent", 4),
					"color": rx.color("accent", 11),
				},
				"border-radius": "0.5em",
			},
		),
		href=href,
		underline="none",
		weight="medium",
		width="100%"
	)

def sidebar_items() -> rx.Component:
	return rx.vstack(
		sidebar_item("Dashboard", "layout-dashboard", "/#"),
		sidebar_item("Projects", "square-library", "/#"),
		sidebar_item("Analytics", "bar-chart-4", "/#"),
		sidebar_item("Messages", "mail", "/#"),
		spacing="1",
		width="100%"
	)

def sidebar_top_profile() -> rx.Component:
	return rx.box(
		rx.desktop_only(
			rx.vstack(
				rx.hstack(
					rx.icon_button(rx.icon("user"), size="3", radius="full"),
					rx.vstack(
						rx.text("My account", size="3", weight="bold"),
						rx.text("user@reflex.dev", size="2", weight="medium"),
						spacing="0",
						justify="start",
						width="100%",
					),
					rx.spacer(),
					rx.icon_button(rx.icon("settings"), size="2", variant="ghost", color_scheme="gray"),
					align="center",
					justify="start",
					padding_x="0.5rem",
					width="100%"
				),
				sidebar_items(),
				rx.spacer(),
				sidebar_item("Help & Support", "life-buoy", "/#"),
				spacing="5",
				position="fixed",
				left="0px",
				top="0px",
				z_index="5",
				padding_x="1em",
				padding_y="1.5em",
				bg=rx.color("accent", 3),
				align="start",
				height="100%",
				width="16em",
			)
		),
		rx.mobile_and_tablet(
			rx.drawer.root(
				rx.drawer.trigger(rx.icon("align-justify", size=30)),
				rx.drawer.overlay(z_index="5"),
				rx.drawer.portal(
					rx.drawer.content(
						rx.vstack(
							rx.drawer.close(rx.icon("x", size=30)),
							sidebar_items(),
							rx.spacer(),
							rx.vstack(
								sidebar_item("Help & Support", "life-buoy", "/#"),
								rx.divider(margin="0"),
								rx.hstack(
									rx.icon_button(rx.icon("user"), size="3", radius="full"),
									rx.vstack(
										rx.text("My account", size="3", weight="bold"),
										rx.text("user@reflex.dev", size="2", weight="medium"),
										spacing="0",
										justify="start",
										width="100%",
									),
									padding_x="0.5rem",
									align="center",
									justify="start",
									width="100%",
								),
								width="100%",
								spacing="5",
							),
							spacing="5",
							width="100%",
						),
						top="auto",
						right="auto",
						height="100%",
						width="20em",
						padding="1.5em",
						bg=rx.color("accent", 2)
					),
					width="100%",
				),
				direction="left"
			)
		)
	)
```

