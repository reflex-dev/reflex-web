from .item import create_item, SidebarItem


def get_sidebar_items_api_reference():
    from pcweb.pages.docs import api_reference, apiref

    return [
        create_item(
            "API Reference",
            children=[
                api_reference.cli,
                api_reference.event_triggers,
                api_reference.special_events,
                api_reference.browser_storage,
                api_reference.browser_javascript,
            ]
            + apiref.pages,
        )
    ]


def get_sidebar_items_recipes():
    from pcweb.pages.docs import (
        recipes,
    )

    return [
        create_item(
            "Recipes",
            children=[
                recipes.navbar,
                recipes.sidebar,
                recipes.checkboxes,
                recipes.filtered_table,
            ],
        )
    ]


def get_sidebar_items_tutorials():
    from pcweb.pages.docs import (
        datatable_tutorial,
    )

    return [
        create_item(
            "Datatable Tutorial",
            children=[
                datatable_tutorial.simple_table,
                datatable_tutorial.add_interactivity,
                datatable_tutorial.add_styling,
                datatable_tutorial.live_stream,
            ],
        )
    ]


api_reference = get_sidebar_items_api_reference()
recipes = get_sidebar_items_recipes()
tutorials = get_sidebar_items_tutorials()
