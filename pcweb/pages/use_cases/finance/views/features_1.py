import reflex as rx

from pcweb.pages.use_cases.common.features_1 import feature_card


def features_1() -> rx.Component:
    return rx.el.section(
        feature_card(
            "ArtificialIntelligence04Icon",
            "Ship AI-Powered Tools Securely",
            "Build chat-based assistants and RAG apps in Python, deployed inside your own cloud or on-prem, with full control over where data lives.",
        ),
        feature_card(
            "RepeatIcon",
            "Modernize Legacy Internal Apps",
            "Replace fragile in-house dashboards with maintainable Python apps that plug into your existing data stack.",
        ),
        feature_card(
            "FlowConnectionIcon",
            "Automate Workflows, Not Just Reports",
            "Turn manual compliance checks, KYC workflows, and operations processes into interactive apps—tied to your systems, not screenshots.",
        ),
        feature_card(
            "Layers01Icon",
            "Orchestrate End-to-End Lifecycles",
            "Let researchers, analysts, and quants move from 'run a script in a Jupyter notebook' to 'share a full app' using the same language they already know.",
        ),
        class_name="grid lg:grid-cols-2 grid-cols-1 mx-auto w-full max-w-[64.19rem] lg:border-l border-slate-3 relative overflow-hidden border-t",
    )
