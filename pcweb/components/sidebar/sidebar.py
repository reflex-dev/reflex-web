"""Logic for the sidebar component."""

from __future__ import annotations

import reflex as rx
from pcweb import styles
from pcweb.components.navbar import NavbarState
from pcweb.route import Route
from pcweb.styles import font_weights as fw
from .state import SidebarState, SidebarItem
from .style import heading_style2, heading_style3

from .sidebar_items.learn import learn, frontend, backend, hosting
from .sidebar_items.component_lib import get_component_link, component_lib, other_libs
from .sidebar_items.reference import api_reference, recipes, tutorials


def sidebar_link(*children, **props):
    """Create a sidebar link that closes the sidebar when clicked."""
    on_click = props.pop("on_click", NavbarState.set_sidebar_open(False))
    return rx.link(
        *children,
        on_click=on_click,
        **props,
    )


def create_item(route: Route, children=None):
    """Create a sidebar item from a route."""
    if children is None:
        name = route.title
        if name.endswith("Overview"):
            # For "Overview", we want to keep the qualifier prefix ("Components overview")
            alt_name_for_next_prev = name
            name = "Overview"
        else:
            alt_name_for_next_prev = ""
        name = name.replace("Api", "API").replace("Cli", "CLI")
        return SidebarItem(
            names=name, alt_name_for_next_prev=alt_name_for_next_prev, link=route.path
        )
    return SidebarItem(
        names=route,
        children=list(map(create_item, children)),
    )


@rx.memo
def sidebar_leaf(
    item: SidebarItem,
    url: str,
) -> rx.Component:
    """Get the leaf node of the sidebar."""
    return rx.accordion_item(
        rx.cond(
            item.link == url,
            sidebar_link(
                rx.text(item.names, style=heading_style2),
                _hover={"text_decoration": "none"},
                href=item.link,
            ),
            rx.cond(
                item.link == "",
                rx.heading(
                    rx.span("[ ", color="#DACEEE"),
                    item.names,
                    rx.span(" ]", color="#DACEEE"),
                    style=heading_style3,
                    margin_left="0em",
                    margin_top="0.5em",
                ),
                sidebar_link(
                    rx.text(
                        item.names,
                        color="#494369",
                        _hover={
                            "color": styles.ACCENT_COLOR,
                            "text_decoration": "none",
                        },
                        transition="color 0.4s ease-in-out",
                        padding_x="0.5em",
                        width="100%",
                    ),
                    _hover={"text_decoration": "none"},
                    href=item.link,
                ),
            ),
        ),
        padding_left=".5em",
        border="none",
        width="100%",
    )


@rx.memo
def sidebar_item_comp(
    item: SidebarItem,
    index: list[int],
    url: str,
):  
    return rx.cond(
        item.children.length() == 0,
        sidebar_leaf(item=item, url=url),
        rx.accordion_item(
            rx.accordion_button(
                rx.text(
                    item.names,
                    font_family=styles.SANS,
                    font_weight="500",
                ),
                rx.cond(
                    item.names == "Radix UI",
                    rx.text(
                        "Experimental",
                        color="#5646ED",
                        bg="#F5EFFE",
                        padding_x="0.5em",
                        border_radius="4px",
                        font_weight=600,
                        font_size=".8em",
                        margin_left="0.5em",
                    )
                ),
                rx.spacer(),
                rx.accordion_icon(),
                _hover={
                    "color": styles.ACCENT_COLOR,
                },
                color="#494369",
                width="100%",
                min_width="10em",
            ),
            rx.accordion_panel(
                rx.accordion(
                    rx.vstack(
                        rx.foreach(
                            item.children,
                            lambda child: sidebar_item_comp(
                                item=child,
                                index=index,
                                url=url,
                            ),
                        ),
                        align_items="start",
                        border_left="1px solid #F4F3F6",
                    ),
                    allow_multiple=True,
                    default_index=rx.cond(index, index[1:2], []),
                ),
                margin_left="0em",
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


def get_prev_next(url):
    """Get the previous and next links in the sidebar."""
    sidebar_items = learn + frontend + backend + hosting + component_lib
    # Flatten the list of sidebar items
    flat_items = []

    def append_to_items(items):
        for item in items:
            if len(item.children) == 0:
                flat_items.append(item)
            append_to_items(item.children)

    append_to_items(sidebar_items)
    for i, item in enumerate(flat_items):
        if item.link == url:
            if i == 0:
                return None, flat_items[i + 1]
            elif i == len(flat_items) - 1:
                return flat_items[i - 1], None
            else:
                return flat_items[i - 1], flat_items[i + 1]
    return None, None


def sidebar_category(name, color, index):
    return rx.box(
            rx.text(
                name,
                font_weight= fw["section"],
                font_size= styles.TEXT_FONT_SIZE,
                color= "#696287",  
            ),    
            on_click=lambda: SidebarState.set_sidebar_index(index),
            background=rx.cond(
                SidebarState.sidebar_index == index,
                "#F5EFFE",
                "transparent",
            ),
            align_items="left",
            padding_y="0.5em",
            padding_x="0.5em",
            border_radius="0.5em",
            border="2px solid #F4F3F6",
            width="100%",
        )

def sidebar_section(name):
    return rx.heading(
        rx.span("[ ", color="#DACEEE"),
        name,
        rx.span(" ]", color="#DACEEE"),
        style=heading_style3,
        margin_top="1em",
        margin_left="0em",
        padding_left="1em",
    )

def create_sidebar_section(section_title, items, index, url):
    return rx.vstack(
        sidebar_section(section_title),
        rx.accordion(
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
        ),
        padding_x="0em",
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
):
    return rx.vstack(
        sidebar_category("Learn", "red", 0),
        sidebar_category("Components", "red", 1),
        sidebar_category("API Reference", "red", 2),
        rx.divider(),
        rx.match(
            SidebarState.sidebar_index,
            (0, rx.vstack(
                create_sidebar_section("Onboarding", learn, learn_index, url),
                create_sidebar_section("UI", frontend, frontend_index, url),
                create_sidebar_section("State", backend, backend_index, url),
                create_sidebar_section("Hosting", hosting, hosting_index, url)
            )),
            (1, rx.vstack(
                create_sidebar_section("Core Components", component_lib, component_lib_index, url),
                create_sidebar_section("Other Libraries", other_libs, other_libs_index, url)         
            )),
            (2, rx.vstack(
                create_sidebar_section("API Reference", api_reference, api_reference_index, url),
                create_sidebar_section("Recipes", recipes, recipes_index, url),
                create_sidebar_section("Tutorials", tutorials, tutorials_index, url)       
            )),
        ),
        align_items="left",
        overflow_y="scroll",
        max_height="90%",
        width="17em",
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
        border_right= f"1px solid {rx.color('mauve', 11)};",
    )


def sidebar(url=None) -> rx.Component:
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

    return rx.box(
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
        ),
        width="100%",
    )


sb = sidebar()
