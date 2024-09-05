import reflex as rx
from pcweb.components.icons.icons import get_icon


def create_pattern(
    pattern: str,
    class_name: str,
) -> rx.Component:
    return get_icon(
        pattern,
        class_name="z-0 absolute w-[1111.528px] h-[1094.945px] overflow-hidden pointer-events-none shrink-0"
        + " "
        + class_name,
    )


def landing_patterns() -> rx.Component:
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
            class_name="top-[715px] z-0 absolute bg-violet-3 opacity-[0.36] blur-[80px] rounded-[768px] w-[768px] h-[768px] overflow-hidden pointer-events-none shrink-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2"
        ),
    ]
