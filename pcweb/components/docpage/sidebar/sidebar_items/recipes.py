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
                recipes.content.checkboxes,
                recipes.content.search_bar,
            ],
        ),
        create_item(
            "user-profiles",
            children=[
                recipes.auth.account_setting,
                recipes.auth.login_form,
                recipes.auth.portfolio,
            ]
        ),
        create_item(
            "e-commerce",
            children=[
                recipes.others.order_summary,
                recipes.others.payment_integration,
                recipes.others.product_card,
            ]
        )
    ]



recipes = get_sidebar_items_recipes()