import reflex as rx

from pcweb.components.button import button
from pcweb.templates.webpage import webpage


def affiliates_title():
    return rx.box(
        rx.heading(
            "Reflex Affiliate Program",
            class_name="gradient-heading font-x-large lg:font-xxx-large text-start text-transparent lg:text-center",
        ),
        rx.text(
            "Earn 50% of your referrals’ subscription revenue for their first six months—start earning today!",
            class_name="font-md text-balance text-slate-9",
        ),
        class_name="section-header",
    )


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                # get_icon(icon, class_name="!text-slate-12 !size-5"),
                rx.text(title, class_name="text-slate-12 text-base font-medium"),
                class_name="flex flex-row gap-2 items-center",
            ),
            rx.text(
                description, class_name="text-slate-9 font-medium text-sm text-start"
            ),
            class_name="flex flex-col gap-2 w-[22rem] h-[9rem] px-8 py-6",
        ),
        class_name="border-slate-3 border-b box-border",
    )


def step_box(step_number: str) -> rx.Component:
    """Helper function to create a step number box with consistent styling."""
    return rx.box(
        rx.text(
            f"Step {step_number}",
            class_name="text-md font-semibold text-center text-slate-10",
        ),
        color=rx.color("accent", 5),
        class_name="h-[5rem] flex items-center justify-center p-3 col-start-2 row-span-full row-start-1 bg-[size:10px_10px] bg-fixed bg-[image:repeating-linear-gradient(315deg,currentColor_0,currentColor_1px,_transparent_0,_transparent_50%)]",
    )


def spacer() -> rx.Component:
    """Helper function to create a consistent height spacer."""
    return rx.box(class_name="h-[4rem]")


def features() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.box(
                # Left column with steps 2 and 4
                feature_card(
                    "backend_db",
                    "Submit Your Application",
                    "Provide your basic info to get a unique affiliate link.",
                ),
                step_box("2"),
                feature_card(
                    "infinity",
                    "Track Your Referrals",
                    "Log in to your Affiliate Dashboard to see clicks, sign‑ups, and revenue data.",
                ),
                step_box("4"),
                spacer(),
                class_name="flex flex-col pt-8 lg:border-r border-slate-3",
            ),
            rx.box(
                # Right column with steps 1 and 3
                spacer(),
                step_box("1"),
                feature_card(
                    "backend_auth",
                    "Share Reflex",
                    "Post your link anywhere—blog posts, social media, email newsletters, even your YouTube channel.",
                ),
                step_box("3"),
                feature_card(
                    "analytics",
                    "Get Paid",
                    "We'll send you 50% of each referred user's subscription revenue for their first six months.",
                ),
                class_name="flex flex-col -mt-[32px]",
            ),
            class_name="flex lg:flex-row flex-col justify-center items-center",
        ),
        rx.link(
            button("Become a Partner", variant="primary", size="xl"),
            href="https://cal.com/forms/09dc3703-39fc-42ec-b03b-8ee32de7590f",
            is_external=True,
            class_name="p-2 border border-slate-3 rounded-[1.375rem] border-solid lg:mt-0 mt-4",
        ),
        class_name="flex flex-col justify-center items-center max-w-[64.19rem] lg:border-x border-slate-3 w-full mx-auto lg:pb-[5.5rem] pb-4 relative overflow-hidden pt-6",
    )


def features_small_screen():
    return rx.box(
        rx.box(
            rx.box(
                step_box("1"),
                feature_card(
                    "backend_db",
                    "Submit Your Application",
                    "Provide your basic info to get a unique affiliate link.",
                ),
                class_name="flex flex-col",
            ),
            rx.box(
                step_box("2"),
                feature_card(
                    "backend_auth",
                    "Share Reflex",
                    "Post your link anywhere—blog posts, social media, email newsletters, even your YouTube channel.",
                ),
                class_name="flex flex-col",
            ),
            rx.box(
                step_box("3"),
                feature_card(
                    "infinity",
                    "Track Your Referrals",
                    "Log in to your Affiliate Dashboard to see clicks, sign‑ups, and revenue data.",
                ),
                class_name="flex flex-col",
            ),
            rx.box(
                step_box("4"),
                feature_card(
                    "analytics",
                    "Get Paid",
                    "We'll send you 50% of each referred user's subscription revenue for their first six months.",
                ),
                class_name="flex flex-col",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
        ),
        rx.box(
            rx.link(
                button("Become a Partner", variant="primary", size="xl"),
                href="https://cal.com/forms/09dc3703-39fc-42ec-b03b-8ee32de7590f",
                is_external=True,
                class_name="p-2 border border-slate-3 rounded-[1.375rem] border-solid lg:mt-0 mt-4",
            ),
            class_name="flex items-center justify-center",
        ),
        class_name="flex flex-col justify-center",
    )


@webpage(path="/affiliates", title="Affiliates · Reflex")
def affiliates() -> rx.Component:
    return rx.el.section(
        affiliates_title(),
        rx.box(
            features(),
            class_name="hidden lg:block",  # Hide by default, show on lg screens and up
        ),
        rx.box(
            features_small_screen(),
            class_name="block lg:hidden",  # Show by default, hide on lg screens and up
        ),
        id="affiliates",
        class_name="section-content",
    )
