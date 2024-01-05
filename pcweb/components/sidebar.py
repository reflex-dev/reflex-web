"""Logic for the sidebar component."""

from __future__ import annotations

import inspect

import reflex as rx
from pcweb import styles
from pcweb.base_state import State
from pcweb.components.navbar import NavbarState
from pcweb.component_list import component_list, chakra_components
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
    "font_size": styles.TEXT_FONT_SIZE,
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


class SidebarState(State):

    _sidebar_index: int = -1

    def set_sidebar_index(self, num) -> int:
        self._sidebar_index = num

    @rx.cached_var
    def sidebar_index(self) -> int:
        if self._sidebar_index < 0:
            route = self.router.page.path
            if "library" in route or "api-reference" in route or "recipe" in route:
                return 1
            else:
                return 0
        return self._sidebar_index

def sidebar_section(name):
    return rx.heading(
        rx.span("[ ", color="#DACEEE"),
        name,
        rx.span(" ]", color="#DACEEE"),
        style=heading_style3,
        margin_top="1em",
    )

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
    try:
        return SidebarItem(
            names=route if isinstance(route, str) else 
            inspect.getmodule(route)
            .__name__.split(".")[-1]
            .replace("_", " ")
            .title()
            .replace("Api", "API"),
            children=list(map(create_item, children)),
        )
    except:
        breakpoint()


def get_sidebar_items_learn():
    from pcweb.pages.docs import (
        getting_started,
        tutorial,
    )

    items = [
        create_item(
            "Getting Started",
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
                tutorial.setup,
                tutorial.frontend,
                tutorial.adding_state,
                tutorial.final_app,
            ],
        ),
    ]
    return items


def get_sidebar_items_frontend():
    from pcweb.pages.docs import (
        ui_overview,
        components,
        pages,
        styling,
        assets,
        wrapping_react,
        library,
    )
 
    items = [
        create_item(ui_overview),
        create_item(
            "Components",
            children=[
                components.props,
                components.style_props,
                components.conditional_props,
                components.conditional_rendering,
                components.rendering_iterables,
                library,
            ],
        ),
        create_item(
            pages,
            children=[
                pages.routes,
                pages.dynamic_routing,
                pages.metadata,
            ]
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
            assets,
            children=[
                assets.referencing_assets,
                assets.upload_and_download_files,
            ]
        ),
        create_item(
            "Wrapping React",
            children=[
                wrapping_react.overview,
                wrapping_react.imports,
                wrapping_react.logic,
                wrapping_react.example,
            ],
        ),
    ]
    return items


def get_sidebar_items_backend():
    from pcweb.pages.docs import (
        state,
        events,
        vars,
        substates,
        api_routes,
        client_storage,
        utility_methods,
        database,
    )

    items = [
        create_item(state.overview),
        create_item(
            "Vars",
            children=[
                vars.base_vars,
                vars.computed_vars,
                vars.var_operations,
                vars.custom_vars,
            ],
        ),
        create_item(
            "Events",
            children=[
                events.events_overview,
                events.event_arguments,
                events.setters,
                events.yield_events,
                events.chaining_events,
                events.special_events,
                events.page_load_events,
                events.background_events,
            ],
        ),
        create_item(
            substates,
            children=[
                substates.substates_overview,
            ],
        ),
        create_item(
            api_routes,
            children=[
                api_routes.api_routes_overview,
            ],
        ),
        create_item(
            "Client Storage",
            children=[
                client_storage.overview,
            ],
        ),
        create_item(
            database,
            children=[
                database.database_overview,
                database.tables,
                database.queries,
                database.relationships,
            ],
        ),
        create_item(
            "Utility Methods",
            children=[
                utility_methods.files_router_methods,
                utility_methods.other_methods,
            ],
        ),
    ]
    return items


def get_sidebar_items_hosting():
    from pcweb.pages.docs import (
        hosting,
    )
    items = [
        create_item(hosting.deploy),
        create_item(hosting.self_hosting),
    ]
    return items


