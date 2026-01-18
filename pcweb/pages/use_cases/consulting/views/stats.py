import reflex as rx

from pcweb.pages.use_cases.common.stats import stat_card


def stats() -> rx.Component:
    return rx.el.section(
        stat_card(
            "Self-host in client VPCs or on-prem",
            "Deploy Reflex apps entirely within client-approved infrastructure for maximum security and compliance.",
            accent=True,
        ),
        stat_card(
            "No data leaves client infrastructure",
            "All application data and processing remain within the client's secure environment at all times.",
            accent=True,
        ),
        stat_card(
            "Enterprise authentication & RBAC",
            "Integrate with client identity providers and enforce role-based access control with SSO support.",
            accent=True,
        ),
        stat_card(
            "Auditability and observability built in",
            "Complete logging of user actions, data access, and system events for compliance and security reviews.",
            accent=True,
        ),
        stat_card(
            "Compatible with regulated industries",
            "Works with finance, healthcare, energy, and public sector compliance frameworks and security requirements.",
            accent=True,
        ),
        stat_card(
            "No vendor lock-in",
            "Clients own the code and infrastructure completely, ensuring long-term control and flexibility.",
            accent=True,
        ),
        class_name="grid lg:grid-cols-3 grid-cols-1 mx-auto w-full max-w-[64.19rem]  border-slate-3 relative overflow-hidden border-t max-lg:divide-y lg:border-l",
    )
