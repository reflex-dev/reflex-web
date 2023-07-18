import reflex as rx

config = rx.Config(
    port=3000,
    app_name="pcweb",
    deploy_url="https://reflex.dev",
    frontend_packages=[
        "react-confetti",
        "react-colorful",
        "react-copy-to-clipboard",
        "chakra-react-select",
        "@radix-ui/react-navigation-menu",
        "@tailwindcss/typography",
        "@splinetool/react-spline",
        "@splinetool/runtime",
    ],
    telemetry_enabled=False,
    tailwind={
        "plugins": [
            "@tailwindcss/typography",
        ],
    },
)
