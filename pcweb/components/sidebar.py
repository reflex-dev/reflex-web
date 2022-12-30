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
    name: str

    # The link to navigate to when the item is clicked.
    link: str = ""

    # The children items.
    children: list[SidebarItem] = []


def create_item(route: Route, children=None):
    """Create a sidebar item from a route."""
    if children is None:
        name = route.title.split(" | Pynecone")[0]
        return SidebarItem(name=name, link=route.path)
    return SidebarItem(
        name=inspect.getmodule(route).__name__.split(".")[-1].replace("_", " ").title(),
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
                styling.fonts,
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
                advanced_guide.middleware,
                advanced_guide.wrapping_react,
            ],
        )
    )
    return items


def get_sidebar_items_examples():
    import pcweb.pages.docs.events_reference as event_ref

    library_item = SidebarItem(
        name="Components",
        children=[
            SidebarItem(name="Overview", link="/docs/library"),
            *[
                SidebarItem(
                    name=category,
                    children=[
                        SidebarItem(
                            name=c[0].__name__,
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
    ]


def render_sidebar_item(
    item: SidebarItem,
    heading_style=heading_style,
    url=None,
    first=False,
    index=None,
) -> pc.Component:
    text_style = {
        "color": styles.DOC_REG_TEXT_COLOR,
        "_hover": {"color": styles.ACCENT_COLOR},
    }
    if item.link == url:
        text_style = {
            "color": styles.ACCENT_COLOR,
            "_hover": {"color": styles.ACCENT_COLOR},
        }
    item_name = item.name

    def format_item_name(name):
        if name.endswith("Overview"):
            return "Overview"
        return name

    if len(item.children) == 0:
        return pc.accordion_item(
            pc.link(
                format_item_name(item_name),
                style=text_style,
                href=item.link,
            ),
            padding_left="1em",
            border="none",
        )
    return pc.accordion_item(
        pc.accordion_button(
            pc.accordion_icon(),
            pc.text(
                item_name,
                font_size="1em",
            ),
            padding_y="0.5em" if first else "0.25em",
            **heading_style,
            _hover={
                "color": styles.ACCENT_COLOR,
            },
        ),
        pc.accordion_panel(
            pc.accordion(
                pc.vstack(
                    *[
                        render_sidebar_item(item, heading_style=heading_style2, url=url)
                        for item in item.children
                    ],
                    align_items="start",
                    border_left="1px solid #e0e0e0",
                ),
                allow_toggle=True,
                allow_multiple=True,
                default_index=[index[0] if index else None],
            ),
            margin_left="1em",
        ),
        border="none",
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


def get_prev_next(url, sidebar_items=None):
    """Get the previous and next links in the sidebar."""
    sidebar_items = sidebar_items or get_sidebar_items_learn()
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


def sidebar(url=None, **props) -> pc.Component:
    """Render the sidebar."""
    from pcweb.pages.docs.gallery import gallery

    learn = get_sidebar_items_learn()
    learn_index = calculate_index(learn, url)

    examples = get_sidebar_items_examples()
    examples_index = calculate_index(examples, url)
    return pc.box(
        pc.heading("Learn", style=heading_style3),
        pc.accordion(
            *[
                render_sidebar_item(
                    item,
                    url=url,
                    first=True,
                    index=learn_index[1:]
                    if learn_index is not None and i == learn_index[0]
                    else None,
                )
                for i, item in enumerate(learn)
            ],
            allow_toggle=True,
            allow_multiple=True,
            default_index=[learn_index[0] if learn_index is not None else None],
        ),
        pc.divider(),
        pc.heading("Reference", style=heading_style3),
        pc.accordion(
            *[
                render_sidebar_item(
                    item,
                    url=url,
                    first=True,
                    index=examples_index[1:]
                    if examples_index is not None and i == examples_index[0]
                    else None,
                )
                for i, item in enumerate(examples)
            ],
            allow_toggle=True,
            allow_multiple=True,
            default_index=[examples_index[0] if examples_index is not None else None],
        ),
        pc.vstack(
            pc.link(
                pc.hstack(
                    pc.icon(tag="MinusIcon", height=".75rem", style=heading_style),
                    pc.text(
                        "Gallery",
                        style={
                            "color": styles.DOC_REG_TEXT_COLOR,
                            "_hover": {"color": styles.ACCENT_COLOR},
                        },
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
        padding_right="4em",
        padding_bottom="4em",
        **props,
    )
