import reflex as rx

from pcweb.components.button import button
from pcweb.components.icons.icons import get_icon
from pcweb.constants import DISCORD_URL
from pcweb.pages.docs import hosting


def card(
    icon: str, heading: str, content: str, button_text: str, link: str
) -> rx.Component:
    return rx.box(
        get_icon(icon, class_name="!justify-start"),
        rx.box(
            rx.text(heading, class_name="font-md-smbold text-slate-11"),
            rx.text(content, class_name="font-small text-slate-9 whitespace-pre"),
            class_name="flex flex-col gap-2 mt-4 mb-6",
        ),
        rx.link(
            button(button_text, variant="secondary"),
            href=link,
            is_external=False,
            underline="none",
        ),
        class_name="flex flex-col border-slate-4 bg-slate-2 p-8 border rounded-[1.125rem]",
    )


def deploy() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.el.h2(
                "Deploy your app fast", class_name="font-x-large gradient-heading"
            ),
            rx.text(
                "With our services or self-hosting.",
                class_name="font-base text-slate-9",
            ),
            class_name="flex flex-col gap-4 text-center",
        ),
        rx.box(
            card(
                "cloud",
                "Reflex Deploy",
                """Use for performance and security.
With autoconfigured CDN, HTTPS, SSL.""",
                "Learn how",
                hosting.deploy_quick_start.path,
            ),
            card(
                "database",
                "Self-host",
                """Host by yourself easily when you need it.
Follow installation instructions.""",
                "Get help",
                DISCORD_URL,
            ),
            class_name="gap-4 grid grid-cols-1 lg:grid-cols-2",
        ),
        class_name="flex flex-col justify-center gap-10 w-full py-40",
    )
