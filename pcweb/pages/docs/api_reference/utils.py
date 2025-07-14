"""Utils API reference page."""

import reflex as rx

from pcweb.templates.docpage import docpage


@docpage("/docs/api-reference/utils/")
def utils():
    """Utils API reference page."""
    with open("docs/api_reference/utils.md", encoding="utf-8") as f:
        content = f.read()
    return rx.markdown(content)
