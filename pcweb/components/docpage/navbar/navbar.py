"""UI and logic for the navbar component."""

import reflex as rx
import reflex_ui as ui
from reflex_ui.blocks.lemcal import lemcal_dialog

from pcweb.components.hosting_banner import hosting_banner
from pcweb.constants import REFLEX_BUILD_URL, REFLEX_CLOUD_URL
from pcweb.pages.blog import blogs
from pcweb.pages.blog.paths import blog_data
from pcweb.pages.docs import ai_builder, getting_started
from pcweb.pages.faq import faq
from pcweb.pages.framework.framework import framework
from pcweb.pages.hosting.hosting import hosting_landing
from pcweb.pages.use_cases.use_cases import use_cases_page

from ...link_button import resources_button
from ..sidebar import SidebarState
from .buttons.discord import discord
from .buttons.github import github
from .buttons.sidebar import navbar_sidebar_button
from .search import search_bar


def resource_item(text: str, url: str, icon: str, index):
    return rx.el.a(
        rx.box(
            ui.icon(icon, size=16, class_name="flex-shrink-0 text-slate-9"),
            rx.text(
                text,
                class_name="font-small text-slate-9 truncate text-start w-[150px]",
            ),
            rx.icon(
                tag="chevron_right",
                size=14,
                stroke_width=2,
                class_name="flex-shrink-0 text-slate-8 ml-auto",
            ),
            class_name="flex flex-row flex-nowrap items-center gap-4 hover:bg-secondary-3 px-[1.125rem] py-2 rounded-md w-full transition-colors",
        ),
        class_name="w-full text-slate-9 hover:text-slate-9",
        to=url,
        on_click=SidebarState.set_sidebar_index(index),
    )


