"""Logic for the sidebar component."""

from __future__ import annotations

import reflex as rx
from pcweb import styles
from pcweb.components.docpage.navbar.state import NavbarState
from pcweb.route import Route
from .state import SidebarState, SidebarItem

from .sidebar_items.learn import learn, frontend, backend, hosting
from .sidebar_items.component_lib import get_component_link, component_lib, other_libs
from .sidebar_items.reference import api_reference, tutorials
from .sidebar_items.recipes import recipes


heading_style2 = {
    "background_color": rx.color("accent", 3),
    "border_radius": "0.5em",
    "width": "100%",
    "padding_left": "0.5em",
    "padding_right": "0.5em",
}


def sidebar_link(*children, **props):
    """Create a sidebar link that closes the sidebar when clicked."""
    on_click = props.pop("on_click", NavbarState.set_sidebar_open(False))
    return rx.link(
        *children,
        on_click=on_click,
        **props,
    )


def sidebar_leaf(
    item: SidebarItem,
    url: str,
) -> rx.Component:
    """Get the leaf node of the sidebar."""
    item.link=item.link.replace("_", "-")

    if item.outer:
        return sidebar_link(
            rx.flex(
                rx.text(
                    item.names,
                    color=rx.cond(
                        item.link == url,
                        rx.color("accent", 11),
                        rx.color("mauve", 11),
                    ),
                    _hover={
                        "color": rx.color("accent", 10),
                        "text_decoration": "none",
                    },
                    margin_left="0.5em",
                    margin_top="0.5em",
                    margin_bottom="0.2em",
                    width="100%",
                ),
            ),
            href=item.link,
        )

    return rx.chakra.accordion_item(
        rx.cond(
            item.link == url,
            sidebar_link(
                rx.flex(
                    rx.flex(
                        rx.text(
                            item.names,
                            color=rx.color("accent", 11),
                            font_weight="600",
                            margin_left="0.25em",
                        ),
                        style=heading_style2,
                        margin_top="0.2em",
                        margin_bottom="0.2em",
                    ),
                    padding_left="0.5em",
                    border_left=f"1.5px solid {rx.color('accent', 11)}",
                ),
                _hover={"text_decoration": "none"},
                href=item.link,
            ),
            sidebar_link(
                rx.flex(
                    rx.text(
                        item.names,
                        color=rx.color("mauve", 11),
                        _hover={
                            "color": rx.color("accent", 11),
                            "text_decoration": "none",
                        },
                        margin_left="0.25em",
                        margin_top="0.2em",
                        margin_bottom="0.2em",
                        width="100%",
                    ),
                    padding_left="1em",
                    border_left=f"1.5px solid {rx.color('mauve', 3)}",
                ),
                _hover={"text_decoration": "none"},
                href=item.link,
            ),
        ),
        border="none",
        width="100%",
    )


def sidebar_icon(name):
    mappings = {
        "Getting Started": "rocket",
        "Tutorial": "life-buoy",
        "Components": "layers",
        "Pages": "sticky-note",
        "Styling": "palette",
        "Assets": "folder-open-dot",
        "Wrapping React": "atom",
        "Vars": "variable",
        "Events": "arrow-left-right",
        "Substates": "boxes",
        "API Routes": "route",
        "Client Storage": "package-open",
        "Database": "database",
        "Authentication": "lock-keyhole",
        "Utility Methods": "cog",
        "Reflex Deploy": "earth",
        "Self Hosting": "server",
        "Custom Components": "blocks",
    }

    if name in mappings:
        return rx.icon(
            tag=mappings[name],
            color=rx.color("mauve", 11),
            size=18,
            margin_right="0.5em",
        )
    else:
        return rx.fragment()


def sidebar_item_comp(
    item: SidebarItem,
    index: list[int],
    url: str,
):

    return rx.cond(
        len(item.children) == 0,
        sidebar_leaf(item=item, url=url),
        rx.chakra.accordion_item(
            rx.chakra.accordion_button(
                sidebar_icon(item.names),
                rx.text(
                    item.names,
                    color=rx.color("mauve", 11),
                    font_family=styles.SANS,
                    font_weight="500",
                ),
                rx.box(
                    flex_grow=1,
                ),
                rx.chakra.accordion_icon(),
                align_items="center",
                _hover={
                    "color": rx.color("accent", 10),
                },
                color=rx.color("mauve", 11),
                width="100%",
                padding_left="10px",
                padding_right="0px",
            ),
            rx.chakra.accordion_panel(
                rx.chakra.accordion(
                    rx.flex(
                        *[
                            sidebar_item_comp(item=child, index=index, url=url)
                            for child in item.children
                        ],
                        align_items="start",
                        direction="column",
                    ),
                    allow_multiple=True,
                    default_index=rx.cond(index, index[1:2], []),
                ),
                width="100%",
            ),
            border="none",
            width="100%",
        ),
    )


def calculate_index(sidebar_items, url):
    if not isinstance(sidebar_items, list):
        sidebar_items = [sidebar_items]

    sub = 0
    for i, item in enumerate(sidebar_items):
        if len(item.children) == 0:
            sub += 1
        if item.link == url:
            return [i - sub]
        index = calculate_index(item.children, url)
        if index is not None:
            return [i - sub] + index
    return None


sidebar_items = learn + frontend + backend + hosting + component_lib
# Flatten the list of sidebar items
flat_items = []

def append_to_items(items):
    for item in items:
        if len(item.children) == 0:
            flat_items.append(item)
        append_to_items(item.children)
append_to_items(sidebar_items)

