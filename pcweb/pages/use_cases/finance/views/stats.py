import reflex as rx

from pcweb.pages.use_cases.common.stats import stat_card


def stats() -> rx.Component:
    return rx.el.section(
        stat_card(
            "Faster Development",
            "Vs. legacy front-end stacks (Crédit Agricole CIB)",
            "10x",
        ),
        stat_card(
            "Legal Professionals",
            "Using AI tools replacing Streamlit (World Bank)",
            "100+",
        ),
        stat_card(
            "Faster & 50% Less Code",
            "Vs. Dash/React for fintech analytics (Bayesline)",
            "4x",
        ),
        class_name="grid lg:grid-cols-3 grid-cols-1 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden border-t lg:divide-x divide-slate-3 max-lg:divide-y",
    )
