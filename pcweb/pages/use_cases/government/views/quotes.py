import reflex as rx

from pcweb.pages.use_cases.common.quote import quote_card


def quotes() -> rx.Component:
    return rx.el.section(
        quote_card(
            "Replace brittle Tableau/Streamlit prototypes with production apps.",
            "Go straight from idea to production, without the “prototype then rebuild” cycle",
            "At the World Bank, teams were stuck jumping between Tableau dashboards, Streamlit prototypes, and custom JavaScript apps. With Reflex, they’re building production-grade data platforms from day one, including a chat-driven data app with AG Grid tables and an AI-powered legal assistant that lets 100+ lawyers and investigators query internal documents securely within the Bank's Azure environment.",
            '"You wouldn’t want to use Dash or Streamlit to build a real production-grade app… We have them go straight into Reflex."',
            "Data Developer, World Bank",
        ),
        quote_card(
            "Ship fintech-grade SaaS without a front-end team.",
            "From YC prototype to fintech SaaS—with no React, Dash, or front-end hires",
            "Bayesline’s founders built a full fintech risk analytics platform on Reflex—wrapping AG Grid, handling hundreds of thousands of instruments, and delivering a UI indistinguishable from a hand-coded React app. Reflex gave them ~4x faster development vs learning React and about 50% less code than their previous Dash implementation, while keeping everything in Python and avoiding the need to hire a dedicated front-end engineer.",
            '"Using Reflex instead of Plotly Dash was like the difference between organized Legos and a plate of spaghetti."',
            "Sebastian, Founder, Bayesline",
        ),
        rx.el.div(
            quote_card(
                "Automate Analytics for Internal AI Tools.",
                "Deploy Bank-Grade Internal Dashboards in Days, Not Months",
                "At Crédit Agricole CIB, Léo's R&D team turned a rough prototype into a production-grade dashboard tracking usage of a GPT-powered internal chatbot. What used to require weeks of front-end work now ships in a couple of days, inside their internal AWS environment.",
                '"It\'s like comparing a bike to a supercar. (Comparing Dash to Reflex)"',
                "Léo, Tech Lead, R&D, Crédit Agricole CIB",
            ),
            class_name="lg:col-span-2 lg:justify-self-center w-full lg:max-w-[42rem]",
        ),
        class_name="grid lg:grid-cols-2 grid-cols-1 gap-4 mx-auto w-full max-w-[84.5rem] relative overflow-hidden",
    )
