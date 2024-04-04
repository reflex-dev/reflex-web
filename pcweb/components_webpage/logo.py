"""The Reflex logo component."""

import reflex as rx
from pcweb import styles


def logo(**style_props):
    """Create a Reflex logo component.

    Args:
        style_props: The style properties to apply to the component.
    """
    return rx.image(
        src=styles.LOGO_URL,
        alt = "The Reflex logo.",
        **style_props,
    )


def navbar_logo(**style_props):
    """Create a Reflex logo component.

    Args:
        style_props: The style properties to apply to the component.
    """
    return rx.link(
        rx.image(
            src=styles.NAVBAR_LOGO,
            **style_props,
        ),
        href="/",
    )
