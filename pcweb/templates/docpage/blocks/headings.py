"""Template for documentation pages."""

import reflex as rx
from pcweb import styles
from pcweb.styles import font_weights as fw


def h_comp_common(
    text: rx.Var[str],
    heading: str,
    font_size: list[str] | str,
    font_weight: str,
    scroll_margin: str,
    margin_top: str,
    margin_bottom: str = "",
    convert_to_str: bool = False,
) -> rx.Component:
    if convert_to_str:
        id_ = text.to(list[str])[0].lower().split().join("-")
    else:
        id_ = text.lower().split().join("-")
    href = rx.State.router.page.full_path + "#" + id_

    return rx.box(
        rx.link(
            rx.flex(
                rx.heading(
                    text,
                    id=id_,
                    as_=heading,
                    color=rx.color("mauve", 12),
                    font_size=font_size,
                    font_weight=font_weight,
                    scroll_margin=scroll_margin,
                    line_height="1.2",
                ),
                rx.icon(
                    tag="link_2",
                    color=rx.color("mauve", 11),
                    _hover={
                        "color": rx.color("violet", 9),
                        "transition": "transform 0.25s ease;",
                        "transform": "rotate(180deg);",
                    },
                ),
                align_items="center",
                spacing="3",
            ),
            _hover={
                "cursor": "pointer",
                "textDecoration": "none",
            },
            href=href,
            on_click=lambda: rx.set_clipboard(href),
            margin_bottom="0.5em",
        ),
        border_top=f"1px solid {rx.color('mauve', 4)}" if heading == "h2" else None,
        padding_top=margin_top, 
        margin_top=margin_top,
        margin_bottom=margin_bottom if margin_bottom else margin_top,
        width="100%",
    )


@rx.memo
def h1_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h1",
        font_size=styles.H1_FONT_SIZE,
        font_weight=fw["heading"],
        margin_top="1.5em",
        scroll_margin="4em",
    )


@rx.memo
def h1_comp_xd(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h1",
        font_size=styles.H1_FONT_SIZE,
        font_weight=fw["heading"],
        margin_top="1.5em",
        scroll_margin="4em",
        convert_to_str=True,
    )


@rx.memo
def h2_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h2",
        font_size=styles.H2_FONT_SIZE,
        font_weight=fw["subheading"],
        margin_top="1.5em",
        margin_bottom="1em",
        scroll_margin="5em",
    )


@rx.memo
def h2_comp_xd(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h2",
        font_size=styles.H2_FONT_SIZE,
        font_weight=fw["subheading"],
        margin_top="1.5em",
        margin_bottom="1em",
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
        font_size=styles.H4_FONT_SIZE,
        font_weight=fw["subheading"],
        margin_top="1em",
        margin_bottom=".5em",
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
        font_size=styles.H4_FONT_SIZE,
        font_weight=fw["subheading"],
        margin_top="1em",
        scroll_margin="6em",
        convert_to_str=True,
    )
