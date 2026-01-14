import reflex as rx

from pcweb.components.marquee import marquee


def social_proof_card(image: str) -> rx.Component:
    return rx.el.div(
        rx.image(
            f"/companies/light/{image}.svg",
            loading="lazy",
            alt=f"{image} logo",
            class_name="grayscale-100 max-h-[2.5rem] opacity-90 dark:opacity-100",
        ),
        class_name="flex justify-center items-center h-[10.75rem] min-w-[10.75rem] px-4 w-auto relative overflow-hidden lg:border-r border-slate-3",
    )


def logos_carousel(logos: list[str]) -> rx.Component:
    return marquee(
        *[social_proof_card(logo) for logo in logos],
        direction="left",
        class_name="h-[10.75rem] w-full overflow-hidden",
        gradient_width=0,
        speed=50,
        pause_on_hover=False,
    )
