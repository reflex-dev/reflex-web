import reflex as rx

from pcweb.components.icons import get_icon


def feature_card(icon: str, stat: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        get_icon(icon, class_name="text-m-violet-9 dark:text-m-violet-10 shrink-0"),
        rx.el.span(
            stat,
            class_name="font-semibold text-m-violet-9 dark:text-m-violet-10 text-sm mt-4",
        ),
        rx.el.span(title, class_name="font-semibold text-slate-12 text-lg mt-4"),
        rx.el.p(
            description,
            class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium mt-2",
        ),
        class_name="flex flex-col items-start p-10",
    )


def features_2() -> rx.Component:
    return rx.el.section(
        feature_card(
            "zap-01",
            "Speed to Production",
            "Ship Internal Tools 10x Faster",
            "Reflex lets Python teams build production-grade apps without leaving their language. Crédit Agricole’s R&D team built a full chatbot analytics dashboard in two days and is rolling it out to 100+ users, without adding a single React engineer.",
        ),
        feature_card(
            "python-01",
            "Python-first Flexibility",
            "Let Experts Build, Not Just Consume",
            "At Man Group, 50+ researchers write Python, not JavaScript. Reflex gives them a full-Python framework to create dashboards and model views without touching javascript front-end code, while the platform team wraps their internal design system.",
        ),
        feature_card(
            "shield-key",
            "Full Control & Enterprise Deployment",
            "Run in Your Cloud, Offline if Needed",
            "Reflex Enterprise runs fully on-prem or in your own cloud. Man Group deploys Reflex apps in air-gapped environments; CACIB and the World Bank run Reflex inside internal AWS and Azure environments with their own SSO, logging, and infra.",
        ),
        feature_card(
            "chart-up",
            "Agility & Cost Efficiency",
            "Do More With Your Python Team",
            "Bayesline avoided hiring a front-end engineer and shipped a fintech SaaS app entirely in Python; One engineer can do the work of two by collapsing front- and back-end into a single Reflex codebase.",
        ),
        class_name="grid lg:grid-cols-4 grid-cols-1 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden border-t lg:divide-x divide-slate-3 max-lg:divide-y",
    )
