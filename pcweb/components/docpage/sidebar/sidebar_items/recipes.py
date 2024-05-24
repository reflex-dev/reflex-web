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
                recipes.layout.footer,
                recipes.layout.grid,
                recipes.layout.multi_column_row,
            ],
        ),
        create_item(
            "Content",
            children=[
                recipes.content.checkboxes,
                # recipes.content.search_bar,
            ],
        ),
        create_item(
            "Auth",
            children=[
                recipes.auth.login_form,
                recipes.auth.signup_form,
            ]
        ),
    ]


recipes = get_sidebar_items_recipes()
