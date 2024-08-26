"""UI and logic for the navbar component."""

import reflex as rx

from pcweb.pages.docs import (
    wrapping_react,
    styling,
    custom_components as custom_c,
    getting_started,
    hosting,
)
from pcweb.pages.docs.library import library
from pcweb.pages.docs.custom_components import custom_components
from pcweb.pages.docs.gallery import gallery
from .buttons.github import github
from .buttons.discord import new_discord
from .buttons.color import color
from .buttons.sidebar import navbar_sidebar_button
from .search import search_bar
from .state import NavbarState

from pcweb.pages.docs import getting_started, hosting
from pcweb.pages.faq import faq
from pcweb.pages.errors import errors
from pcweb.pages.docs.library import library
from pcweb.pages.blog import blogs
from pcweb.pages.changelog import changelog
from pcweb.pages.docs.gallery import gallery

from pcweb.pages.blog.paths import blog_data

# from pcweb.components.docpage.navbar.nav_menu.nav_menu import nav_menu
from pcweb.styles.fonts import small, small_semibold, base
from pcweb.styles.colors import c_color
from pcweb.components.docpage.navbar.navmenu.navmenu import nav_menu as new_nav_menu
from pcweb.styles.shadows import shadows
from pcweb.constants import CONTRIBUTING_URL, GITHUB_DISCUSSIONS_URL, ROADMAP_URL


def resource_header(text, url):
    return rx.link(
        rx.text(
            text,
            color=rx.color("mauve", 12),
            font_weight="600",
        ),
        href=url,
    )


def resources_item(text, url, icon):
    return rx.link(
        rx.flex(
            rx.icon(icon, size=20, color=rx.color("mauve", 10)),
            rx.text(text, color=rx.color("mauve", 10)),
            wrap="nowrap",
            spacing="2",
        ),
        href=url,
    )

def menu_trigger():
    return rx.flex(
        rx.text(
            "Components",
            color=rx.color("mauve", 11),
            font="Instrument Sans",
            weight="medium",
            style={"font-size": "16px"},
        ),
        rx.icon(tag="chevron_down", color=rx.color("mauve", 11), size=18),
        rx.badge("New", variant="solid"),
        align_items="center",
        _hover={
            "cursor": "pointer",
        },
        spacing="1",
    )


def menu_content():
    return rx.flex(
        rx.flex(
            rx.flex(
                resource_header("Core Components", library.path),
                resources_item("Library", library.path, "library-big"),
                resources_item("Theming", styling.theming.path, "palette"),
                direction="column",
                align_items="start",
                padding="20px",
                spacing="3",
                background_color=rx.color("mauve", 3),
            ),
            rx.flex(
                rx.flex(
                    resource_header("Custom Components", custom_components.path),
                    rx.badge("New", variant="solid"),
                    align_items="center",
                    spacing="1",
                ),
                resources_item(
                    "Community Library", custom_components.path, "library-big"
                ),
                resources_item("Wrapping React", wrapping_react.overview.path, "atom"),
                resources_item(
                    "Publishing Components", custom_c.overview.path, "globe"
                ),
                direction="column",
                align_items="start",
                height="200px",
                padding_y="20px",
                padding_left="10px",
                padding_right="40px",
                spacing="3",
            ),
            spacing="6",
            max_width="1000px",
            height="200px",
        ),
        border=f"1px solid {rx.color('mauve', 4)}",
        background=rx.color("mauve", 1),
        max_width="1000px",
        height="200px",
        padding="0",
        overflow="hidden",
        border_radius="8px",
    )


# def components_section():
#     return nav_menu.root(
#         nav_menu.list(
#             nav_menu.item(
#                 nav_menu.trigger(
#                     menu_trigger(),
#                     style=None,
#                 ),
#                 nav_menu.content(
#                     menu_content(),
#                 ),
#             ),
#             background_color="transparent",
#         ),
#         nav_menu.indicator(className="Arrow"),
#         nav_menu.viewport(),
#     )


def resource_item(text: str, url: str, icon: str, width: str = "236px"):
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16, color=c_color("slate", 9), flex_shrink="0"),
            rx.text(
                text,
                style={
                    "color": c_color("slate", 9),
                    "overflow": "hidden",
                    "text-overflow": "ellipsis",
                    "white-space": "nowrap",
                    **small,
                },
            ),
            rx.spacer(),
            rx.icon(
                tag="chevron_right",
                size=14,
                color=c_color("slate", 12),
                flex_shrink="0",
            ),
            style={
                "transition": "background 0.035s ease-out",
                "gap": "12px",
                "padding": "8px 18px",
                "border-radius": "6px",
                "align_items": "center",
                "width": "100%",
                "_hover": {
                    "background": c_color("slate", 3),
                },
                "wrap": "nowrap",
            },
        ),
        width=width,
        underline="none",
        href=url,
    )


