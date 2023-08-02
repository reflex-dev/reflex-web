"""Logic for the sidebar component."""

from __future__ import annotations

import inspect

import reflex as rx
from pcweb import styles
from pcweb.component_list import component_list
from pcweb.route import Route
from reflex.base import Base
from pcweb.styles import font_weights as fw

from pcweb.styles import text_colors as tc

# Sidebar styles.
heading_style = {
    "color": "#494369",
    "font_weight": "500",
}
heading_style2 = {
    "font_size": styles.TEXT_FONT_SIZE,
    "color": "#5646ED",
    "background_color": "#F5EFFE",
    "border_radius": "0.5em",
    "font_weight": "500",
    "width": "100%",
    "padding_x": "0.5em",
    "padding_y": "0.25em",
}
heading_style3 = {
    "font_weight": fw["section"],
    "font_size": styles.H4_FONT_SIZE,
    "color": "#696287",
    "margin_bottom": "0.5em",
    "margin_left": "1.1em",
}


class SidebarItem(Base):
    """A single item in the sidebar."""

    # The name to display in the sidebar.
    names: str = ""

    alt_name_for_next_prev: str = ""

    # The link to navigate to when the item is clicked.
    link: str = ""

    # The children items.
    children: list[SidebarItem] = []


def create_item(route: Route, children=None):
    """Create a sidebar item from a route."""
    if children is None:
        name = route.title.split(" | Reflex")[0]
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
        names=inspect.getmodule(route)
        .__name__.split(".")[-1]
        .replace("_", " ")
        .title()
        .replace("Api", "API"),
        children=list(map(create_item, children)),
    )


def get_sidebar_items_learn():
    from pcweb.pages.docs import (
        getting_started,
        tutorial,
    )

    items = [
        create_item(
            getting_started,
            children=[
                getting_started.introduction,
                getting_started.installation,
                getting_started.project_structure,
                getting_started.configuration,
            ],
        ),
        create_item(
            tutorial,
            children=[
                tutorial.intro,
                tutorial.starting_point,
                tutorial.adding_state,
                tutorial.chat_history,
                tutorial.deployment,
            ],
        ),
    ]
    return items


def get_sidebar_items_concepts():
    from pcweb.pages.docs import (
        advanced_guide,
        components,
        database,
        hosting,
        state,
        styling,
    )

    items = [
        create_item(
            components,
            children=[
                components.components_overview,
                components.props,
                components.pages,
                components.assets,
            ],
        ),
        create_item(
            state,
            children=[
                state.state_overview,
                state.vars,
                state.events,
                state.substates,
                state.utility_methods,
            ],
        ),
        create_item(
            styling,
            children=[
                styling.styling_overview,
                styling.responsive,
                styling.custom_stylesheets,
                styling.theming,
            ],
        ),
        create_item(
            database,
            children=[
                database.database_overview,
                database.tables,
                database.queries,
            ],
        ),
        create_item(
            hosting,
            children=[
                hosting.deploy,
                hosting.self_hosting,
            ],
        ),
    ]
    items.append(
        create_item(
            advanced_guide,
            children=[
                advanced_guide.custom_vars,
                advanced_guide.memoization,
                advanced_guide.wrapping_react,
                advanced_guide.api_routes,
                advanced_guide.use_middleware,
                advanced_guide.telemetry,
            ],
        )
    )
    return items


def get_sidebar_items_reference():
    from pcweb.pages.docs import recipes
    from pcweb.pages.docs import api_reference

    library_item = SidebarItem(
        names="Components",
        children=[
            SidebarItem(
                names="Overview",
                alt_name_for_next_prev="Components Reference: Overview",
                link="/docs/library",
            ),
            *[
                SidebarItem(
                    names=category,
                    children=[
                        SidebarItem(
                            names=c[0].__name__,
                            link=f"/docs/library/{category.lower()}/{c[0].__name__.lower()}",
                        )
                        for c in component_list[category]
                    ],
                )
                for category in component_list
            ],
        ],
    )

    children = [
        SidebarItem(
            names=module.__name__, link=f"/docs/api-reference/{module.__name__.lower()}"
        )
        for module in api_reference.modules
    ]

    ref = create_item(
        api_reference,
        children=[
            api_reference.cli,
            api_reference.event_triggers,
            api_reference.special_events,
            api_reference.browser,
        ],
    )
    ref.children.extend(children)

    return [
        library_item,
        ref,
        create_item(
            recipes,
            children=[
                recipes.navbar,
                recipes.sidebar,
                recipes.checkboxes,
            ],
        ),
    ]


