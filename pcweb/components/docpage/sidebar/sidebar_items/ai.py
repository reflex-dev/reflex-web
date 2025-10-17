from .item import create_item


def get_sidebar_items_ai_builder_overview():
    from pcweb.pages.docs import ai_builder

    return [
        create_item(
            "Overview",
            children=[
                ai_builder.overview.best_practices,
                ai_builder.overview.what_is_reflex_build,
                ai_builder.overview.tutorial,
                ai_builder.overview.templates,
            ],
        ),
        create_item(
            "Features",
            children=[
                ai_builder.features.ide,
                ai_builder.features.editor_modes,
                ai_builder.features.file_tree,
                ai_builder.features.restore_checkpoint,
                ai_builder.features.secrets,
                ai_builder.features.installing_external_packages,
                ai_builder.features.integration_shortcut,
                ai_builder.features.knowledge,
                ai_builder.features.image_as_prompt,
                ai_builder.features.interaction_modes,
                ai_builder.features.automated_testing,
                ai_builder.features.customization,
            ],
        ),
        create_item(
            "App Lifecycle",
            children=[
                ai_builder.app_lifecycle.general,
                ai_builder.app_lifecycle.fork_app,
                ai_builder.app_lifecycle.deploy_app,
                ai_builder.app_lifecycle.download_app,
                ai_builder.app_lifecycle.copy_app,
                ai_builder.app_lifecycle.share_app,
            ],
        ),
        # create_item(
        #     "Integrations",
        #     children=[
        #         ai_builder.integrations.overview,
        #         ai_builder.integrations.github,
        #         ai_builder.integrations.database,
        #         ai_builder.integrations.databricks,
        #         ai_builder.integrations.azure_auth,
        #         ai_builder.integrations.okta_auth,
        #         ai_builder.integrations.google_auth,
        #         ai_builder.integrations.open_ai,
        #     ],
        # ),
    ]


def get_ai_builder_integrations():
    from pcweb.pages.docs import ai_builder

    return [
        create_item(
            "Integrations",
            children=[
                ai_builder.integrations.overview,
                create_item("Python Libraries", children=[ai_builder.integrations.python_libraries]),
                create_item("APIs", children=[ai_builder.integrations.apis]),
                create_item("Webhook", children=[ai_builder.integrations.webhook]),
                create_item("Files", children=[ai_builder.integrations.files]),
                create_item("Databases", children=[ai_builder.integrations.databases]),
                create_item("Agents/MCPs", children=[ai_builder.integrations.agents_mcps]),
                create_item("Images/Video", children=[ai_builder.integrations.images_video]),
                create_item("Figma (Coming Soon)", children=[ai_builder.integrations.figma]),
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
ai_builder_integrations = get_ai_builder_integrations()
mcp_items = get_sidebar_items_mcp()
