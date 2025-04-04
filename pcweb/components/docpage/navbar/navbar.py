"""UI and logic for the navbar component."""

import reflex as rx
from reflex.experimental import ClientStateVar

from pcweb.pages.customers.views.bento_cards import _card
from pcweb.pages.docs import (
    wrapping_react,
    styling,
    custom_components as custom_c,
    getting_started,
)
from pcweb.components.button import button
from pcweb.pages.docs.library import library
from pcweb.pages.docs.custom_components import custom_components
from pcweb.pages.gallery import gallery
from .buttons.github import github
from .buttons.discord import discord
from .buttons.color import color
from .buttons.sidebar import navbar_sidebar_button
from .search import search_bar

from pcweb.pages.faq import faq
from pcweb.pages.errors import errors
from pcweb.pages.blog import blogs
from pcweb.pages.changelog import changelog
from pcweb.components.hosting_banner import hosting_banner
from pcweb.pages.blog.paths import blog_data

from pcweb.components.docpage.navbar.navmenu.navmenu import nav_menu
from pcweb.constants import (
    CONTRIBUTING_URL,
    FORUM_URL,
    ROADMAP_URL,
    REFLEX_CLOUD_URL,
    REFLEX_AI_BUILDER,
)
from ..sidebar import SidebarState


def resource_item(text: str, url: str, icon: str, index):
    return rx.el.li(
        rx.link(
            rx.box(
                rx.icon(icon, size=16, class_name="flex-shrink-0 text-slate-9"),
                rx.spacer(),
                rx.text(
                    text,
                    class_name="font-small text-slate-9 truncate text-start w-[100px]",
                ),
                rx.spacer(),
                rx.icon(
                    tag="chevron_right",
                    size=14,
                    class_name="flex-shrink-0 text-slate-12",
                ),
                class_name="flex flex-row flex-nowrap items-center gap-3 hover:bg-slate-3 px-[1.125rem] py-2 rounded-md w-full transition-bg justify-between",
            ),
            class_name="w-full text-slate-9 hover:!text-slate-9",
            underline="none",
            href=url,
            on_click=SidebarState.set_sidebar_index(index),
        ),
        class_name="w-full",
    )


def link_item(name: str, url: str, active_str: str = ""):
    # If URL doesn't end with a slash, add one
    router_path = rx.State.router.page.path
    url = url.rstrip("/") + "/"
    active = router_path.contains(active_str)
    if active_str == "docs":
        active = rx.cond(
            router_path.contains("library"),
            False,
            active,
        )
    if active_str == "":
        active = False

    common_cn = "transition-color p-[1.406rem_0px] font-small desktop-only items-center justify-center "
    active_cn = "shadow-[inset_0_-1px_0_0_var(--c-violet-9)] text-violet-9"
    unactive_cn = "shadow-none text-slate-9"
    return rx.link(
        name,
        href=url,
        underline="none",
        _hover={"color": rx.cond(active, "var(--c-violet-9)", "var(--c-slate-11)")},
        style={
            ":hover": {
                "color": rx.cond(active, "var(--c-violet-9)", "var(--c-slate-11)")
            }
        },
        class_name=common_cn + rx.cond(active, active_cn, unactive_cn),
    )


def blog_section_item(date: str, title: str, url: str) -> rx.Component:
    return rx.link(
        rx.box(
            rx.moment(
                date,
                format="MMM DD, YYYY",
                class_name="font-medium font-size-[0.8125rem] text-slate-9 truncate leading-[1.25rem] tracking-[-0.01013rem]",
            ),
            rx.box(
                rx.text(
                    title,
                    class_name="font-base text-slate-11 truncate",
                ),
                rx.icon(tag="chevron-right", size=14, class_name="!text-slate-8"),
                class_name="flex flex-row justify-between items-center w-full",
            ),
            class_name="flex flex-col items-start gap-1 hover:bg-slate-3 px-3.5 py-[1.125rem] rounded-md w-full transition-bg self-stretch",
        ),
        class_name="w-full",
        underline="none",
        href=url,
    )


