import reflex as rx
import reflex_ui as ui


def first_card() -> rx.Component:
    return rx.el.div(
        ui.icon(
            "CheckmarkBadge02Icon",
            class_name="text-m-slate-11 dark:text-m-slate-9 shrink-0",
        ),
        rx.el.span(
            "Trusted by innovative finance teams",
            class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium text-nowrap",
        ),
        class_name="flex flex-row gap-2.5 items-center max-lg:justify-center lg:col-span-2 px-10 h-full max-lg:h-[10.75rem] max-lg:w-full",
    )


def social_proof_card(image: str) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=rx.color_mode_cond(
                f"/companies/light/{image}.svg", f"/companies/dark/{image}.svg"
            ),
            loading="lazy",
            alt=f"{image} logo",
        ),
        class_name="flex justify-center items-center lg:size-[10.75rem] max-lg:h-[10.75rem] max-lg:w-full",
    )


def social_proof() -> rx.Component:
    return rx.el.div(
        first_card(),
        social_proof_card("man_group"),
        social_proof_card("world_bank"),
        social_proof_card("credit_agricole"),
        social_proof_card("bayesline"),
        class_name="grid lg:grid-cols-6 grid-cols-1 justify-center items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 lg:divide-x divide-slate-3 lg:border-t max-lg:divide-y",
    )
