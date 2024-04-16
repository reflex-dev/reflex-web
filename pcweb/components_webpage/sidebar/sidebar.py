"""Logic for the sidebar component."""

from __future__ import annotations

import reflex as rx

from pcweb.pages.docs import getting_started, hosting
from pcweb.pages.faq import faq
from pcweb.pages.docs.library import library
from pcweb.pages.blog import blg
from pcweb.pages.changelog import changelog
from pcweb.pages.docs.gallery import gallery


def resource_header(text):
    return rx.text(
        text,
        color=rx.color_mode_cond(rx.color("mauve", 12), rx.color("mauve", 10)),
        padding_bottom="10px",
        font_weight="600",
    )


def resources_item(text, url, icon):
    return rx.link(
        rx.flex(
            rx.icon(icon, size=20, color=rx.color("mauve", 9)),
            rx.text(text, color=rx.color("mauve", 9)),
            wrap="nowrap",
            spacing="2",
        ),
        href=url,
    )


def resources_section(style):
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.flex(
                rx.text("Resources", style=style),
                rx.icon(tag="chevron_down", size=18, style=style),
                align_items="center",
                _hover={
                    "cursor": "pointer",
                },
                spacing="2",
            )
        ),
        rx.hover_card.content(
            rx.flex(
                rx.flex(
                    resource_header("Open Source"),
                    resources_item("Github", "https://github.com/reflex-dev", "github"),
                    resources_item(
                        "Github Discussions",
                        "https://github.com/orgs/reflex-dev/discussions",
                        "message-circle-question",
                    ),
                    resources_item(
                        "Contribute to Reflex",
                        "https://github.com/reflex-dev/reflex/blob/main/CONTRIBUTING.md",
                        "file-json-2",
                    ),
                    resources_item("Changelog", changelog.path, "list-checks"),
                    direction="column",
                    align_items="start",
                    padding_left="20px",
                    padding_y="20px",
                    spacing="2",
                ),
                rx.flex(
                    resource_header("Resources"),
                    resources_item(
                        "Component Library", library.path, "layout-panel-left"
                    ),
                    resources_item(
                        "Roadmap",
                        "https://reflex-dev.notion.site/d1b60926ced14914bdbb42547ac84e50?v=723e0afc57294e40961d177aa691ee37",
                        "map-pinned",
                    ),
                    resources_item("Blog", blg.path, "text"),
                    resources_item("FAQ", faq.path, "list-todo"),
                    direction="column",
                    align_items="start",
                    padding_top="20px",
                    padding_bottom="20px",
                    spacing="2",
                ),
                rx.flex(
                    resource_header("Hosting"),
                    resources_item(
                        "Deployment", hosting.deploy_quick_start.path, "globe"
                    ),
                    resources_item("Self-Hosting", hosting.self_hosting.path, "server"),
                    direction="column",
                    background="linear-gradient(218deg, #1D1B23 -35.66%, #131217 100.84%);",
                    border_left="1px solid rgba(29, 29, 32, 0.08);",
                    align_items="start",
                    height="210px",
                    padding_top="20px",
                    padding_left="20px",
                    padding_bottom="20px",
                    padding_right="20px",
                    spacing="2",
                ),
                spacing="6",
            ),
            border="1px solid rgba(29, 29, 32, 0.08);",
            background="linear-gradient(180deg, rgba(29, 27, 33, 0.95) 0%, rgba(20, 19, 24, 0.95) 100%);",
            box_shadow="0px 24px 54px -17px rgba(13, 12, 16, 0.30), 0px 0px 0px 1px rgba(93, 93, 107, 0.29), 0px 0px 64px 5px rgba(53, 51, 60, 0.30) inset;",
            max_width="1000px",
            height="210px",
            padding="0",
            overflow="hidden",
        ),
    )


def sidebar(url=None, width: str = "100%") -> rx.Component:
    """Render the sidebar."""

    section_style = {
        "color": "#6C6C81",
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
            href="https://reflex-dev.notion.site/d1b60926ced14914bdbb42547ac84e50?v=723e0afc57294e40961d177aa691ee37",
            style=section_style,
        ),
        rx.link(
            "Deployment", href=hosting.deploy_quick_start.path, style=section_style
        ),
        rx.link("Self-Hosting", href=hosting.self_hosting.path, style=section_style),
        rx.link(
            "Contribute",
            href="https://github.com/reflex-dev/reflex/blob/main/CONTRIBUTING.md",
            style=section_style,
        ),
        rx.link("FAQ", href=faq.path, style=section_style),
        spacing="5",
        width="100%",
        height="100%",
        justify="end",
    )


sb = sidebar(width="100%")
