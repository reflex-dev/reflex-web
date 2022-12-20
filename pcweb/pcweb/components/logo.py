"""The Pynecone logo component."""

import pynecone as pc

from pcweb import styles


def logo(**style_props):
    """Create a Pynecone logo component.

    Args:
        style_props: The style properties to apply to the component.
    """
    return pc.image(
        src=styles.LOGO_URL,
        **style_props,
    )


def navbar_logo(**style_props):
    """Create a Pynecone logo component.

    Args:
        style_props: The style properties to apply to the component.
    """
    return pc.image(
        src=styles.NAVBAR_LOGO,
        **style_props,
    )
