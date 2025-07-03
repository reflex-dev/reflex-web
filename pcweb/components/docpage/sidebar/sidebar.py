"""Logic for the sidebar component."""

from __future__ import annotations

import reflex as rx

from pcweb.components.docpage.navbar.state import NavbarState
from pcweb.constants import ENTERPRISE_DOCS_URL
from pcweb.styles.colors import c_color

from .sidebar_items.ai import ai_builder_overview_items
from .sidebar_items.component_lib import component_lib, graphing_libs
from .sidebar_items.enterprise import enterprise_items, enterprise_usage_items, enterprise_component_items
from .sidebar_items.learn import backend, cli_ref, frontend, hosting, learn
from .sidebar_items.recipes import recipes
from .sidebar_items.reference import api_reference
from .state import SideBarBase, SideBarItem, SidebarState

Scrollable_SideBar = """
function scrollToActiveSidebarLink() {
  const currentPath = window.location.pathname.replace(/\\/+$|\\/$/g, "") + "/";

  const activeLink = document.querySelector(`#sidebar-container a[href="${currentPath}"]`) ||
                    document.querySelector(`#sidebar-container a[href="${currentPath.slice(0, -1)}"]`);

  if (activeLink) {
    activeLink.scrollIntoView({
      block: "center",
    });
  }
}

setTimeout(scrollToActiveSidebarLink, 100);

window.addEventListener("popstate", () => {
  setTimeout(scrollToActiveSidebarLink, 100);
});

document.addEventListener('click', (e) => {
  const link = e.target.closest('a[href^="/docs"]');
  if (link) {
    setTimeout(scrollToActiveSidebarLink, 200);
  }
});
"""


def sidebar_link(*children, **props):
    """Create a sidebar link that closes the sidebar when clicked."""
    return rx.link(
        *children,
        on_click=props.pop("on_click", NavbarState.set_sidebar_open(False)),
        underline="none",
        **props,
    )


def sidebar_leaf(
    item_index: str,
    item: SideBarItem,
    url: str,
) -> rx.Component:
    """Get the leaf node of the sidebar."""
    item.link = item.link.replace("_", "-").rstrip("/") + "/"
    return (
        rx.accordion.item(
            rx.accordion.header(
                sidebar_link(
                    rx.flex(
                        rx.text(
                            item.names,
                            color=rx.cond(
                                item.link == url,
                                c_color("violet", 9),
                                c_color("slate", 9),
                            ),
                            _hover={
                                "color": c_color("slate", 11),
                            },
                            margin="0.5em 0.5em 0.2em 0.5em",
                            width="100%",
                            class_name="transition-color",
                        ),
                    ),
                    href=item.link,
                ),
            ),
            value=item_index,
            border="none",
            width="100%",
            class_name="!overflow-visible",
        )
        if item.outer
        else rx.accordion.item(
            rx.accordion.header(
                rx.cond(
                    item.link == url,
                    sidebar_link(
                        rx.flex(
                            rx.text(
                                item.names,
                                class_name="font-small text-violet-9 transition-color",
                            ),
                            padding="0px 8px 0px 28px",
                            class_name="border-l-[1.5px] border-violet-9",
                        ),
                        href=item.link,
                    ),
                    sidebar_link(
                        rx.flex(
                            rx.text(
                                item.names,
                                class_name="font-small text-slate-9 transition-color hover:text-slate-11 w-full",
                            ),
                            padding="0px 8px 0px 28px",
                            class_name="border-l-[1.5px] border-slate-4 hover:border-slate-8",
                        ),
                        href=item.link,
                    ),
                ),
            ),
            border="none",
            value=item_index,
            width="100%",
            class_name="!overflow-visible",
        )
    )


