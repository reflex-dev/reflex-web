"""UI and logic for the navbar component."""
import reflex as rx
import reflex.components.radix.themes as rdxt
from .buttons.github import github
from .buttons.discord import discord
from .state import NavbarState
from .search import search_bar


def resource_header(text):
    return rdxt.text(text, color=rx.color("mauve", 12), padding_bottom="10px", font_weight="600")

def resources_item(text, url, icon):
    return rdxt.link(
            rdxt.flex(
                rx.lucide.icon(icon, size=20, color=rx.color("mauve", 9)),
                rdxt.text(text, color=rx.color("mauve", 9)),
                wrap="nowrap",
                gap="2",
            ),
            href=url,
        )


def resources_section():
    return rdxt.hovercard_root(
            rdxt.hovercard_trigger(
                rdxt.flex(
                    rdxt.text("Resources", color=rx.color("mauve", 11)),
                    rdxt.icon(tag="chevron_down", color=rx.color("mauve", 11)),
                    align_items="center",
                    gap="2",
                )
            ),
            rdxt.hovercard_content(
                rdxt.flex(
                        rdxt.flex(
                            resource_header("Open Source"),
                            resources_item("Github", "https://github.com/reflex-dev", "github"),
                            resources_item("Github Discussions","https://github.com/orgs/reflex-dev/discussions", "message-circle-question"),
                            resources_item("Contribute to Reflex", "https://github.com/reflex-dev/reflex/blob/main/CONTRIBUTING.md", "file-json-2"),
                            resources_item("Changelog", "/changelog", "list-checks"),
                            direction="column",
                            align_items = "start",
                            padding_left="20px",
                            padding_top="20px",
                            padding_bottom="20px",
                            gap="2",
                        ),
                        rdxt.flex(
                            resource_header("Resources"),
                            resources_item("Component Library", "/docs/library", "layout-panel-left"),
                            resources_item("Roadmap", "https://reflex-dev.notion.site/d1b60926ced14914bdbb42547ac84e50?v=723e0afc57294e40961d177aa691ee37", "map-pinned"),
                            resources_item("Blog", "/blog", "text"),
                            resources_item("FAQ", "/faq", "list-todo"),
                            direction="column",
                            align_items = "start",
                            padding_top="20px",
                            padding_bottom="20px",
                            gap="2",
                        ),
                        rdxt.flex(
                            resource_header("Hosting"),
                            resources_item("Deployment", "/docs/hosting/deploy-quick-start/", "globe"),
                            resources_item("Self-Hosting", "/docs/hosting/self-hosting/", "server"),
                            direction="column",
                            background_color = rx.color("mauve", 3),
                            border_left = f"1px solid {rx.color('mauve', 4)}",
                            align_items = "start",
                            height="250",
                            padding_top="20px",
                            padding_left="20px",
                            padding_bottom="20px",
                            padding_right="20px",
                            gap="2",
                        ),
                        gap="5",
                ),
                border=f"1px solid {rx.color('mauve', 4)}",
                background_color = rx.color("mauve", 2),
                width = "1000",
                height = "250",
                padding="0"
            ),
        )

def navigation_section():
    return rx.desktop_only(
        rdxt.flex(
            rdxt.text("Docs", color=rx.color("mauve", 11)),
            rdxt.text("Blog",color=rx.color("mauve", 11)),
            rdxt.text("Gallery", color=rx.color("mauve", 11)),
            resources_section(),
            gap="5",
        )
    )

def navbar(sidebar: rx.Component = None) -> rx.Component():
    return rdxt.flex(
        rx.image(
            src="/logos/light/reflex.svg",
            height="20px",
        ),
        navigation_section(),
        rdxt.box(
                flex_grow='1',
        ),
        rdxt.flex(
            search_bar(),
            github(),
            rdxt.separator(size="2", color='mauve', orientation="vertical"), 
            discord(),
            gap="3",
            align_items="center",
        ),
        background = rx.color("mauve", 1),
        border_bottom= f"1px solid {rx.color('mauve', 4)};",
        height="80px",
        position="fixed",
        width="100%",
        top="0px",
        z_index="5",
        align_items= "center;",
        gap="6",
        padding= "7px 20px 7px 20px;",
    )
