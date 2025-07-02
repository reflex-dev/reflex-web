"""Header section for security page."""

import reflex as rx
from pcweb.components.hosting_banner import HostingBannerState
from ..data import PAGE_CONTENT


def security_title() -> rx.Component:
    """Main title section for security page."""
    content = PAGE_CONTENT

    return rx.el.section(
        rx.el.h1(
            content["title"],
            class_name="max-w-full inline-block bg-clip-text bg-gradient-to-r from-slate-12 to-slate-11 w-full text-4xl lg:text-5xl text-center text-transparent text-balance mx-auto break-words font-semibold",
        ),
        rx.el.h2(
            content["subtitle"],
            class_name="max-w-full w-full font-large text-center text-slate-11 -mt-2 font-normal text-[1.25rem] mx-auto text-balance word-wrap break-words md:whitespace-pre",
        ),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-4 lg:pb-[7.875rem]"
        + rx.cond(
            HostingBannerState.show_banner,
            " lg:pt-[15.2rem] pt-[8rem]",
            " lg:pt-[13.2rem] pt-[6rem]",
        ),
    )
