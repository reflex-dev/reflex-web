"""Search bar component for the navbar."""

import reflex as rx
from pcweb import constants, styles
from .inkeep import inkeep
from .state import NavbarState

import reflex.components.radix.themes as rdxt
from .buttons.style import button_style


def search_badge(category, stateful=True):
    if stateful:
        return rx.badge(
            category,
            border_radius="8px",
            padding_x=".5em",
            on_click=NavbarState.update_category(category),
            color=rx.cond(
                NavbarState.current_category == category,
                styles.c["violet"][500],
                styles.c["gray"][500],
            ),
            bg=rx.cond(
                NavbarState.current_category == category,
                styles.c["violet"][50],
                styles.c["gray"][50],
            ),
            _hover={
                "color": styles.c["violet"][500],
            },
            transition="all 0.2s ease-in-out",
        )
    else:
        return rx.badge(
            category,
            border_radius="8px",
            color=styles.c["violet"][500],
            bg=styles.c["violet"][50],
            padding_x=".5em",
        )


def format_search_results(result):
    return rx.link(
        rx.vstack(
            rx.hstack(
                rx.text(
                    result["document"]["heading"],
                    font_weight=600,
                    color=styles.c["indigo"][700],
                ),
                rx.spacer(),
                search_badge(result["document"]["category"], stateful=False),
                width="100%",
            ),
            rx.text(
                result["document"]["description"],
                no_of_lines=1,
                font_weight=400,
                color=styles.c["indigo"][500],
            ),
            width="100%",
            _hover={
                "bg": "#F5EFFE",
            },
            bg="#f4f3f4",
            border_radius="8px",
            padding_x=".5em",
            padding_y=".25em",
            spacing="0.25em",
        ),
        on_click=NavbarState.close_search,
        href=result["document"]["href"],
        style={"text_decoration": "none"},
        width="100%",
    )


def ai_button():
    return rx.center(
        rx.icon(
            tag="chat",
            color=rx.cond(
                NavbarState.ai_chat,
                "#342E5C",
                "#5646ED",
            ),
        ),
        on_click=NavbarState.toggle_ai_chat,
        _hover={
            "cursor": "pointer",
            "color": styles.ACCENT_COLOR,
        },
        height="1em",
        transition="all 0.2s ease-in-out",
    )


def search_bar_categories(categories):
    return rx.hstack(
        *[search_badge(category) for category in categories],
        padding_bottom=".25em",
    )


def search_modal():
    return rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.modal_header(
                    # add in filter tabs here categories
                    search_bar_categories(
                        ["All", "Learn", "Component", "API Reference", "Blog"]
                    ),
                    rx.hstack(
                        rx.icon(
                            tag="search2",
                            style=styles.NAV_SEARCH_STYLE,
                            height="1em",
                        ),
                        rx.input(
                            placeholder="Search the docs...",
                            on_change=NavbarState.set_search_input,
                            focus_border_color="transparent",
                            border_color="transparent",
                            font_weight=400,
                            _placeholder={"color": "#342E5C"},
                            _hover={"border_color": "transparent"},
                        ),
                        ai_button(),
                        border_bottom="1px solid #F4F3F6",
                    ),
                ),
                rx.modal_body(
                    rx.vstack(
                        rx.cond(
                            NavbarState.ai_chat,
                            rx.vstack(
                                rx.foreach(
                                    NavbarState.search_results,
                                    format_search_results,
                                ),
                                spacing="1em",
                                width="100%",
                                max_height="30em",
                                align_items="start",
                                overflow_y="auto",
                                padding_top="0em",
                            ),
                            inkeep(
                                width="100%",
                            ),
                        ),
                        max_height="40em",
                        overflow="auto",
                        scrollbar_width="none",
                    ),
                    width="100%",
                ),
                bg="#FFFFFF",
                max_width="50em",
            )
        ),
        is_open=NavbarState.search_modal,
        on_close=NavbarState.close_search,
        size="xl",
        padding_top="1em",
        padding_x="1em",
    )

def search_bar_desktop() -> rx.Component:
    return rdxt.dialog_root(
    rdxt.dialog_trigger(
        rdxt.flex(
            rdxt.text(
                "Search",
            ),
            rdxt.box(
                grow='1',
            ),
            rdxt.text(
                "⌘+K",
                color=rx.color("mauve", 9),
                background=rx.color("mauve", 4),
                border_radius="5px",
            ),
            search_modal(),
            on_click=NavbarState.open_search,
            width=["15em", "15em", "15em", "20em", "20em",],
            padding="7px 12px 7px 12px",
            style=button_style
        )
    ),
    rdxt.dialog_content(
        rdxt.flex(
            rdxt.icon(tag="magnifying_glass"),
            rdxt.text(
                "search docs",
            ),
            align_items= "center;",
            gap="2",
            padding_bottom="5px",
            border_bottom= f"1px solid {rx.color('mauve', 4)};",
        ),
        border_radius= "10px",
        box_shadow= "none"
    ),
)

def search_bar_mobile():
    return rdxt.flex(
        rdxt.icon(
            tag="magnifying_glass",
            style=styles.NAV_SEARCH_STYLE,
            color=rx.color("mauve", 9),
            height="20px",
            width="20px",
        ),
        on_click=NavbarState.open_search,
        padding="7px",
        style=button_style,
        border_radius="8px",
    )


def search_bar() -> rx.Component:
    return  rx.fragment(
        search_bar_desktop(),
    )