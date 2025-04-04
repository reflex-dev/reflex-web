import reflex as rx
from pcweb.components.hosting_banner import HostingBannerState


def header() -> rx.Component:
    return rx.box(
        rx.el.h1(
            "Pricing that scales with you",
            class_name="gradient-heading font-semibold text-4xl xl:text-5xl text-center",
        ),
        rx.hstack(
            rx.el.a(
                rx.badge(
                    "Build with AI",
                    class_name="text-lg text-center text-wrap rounded-md bg-[--violet-9] flex items-center justify-center text-[#FCFCFD]",
                ),
                href="https://reflex.build",
            ),
            rx.el.a(
                rx.badge(
                    "Deploy with Cloud",
                    class_name="text-lg text-center text-wrap rounded-md bg-[--violet-9] flex items-center justify-center text-[#FCFCFD]",
                ),
                href="https://cloud.reflex.dev",
            ),
            rx.badge(
                "Scale with Enterprise",
                class_name="text-lg text-center text-wrap rounded-md bg-[--violet-9] flex items-center justify-center text-[#FCFCFD]",
            ),
            gap="2rem",
        ),
        class_name="flex flex-col gap-4 justify-center items-center max-w-[64.19rem] 2xl:border-x border-slate-4 w-full pb-16 "
        + rx.cond(HostingBannerState.show_banner, "pt-[13rem]", "pt-[10rem]"),
    )
