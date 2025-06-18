import reflex as rx

from pcweb.components.icons.hugeicons import hi
from pcweb.components.new_button import button
from pcweb.components.tabs import tabs

items = [
    {
        "title": "Analytics",
        "icon": "analytics-01",
        "value": "data",
        "color": "orange",
        "image": "/case_studies/analytics_dashboard.webp",
        "description": "Convert notebooks into production apps with live tables, charts, and custom components.",
    },
    {
        "title": "Finance",
        "icon": "money-02",
        "value": "financial",
        "color": "jade",
        "image": "/case_studies/bayesline_app.png",
        "description": "Financial analytics dashboard that delivers custom equity-factor risk models in minutes.",
    },
    {
        "title": "E-commerce",
        "icon": "shopping-bag-01",
        "value": "ecommerce",
        "color": "blue",
        "image": "/case_studies/sellerx_app.png",
        "description": "Unify marketplace sales, inventory alerts, and supplier data in a single dashboard.",
    },
    {
        "title": "DevOps",
        "icon": "ai-cloud-01",
        "value": "engineering",
        "color": "pink",
        "image": "/case_studies/devops_app.png",
        "description": "Surface real-time telemetry, automate routine infra tasks, and replace shell scripts with role-based web UIs",
    },
    {
        "title": "Databases",
        "icon": "database",
        "value": "database",
        "color": "gold",
        "image": "/case_studies/admin_app.png",
        "description": "Full-featured database dashboards and CRUD apps come together in minutes",
    },
    {
        "title": "AI Workflows",
        "icon": "sparkles",
        "value": "ai",
        "color": "purple",
        "image": "/case_studies/ai_workflow.webp",
        "description": "Transform unstructured content into actionable insights with OCR, speech-to-text, and LLM pipelines.",
    },
]


def tab_item(item: dict[str, str]):
    return tabs.tab(
        hi(item["icon"], class_name=f"text-{item['color']}-9", size=19),
        item["title"],
        value=item["value"],
        class_name="w-full rounded-none border border-slate-3 text-base",
    )


def tab_panel(item: dict[str, str]):
    return tabs.panel(
        rx.box(
            rx.image(
                src=item["image"],
                class_name="size-full object-cover object-left-top border border-slate-3",
            ),
            class_name="h-[550px] overflow-hidden p-3",
        ),
        rx.box(
            rx.el.p(
                item["description"], class_name="text-xl text-slate-10 font-semibold"
            ),
            class_name="p-4",
        ),
        keep_mounted=True,
        value=item["value"],
        class_name="border-t border-slate-3 flex flex-col divide-y divide-slate-3 data-[hidden]:hidden border-b",
    )


def use_cases():
    return rx.el.section(
        rx.box(
            rx.el.h3(
                "Use Cases by Industry",
                class_name="lg:text-3xl text-xl font-semibold text-slate-12 text-balance",
            ),
            rx.el.p(
                "Build internal tools, dashboards, and AI apps with Reflex.",
                class_name="lg:text-3xl text-xl font-semibold text-slate-9 text-balance",
            ),
            class_name="w-full flex flex-col gap-2 px-6 py-[3.5rem] text-center",
        ),
        tabs.root(
            rx.box(
                tabs.list(
                    *[tab_item(item) for item in items],
                    tabs.indicator(class_name="rounded-none bg-slate-4"),
                    class_name="w-full flex justify-start rounded-none bg-slate-1 gap-2",
                ),
                class_name="w-full flex justify-start px-2 py-1",
            ),
            *[tab_panel(item) for item in items],
            default_value=items[0]["value"],
            class_name="w-full flex flex-col border-t border-slate-3",
        ),
        rx.link(
            button(
                "View all use cases",
                size="lg",
                icon=rx.icon("chevron-right", size=16),
                variant="transparent",
                class_name="flex-row-reverse my-3.5",
            ),
            href="/use-cases",
        ),
        class_name="flex flex-col mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 justify-center items-center relative overflow-hidden border-y border-slate-3",
    )
