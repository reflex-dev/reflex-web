import reflex as rx

from pcweb.components.button import button
from pcweb.components.docpage.navbar import navbar
from pcweb.components.webpage.badge import badge
from pcweb.pages.hosting.views.features import grid
from pcweb.pages.index.index_colors import index_colors
from pcweb.pages.index.views.footer_index import footer_index

numbers = {
    "1": """
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#000000" fill="none">
            <path d="M10.5 8.5L12.5 7V17" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            """,
    "2": """
           <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#000000" fill="none" class="text-purple-10">
    <path d="M9 10C9 8.34315 10.3431 7 12 7C13.6569 7 15 8.34315 15 10C15 12.0786 12.1196 13.9172 10.3503 14.8505C9.54685 15.2743 9 16.0917 9 17H15" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
    <path d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
</svg>
           
           """,
    "3": """
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#000000" fill="none">
    <path d="M12.5 12H11.5M12.5 12C13.8807 12 15 10.8807 15 9.5C15 8.11929 13.8807 7 12.5 7H11.5C10.1193 7 9 8.11929 9 9.5M12.5 12C13.8807 12 15 13.1193 15 14.5C15 15.8807 13.8807 17 12.5 17H11.5C10.1193 17 9 15.8807 9 14.5" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
    <path d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
</svg>
    """,
    "4": """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#000000" fill="none">
    <path d="M15 7V12.5M15 12.5V17M15 12.5H9.43601C9.19521 12.5 9 12.3048 9 12.064C9 12.0216 9.00619 11.9794 9.01839 11.9387L10.5 7" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
    <path d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
</svg>
    
    """,
}


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
            # rx.text(
            #     f"Step {step_number}",
            #     class_name="text-md text-center text-slate-10",
            # ),
            # rx.html(
            #     numbers[step_number],
            #     filter=rx.color_mode_cond("", "invert(0.85)"),
            # ),
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
                # Left column with steps 2 and 4
                feature_card(
                    "frame",
                    "Submit Your Application",
                    "Provide your basic info to get a unique affiliate link.",
                ),
                # step_box("2"),
                feature_card(
                    "audio-lines",
                    "Track Your Referrals",
                    "Log in to your Affiliate Dashboard to see clicks, sign‑ups, and revenue data.",
                ),
                # step_box("4"),
                spacer(),
                class_name="flex flex-col pt-8 lg:border-r border-slate-3",
            ),
            rx.box(
                # Right column with steps 1 and 3
                spacer(),
                # step_box("1"),
                feature_card(
                    "share-2",
                    "Share Reflex",
                    "Post your link anywhere—blog posts, social media, email newsletters, even your YouTube channel.",
                ),
                # step_box("3"),
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
            href="https://cal.com/forms/09dc3703-39fc-42ec-b03b-8ee32de7590f",
            is_external=True,
            class_name="p-2 border border-slate-3 rounded-[1.375rem] border-solid lg:mt-0 mt-4",
        ),
        class_name="flex flex-col justify-center items-center max-w-[64.19rem] lg:border-x border-slate-3 w-full mx-auto lg:pb-[5.5rem] pb-4 relative overflow-hidden pt-10",
    )


def features_small_screen():
    return rx.box(
        rx.box(
            rx.box(
                # step_box("1"),
                feature_card(
                    "backend_db",
                    "Submit Your Application",
                    "Provide your basic info to get a unique affiliate link.",
                ),
                class_name="flex flex-col",
            ),
            rx.box(
                # step_box("2"),
                feature_card(
                    "backend_auth",
                    "Share Reflex",
                    "Post your link anywhere—blog posts, social media, email newsletters, even your YouTube channel.",
                ),
                class_name="flex flex-col",
            ),
            rx.box(
                # step_box("3"),
                feature_card(
                    "infinity",
                    "Track Your Referrals",
                    "Log in to your Affiliate Dashboard to see clicks, sign‑ups, and revenue data.",
                ),
                class_name="flex flex-col",
            ),
            rx.box(
                # step_box("4"),
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
                class_name="p-4 border border-slate-3 rounded-[1.375rem] border-solid lg:mt-0 mt-4",
            ),
            class_name="flex items-center justify-center",
        ),
        class_name="flex flex-col justify-center",
    )


@rx.page(route="/affiliates", title="Affiliates · Reflex")
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
        badge(),
        class_name="flex flex-col w-full max-w-[94.5rem] justify-center items-center mx-auto px-4 lg:px-5 relative overflow-hidden",
    )
