import reflex as rx
from pcweb.components.icons.icons import get_icon
from pcweb.components.icons.hugeicons import hi
from pcweb.pages.framework.views.companies import companies as index_companies

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

companies_case_studies = {
    "fastly": {
        "company_name": "Fastly",
        "quote": "Fastly is a cloud computing company that provides content delivery network (CDN) services.",
        "person": "Juan",
        "role": "CEO",
    },
    "autodesk": {
        "company_name": "Autodesk",
        "quote": "Autodesk is a software company that provides design and engineering software.",
        "person": "Juan",
        "role": "CEO",
    },
}


def stat(stat: str, text: str) -> rx.Component:
    return rx.el.section(
        get_icon("feather"),
        rx.box(
            rx.text(
                stat,
                class_name="text-3xl inline-block text-slate-12 font-semibold w-full text-balance text-center",
            ),
            rx.text(text, class_name="text-sm text-slate-9 font-medium"),
            class_name="flex flex-col justify-center items-center text-center text-nowrap",
        ),
        get_icon("feather", class_name="scale-x-[-1]"),
        class_name="flex flex-row items-center gap-4 justify-center",
    )


def company_card(path: str, name: str) -> rx.Component:
    if name == "STATS":
        return rx.box(
            stat(stat="100K+", text="Apps built with Reflex"),
            class_name="w-full col-span-2 h-[10.75rem] flex justify-center items-center bg-slate-1 border-box",
        )

    is_case_study = name in companies_case_studies
    parent_box_class_name = "h-[10.75rem] w-full relative overflow-hidden flex justify-center items-center bg-slate-1 border-box"
    image_component = rx.image(
        src=path,
        class_name="w-[4.75rem] h-auto pointer-events-none",
        alt=f"{name} logo",
    )
    content_items = [image_component]
    badge_component = None

    if is_case_study:
        parent_box_class_name += " cursor-pointer group"
        badge_component = rx.box(
            "Case Study",
            get_icon("arrow_top_right", class_name="size-3.5 rotate-45 group-hover:rotate-0 transition-transform"),
            class_name="absolute bottom-4 right-4 bg-violet-3 border border-violet-6 text-violet-9 group-hover:bg-violet-4 text-xs font-semibold px-2 py-1 rounded-full transition-colors flex flex-row items-center gap-1 scale-[0.85]",
        )
        content_items.append(badge_component)

    trigger_box = rx.box(
        *content_items,
        class_name=parent_box_class_name,
    )

    if is_case_study:
        case_study = companies_case_studies[name]
        hover_content = rx.hover_card.content(
            rx.box(
                rx.text(
                    f'“{case_study["quote"]}”',
                    class_name="text-sm text-slate-12 italic font-medium",
                ),
                rx.text(
                    f"{case_study['person']}, {case_study['role']}",
                    class_name="text-sm text-slate-9 font-medium",
                ),
                class_name="flex flex-col gap-2",
            ),
            side="top",
            side_offset=-50,
            align="center",
            class_name="flex justify-center items-center bg-slate-1 p-3 rounded-xl shadow-large border border-slate-5 w-[17rem]",
        )
        return rx.hover_card.root(
            rx.hover_card.trigger(trigger_box),
            hover_content,
        )
    else:
        return trigger_box


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
