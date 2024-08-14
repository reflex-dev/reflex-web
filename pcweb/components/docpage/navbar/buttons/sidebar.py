import reflex as rx
from pcweb.styles.colors import c_color
from pcweb.styles.fonts import small
from pcweb.components.icons.icons import get_icon
from pcweb.constants import GITHUB_URL, TWITTER_URL, DISCORD_URL
from pcweb.pages.docs import getting_started, hosting
from pcweb.pages.docs.library import library
from pcweb.pages.blog import blogs
from pcweb.pages.docs.gallery import gallery
from reflex.style import toggle_color_mode


def social_menu_item(
    icon: str,
    url="/",
    border: bool = False,
    border_color: list = [
        f"1px solid {c_color('slate', 1)}",
        f"1px solid {c_color('slate', 1)}",
        f"1px solid {c_color('slate', 5)}",
        f"1px solid {c_color('slate', 5)}",
        f"1px solid {c_color('slate', 5)}",
    ],
    **props,
) -> rx.Component:
    return rx.link(
        rx.box(
            get_icon(icon, color=c_color("slate", 9)),
            style={
                "display": "flex",
                "padding": "4px 12px",
                "justify-content": "center",
                "align-items": "center",
                "gap": "8px",
                "align-self": "stretch",
                "cursor": "pointer",
                ":hover": {"background_color": c_color("slate", 3)},
                "transition": "background 0.075s ease-out",
                "overflow": "hidden",
            },
            _hover={
                "background_color": c_color("slate", 3),
            },
            **props,
            overflow="hidden",
            border_left=border_color if border else "none",
            border_right=border_color if border else "none",
        ),
        width="100%",
        href=url,
        is_external=True,
    )


def drawer_socials():
    return rx.hstack(
        social_menu_item("github", GITHUB_URL, height="47px"),
        social_menu_item(
            "twitter",
            TWITTER_URL,
            border=True,
            border_color=[f"1px solid {c_color('slate', 4)}"],
            height="47px",
        ),
        social_menu_item("discord", DISCORD_URL, height="47px"),
        border_bottom=f"1px solid {c_color('slate', 4)}",
        gap="0px",
        width="100%",
        align="center",
    )


def drawer_item(text: str, url: str, active_str: str = ""):
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
    return rx.link(
        text,
        href=url,
        display="flex",
        underline="none",
        justify_content="center",
        align_items="center",
        padding="14px 16px",
        width="100%",
        color=rx.cond(active, c_color("violet", 9), c_color("slate", 9)),
        _hover={
            "color": c_color("violet", 9),
        },
        style={
            ":hover": {
                "color": c_color("violet", 9),
            },
            **small,
        },
        border_bottom=f"1px solid {c_color('slate', 4)}",
    )


def navbar_sidebar_drawer(trigger):
    return (
        rx.drawer.root(
            rx.drawer.trigger(
                trigger,
            ),
            rx.drawer.portal(
                rx.drawer.content(
                    rx.vstack(
                        drawer_item("Docs", getting_started.introduction.path, "docs"),
                        drawer_item("Showcase", gallery.path, "gallery"),
                        drawer_item("Blog", blogs.path, "blog"),
                        drawer_item("Components", library.path, "library"),
                        drawer_item(
                            "Hosting", hosting.deploy_quick_start.path, "hosting"
                        ),
                        drawer_socials(),
                        rx.el.button(
                            rx.color_mode.icon(
                                light_component=rx.icon(
                                    "sun", color=c_color("slate", 9), size=16
                                ),
                                dark_component=rx.icon(
                                    "moon", color=c_color("slate", 9), size=16
                                ),
                            ),
                            display="flex",
                            justify_content="center",
                            align_items="center",
                            width="100%",
                            height="47px",
                            padding="4px 12px",
                            on_click=toggle_color_mode,
                        ),
                        align_items="center",
                        background_color=c_color("slate", 1),
                        width="100%",
                        height="100%",
                        gap="0px",
                    ),
                    style={
                        "@media (min-width: 0em)": {
                            "inset": "48px auto auto auto",
                        },
                        "@media (min-width: 30em)": {
                            "inset": "64px auto auto auto",
                        },
                        "@media (min-width: 48em)": {
                            "inset": "64px auto auto auto",
                        },
                    },
                    height="100%",
                    width="100%",
                    background_color="transparent",
                    outline="none",
                )
            ),
            direction="bottom",
        ),
    )


def docs_sidebar_drawer(sidebar: rx.Component, trigger):
    return rx.drawer.root(
        rx.drawer.trigger(trigger, as_child=True),
        rx.drawer.portal(
            rx.drawer.overlay(
                backdrop_filter="blur(4px)",
                background="rgba(0, 0, 0, 0.1)",
            ),
            rx.drawer.content(
                rx.vstack(
                    rx.drawer.close(
                        rx.box(
                            height="5px",
                            width="96px",
                            flex_shrink="0",
                            top="-12px",
                            border_radius="1000px",
                            background_color=c_color("slate", 9),
                            position="absolute",
                        ),
                        as_child=True,
                    ),
                    sidebar,
                    gap="0px",
                    position="relative",
                    width="100%",
                ),
                border_radius="24px 24px 0px 0px",
                top="64px",
                height="100%",
                width="100%",
                flex_direction="column",
                background_color=c_color("slate", 1),
                outline="none",
            ),
        ),
    )

def navbar_sidebar_button() -> rx.Component:
    return rx.flex(
        navbar_sidebar_drawer(
            rx.el.button(
                rx.icon(
                    "x",
                    size=24,
                    color=c_color("slate", 9),
                    flex_shrink="0",
                    style={
                        "[data-state=open] &": {
                            "display": "flex",
                        },
                        "[data-state=closed] &": {
                            "display": "none",
                        },
                    },
                ),
                rx.icon(
                    "menu",
                    size=24,
                    color=c_color("slate", 9),
                    flex_shrink="0",
                    style={
                        "[data-state=open] &": {
                            "display": "none",
                        },
                        "[data-state=closed] &": {
                            "display": "flex",
                        },
                    },
                ),
            ),
        ),
        style={
            "width": "32px",
            "height": "32px",
            "align_items": "center",
            "justify_content": "center",
        },
        width="auto",
    )
