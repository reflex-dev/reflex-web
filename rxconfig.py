import reflex as rx
from tailwind_config import tw_config

config = rx.Config(
    port=3000,
    app_name="pcweb",
    deploy_url="https://reflex.dev",
    frontend_packages=[
        "chakra-react-select",
        "@radix-ui/react-navigation-menu",
    ],
    show_build_with_reflex=False,
    telemetry_enabled=False,
<<<<<<< HEAD
    plugins=[rx.plugins.TailwindV3Plugin(tw_config)],
=======
    tailwind=tw_config,
>>>>>>> 41fefec (Address UI feedback: bigger search input, lighter violet pills, wider modal, card shadows)
)
