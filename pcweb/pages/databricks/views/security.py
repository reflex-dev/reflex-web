import reflex as rx


def badge_card(component: rx.Component, link: str) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            component,
            class_name="size-18 rounded-lg border border-slate-5 dark:border-[#1C2024] shadow-large bg-white-1 group-hover:bg-slate-2 transition-colors flex items-center justify-center z-[2]",
        ),
        href=link,
        target="_blank",
        class_name="size-21 rounded-xl border border-slate-3 dark:border-[#1C2024] shadow-large bg-white/76 dark:bg-slate-1 z-[2] group relative cursor-pointer flex items-center justify-center",
    )


def security_badges() -> rx.Component:
    from pcweb.pages.databricks.databricks import databricks_page
    from pcweb.pages.security.security import security_page

    return rx.box(
        rx.box(
            badge_card(
                rx.el.div(
                    rx.el.span(
                        "AICPA",
                        class_name="text-violet-9 text-base font-semibold",
                    ),
                    rx.el.span("SOC 2", class_name="text-slate-9 text-sm font-medium"),
                    class_name="flex flex-col items-center justify-center",
                ),
                security_page.path,
            ),
            badge_card(
                rx.el.div(
                    rx.image(
                        src="/landing/integrations/light/databricks.svg",
                        class_name="h-[24px] w-auto pb-0.5",
                    ),
                    rx.el.span(
                        "Partner", class_name="text-slate-9 text-sm font-medium"
                    ),
                    class_name="flex flex-col items-center justify-center",
                ),
                databricks_page.path,
            ),
            class_name="flex flex-row gap-4 items-center justify-center",
        ),
        class_name="p-6 flex items-center justify-center",
    )


def security() -> rx.Component:
    return rx.el.div(
        rx.box(
            rx.box(
                rx.el.h2(
                    "Secure by default",
                    class_name="text-slate-12 text-xl lg:text-2xl font-semibold lg:text-start text-center",
                ),
                rx.el.h3(
                    "Deploy directly in your databricks app account, fast and secure.",
                    class_name="text-slate-9 text-lg lg:text-2xl font-semibold lg:text-start text-center text-balance",
                ),
                class_name="flex flex-col lg:col-span-2 p-10 max-lg:border-b border-slate-3",
            ),
            security_badges(),
            class_name="grid grid-cols-1 lg:grid-cols-3 lg:divide-x divide-slate-4 w-full",
        ),
        class_name="flex flex-col gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x justify-center items-center relative overflow-hidden border-slate-3 border-b",
    )