def link_item(name: str, url: str, active_str: str = ""):
    router_path = rx.State.router.page.path

    url = url.rstrip("/") + "/"

    if active_str == "/":
        is_home = router_path == "/"
        is_docs = router_path.contains("docs")
        not_cloud = ~(router_path.contains("cloud") | router_path.contains("hosting"))
        not_ai_builder = ~router_path.contains("ai-builder")

        active = rx.cond(
            is_home, True, rx.cond(is_docs & not_cloud & not_ai_builder, True, False)
        )

    elif active_str == "builder":
        active = router_path.contains("ai-builder")

    elif active_str == "hosting" or active_str == "cloud":
        active = router_path.contains("cloud") | router_path.contains("hosting")

    elif active_str == "pricing":
        active = router_path.contains("pricing")

    elif active_str == "framework":
        # Check if path contains "docs" but excludes ai-builder, cloud, and hosting
        # OR if path contains "open-source" (for the main open source landing page)
        is_docs = router_path.contains("docs")
        is_open_source_page = router_path.contains("open-source")
        not_cloud = ~(router_path.contains("cloud") | router_path.contains("hosting"))
        not_ai_builder = ~router_path.contains("ai-builder")
        active = (is_docs & not_cloud & not_ai_builder) | is_open_source_page

    elif active_str == "docs":
        active = rx.cond(
            router_path.contains("library"), False, router_path.contains("docs")
        )
    elif active_str:
        active = router_path.contains(active_str)
    else:
        active = False

    common_cn = "transition-color p-[1.406rem_0px] font-small xl:flex hidden items-center justify-center hover:text-secondary-12 "
    active_cn = "shadow-[inset_0_-0.5px_0_0_var(--c-violet-9)] text-violet-9 hover:text-violet-9"
    unactive_cn = "shadow-none text-secondary-11"

    return rx.el.a(
        name,
        to=url,
        class_name=common_cn + rx.cond(active, active_cn, unactive_cn),
        on_click=SidebarState.set_sidebar_index(0),
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
    return ui.navigation_menu.content(
        rx.box(
            rx.link(
                rx.moment(
                    str(next(iter(blog_data.values())).metadata["date"]),
                    format="MMM DD, YYYY",
                    class_name="z-[2] pt-[0.875rem] pl-[1.125rem] font-instrument-sans font-medium text-[0.8125rem] text-white truncate leading-[1.25rem] tracking-[-0.01013rem]",
                ),
                rx.spacer(),
                rx.box(
                    rx.text(
                        next(iter(blog_data.values())).metadata["title"],
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
                    background_image=f"linear-gradient(to top, rgba(0, 0, 0, 3) 0%, rgba(0, 0, 0, 0) 35%), url({next(iter(blog_data.values())).metadata['image']})",
                    class_name="group-hover:scale-105 absolute inset-0 bg-cover bg-no-repeat bg-center rounded-md transition-all duration-150 ease-out brightness-[0.8] group-hover:brightness-100",
                ),
                href="/" + next(iter(blog_data.keys())),
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
    return rx.el.a(
        resources_button(
            label, size="md", variant="transparent", class_name="justify-start w-full"
        ),
        to=url,
        target="_blank",
        underline="none",
        class_name="!w-full",
    )


def grid_card(
    title: str, description: str, url: str, image: str, image_style: str
) -> rx.Component:
    return rx.el.a(
        rx.box(
            rx.text(title, class_name="text-slate-12 text-base font-semibold"),
            rx.el.button(
                rx.icon("chevron-right", class_name="text-slate-9 size-4"),
                class_name="size-6 group-hover:bg-secondary-3 transition-colors rounded-md flex items-center justify-center",
            ),
            class_name="flex flex-row items-center gap-2 justify-between",
        ),
        rx.text(description, class_name="text-slate-9 text-sm font-medium"),
        rx.image(
            src=image,
            class_name=image_style,
        ),
        to=url,
        class_name="w-[14.5rem] rounded-md shadow-small bg-white-1 border border-slate-4 flex flex-col gap-3 p-5 relative border-solid !h-[16.5625rem] overflow-hidden group",
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
        class_name="w-[14.5rem] rounded-md shadow-small bg-white-1 border border-slate-4 flex flex-col gap-3 p-5 relative border-solid !h-[14.5625rem] overflow-hidden group",
    )


#
def new_resource_section():
    _company_items = [
        {
            "label": "Newsletter",
            "url": "https://reflex.dev/open-source/#newsletter",
            "icon": "MailAtSign01Icon",
        },
        {"label": "Blog", "url": "/blog", "icon": "RightToLeftListDashIcon"},
        {"label": "Affiliates", "url": "/affiliates", "icon": "AddTeamIcon"},
        {"label": "Use Cases", "url": use_cases_page.path, "icon": "CheckListIcon"},
    ]

    _open_source_items = [
        {"label": "Templates", "url": "/templates", "icon": "SidebarTopIcon"},
        {
            "label": "Changelog",
            "url": "https://github.com/reflex-dev/reflex/releases",
            "icon": "Clock02Icon",
        },
        {
            "label": "Contributing",
            "url": "https://github.com/reflex-dev/reflex/blob/main/CONTRIBUTING.md",
            "icon": "SourceCodeIcon",
        },
        {
            "label": "Discussions",
            "url": "https://github.com/orgs/reflex-dev/discussions",
            "icon": "Message01Icon",
        },
        {
            "label": "FAQ",
            "url": faq.path,
            "icon": "HelpCircleIcon",
        },
    ]

    def _link_button(label: str, url: str, icon: str) -> rx.Component:
        return rx.el.a(
            resources_button(
                ui.icon(icon, size=16, class_name="flex-shrink-0"),
                label,
                size="md",
                variant="transparent",
                class_name="justify-start w-full items-center gap-3",
            ),
            to=url,
            class_name="w-full",
        )

    def _resource_section_column(
        section_title: str, resource_item: list[dict[str, str]]
    ):
        return rx.box(
            rx.box(
                rx.text(
                    section_title,
                    class_name="text-sm text-slate-12 font-semibold px-2.5 py-1 pb-2",
                ),
                *[
                    _link_button(item["label"], item["url"], item["icon"])
                    for item in resource_item
                ],
                class_name="flex flex-col w-full p-2",
            ),
            class_name="flex flex-col w-full max-w-[9.1875rem]",
        )

    return ui.navigation_menu.content(
        _resource_section_column("Open Source", _open_source_items),
        _resource_section_column("Company", _company_items),
        # Grid cards
        rx.box(
            grid_card(
                "Customers",
                "Meet the teams who chose Reflex.",
                "/customers",
                rx.color_mode_cond(
                    "/bayesline_light_landing.png",
                    "/bayesline_dark_landing.png",
                ),
                "absolute -bottom-7 rounded-tl-md",
            ),
            class_name="grid grid-cols-2 gap-3 p-3 bg-slate-1",
        ),
        unstyled=True,
        class_name=ui.cn(
            ui.navigation_menu.class_names.CONTENT,
            "flex flex-row rounded-xl w-[34.55rem] font-sans overflow-hidden p-1.5",
        ),
    )


def new_menu_trigger(
    title: str, url: str | None = None, active_str: str = ""
) -> rx.Component:
    if url:
        return ui.navigation_menu.trigger(link_item(title, url, active_str))
    return ui.navigation_menu.trigger(
        rx.box(
            rx.text(
                title,
                class_name="p-[1.406rem_0px] font-medium text-sm text-secondary-11 group-hover:text-secondary-12 transition-colors",
            ),
            rx.icon(
                "chevron-down",
                class_name="chevron size-5 !text-secondary-11 group-hover:!text-secondary-12 py-1 mr-0 transition-all ease-out",
            ),
            class_name="flex-row items-center gap-x-1 group user-select-none cursor-pointer xl:flex hidden",
            on_click=rx.stop_propagation,
        ),
        style={
            "&[data-popup-open] .chevron": {
                "transform": "rotate(180deg)",
            },
        },
        unstyled=True,
    )


def logo() -> rx.Component:
    return rx.el.a(
        rx.fragment(
            rx.image(
                src="/logos/light/reflex.svg",
                alt="Reflex Logo",
                class_name="shrink-0 block dark:hidden",
            ),
            rx.image(
                src="/logos/dark/reflex.svg",
                alt="Reflex Logo",
                class_name="shrink-0 hidden dark:block",
            ),
        ),
        class_name="block shrink-0 mr-3",
        to="/",
    )


def doc_section():
    from pcweb.pages.docs import hosting as hosting_page

    return ui.navigation_menu.content(
        resource_item(
            "AI Builder Docs",
            ai_builder.overview.best_practices.path,
            "MagicWand01Icon",
            0,
        ),
        resource_item(
            "Open Source Docs",
            getting_started.introduction.path,
            "SourceCodeCircleIcon",
            0,
        ),
        resource_item(
            "Cloud Docs", hosting_page.deploy_quick_start.path, "CloudServerIcon", 0
        ),
        unstyled=True,
        class_name=ui.cn(
            ui.navigation_menu.class_names.CONTENT,
            "flex flex-col gap-1.5 m-0 p-1.5 w-[280px] min-w-max h-auto",
        ),
    )


def new_component_section() -> rx.Component:
    from pcweb.pages.docs import ai_builder as ai_builder_pages
    from pcweb.pages.docs import hosting as hosting_page

    return ui.navigation_menu.root(
        ui.navigation_menu.list(
            ui.navigation_menu.item(
                rx.box(
                    logo(),
                    rx.badge(
                        "Docs",
                        variant="surface",
                        class_name=(
                            "text-violet-9 text-sm "
                            + rx.cond(
                                rx.State.router.page.path.contains("docs")
                                | rx.State.router.page.path.contains("ai-builder")
                                | rx.State.router.page.path.contains("cloud"),
                                "hidden lg:flex",
                                "hidden",
                            )
                        ),
                    ),
                    class_name="flex flex-row gap-x-0 items-center",
                    unstyled=True,
                ),
            ),
            rx.cond(
                rx.State.router.page.path.contains("docs")
                | rx.State.router.page.path.contains("ai-builder")
                | rx.State.router.page.path.contains("cloud"),
                rx.el.div(
                    ui.navigation_menu.item(
                        render_=link_item(
                            "AI Builder",
                            ai_builder_pages.overview.best_practices.path,
                            "builder",
                        ),
                        unstyled=True,
                    ),
                    ui.navigation_menu.item(
                        render_=link_item(
                            "Open Source",
                            getting_started.introduction.path,
                            "framework",
                        ),
                        unstyled=True,
                        class_name="whitespace-nowrap",
                    ),
                    ui.navigation_menu.item(
                        render_=link_item(
                            "Cloud", hosting_page.deploy_quick_start.path, "hosting"
                        ),
                        unstyled=True,
                    ),
                    class_name="xl:flex hidden flex-row items-center gap-0 lg:gap-5 2xl:gap-7 m-0 h-full list-none",
                ),
                rx.el.div(
                    ui.navigation_menu.item(
                        render_=link_item(
                            "AI Builder",
                            REFLEX_BUILD_URL,
                            "builder",
                        ),
                        unstyled=True,
                    ),
                    ui.navigation_menu.item(
                        render_=link_item("Open Source", framework.path, "framework"),
                        class_name="whitespace-nowrap",
                        unstyled=True,
                    ),
                    ui.navigation_menu.item(
                        render_=link_item("Cloud", hosting_landing.path, "hosting"),
                        unstyled=True,
                    ),
                    class_name="xl:flex hidden flex-row items-center gap-0 lg:gap-5 2xl:gap-7 m-0 h-full list-none",
                ),
            ),
            ui.navigation_menu.item(
                new_menu_trigger("Docs"),
                doc_section(),
                display=rx.cond(
                    rx.State.router.page.path.contains("docs")
                    | rx.State.router.page.path.contains("ai-builder")
                    | rx.State.router.page.path.contains("cloud"),
                    "none",
                    "block",
                ),
                class_name="cursor-pointer",
                unstyled=True,
            ),
            ui.navigation_menu.item(
                new_menu_trigger("Resources"),
                new_resource_section(),
                class_name="cursor-pointer",
                unstyled=True,
            ),
            ui.navigation_menu.item(
                ui.navigation_menu.item(
                    render_=link_item(
                        "Pricing",
                        "/pricing",
                        "pricing",
                    ),
                    unstyled=True,
                ),
                class_name="xl:flex hidden",
                unstyled=True,
            ),
            class_name="flex flex-row items-center gap-0 lg:gap-5 2xl:gap-7 m-0 h-full list-none",
        ),
        ui.navigation_menu.list(
            ui.navigation_menu.item(search_bar()),
            ui.navigation_menu.item(github()),
            ui.navigation_menu.item(discord(), class_name="xl:flex hidden"),
            ui.navigation_menu.item(
                rx.link(
                    ui.button(
                        "Sign In",
                        size="sm",
                        variant="secondary",
                        class_name="font-semibold text-secondary-11 whitespace-nowrap",
                    ),
                    underline="none",
                    is_external=True,
                    href=f"{REFLEX_CLOUD_URL.strip('/')}/?redirect_url={REFLEX_BUILD_URL}",
                ),
                class_name="desktop-only",
            ),
            ui.navigation_menu.item(
                render_=lemcal_dialog(
                    ui.button(
                        "Book a Demo",
                        size="sm",
                        variant="primary",
                        class_name="font-semibold whitespace-nowrap max-xl:hidden",
                    ),
                ),
                unstyled=True,
                class_name="xl:flex hidden",
            ),
            ui.navigation_menu.item(
                navbar_sidebar_button(),
                class_name="xl:hidden flex",
                unstyled=True,
            ),
            class_name="flex flex-row gap-2 m-0 h-full list-none items-center",
        ),
        ui.navigation_menu.portal(
            ui.navigation_menu.positioner(
                ui.navigation_menu.popup(
                    ui.navigation_menu.viewport(),
                ),
                side_offset=-10,
            ),
        ),
        unstyled=True,
        class_name="relative flex w-full items-center h-full justify-between gap-6 mx-auto z-[9999] flex-row max-w-[94.5rem]",
    )


@rx.memo
def navbar() -> rx.Component:
    return rx.box(
        hosting_banner(),
        rx.el.header(
            new_component_section(),
            class_name="flex flex-row items-center gap-12 bg-slate-1 shadow-[inset_0_-0.5px_0_0_var(--c-slate-3)] px-4 lg:px-6 w-screen h-[48px] lg:h-[65px]",
        ),
        class_name="flex flex-col w-full top-0 z-[9999] fixed text-secondary-12",
    )
