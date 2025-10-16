import reflex as rx
import reflex_ui as ui

from pcweb.components.numbers_pattern import numbers_pattern


def header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            ui.icon("WorkflowSquare08Icon", class_name="shrink-0"),
            rx.el.span("Integrations", class_name="text-sm font-semibold"),
            class_name="flex flex-row gap-2 items-center text-violet-9",
        ),
        rx.el.h2(
            "Integrate With Your Platforms",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            "Build entire app flow using powerful integrations.",
            class_name="text-slate-9 text-sm font-medium text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        class_name="flex flex-col gap-4 items-center mx-auto w-full relative overflow-hidden",
    )


def intregation_card(
    first_integration: str, second_integration: str, class_name: str = ""
):
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=f"/landing/integrations/light/{first_integration}.svg",
                class_name="size-7 pointer-events-none shrink-0",
            ),
            class_name=ui.cn(
                "absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 size-14 rounded-[0.625rem] border border-slate-5 shadow-medium bg-white-1 z-[3] flex justify-center items-center",
                "animate-[fade-scale-out] animate-duration-[8000ms] animate-ease-out animate-infinite",
                class_name,
            ),
        ),
        rx.el.div(
            rx.image(
                src=f"/landing/integrations/light/{second_integration}.svg",
                class_name="size-7 pointer-events-none shrink-0",
            ),
            class_name=ui.cn(
                "absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 size-14 rounded-[0.625rem] border border-slate-5 shadow-medium bg-white-1 z-[3] flex justify-center items-center",
                "animate-[fade-scale-in] animate-duration-[8000ms] animate-ease-out animate-infinite",
                class_name,
            ),
        ),
        class_name="relative size-14",
    )


def line_svg(class_name: str = "") -> rx.Component:
    return rx.html(
        """<svg xmlns="http://www.w3.org/2000/svg" width="284" height="2" viewBox="0 0 284 2" fill="none"><path d="M0 1h284" stroke="url(#a)"/><defs><linearGradient id="a" x1="0" y1="1.5" x2="284" y2="1.5" gradientUnits="userSpaceOnUse"><stop stop-color="#FCFCFD"/><stop offset=".04" stop-color="#E8E8EC"/><stop offset=".8" stop-color="#E8E8EC"/><stop offset="1" stop-color="#FCFCFD"/></linearGradient></defs></svg>""",
        class_name=f"absolute z-[0] w-[17.75rem] {class_name}",
    )


def ellipse_svg(class_name: str = "") -> rx.Component:
    return rx.html(
        """<svg xmlns="http://www.w3.org/2000/svg" width="236" height="1" viewBox="0 0 236 1" fill="none">
  <g filter="url(#filter0_f_18006_49950)">
    <circle cx="118" cy="1" r="86" fill="#6E56CF"/>
  </g>
  <defs>
    <filter id="filter0_f_18006_49950" x="0" y="-117" width="236" height="236" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="16" result="effect1_foregroundBlur_18006_49950"/>
    </filter>
  </defs>
</svg>""",
        class_name=f"absolute z-[1] {class_name}",
    )


def r_logo_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src="/landing/integrations/light/r_logo.svg",
                class_name="h-8 w-autopointer-events-none shrink-0 absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2",
            ),
            class_name="size-15 rounded-lg border border-slate-5 shadow-large bg-white-1 absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 z-[2]",
        ),
        class_name="size-18 rounded-xl border border-slate-3 shadow-large bg-white/76 dark:bg-black/76 relative z-[2] mx-6",
    )


def lines() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            line_svg(class_name="left-0 top-1/2 -translate-y-1/2"),
            ellipse_svg(
                class_name="top-1/2 -translate-y-1/2 mix-blend-darken z-[0] animate-[ellipse-slide-left] animate-duration-[8000ms] animate-ease-in-out animate-infinite"
            ),
            class_name="relative overflow-hidden ml-12.5",
        ),
        rx.el.div(
            ellipse_svg(
                class_name="top-1/2 -translate-y-1/2 mix-blend-darken z-[0] animate-[ellipse-slide-right] animate-duration-[8000ms] animate-ease-in-out animate-infinite"
            ),
            line_svg(class_name="right-0 top-1/2 -translate-y-1/2 scale-x-[-1]"),
            class_name="relative overflow-hidden mr-12.5",
        ),
        class_name="grid grid-cols-2 absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[43.5rem] z-[0] overflow-hidden h-[20rem]",
    )


def integrations_row() -> rx.Component:
    return rx.el.div(
        lines(),
        intregation_card("supabase", "langchain"),
        intregation_card("openai", "databricks"),
        intregation_card("stripe", "anthropic"),
        r_logo_card(),
        intregation_card("aws", "gcp"),
        intregation_card("azure", "oracle"),
        intregation_card("databricks", "reflex"),
        class_name="flex flex-row items-center gap-10 mt-10 relative",
    )


def integrations() -> rx.Component:
    return rx.el.section(
        numbers_pattern(side="left", class_name="left-0 top-0"),
        numbers_pattern(side="right", class_name="right-0 top-0"),
        header(),
        integrations_row(),
        class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden border-t py-30",
    )
