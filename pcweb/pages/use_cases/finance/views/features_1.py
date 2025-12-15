import reflex as rx

from pcweb.components.icons import get_icon


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        get_icon(icon, class_name="text-m-violet-9 dark:text-m-violet-10 shrink-0"),
        rx.el.span(title, class_name="font-semibold text-slate-12 text-lg mt-2"),
        rx.el.p(
            description,
            class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium",
        ),
        class_name="flex flex-col items-start gap-2 p-10 lg:border-r border-b border-slate-3",
    )


def features_1() -> rx.Component:
    return rx.el.section(
        feature_card(
            "ai-04",
            "Ship AI-Powered Tools Securely",
            "Build chat-based assistants and RAG apps in Python, deployed inside your own cloud or on-prem, with full control over where data lives.",
        ),
        feature_card(
            "refresh-dot",
            "Modernize Legacy Internal Apps",
            "Replace fragile in-house dashboards with maintainable Python apps that plug into your existing data stack.",
        ),
        feature_card(
            "flow-connection",
            "Automate Workflows, Not Just Reports",
            "Turn manual compliance checks, KYC workflows, and operations processes into interactive apps—tied to your systems, not screenshots.",
        ),
        feature_card(
            "layers-01",
            "Orchestrate End-to-End Lifecycles",
            "Let researchers, analysts, and quants move from 'run a script in a Jupyter notebook' to 'share a full app' using the same language they already know.",
        ),
        class_name="grid lg:grid-cols-2 grid-cols-1 mx-auto w-full max-w-[64.19rem] lg:border-l border-slate-3 relative overflow-hidden border-t",
    )
