import reflex as rx
from pcweb.components.icons.icons import get_icon
from pcweb.pages.docs import (
    getting_started,
)
from pcweb.constants import REFLEX_CLOUD_URL, REFLEX_BUILD_URL


def product_card(
    number: int,
    name: str,
    title: str,
    description: str,
    link: str,
    url: str,
    color: tuple[str, str],
    graphic: str,
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(title, class_name="text-slate-12 text-xl font-semibold"),
            rx.el.span(description, class_name="text-slate-9 text-sm font-medium"),
            rx.link(
                rx.el.span(
                    link,
                    class_name="text-sm font-medium text-slate-12 underline-none hover:text-slate-12",
                ),
                get_icon(
                    "chevron_right",
                    class_name="size-4 text-slate-9 group-hover:text-slate-12 group-hover:translate-x-1 transition-all duration-300",
                ),
                href=url,
                underline="none",
                class_name="flex flex-row gap-2 items-center gap-[0.375rem] mt-4 group",
            ),
            class_name="flex flex-col gap-2 px-10 pb-10 pt-6",
        ),
        rx.el.div(
            rx.el.span(number),
            rx.el.span(name),
            rx.image(
                src=f"/landing/lines/light/lines_{color[0]}.webp",
                class_name="h-6 w-auto pointer-events-none",
            ),
            class_name=f"flex flex-row gap-5 items-center px-3.5 h-10 font-mono text-xs font-medium text-{color[0]}-{color[1]} overflow-hidden",
        ),
        rx.el.div(
            rx.image(
                src=f"/landing/products/light/product_{graphic}.webp",
                class_name="w-auto pointer-events-none block dark:hidden",
            ),
            rx.image(
                src=f"/landing/products/dark/product_{graphic}.webp",
                class_name="w-auto pointer-events-none hidden dark:block",
            ),
        ),
        class_name="flex flex-col divide-y divide-slate-3",
    )


def products() -> rx.Component:
    return rx.el.section(
        product_card(
            1,
            "AI Builder",
            "Generate Your App With AI",
            "Describe your idea, and let AI turn it into a full-stack Python app.",
            "Explore Gallery",
            REFLEX_BUILD_URL,
            ("violet", "9"),
            "ai",
        ),
        product_card(
            2,
            "Reflex Framework",
            "Iterate In Python With Reflex",
            "Build and refine your app using pure Python—fast, flexible, and scalable.",
            "Get Started In Docs",
            getting_started.introduction.path,
            ("jade", "10"),
            "framework",
        ),
        product_card(
            3,
            "Hosting Platform",
            "Deploy, Host, and Scale",
            "Launch your app instantly with Reflex's powerful hosting platform.",
            "Start Building",
            REFLEX_CLOUD_URL,
            ("amber", "11"),
            "hosting",
        ),
        class_name="grid grid-cols-1 md:grid-cols-3 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 lg:divide-x divide-slate-3 lg:border-y",
    )
