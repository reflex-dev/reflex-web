import reflex as rx

from pcweb.pages.use_cases.common.stats import stat_card


def stats() -> rx.Component:
    return rx.el.section(
        stat_card(
            "Deploy on-prem, VPC, or air-gapped",
            "Run Reflex entirely within your controlled infrastructure with complete offline operation capabilities.",
            accent=True,
        ),
        stat_card(
            "No data leaves government infrastructure",
            "All application data, user information, and processing remain within your secure environment at all times.",
            accent=True,
        ),
        stat_card(
            "Role-based access control & identity integration",
            "Integrate with existing identity providers and enforce granular permissions with SSO and SAML support.",
            accent=True,
        ),
        stat_card(
            "Full auditability and observability",
            "Complete audit logging of all user actions, data access, and system events for compliance and security reviews.",
            accent=True,
        ),
        stat_card(
            "FedRAMP and SOC 2-aligned",
            "Architecture designed to meet federal security requirements and enterprise compliance standards.",
            accent=True,
        ),
        stat_card(
            "Compatible with public sector security models",
            "Works with government-specific security and compliance requirements.",
            accent=True,
        ),
        class_name="grid lg:grid-cols-3 grid-cols-1 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden border-t lg:divide-x divide-slate-3 max-lg:divide-y",
    )
