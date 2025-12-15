import reflex as rx


def card(h1: str, h2: str, description: str, quote: str, name: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(h1, class_name="text-slate-12 text-2xl font-semibold"),
                rx.el.h2(
                    h2,
                    class_name="text-m-violet-11 dark:text-m-violet-10 text-2xl font-semibold",
                ),
                class_name="flex flex-col",
            ),
            rx.el.p(
                description,
                class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium",
            ),
            class_name="flex flex-col gap-6 border-b border-m-slate-4 dark:border-m-slate-12 p-10",
        ),
        rx.el.div(
            rx.el.p(quote, class_name="text-slate-12 text-lg font-semibold"),
            rx.el.p(
                name,
                class_name="text-m-slate-11 dark:text-m-slate-9 text-base font-medium",
            ),
            class_name="flex flex-col gap-2 p-10",
        ),
        class_name="flex flex-col border border-m-slate-4 dark:border-m-slate-12 shadow-small rounded-[1.125rem] bg-white-1 dark:bg-m-slate-14",
    )


def quotes() -> rx.Component:
    return rx.el.section(
        card(
            "Automate Analytics for Internal AI Tools.",
            "Deploy Bank-Grade Internal Dashboards in Days, Not Months",
            "Léo's R&D team turned a rough prototype into a production-grade dashboard tracking usage of a GPT-powered internal chatbot. What used to require weeks of front-end work now ships in a couple of days, inside their internal AWS environment.",
            '"—It\'s like comparing a bike to a supercar. (Comparing Dash to Reflex)"',
            "FirstName LastName, Crédit Agricole CIB",
        ),
        card(
            "Automate Analytics for Internal AI Tools.",
            "Deploy Bank-Grade Internal Dashboards in Days, Not Months",
            "Léo's R&D team turned a rough prototype into a production-grade dashboard tracking usage of a GPT-powered internal chatbot. What used to require weeks of front-end work now ships in a couple of days, inside their internal AWS environment.",
            '"—It\'s like comparing a bike to a supercar. (Comparing Dash to Reflex)"',
            "FirstName LastName, Crédit Agricole CIB",
        ),
        card(
            "Automate Analytics for Internal AI Tools.",
            "Deploy Bank-Grade Internal Dashboards in Days, Not Months",
            "Léo's R&D team turned a rough prototype into a production-grade dashboard tracking usage of a GPT-powered internal chatbot. What used to require weeks of front-end work now ships in a couple of days, inside their internal AWS environment.",
            '"—It\'s like comparing a bike to a supercar. (Comparing Dash to Reflex)"',
            "FirstName LastName, Crédit Agricole CIB",
        ),
        card(
            "Automate Analytics for Internal AI Tools.",
            "Deploy Bank-Grade Internal Dashboards in Days, Not Months",
            "Léo's R&D team turned a rough prototype into a production-grade dashboard tracking usage of a GPT-powered internal chatbot. What used to require weeks of front-end work now ships in a couple of days, inside their internal AWS environment.",
            '"—It\'s like comparing a bike to a supercar. (Comparing Dash to Reflex)"',
            "FirstName LastName, Crédit Agricole CIB",
        ),
        class_name="grid lg:grid-cols-2 grid-cols-1 gap-4 mx-auto w-full max-w-[84.5rem] relative overflow-hidden",
    )
