from .item import create_item


def get_sidebar_items_ai_builder_overview():
    from pcweb.pages.docs import (
        ai_builder,
    )

    return [
        create_item(
            "Overview",
            children=[
                ai_builder.overview,
            ],
        ),
    ]


def get_sidebar_items_ai_builder_integrations():
    from pcweb.pages.docs import (
        ai_builder,
    )

    return [
        create_item(
            "Integrations",
            children=[
                ai_builder.integrations,
            ],
        ),
    ]


ai_builder_overview_items = get_sidebar_items_ai_builder_overview()
ai_builder_integrations_items = get_sidebar_items_ai_builder_integrations()
