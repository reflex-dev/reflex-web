import reflex as rx

from pcweb.components.icons import get_icon
from pcweb.components.icons.hugeicons import hi


def header() -> rx.Component:
    return rx.box(
        rx.image(
            src="/landing/patterns/light/pattern_hosting.webp",
            class_name="absolute top-0 left-0 w-full h-full object-cover pointer-events-none",
        ),
        rx.box(
            hi("cloud-server", class_name="shrink-0"),
            rx.el.span("Hosting Platform", class_name="text-sm font-semibold"),
            class_name="flex flex-row gap-2 items-center text-amber-11",
        ),
        rx.el.h2(
            """Deploy, manage, and scale.
A complete infrastructure for your app""",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            """Deploy anywhere — Reflex supports all major cloud providers,
including Databricks, AWS, GCP, Azure, Snowflake and more.""",
            class_name="text-slate-11 text-sm font-medium text-center text-balance word-wrap break-words md:whitespace-pre pb-6",
        ),
        rx.image(
            src="/hosting_graphing.svg",
            class_name="h-auto max-w-[25rem] w-full mx-auto",
        ),
        class_name="flex flex-col gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 p-10 justify-center items-center relative overflow-hidden h-[22.75rem] border-b border-slate-3",
    )


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.box(
        rx.box(
            get_icon(icon, class_name="!text-slate-9 !size-5"),
            rx.text(title, class_name="text-slate-12 text-base font-semibold"),
            class_name="flex flex-row gap-2 items-center",
        ),
        rx.text(description, class_name="text-slate-9 font-medium text-sm text-start"),
        class_name="flex flex-col gap-2 w-full lg:w-[22rem] h-[8rem] px-8 py-5",
    )


def content() -> rx.Component:
    return rx.box(
        rx.box(
            feature_card(
                "backend_db",
                "Build and deploy",
                "Deploy and scale your Reflex app with a single command.",
            ),
            feature_card(
                "backend_auth",
                "Add team members",
                "Invite team members to your Reflex app and manage their permissions.",
            ),
            feature_card(
                "infinity",
                "Integrate with CI/CD",
                "Deploy via GitHub Actions, GitLab CI, or your own custom pipeline.",
            ),
            feature_card(
                "globe",
                "Scale to multiple regions",
                "Deploy your app to multiple regions for high availability and low latency.",
            ),
            feature_card(
                "analytics",
                "Get alerts and metrics",
                "Get alerts and metrics for your Reflex app to help you monitor and optimize your app.",
            ),
            class_name="flex flex-col max-w-full lg:max-w-[21.4375rem] divide-y divide-slate-3",
        ),
        rx.box(
            rx.image(
                src="/landing/hosting_features/light/card.webp",
                class_name="absolute top-0 left-0 w-full h-full object-cover pointer-events-none dark:hidden",
            ),
            rx.image(
                src="/landing/hosting_features/dark/card.webp",
                class_name="absolute top-0 left-0 w-full h-full object-cover pointer-events-none dark:block hidden",
            ),
            class_name="justify-center items-center relative overflow-hidden w-full lg:flex hidden",
        ),
        class_name="flex flex-col lg:flex-row max-w-[64.19rem] mx-auto w-full border-x-0 lg:border-x border-slate-3 divide-x-0 lg:divide-x divide-slate-3",
    )


def graph() -> rx.Component:
    return rx.box(
        rx.image(
            src="/hosting_graphing.svg",
            class_name="w-full h-[10rem]",
        ),
        class_name="flex flex-col lg:flex-row max-w-[64.19rem] mx-auto w-full border-x-0 lg:border-x border-slate-3 divide-x-0 lg:divide-x divide-slate-3 p-10",
    )


def hosting_section() -> rx.Component:
    return rx.el.section(
        header(),
        # graph(),
        content(),
        class_name="flex flex-col mx-auto w-full max-w-[84.19rem] relative",
    )
