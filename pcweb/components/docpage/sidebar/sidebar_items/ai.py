from .item import create_item


def get_sidebar_items_ai_builder_overview():
    from pcweb.pages.docs import ai_builder

    # !!! leave commented out sidebar items until they are filled out !!!

    return [
        create_item(
            "Overview",
            children=[
                ai_builder.overview.what_is_reflex_build,
                ai_builder.overview.best_practices,
                # ai_builder.overview.use_cases,
                # ai_builder.overview.quickstart,
                # ai_builder.overview.frequently_asked_questions,
            ],
        ),
        create_item(
            "Features",
            children=[
                ai_builder.features.image_as_prompt,
                ai_builder.features.templates,
                ai_builder.features.ide,
                ai_builder.features.environment_variables,
                ai_builder.features.installing_external_packages,
                ai_builder.features.download_app,
                ai_builder.features.deploy_app,
            ],
        ),
        create_item(
            "Prompting Guide",
            children=[
                # ai_builder.prompting.fixing_errors,
                ai_builder.prompting.breaking_up_complex_prompts,
            ],
        ),
        create_item(
            "Integrations",
            children=[
                ai_builder.integrations.github,
                ai_builder.integrations.database,
            ],
        ),
    ]


def get_sidebar_items_mcp():
    from pcweb.pages.docs import ai_builder

    return [
        create_item(
            "MCP Integration",
            children=[
                ai_builder.integrations.mcp_overview,
                ai_builder.integrations.mcp_installation,
            ],
        ),
    ]


ai_builder_overview_items = get_sidebar_items_ai_builder_overview()
mcp_items = get_sidebar_items_mcp()
