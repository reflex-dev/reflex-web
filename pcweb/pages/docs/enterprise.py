"""The enterprise documentation pages."""

import reflex as rx
from pcweb.templates.docpage import docpage


@docpage(
    set_path="/docs/enterprise/overview",
    t="Overview | Enterprise",
)
def overview():
    """The enterprise overview page."""
    pass