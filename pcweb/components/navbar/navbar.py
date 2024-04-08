"""UI and logic for the navbar component."""
import reflex as rx
from .buttons.github import github
from .buttons.color import color
from .buttons.sidebar import sidebar_button
from .search import search_bar
from .state import NavbarState

def resource_header(text):
    return rx.text(
        text, color=rx.color("mauve", 12), font_weight="600"
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
                    " 🚀 Reflex is launching on Product Hunt on April 17th! Learn more ", 
                    rx.link(
                        "here",
                        href="https://www.producthunt.com/products/reflex-5",
                        style={
                            "text_decoration": "underline",
                        },
                        is_external=True,
                    ),
                    ". 🎉",
                    color=rx.color("mauve", 12),
                    font_weight=600,
                    text_align="center",
                    width="100%",
                ),
                rx.icon(
                    tag="x",
                    z_index=1000,
                    color=rx.color("mauve", 9),
                    on_click=NavbarState.toggle_banner,
                ),
                width="100%",
                align_items="center",
            ),
            background_color=rx.color("mauve", 1),
            border_bottom=f"1px solid {rx.color('mauve', 4)}",
            padding_y=["0.8em", "0.8em", "0.5em"],
            width="100%",
        ),
    )


def components_section():
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.flex(
                rx.text("Components", color=rx.color("mauve", 11)),
                rx.icon(tag="chevron_down", color=rx.color("mauve", 11), size=18),
                rx.badge("New", variant="solid"),
                align_items="center",
                _hover={
                    "cursor": "pointer",
                },
                spacing="1",
            )
        ),
        rx.hover_card.content(
            rx.flex(
                rx.flex(
                    resource_header("Core Components"),
                    resources_item("Library", "/docs/library", "library-big"),
                    resources_item("Theming","/docs/styling/theming/","palette"),
                    direction="column",
                    align_items="start",
                    padding_left="20px",
                    padding_right="20px",
                    padding_top="20px",
                    padding_bottom="20px",
                    spacing="3",
                    background_color=rx.color("mauve", 3),
                ),
                rx.flex(
                    rx.flex(
                        resource_header("Custom Components"),
                        rx.badge("New", variant="solid"),
                        align_items="center",
                        spacing="1",
                    ),
                    resources_item(
                        "Community Library", "/docs/hosting/deploy-quick-start/", "library-big"
                    ),
                    resources_item(
                        "Wrapping React", "/docs/wrapping-react/overview/", "atom"
                    ),
                    resources_item(
                        "Publishing Components", "/docs/custom-components/overview/", "globe"
                    ),
                    direction="column",
                    align_items="start",
                    height="200px",
                    padding_top="20px",
                    padding_left="10px",
                    padding_bottom="20px",
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
        ),
    )


def navigation_section():
    return rx.box(
        rx.flex(
            rx.link(rx.text("Intro", color=rx.color("mauve", 11)), href="/docs/"),
            rx.link(
                rx.text("Gallery", color=rx.color("mauve", 11)), href="/docs/gallery/"
            ),
            rx.link(
                rx.text("Hosting", color=rx.color("mauve", 11)), href="/docs/hosting/deploy-quick-start/"
            ),
            components_section(),
            
            spacing="5",
        ),
        display=["none", "none", "none", "flex", "flex", "flex"],
    )

def navbar(sidebar: rx.Component = None) -> rx.Component():
    return rx.flex(
        #banner(),
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
            height="80px",
            width="100%",
            align_items="center",
            spacing="6",
            padding="7px 20px 7px 20px;",  
        ),
        width="100%",
        z_index="5",
        top="0px",
        position="fixed",
        align_items="center",
        direction="column",
    )