def blog_section_item(date: str, title: str, url: str) -> rx.Component:
    moment_style = {
        "overflow": "hidden",
        "text-wrap": "nowrap",
        "color": c_color("slate", 9),
        "text-overflow": "ellipsis",
        "font-family": "Instrument Sans",
        "font-size": "13px",
        "font-style": "normal",
        "font-weight": "500",
        "line-height": "20px",
        "letter-spacing": "-0.162px",
    }
    return rx.link(
        rx.vstack(
            rx.text(rx.moment(date, format="MMM DD, YYYY"), **moment_style),
            rx.hstack(
                rx.text(
                    title,
                    color=c_color("slate", 11),
                    style={
                        "overflow": "hidden",
                        "text-overflow": "ellipsis",
                        "white-space": "nowrap",
                        **base,
                    },
                ),
                rx.icon(tag="chevron-right", color=c_color("slate", 8), size=14),
                align_items="center",
                justify="between",
                width="100%",
            ),
            gap="4px",
            align="start",
            padding="14px 18px",
            flex_direction="column",
            align_items="flex-start",
            align_self="stretch",
            width="100%",
            border_radius="6px",
            style={
                "transition": "background 0.035s ease-out",
                "_hover": {
                    "background": c_color("slate", 3),
                },
            },
        ),
        width="100%",
        underline="none",
        href=url,
    )


def blog_section() -> rx.Component:
    h3_style = {
        "overflow": "hidden",
        "color": c_color("slate", 12),
        "text-overflow": "ellipsis",
        "white-space": "nowrap",
        "display": "flex",
        "align-items": "flex-start",
        "align-self": "stretch",
        **small_semibold,
    }
    return new_nav_menu.content(
        rx.hstack(
            rx.link(
                rx.moment(
                    str(list(blog_data.values())[0].metadata["date"]),
                    format="MMM DD, YYYY",
                    style={
                        "overflow": "hidden",
                        "color": "white",
                        "text-overflow": "ellipsis",
                        "white-space": "nowrap",
                        "font-family": "Instrument Sans",
                        "font-size": "13px",
                        "font-style": "normal",
                        "font-weight": "500",
                        "line-height": "20px",
                        "letter-spacing": "-0.162px",
                        "padding-top": "14px",
                        "padding-left": "18px",
                        "z_index": "1",
                    },
                ),
                rx.spacer(),
                rx.hstack(
                    rx.text(
                        list(blog_data.values())[0].metadata["title"],
                        color="white",
                        **base,
                        style={
                            "text-overflow": "ellipsis",
                            "white-space": "nowrap",
                            "overflow": "hidden",
                            "align_self": "flex-start",
                        },
                    ),
                    rx.hstack(
                        rx.icon(
                            tag="chevron-right",
                            color="white",
                            size=14,
                        ),
                        align_items="center",
                        justify="start",
                    ),
                    z_index="1",
                    padding_bottom="14px",
                    padding_x="18px",
                    width="100%",
                    justify="between",
                ),
                rx.box(
                    position="absolute",
                    inset="0",
                    background_image=f'linear-gradient(to top, rgba(0, 0, 0, 0.7) 0%, rgba(0, 0, 0, 0) 25%), url({list(blog_data.values())[0].metadata["image"]})',
                    background_size="cover",
                    background_position="center",
                    background_repeat="no-repeat",
                    transition="transform 0.150s ease-out",
                    class_name="blog-cover",
                    border_radius="6px",
                ),
                style={
                    "&:hover > .blog-cover": {
                        "transform": "scale(1.05)",
                    },
                },
                width="295px",
                height="236px",
                flex_shrink="0",
                border_radius="6px",
                position="relative",
                display="flex",
                overflow="hidden",
                align_items="start",
                gap="6px",
                flex_direction="column",
                justify_content="start",
                href="/" + list(blog_data.keys())[0],
                underline="none",
            ),
            rx.vstack(
                rx.link(
                    rx.hstack(
                        rx.heading("Latest in Blog", as_="h3", style=h3_style),
                        rx.hstack(
                            rx.text(
                                "View all",
                                style={
                                    "overflow": "hidden",
                                    "color": c_color("slate", 9),
                                    "text-overflow": "ellipsis",
                                    "white-space": "nowrap",
                                    **small,
                                },
                            ),
                            rx.icon(
                                tag="chevron-right",
                                color=c_color("slate", 8),
                                size=14,
                            ),
                            align_items="center",
                            gap="8px",
                        ),
                        style={
                            "transition": "background 0.035s ease-out",
                            "gap": "12px",
                            "padding": "8px 18px",
                            "border-radius": "6px",
                            "align-items": "center",
                            "align-self": "stretch",
                            "justify-content": "space-between",
                            "width": "100%",
                            "_hover": {
                                "background": c_color("slate", 3),
                            },
                            "wrap": "nowrap",
                        },
                    ),
                    width="100%",
                    underline="none",
                    href=blogs.path,
                ),
                blog_section_item(
                    date=str(list(blog_data.values())[1].metadata["date"]),
                    title=list(blog_data.values())[1].metadata["title"],
                    url="/" + list(blog_data.keys())[1].replace("/docs/", ""),
                ),
                blog_section_item(
                    date=str(list(blog_data.values())[2].metadata["date"]),
                    title=list(blog_data.values())[2].metadata["title"],
                    url="/" + list(blog_data.keys())[2],
                ),
                gap="6px",
                width="100%",
                align_items="flex-start",
            ),
            width="100%",
            padding="6px",
            align_items="flex-start",
            gap="6px",
        ),
    )


