from .item import create_item, SidebarItem


def get_sidebar_items_recipes():
    from pcweb.pages.docs import (
        recipes,
    )

    return [
        create_item(
            "Overview",
            children=[
                recipes.navbar,
                recipes.sidebar,
                recipes.checkboxes,
                recipes.filtered_table,
            ],
        )
    ]



recipes = get_sidebar_items_recipes()