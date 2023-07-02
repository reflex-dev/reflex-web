import reflex as rx

config = rx.Config(
    port=3000,
    app_name="pcweb",
    rxdeploy_url="",
    api_url="https://pynecone-test37.fly.dev:8000",
    frontend_packages=[
        "react-confetti",
        "react-colorful",
        "react-copy-to-clipboard",
        "chakra-react-select",
        "@radix-ui/react-navigation-menu",
    ],
    telemetry_enabled=False,
    tailwind={},
)
