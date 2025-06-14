import reflex as rx
from pcweb.components.hosting_banner import HostingBannerState


def header() -> rx.Component:
    return rx.box(
        rx.el.h1(
            "Get a custom quote",
            class_name="gradient-heading font-semibold text-3xl lg:text-5xl text-center",
        ),
        rx.el.p(
            "The complete platform for building and deploying your apps.",
            class_name="text-slate-9 text-md lg:text-xl font-semibold text-center",
        ),
        class_name="flex flex-col gap-2 justify-center items-center max-w-[64.19rem] 2xl:border-x border-slate-4 w-full pb-16 "
        + rx.cond(HostingBannerState.show_banner, "pt-[11rem]", "pt-[12rem]"),
    )
