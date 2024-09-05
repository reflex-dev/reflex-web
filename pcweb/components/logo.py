import reflex as rx


def logo(class_name: str = "") -> rx.Component:
    return rx.link(
        rx.color_mode_cond(
            rx.image(
                src="/logos/light/reflex.svg",
                alt="Reflex Logo",
                class_name="shrink-0" + class_name,
            ),
            rx.image(
                src="/logos/dark/reflex.svg",
                alt="Reflex Logo",
                class_name="shrink-0" + class_name,
            ),
        ),
        class_name="flex items-start shrink-0",
        href="/",
    )
