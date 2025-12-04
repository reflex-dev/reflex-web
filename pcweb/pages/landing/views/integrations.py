import reflex as rx
import reflex_ui as ui

from pcweb.components.numbers_pattern import numbers_pattern


def header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            ui.icon("WorkflowSquare08Icon", class_name="shrink-0"),
            rx.el.span("Integrations", class_name="text-sm font-semibold"),
            class_name="flex flex-row gap-2 items-center text-primary-9",
        ),
        rx.el.h2(
            "Integrate With Your Platforms",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            "Build entire app flow using powerful integrations.",
            class_name="text-secondary-11 text-sm font-medium text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        class_name="flex flex-col gap-4 items-center mx-auto w-full relative overflow-hidden",
    )


def intregation_card(
    first_integration: str,
    second_integration: str,
    class_name: str = "",
):
    first_light_dark_path = rx.color_mode_cond(
        f"/landing/integrations/light/{first_integration}.svg",
        f"/landing/integrations/dark/{first_integration}.svg",
    )
    second_light_dark_path = rx.color_mode_cond(
        f"/landing/integrations/light/{second_integration}.svg",
        f"/landing/integrations/dark/{second_integration}.svg",
    )
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=first_light_dark_path,
                loading="lazy",
                alt=f"{first_integration} integration icon",
                class_name="size-7 pointer-events-none shrink-0",
            ),
            class_name=ui.cn(
                "absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 size-14 rounded-[0.625rem] border border-slate-5 dark:border-[#1C2024] shadow-medium bg-white-1 z-[3] flex justify-center items-center",
                "animate-[fade-scale-out] animate-duration-[8000ms] animate-ease-out animate-infinite",
                class_name,
            ),
        ),
        rx.el.div(
            rx.image(
                src=second_light_dark_path,
                loading="lazy",
                alt=f"{second_integration} integration icon",
                class_name="size-7 pointer-events-none shrink-0",
            ),
            class_name=ui.cn(
                "absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 size-14 rounded-[0.625rem] border border-slate-5 dark:border-[#1C2024] shadow-medium bg-white-1 z-[3] flex justify-center items-center",
                "animate-[fade-scale-in] animate-duration-[8000ms] animate-ease-out animate-infinite",
                class_name,
            ),
        ),
        class_name="relative size-14",
    )


def line_svg(class_name: str = "") -> rx.Component:
    return rx.html(
        """<svg xmlns="http://www.w3.org/2000/svg" width="120" height="194" viewBox="0 0 120 194" fill="none">
  <path d="M0 0.999756L22.8101 0.999921C28.5007 0.999963 33.7631 4.02254 36.6304 8.93798L87.9999 97M87.9999 97H120M87.9999 97L0 96.9998M87.9999 97L36.6305 185.062C33.7631 189.977 28.5006 193 22.8099 193L0 193" stroke="url(#paint0_linear_18320_122295)"/>
  <defs>
    <linearGradient id="paint0_linear_18320_122295" x1="120" y1="96.9999" x2="0" y2="96.9999" gradientUnits="userSpaceOnUse">
      <stop stop-color="#1C2024" stop-opacity="0"/>
      <stop offset="0.08" stop-color="#60646C" stop-opacity="0.2"/>
      <stop offset="0.92" stop-color="#60646C" stop-opacity="0.2"/>
      <stop offset="1" stop-color="#1C2024" stop-opacity="0"/>
    </linearGradient>
  </defs>
</svg>""",
        class_name=f"absolute z-[0] opacity-50 dark:opacity-100 {class_name}",
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
                loading="lazy",
                alt="R logo integration icon",
                class_name="h-8 w-autopointer-events-none shrink-0 absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2",
            ),
            class_name="size-15 rounded-lg border border-slate-5 dark:border-[#1C2024] shadow-large bg-white-1 absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 z-[2]",
        ),
        class_name="size-18 rounded-xl border border-slate-3 dark:border-[#1C2024] shadow-large bg-white/76 dark:bg-slate-1 relative z-[2]",
    )


def lines() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            line_svg(class_name="left-[12rem] top-1/2 -translate-y-1/2"),
            # ellipse_svg(
            #     class_name="top-1/2 -translate-y-1/2 mix-blend-darken z-[0] animate-[ellipse-slide-left] animate-duration-[8000ms] animate-ease-in-out animate-infinite"
            # ),
            class_name="relative overflow-hidden",
        ),
        rx.el.div(
            # ellipse_svg(
            #     class_name="top-1/2 -translate-y-1/2 mix-blend-darken z-[0] animate-[ellipse-slide-right] animate-duration-[8000ms] animate-ease-in-out animate-infinite"
            # ),
            line_svg(class_name="right-[12rem] top-1/2 -translate-y-1/2 scale-x-[-1]"),
            class_name="relative overflow-hidden",
        ),
        class_name="grid grid-cols-2 absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 lg:w-[43.5rem] w-[36rem] z-[0] overflow-hidden h-[20rem]",
    )


def integrations_row() -> rx.Component:
    return rx.el.div(
        lines(),
        rx.el.div(
            intregation_card("supabase", "langchain"),
            intregation_card("openai", "databricks"),
            intregation_card("stripe", "anthropic"),
            class_name="flex flex-col gap-10",
        ),
        r_logo_card(),
        rx.el.div(
            intregation_card("aws", "gcp"),
            intregation_card("azure", "oracle"),
            intregation_card("databricks", "reflex"),
            class_name="flex flex-col gap-10",
        ),
        class_name="flex flex-row items-center lg:gap-[7.5rem] gap-14 mt-10 relative max-lg:w-full justify-center",
    )


def integrations() -> rx.Component:
    return rx.el.section(
        numbers_pattern(side="left", class_name="left-0 top-0"),
        numbers_pattern(side="right", class_name="right-0 top-0"),
        header(),
        integrations_row(),
        class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden lg:border-t lg:pb-26 pb-20 pt-20",
    )
