import reflex as rx
import reflex_ui as ui
from reflex.experimental.client_state import ClientStateVar

from pcweb.components.numbers_pattern import numbers_pattern

items = [
    ("Analytics", "Analytics01Icon"),
    ("Finance", "CreditCardPosIcon"),
    ("E-commerce", "ShoppingBasket03Icon"),
    ("DevOps", "CloudServerIcon"),
    ("Databases", "Database02Icon"),
    ("AI Workflows", "MagicWand01Icon"),
]

selected_industry = ClientStateVar.create(
    var_name="selected_industry", default=items[0][0]
)


def header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            ui.icon("BrowserIcon", class_name="shrink-0"),
            rx.el.span("Use Cases", class_name="text-sm font-semibold"),
            class_name="flex flex-row gap-2 items-center text-primary-9",
        ),
        rx.el.h2(
            "Use Cases by Industry",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            "See what’s built with Reflex.",
            class_name="text-slate-9 text-sm font-medium text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        class_name="flex flex-col gap-4 items-center mx-auto w-full relative overflow-hidden",
    )


def pill_item(name: str, icon: str) -> rx.Component:
    active_cn = "bg-slate-2 shadow-large text-slate-12"
    is_active = selected_industry.value == name
    return rx.el.div(
        ui.icon(icon),
        rx.el.span(name),
        class_name=ui.cn(
            "h-8 flex flex-row gap-2 items-center px-3 text-slate-9 font-medium text-sm cursor-pointer hover:bg-slate-2 transition-colors text-nowrap",
            rx.cond(is_active, active_cn, ""),
        ),
        on_click=selected_industry.set_value(name),
    )


def pills() -> rx.Component:
    return rx.el.div(
        *[pill_item(name, icon) for name, icon in items],
        class_name="flex flex-row items-center justify-start border border-slate-4 rounded-lg shadow-small bg-white-1 divide-x divide-slate-4 h-8 mt-10 flex-nowrap overflow-x-auto max-lg:w-full lg:justify-center max-lg:overflow-y-hidden",
    )


def gradients() -> rx.Component:
    return rx.fragment(
        rx.html(
            """<svg xmlns="http://www.w3.org/2000/svg" width="1298" height="728" viewBox="0 0 1298 728" fill="none">
  <g opacity="0.48" filter="url(#filter0_f_18264_136883)">
    <path d="M176.126 284.172C68.3898 75.0632 -26.8819 15.1277 637.681 128.494C895.881 172.539 1406.87 -42.2487 1155.98 215.019C983.495 391.891 1160.9 306.595 1214 460.374C1234.85 520.772 1258.25 749.789 1005.53 613.288C946.741 581.537 582.142 591.537 386.794 637.841C191.447 684.146 102.392 620.277 74.622 504.517C46.8521 388.756 250.491 428.511 176.126 284.172Z" stroke="#C2B5F5" stroke-width="16"/>
  </g>
  <defs>
    <filter id="filter0_f_18264_136883" x="0" y="0" width="1298" height="728" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="32" result="effect1_foregroundBlur_18264_136883"/>
    </filter>
  </defs>
</svg>
""",
            class_name="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 pointer-events-none z-1 dark:hidden block",
        ),
        rx.html(
            """<svg xmlns="http://www.w3.org/2000/svg" width="1298" height="728" viewBox="0 0 1298 728" fill="none">
  <g opacity="0.48" filter="url(#filter0_f_18310_74656)">
    <path d="M176.126 284.172C68.3898 75.0632 -26.8819 15.1277 637.681 128.494C895.881 172.539 1406.87 -42.2487 1155.98 215.019C983.495 391.891 1160.9 306.595 1214 460.374C1234.85 520.772 1258.25 749.789 1005.53 613.288C946.741 581.537 582.142 591.537 386.794 637.841C191.447 684.146 102.392 620.277 74.622 504.517C46.8521 388.756 250.491 428.511 176.126 284.172Z" stroke="#2F265F" stroke-width="16"/>
  </g>
  <defs>
    <filter id="filter0_f_18310_74656" x="0" y="0" width="1298" height="728" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="32" result="effect1_foregroundBlur_18310_74656"/>
    </filter>
  </defs>
</svg>
""",
            class_name="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 pointer-events-none z-2 hidden dark:block",
        ),
    )


def app_card() -> rx.Component:
    return rx.el.div(
        gradients(),
        rx.image(
            src=rx.match(
                selected_industry.value,
                ("Analytics", "/case_studies/analytics_dashboard.webp"),
                ("Finance", "/case_studies/bayesline_app.webp"),
                ("E-commerce", "/case_studies/sellerx_app.webp"),
                ("DevOps", "/case_studies/devops_app.webp"),
                ("Databases", "/case_studies/admin_app.webp"),
                ("AI Workflows", "/case_studies/ai_workflow.webp"),
                "/case_studies/analytics_dashboard.webp",
            ),
            class_name="w-full lg:h-[33.05038rem] h-[24rem] object-cover rounded-2xl border border-slate-4 z-5 lg:p-4 bg-slate-1 object-top",
        ),
        class_name="w-full rounded-4xl lg:border border-slate-4 lg:backdrop-blur-[6px] lg:bg-slate-2/48 lg:p-4 flex relative z-1",
    )


def use_cases_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                numbers_pattern(side="left", class_name="left-0 top-0"),
                numbers_pattern(side="right", class_name="right-0 top-0"),
                header(),
                pills(),
                class_name="max-w-[64.19rem] w-full lg:border-x border-slate-3 flex flex-col items-center mx-auto pt-20 pb-10 relative overflow-hidden",
            ),
            app_card(),
            class_name="relative max-w-[71.125rem] mx-auto flex flex-col items-center justify-center w-full",
        ),
        class_name="flex flex-col items-center mx-auto w-full max-w-[84.5rem]",
    )