def get_sidebar_items_other():
    from pcweb.pages.docs import (
        advanced_guide,
    )

    items = [
        create_item(
            advanced_guide,
            children=[
                advanced_guide.memoization,
                advanced_guide.use_middleware,
                advanced_guide.telemetry,
            ],
        )
    ]

    return items


def get_category_children(category, category_list, prefix=""):
    if isinstance(category_list, dict):
        return SidebarItem(
            names=category,
            children=[
                get_category_children(c, category_list[c]) for c in category_list
            ],
        )
    category_item_children = []
    for c in category_list:
        if isinstance(c[0], str):
            category_name = c[0]
            item = SidebarItem(names=category_name, children=[])
        else:
            component_name = c[0].__name__
            component_link = (
                f"/docs/library/{prefix}{category.lower()}/{component_name.lower()}"
            )
            item = SidebarItem(
                names=component_name.replace("Chart", "").replace("X", ""),
                link=component_link,
            )
        category_item_children.append(item)
    return SidebarItem(names=category, children=category_item_children)


def get_sidebar_items_reference():
    from pcweb.pages.docs import datatable_tutorial
    from pcweb.pages.docs import recipes
    from pcweb.pages.docs import api_reference

    library_item_children = []

    for category in component_list:
        category_item = get_category_children(category, component_list[category])
        library_item_children.append(category_item)

    library_item = SidebarItem(
        names="Components",
        children=[
            SidebarItem(
                names="Overview",
                alt_name_for_next_prev="Components Reference: Overview",
                link="/docs/library",
            ),
            *library_item_children,
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
            api_reference.browser_storage,
            api_reference.browser_javascript,
        ],
    )
    ref.children.extend(children)

    return [
        SidebarItem(
            names="Overview",
            alt_name_for_next_prev="Components Reference: Overview",
            link="/docs/library",
        ),
        *library_item_children,
        # library_item,
        # ref,
        # create_item(
        #     recipes,
        #     children=[
        #         recipes.navbar,
        #         recipes.sidebar,
        #         recipes.checkboxes,
        #         recipes.filtered_table,
        #     ],
        # ),
        # create_item(
        #     datatable_tutorial,
        #     children=[
        #         datatable_tutorial.simple_table,
        #         datatable_tutorial.add_interactivity,
        #         datatable_tutorial.add_styling,
        #         datatable_tutorial.live_stream,
        #     ],
        # ),
    ]

def get_sidebar_items_other_libraries():

    chakra_children = []
    for category in chakra_components:
        category_item = get_category_children(category, chakra_components[category], prefix="chakra/")
        chakra_children.append(category_item)

    chakra_item = SidebarItem(
        names="Chakra UI",
        children=chakra_children
    )

    return [
        chakra_item
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
                    rx.spacer(),
                    rx.accordion_icon(),
                    _hover={
                        "color": styles.ACCENT_COLOR,
                    },
                    color="#494369",
                    width="100%",
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
                            border_left="1px solid #F4F3F6",
                        ),
                        allow_multiple=True,
                        default_index=rx.cond(index, index[1:2], []),
                    ),
                    margin_left=".7em",
                    width="100%"
                ),
                border="none",
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


learn = get_sidebar_items_learn()
reference = get_sidebar_items_reference()
frontend = get_sidebar_items_frontend()
backend = get_sidebar_items_backend()
hosting = get_sidebar_items_hosting()
other = get_sidebar_items_other()
other_libs = get_sidebar_items_other_libraries()


