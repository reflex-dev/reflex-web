"""Typography blocks for doc pages."""

import reflex as rx
import reflex.components.radix.themes as rdxt
from pcweb import styles
from pcweb.styles import colors as c

def definition(title: str, *children) -> rx.Component:
    """Create a definition for a doc page.

    Args:
        title: The title of the definition.
        children: The children to display.

    Returns:
        The styled definition.
    """
    return rdxt.flex(
        rdxt.heading(title, font_size="1em", margin_bottom="0.5em", font_weight="bold"),
        *children,
        padding="1em",
        border=styles.DOC_BORDER,
        border_radius=styles.DOC_BORDER_RADIUS,
        _hover={
            "box_shadow": styles.DOC_SHADOW_LIGHT,
            "border": f"2px solid {c['violet'][200]}",
        },
    )

@rx.memo
def text_comp(text: rx.Var[str]) -> rx.Component:
    return rdxt.text(text, margin_bottom="1em", font_size=styles.TEXT_FONT_SIZE)


@rx.memo
def code_comp(text: rx.Var[str]) -> rx.Component:
    return rdxt.code(text)


def doclink(text: str, href: str, **props) -> rx.Component:
    """Create a styled link for doc pages.

    Args:
        text: The text to display.
        href: The link to go to.
        props: Props to apply to the link.

    Returns:
        The styled link.
    """
    return rdxt.link(text, underline="always", href=href, **props)


def doclink2(text: str, **props) -> rx.Component:
    """Create a styled link for doc pages.

    Args:
        text: The text to display.
        href: The link to go to.
        props: Props to apply to the link.

    Returns:
        The styled link.
    """
    return rdxt.link(text, underline="always", **props)
