import reflex as rx
from pcweb.components.new_button import button
from pcweb.pages.docs import hosting
from pcweb.components.hosting_banner import HostingBannerState


def hero() -> rx.Component:
    """Render the hero section of the landing page."""
    return rx.el.section(
        # Headings
        rx.el.h1(
            "Deploy with a single command",
            class_name="max-w-full inline-block bg-clip-text bg-gradient-to-r from-slate-12 to-slate-11 w-full text-4xl lg:text-5xl text-center text-transparent text-balance mx-auto break-words font-semibold",
        ),
        # TODO: Change this wording
        rx.el.h2(
            """A unified platform to build and manage your Reflex apps""",
            class_name="max-w-full w-full font-large text-center text-slate-11 -mt-2 font-normal text-[1.25rem] mx-auto text-balance word-wrap break-words md:whitespace-pre",
        ),
        # Buttons
        rx.box(
            rx.link(
                button(
                    "Start deploying",
                    size="xl",
                    class_name="w-full lg:w-fit",
                ),
                underline="none",
                href=hosting.deploy_quick_start.path,
                class_name="w-full lg:w-fit",
            ),
            rx.link(
                button(
                    "Get a demo",
                    size="xl",
                    variant="secondary",
                    class_name="lg:!w-[8.25rem] w-full",
                ),
                href="/pricing",
                underline="none",
                class_name="w-full lg:w-fit",
            ),
            class_name="flex flex-col lg:flex-row items-center gap-4 mt-4 w-full lg:w-auto lg:max-w-full max-w-[24rem]",
        ),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-4 lg:pb-[7.875rem]"
        + rx.cond(
            HostingBannerState.show_banner,
            " lg:pt-[18.2rem] pt-[11rem]",
            " lg:pt-[13.2rem] pt-[6rem]",
        ),
    )
