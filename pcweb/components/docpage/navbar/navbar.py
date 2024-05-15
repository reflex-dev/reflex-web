"""UI and logic for the navbar component."""
import reflex as rx

from pcweb.pages.docs import wrapping_react, styling, custom_components as custom_c, getting_started, hosting
from pcweb.pages.docs.library import library
from pcweb.pages.docs.custom_components import custom_components
from pcweb.pages.docs.gallery import gallery
from .buttons.github import github
from .buttons.color import color
from .buttons.sidebar import sidebar_button
from .search import search_bar
from .state import NavbarState
from pcweb.components.docpage.navbar.nav_menu.nav_menu import nav_menu

def resource_header(text, url):
    return rx.link(
        rx.text(
            text,
            color=rx.color("mauve", 12),
            font_weight="600",
        ),
        href=url,
    )


def resources_item(text, url, icon):
    return rx.link(
        rx.flex(
            rx.icon(icon, size=20, color=rx.color("mauve", 10)),
            rx.text(text, color=rx.color("mauve", 10)),
            wrap="nowrap",
            spacing="2",
        ),
        href=url,
    )


def banner():
    return rx.cond(
        NavbarState.banner,
        rx.box(
            rx.hstack(
                rx.text(
                    " 🚀 Reflex live on Product Hunt! Check out our launch ", 
                    rx.link(
                        "here",
                        href="https://www.producthunt.com/posts/reflex-6",
                        style={
                            "text_decoration": "underline",
                        },
                        color="#fff",
                        is_external=True,
                    ),
                    ". 🎉",
                    font_weight=600,
                    text_align="center",
                    width="100%",
                ),
                rx.icon(
                    tag="x",
                    z_index=1000,
                    on_click=NavbarState.toggle_banner,
                ),
                width="100%",
                align_items="center",
            ),
            color="#fff",
            background_color=rx.color("violet", 9),
            border_bottom=f"1px solid {rx.color('mauve', 4)}",
            padding_y=["0.8em", "0.8em", "0.5em"],
            width="100%",
        ),
    )


def menu_trigger():
    return rx.flex(
        rx.text(
            "Components", 
            color=rx.color("mauve", 11),
            font="Instrument Sans",
            weight="medium",
            style={"font-size":"16px"},
        ),
        rx.icon(tag="chevron_down", color=rx.color("mauve", 11), size=18),
        rx.badge("New", variant="solid"),
        align_items="center",
        _hover={
            "cursor": "pointer",
        },
        spacing="1",
    )

def menu_content():
    return rx.flex(
        rx.flex(
            rx.flex(
                resource_header("Core Components", library.path),
                resources_item("Library", library.path, "library-big"),
                resources_item("Theming", styling.theming.path,"palette"),
                direction="column",
                align_items="start",
                padding="20px",
                spacing="3",
                background_color=rx.color("mauve", 3),
            ),
            rx.flex(
                rx.flex(
                    resource_header("Custom Components", custom_components.path),
                    rx.badge("New", variant="solid"),
                    align_items="center",
                    spacing="1",
                ),
                resources_item(
                    "Community Library", custom_components.path, "library-big"
                ),
                resources_item(
                    "Wrapping React", wrapping_react.overview.path, "atom"
                ),
                resources_item(
                    "Publishing Components", custom_c.overview.path, "globe"
                ),
                direction="column",
                align_items="start",
                height="200px",
                padding_y="20px",
                padding_left="10px",
                padding_right="40px",
                spacing="3",
            ),
            spacing="6",
            max_width="1000px",
            height="200px",
        ),
        border=f"1px solid {rx.color('mauve', 4)}",
        background=rx.color("mauve", 1),
        max_width="1000px",
        height="200px",
        padding="0",
        overflow="hidden",
        border_radius="8px",
    )

def components_section():
    return nav_menu.root(
        nav_menu.list(
            nav_menu.item(
                nav_menu.trigger(
                    menu_trigger(),
                    style=None,
                ),
                nav_menu.content(
                    menu_content(),
                ),
            ),
            background_color = "transparent",
        ),
        nav_menu.indicator(className="Arrow"),
        nav_menu.viewport(),
    )


def link_item(name: str, url: str):
    return rx.link(
        rx.center(
            rx.text(
                name, 
                color=rx.color("mauve", 11),
                font="Instrument Sans",
                style={"font-size":"16px"},
                weight="medium",
            ), 
            height="100%",
        ),
        href=url,
    )

def navigation_section():
    return rx.box(
        rx.flex(
            link_item("Intro", getting_started.introduction.path),
            link_item("Gallery", gallery.path),
            link_item("Hosting", hosting.deploy_quick_start.path),
            components_section(),
            spacing="5",
            padding_left="1.25em",
        ),
        display=["none", "none", "none", "flex", "flex", "flex"],
    )

def navbar(sidebar: rx.Component = None) -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.link(
                rx.box(
                    rx.color_mode_cond(
                        rx.image(
                            src="/logos/light/reflex.svg",
                            alt="Reflex Logo",
                            height="20px",
                            justify="start",
                        ),
                        rx.image(
                            src="/logos/dark/reflex.svg",
                            alt="Reflex Logo",
                            height="20px",
                            justify="start",
                        ),
                    ),
                ),
                href="/",
            ),
            navigation_section(),
            rx.box(
                flex_grow="1",
            ),
            rx.flex(
                search_bar(),
                github(),
                rx.box(
                    color(),
                    display=["none", "none", "none", "none", "flex", "flex"],
                ),
                rx.box(
                    sidebar_button(sidebar),
                    display=["flex", "flex", "flex", "flex", "none", "none"],
                ),
                spacing="3",
                align_items="center",
            ),
            background_color=rx.color("mauve", 1),
            border_bottom=f"1px solid {rx.color('mauve', 4)}",
            width="100%",
            align_items="center",
            spacing="5",
            padding="15px",
        ),
        width="100%",
        z_index="5",
        top="0px",
        position="fixed",
        align_items="center",
        direction="column",
    )
