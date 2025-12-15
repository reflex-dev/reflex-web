import reflex as rx

from pcweb.pages.use_cases.common.quote import quote_card


def quotes() -> rx.Component:
    return rx.el.section(
        quote_card(
            "Automate Analytics for Internal AI Tools.",
            "Deploy Bank-Grade Internal Dashboards in Days, Not Months",
            "Léo's R&D team turned a rough prototype into a production-grade dashboard tracking usage of a GPT-powered internal chatbot. What used to require weeks of front-end work now ships in a couple of days, inside their internal AWS environment.",
            '"—It\'s like comparing a bike to a supercar. (Comparing Dash to Reflex)"',
            "FirstName LastName, Crédit Agricole CIB",
        ),
        quote_card(
            "Automate Analytics for Internal AI Tools.",
            "Deploy Bank-Grade Internal Dashboards in Days, Not Months",
            "Léo's R&D team turned a rough prototype into a production-grade dashboard tracking usage of a GPT-powered internal chatbot. What used to require weeks of front-end work now ships in a couple of days, inside their internal AWS environment.",
            '"—It\'s like comparing a bike to a supercar. (Comparing Dash to Reflex)"',
            "FirstName LastName, Crédit Agricole CIB",
        ),
        quote_card(
            "Automate Analytics for Internal AI Tools.",
            "Deploy Bank-Grade Internal Dashboards in Days, Not Months",
            "Léo's R&D team turned a rough prototype into a production-grade dashboard tracking usage of a GPT-powered internal chatbot. What used to require weeks of front-end work now ships in a couple of days, inside their internal AWS environment.",
            '"—It\'s like comparing a bike to a supercar. (Comparing Dash to Reflex)"',
            "FirstName LastName, Crédit Agricole CIB",
        ),
        quote_card(
            "Automate Analytics for Internal AI Tools.",
            "Deploy Bank-Grade Internal Dashboards in Days, Not Months",
            "Léo's R&D team turned a rough prototype into a production-grade dashboard tracking usage of a GPT-powered internal chatbot. What used to require weeks of front-end work now ships in a couple of days, inside their internal AWS environment.",
            '"—It\'s like comparing a bike to a supercar. (Comparing Dash to Reflex)"',
            "FirstName LastName, Crédit Agricole CIB",
        ),
        class_name="grid lg:grid-cols-2 grid-cols-1 gap-4 mx-auto w-full max-w-[84.5rem] relative overflow-hidden",
    )
