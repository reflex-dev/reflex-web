import reflex as rx
from reflex.style import toggle_color_mode

from pcweb.components.icons.icons import get_icon
from pcweb.constants import DISCORD_URL, GITHUB_URL, TWITTER_URL
from pcweb.pages.blog import blogs
from pcweb.pages.docs import getting_started
from pcweb.pages.docs.library import library
from pcweb.pages.framework.framework import framework
from pcweb.pages.gallery import gallery
from pcweb.pages.hosting.hosting import hosting_landing


def social_menu_item(
    icon: str,
    url="/",
    border: bool = False,
) -> rx.Component:
    aria_labels = {
        "github": "Visit Reflex on GitHub",
        "twitter": "Follow Reflex on X",
        "discord": "Join Reflex Discord community",
    }
    return rx.link(
        get_icon(icon=icon, class_name="!text-slate-9"),
        class_name="flex justify-center items-center gap-2 hover:bg-slate-3 px-4 py-[0.875rem] w-full h-[47px] transition-bg overflow-hidden"
        + (" border-slate-4 border-x border-solid border-y-0" if border else ""),
        href=url,
        is_external=True,
        custom_attrs={"aria-label": aria_labels.get(icon, f"Visit {icon}")},
    )


def drawer_socials() -> rx.Component:
    return rx.box(
        social_menu_item("github", GITHUB_URL),
        social_menu_item(
            "twitter",
            TWITTER_URL,
            border=True,
        ),
        social_menu_item("discord", DISCORD_URL),
        class_name="flex flex-row items-center border-slate-4 border-y-0 !border-b w-full",
    )


def drawer_item(text: str, url: str, active_str: str = "") -> rx.Component:
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
        underline="none",
        color=rx.cond(active, "var(--c-violet-9)", "var(--c-slate-9)"),
        class_name="flex justify-center items-center border-slate-4 px-4 py-[0.875rem] border-t-0 border-b border-solid w-full font-small hover:!text-violet-9 border-x-0",
    )


def navbar_sidebar_drawer(trigger) -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(
            trigger,
        ),
        rx.drawer.portal(
            rx.drawer.content(
                rx.box(
                    drawer_item("Docs", getting_started.introduction.path, "docs"),
                    drawer_item("Templates", gallery.path, "gallery"),
                    drawer_item("Blog", blogs.path, "blog"),
                    drawer_item("Case Studies", "/customers", "customers"),
                    drawer_item("Components", library.path, "library"),
                    drawer_item("Open Source", framework.path, "open-source"),
                    drawer_item("Cloud", hosting_landing.path, "hosting"),
                    drawer_item("Pricing", "/pricing", "pricing"),
                    drawer_socials(),
                    rx.el.button(
                        rx.color_mode.icon(
                            light_component=rx.icon(
                                "sun", size=16, class_name="!text-slate-9"
                            ),
                            dark_component=rx.icon(
                                "moon", size=16, class_name="!text-slate-9"
                            ),
                        ),
                        on_click=toggle_color_mode,
                        class_name="flex flex-row justify-center items-center px-3 py-0.5 w-full h-[47px]",
                        custom_attrs={"aria-label": "Toggle color mode"},
                    ),
                    class_name="flex flex-col items-center bg-slate-1 w-full h-full",
                ),
                class_name="!bg-transparent w-full h-full !outline-none !top-[47px]",
            )
        ),
        direction="bottom",
    )


def docs_sidebar_drawer(sidebar: rx.Component, trigger) -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(trigger, as_child=True),
        rx.drawer.portal(
            rx.drawer.overlay(
                class_name="!bg-[rgba(0,0,0,0.1)] backdrop-blur-[4px]",
            ),
            rx.drawer.content(
                rx.box(
                    rx.drawer.close(
                        rx.box(
                            class_name="absolute left-1/2 transform -translate-x-1/2 top-[-12px] flex-shrink-0 bg-slate-9 rounded-full w-[96px] h-[5px]",
                        ),
                        as_child=True,
                    ),
                    sidebar,
                    class_name="relative flex flex-col w-full",
                ),
                class_name="!top-[4rem] flex-col !bg-slate-1 rounded-[24px_24px_0px_0px] w-full h-full !outline-none",
            ),
        ),
    )


def navbar_sidebar_button() -> rx.Component:
    return rx.box(
        navbar_sidebar_drawer(
            rx.el.button(
                rx.icon(
                    "x",
                    size=24,
                    style={
                        "[data-state=open] &": {
                            "display": "flex",
                        },
                        "[data-state=closed] &": {
                            "display": "none",
                        },
                    },
                    class_name="!text-slate-9 shrink-0",
                ),
                rx.icon(
                    "menu",
                    size=24,
                    style={
                        "[data-state=open] &": {
                            "display": "none",
                        },
                        "[data-state=closed] &": {
                            "display": "flex",
                        },
                    },
                    class_name="!text-slate-9 shrink-0",
                ),
                custom_attrs={"aria-label": "Open sidebar"},
            ),
        ),
        class_name="flex justify-center items-center size-8",
    )
