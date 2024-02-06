"""UI and logic for the navbar component."""
import reflex as rx
import reflex.components.radix.themes as rdxt
from .buttons.github import github
from .buttons.discord import discord
from .state import NavbarState
from .search import search_bar


def resources_item(text, url, icon):
    return rdxt.flex(
        rx.lucide.icon(icon, size=20, color=rx.color("mauve", 9)),
        rdxt.link(
            rdxt.text(text, color=rx.color("mauve", 9)),
            href=url,
        ),
        gap="2",
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
                            rdxt.text("Open Source", color=rx.color("mauve", 12)),
                            resources_item("Github", "", "github"),
                            resources_item("Github Discussions","", "message-circle-question"),
                            resources_item("Contribute to Reflex", "", "file-json-2"),
                            resources_item("Changelog", "", "list-checks"),
                            direction="column",
                            align_items = "start",
                            padding_left="20px",
                            padding_top="20px",
                            padding_bottom="20px",
                            gap="2",
                        ),
                        rdxt.flex(
                            rdxt.text("Resources", color=rx.color("mauve", 12)),
                            resources_item("Component Library", "", "layout-panel-left"),
                            resources_item("Roadmap", "", "map-pinned"),
                            resources_item("Blog", "", "text"),
                            resources_item("FAQ", "", "list-todo"),
                            direction="column",
                            align_items = "start",
                            padding_top="20px",
                            padding_bottom="20px",
                            gap="2",
                        ),
                        rdxt.flex(
                            rdxt.text("Hosting", color=rx.color("mauve", 11)),
                            resources_item("Deployment", "", "globe"),
                            resources_item("Self-Hosting", "", "server"),
                            direction="column",
                            background_color = rx.color("mauve", 4),
                            align_items = "start",
                            height="100%",
                            padding_top="20px",
                            padding_bottom="20px",
                            padding_right="20px",
                            gap="2",
                        ),
                        gap="3",
                        height="100%",
                ),
                border=f"1px solid {rx.color('mauve', 4)}",
                background_color = rx.color("mauve", 2),
                width = "500",
                height = "200",
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
