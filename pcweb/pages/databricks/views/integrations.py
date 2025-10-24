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
            "Integrate with Everything in Databricks",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance",
        ),
        class_name="flex flex-col gap-4 items-center justify-center w-full relative overflow-hidden mx-auto",
    )


def intregation_card(
    first_integration: str,
    text: str = "",
    class_name: str = "",
):
    first_light_dark_path = f"/landing/integrations/light/{first_integration}.svg"
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=first_light_dark_path,
                class_name="size-7 pointer-events-none shrink-0",
            ),
            class_name=ui.cn(
                "absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 size-14 rounded-[0.625rem] border border-slate-5 dark:border-[#1C2024] shadow-medium bg-white-1 z-[3] flex justify-center items-center",
                class_name,
            ),
        ),
        rx.el.span(
            text,
            class_name="text-slate-9 text-xs font-medium mt-[5rem]",
        )
        if text
        else None,
        class_name="relative flex flex-col items-center justify-center h-14",
    )


def line_svg(class_name: str = "") -> rx.Component:
    return rx.html(
        """<svg width="120" height="293" viewBox="0 0 120 293" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M0 0.5H20.9869C27.6193 0.5 33.5641 4.5919 35.9322 10.7871L87.9999 147M87.9999 147H120M87.9999 147L35.946 282.247C33.5685 288.424 27.6328 292.5 21.0138 292.5H0M87.9999 147L36.5527 101.065C33.6206 98.447 29.8273 97 25.8965 97H0M87.9999 147L36.4938 191.148C33.5939 193.634 29.9005 195 26.0811 195H0" stroke="url(#paint0_linear_20013_5747)"/>
<defs>
<linearGradient id="paint0_linear_20013_5747" x1="120" y1="147" x2="0" y2="147" gradientUnits="userSpaceOnUse">
<stop stop-color="#FCFCFD" stop-opacity="0"/>
<stop offset="0.08" stop-color="#E8E8EC"/>
<stop offset="0.92" stop-color="#E8E8EC"/>
<stop offset="1" stop-color="#FCFCFD" stop-opacity="0"/>
</linearGradient>
</defs>
</svg>
""",
        class_name=f"absolute z-[0] opacity-60 dark:opacity-100 {class_name}",
    )


def one_line_svg(class_name: str = "") -> rx.Component:
    return rx.html(
        """<svg width="123" height="1" viewBox="0 0 123 1" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M7.62939e-05 0.500229H32.0001L120 0.5" stroke="url(#paint0_linear_20012_5680)"/>
<defs>
<linearGradient id="paint0_linear_20012_5680" x1="7.62939e-05" y1="0.500121" x2="123" y2="0.500121" gradientUnits="userSpaceOnUse">
<stop stop-color="#FCFCFD" stop-opacity="0"/>
<stop offset="0.08" stop-color="#E8E8EC"/>
<stop offset="0.92" stop-color="#E8E8EC"/>
<stop offset="1" stop-color="#FCFCFD" stop-opacity="0"/>
</linearGradient>
</defs>
</svg>
""",
        class_name=f"absolute z-[0] opacity-60 dark:opacity-100 {class_name}",
    )


def r_logo_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src="/landing/integrations/light/r_logo_violet.svg",
                class_name="h-8 w-autopointer-events-none shrink-0 absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2",
            ),
            class_name="size-15 rounded-lg shadow-large bg-primary-9 absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 z-[2]",
        ),
        class_name="size-18 rounded-xl border border-violet-6 shadow-large bg-violet-3 dark:bg-violet-1 relative z-[2]",
    )


def lines() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            line_svg(class_name="left-[13.5rem] top-1/2 -translate-y-1/2"),
            class_name="relative overflow-hidden",
        ),
        rx.el.div(
            one_line_svg(
                class_name="right-[12rem] top-1/2 -translate-y-1/2 scale-x-[-1]"
            ),
            class_name="relative overflow-hidden",
        ),
        class_name="grid grid-cols-2 absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 lg:w-[43.5rem] w-[36rem] z-[0] overflow-hidden h-[20rem]",
    )


def integrations_row() -> rx.Component:
    return rx.el.div(
        lines(),
        rx.el.div(
            intregation_card("databricks_oauth", "OAuth"),
            intregation_card("databricks_db", "SQL"),
            intregation_card("databricks_genie_ai", "Genie AI"),
            intregation_card("databricks_unity", "Unity"),
            class_name="flex flex-col gap-10",
        ),
        r_logo_card(),
        rx.el.div(
            intregation_card("databricks"),
            class_name="flex flex-col gap-10",
        ),
        class_name="flex flex-row items-center lg:gap-[7.5rem] gap-14 mt-10 relative max-lg:w-full justify-center ml-[-3.5rem]",
    )


def content_text() -> rx.Component:
    return rx.el.div(
        rx.el.p(
            "With Reflex's Databricks integration, you can build customizable, performant web apps that seamlessly leverage Databricks' powerful data and AI services:",
            class_name="text-slate-12 text-left mb-4",
        ),
        rx.el.ul(
            rx.el.li("SQL Warehouse", class_name="text-slate-12 mb-1"),
            rx.el.li("Unity Catalog", class_name="text-slate-12 mb-1"),
            rx.el.li("Genie AI", class_name="text-slate-12 mb-1"),
            rx.el.li("OAuth-based authentication", class_name="text-slate-12 mb-1"),
            class_name="text-left mb-4 ml-4 list-disc",
        ),
        rx.el.p(
            "These are just a few examples — Reflex can hook into most Databricks services, giving you the flexibility to integrate analytics, governance, AI, and data pipelines directly into your apps.",
            class_name="text-slate-12 text-left mb-6",
        ),
        rx.el.p(
            "Once your app is ready, you can deploy it directly to Databricks Apps, ensuring that all data, compute, and governance remain fully within your organization's Databricks environment — maintaining compliance, security, and performance at scale.",
            class_name="text-slate-12 text-left mb-6",
        ),
        rx.el.p(
            "With Reflex + Databricks, you can transform data workflows, analytics dashboards, and AI interfaces into interactive, secure, and enterprise-ready applications — all without leaving your Databricks ecosystem.",
            class_name="text-slate-12 text-left mb-8",
        ),
        class_name="flex flex-col items-start mx-auto w-full justify-start max-w-[36rem] mt-8",
    )


def integrations() -> rx.Component:
    return rx.el.section(
        numbers_pattern(side="left", class_name="left-0 top-0"),
        numbers_pattern(side="right", class_name="right-0 top-0"),
        header(),
        content_text(),
        integrations_row(),
        class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden lg:pb-26 pb-20 pt-20 lg:border-b",
    )
