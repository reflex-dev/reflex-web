"""Template for documentation pages."""

import reflex as rx

from pcweb import styles
from pcweb.styles import font_weights as fw
from pcweb.styles import fonts
from pcweb.styles.colors import c_color

icon_margins = {
    "h1": "10px",
    "h2": "5px",
    "h3": "2px",
    "h4": "0px",
}


def h_comp_common(
    text: rx.Var[str],
    heading: str,
    font_size: list[str] | str = "",
    font_weight: str = "",
    scroll_margin: str = "",
    margin_top: str = "",
    margin_bottom: str = "",
    convert_to_str: bool = False,
    style: dict = {},
) -> rx.Component:
    if convert_to_str:
        id_ = text.to(list[str])[0].lower().split().join("-")
    else:
        id_ = text.lower().split().join("-")
    href = rx.State.router.page.full_path + "#" + id_

    return rx.box(
        rx.link(
            rx.hstack(
                rx.heading(
                    text,
                    id=id_,
                    as_=heading,
                    font_size=font_size,
                    font_weight=font_weight,
                    scroll_margin=scroll_margin,
                    style=style,
                ),
                rx.icon(
                    tag="link",
                    margin_top=icon_margins.get(heading, "0px"),
                    size=18,
                    visibility="hidden",
                    transition="visibility 0.075s ease-out",
                    color=c_color("violet", 9),
                ),
                align_items="center",
                gap="16px",
            ),
            style={
                ":hover": {
                    "color": c_color("violet", 9),
                },
                ":hover svg": {
                    "visibility": "visible",
                },
                "transition": "color 0.075s ease-out",
            },
            _hover={
                "color": c_color("violet", 9),
            },
            color=c_color("slate", 12),
            cursor="pointer",
            underline="none",
            href=href,
            on_click=lambda: rx.set_clipboard(href),
            margin_bottom="0.5em",
        ),
        _hover={
            "color": c_color("violet", 9),
        },
        margin_top=margin_top,
        margin_bottom=margin_bottom,
        width="100%",
    )


@rx.memo
def h1_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h1",
        style={
            "font-size": ["32px", "48px"],
            "font-style": "normal",
            "font-weight": "600",
            "line-height": ["48px", "56px"],
            "letter-spacing": "-2.4px",
        },
        margin_bottom="24px",
        scroll_margin="4em",
    )


@rx.memo
def h1_comp_xd(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h1",
        style=fonts.xx_large,
        margin_bottom="24px",
        scroll_margin="4em",
        convert_to_str=True,
    )


@rx.memo
def h2_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h2",
        style=fonts.x_large,
        margin_bottom="24px",
        margin_top=["24px", "40px"],
        scroll_margin="5em",
    )


@rx.memo
def h2_comp_xd(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h2",
        style=fonts.x_large,
        margin_bottom="24px",
        margin_top="0px",
        scroll_margin="5em",
        convert_to_str=True,
    )


@rx.memo
def h3_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h3",
        font_size=styles.H4_FONT_SIZE,
        font_weight=fw["subheading"],
        margin_top="1em",
        margin_bottom="0em",
        scroll_margin="5em",
    )


@rx.memo
def h3_comp_xd(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h3",
        style=fonts.large,
        margin_bottom="24px",
        margin_top="24px",
        scroll_margin="5em",
        convert_to_str=True,
    )


@rx.memo
def h4_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h4",
        font_size=styles.H4_FONT_SIZE,
        font_weight=fw["subheading"],
        margin_top="1em",
        scroll_margin="6em",
    )


@rx.memo
def h4_comp_xd(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h4",
        style=fonts.medium,
        margin_bottom="24px",
        scroll_margin="6em",
        convert_to_str=True,
    )
