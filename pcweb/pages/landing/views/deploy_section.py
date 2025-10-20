import reflex as rx
import reflex_ui as ui

from pcweb.components.icons.icons import get_icon
from pcweb.components.numbers_pattern import numbers_pattern
from pcweb.constants import REFLEX_CLOUD_URL
from pcweb.pages.databricks.databricks import databricks_page
from pcweb.pages.hosting.views.deploy_animation import animated_box
from pcweb.pages.security.security import security_page


def header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            ui.icon("CloudServerIcon", class_name="shrink-0"),
            rx.el.span(
                "Hosting",
                class_name="text-sm font-semibold",
            ),
            class_name="flex flex-row gap-2 items-center text-primary-9",
        ),
        rx.el.h2(
            "Deploy, manage, and scale.",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            "A complete infrastructure for your apps.",
            class_name="text-slate-9 text-sm font-medium text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        class_name="flex flex-col gap-4 items-center mx-auto w-full relative overflow-hidden",
    )


def deploy_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.html(
                """<svg xmlns="http://www.w3.org/2000/svg" width="342" height="322" viewBox="0 0 342 322" fill="none">
  <g filter="url(#filter0_f_10857_12767)">
    <path d="M229.949 96.5486C278.245 98.9569 202.581 123.44 198.154 159.563C193.726 195.686 216.25 229 176.018 229C135.785 229 165.151 137.087 98.7436 118.222C32.3361 99.3581 181.652 94.1404 229.949 96.5486Z" fill="#261958"/>
  </g>
  <defs>
    <filter id="filter0_f_10857_12767" x="-14" y="0" width="356" height="325" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="48" result="effect1_foregroundBlur_10857_12767"/>
    </filter>
  </defs>
</svg>""",
                class_name="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 object-cover pointer-events-none z-[0] dark:block hidden",
            ),
            rx.html(
                """<svg xmlns="http://www.w3.org/2000/svg" width="342" height="322" viewBox="0 0 342 322" fill="none">
  <g filter="url(#filter0_f_10857_13202)">
    <path d="M229.949 96.5486C278.245 98.9569 202.581 123.44 198.154 159.563C193.726 195.686 216.25 229 176.018 229C135.785 229 165.151 137.087 98.7436 118.222C32.3361 99.3581 181.652 94.1404 229.949 96.5486Z" fill="#F4F0FE"/>
  </g>
  <defs>
    <filter id="filter0_f_10857_13202" x="-14" y="0" width="356" height="325" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="48" result="effect1_foregroundBlur_10857_13202"/>
    </filter>
  </defs>
</svg>""",
                class_name="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 object-cover pointer-events-none z-[0] dark:hidden",
            ),
            rx.image(
                f"/landing/deploy/{rx.color_mode_cond('light', 'dark')}/deploy_visual.webp",
                class_name="h-[8.5rem] w-auto ml-[6rem] z-[1] block",
            ),
            class_name="relative flex flex-col max-lg:hidden",
        ),
        rx.el.div(
            rx.el.span(
                "Deploy your app with a single command.",
                class_name="text-slate-12 lg:text-3xl text-2xl font-semibold",
            ),
            rx.el.span(
                "Performant, secure, and scalable.",
                class_name="text-slate-9 lg:text-3xl text-2xl font-semibold",
            ),
            rx.el.div(
                rx.image(
                    src="/hosting_graphing.svg",
                    class_name="w-auto h-[1.95rem]",
                ),
                ui.link(
                    render_=ui.button(
                        "Start deploying",
                        variant="primary",
                        size="lg",
                        class_name="font-semibold h-10 w-fit",
                    ),
                    to=REFLEX_CLOUD_URL,
                    target="_blank",
                ),
                class_name="flex flex-col lg:flex-row lg:gap-8 gap-6 items-center mt-8 max-lg:w-full max-lg:justify-start max-lg:items-start",
            ),
            class_name="flex flex-col items-end",
        ),
        class_name="max-w-[71.125rem] w-full rounded-[1.125rem] border border-slate-3 bg-white-1 pt-[5rem] pb-[5.5rem] px-10 h-[20.5625rem] flex flex-row items-center gap-[10.5rem] z-10 shadow-small",
    )


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.box(
        rx.box(
            get_icon(icon, class_name="!text-slate-9 !size-5"),
            rx.text(title, class_name="text-slate-12 text-base font-semibold"),
            class_name="flex flex-row gap-2 items-center",
        ),
        rx.text(description, class_name="text-slate-9 font-medium text-sm text-start"),
        class_name="flex flex-col gap-2 w-full lg:w-[22.05rem] h-[8rem] px-8 py-5",
    )


