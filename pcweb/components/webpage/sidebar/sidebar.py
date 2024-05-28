"""Logic for the sidebar component."""

from __future__ import annotations

import reflex as rx

from pcweb import constants
from pcweb.pages.docs import getting_started, hosting
from pcweb.pages.faq import faq
from pcweb.pages.docs.library import library
from pcweb.pages.blog import blogs
from pcweb.pages.changelog import changelog
from pcweb.pages.docs.gallery import gallery
from ..navbar.buttons.github import github_desktop
from ..navbar.buttons.discord import discord

def sidebar_item(text: str, href: str) -> rx.Component:
    section_style = {
        "color": "#D6D6ED",
        "font_weight": "400",
    }

    return rx.link(
        rx.hstack(
            rx.text(text, style=section_style),
            rx.spacer(),
            rx.icon(tag="arrow-up-right", stroke_width="2px", color="#6C6C81"),
            width="100%",
            border="1px solid rgba(138, 140, 164, 0.10);",
            background= "rgba(161, 157, 213, 0.03);",
            padding="1em",
            border_radius="8px",
            _hover={
                "border": "1px solid rgba(138, 140, 164, 0.20);",
                "background": "rgba(161, 157, 213, 0.05);",
            },
        ),
        href=href,
        width="100%",
    )

def header() -> rx.Component:
    return rx.hstack(
    rx.link(
        rx.box(
            rx.image(
                src="/logos/dark/reflex.svg",
                alt="Reflex Logo",
                height="20px",
                justify="start",
            ),
        ),
        href="/",
    ),
    rx.spacer(),
    rx.drawer.close(
        rx.icon(
            tag="x",
            color="#6f6d78",
        ),
        as_child=True,
    ),
    width="100%",
    padding_bottom="1em",
)

def footer() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.image(src="/companies/light/github.svg", alt="A link to Reflex's Github", height="1.5em"),
            href=constants.GITHUB_URL,
        ),
        rx.link(
            rx.image(src="/companies/light/linkedin.svg", alt="A link to Reflex's Linkedin", height="1.5em"),
            href=constants.LINKEDIN_URL,
        ),
        rx.link(
            rx.image(src="/companies/light/yc.svg", alt="A link to Reflex's YC profile", height="1.5em"),
            href=constants.YC_URL,
        ),
        rx.link(
            rx.image(src="/companies/light/twitter.svg", alt="A link to Reflex's Twitter", height="1.5em"),
            href=constants.TWITTER_URL,
        ),
        rx.link(
            rx.image(src="/companies/light/discord.svg", alt="A link to Reflex's Discord", height="1.5em"),
            href=constants.DISCORD_URL,
        ),
        width="100%",
        gap="2em",
        padding_top=".5em",
        justify="center",
    )

def get_started() -> rx.Component:

    button_size={
        "padding_y": ".75em",
        "padding_x": "2em",
        "border_radius": "8px",
        "color":"#FFFFFF",
        "align_items":"center",
        "justify_content":"center",
        "font_weight":"400",
    }

    return rx.flex(
        rx.flex(
            "Get Started",
            rx.icon(
            tag="chevron-right",
                size=18,
                stroke_width="1px",
                padding_left=".1em",
            ),
            background="linear-gradient(180deg, #6151F3 0%, #5646ED 100%)",
            box_shadow="0px 2px 9px -4px rgba(64, 51, 192, 0.70), 0px 0px 6px 2px rgba(255, 255, 255, 0.12) inset, 0px 0px 0px 1px rgba(255, 255, 255, 0.09) inset",
            display= "inline-flex;",   
            border= "1px solid transparent;", 
            width="100%",
            style=button_size,
        ),
        _hover={
            "border": "1px solid rgba(94, 78, 242, .15)",
        },
        border= "1px solid transparent;",
        padding="3px",
        border_radius="8px",
        width="100%",
    ),


def sidebar(url=None, width: str = "100%") -> rx.Component:
    """Render the sidebar."""

    return rx.vstack(
        header(),
        sidebar_item("Docs", href=getting_started.introduction.path),
        sidebar_item("Blog", href=blogs.path),
        sidebar_item("Hosting", href=hosting.deploy_quick_start.path),
        sidebar_item("Gallery", href=gallery.path),
        sidebar_item("Changelog", href=changelog.path, ),
        sidebar_item("Roadmap", href=constants.ROADMAP_URL),
        sidebar_item("FAQ", href=faq.path),
        get_started(),
        footer(),
        spacing="3",
        width="100%",
        height="100%",
        justify="start",
        padding_x="1em",
    )


sb = sidebar(width="100%")
