import reflex as rx
import reflex_ui as ui

from pcweb.constants import REFLEX_ASSETS_CDN


def first_card(title: str) -> rx.Component:
    return rx.el.div(
        ui.icon(
            "CheckmarkBadge02Icon",
            class_name="text-secondary-11 shrink-0",
        ),
        rx.el.span(
            title,
            class_name="text-secondary-11 text-sm font-medium text-wrap",
        ),
        class_name="flex flex-row gap-2.5 items-center max-lg:justify-center lg:col-span-2 px-10 h-full max-lg:h-[10.75rem] max-lg:w-full lg:border-r border-b w-full",
    )


def social_proof_card(image: str) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=rx.color_mode_cond(
                f"{REFLEX_ASSETS_CDN}companies/light/{image}.svg",
                f"{REFLEX_ASSETS_CDN}companies/dark/{image}.svg",
            ),
            loading="lazy",
            alt=f"{image} logo",
        ),
        class_name="flex justify-center items-center lg:size-[10.75rem] max-lg:h-[10.75rem] max-lg:w-full lg:border-r border-b",
    )


def social_proof(title: str, images: list[str]) -> rx.Component:
    return rx.el.div(
        first_card(title),
        *[social_proof_card(image) for image in images],
        class_name="grid lg:grid-cols-6 grid-cols-1 justify-center items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 lg:divide-x divide-slate-3 lg:border-t max-lg:divide-y",
    )
