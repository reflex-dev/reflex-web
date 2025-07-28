"""Plugins API reference page."""

import reflex as rx

from pcweb.templates.docpage import docpage


@docpage("/docs/api-reference/plugins/")
def plugins():
    """Plugins API reference page."""
    with open("docs/api-reference/plugins.md", encoding="utf-8") as f:
        content = f.read()
    return rx.markdown(content)
