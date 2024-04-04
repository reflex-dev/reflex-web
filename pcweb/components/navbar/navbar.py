"""UI and logic for the navbar component."""
import reflex as rx
from .buttons.github import github
from .buttons.discord import discord
from .buttons.sidebar import sidebar_button
from .search import search_bar
from .buttons.product_hunt import product_hunt
from .state import NavbarState

def resource_header(text):
    return rx.text(
        text, color=rx.color_mode_cond(rx.color("mauve", 12), rx.color("mauve", 10)), padding_bottom="10px", font_weight="600"
    )


def resources_item(text, url, icon):
    return rx.link(
        rx.flex(
            rx.icon(icon, size=20, color=rx.color("mauve", 9)),
            rx.text(text, color=rx.color("mauve", 9)),
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
                            "color": "#FFFFFF",
                            "text_decoration": "underline",
                            "_hover": {"color": "#AD9BF8"},
                        },
                        is_external=True,
                    ),
                    ". 🎉",
                    color="#FFFFFF",
                    font_weight=600,
                    text_align="center",
                    width="100%",
                ),
                rx.icon(
                    tag="x",
                    z_index=1000,
                    style={
                        "color": "#FFFFFF",
                        "text_decoration": "underline",
                        "_hover": {"color": "#AD9BF8"},
                    },
                    on_click=NavbarState.toggle_banner,
                ),
                width="100%",
                align_items="center",
            ),
            background_color="#110F1F",
            padding_y=["0.8em", "0.8em", "0.5em"],
            width="100%",
        ),
    )



def resources_section():
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.flex(
                rx.text("Resources", color=rx.color_mode_cond(rx.color("mauve", 11), rx.color("mauve", 10))),
                rx.icon(tag="chevron_down", color=rx.color("mauve", 11), size=18),
                align_items="center",
                _hover={
                    "cursor": "pointer",
                },
                spacing="2",
            )
        ),
        rx.hover_card.content(
            rx.flex(
                rx.flex(
                    resource_header("Open Source"),
                    resources_item("Github", "https://github.com/reflex-dev", "github"),
                    resources_item(
                        "Github Discussions",
                        "https://github.com/orgs/reflex-dev/discussions",
                        "message-circle-question",
                    ),
                    resources_item(
                        "Contribute to Reflex",
                        "https://github.com/reflex-dev/reflex/blob/main/CONTRIBUTING.md",
                        "file-json-2",
                    ),
                    resources_item("Changelog", "/changelog", "list-checks"),
                    direction="column",
                    align_items="start",
                    padding_left="20px",
                    padding_top="20px",
                    padding_bottom="20px",
                    spacing="2",
                ),
                rx.flex(
                    resource_header("Resources"),
                    resources_item(
                        "Component Library", "/docs/library", "layout-panel-left"
                    ),
                    resources_item(
                        "Roadmap",
                        "https://reflex-dev.notion.site/d1b60926ced14914bdbb42547ac84e50?v=723e0afc57294e40961d177aa691ee37",
                        "map-pinned",
                    ),
                    resources_item("Blog", "/blog", "text"),
                    resources_item("FAQ", "/faq", "list-todo"),
                    direction="column",
                    align_items="start",
                    padding_top="20px",
                    padding_bottom="20px",
                    spacing="2",
                ),
                rx.flex(
                    resource_header("Hosting"),
                    resources_item(
                        "Deployment", "/docs/hosting/deploy-quick-start/", "globe"
                    ),
                    resources_item(
                        "Self-Hosting", "/docs/hosting/self-hosting/", "server"
                    ),
                    direction="column",
                    background_color=rx.color("mauve", 3),
                    align_items="start",
                    height="200px",
                    padding_top="20px",
                    padding_left="20px",
                    padding_bottom="20px",
                    padding_right="20px",
                    spacing="2",
                ),
                spacing="6",
            ),
            border=f"1px solid {rx.color('mauve', 4)}",
            background=rx.color("mauve", 1),
            max_width="1000px",
            height="200px",
            padding="0",
        ),
    )


def navigation_section():
    return rx.box(
        rx.flex(
            rx.link(
                rx.text("Docs", color=rx.color_mode_cond(rx.color("mauve", 11), rx.color("mauve", 10))),
                href="/docs/getting-started/introduction/",
            ),
            rx.link(rx.text("Blog", color=rx.color_mode_cond(rx.color("mauve", 11), rx.color("mauve", 10))), href="/blog"),
            rx.link(
                rx.text("Gallery", color=rx.color_mode_cond(rx.color("mauve", 11), rx.color("mauve", 10))), href="/docs/gallery"
                ),
            resources_section(),
            spacing="5",
        ),
        display=["none", "none", "none", "none", "flex", "flex"],
    )

def navbar(sidebar: rx.Component = None) -> rx.Component():
    return rx.flex(
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
            rx.divider(size="2", color=rx.color("mauve"), orientation="vertical"),
            rx.box(
                discord(),
                display=["none", "none", "none", "none", "flex", "flex"],
            ),
            navigation_section(),
            rx.box(
                flex_grow="1",
            ),
            rx.flex(
                search_bar(),
                github(),
                #product_hunt(),
                rx.divider(size="2", color="mauve", orientation="vertical"),
                rx.box(
                    discord(),
                    display=["none", "none", "none", "none", "flex", "flex"],
                ),
                rx.box(
                    sidebar_button(sidebar),
                    display=["flex", "flex", "flex", "flex", "none", "none"],
                ),
                spacing="3",
                align_items="center",
            ),
            background="rgba(255,255,255, 0.8)",
            backdrop_filter="blur(10px)",
            border_bottom=f"1px solid {rx.color('mauve', 4)};",
            width="100%",
            align_items="center",
            spacing="6",
            padding="7px 20px 7px 20px;",
        ),
        background_color=rx.color("mauve", 1),
        height="80px",
        position="fixed",
        width="100%",
        z_index="5",
        top="0px",
        position="fixed",
        align_items="center",
        spacing="6",
        padding="7px 20px 7px 20px;",  
    )