def get_prev_next(url):
    """Get the previous and next links in the sidebar."""
    url = url.strip("/")
    for i, item in enumerate(flat_items):
        if item.link.strip("/") == url:
            if i == 0:
                return None, flat_items[i + 1]
            elif i == len(flat_items) - 1:
                return flat_items[i - 1], None
            else:
                return flat_items[i - 1], flat_items[i + 1]
    return None, None


def sidebar_category(name, url, icon, color, index):
    return rx.link(
        rx.flex(
            rx.button(
                rx.icon(
                    tag=icon,
                    color="white",
                    fill="rgba(255, 255, 255, 0.25)",
                    size=20,
                ),
                height="35px",
                width="35px",
                padding="0px",
                border_radius="6px",
                color_scheme=color,
                variant="classic",
                align_items="center",
                justify="center",
            ),
            rx.text(
                name,
                color=rx.cond(
                    SidebarState.sidebar_index == index,
                    rx.color("mauve", 12),
                    rx.color("mauve", 11),
                ),
                font_size="16px",
                font_weight="500",
                padding="0px 0px 0px 14px",
            ),
            on_click=lambda: SidebarState.set_sidebar_index(index),
            _hover={
                "background_color": rx.color("mauve", 2),
            },
            align_items="center",
            justify="start",
            padding_y="0.5em",
            padding_x="0.5em",
            border_radius="0.5em",
            width="100%",
            cursor="pointer",
        ),
        href=url,
    )


def create_sidebar_section(section_title, items, index, url):
    return rx.flex(
        rx.link(
            section_title,
            color=rx.color("mauve", 12),
            font_weight="600",
            padding_top="1em",
            padding_left="0.5em",
            href=url,
        ),
        rx.chakra.accordion(
            *[
                sidebar_item_comp(
                    item=item,
                    index=[-1],
                    url=url,
                )
                for item in items
            ],
            allow_multiple=True,
            default_index=index if index is not None else [],
            width="100%",
            padding_left="0em",
            margin_left="0em",
        ),
        margin_left="0em",
        direction="column",
        width="100%",
        align_items="left",
    )


@rx.memo
def sidebar_comp(
    url: str,
    learn_index: list[int],
    component_lib_index: list[int],
    frontend_index: list[int],
    backend_index: list[int],
    hosting_index: list[int],
    other_libs_index: list[int],
    api_reference_index: list[int],
    recipes_index: list[int],
    tutorials_index: list[int],
    width: str = "100%",
):

    from pcweb.pages.docs.recipes_overview import overview
    from pcweb.pages.docs.library import library
    from pcweb.pages.docs import getting_started, state, ui, hosting as hosting_page
    from pcweb.pages.docs.apiref import pages


    return rx.flex(
        sidebar_category("Learn", getting_started.introduction.path, "graduation-cap", "jade", 0),
        sidebar_category("Components", library.path,  "layout-panel-left", "blue", 1),
        sidebar_category("Recipes", overview.path, "scan-text", "indigo", 2),
        sidebar_category("API Reference", pages[0].path, "book-text", "violet", 3),

        rx.divider(size="4", margin_top="0.5em", margin_bottom="0.5em"),
        rx.match(
            SidebarState.sidebar_index,
            (
                0,
                rx.flex(
                    create_sidebar_section("Onboarding", learn, learn_index, url),
                    create_sidebar_section("UI", frontend, frontend_index, url),
                    create_sidebar_section("State", backend, backend_index, url),
                    create_sidebar_section("Hosting", hosting, hosting_index, url),
                    direction="column",
                ),
            ),
            (
                1,
                rx.flex(
                    create_sidebar_section(
                        "Core Components", component_lib, component_lib_index, url
                    ),
                    create_sidebar_section(
                        "Other Libraries", other_libs, other_libs_index, url
                    ),
                    direction="column",
                ),
            ),
            (
                2,
                rx.flex(
                    create_sidebar_section(
                        "Recipes", recipes, recipes_index, url
                    ),
                    direction="column",
                )
            ),
            (
                3,
                rx.flex(
                    create_sidebar_section(
                        "Reference", api_reference, api_reference_index, url
                    ),
                    create_sidebar_section(
                        "Tutorials", tutorials, tutorials_index, url
                    ),
                    direction="column",
                ),
            ),
        ),
        direction="column",
        align_items="left",
        overflow_y="scroll",
        max_height="90%",
        width=width,
        padding_bottom="6em",
        position="fixed",
        scroll_padding="1em",
        style={
            "&::-webkit-scrollbar-thumb": {
                "background_color": "transparent",
            },
            "&::-webkit-scrollbar": {
                "background_color": "transparent",
            },
        },
    )


def sidebar(url=None, width: str = "100%") -> rx.Component:
    """Render the sidebar."""
    learn_index = calculate_index(learn, url)
    component_lib_index = calculate_index(component_lib, url)
    frontend_index = calculate_index(frontend, url)
    backend_index = calculate_index(backend, url)
    hosting_index = calculate_index(hosting, url)
    other_libs_index = calculate_index(other_libs, url)
    api_reference_index = calculate_index(api_reference, url)
    recipes_index = calculate_index(recipes, url)
    tutorials_index = calculate_index(tutorials, url)

    return rx.flex(
        sidebar_comp(
            url=url,
            learn_index=learn_index,
            component_lib_index=component_lib_index,
            frontend_index=frontend_index,
            backend_index=backend_index,
            hosting_index=hosting_index,
            other_libs_index=other_libs_index,
            api_reference_index=api_reference_index,
            recipes_index=recipes_index,
            tutorials_index=tutorials_index,
            width=width,
        ),
        width="100%",
        height="100%",
        justify="center",
    )


sb = sidebar(width="100%")
