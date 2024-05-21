from .item import create_item, SidebarItem


def get_sidebar_items_recipes():
    from pcweb.pages.docs import (
        recipes,
    )
    from pcweb.pages.docs.recipes_overview import (
        overview,
    )

    return [
        create_item(overview),
        create_item(
            "Layout",
            children=[
                recipes.layout.navbar,
                recipes.layout.sidebar,
            ],
        ),
        create_item(
            "interactive",
            children=[
                recipes.interactive.checkboxes,
            ],
        ),
    ]



recipes = get_sidebar_items_recipes()