import reflex as rx

from pcweb.pages.use_cases.common.stats import stat_card


def stats() -> rx.Component:
    return rx.el.section(
        stat_card(
            "Self-host anywhere",
            "VPC, on-prem, or air-gapped environments",
            accent=True,
        ),
        stat_card(
            "Full control over PHI",
            "Reflex never sees your data",
            accent=True,
        ),
        stat_card(
            "Encrypted data & secure architecture",
            "Built for enterprise healthcare security",
            accent=True,
        ),
        stat_card(
            "Role-based access control",
            "Audit trails and identity management",
            accent=True,
        ),
        stat_card(
            "HIPAA & SOC 2 compatible",
            "Deploy in compliant environments",
            accent=True,
        ),
        stat_card(
            "No vendor lock-in",
            "Own your code and infrastructure completely",
            accent=True,
        ),
        class_name="grid lg:grid-cols-3 grid-cols-1 mx-auto w-full max-w-[64.19rem]  border-slate-3 relative overflow-hidden border-t max-lg:divide-y lg:border-l",
    )