def get_prev_next(url):
    """Get the previous and next links in the sidebar."""
    sidebar_items = learn + frontend + backend + hosting + other + reference
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
    reference_index: list[int],
    frontend_index: list[int],
    backend_index: list[int],
    hosting_index: list[int],
    other_index: list[int],
    other_libs_index: list[int],
):
    return rx.vstack(
        rx.tabs(
            rx.tab_list(
                rx.tab(
                    rx.hstack(
                        rx.image(src="/icons/doc.svg", height="1em"),
                        rx.text("Learn"),
                        on_click=lambda: SidebarState.set_sidebar_index(0),
                    ),
                    color="#494369",
                    padding_left="0em",
                ),
                rx.tab(
                    rx.hstack(
                        rx.image(src="/icons/ref.svg", height="1em"),
                        rx.text("Reference"),
                        on_click=lambda: SidebarState.set_sidebar_index(1),
                    ),
                    padding_left="0em",
                    color="#494369",
                ),
                color="#494369",
                margin_left="1.1em",
                align="left",
                font_weight="450",
            ),
            rx.tab_panels(
                rx.tab_panel(
                    sidebar_section("Onboarding"),
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
                        default_index=learn_index if learn_index is not None else [],
                        width="100%",
                    ),
                    sidebar_section("UI"),
                    rx.accordion(
                        *[
                            sidebar_item_comp(
                                item=item,
                                index=[-1],
                                url=url,
                                first=True,
                            )
                            for item in frontend
                        ],
                        allow_multiple=True,
                        default_index=frontend_index
                        if frontend_index is not None
                        else [],
                        width="100%",
                    ),
                    sidebar_section("State"),
                    rx.accordion(
                        *[
                            sidebar_item_comp(
                                item=item,
                                index=[-1],
                                url=url,
                                first=True,
                            )
                            for item in backend
                        ],
                        allow_multiple=True,
                        default_index=backend_index
                        if backend_index is not None
                        else [],
                        width="100%",
                    ),
                    sidebar_section("Hosting"),
                    rx.accordion(
                        *[
                            sidebar_item_comp(
                                item=item,
                                index=[-1],
                                url=url,
                                first=True,
                            )
                            for item in hosting
                        ],
                        allow_multiple=True,
                        default_index=hosting_index if hosting_index is not None else [],
                        width="100%",
                    ),
                    sidebar_section("Other"),
                    rx.accordion(
                        *[
                            sidebar_item_comp(
                                item=item,
                                index=[-1],
                                url=url,
                                first=True,
                            )
                            for item in other
                        ],
                        allow_multiple=True,
                        default_index=other_index if other_index is not None else [],
                    ),
                    padding_x="0em",
                    width="100%",
                ),
                rx.tab_panel(
                    sidebar_section("Core"),
                    rx.accordion(
                        *[
                            sidebar_item_comp(
                                item=item, url=url, first=True, index=reference_index
                            )
                            for item in reference
                        ],
                        allow_multiple=True,
                        default_index=reference_index
                        if reference_index is not None
                        else [],
                    ),
                    sidebar_section("Other Libraries"),
                    rx.accordion(
                        *[
                            sidebar_item_comp(
                                item=item, url=url, first=True, index=other_libs_index
                            )
                            for item in other_libs
                        ],
                        allow_multiple=True,
                        default_index=other_libs_index
                        if other_libs_index is not None
                        else [],
                    ),
                    padding_x="0em",
                    width="100%",
                ),
                width="100%",
            ),
            index=SidebarState.sidebar_index,
            width="100%",
        ),
        align_items="start",
        overflow_y="scroll",
        max_height="90%",
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


def sidebar(url=None) -> rx.Component:
    """Render the sidebar."""
    learn_index = calculate_index(learn, url)
    reference_index = calculate_index(reference, url)
    frontend_index = calculate_index(frontend, url)
    backend_index = calculate_index(backend, url)
    hosting_index = calculate_index(hosting, url)
    other_index = calculate_index(other, url)
    other_libs_index = calculate_index(other_libs, url)



    return rx.box(
        sidebar_comp(
            url=url,
            learn_index=learn_index,
            reference_index=reference_index,
            frontend_index=frontend_index,
            backend_index=backend_index,
            hosting_index=hosting_index,
            other_index=other_index,
            other_libs_index=other_libs_index,
        ),
    )


sb = sidebar()
