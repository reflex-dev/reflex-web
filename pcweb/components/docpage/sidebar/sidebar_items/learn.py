from .item import create_item


def get_sidebar_items_learn():
    from pcweb.pages.docs import (
        getting_started,
        tutorial,
    )

    items = [
        create_item(
            "Getting Started",
            children=[
                getting_started.installation,
                getting_started.introduction,
                getting_started.project_structure,
                getting_started.configuration,
                getting_started.how_reflex_works,
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
        custom_components,
    )

    items = [
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
                styling.theming,
                styling.responsive,
                styling.custom_stylesheets,
                styling.layout,
                styling.common_props,
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
                wrapping_react.guide,
                wrapping_react.example,
            ],
        ),
        create_item(
            "Custom Components",
            children=[
                custom_components.overview,
                custom_components.prerequisites_for_publishing,
                custom_components.command_reference,
            ],
        ),
    ]
    return items


def get_sidebar_items_backend():
    from pcweb.pages.docs import (
        api_routes,
        authentication,
        client_storage,
        database,
        events,
        state,
        substates,
        utility_methods,
        vars,
    )

    items = [
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
                events.event_actions,
            ],
        ),
        create_item(
            "Substates",
            children=[
                substates.overview,
                substates.component_state,
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
            "Authentication",
            children=[
                authentication.authentication_overview,
            ],
        ),
        create_item(
            "Utility Methods",
            children=[
                utility_methods.router_attributes,
                utility_methods.lifespan_tasks,
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


learn = get_sidebar_items_learn()
frontend = get_sidebar_items_frontend()
backend = get_sidebar_items_backend()
hosting = get_sidebar_items_hosting()
