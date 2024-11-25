import reflex as rx
from pcweb.components.hosting_banner import HostingBannerState


def header() -> rx.Component:
    return rx.box(
        rx.el.h1(
            "Find a plan that's right for you",
            class_name="gradient-heading font-semibold text-4xl xl:text-5xl text-center",
        ),
        rx.el.h2(
            "Start for free using the open-source and scale as you grow.",
            class_name="font-medium text-slate-9 text-lg text-center text-wrap",
        ),
        class_name="flex flex-col gap-4 justify-center items-center max-w-[64.19rem] 2xl:border-x border-slate-4 w-full pb-16 "
        + rx.cond(HostingBannerState.show_banner, "pt-[13rem]", "pt-[10rem]"),
    )
