import reflex as rx

from pcweb.components.numbers_pattern import numbers_pattern
from pcweb.pages.use_cases.common.hero import left_content, right_content


def hero() -> rx.Component:
    return rx.el.section(
        numbers_pattern(
            side="right",
            class_name="lg:top-[65px] top-[45px] lg:h-[calc(100%-65px)] h-[calc(100%-45px)] max-lg:hidden",
        ),
        rx.el.div(
            left_content(
                "Build Secure Government Apps —",
                " 10x Faster with Reflex AI",
                "The fastest way for government teams to build secure internal tools, dashboards, and AI-powered workflows using only Python. Designed for public sector constraints: security-first, auditable, and deployable entirely within government-controlled infrastructure.",
                "Book a Demo",
                "Get Started Free",
            ),
            right_content(
                [
                    (
                        "ShieldEnergyIcon",
                        "Deploy entirely on-premises, in your VPC, or in air-gapped networks",
                    ),
                    (
                        "DashboardSpeed01Icon",
                        "Build production-grade apps 10x faster using only Python",
                    ),
                    (
                        "LockIcon",
                        "Maintain full security, compliance, and audit control at all times",
                    ),
                    (
                        "DatabaseIcon",
                        "Keep all data within government-controlled infrastructure—nothing leaves your environment",
                    ),
                ],
            ),
            class_name="flex lg:flex-row flex-col lg:gap-20 gap-10 max-lg:items-center max-lg:justify-center max-lg:text-center",
        ),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-[3rem] pt-32 lg:pt-[11.5rem] lg:pb-[7.5rem] relative lg:overflow-hidden overflow-hidden z-[1] lg:px-10",
    )
