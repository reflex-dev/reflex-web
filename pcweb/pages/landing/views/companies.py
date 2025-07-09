import reflex as rx
from reflex.experimental import ClientStateVar
from pcweb.components.icons.icons import get_icon
from pcweb.pages.framework.views.companies import companies as index_companies

company_cs = ClientStateVar.create("company", "")
area_x_pos = ClientStateVar.create(var_name="area_x_pos", default=0)
area_y_pos = ClientStateVar.create(var_name="area_y_pos", default=0)
area_opacity = ClientStateVar.create(var_name="area_opacity", default=0)

companies_list = [
    "apple",
    "microsoft",
    "amazon",
    "fastly",
    "accenture",
    "ibm",
    "unicef",
    "autodesk",
    "STATS",
    "sellerx",
    "ford",
    "paloalto",
    "bosch",
    "dell",
    "twilio",
    "rappi",
    "nike",
]

companies_case_studies = {
    "dell": {
        "company_name": "Dell",
        "quote": """Reflex has been a game changer. 
        In just a week, I had a demo up and running with excellent performance. 
        It made the project feasible for my support team, helping us build a smooth, efficient interface.""",
        "person": "JL",
        "picture": "/favicon.ico",
        "role": "Principal Engineer",
    },
    "autodesk": {
        "company_name": "Autodesk",
        "quote": "One person can do the job of two with Reflex, so it cut our cost in half. I am able to wear all the caps at once: Solution Architecture, UI/UX, front-end and back-end.",
        "person": "Paolo",
        "picture": "/favicon.ico",
        "role": "Principal Consultant",
        "url": "/customers/autodesk",
    },
    "fastly": {
        "company_name": "Fastly",
        "quote": "Migrating our cybersecurity app from Streamlit to Reflex has been excellent. We quickly built a unified interface connecting BigQuery, Salesforce, and PagerDuty for our 15+ team members. The ease of use and rapid development, supported by your responsive team, made it a great experience.",
        "person": "Emanuele Bonura",
        "picture": "/favicon.ico",
        "role": "Senior SOC Engineer",
    },
    # "unicef": {
    #     "company_name": "Unicef",
    #     "quote": """Reflex made it easy to focus on building my app with pure Python and integrate the components I needed without the hassle of learning new front-end frameworks.
    #     It integrates seamlessly with Microsoft Azure, making deployment and scaling smooth and efficient.""",
    #     "person": "Lakshmi",
    #     "picture": "/favicon.ico",
    #     "role": "Data Science Specialist",
    # },
    "sellerx": {
        "company_name": "SellerX",
        "quote": """With Reflex, we're able to ingest 100 GB of data and over 500,000 data points daily, all while developing ten times faster than with React and FastAPI. 
        The built-in AG Grid functionality seamlessly integrates, making it the perfect solution for handling and visualizing large-scale data efficiently.""",
        "person": "Mike",
        "picture": "/favicon.ico",
        "role": "Head of AI & Automation",
        "url": "/customers/sellerx",
    },
}

companies_case_studies_var = rx.Var.create(companies_case_studies)


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


def quote_box(company: str) -> rx.Component:
    case_study = companies_case_studies_var[company]
    return rx.fragment(
        rx.text(
            f"“{case_study['quote']}”",
            class_name="text-xs text-slate-12 italic font-medium animate-fade animate-duration-[750ms] animate-fill-both",
        ),
        rx.box(
            rx.image(
                src=case_study["picture"],
                class_name="size-6 rounded-full",
            ),
            rx.box(
                rx.text(
                    f"{case_study['person']}",
                    class_name="text-xs text-slate-9 font-medium",
                ),
                rx.text(
                    case_study["role"],
                    class_name="text-xs text-slate-9 font-medium",
                ),
            ),
            class_name="flex flex-row items-center gap-2 w-full animate-fade animate-duration-[750ms] animate-fill-both",
        ),
    )


def case_study_badge() -> rx.Component:
    return rx.box(
        rx.text("Case Study", class_name="text-xs text-violet-9 font-semibold"),
        get_icon(
            "arrow_top_right",
            class_name="size-3 group-hover:rotate-0 transition-transform rotate-45",
        ),
        class_name="absolute bottom-4 right-4 bg-violet-3 border border-violet-6 text-violet-9 group-hover:bg-violet-4 group-hover:border-violet-7 text-xs font-semibold px-2 py-1 rounded-full transition-colors flex flex-row items-center gap-1 scale-[0.85] pointer-events-none",
    )


def quote_badge() -> rx.Component:
    return rx.box(
        rx.text("Quote", class_name="text-xs text-violet-9 font-semibold"),
        get_icon("quote", class_name="size-3"),
        class_name="absolute bottom-4 right-4 bg-violet-3 border border-violet-6 text-violet-9 group-hover:bg-violet-4 group-hover:border-violet-7 text-xs font-semibold px-2 py-1 rounded-full transition-colors flex flex-row items-center gap-1 scale-[0.85] pointer-events-none",
    )