def resources_section() -> rx.Component:
    return new_nav_menu.content(
        rx.unordered_list(
            resource_item("Changelog", changelog.path, "list"),
            resource_item("Debugging Guide", errors.path, "bug"),
            resource_item("FAQ", faq.path, "circle-help"),
            resource_item("Contribute", CONTRIBUTING_URL, "code-xml"),
            resource_item("Roadmap", ROADMAP_URL, "route"),
            resource_item("Github Discussions", GITHUB_DISCUSSIONS_URL, "github"),
            style={
                "display": "grid",
                "margin": "0",
                "column-gap": "6px",
                "width": "100%",
                "grid-template-columns": "repeat(2, 1fr)",
                "align-items": "flex-start",
                "gap": "6px",
                "padding": "6px",
            },
            margin_left="0px !important",
        ),
    )


def components_section() -> rx.Component:
    h3_style = {
        "overflow": "hidden",
        "color": c_color("slate", 12),
        "text-overflow": "ellipsis",
        "white-space": "nowrap",
        "display": "flex",
        "padding": "14px 18px",
        "align-items": "flex-start",
        "align-self": "stretch",
        **small_semibold,
    }
    return new_nav_menu.content(
        rx.vstack(
            rx.heading("Core Components", as_="h3", style=h3_style),
            rx.unordered_list(
                resource_item("Component Library", library.path, "layout-panel-left"),
                resource_item("Theming", styling.theming.path, "palette"),
                margin_left="0px !important",
                display="flex",
                flex_direction="column",
                gap="6px",
            ),
            width="100%",
            padding="6px",
            align="start",
            gap="6px",
        ),
        rx.vstack(
            rx.heading("Custom Components", as_="h3", style=h3_style),
            rx.unordered_list(
                resource_item(
                    "Community Library", custom_components.path, "blocks", width="280px"
                ),
                resource_item(
                    "Wrapping React",
                    wrapping_react.overview.path,
                    "atom",
                    width="280px",
                ),
                resource_item(
                    "Publishing Components",
                    custom_c.overview.path,
                    "git-fork",
                    width="280px",
                ),
                display="flex",
                flex_direction="column",
                gap="6px",
                margin_left="0px !important",
                align_items="flex-start",
            ),
            border_left=f"1px solid {rx.color('slate', 5)}",
            background_color=rx.color("slate", 1),
            width="100%",
            padding="6px",
            align="start",
            gap="6px",
        ),
        style={
            "display": "grid",
            "margin": "0",
            "column-gap": "6px",
            "width": "100%",
            "grid-template-columns": "repeat(2, 1fr)",
            "align-items": "flex-start",
            "gap": "6px",
        },
    )


