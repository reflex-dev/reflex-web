import reflex as rx

config = rx.Config(
    state_auto_setters=True,
    port=3000,
    app_name="pcweb",
    deploy_url="https://reflex.dev",
    frontend_packages=[
        "chakra-react-select",
        "@radix-ui/react-navigation-menu",
        "tailwindcss-animated",
    ],
    show_build_with_reflex=True,
    telemetry_enabled=False,
    plugins=[rx.plugins.TailwindV4Plugin(), rx.plugins.SitemapPlugin()],
)