def sidebar_icon(name):
    icon_map = {
        "Getting Started": "rocket",
        "Advanced Onboarding": "newspaper",
        "Components": "layers",
        "Pages": "sticky-note",
        "Styling": "palette",
        "Assets": "folder-open-dot",
        "Wrapping React": "atom",
        "Vars": "variable",
        "Events": "arrow-left-right",
        "State Structure": "boxes",
        "API Routes": "route",
        "Client Storage": "package-open",
        "Database": "database",
        "Authentication": "lock-keyhole",
        "Utility Methods": "cog",
        "Deploy Quick Start": "earth",
        "CLI Reference": "square-terminal",
        "App": "blocks",
        "Project": "server",
        "Self Hosting": "server",
        "Custom Components": "blocks",
        "Usage": "chart-column",
    }

    return (
        rx.icon(tag=icon_map.get(name), size=16, class_name="mr-5")
        if name in icon_map
        else rx.fragment()
    )


def sidebar_item_comp(
    item_index: str,
    item: SideBarItem,
    index: list[int],
    url: str,
):
    index = rx.Var.create(index)
    return (
        sidebar_leaf(item_index=item_index, item=item, url=url)
        if not item.children
        else rx.accordion.item(
            rx.accordion.header(
                rx.accordion.trigger(
                    sidebar_icon(item.names),
                    rx.text(
                        item.names,
                        class_name="font-small",
                    ),
                    rx.box(class_name="flex-grow"),
                    rx.accordion.icon(
                        class_name="size-4 !text-slate-9 group-hover:!text-violet-9"
                    ),
                    class_name="!px-0 flex items-center !bg-transparent !hover:bg-transparent !py-2 !pr-0 w-full !text-slate-9 aria-expanded:text-slate-11 hover:!text-slate-11 transition-color group",
                ),
            ),
            rx.accordion.content(
                rx.accordion.root(
                    *[
                        sidebar_item_comp(
                            item_index="index" + str(child_index),
                            item=child,
                            index=index[1:],
                            url=url,
                        )
                        for child_index, child in enumerate(item.children)
                    ],
                    type="multiple",
                    collapsible=True,
                    default_value=index[:1].foreach(lambda x: "index" + x.to_string()),
                    class_name="!my-2 flex flex-col items-start gap-4 !ml-[10px] list-none [box-shadow:inset_1.25px_0_0_0_var(--c-slate-4)_!important] !bg-transparent !rounded-none",
                ),
                class_name="!p-0 w-full !bg-transparent before:!h-0 after:!h-0",
            ),
            value=item_index,
            class_name="border-none w-full !bg-transparent",
        )
    )


def calculate_index(sidebar_items, url: str) -> list[int]:
    sidebar_items = (
        sidebar_items if isinstance(sidebar_items, list) else [sidebar_items]
    )
    index_list = []

    if not url:
        return index_list

    url = url.rstrip("/") + "/"
    for item in sidebar_items:
        item.link = item.link.rstrip("/") + "/"
    sub = 0
    for i, item in enumerate(sidebar_items):
        if not item.children:
            sub += 1
        if item.link == url:
            return [i - sub]
        index = calculate_index(item.children, url)
        if index:
            return [i - sub] + index

    return index_list


def append_to_items(items, flat_items):
    for item in items:
        if not item.children:
            flat_items.append(item)
        append_to_items(item.children, flat_items)


flat_items = []
append_to_items(
    learn
    + frontend
    + backend
    + hosting
    + component_lib
    + graphing_libs
    + recipes
    + ai_builder_overview_items
    + api_reference
    + enterprise_items,
    flat_items,
)


def get_prev_next(url):
    """Get the previous and next links in the sidebar."""
    url = url.strip("/")
    for i, item in enumerate(flat_items):
        if item.link.strip("/") == url:
            prev_link = flat_items[i - 1] if i > 0 else None
            next_link = flat_items[i + 1] if i < len(flat_items) - 1 else None
            return prev_link, next_link
    return None, None


def filter_out_non_sidebar_items(items: list[SideBarBase]) -> list[SideBarItem]:
    """Filter out non-sidebar items making sure only SideBarItems are present.

    Args:
        items: The items to filter.

    Return:
        The filtered side bar items.
    """
    return [item for item in items if isinstance(item, SideBarItem)]


