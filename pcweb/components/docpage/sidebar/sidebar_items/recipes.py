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
            "Example",
            children=[
                recipes.navbar,
                recipes.sidebar,
                recipes.checkboxes,
                recipes.filtered_table,
            ],
        )
    ]



recipes = get_sidebar_items_recipes()