"""Typography blocks for doc pages."""

import reflex as rx


def definition(title: str, *children) -> rx.Component:
    """Create a definition for a doc page.

    Args:
        title: The title of the definition.
        children: The children to display.

    Returns:
        The styled definition.
    """
    return rx.vstack(
        rx.heading(title, font_size="1em", font_weight="bold", color=rx.color("mauve", 12)),
        *children,
        color=rx.color("mauve", 10),
        padding="1em",
        border=f"1px solid {rx.color('mauve', 4)}",
        background_color=rx.color("mauve", 2),
        border_radius="8px",
        _hover={
            "border": f"1px solid {rx.color('mauve', 5)}",
            "background_color": rx.color("mauve", 3),
        },
        align_items="start"
)


@rx.memo
def text_comp(text: rx.Var[str]) -> rx.Component:
    return rx.text(text, size="3", line_height="1.7", margin_bottom="1em")


@rx.memo
def code_comp(text: rx.Var[str]) -> rx.Component:
    return rx.code(text)


def doclink(text: str, href: str, **props) -> rx.Component:
    """Create a styled link for doc pages.

    Args:
        text: The text to display.
        href: The link to go to.
        props: Props to apply to the link.

    Returns:
        The styled link.
    """
    return rx.link(text, underline="always", href=href, **props)


def doclink2(text: str, **props) -> rx.Component:
    """Create a styled link for doc pages.

    Args:
        text: The text to display.
        href: The link to go to.
        props: Props to apply to the link.

    Returns:
        The styled link.
    """
    return rx.link(text, underline="always", **props)
