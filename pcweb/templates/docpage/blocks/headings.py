"""Template for documentation pages."""

import reflex as rx
from pcweb import styles
from pcweb.styles import font_weights as fw

def h_comp_common(
    text: rx.Var[str],
    heading: str,
    font_size: list[str] | str,
    font_weight: str,
    margin_top: str,
    scroll_margin: str,
) -> rx.Component:
    id_ = text.to(list[str])[0].lower().split().join("-")
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
                ),
                rx.icon(
                    tag="link_2",
                    color="#696287",
                    _hover={
                        "color": styles.ACCENT_COLOR,
                    },
                ),
                align_items="center",
            ),
            _hover={
                "cursor": "pointer",
                "textDecoration": "none",
            },
            href=href,
            on_click=lambda: rx.set_clipboard(href),
            margin_bottom="0.5em",
        ),
        rx.flex(
            rx.separator(size="4"),
            margin_top=".5em",
            margin_bottom="1em",
            width="100%"
        ),
        margin_top=margin_top,
        margin_bottom=margin_top,
        width="100%",
    )


@rx.memo
def h1_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h1",
        font_size=styles.H1_FONT_SIZE,
        font_weight=fw["heading"],
        margin_top="0",
        scroll_margin="4em",
    )


@rx.memo
def h2_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h2",
        font_size=styles.H3_FONT_SIZE,
        font_weight=fw["subheading"],
        margin_top="1.5em",
        scroll_margin="5em",
    )


@rx.memo
def h3_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h3",
        font_size=styles.H4_FONT_SIZE,
        font_weight=fw["subheading"],
        margin_top="1.5em",
        scroll_margin="5em",
    )


@rx.memo
def h4_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h4",
        font_size=styles.H4_FONT_SIZE,
        font_weight=fw["subheading"],
        margin_top="1.5em",
        scroll_margin="6em",
    )
