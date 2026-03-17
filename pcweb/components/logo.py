import reflex as rx

from pcweb.constants import REFLEX_ASSETS_CDN


def logo(class_name: str = "") -> rx.Component:
    return rx.link(
        rx.fragment(
            rx.image(
                src=f"{REFLEX_ASSETS_CDN}logos/light/reflex.svg",
                alt="Reflex Logo",
                class_name="shrink-0 block dark:hidden" + class_name,
            ),
            rx.image(
                src=f"{REFLEX_ASSETS_CDN}logos/dark/reflex.svg",
                alt="Reflex Logo",
                class_name="shrink-0 hidden dark:block" + class_name,
            ),
        ),
        class_name="flex items-start shrink-0",
        href="/",
    )