@rx.memo
def sidebar_leaf(
    item: SidebarItem,
    url: str,
) -> rx.Component:
    """Get the leaf node of the sidebar."""
    return rx.accordion_item(
        rx.cond(
            item.link == url,
            rx.link(
                rx.text(item.names, style=heading_style2),
                href=item.link,
            ),
            rx.link(
                rx.text(
                    item.names,
                    color=tc["docs"]["body"],
                    _hover={"color": styles.ACCENT_COLOR},
                    padding_x="0.5em",
                ),
                href=item.link,
            ),
        ),
        padding_left="1em",
        border="none",
        width="100%",
    )


@rx.memo
def sidebar_item_comp(
    item: SidebarItem,
    index: list[int],
    url: str,
    first: bool,
):
    return rx.fragment(
        rx.cond(
            item.children.length() == 0,
            sidebar_leaf(item=item, url=url),
            rx.accordion_item(
                rx.accordion_button(
                    rx.box(rx.accordion_icon(), opacity="0.6"),
                    rx.text(
                        item.names,
                        font_family=styles.SANS,
                    ),
                    _hover={
                        "color": styles.ACCENT_COLOR,
                    },
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
                                    first=False,
                                ),
                            ),
                            align_items="start",
                            border_left="1px solid #e0e0e0",
                        ),
                        allow_multiple=True,
                        default_index=rx.cond(index, index[1:2], []),
                    ),
                    margin_left="1em",
                ),
                border="none",
            ),
        )
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


learn = get_sidebar_items_learn()
concepts = get_sidebar_items_concepts()
reference = get_sidebar_items_reference()


def get_prev_next(url):
    """Get the previous and next links in the sidebar."""
    sidebar_items = learn + concepts + reference
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


signle_item = {
    "color": tc["docs"]["body"],
    "_hover": {"color": styles.ACCENT_COLOR},
    "font_family": styles.SANS,
}


@rx.memo
def sidebar_comp(
    url: str,
    learn_index: list[int],
    concepts_index: list[int],
    reference_index: list[int],
):
    from pcweb.pages.docs.gallery import gallery

    return rx.box(
        rx.heading(
            rx.span("[ ", color="#DACEEE"),
            "Learn",
            rx.span(" ]", color="#DACEEE"),
            style=heading_style3,
        ),
        rx.accordion(
            *[
                sidebar_item_comp(
                    item=item,
                    index=[-1],
                    url=url,
                    first=True,
                )
                for item in learn
            ],
            allow_multiple=True,
            default_index=learn_index,
        ),
        rx.heading(
            rx.span("[ ", color="#DACEEE"),
            "Concepts",
            rx.span(" ]", color="#DACEEE"),
            style=heading_style3,
            margin_top="1em",
        ),
        rx.accordion(
            *[
                sidebar_item_comp(
                    item=item,
                    index=[-1],
                    url=url,
                    first=True,
                )
                for item in concepts
            ],
            allow_multiple=True,
            default_index=concepts_index,
        ),
        rx.heading(
            rx.span("[ ", color="#DACEEE"),
            "Reference",
            rx.span(" ]", color="#DACEEE"),
            style=heading_style3,
            margin_top="1em",
        ),
        rx.accordion(
            *[
                sidebar_item_comp(item=item, url=url, first=True, index=reference_index)
                for item in reference
            ],
            allow_multiple=True,
            default_index=reference_index,
        ),
        align_items="start",
        overflow_y="scroll",
        max_height="90%",
        padding_bottom="6em",
        padding_right="4em",
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


def sidebar(url=None) -> rx.Component:
    """Render the sidebar."""
    learn_index = calculate_index(learn, url)
    concepts_index = calculate_index(concepts, url)
    reference_index = calculate_index(reference, url)
    return rx.box(
        sidebar_comp(
            url=url,
            learn_index=learn_index,
            concepts_index=concepts_index,
            reference_index=reference_index,
        ),
        padding_right="2em",
    )
