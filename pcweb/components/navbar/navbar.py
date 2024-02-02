"""UI and logic for the navbar component."""
import reflex as rx
import reflex.components.radix.themes as rdxt
from .buttons.github import github
from .buttons.discord import discord
from .state import NavbarState
from .search import search_bar


def resources_section():
    return rdxt.hovercard_root(
            rdxt.hovercard_trigger(
                rdxt.flex(
                    rdxt.text("Resources", color=rx.color("mauve", 11)),
                    rdxt.icon(tag="chevron_down", color=rx.color("mauve", 11)),
                    align_items="center",
                    gap="1",
                )
            ),
            rdxt.hovercard_content(
                rdxt.grid(
                    rdxt.box("Changelog"),
                    rdxt.box("Roadmap"),
                    rdxt.box("FAQ"),
                    rdxt.box("Components"),
                    rdxt.box("Contribute to Reflex"),
                    rdxt.box("Report a Bug"),
                    columns="2",
                    gap="2",
                    width="auto"
                ),
                border=f"1px solid {rx.color('mauve', 4)}",
                style={"width": 360, "height": 200, "opacity": 0.9},
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
            grow='1',
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
