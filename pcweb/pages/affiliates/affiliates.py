import reflex as rx

from pcweb.components.button import button
from pcweb.components.docpage.navbar import navbar
from pcweb.pages.framework.index_colors import index_colors
from pcweb.pages.framework.views.footer_index import footer_index
from pcweb.pages.hosting.views.features import grid

meta_tags = [
    {"property": "og:url", "content": "https://reflex.dev/affiliates/"},
    {"property": "og:type", "content": "website"},
    {"property": "og:title", "content": "Reflex Affiliates · Earn by sharing Reflex"},
    {
        "property": "og:description",
        "content": "Join the Reflex affiliate program and earn rewards today.",
    },
    {"property": "og:image", "content": "/previews/affiliates_preview.webp"},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"property": "twitter:domain", "content": "reflex.dev"},
    {"property": "twitter:url", "content": "https://reflex.dev/affiliates/"},
    {"name": "twitter:title", "content": "Reflex Affiliate Program"},
    {
        "name": "twitter:description",
        "content": "Join the Reflex affiliate program and earn rewards today.",
    },
    {"name": "twitter:image", "content": "/previews/affiliates_preview.webp"},
]


def affiliates_title():
    return rx.box(
        rx.heading(
            "Reflex Affiliate Program",
            class_name="gradient-heading font-x-large lg:font-xxx-large text-start text-transparent lg:text-center",
        ),
        rx.text(
            "Become a Reflex partner in under 5 minutes and start earning 50% of your referrals’ subscription revenue for their first six months—join today!",
            class_name="font-md text-balance text-slate-9",
        ),
        class_name="section-header",
    )


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.icon(tag=icon, class_name="!text-slate-12 !size-5"),
                rx.text(title, class_name="text-slate-12 text-base font-medium"),
                class_name="flex flex-row gap-2 items-center",
            ),
            rx.text(
                description, class_name="text-slate-9 font-medium text-sm text-start"
            ),
            class_name="flex flex-col gap-2 w-[22rem] h-[9rem] px-1 lg:px-8 py-6",
        ),
        class_name="border-slate-3 border-b box-border",
    )


def step_box(step_number: str) -> rx.Component:
    """Helper function to create a step number box with consistent styling."""
    return rx.box(
        rx.box(
            color=rx.color("accent", 5),
            class_name="w-full h-[5rem] flex items-center justify-center p-3 col-start-2 row-span-full row-start-1 bg-[size:10px_10px] bg-fixed bg-[image:repeating-linear-gradient(315deg,currentColor_0,currentColor_1px,_transparent_0,_transparent_50%)]",
        ),
        display=["none" if i <= 3 else "flex" for i in range(6)],
        color=rx.color("accent", 4),
        class_name="w-full h-[5rem] flex items-center justify-center py-3 col-start-2 row-span-full row-start-1 bg-[size:10px_10px] bg-fixed bg-[image:repeating-linear-gradient(-315deg,currentColor_0,currentColor_1px,_transparent_0,_transparent_50%)]",
    )


def spacer() -> rx.Component:
    """Helper function to create a consistent height spacer."""
    return rx.box(class_name="h-[4rem]")


def features() -> rx.Component:
    return rx.el.section(
        grid(),
        rx.box(
            rx.box(
                feature_card(
                    "frame",
                    "Submit Your Application",
                    "Provide your basic info to get a unique affiliate link.",
                ),
                feature_card(
                    "audio-lines",
                    "Track Your Referrals",
                    "Log in to your Affiliate Dashboard to see clicks, sign‑ups, and revenue data.",  # noqa: RUF001
                ),
                spacer(),
                class_name="flex flex-col pt-8 lg:border-r border-slate-3",
            ),
            rx.box(
                # Right column with steps 1 and 3
                spacer(),
                feature_card(
                    "share-2",
                    "Share Reflex",
                    "Post your link anywhere—blog posts, social media, email newsletters, even your YouTube channel.",
                ),
                feature_card(
                    "dollar-sign",
                    "Get Paid",
                    "We'll send you 50% of each referred user's subscription revenue for their first six months.",
                ),
                class_name="flex flex-col",
            ),
            class_name="flex lg:flex-row flex-col justify-center items-center",
        ),
        rx.link(
            button("Become a Partner", variant="primary", size="xl"),
            href="https://cal.com/team/reflex/affiliate-program",
            is_external=True,
            class_name="p-3 border border-slate-3 rounded-[1.375rem] border-solid lg:mt-0 mt-4",
        ),
        class_name="flex flex-col justify-center items-center max-w-[64.19rem] lg:border-x border-slate-3 w-full mx-auto lg:pb-[5.5rem] pb-4 relative overflow-hidden pt-10",
    )


def features_small_screen():
    return rx.box(
        rx.box(
            rx.box(
                feature_card(
                    "frame",
                    "Submit Your Application",
                    "Provide your basic info to get a unique affiliate link.",
                ),
                class_name="flex flex-col",
            ),
            rx.box(
                feature_card(
                    "share-2",
                    "Share Reflex",
                    "Post your link anywhere—blog posts, social media, email newsletters, even your YouTube channel.",
                ),
                class_name="flex flex-col",
            ),
            rx.box(
                feature_card(
                    "audio-lines",
                    "Track Your Referrals",
                    "Log in to your Affiliate Dashboard to see clicks, sign‑ups, and revenue data.",  # noqa: RUF001
                ),
                class_name="flex flex-col",
            ),
            rx.box(
                feature_card(
                    "dollar-sign",
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
                href="https://cal.com/team/reflex/affiliate-program",
                is_external=True,
                class_name="p-3 border border-slate-3 rounded-[1.375rem] border-solid lg:mt-0 mt-4",
            ),
            class_name="flex items-center justify-center",
        ),
        class_name="flex flex-col justify-center",
    )


@rx.page(
    route="/affiliates",
    title="Affiliates · Reflex",
    meta=meta_tags,
)
def affiliates() -> rx.Component:
    return rx.box(
        index_colors(),
        navbar(),
        rx.el.section(
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
        ),
        footer_index(),
        class_name="flex flex-col w-full max-w-[94.5rem] justify-center items-center mx-auto px-4 lg:px-5 relative overflow-hidden",
    )
