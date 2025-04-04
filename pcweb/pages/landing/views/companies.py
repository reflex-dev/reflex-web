import reflex as rx
from pcweb.components.icons.icons import get_icon
from pcweb.pages.index.views.companies import companies as index_companies

companies_list = [
    "apple",
    "microsoft",
    "amazon",
    "rappi",
    "accenture",
    "ibm",
    "dell",
    "autodesk",
    "STATS",
    "twilio",
    "ford",
    "paloalto",
    "bosch",
    "fastly",
    "unicef",
    "nasa",
    "nike",
]


def stat(stat: str, text: str) -> rx.Component:
    return rx.el.section(
        get_icon("feather"),
        rx.box(
            rx.text(
                stat,
                class_name="text-3xl inline-block text-slate-12 font-semibold w-full text-balance text-center",
            ),
            rx.text(text, class_name="text-sm text-slate-9"),
            class_name="flex flex-col justify-center items-center text-center text-nowrap",
        ),
        get_icon("feather", class_name="scale-x-[-1]"),
        class_name="flex flex-row items-center gap-4 justify-center",
    )


def company_card(path: str, name: str) -> rx.Component:
    return (
        (
            rx.box(
                rx.image(src=path, class_name="w-[4.75rem] h-auto pointer-events-none", alt=f"{name} logo"),
                class_name="h-[10.75rem] w-full relative overflow-hidden flex justify-center items-center bg-slate-1 border-box",
            )
            if name != "STATS"
            else rx.box(
                stat(stat="100K+", text="Apps built with Reflex"),
                class_name="w-full col-span-2 h-[10.75rem] flex justify-center items-center bg-slate-1 border-box",
            )
        ),
    )


def companies() -> rx.Component:
    return rx.el.section(
        rx.box(class_name="h-[3rem] w-full border-b border-slate-3 lg:flex hidden"),
        rx.box(
            *[
                company_card(
                    f"/landing/companies/{rx.color_mode_cond(light='light', dark='dark')}/{company}.svg",
                    company,
                )
                for company in companies_list
            ],
            class_name="lg:grid grid-cols-6 w-full gap-[1px] bg-slate-3 hidden relative",
        ),
        rx.el.div(
            index_companies(),
            class_name="lg:hidden flex border-t border-slate-3 lg:border-t-0",
        ),
        class_name="flex flex-col justify-center items-center mx-auto w-full max-w-[64.19rem] border-slate-3 relative z-[1] overflow-hidden isolate lg:border-b lg:border-x",
    )
