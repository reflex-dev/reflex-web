import reflex as rx
import reflex_ui as ui

from pcweb.components.numbers_pattern import numbers_pattern


def header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            ui.icon("UserGroupIcon", class_name="shrink-0"),
            rx.el.span("Teams", class_name="text-sm font-semibold"),
            class_name="flex flex-row gap-2 items-center text-primary-9",
        ),
        rx.el.h2(
            "Hear from the teams that use Reflex",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            "Companies of all sizes trust Reflex to build internal tools and customer-facing apps.",
            class_name="text-slate-9 text-sm font-medium text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        class_name="flex flex-col gap-4 items-center mx-auto w-full relative overflow-hidden",
    )


def enterprise_card(image: str, name: str, stat: str, text: str) -> rx.Component:
    first_word = text.split(" ")[0]
    rest_of_text = " ".join(text.split(" ")[1:])
    return rx.el.a(
        rx.el.div(
            rx.image(
                src=f"/customers/{rx.color_mode_cond('light', 'dark')}{image}",
                class_name="w-auto h-[1.875rem]",
            ),
            rx.el.span(
                name,
                class_name="text-slate-12 text-3xl font-bold",
            ),
            class_name="flex flex-row gap-3 items-center justify-start mr-auto",
        ),
        rx.el.div(
            rx.el.h3(
                stat,
                class_name="text-4xl font-semibold text-slate-12",
            ),
            rx.el.div(
                rx.el.span(
                    first_word, class_name="text-slate-12 text-base font-semibold"
                ),
                rx.el.span(
                    f" {rest_of_text}",
                    class_name="text-slate-10 text-base font-medium",
                ),
                class_name="inline-block",
            ),
            class_name="flex flex-col gap-2",
        ),
        to=f"/customers/{name.lower().replace(' ', '-')}",
        class_name="flex flex-col gap-10 p-10 shadow-small border border-slate-3 hover:border-slate-4 rounded-2xl bg-white-1 hover:bg-slate-2 transition-colors h-[15.875rem] cursor-pointer",
    )


def enterprise_social() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            numbers_pattern(side="left", reversed=True, class_name="left-0 top-0"),
            numbers_pattern(side="right", reversed=True, class_name="right-0 top-0"),
            header(),
            class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden py-20",
        ),
        rx.el.div(
            enterprise_card(
                "/autodesk/autodesk_small.svg",
                "Autodesk",
                "25%",
                "Time saved on each project with Reflex.",
            ),
            enterprise_card(
                "/bayesline/bayesline_small.svg",
                "Bayesline",
                "30%",
                "Production codebase smaller than Dash.",
            ),
            enterprise_card(
                "/ansa/ansa_small.svg",
                "Ansa",
                "100+",
                "Hours of manual work saved a month.",
            ),
            enterprise_card(
                "/sellerx/sellerx_small.svg",
                "SellerX",
                "10x",
                "Faster than developing with React and FastAPI.",
            ),
            class_name="w-full grid grid-cols-1 lg:grid-cols-4 gap-2",
        ),
        class_name="flex flex-col items-center mx-auto w-full max-w-[84.5rem]",
    )
