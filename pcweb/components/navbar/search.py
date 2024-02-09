"""Search bar component for the navbar."""

import reflex as rx
from pcweb import styles
from .inkeep import inkeep
from .state import NavbarState

from .buttons.style import button_style


icon_style = {
    "stroke_width": "1px",
}

search_badge_style={
    "border_radius":"6px",
    "padding_x":".5em",
    "font_size":"14px",
    "gap":"2",
    "align_items":"center",
    "justify":"center"
}


def search_badge(category, stateful=True):
    icon = ""
    match category:
        case "Component":
            icon =  rx.icon(tag="component", size=16, style = icon_style)
        case "Blog":
            icon = rx.icon(tag="file-text", size=16, style = icon_style)
        case "Learn":
            icon = rx.icon(tag="graduation-cap", size=16, style = icon_style)
        case "API Reference":
            icon = rx.icon(tag="file-text", size=16, style = icon_style)
                    
    return rx.flex(
            icon,
            rx.text(category),
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
            style=search_badge_style
        )


def format_search_results(result):
    return rx.link(
        rx.flex(
            rx.flex(
                rx.match(
                        result["document"]["category"],
                        ("Component", rx.icon(tag="component", size=16, style = icon_style)),
                        ("Blog", rx.icon(tag="file-text", size=16, style = icon_style)),
                        ("Learn", rx.icon(tag="graduation-cap", size=16, style = icon_style)),
                        ("API Reference", rx.icon(tag="file-code", size=16, style = icon_style)),
                        rx.icon(tag="file-text", size=16, style = icon_style)
                ), 
                color=rx.color("mauve", 11),
                width="2em",
                height="2em",
                border_radius="6px",
                bg= rx.color("mauve", 1),
                box_shadow="0px 0px 0px 1px #E8E9EB, 0px 4px 4px -4px rgba(194, 198, 215, 0.40), 0px 1px 4px -1px rgba(135, 144, 181, 0.40);",
                align_items="center",
                justify="center"
            ),
            rx.text(
                result["document"]["heading"],
                font_weight=500,
                font_size="14px",
                color=rx.color('mauve', 12),
            ),
            rx.text(
                result["document"]["description"][:30] + "...",
                no_of_lines=1,
                font_weight=400,
                font_size="12px",
                color=rx.color('mauve', 11),
            ),
            width="100%",
            align_items="center",
            border_radius = "8px",
            _hover={
                "bg": rx.color("mauve", 3),
            },
            gap="2",
            padding=".4em"
        ),
        href=result["document"]["href"],
        style={"text_decoration": "none"},
        width="100%",
    )

 
def ai_button():
    return rx.radix.text_field.slot(
        rx.icon(
            tag="messages-square",
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
            rx.icon(tag="arrow-up-down", size=16, style = icon_style),
            rx.text("Sort"),
            background=rx.color("violet", 9),
            color=rx.color("violet", 1),
            gap="1",
            style=search_badge_style
        ),
        width="100%",
        align_items="center",
        gap="2",
        padding=".4em"
    )  
 
def search_input():
    return rx.flex(
            rx.radix.text_field.root(
                rx.radix.text_field.slot(
                    rx.icon(
                    tag="search",
                    style=styles.NAV_SEARCH_STYLE,
                    height="1em",
                    )
                ),
                rx.radix.text_field.input(
                    placeholder="Search the docs...",
                    on_change=NavbarState.set_search_input,
                    font_weight=400,
                    width= "100%",
                ),
                ai_button(),
                border_bottom="1px solid #F4F3F6",
            ),
            gap="2",
            direction="column",
            padding=".4em"
        )

def search_results():
    return rx.flex(
            rx.vstack(
                rx.cond(
                    NavbarState.ai_chat,
                    rx.flex(
                        search_bar_categories(
                            ["All", "Learn", "Component", "API Reference", "Blog"]
                        ),
                        rx.foreach(
                            NavbarState.search_results,
                            format_search_results,
                        ),
                        width="100%",
                        align_items="start",
                        # overflow_y="auto",
                        direction = "column",
                        gap="3",
                    ),
                    inkeep(
                        width="100%",
                    ),
                ),
                max_height="40em",
                overflow="auto",
                scrollbar_width="none",
                width="100%"
            ),
            width="100%",
        )

def search_bar_desktop() -> rx.Component:
    return rx.dialog.root(
    rx.dialog.trigger(
        rx.flex(
            rx.text(
                "Search",
            ),
            rx.box(
                flex_grow='1',
            ),
            rx.text(
                "/",
                color=rx.color("mauve", 9),
                background=rx.color("mauve", 4),
                padding="0px 3px",
                border_radius="5px",
            ),
            width=["15em", "15em", "15em", "20em", "20em",],
            padding="7px 12px 7px 12px",
            style=button_style
        )
    ),
    rx.dialog.content(
                rx.flex(
                    search_input(),
                    search_results(),
                    direction="column",
                ),
                padding ="1em",
                bg="#FFFFFF",
                max_width="40em",
                top="150px",
                position="fixed"
        ),
)

def search_bar() -> rx.Component:
    return  rx.fragment(
        search_bar_desktop(),
    ) 