import reflex as rx

config = rx.Config(
    port=3000,
    app_name="pcweb",
    deploy_url="https://reflex.dev",
    frontend_packages=[
        "chakra-react-select",
        "@radix-ui/react-navigation-menu",
         "@inkeep/widgets@latest"
    ],
    telemetry_enabled=False,
    tailwind={
        "plugins": [
            "@tailwindcss/typography",
        ],
    },
)
