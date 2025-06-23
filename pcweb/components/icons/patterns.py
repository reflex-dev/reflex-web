import reflex as rx
from pcweb.components.icons.icons import get_icon
from pcweb.components.hosting_banner import HostingBannerState


def create_pattern(
    pattern: str,
    class_name: str,
) -> rx.Component:
    return get_icon(
        pattern,
        class_name="z-[-1] absolute w-[1111.528px] h-[1094.945px] overflow-hidden pointer-events-none shrink-0"
        + " "
        + class_name,
    )


def default_patterns() -> rx.Component:
    return [
        # Left
        create_pattern(
            "radial_small",
            class_name="top-0 mt-[-80px] mr-[725px] translate-y-0",
        ),
        create_pattern(
            "radial_big",
            class_name="top-0 mt-[90px] mr-[700px] translate-y-0 rotate-180 scale-x-[-1] scale-y-[-1]",
        ),
        # Right
        create_pattern(
            "radial_small",
            class_name="top-0 mt-[-80px] ml-[725px] scale-x-[-1]",
        ),
        create_pattern(
            "radial_big",
            class_name="top-0 mt-[90px] ml-[700px] scale-x-[-1]",
        ),
        # Glowing
        rx.box(
            class_name="top-[715px] z-[-1] absolute bg-violet-3 opacity-[0.36] blur-[80px] rounded-[768px] w-[768px] h-[768px] overflow-hidden pointer-events-none shrink-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2"
        ),
    ]


def index_patterns() -> rx.Component:
    return [
        rx.box(
            get_icon("wave_pattern", class_name=""),
            get_icon("wave_pattern", class_name="scale-x-[-1]"),
            class_name="flex flex-row gap-[4.125rem] absolute top-0 left-1/2 transform -translate-x-1/2 lg:mt-[65px] mt-[0px] z-[-1] w-[64.15rem] overflow-hidden opacity-70 lg:opacity-100",
        ),
        # Glowing
        rx.box(
            class_name="bg-[radial-gradient(50%_50%_at_50%_50%,_var(--glow)_0%,_rgba(21,_22,_24,_0.00)_100%)] w-[56.0625rem] h-[35.3125rem] rounded-[56.0625rem] overflow-hidden pointer-events-none shrink-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[-1] mt-[40rem] absolute top-0"
        ),
        # Glowing small
        rx.box(
            class_name="bg-[radial-gradient(50%_50%_at_50%_50%,_var(--glow)_0%,_rgba(21,_22,_24,_0.00)_100%)] w-[56.125rem] h-[11.625rem] rounded-[56.125rem] overflow-hidden pointer-events-none shrink-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[-1] mt-[65.75rem] absolute top-0"
        ),
    ]


def landing_patterns() -> rx.Component:
    return [
        rx.box(
            get_icon("wave_pattern", class_name=""),
            get_icon("wave_pattern", class_name="scale-x-[-1]"),
            class_name="flex flex-row gap-[4.125rem] absolute top-0 left-1/2 transform -translate-x-1/2 lg:mt-[65px] mt-[0px] z-[-1] w-[64.15rem] overflow-hidden opacity-70 lg:opacity-100",
        ),
        # Glowing small
        rx.box(
            class_name="bg-[radial-gradient(50%_50%_at_50%_50%,_var(--glow)_0%,_rgba(21,_22,_24,_0.00)_100%)] w-[56.125rem] h-[23.625rem] rounded-[56.125rem] overflow-hidden pointer-events-none shrink-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[-1] mt-[27.75rem] absolute top-0 block lg:hidden"
        ),
    ]


def hosting_patterns() -> rx.Component:
    return [
        rx.image(
            src=rx.color_mode_cond(
                light="/hosting/light/hosting_patterns.svg",
                dark="/hosting/dark/hosting_patterns.svg",
            ),
            alt="Reflex Hosting Patterns",
            class_name="desktop-only absolute top-0 z-[-1] w-[1028px] h-[478px] pointer-events-none shrink-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2"
            + rx.cond(
                HostingBannerState.show_banner,
                " lg:mt-[24rem] mt-[3.5rem]",
                " lg:mt-[19rem] mt-[8.5rem]",
            ),
        )
    ]
