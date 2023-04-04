"""Logic for the sidebar component."""

from __future__ import annotations

import inspect

import pynecone as pc
from pynecone.base import Base

from pcweb import styles
from pcweb.component_list import component_list
from pcweb.route import Route

# Sidebar styles.
heading_style = {
    "color": styles.DOC_REG_TEXT_COLOR,
    "font_weight": "500",
}
heading_style2 = {
    "font_size": styles.TEXT_FONT_SIZE,
    "color": styles.DOC_REG_TEXT_COLOR,
    "font_weight": "500",
}
heading_style3 = {
    "font_weight": styles.DOC_SECTION_FONT_WEIGHT,
    "font_size": styles.H3_FONT_SIZE,
    "color": styles.DOC_HEADER_COLOR,
    "margin_bottom": "0.5em",
    "margin_left": "1.1em",
}


class SidebarItem(Base):
    """A single item in the sidebar."""

    # The name to display in the sidebar.
    names: str = ""

    # The link to navigate to when the item is clicked.
    link: str = ""

    # The children items.
    children: list[SidebarItem] = []


def create_item(route: Route, children=None):
    """Create a sidebar item from a route."""
    if children is None:
        name = route.title.split(" | Pynecone")[0]
        if name.endswith("Overview"):
            name = "Overview"
        name = name.replace("Api", "API").replace("Cli", "CLI")
        return SidebarItem(names=name, link=route.path)
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
        advanced_guide,
        components,
        database,
        getting_started,
        hosting,
        state,
        styling,
    )

    items = [
        create_item(
            getting_started,
            children=[
                getting_started.introduction,
                getting_started.installation,
                getting_started.project_structure,
            ],
        ),
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
                advanced_guide.middleware,
                advanced_guide.telemetry,
            ],
        )
    )
    return items


def get_sidebar_items_reference():
    import pcweb.pages.docs.events_reference as event_ref
    from pcweb.pages.docs import recipes
    from pcweb.pages.docs import api_reference

    library_item = SidebarItem(
        names="Components",
        children=[
            SidebarItem(names="Overview", link="/docs/library"),
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
    return [
        library_item,
        create_item(
            event_ref,
            children=[
                event_ref.triggers,
                event_ref.server_side,
            ],
        ),
        create_item(
            recipes,
            children=[
                recipes.navbar,
                recipes.sidebar,
            ],
        ),
        create_item(
            api_reference,
            children=[
                api_reference.cli,
            ],
        ),
    ]


@pc.memo
def sidebar_leaf(
    item: SidebarItem,
    url: str,
) -> pc.Component:
    """Get the leaf node of the sidebar."""
    return pc.accordion_item(
        pc.cond(
            item.link == url,
            pc.link(
                item.names,
                href=item.link,
                color=styles.ACCENT_COLOR,
                _hover={"color": styles.ACCENT_COLOR},
            ),
            pc.link(
                item.names,
                href=item.link,
                color=styles.DOC_REG_TEXT_COLOR,
                _hover={"color": styles.ACCENT_COLOR},
            ),
        ),
        padding_left="1em",
        border="none",
    )


@pc.memo
def sidebar_item_comp(
    item: SidebarItem,
    index: list[int],
    url: str,
    first: bool,
):
    return pc.fragment(
        pc.cond(
            item.children.length() == 0,
            sidebar_leaf(item=item, url=url),
            pc.accordion_item(
                pc.cond(
                    first,
                    pc.accordion_button(
                        pc.accordion_icon(),
                        pc.text(
                            item.names,
                            font_family="Inter",
                            font_size="1em",
                        ),
                        padding_y="0.5em",
                        _hover={
                            "color": styles.ACCENT_COLOR,
                        },
                    ),
                    pc.accordion_button(
                        pc.accordion_icon(),
                        pc.text(
                            item.names,
                            font_family="Inter",
                            font_size="1em",
                        ),
                        padding_y="0.2em",
                        _hover={
                            "color": styles.ACCENT_COLOR,
                        },
                    ),
                ),
                pc.accordion_panel(
                    pc.accordion(
                        pc.vstack(
                            pc.foreach(
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
                        allow_toggle=True,
                        allow_multiple=True,
                        default_index=pc.cond(index, index[1:2], []),
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
reference = get_sidebar_items_reference()


def get_prev_next(url):
    """Get the previous and next links in the sidebar."""
    sidebar_items = learn + reference
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


@pc.memo
def sidebar_comp(
    url: str,
    learn_index: list[int],
    reference_index: list[int],
):
    from pcweb.pages.docs.gallery import gallery

    return pc.box(
        pc.heading("Learn", style=heading_style3),
        pc.accordion(
            *[
                sidebar_item_comp(
                    item=item,
                    index=[-1],
                    url=url,
                    first=True,
                )
                for item in learn
            ],
            allow_toggle=True,
            allow_multiple=True,
            default_index=learn_index,
        ),
        pc.divider(
            margin_bottom="1em",
            margin_top="0.5em",
        ),
        pc.heading("Reference", style=heading_style3),
        pc.accordion(
            *[
                sidebar_item_comp(item=item, url=url, first=True, index=reference_index)
                for item in reference
            ],
            allow_toggle=True,
            allow_multiple=True,
            default_index=reference_index,
        ),
        pc.vstack(
            pc.link(
                pc.hstack(
                    pc.icon(tag="minus", height=".75rem", style=heading_style),
                    pc.text(
                        "Gallery",
                        style={
                            "color": styles.DOC_REG_TEXT_COLOR,
                            "_hover": {"color": styles.ACCENT_COLOR},
                        },
                        font_family="Inter",
                    ),
                ),
                href=gallery.path,
            ),
            align_items="left",
            margin_left="1.3em",
            margin_top="0.5em",
        ),
        align_items="start",
        overflow_y="scroll",
        max_height="90%",
        padding_bottom="6em",
        padding_right="4em",
        position="fixed",
        scroll_padding="4em",
    )


def sidebar(url=None) -> pc.Component:
    """Render the sidebar."""
    learn_index = calculate_index(learn, url)
    reference_index = calculate_index(reference, url)
    return pc.box(
        sidebar_comp(
            url=url,
            learn_index=learn_index,
            reference_index=reference_index,
        ),
    )