def sidebar_category(name: str, url: str, icon: str, index: int):
    return rx.el.li(
        rx.link(
            rx.box(
                rx.box(
                    rx.box(
                        rx.icon(
                            tag=icon,
                            size=16,
                            class_name="!text-slate-9",
                        ),
                        class_name="flex justify-center items-center border-slate-4 bg-white-1 shadow-medium border rounded-md size-8",
                    ),
                    rx.el.h3(
                        name,
                        class_name="font-small"
                        + rx.cond(
                            SidebarState.sidebar_index == index,
                            " text-slate-11",
                            " text-slate-9",
                        ),
                    ),
                    class_name="flex flex-row justify-start items-center gap-3 w-full",
                ),
                rx.box(
                    class_name="bg-violet-9 rounded-full shrink-0 size-[7px]"
                    + rx.cond(
                        SidebarState.sidebar_index == index, " visible", " hidden"
                    ),
                ),
                class_name="flex flex-row justify-between items-center hover:bg-slate-3 p-[0.5rem_1rem_0.5rem_0.5rem] rounded-2xl w-full transition-bg self-stretch"
                + rx.cond(
                    SidebarState.sidebar_index == index,
                    " bg-slate-3",
                    " bg-transparent",
                ),
            ),
            on_click=SidebarState.set_sidebar_index(index),
            class_name="w-full text-slate-9 hover:!text-slate-9",
            underline="none",
            href=url,
        ),
        class_name="w-full",
    )


def create_sidebar_section(
    section_title: str,
    section_url: str,
    items: list[SideBarItem],
    index: rx.Var[list[str]] | list[str],
    url: rx.Var[str] | str,
) -> rx.Component:
    # Check if the section has any nested sections (Like the Other Libraries Section)
    nested = any(len(child.children) > 0 for item in items for child in item.children)
    # Make sure the index is a list
    index = index.to(list)
    return rx.el.li(
        rx.link(
            rx.el.h5(
                section_title,
                class_name="font-smbold text-[0.875rem] text-slate-12 hover:text-violet-9 leading-5 tracking-[-0.01313rem] transition-color",
            ),
            underline="none",
            href=section_url,
            class_name="py-3",
        ),
        rx.accordion.root(
            *[
                sidebar_item_comp(
                    item_index="index" + str(item_index),
                    item=item,
                    index=index[1:] if nested else [],
                    url=url,
                )
                for item_index, item in enumerate(items)
            ],
            type="multiple",
            collapsible=True,
            default_value=index[:1].foreach(lambda x: "index" + x.to_string()),
            class_name="ml-0 pl-0 w-full !bg-transparent !shadow-none rounded-[0px]",
        ),
        class_name="flex flex-col items-start ml-0 w-full",
    )


