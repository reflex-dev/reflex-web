"""UI and logic for the navbar component."""
import reflex as rx
import reflex.components.radix.themes as rdxt
from .buttons.github import github
from .buttons.discord import discord

import reflex as rx
from pcweb import constants, styles
from pcweb.components.logo import navbar_logo
from .state import NavbarState
from .search import search_bar


def feedback_indicator(icon, score):
    return rx.hstack(
        rx.image(src=icon, height="1em"),
        on_click=NavbarState.update_score(score),
        box_shadow=rx.cond(
            NavbarState.page_score == score,
            "0px 4px 10px -2px rgba(3, 3, 11, 0.12), 0px 4px 8px 0px rgba(3, 3, 11, 0.12), 0px 2px 3px 0px rgba(3, 3, 11, 0.10), 0px 0px 0px 2px rgba(149, 128, 247, 0.60), 0px -20px 12px -4px rgba(126, 105, 224, 0.60) inset, 0px 12px 12px -2px rgba(86, 70, 237, 0.12) inset, 0px 0px 0px 1px rgba(32, 17, 126, 0.40) inset;",
            "0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
        ),
        padding_x=".5em",
        height="2em",
        border_radius="8px",
        bg="#FFFFFF",
    )


def feedback_button():
    return rx.vstack(
        rx.hstack(
            rx.text(
                "Was this page useful?",
                style=styles.NAV_TEXT_STYLE,
                font_size="1em",
            ),
            feedback_indicator("/icons/thumbs-down.svg", 1),
            feedback_indicator("/icons/thumbs-up.svg", 2),
            padding_x=".5em",
            padding_y=".25em",
        ),
        transition="all 2s",
        border="2px solid #F4F3F6",
        border_radius="8px",
        padding="0.2em",
    )

def navbar(sidebar: rx.Component = None) -> rx.Component():
    return rdxt.flex(
        rx.image(
            src="/logo/light.svg",
        ),
        rdxt.flex(
            rdxt.text("Docs", color=rx.color("mauve", 11)),
            rdxt.text("Blog",color=rx.color("mauve", 11)),
            rdxt.text("Gallery", color=rx.color("mauve", 11)),
            rdxt.text("Resources", color=rx.color("mauve", 11)),
            gap="5",
        ),
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
        padding= "7px 12px 7px 8px;",
    )