def blog_section() -> rx.Component:
    return nav_menu.content(
        rx.box(
            rx.link(
                rx.moment(
                    str(list(blog_data.values())[0].metadata["date"]),
                    format="MMM DD, YYYY",
                    class_name="z-[2] pt-[0.875rem] pl-[1.125rem] font-instrument-sans font-medium text-[0.8125rem] text-white truncate leading-[1.25rem] tracking-[-0.01013rem]",
                ),
                rx.spacer(),
                rx.box(
                    rx.text(
                        list(blog_data.values())[0].metadata["title"],
                        class_name="font-base text-white truncate self-start",
                    ),
                    rx.box(
                        rx.icon(
                            tag="chevron-right",
                            size=14,
                            class_name="text-white",
                        ),
                        align_items="center",
                        justify="start",
                        class_name="flex flex-row justify-start",
                    ),
                    class_name="z-[2] flex flex-row justify-between px-[1.125rem] pb-[0.875rem] w-full",
                ),
                rx.box(
                    background_image=f"linear-gradient(to top, rgba(0, 0, 0, 3) 0%, rgba(0, 0, 0, 0) 35%), url({list(blog_data.values())[0].metadata['image']})",
                    class_name="group-hover:scale-105 absolute inset-0 bg-cover bg-no-repeat bg-center rounded-md transition-all duration-150 ease-out brightness-[0.8] group-hover:brightness-100",
                ),
                href="/" + list(blog_data.keys())[0],
                underline="none",
                class_name="relative flex flex-col flex-shrink-0 justify-start items-start gap-[6px] rounded-md w-[295px] h-[236px] text-white hover:text-white overflow-hidden group",
            ),
            rx.box(
                rx.link(
                    rx.box(
                        rx.el.h3(
                            "Latest in Blog",
                            class_name="flex items-start font-smbold text-slate-12 truncate self-stretch",
                        ),
                        rx.box(
                            rx.text(
                                "View all",
                                class_name="font-small text-slate-9 truncate",
                            ),
                            rx.icon(
                                tag="chevron-right",
                                size=14,
                                class_name="!text-slate-8",
                            ),
                            class_name="flex flex-row items-center gap-2",
                        ),
                        class_name="flex flex-row justify-between gap-3 hover:bg-slate-3 px-[1.125rem] py-3 rounded-md w-full text-nowrap transition-bg self-stretch",
                    ),
                    class_name="w-full",
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
                class_name="flex flex-col items-start gap-1.5 w-full",
            ),
            class_name="flex flex-row items-start gap-1.5 p-1.5 w-[610px]",
        ),
    )


def link_button(label: str, url: str) -> rx.Component:
    common_cn = (
        "transition-color font-small desktop-only items-center justify-start p-1 "
    )

    return rx.link(
        label,
        href=url,
        underline="none",
        _hover={"color": "var(--c-slate-11)"},
        class_name=common_cn + "text-slate-9",
    )


def grid_card(title: str, description: str, url: str, image: str) -> rx.Component:
    return rx.link(
        rx.box(
            rx.text(title, class_name="text-slate-12 text-base font-semibold"),
            rx.el.button(
                rx.icon("chevron-right", class_name="text-slate-9 size-4"),
                class_name="size-6 group-hover:bg-slate-3 transition-bg rounded-md flex items-center justify-center",
            ),
            class_name="flex flex-row items-center gap-2 justify-between",
        ),
        rx.text(description, class_name="text-slate-9 text-sm font-medium"),
        rx.image(
            src=image,
            class_name="absolute bottom-0 right-0",
        ),
        href=url,
        is_external=True,
        underline="none",
        class_name="w-[14.5rem] rounded-md shadow-small bg-white-1 border border-slate-4 flex flex-col gap-3 p-5 relative border-solid !h-[19.5625rem] overflow-hidden group",
    )


def grid_card_unique(title: str, description: str, url: str, component) -> rx.Component:
    return rx.link(
        rx.box(
            rx.text(title, class_name="text-slate-12 text-base font-semibold"),
            rx.el.button(
                rx.icon("chevron-right", class_name="text-slate-9 size-4"),
                class_name="size-6 group-hover:bg-slate-3 transition-bg rounded-md flex items-center justify-center",
            ),
            class_name="flex flex-row items-center gap-2 justify-between",
        ),
        rx.text(description, class_name="text-slate-9 text-sm font-medium"),
        component,
        href=url,
        is_external=True,
        underline="none",
        class_name="w-[14.5rem] rounded-md shadow-small bg-white-1 border border-slate-4 flex flex-col gap-3 p-5 relative border-solid !h-[17.5625rem] overflow-hidden group",
    )


def new_resource_section():
    return nav_menu.content(
        rx.box(
            # Links
            rx.box(
                link_button("Changelog", changelog.path),
                link_button("Contributing", "/"),
                link_button("Discussions", "/"),
                link_button("FAQ", faq.path),
                class_name="flex flex-col w-full p-2",
            ),
            class_name="flex flex-col w-full max-w-[9.1875rem] border-r border-slate-5",
        ),
        # Grid cards
        rx.box(
            grid_card_unique(
                "Blog",
                "See what's new in the Reflex ecosystem.",
                f"/blog",
                _card(
                    company="reflex",
                    is_company=False,
                    src=rx.color_mode_cond(
                        "/logos/light/reflex.svg",
                        "/logos/dark/reflex.svg",
                    ),
                ),
            ),
            grid_card_unique(
                "Customers",
                "Meet the teams who chose Reflex.",
                "/customers",
                _card("bayesline"),
            ),
            class_name="grid grid-cols-2 gap-3 p-3 bg-slate-1",
        ),
        class_name="flex flex-row shadow-large rounded-xl bg-slate-2 border border-slate-5 w-[40.55rem] font-sans overflow-hidden",
    )


# def resources_section() -> rx.Component:
#     return nav_menu.content(
#         rx.el.ul(
#             resource_item("Changelog", changelog.path, "list"),
#             resource_item("Debugging Guide", errors.path, "bug"),
#             resource_item("FAQ", faq.path, "circle-help"),
#             resource_item("Contribute", CONTRIBUTING_URL, "code-xml"),
#             resource_item("Roadmap", ROADMAP_URL, "route"),
#             resource_item("Forum", FORUM_URL, "github"),
#             resource_item("Blog", blogs.path, "blog"),
#             resource_item("Blog", blogs.path, "rss"),
#             resource_item("Templates", gallery.path, "layout-panel-top"),
#             class_name="items-start gap-1.5 gap-x-1.5 grid grid-cols-2 m-0 p-1.5 w-[492px] min-w-max",
#         ),
#     )


def new_menu_trigger(title: str, url: str = None, active_str: str = "") -> rx.Component:
    if url:
        return nav_menu.trigger(link_item(title, url, active_str))
    return nav_menu.trigger(
        rx.text(
            title,
            class_name="p-[1.406rem_0px] font-small text-slate-9 hover:text-slate-11 transition-color desktop-only",
        )
    )


def logo() -> rx.Component:
    return rx.link(
        rx.color_mode_cond(
            rx.image(
                src="/logos/light/reflex.svg", alt="Reflex Logo", class_name="shrink-0"
            ),
            rx.image(
                src="/logos/dark/reflex.svg", alt="Reflex Logo", class_name="shrink-0"
            ),
        ),
        class_name="flex shrink-0 mr-3",
        href="/",
    )


def doc_section():
    from pcweb.pages.docs.ai_builder import pages as ai_pages
    from pcweb.pages.docs.cloud import pages as cloud_pages

    return nav_menu.content(
        rx.el.ul(
            resource_item("AI Builder Docs", ai_pages[0].path, "bot", 0),
            resource_item(
                "Framework Docs", getting_started.introduction.path, "frame", 0
            ),
            resource_item("Cloud Docs", cloud_pages[0].path, "server", 0),
            class_name="items-start gap-1.5 gap-x-1.5 grid grid-cols-1 m-0 p-1.5 w-[180px] min-w-max",
        ),
    )


def new_component_section() -> rx.Component:
    return nav_menu.root(
        nav_menu.list(
            nav_menu.item(
                logo(),
            ),
            nav_menu.item(
                link_item("AI Builder", REFLEX_AI_BUILDER, "builder"),
            ),
            nav_menu.item(
                link_item("Framework", "/", "framework"),
            ),
            nav_menu.item(
                link_item("Cloud", "/hosting", "hosting"),
            ),
            nav_menu.item(new_menu_trigger("Docs"), doc_section()),
            nav_menu.item(new_menu_trigger("Resources"), new_resource_section()),
            nav_menu.item(
                new_menu_trigger("Pricing", "/pricing", "pricing"),
            ),
            class_name="desktop-only flex flex-row items-center gap-0 lg:gap-7 m-0 h-full list-none",
        ),
        nav_menu.list(
            nav_menu.item(search_bar()),
            nav_menu.item(github()),
            nav_menu.item(discord(), class_name="desktop-only"),
            nav_menu.item(color(), class_name="desktop-only"),
            nav_menu.item(
                rx.link(
                    button(
                        "Deploy",
                        class_name="!h-8 !font-small-smbold !rounded-[0.625rem] whitespace-nowrap",
                    ),
                    underline="none",
                    is_external=True,
                    href=REFLEX_CLOUD_URL,
                ),
                class_name="desktop-only",
            ),
            nav_menu.item(navbar_sidebar_button(), class_name="mobile-only"),
            class_name="flex flex-row gap-2 m-0 h-full list-none items-center",
        ),
        rx.box(
            nav_menu.viewport(),
            class_name="top-[80%] left-[250px] absolute flex justify-start w-full",
        ),
    )


@rx.memo
def navbar() -> rx.Component:
    return rx.box(
        hosting_banner(),
        rx.el.header(
            new_component_section(),
            class_name="flex flex-row items-center gap-12 bg-slate-1 shadow-[inset_0_-1px_0_0_var(--c-slate-3)] px-4 lg:px-6 w-screen h-[48px] lg:h-[65px]",
        ),
        class_name="flex flex-col w-full top-0 z-[9999] fixed",
    )