@rx.memo
def company_card(name: str, id: str) -> rx.Component:
    area_x_pos = ClientStateVar.create(
        var_name="area_x_pos", default=0, global_ref=False
    )
    area_y_pos = ClientStateVar.create(
        var_name="area_y_pos", default=0, global_ref=False
    )
    area_opacity = ClientStateVar.create(
        var_name="area_opacity", default=0, global_ref=False
    )
    return rx.box(
        rx.cond(
            name == "STATS",
            rx.box(
                rx.cond(
                    companies_case_studies_var.contains(company_cs.value),
                    quote_box(company_cs.value),
                    rx.box(
                        stat(stat="100K+", text="Apps built with Reflex"),
                        class_name="animate-fade flex justify-center items-center size-full animate-duration-[750ms] animate-fill-both",
                    ),
                ),
                class_name="flex flex-col gap-2.5 w-full h-[10.75rem] justify-between bg-slate-1 border-box p-4 overflow-hidden",
            ),
            rx.box(
                # Light
                rx.image(
                    src=f"/landing/companies/light/{name}.svg",
                    class_name="w-[4.75rem] h-auto pointer-events-none group-hover:grayscale-0 grayscale-[1] opacity-50 group-hover:opacity-100 transition-all dark:hidden",
                    alt=f"{name} logo",
                ),
                # Dark
                rx.image(
                    src=f"/landing/companies/dark/{name}.svg",
                    class_name="w-[4.75rem] h-auto pointer-events-none group-hover:grayscale-0 grayscale-[1] opacity-50 group-hover:opacity-100 transition-all dark:block hidden",
                    alt=f"{name} logo",
                ),
                class_name=(
                    "w-full h-[10.75rem] flex justify-center items-center bg-slate-1 border-box transition-colors group",
                    rx.cond(
                        companies_case_studies_var.contains(name)
                        & companies_case_studies_var[name].get("url", None),
                        "cursor-pointer hover:bg-violet-3 dark:hover:bg-violet-1",
                        "hover:bg-[#fdfdfd78] dark:hover:bg-[#15161863]",
                    ),
                ),
                on_mouse_enter=company_cs.set_value(name),
                on_mouse_leave=company_cs.set_value(""),
            ),
        ),
        rx.box(
            aria_hidden=True,
            style={
                "border": "2px solid var(--c-violet-6)",
                "opacity": area_opacity.value,
                "WebkitMaskImage": f"radial-gradient(circle at {area_x_pos.value}px {area_y_pos.value}px, black 45%, transparent)",
            },
            class_name="pointer-events-none absolute left-0 top-0 z-10 h-full w-full border bg-[transparent] opacity-0 transition-opacity duration-500 box-border",
        ),
        rx.cond(
            companies_case_studies_var.contains(name),
            rx.cond(
                companies_case_studies_var[name].get("url", None),
                case_study_badge(),
                quote_badge(),
            ),
        ),
        on_mouse_enter=area_opacity.set_value(1),
        on_mouse_leave=area_opacity.set_value(0),
        on_mouse_move=[
            rx.call_function(
                area_x_pos.set_value(
                    rx.Var(
                        f"event.clientX - document.getElementById({id}).getBoundingClientRect().left"
                    )
                )
            ),
            rx.call_function(
                area_y_pos.set_value(
                    rx.Var(
                        f"event.clientY - document.getElementById({id}).getBoundingClientRect().top"
                    )
                )
            ),
        ],
        id=id,
        class_name=(
            "relative w-full after:content[''] after:absolute after:z-[1] after:bg-slate-3 after:left-0 after:top-[-1px] after:w-full after:h-[1px] before:content[''] before:absolute before:z-[1] before:bg-slate-3 before:top-0 before:left-[-1px] before:h-full before:w-[1px] group",
            rx.cond(
                name == "STATS",
                "col-span-2",
                "",
            ),
        ),
        on_click=rx.cond(
            companies_case_studies_var.contains(name)
            & companies_case_studies_var[name].get("url", None),
            rx.redirect(companies_case_studies_var[name].get("url", "#")),
            rx.noop(),
        ),
    )


def companies() -> rx.Component:
    return rx.el.section(
        rx.box(class_name="h-[3rem] w-full border-b border-slate-3 lg:flex hidden"),
        rx.box(
            *[
                company_card(
                    name=company,
                    id=f"landing-company-card-{company}",
                )
                for company in companies_list
            ],
            class_name="lg:grid grid-cols-6 w-full hidden relative",
        ),
        rx.el.div(
            index_companies(),
            class_name="lg:hidden flex border-t border-slate-3 lg:border-t-0",
        ),
        class_name="flex flex-col justify-center items-center mx-auto w-full max-w-[64.19rem] border-slate-3 relative z-[1] overflow-hidden isolate lg:border-b lg:border-x",
    )
