"""Logic for the sidebar component."""

from __future__ import annotations

import reflex as rx
from pcweb import styles
from pcweb.components.navbar import NavbarState
from pcweb.route import Route
from pcweb.styles import font_weights as fw
from pcweb.styles import text_colors as tc
from reflex.base import Base

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


class SidebarState(rx.State):
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
    return SidebarItem(
        names=route,
        children=list(map(create_item, children)),
    )


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
            "Tutorial",
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
        assets,
        components,
        library_,
        pages,
        styling,
        ui,
        wrapping_react,
    )

    items = [
        create_item(ui.overview),
        create_item(
            "Components",
            children=[
                components.props,
                components.style_props,
                components.conditional_props,
                components.conditional_rendering,
                components.rendering_iterables,
                library_,
            ],
        ),
        create_item(
            "Pages",
            children=[
                pages.routes,
                pages.dynamic_routing,
                pages.metadata,
            ],
        ),
        create_item(
            "Styling",
            children=[
                styling.overview,
                styling.responsive,
                styling.custom_stylesheets,
                styling.theming,
            ],
        ),
        create_item(
            "Assets",
            children=[
                assets.referencing_assets,
                assets.upload_and_download_files,
            ],
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
        api_routes,
        client_storage,
        database,
        events,
        state,
        substates,
        utility_methods,
        vars,
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
            "Substates",
            children=[
                substates.overview,
            ],
        ),
        create_item(
            "API Routes",
            children=[
                api_routes.overview,
            ],
        ),
        create_item(
            "Client Storage",
            children=[
                client_storage.overview,
            ],
        ),
        create_item(
            "Database",
            children=[
                database.overview,
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
    from pcweb.pages.docs import hosting

    items = [
        create_item(
            "Reflex Deploy",
            children=[
                hosting.deploy_quick_start,
                hosting.hosting_cli_commands,
            ],
        ),
        create_item(
            "Self Hosting",
            children=[hosting.self_hosting],
        ),
    ]
    return items


from reflex.components.chakra.base import ChakraComponent


def get_component_link(category, clist, prefix="") -> str:
    if issubclass(clist[1], ChakraComponent):
        prefix = "chakra/"
    component_name = rx.utils.format.to_snake_case(clist[0])
    return f"/docs/library/{prefix}{category.lower()}/{component_name.lower()}"


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
        component_name = rx.utils.format.to_snake_case(c[0])
        name = rx.utils.format.to_title_case(component_name)
        item = SidebarItem(
            names=name,
            link=get_component_link(category, c, prefix=prefix),
        )
        category_item_children.append(item)
    return SidebarItem(names=category, children=category_item_children)


def get_sidebar_items_reference():
    from pcweb.pages.docs import (
        api_reference,
        component_list,
        datatable_tutorial,
        recipes,
    )

    library_item_children = []

    for category in component_list:
        category_item = get_category_children(category, component_list[category])
        library_item_children.append(category_item)

    # children = [
    #     SidebarItem(
    #         names=module.__name__, link=f"/docs/api-reference/{module.__name__.lower()}"
    #     )
    #     for module in api_reference.modules
    # ]

    ref = create_item(
        "API Reference",
        children=[
            api_reference.cli,
            api_reference.event_triggers,
            api_reference.special_events,
            api_reference.browser_storage,
            api_reference.browser_javascript,
        ],
    )
    # ref.children.extend(children)

    return [
        SidebarItem(
            names="Overview",
            alt_name_for_next_prev="Components Reference: Overview",
            link="/docs/library",
        ),
        *library_item_children,
        ref,
        create_item(
            "Recipes",
            children=[
                recipes.navbar,
                recipes.sidebar,
                recipes.checkboxes,
                recipes.filtered_table,
            ],
        ),
        create_item(
            "Datatable Tutorial",
            children=[
                datatable_tutorial.simple_table,
                datatable_tutorial.add_interactivity,
                datatable_tutorial.add_styling,
                datatable_tutorial.live_stream,
            ],
        ),
    ]


def get_sidebar_items_other_libraries():
    from pcweb.pages.docs import radix_components

    chakra_children = []
    for category in radix_components:
        category_item = get_category_children(
            category, radix_components[category], prefix="radix/"
        )
        chakra_children.append(category_item)

    chakra_item = SidebarItem(names="Radix UI", children=chakra_children)

    return [chakra_item]


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
                margin_left=".7em",
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


learn = get_sidebar_items_learn()
reference = get_sidebar_items_reference()
frontend = get_sidebar_items_frontend()
backend = get_sidebar_items_backend()
hosting = get_sidebar_items_hosting()
other_libs = get_sidebar_items_other_libraries()


def get_prev_next(url):
    """Get the previous and next links in the sidebar."""
    sidebar_items = learn + frontend + backend + hosting + reference
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
    other_libs_index: list[int],
):
    return rx.vstack(
        rx.box(
            rx.text(
                "Learn",
                font_weight= fw["section"],
                font_size= styles.TEXT_FONT_SIZE,
                color= "#696287",  
            ),    
            on_click=lambda: SidebarState.set_sidebar_index(0),
            background=rx.cond(
                SidebarState.sidebar_index == 0,
                "#F5EFFE",
                "transparent",
            ),
            align_items="left",
            padding_y="0.5em",
            padding_x="0.5em",
            border_radius="0.5em",
            border="2px solid #F4F3F6",
            width="100%",
        ),
        rx.box(
            rx.text(
                "Reference",
                font_weight= fw["section"],
                font_size= styles.TEXT_FONT_SIZE,
                color= "#696287",  
            ), 
            on_click=lambda: SidebarState.set_sidebar_index(1),
            background=rx.cond(
                SidebarState.sidebar_index == 1,
                "#F5EFFE",
                "transparent",
            ),
            align_items="left",
            padding_y="0.5em",
            padding_x="0.5em",
            border_radius="0.5em",
            border="2px solid #F4F3F6",
            width="100%",
        ),
        rx.divider(),
        rx.cond(
            SidebarState.sidebar_index == 0,
            rx.vstack(
                sidebar_section("Onboarding"),
                rx.accordion(
                    *[
                        sidebar_item_comp(
                            item=item,
                            index=[-1],
                            url=url,
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
                        )
                        for item in frontend
                    ],
                    allow_multiple=True,
                    default_index=frontend_index if frontend_index is not None else [],
                    width="100%",
                ),
                sidebar_section("State"),
                rx.accordion(
                    *[
                        sidebar_item_comp(
                            item=item,
                            index=[-1],
                            url=url,
                        )
                        for item in backend
                    ],
                    allow_multiple=True,
                    default_index=backend_index if backend_index is not None else [],
                    width="100%",
                ),
                sidebar_section("Hosting"),
                rx.accordion(
                    *[
                        sidebar_item_comp(
                            item=item,
                            index=[-1],
                            url=url,
                        )
                        for item in hosting
                    ],
                    allow_multiple=True,
                    default_index=hosting_index if hosting_index is not None else [],
                    width="100%",
                ),
                padding_x="0em",
                width="100%",
                align_items="start",
            ),
            rx.vstack(
                sidebar_section("Core"),
                rx.accordion(
                    *[
                        sidebar_item_comp(item=item, url=url, index=reference_index)
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
                        sidebar_item_comp(item=item, url=url, index=other_libs_index)
                        for item in other_libs
                    ],
                    allow_multiple=True,
                    default_index=other_libs_index
                    if other_libs_index is not None
                    else [],
                ),
                padding_x="0em",
                width="100%",
                align_items="start",
            ),
        ),
        align_items="start",
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
    )


def sidebar(url=None) -> rx.Component:
    """Render the sidebar."""
    learn_index = calculate_index(learn, url)
    reference_index = calculate_index(reference, url)
    frontend_index = calculate_index(frontend, url)
    backend_index = calculate_index(backend, url)
    hosting_index = calculate_index(hosting, url)
    other_libs_index = calculate_index(other_libs, url)

    return rx.box(
        sidebar_comp(
            url=url,
            learn_index=learn_index,
            reference_index=reference_index,
            frontend_index=frontend_index,
            backend_index=backend_index,
            hosting_index=hosting_index,
            other_libs_index=other_libs_index,
        ),
        width="100%",
    )


sb = sidebar()
