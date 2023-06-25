import pynecone as pc

config = pc.Config(
    port=3000,
    app_name="pcweb",
    frontend_packages=[
        "react-confetti",
        "react-colorful",
        "react-copy-to-clipboard",
        "chakra-react-select",
        "@radix-ui/react-navigation-menu"
    ],
    telemetry_enabled=False,
)