def new_menu_trigger(title: str, url: str = None, active_str: str = "") -> rx.Component:
    text_style = {
        "transition": "color 0.035s ease-out",
        "padding": "22.5px 0px",
        "color": c_color("slate", 9),
        "_hover": {
            "color": c_color("slate", 11),
        },
        **small,
    }
    if url:
        return new_nav_menu.trigger(link_item(title, url, active_str))
    return new_nav_menu.trigger(
        rx.text(
            title,
            style=text_style,
            display=["none", "none", "none", "none", "flex", "flex"],
        )
    )


def logo() -> rx.Component:
    return rx.link(
        rx.color_mode_cond(
            rx.image(
                src="/logos/light/reflex.svg",
                alt="Reflex Logo",
                justify="start",
                flex_shrink="0",
            ),
            rx.image(
                src="/logos/dark/reflex.svg",
                alt="Reflex Logo",
                justify="start",
                flex_shrink="0",
            ),
        ),
        flex_shrink="0",
        display="flex",
        href="/",
    )


def new_component_section() -> rx.Component:
    return new_nav_menu.root(
        new_nav_menu.list(
            new_nav_menu.item(
                logo(),
            ),
            new_nav_menu.item(
                link_item("Docs", getting_started.introduction.path, "docs"),
            ),
            new_nav_menu.item(
                link_item("Showcase", gallery.path, "gallery"),
            ),
            new_nav_menu.item(
                new_menu_trigger("Blog", blogs.path, "blog"),
                blog_section(),
            ),
            new_nav_menu.item(
                new_menu_trigger("Resources"),
                resources_section(),
            ),
            new_nav_menu.item(
                new_menu_trigger("Components", library.path, "library"),
                components_section(),
            ),
            new_nav_menu.item(
                link_item("Hosting", hosting.deploy_quick_start.path, "hosting"),
            ),
            gap=["0px", "0px", "0px", "24px", "24px"],
        ),
        new_nav_menu.list(
            rx.flex(
                new_nav_menu.item(
                    search_bar(),
                ),
                new_nav_menu.item(
                    github(),
                ),
                gap="8px",
                flex_direction=[
                    "row-reverse",
                    "row-reverse",
                    "row-reverse",
                    "row",
                    "row",
                ],
                align_items="center",
            ),
            new_nav_menu.item(
                new_discord(),
                display=["none", "none", "none", "none", "flex", "flex"],
            ),
            new_nav_menu.item(
                color(), display=["none", "none", "none", "none", "flex", "flex"]
            ),
            new_nav_menu.item(
                navbar_sidebar_button(),
                display=["flex", "flex", "flex", "flex", "none", "none"],
            ),
            gap=["16px", "16px", "16px", "8px", "8px"],
        ),
        rx.box(
            new_nav_menu.viewport(),
            style={
                "position": "absolute",
                "display": "flex",
                "justify-content": "flex-start",
                "width": "100%",
                "top": "80%",
                "left": "250px",
            },
        ),
    )


def link_item(name: str, url: str, active_str: str = ""):
    # If URL doesnt end with a slash, add one
    router_path = rx.State.router.page.path
    if not url.endswith("/"):
        url += "/"
    active = router_path.contains(active_str)
    if active_str == "docs":
        active = rx.cond(
            router_path.contains("hosting")
            | router_path.contains("library")
            | router_path.contains("gallery"),
            False,
            active,
        )
    if active_str == "":
        active = False
    link_style = {
        "text-decoration": "none !important",
        "transition": "color 0.035s ease-out",
        "box_shadow": rx.cond(
            active, f"inset 0 -1px 0 0 {c_color('violet', 9)}", "none"
        ),
        "padding": "22.5px 0px",
        ":hover": {
            "color": rx.cond(active, c_color("violet", 9), c_color("slate", 11)),
        },
        **small,
    }
    return rx.link(
        name,
        color=rx.cond(active, c_color("violet", 9), c_color("slate", 9)),
        style=link_style,
        href=url,
        _hover={
            "color": rx.cond(active, c_color("violet", 9), c_color("slate", 11)),
        },
        align_items="center",
        justify_content="center",
        display=["none", "none", "none", "none", "flex", "flex"],
    )


def navbar() -> rx.Component:
    return rx.el.header(
        new_component_section(),
        background_color=c_color("slate", 1),
        box_shadow=f"inset 0 -1px 0 0 {c_color('slate', 4)}",
        width="100%",
        align_items="center",
        gap="48px",
        height=["48px", "65px"],
        flex_direction="row",
        z_index="15",
        top="0px",
        position="fixed",
    )
