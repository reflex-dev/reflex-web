"""Search bar component for the navbar."""

import reflex as rx
from pcweb import styles
from .inkeep import inkeep
from .state import NavbarState

from .buttons.style import button_style


icon_style = {
    "stroke_width": "1px",
}

search_badge_style = {
    "border_radius": "6px",
    "padding_x": ".5em",
    "font_size": "14px",
    "align_items": "center",
    "justify": "center",
}


def search_badge(category, stateful=True):
    icon = ""
    match category:
        case "Component":
            icon = rx.icon("component", size=16, style=icon_style)
        case "Blog":
            icon = rx.icon("file-text", size=16, style=icon_style)
        case "Learn":
            icon = rx.icon("graduation-cap", size=16, style=icon_style)
        case "API Reference":
            icon = rx.icon("file-text", size=16, style=icon_style)

    return rx.flex(
        icon,
        rx.text.span(category),
        on_click=NavbarState.update_category(category),
        background=rx.cond(
            NavbarState.current_category == category,
            rx.color("violet", 9),
            rx.color("mauve", 1),
        ),
        color=rx.cond(
            NavbarState.current_category == category,
            rx.color("violet", 1),
            rx.color("mauve", 11),
        ),
        box_shadow="0px 0px 0px 1px #E8E9EB, 0px 4px 4px -4px rgba(194, 198, 215, 0.40), 0px 1px 4px -1px rgba(135, 144, 181, 0.40);",
        style=search_badge_style,
        spacing="2",
        flex_shrink=0,
    )


def format_search_results(result):
    return rx.link(
        rx.flex(
            rx.flex(
                rx.match(
                    result["document"]["category"],
                    ("Component", rx.icon("component", size=16, style=icon_style)),
                    ("Blog", rx.icon("file-text", size=16, style=icon_style)),
                    ("Learn", rx.icon("graduation-cap", size=16, style=icon_style)),
                    ("API Reference", rx.icon("file-code", size=16, style=icon_style)),
                    rx.icon("file-text", size=16, style=icon_style),
                ),
                color=rx.color("mauve", 11),
                width="2em",
                height="2em",
                border_radius="6px",
                bg=rx.color("mauve", 1),
                box_shadow="0px 0px 0px 1px #E8E9EB, 0px 4px 4px -4px rgba(194, 198, 215, 0.40), 0px 1px 4px -1px rgba(135, 144, 181, 0.40);",
                align_items="center",
                justify="center",
                ga="2",
            ),
            rx.text(
                result["document"]["heading"],
                font_weight=500,
                font_size="14px",
                color=rx.color("mauve", 12),
            ),
            rx.text(
                result["document"]["description"][:30] + "...",
                no_of_lines=1,
                font_weight=400,
                font_size="12px",
                color=rx.color("mauve", 11),
            ),
            width="100%",
            align_items="center",
            border_radius="8px",
            _hover={
                "bg": rx.color("mauve", 3),
            },
            spacing="2",
            padding=".4em",
        ),
        href=result["document"]["href"],
        style={"text_decoration": "none"},
        width="100%",
    )


def ai_button():
    return rx.radix.text_field.slot(
        rx.icon(
            "messages-square",
            on_click=NavbarState.toggle_ai_chat,
            _hover={
                "cursor": "pointer",
                "color": styles.ACCENT_COLOR,
            },
        )
    )


def search_bar_categories(categories):
    return rx.flex(
        *[search_badge(category) for category in categories],
        rx.box(flex_grow="1"),
        rx.flex(
            rx.icon("arrow-up-down", size=16, style=icon_style),
            rx.text("Sort"),
            background=rx.color("violet", 9),
            color=rx.color("violet", 1),
            spacing="2",
            style=search_badge_style,
        ),
        width="100%",
        align_items="center",
        spacing="2",
        padding=".4em"
    )


def search_bar_desktop() -> rx.Component:
    return inkeep(width="100%", border_radius="8px")


def search_bar() -> rx.Component:
    return rx.fragment(
        search_bar_desktop(),
    )
