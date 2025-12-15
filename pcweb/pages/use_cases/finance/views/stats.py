import reflex as rx

from pcweb.pages.use_cases.common.stats import stat_card


def stats() -> rx.Component:
    return rx.el.section(
        stat_card(
            "10x",
            "Faster Development",
            "Vs. legacy front-end stacks (Crédit Agricole CIB)",
        ),
        stat_card(
            "50+",
            "Quant Researchers",
            "Building dashboards in Python (Man Group)",
        ),
        stat_card(
            "100+",
            "Legal Professionals",
            "Using AI tools replacing Tableau (World Bank)",
        ),
        stat_card(
            "4x",
            "Faster & 50% Less Code",
            "Vs. Dash/React for fintech analytics (Bayesline)",
        ),
        class_name="grid lg:grid-cols-4 grid-cols-1 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden border-t lg:divide-x divide-slate-3 max-lg:divide-y",
    )
