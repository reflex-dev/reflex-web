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
                recipes.interactive.search_bar,
            ],
        ),
        create_item(
            "user-profiles",
            children=[
                recipes.user_profiles.account_setting,
                recipes.user_profiles.login_form,
                recipes.user_profiles.portfolio,
            ]
        ),
        create_item(
            "e-commerce",
            children=[
                recipes.e_commerce.order_summary,
                recipes.e_commerce.payment_integration,
                recipes.e_commerce.product_card,
            ]
        )
    ]



recipes = get_sidebar_items_recipes()