@rx.memo
def sidebar_comp(
    url: str,
    learn_index: list[int],
    component_lib_index: list[int],
    frontend_index: list[int],
    backend_index: list[int],
    hosting_index: list[int],
    graphing_libs_index: list[int],
    api_reference_index: list[int],
    recipes_index: list[int],
    enterprise_index: list[int],
    #
    cli_ref_index: list[int],
    ai_builder_overview_index: list[int],
    tutorials_index: list[int],
    width: str = "100%",
):
    from pcweb.pages.docs import ai_builder as ai_builder_pages
    from pcweb.pages.docs import enterprise, getting_started
    from pcweb.pages.docs import hosting as hosting_page
    from pcweb.pages.docs import state, ui
    from pcweb.pages.docs.apiref import pages
    from pcweb.pages.docs.custom_components import custom_components
    from pcweb.pages.docs.library import library
    from pcweb.pages.docs.recipes_overview import overview

    return rx.box(  # pyright: ignore [reportCallIssue]
        # Handle sidebar categories for docs/cloud first
        rx.cond(  # pyright: ignore [reportCallIssue]
            rx.State.router.page.path.startswith("/docs/hosting/"),
            rx.el.ul(
                sidebar_category(
                    "Cloud", hosting_page.deploy_quick_start.path, "cloud", 0
                ),
                # sidebar_category(
                #     "CLI Reference", cloud_pages[0].path, "book-marked", 1
                # ),
                class_name="flex flex-col items-start gap-1 w-full list-none",
            ),
            rx.cond(  # pyright: ignore [reportCallIssue]
                rx.State.router.page.path.startswith("/docs/ai-builder/"),
                rx.el.ul(
                    sidebar_category(
                        "Learn",
                        "/docs/ai-builder/overview/what-is-reflex-build",
                        "bot",
                        0,
                    ),
                    class_name="flex flex-col items-start gap-1 w-full list-none",
                ),
                # If the path doesn't start with /docs/cloud, check for general docs
                rx.cond(  # pyright: ignore [reportCallIssue]
                    rx.State.router.page.path.startswith("/docs/"),
                    rx.el.ul(
                        sidebar_category(
                            "Learn",
                            getting_started.introduction.path,
                            "graduation-cap",
                            0,
                        ),
                        sidebar_category(
                            "Components",
                            library.path,
                            "layout-panel-left",
                            1,
                        ),
                        sidebar_category(
                            "API Reference",
                            pages[0].path,
                            "book-text",
                            2,
                        ),
                        sidebar_category(
                            "Enterprise",
                            enterprise.overview.path,
                            "building-2",
                            3,
                        ),
                        class_name="flex flex-col items-start gap-1 w-full list-none",
                    ),
                ),
            ),
        ),
        # Handle the sidebar content based on docs/cloud or docs
        rx.cond(  # pyright: ignore [reportCallIssue]
            rx.State.router.page.path.startswith("/docs/hosting/"),
            rx.match(  # pyright: ignore [reportCallIssue]
                SidebarState.sidebar_index,
                (
                    0,
                    rx.el.ul(
                        create_sidebar_section(
                            "Cloud",
                            hosting_page.deploy_quick_start.path,
                            hosting,
                            hosting_index,
                            url,
                        ),
                        class_name="flex flex-col items-start gap-6 p-[0px_1rem_0px_0.5rem] w-full list-none list-style-none",
                    ),
                ),
                # (
                #     1,
                #     rx.el.ul(
                #         create_sidebar_section(
                #             "CLI Reference",
                #             cloud_pages[0].path,
                #             cli_ref,
                #             cli_ref_index,
                #             url,
                #         ),
                #         class_name="flex flex-col items-start gap-6 p-[0px_1rem_0px_0.5rem] w-full list-none list-style-none",
                #     ),
                # ),
            ),
            rx.cond(  # pyright: ignore [reportCallIssue]
                rx.State.router.page.path.startswith("/docs/ai-builder/"),
                rx.el.ul(
                    create_sidebar_section(
                        "Overview",
                        ai_builder_pages.overview.what_is_reflex_build.path,
                        ai_builder_overview_items,
                        ai_builder_overview_index,
                        url,
                    ),
                    class_name="flex flex-col items-start gap-6 p-[0px_1rem_0px_0.5rem] w-full list-none list-style-none",
                ),
                rx.cond(  # pyright: ignore [reportCallIssue]
                    rx.State.router.page.path.startswith("/docs/"),
                    rx.match(  # pyright: ignore [reportCallIssue]
                        SidebarState.sidebar_index,
                        (
                            0,
                            rx.el.ul(
                                create_sidebar_section(
                                    "Onboarding",
                                    getting_started.introduction.path,
                                    learn,
                                    learn_index,
                                    url,
                                ),
                                create_sidebar_section(
                                    "User Interface",
                                    ui.overview.path,
                                    filter_out_non_sidebar_items(frontend),
                                    frontend_index,
                                    url,
                                ),
                                create_sidebar_section(
                                    "State",
                                    state.overview.path,
                                    filter_out_non_sidebar_items(backend),
                                    backend_index,
                                    url,
                                ),
                                create_sidebar_section(
                                    "Recipes",
                                    overview.path,
                                    recipes,
                                    recipes_index,
                                    url,
                                ),
                                class_name="flex flex-col items-start gap-6 p-[0px_1rem_0px_0.5rem] w-full list-none list-style-none",
                            ),
                        ),
                        (
                            1,
                            rx.el.ul(
                                create_sidebar_section(
                                    "Core",
                                    library.path,
                                    component_lib,
                                    component_lib_index,
                                    url,
                                ),
                                create_sidebar_section(
                                    "Graphing",
                                    library.path,
                                    graphing_libs,
                                    graphing_libs_index,
                                    url,
                                ),
                                rx.link(  # pyright: ignore [reportCallIssue]
                                    rx.box(  # pyright: ignore [reportCallIssue]
                                        rx.box(  # pyright: ignore [reportCallIssue]
                                            rx.icon("atom", size=16),  # pyright: ignore [reportCallIssue]
                                            rx.el.h5(
                                                "Custom Components",
                                                class_name="font-smbold text-[0.875rem] text-slate-12 leading-5 tracking-[-0.01313rem] transition-color",
                                            ),
                                            class_name="flex flex-row items-center gap-3 text-slate-12",
                                        ),
                                        rx.text(  # pyright: ignore [reportCallIssue]
                                            "See what components people have made with Reflex!",
                                            class_name="font-small text-slate-9",
                                        ),
                                        class_name="flex flex-col gap-2 border-slate-5 bg-slate-1 hover:bg-slate-3 shadow-large px-3.5 py-2 border rounded-xl transition-bg",
                                    ),
                                    underline="none",
                                    href=custom_components.path,
                                ),
                                class_name="flex flex-col items-start gap-6 p-[0px_1rem_0px_0.5rem] w-full list-none list-style-none",
                            ),
                        ),
                        (
                            2,
                            rx.el.ul(
                                create_sidebar_section(
                                    "Reference",
                                    pages[0].path,
                                    api_reference,
                                    api_reference_index,
                                    url,
                                ),
                                class_name="flex flex-col items-start gap-6 p-[0px_1rem_0px_0.5rem] w-full list-none list-style-none",
                            ),
                        ),
                        (
                            3,
                            rx.el.ul(
                                create_sidebar_section(
                                    "Enterprise Usage",
                                    enterprise.overview.path,
                                    enterprise_usage_items,
                                    enterprise_index,
                                    url,
                                ),
                                create_sidebar_section(
                                    "Components",
                                    enterprise.ag_grid.index.path,
                                    enterprise_component_items,
                                    enterprise_index,
                                    url,
                                ),
                                class_name="flex flex-col items-start gap-6 p-[0px_1rem_0px_0.5rem] w-full list-none list-style-none",
                            ),
                        ),
                    ),
                ),
            ),
        ),
        # Handle general docs sections
        style={
            "&::-webkit-scrollbar-thumb": {
                "background_color": "transparent",
            },
            "&::-webkit-scrollbar": {
                "background_color": "transparent",
            },
        },
        class_name="flex flex-col !pb-24 gap-6 items-start max-h-[90%] p-[1rem_0rem_1rem_1rem] lg-p2 scroll-p-4 fixed w-full overflow-y-scroll hidden-scrollbar lg:max-w-[300px]",
    )