def badge_card(component: rx.Component, link: str) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            component,
            class_name="size-18 rounded-lg border border-slate-5 dark:border-[#1C2024] shadow-large bg-white-1 group-hover:bg-slate-2 transition-colors flex items-center justify-center z-[2]",
        ),
        href=link,
        target="_blank",
        class_name="size-21 rounded-xl border border-slate-3 dark:border-[#1C2024] shadow-large bg-white/76 dark:bg-slate-1 z-[2] group relative cursor-pointer flex items-center justify-center",
    )


def security_badges() -> rx.Component:
    return rx.box(
        rx.box(
            badge_card(
                rx.el.div(
                    rx.el.span(
                        "AICPA",
                        class_name="text-violet-9 text-base font-semibold",
                    ),
                    rx.el.span("SOC 2", class_name="text-slate-9 text-sm font-medium"),
                    class_name="flex flex-col items-center justify-center",
                ),
                security_page.path,
            ),
            badge_card(
                rx.el.div(
                    rx.image(
                        src="/landing/integrations/light/databricks.svg",
                        class_name="h-[24px] w-auto pb-0.5",
                    ),
                    rx.el.span(
                        "Partner", class_name="text-slate-9 text-sm font-medium"
                    ),
                    class_name="flex flex-col items-center justify-center",
                ),
                databricks_page.path,
            ),
            class_name="flex flex-row gap-4 items-center justify-center",
        ),
        class_name="p-6 flex items-center justify-center",
    )


def security() -> rx.Component:
    return rx.el.div(
        rx.box(
            rx.box(
                rx.el.h2(
                    "Secure by default",
                    class_name="text-slate-12 text-xl lg:text-2xl font-semibold lg:text-start text-center",
                ),
                rx.el.h3(
                    "SOC 2 compliant with enterprise-grade security and flexible deployment options.",
                    class_name="text-slate-9 text-lg lg:text-2xl font-semibold lg:text-start text-center text-balance",
                ),
                class_name="flex flex-col lg:col-span-2 p-10 max-lg:border-b border-slate-3",
            ),
            security_badges(),
            class_name="grid grid-cols-1 lg:grid-cols-3 lg:divide-x divide-slate-4 w-full",
        ),
        class_name="flex flex-col gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x justify-center items-center relative overflow-hidden border-slate-3 border-b",
    )


def deploy_content() -> rx.Component:
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
            class_name="flex flex-col max-w-full lg:max-w-full divide-y divide-slate-3",
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
        class_name="flex flex-col lg:flex-row mx-auto w-full border-x-0 divide-x-0 lg:divide-x divide-slate-3 border-t border-slate-3",
    )


def deploy_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                numbers_pattern(side="left", class_name="left-0 top-0"),
                numbers_pattern(side="right", class_name="right-0 top-0"),
                header(),
                rx.el.div(
                    animated_box(),
                    class_name="flex justify-center items-center pt-[3.75rem] w-full",
                ),
                class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] relative overflow-hidden pt-20 border-t border-slate-3",
            ),
            deploy_content(),
            class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3",
        ),
        deploy_card(),
        security(),
        class_name="flex flex-col items-center mx-auto w-full",
    )
