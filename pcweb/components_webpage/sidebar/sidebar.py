"""Logic for the sidebar component."""

from __future__ import annotations

import reflex as rx

from pcweb import constants
from pcweb.pages.docs import getting_started, hosting
from pcweb.pages.faq import faq
from pcweb.pages.docs.library import library
from pcweb.pages.blog import blg
from pcweb.pages.changelog import changelog
from pcweb.pages.docs.gallery import gallery


def sidebar(url=None, width: str = "100%") -> rx.Component:
    """Render the sidebar."""

    section_style = {
        "color": "#ffffff",
        "font-weight": "400",
    }

    return rx.vstack(
        rx.link("Blog", href=blg.path, style=section_style),
        rx.link("Gallery", href=gallery.path, style=section_style),
        rx.link("Docs", href=getting_started.introduction.path, style=section_style),
        rx.link("Component Library", href=library.path, style=section_style),
        rx.link("Changelog", href=changelog.path, style=section_style),
        rx.link(
            "Roadmap",
            href=constants.ROADMAP_URL,
            style=section_style,
        ),
        rx.link(
            "Deployment", href=hosting.deploy_quick_start.path, style=section_style
        ),
        rx.link("Self-Hosting", href=hosting.self_hosting.path, style=section_style),
        rx.link(
            "Contribute",
            href=constants.CONTRIBUTING_URL,
            style=section_style,
        ),
        rx.link("FAQ", href=faq.path, style=section_style),
        spacing="5",
        width="100%",
        height="100%",
        justify="end",
    )


sb = sidebar(width="100%")