def sidebar(url=None, width: str = "100%") -> rx.Component:
    """Render the sidebar."""
    learn_index = calculate_index(learn, url)
    component_lib_index = calculate_index(component_lib, url)
    frontend_index = calculate_index(frontend, url)
    backend_index = calculate_index(backend, url)
    hosting_index = calculate_index(hosting, url)
    graphing_libs_index = calculate_index(graphing_libs, url)
    api_reference_index = calculate_index(api_reference, url)
    recipes_index = calculate_index(recipes, url)
    enterprise_index = calculate_index(enterprise_items, url)

    cli_ref_index = calculate_index(cli_ref, url)
    ai_builder_overview_index = calculate_index(ai_builder_overview_items, url)

    return rx.box(
        sidebar_comp(
            url=url,
            learn_index=learn_index,
            component_lib_index=component_lib_index,
            frontend_index=frontend_index,
            backend_index=backend_index,
            hosting_index=hosting_index,
            graphing_libs_index=graphing_libs_index,
            api_reference_index=api_reference_index,
            recipes_index=recipes_index,
            enterprise_index=enterprise_index,
            ai_builder_overview_index=ai_builder_overview_index,
            cli_ref_index=cli_ref_index,
            #
            width=width,
        ),
        on_mount=rx.call_script(Scrollable_SideBar),
        id=rx.Var.create("sidebar-container"),
        class_name="flex justify-end w-full h-full",
    )


sb = sidebar(width="100%")
