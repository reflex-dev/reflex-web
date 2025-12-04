import reflex as rx

from pcweb.components.icons.icons import get_icon
from pcweb.pages.docs import getting_started


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
            rx.el.span(description, class_name="text-secondary-11 text-sm font-medium"),
            class_name="flex flex-col gap-2 px-10 pt-10",
        ),
        rx.el.div(
            rx.image(
                src=f"/landing/products/light/product_{graphic}.avif",
                loading="lazy",
                alt=f"{name} product image light",
                class_name="w-auto pointer-events-none block dark:hidden",
            ),
            rx.image(
                src=f"/landing/products/dark/product_{graphic}.avif",
                loading="lazy",
                alt=f"{name} product image dark",
                class_name="w-auto pointer-events-none hidden dark:block",
            ),
            class_name="w-full max-h-[17.25rem] h-full overflow-hidden",
        ),
        rx.el.a(
            rx.el.span(
                link,
                class_name="text-sm font-medium text-slate-12 underline-none hover:text-slate-12",
            ),
            get_icon(
                "chevron_right",
                class_name="size-4 text-secondary-11 group-hover:text-slate-12 group-hover:translate-x-1 transition-all duration-300",
            ),
            to=url,
            class_name="flex flex-row items-center gap-2 justify-between group h-[4rem] px-10 hover:bg-slate-2 transition-colors border-t max-lg:border-b border-slate-3",
        ),
        class_name="flex flex-col",
    )


def products() -> rx.Component:
    return rx.el.section(
        product_card(
            1,
            "AI Builder",
            "Generate Your App With AI",
            "Describe your idea, and let AI transform it into a complete, production-ready Python web application.",
            "View Use Cases",
            "/use-cases",
            ("violet", "9"),
            "ai",
        ),
        product_card(
            2,
            "Reflex Framework",
            "Iterate In Python With Reflex",
            "Build and refine your app using pure Python—fast, flexible, scalable, and open source.",
            "Get Started In Docs",
            getting_started.introduction.path,
            ("jade", "10"),
            "framework",
        ),
        product_card(
            3,
            "Hosting Platform",
            "Deploy, Host, and Scale",
            "Deploy through Databricks, Snowflake, self-host on AWS, GCP, Azure, or use Reflex Cloud.",
            "Explore Hosting Options",
            "/hosting",
            ("amber", "11"),
            "hosting",
        ),
        class_name="grid grid-cols-1 lg:grid-cols-3 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 lg:divide-x divide-slate-3 lg:border-t",
    )
